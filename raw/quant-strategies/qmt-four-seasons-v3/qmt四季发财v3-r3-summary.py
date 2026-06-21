# 克隆自聚宽文章：https://www.joinquant.com/post/73227
# 标题：【精品】四季发财Q.M.T版-低拟合-稳健低波
# 作者：Ai夸我像真人

# 克隆自聚宽文章：https://www.joinquant.com/post/65759
# 标题：【策略改造】ETF轮动策略适应性改造
# 作者：屌丝逆袭量化

# 策略名称：ETF收益率稳定性轮动策略（带短期动量过滤和ATR动态止损）
# 策略作者：屌丝逆袭量化
# 优化时间：2026-1-3
# 优化内容：增加短期动量过滤功能，增加MA5/MA25过滤条件
# 新增内容：增加RSI指标过滤功能，增加MACD指标过滤功能
# 新增内容：增加成交量异常过滤功能
# 新增内容：增加布林带过滤功能
# 新增内容：增加基于ATR的动态止损功能

# 添加必要的导入
import numpy as np
import math
import pandas as pd
import json

STRATEGY_CODE = "qmt_four_seasons_v3"
STRATEGY_DISPLAY_NAME = "QMT四季发财v3"
STRATEGY_FILE = "qmt四季发财v3.py"
STRATEGY_VERSION = "v3-audit-log-20260619-r3-summary"
STRATEGY_ROLE = "community_strategy_audit_enhanced"
STRATEGY_DESCRIPTION = "ETF轮动策略：长期动量稳定性得分、短期动量过滤、RSI过滤、ATR动态止损和防御ETF切换。"
BENCHMARK_SECURITY = "513100.XSHG"
AUDIT_TOP_CANDIDATE_COUNT = 3
AUDIT_REJECT_SAMPLE_LIMIT = 8


def audit_clean(value):
    """Convert common numpy/pandas values into JSON-safe primitives."""
    if isinstance(value, dict):
        return {str(k): audit_clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [audit_clean(v) for v in value]
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        if np.isnan(value) or np.isinf(value):
            return None
        return float(value)
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, float):
        if np.isnan(value) or np.isinf(value):
            return None
        return value
    return value


def audit_log(context, payload):
    """Emit machine-readable audit logs without changing strategy behavior."""
    try:
        if 'event' not in payload:
            payload['event'] = 'unknown'
        if 'dt' not in payload:
            if context is not None and hasattr(context, 'current_dt'):
                payload['dt'] = str(context.current_dt)
            elif hasattr(g, 'audit_current_dt'):
                payload['dt'] = g.audit_current_dt
            else:
                payload['dt'] = None
        log.info('JQ_AUDIT|' + json.dumps(audit_clean(payload), ensure_ascii=True, sort_keys=True))
    except Exception as e:
        log.warn(f"JQ_AUDIT日志写入失败: {e}")


def get_position_amount(context, security):
    position = context.portfolio.positions.get(security, None)
    return position.total_amount if position else 0


def get_audit_benchmark_snapshot(context):
    benchmark_price = None
    try:
        current_data = get_current_data()
        if BENCHMARK_SECURITY in current_data:
            benchmark_price = current_data[BENCHMARK_SECURITY].last_price
    except Exception:
        benchmark_price = None

    if benchmark_price is None or benchmark_price <= 0:
        try:
            hist = attribute_history(BENCHMARK_SECURITY, 1, '1d', ['close'])
            if len(hist) > 0:
                benchmark_price = hist['close'][-1]
        except Exception:
            benchmark_price = None

    if benchmark_price is not None and benchmark_price > 0:
        if not hasattr(g, 'audit_benchmark_start_price') or g.audit_benchmark_start_price <= 0:
            g.audit_benchmark_start_price = benchmark_price
        if not hasattr(g, 'audit_benchmark_peak_price') or g.audit_benchmark_peak_price <= 0:
            g.audit_benchmark_peak_price = benchmark_price
        if benchmark_price > g.audit_benchmark_peak_price:
            g.audit_benchmark_peak_price = benchmark_price

    benchmark_return = None
    benchmark_drawdown = None
    if benchmark_price is not None and benchmark_price > 0:
        benchmark_return = benchmark_price / g.audit_benchmark_start_price - 1 if g.audit_benchmark_start_price else None
        benchmark_drawdown = benchmark_price / g.audit_benchmark_peak_price - 1 if g.audit_benchmark_peak_price else None

    return {
        'benchmark_security': BENCHMARK_SECURITY,
        'benchmark_price': benchmark_price,
        'benchmark_start_price': getattr(g, 'audit_benchmark_start_price', None),
        'benchmark_peak_price': getattr(g, 'audit_benchmark_peak_price', None),
        'benchmark_return': benchmark_return,
        'benchmark_drawdown_from_peak': benchmark_drawdown,
    }


def get_portfolio_audit_snapshot(context):
    positions = []
    position_value = 0.0
    for security in context.portfolio.positions:
        position = context.portfolio.positions[security]
        if position.total_amount <= 0:
            continue
        price = position.price
        value = position.total_amount * price
        position_value += value
        avg_cost = position.avg_cost
        positions.append({
            'security': security,
            'name': get_security_name(security),
            'amount': position.total_amount,
            'closeable_amount': getattr(position, 'closeable_amount', None),
            'avg_cost': avg_cost,
            'price': price,
            'value': value,
            'pnl_pct': price / avg_cost - 1 if avg_cost else None,
        })

    total_value = context.portfolio.total_value
    available_cash = context.portfolio.available_cash
    if not hasattr(g, 'audit_start_value') or g.audit_start_value <= 0:
        g.audit_start_value = total_value
    if not hasattr(g, 'audit_peak_value') or g.audit_peak_value <= 0:
        g.audit_peak_value = total_value
    if total_value > g.audit_peak_value:
        g.audit_peak_value = total_value

    benchmark_snapshot = get_audit_benchmark_snapshot(context)
    cumulative_return = total_value / g.audit_start_value - 1 if g.audit_start_value else None
    benchmark_return = benchmark_snapshot.get('benchmark_return')

    return {
        'total_value': total_value,
        'available_cash': available_cash,
        'position_value': position_value,
        'position_count': len(positions),
        'positions': positions,
        'exposure': position_value / total_value if total_value else 0,
        'cash_ratio': available_cash / total_value if total_value else 0,
        'cumulative_return': cumulative_return,
        'drawdown_from_peak': total_value / g.audit_peak_value - 1 if g.audit_peak_value else None,
        'benchmark': benchmark_snapshot,
        'excess_return_vs_benchmark': cumulative_return - benchmark_return if cumulative_return is not None and benchmark_return is not None else None,
        'audit_start_value': g.audit_start_value,
        'audit_peak_value': g.audit_peak_value,
    }


def audit_portfolio_state(context, event, extra=None):
    payload = get_portfolio_audit_snapshot(context)
    payload['event'] = event
    if extra:
        payload.update(extra)
    audit_log(context, payload)


def metric_audit_payload(metrics, rank=None):
    payload = {
        'security': metrics['etf'],
        'name': get_security_name(metrics['etf']),
        'annualized_returns': metrics['annualized_returns'],
        'r_squared': metrics['r_squared'],
        'score': metrics['score'],
        'current_price': metrics['current_price'],
        'short_return': metrics['short_return'],
        'ma_ratio': metrics['ma_ratio'],
        'rsi_filter_pass': metrics['rsi_filter_pass'],
        'current_rsi': metrics['current_rsi'],
        'max_recent_rsi': metrics['max_recent_rsi'],
        'macd_filter_pass': metrics['macd_filter_pass'],
        'macd_bar': metrics['macd_bar'],
        'volume_filter_pass': metrics['volume_filter_pass'],
        'volume_ratio': metrics['volume_ratio'],
        'bollinger_filter_pass': metrics['bollinger_filter_pass'],
    }
    if rank is not None:
        payload['rank'] = rank
    return payload


def reset_filter_summary():
    g.audit_filter_summary = {
        'universe_size': len(g.etf_pool),
        'metric_ok_count': 0,
        'accepted_count': 0,
        'rejected_count': 0,
        'rejected_by_filter': {},
        'accepted_samples': [],
        'rejected_samples': [],
    }


def audit_count_rejected(metrics, filter_name, reason):
    if not hasattr(g, 'audit_filter_summary'):
        reset_filter_summary()
    g.audit_filter_summary['rejected_count'] += 1
    current_count = g.audit_filter_summary['rejected_by_filter'].get(filter_name, 0)
    g.audit_filter_summary['rejected_by_filter'][filter_name] = current_count + 1
    if len(g.audit_filter_summary['rejected_samples']) < AUDIT_REJECT_SAMPLE_LIMIT:
        g.audit_filter_summary['rejected_samples'].append({
            'security': metrics['etf'],
            'score': metrics['score'],
            'short_return': metrics['short_return'],
            'filter': filter_name,
            'reason': reason,
        })


def audit_count_accepted(metrics):
    if not hasattr(g, 'audit_filter_summary'):
        reset_filter_summary()
    g.audit_filter_summary['accepted_count'] += 1
    if len(g.audit_filter_summary['accepted_samples']) < AUDIT_TOP_CANDIDATE_COUNT:
        g.audit_filter_summary['accepted_samples'].append({
            'security': metrics['etf'],
            'score': metrics['score'],
            'short_return': metrics['short_return'],
        })


# 初始化函数，设置策略参数
def initialize(context):
    # ==================== 实盘交易设置（参考策略1）====================
    set_option("avoid_future_data", True)  # 打开防未来函数
    set_option("use_real_price", True)     # 开启动态复权模式(真实价格)
    
    # 设置滑点
    set_slippage(FixedSlippage(0.0001), type="fund")
    set_slippage(FixedSlippage(0.003), type="stock")
    
    # 设置交易成本（ETF交易成本较低）
    set_order_cost(
        OrderCost(
            open_tax=0,               # 买入印花税
            close_tax=0,          # 卖出印花税:近股票收取
            open_commission=0.0002,   # 买入佣金
            close_commission=0.0002,  # 卖出佣金
            close_today_commission=0, # 今平佣金
            min_commission=5,         # 最低佣金
        ),
        type="fund",
    )
    
    # 设置货币ETF交易佣金为0
    set_order_cost(
        OrderCost(
            open_tax=0,
            close_tax=0,
            open_commission=0,
            close_commission=0,
            close_today_commission=0,
            min_commission=0,
        ),
        type="mmf",
    )
    
    # 设置日志级别
    log.set_level('order', 'error')
    log.set_level('system', 'error')
    
    log.info("策略2优化版初始化完成 - 包含完整实盘交易设置和短期动量过滤")
    #设置基准
    set_benchmark("513100.XSHG")  #组合中含纳斯达克，故设置纳斯达克为参考基准
    # ==================== 策略参数设置 ====================
    # 设置ETF池，包含A股、美股、商品等全球主要ETF
    g.etf_pool1 = [
        ##成立超过10年，规模超过10亿，只选宽基、外盘、商品
        #中国ETF
        "159915.XSHE",  # 创业板ETF：小盘代表
         #大宗商品ETF
        "518880.XSHG",  # 黄金ETF：商品资产代表
        #国际ETF
        "513100.XSHG",  # 纳指ETF：外盘代表
        #防御ETF
        "511220.XSHG",  # 防御性ETF：城投债ETF：债券代表
        ]
    #低相关ETF池
    g.etf_pool2 = [
         "513090.XSHG",  # - 香港证券 - 成交量: 3883058105
         "518880.XSHG",  # - 黄金ETF - 成交量: 546428739
         "159941.XSHE",  # - 纳指ETF - 成交量: 601033300
         "512710.XSHG",  # - 军工龙头 - 成交量: 938404037
         "512800.XSHG",  # - 银行ETF - 成交量: 1014007979
         "159980.XSHE",  # - 有色ETF大成 - 成交量: 379745360
         "159992.XSHE",  # - 创新药ETF - 成交量: 433275556
         "515220.XSHG",  # - 煤炭ETF - 成交量: 374748744
         "159981.XSHE",  # - 能源化工ETF - 成交量: 125399481
         "512980.XSHG",  # - 传媒ETF - 成交量: 97396162
         "159985.XSHE",  # - 豆粕ETF - 成交量: 76748697
         "511220.XSHG",  # - 城投ETF - 成交量: 71803300
         "511260.XSHG",  # - 十年国债 - 成交量: 34983880
         "511030.XSHG",  # - 公司债 - 成交量: 22464115
        ]
    
    # ETF轮动策略备选ETF池
    g.etf_pool = [
        #大宗商品ETF
        "518880.XSHG",  # 黄金ETF
        "159980.XSHE",  # 有色ETF（跟踪有色金属板块）
        "159985.XSHE",  # 豆粕ETF（跟踪豆粕期货价格）
        "501018.XSHG",  # 南方原油（投资原油相关资产）
        #国际ETF
        "513100.XSHG",  # 纳指ETF
        "513500.XSHG",  # 标普500ETF
        "513520.XSHG",  # 日经225ETF
        "513030.XSHG",  # 德国30ETF
        "513080.XSHG",  # 法国ETF
        #香港ETF
        "159920.XSHE",  # 恒生ETF
        #中国ETF
        "510300.XSHG",  # 沪深300ETF
        "510500.XSHG",  # 上证500ETF
        "510050.XSHG",  # 上证50ETF
        "510210.XSHG",  # 上证ETF
        "159915.XSHE",  # 创业板ETF
        "588080.XSHG",  # 科创50          
        "159995.XSHE",  # 芯片ETF             
        "513050.XSHG",  # 中概互联网             
        "159852.XSHE",  # 软件 
        "159845.XSHE",  # 华夏中证1000ETF
        "515030.XSHG",  # 华夏国证半导体ETF
        "159806.XSHE",  # 国泰中证新能源汽车ETF
        "516160.XSHG",  # 南方中证新能源ETF
        "159928.XSHE",  # 汇添富中证主要消费ETF
        #防御ETF
        "511010.XSHG",  # 防御性ETF（国债ETF
        "511880.XSHG",  # 防御性ETF（货币ETF
    ]
        # B方案：ETF池设置
    g.etf_pool3 = [  # ETF池列表
        '518880.XSHG',  # 黄金ETF
        '161226.XSHE',  # (白银JJ)
        '501018.XSHG',  # 南方原油etf
        '159985.XSHE',  # 豆粕etf
        '513520.XSHG',  # 日经ETF
        '513100.XSHG',  # 纳指100
        '513300.XSHG',  # (纳斯达克ETF)
        '513400.XSHG',  # (道琼斯)
        '159529.XSHE',  # (标普消费ETF)
        '513030.XSHG',  # (德国30)
        '159329.XSHE',  # (沙特ETF)
        '513020.XSHG',  # 港股科技etf
        '513130.XSHG',  # 恒生科技ETF
        '513090.XSHG',  # (香港证券etf)
        '513120.XSHG',  # (香港创新药)
        '159206.XSHE',  # (卫星ETF).
        '159218.XSHE',  # (卫星产业ETF)
        '159227.XSHE',  # (航天航空ETF)
        '159565.XSHE',  # (汽车零部件ETF)
        '562500.XSHG',  # (机器人)
        '159819.XSHE',  # (人工智能)
        '159363.XSHE',  # (创业板人工智能TFHB)
        '512480.XSHG',  # (半导体)
        '512760.XSHG',  # (存储芯片)
        '515880.XSHG',  # (通信ETF)
        '515050.XSHG',  # (5GETF)
        '159786.XSHE',  # (VRETF)
        '159890.XSHE',  # (云计算ETF)
        '516160.XSHG',  # (新能源)
        '515790.XSHG',  # (光伏ETF)
        '159755.XSHE',  # (电池ETF)
        '512660.XSHG',  # (军工ETF)
        '159732.XSHE',  # (消费电子)
        '159992.XSHE',  # (创新药XY)
        '159852.XSHE',  # (软件ETF)
        '159851.XSHE',  # (金融科技ETF)
        '159869.XSHE',  # (游戏ETF)
        '516780.XSHG',  # (稀土ETF)
        '159928.XSHE',  # (消费ETF)
        '512690.XSHG',  # (酒ETF)
        '515170.XSHG',  # (食品饮料ETF)
        '512010.XSHG',  # (医药ETF)
        '512980.XSHG',  # (传媒ETF)
        '159378.XSHE',  # (通用航空ETF)
        '159611.XSHE',  # (电力ETF)
        '159766.XSHE',  # (旅游ETF)
        '515220.XSHG',  # (煤炭ETF)
        '159865.XSHE',  # (养殖ETF)
        '562800.XSHG',  # (稀有金属)
        '510050.XSHG',  # 上证50etf
        '510300.XSHG',  # 沪深300etf
        '159922.XSHE',  # 中证500etf
        '159531.XSHE',  # 中证2000ETF
        '159915.XSHE',  # 创业板etf
        '588080.XSHG',  #(科创板50)
        '588380.XSHG',  # (双创50ETF)
        '160211.XSHE',  # 国泰小盘
        '512000.XSHG',  # 券商ETF
        '512800.XSHG',  # 银行ETF
        '510880.XSHG',  # 红利ETF
        '511090.XSHG',  # 30年国债ETF
    ]
        
    # 策略参数
    g.lookback_days = 25  # 长期动量计算周期
    g.holdings_num = 1    # 只持有1只ETF
    g.stop_loss = 0.95    # 止损线（0.92表示下跌8%止损）
    g.loss = 0.97   #近3日跌幅止损线：用于过滤
    g.defensive_etf = "511880.XSHG"  # 防御性ETF（货币ETF）
    g.min_score_threshold = 0.0  # 最低得分阈值，低于此值进入防御模式
    g.max_score_threshold = 5.0  # 最高得分阈值，高于此值的ETF视为异常值:过度上涨，下跌风险高
    g.min_money = 5000  # 最小交易金额
    
    # ==================== 新增短期动量过滤参数 ====================
    g.use_short_momentum_filter = True  # 是否启用短期动量过滤（新增参数）
    g.short_lookback_days = 10  # 短期动量计算周期（新增参数）
    g.short_momentum_threshold = 0.0  # 短期动量阈值（新增参数）
    
    # ==================== 新增ATR动态止损参数 ====================
    g.use_atr_stop_loss = True  # 是否启用ATR动态止损（新增参数）
    g.atr_period = 14  # ATR计算周期，默认14日（新增参数）
    g.atr_multiplier = 2  # ATR倍数，默认2倍（新增参数）
    g.atr_trailing_stop = False  # 是否使用跟踪止损（新增参数）
    g.atr_exclude_defensive = True  # 防御ETF是否豁免ATR止损（新增参数）

    
    # ==================== 新增MA过滤参数 ====================
    g.use_ma_filter = False  # 是否启用MA过滤（新增参数）
    g.ma_short_period = 5   # 短期MA周期，默认5日（新增参数）
    g.ma_long_period = 25   # 长期MA周期，默认25日（新增参数）
    g.ma_filter_condition = "above"  # MA过滤条件："above"表示MA5>MA25，"below"表示MA5<MA25（新增参数）
    
    # ==================== 新增RSI过滤参数 ====================
    g.use_rsi_filter = True  # 是否启用RSI过滤（新增参数）
    g.rsi_period = 6  # RSI计算周期（默认6日）
    g.rsi_lookback_days = 1  # 检查RSI的历史天数（默认5日）
    g.rsi_threshold = 95  # RSI阈值（默认90）
    
    # ==================== 新增MACD过滤参数 ====================
    g.use_macd_filter = False  # 是否启用MACD过滤（新增参数）
    g.macd_fast_period = 12  # MACD快线周期（默认12）
    g.macd_slow_period = 26  # MACD慢线周期（默认26）
    g.macd_signal_period = 9  # MACD信号线周期（默认9）
    g.macd_filter_condition = "bullish"  # MACD过滤条件："bullish"表示看多（DIF>DEA），"bearish"表示看空（DIF<DEA）
    
    # ==================== 新增成交量异常过滤参数 ====================
    g.use_volume_filter = False  # 是否启用成交量异常过滤（新增参数）
    g.volume_lookback_days = 7  # 成交量计算周期，默认10日（新增参数）
    g.volume_threshold = 2.0  # 成交量异常倍数，默认2倍（新增参数）
    g.volume_exclude_defensive = True  # 防御ETF是否豁免成交量过滤（新增参数）
    
    # ==================== 新增布林带过滤参数 ====================
    g.use_bollinger_filter = False  # 是否启用布林带过滤（新增参数）
    g.bollinger_period = 20  # 布林带周期，默认20日（新增参数）
    g.bollinger_std = 2.0  # 布林带标准差倍数，默认2.0（新增参数）
    g.bollinger_lookback_days = 3  # 检查布林带突破的天数，默认5日（新增参数）
    

    # 持仓管理（参考策略1的持仓管理方式）
    g.positions = {}  # 记录持仓
    # 新增：记录每个持仓的最高价和ATR止损价
    g.position_highs = {}  # 记录持仓期间的最高价
    g.position_stop_prices = {}  # 记录持仓的ATR止损价
    g.audit_start_value = context.portfolio.total_value
    g.audit_peak_value = context.portfolio.total_value
    g.audit_current_dt = str(context.current_dt)

    log.info(f"HUMAN|策略启动：{STRATEGY_DISPLAY_NAME}，ETF池数量={len(g.etf_pool)}，持仓数量={g.holdings_num}，调仓时间=14:29，防御ETF={g.defensive_etf}")
    audit_log(context, {
        'event': 'strategy_metadata',
        'strategy_code': STRATEGY_CODE,
        'strategy_name': STRATEGY_DISPLAY_NAME,
        'strategy_file': STRATEGY_FILE,
        'strategy_version': STRATEGY_VERSION,
        'strategy_role': STRATEGY_ROLE,
        'description': STRATEGY_DESCRIPTION,
        'benchmark': "513100.XSHG",
        'universe_size': len(g.etf_pool),
        'defensive_etf': g.defensive_etf,
        'holdings_num': g.holdings_num,
        'audit_log_policy': 'summary_only',
        'audit_top_candidate_count': AUDIT_TOP_CANDIDATE_COUNT,
        'audit_reject_sample_limit': AUDIT_REJECT_SAMPLE_LIMIT,
        'lookback_days': g.lookback_days,
        'short_lookback_days': g.short_lookback_days,
        'min_score_threshold': g.min_score_threshold,
        'max_score_threshold': g.max_score_threshold,
        'stop_loss': g.stop_loss,
        'loss_filter_threshold': g.loss,
        'min_money': g.min_money,
        'filters': {
            'short_momentum': g.use_short_momentum_filter,
            'ma': g.use_ma_filter,
            'rsi': g.use_rsi_filter,
            'macd': g.use_macd_filter,
            'volume': g.use_volume_filter,
            'bollinger': g.use_bollinger_filter,
            'atr_stop_loss': g.use_atr_stop_loss,
        },
        'filter_params': {
            'short_momentum_threshold': g.short_momentum_threshold,
            'ma_short_period': g.ma_short_period,
            'ma_long_period': g.ma_long_period,
            'ma_filter_condition': g.ma_filter_condition,
            'rsi_period': g.rsi_period,
            'rsi_lookback_days': g.rsi_lookback_days,
            'rsi_threshold': g.rsi_threshold,
            'macd_fast_period': g.macd_fast_period,
            'macd_slow_period': g.macd_slow_period,
            'macd_signal_period': g.macd_signal_period,
            'macd_filter_condition': g.macd_filter_condition,
            'volume_lookback_days': g.volume_lookback_days,
            'volume_threshold': g.volume_threshold,
            'bollinger_period': g.bollinger_period,
            'bollinger_std': g.bollinger_std,
            'bollinger_lookback_days': g.bollinger_lookback_days,
            'atr_period': g.atr_period,
            'atr_multiplier': g.atr_multiplier,
            'atr_trailing_stop': g.atr_trailing_stop,
            'atr_exclude_defensive': g.atr_exclude_defensive,
        },
        'etf_pool': g.etf_pool,
    })

    # ==================== 交易调度 ====================
    # 每天14:50执行ETF轮动交易
    run_daily(etf_trade, time='14:29')
    # 每天开盘后检查持仓（参考策略1）
    run_daily(check_positions, time='09:30')
    # 新增：每天开盘后检查ATR动态止损
    run_daily(check_atr_stop_loss, time='09:35')

# 计算ATR（平均真实波幅）指标
def calculate_atr(security, period=14):
    """
    计算ATR（平均真实波幅）指标
    :param security: 证券代码
    :param period: ATR计算周期
    :return: 当前ATR值，ATR序列，是否计算成功
    """
    try:
        # 获取历史数据，需要period+1天的数据来计算TR
        needed_days = period + 20  # 多取一些数据
        hist_data = attribute_history(security, needed_days, '1d', 
                                     ['high', 'low', 'close'])
        
        if len(hist_data) < period + 1:
            return 0, [], False, f"数据不足{period+1}天"
        
        # 计算真实波幅（TR）
        high_prices = hist_data['high'].values
        low_prices = hist_data['low'].values
        close_prices = hist_data['close'].values
        
        # 初始化TR数组
        tr_values = np.zeros(len(high_prices))
        
        # 计算每天的TR值
        for i in range(1, len(high_prices)):
            tr1 = high_prices[i] - low_prices[i]  # 当日最高价-最低价
            tr2 = abs(high_prices[i] - close_prices[i-1])  # 当日最高价-前日收盘价
            tr3 = abs(low_prices[i] - close_prices[i-1])   # 当日最低价-前日收盘价
            tr_values[i] = max(tr1, tr2, tr3)
        
        # 计算ATR（使用简单移动平均）
        atr_values = np.zeros(len(tr_values))
        
        # 前period个ATR值为0
        for i in range(period, len(tr_values)):
            atr_values[i] = np.mean(tr_values[i-period+1:i+1])
        
        # 获取最新的ATR值
        current_atr = atr_values[-1] if len(atr_values) > 0 else 0
        
        # 返回ATR序列（只返回有效部分）
        valid_atr = atr_values[period:] if len(atr_values) > period else atr_values
        
        return current_atr, valid_atr, True, "计算成功"
    
    except Exception as e:
        log.warn(f"计算{security} ATR时出错: {e}")
        return 0, [], False, f"计算出错:{str(e)}"

# 检查并执行ATR动态止损
def check_atr_stop_loss(context):
    """
    检查并执行ATR动态止损
    """
    g.audit_current_dt = str(context.current_dt)
    if not g.use_atr_stop_loss:
        audit_log(context, {
            'event': 'risk_check',
            'risk_type': 'atr_stop_loss',
            'enabled': False,
            'action': 'skip',
            'reason': 'atr_stop_loss_disabled',
        })
        return
    
    current_data = get_current_data()
    
    for security in list(context.portfolio.positions.keys()):
        # 只处理ETF池中的标的且当前有持仓
        if security not in g.etf_pool:
            continue
            
        position = context.portfolio.positions[security]
        if position.total_amount <= 0:
            continue
            
        # 防御ETF豁免检查
        if g.atr_exclude_defensive and security == g.defensive_etf:
            continue
        
        try:
            # 获取当前价格
            current_price = current_data[security].last_price
            if current_price == 0:
                continue
            
            # 获取成本价
            cost_price = position.avg_cost
            
            # 计算当前ATR值
            current_atr, atr_values, success, atr_info = calculate_atr(security, g.atr_period)
            
            if not success:
                log.info(f"⚠️ {security} {get_security_name(security)} ATR计算失败: {atr_info}")
                audit_log(context, {
                    'event': 'risk_check',
                    'risk_type': 'atr_stop_loss',
                    'security': security,
                    'name': get_security_name(security),
                    'action': 'skip',
                    'reason': 'atr_calculation_failed',
                    'atr_info': atr_info,
                })
                continue
            
            # 更新持仓期间的最高价
            if security not in g.position_highs:
                g.position_highs[security] = current_price
            else:
                g.position_highs[security] = max(g.position_highs[security], current_price)
            
            # 获取当前持仓期间的最高价
            position_high = g.position_highs[security]
            
            # 计算ATR止损价
            if g.atr_trailing_stop:
                # 跟踪止损：基于持仓期间最高价
                atr_stop_price = position_high - g.atr_multiplier * current_atr
            else:
                # 固定止损：基于成本价
                atr_stop_price = cost_price - g.atr_multiplier * current_atr
            
            # 记录止损价
            g.position_stop_prices[security] = atr_stop_price
            
            # 检查是否触发ATR止损
            if current_price <= atr_stop_price:
                # 触发ATR止损
                audit_log(context, {
                    'event': 'risk_event',
                    'risk_type': 'atr_stop_loss',
                    'security': security,
                    'name': get_security_name(security),
                    'current_price': current_price,
                    'cost_price': cost_price,
                    'position_high': position_high,
                    'current_atr': current_atr,
                    'atr_stop_price': atr_stop_price,
                    'atr_multiplier': g.atr_multiplier,
                    'atr_trailing_stop': g.atr_trailing_stop,
                    'position_before': position.total_amount,
                    'action': 'sell_to_zero',
                    'reason': 'current_price_below_atr_stop',
                })
                success = smart_order_target_value(security, 0, context)
                if success:
                    security_name = get_security_name(security)
                    loss_percent = (current_price/cost_price - 1) * 100
                    atr_stop_type = "跟踪" if g.atr_trailing_stop else "固定"
                    log.info(f"🚨 ATR动态止损({atr_stop_type})卖出: {security} {security_name}，成本: {cost_price:.3f}，现价: {current_price:.3f}，ATR: {current_atr:.3f}，止损价: {atr_stop_price:.3f}，亏损: {loss_percent:.2f}%")
                    
                    # 清除记录
                    if security in g.position_highs:
                        del g.position_highs[security]
                    if security in g.position_stop_prices:
                        del g.position_stop_prices[security]
        
        except Exception as e:
            log.warn(f"检查{security} ATR止损时出错: {e}")

# 计算布林带指标
def calculate_bollinger_bands(prices, period=20, std_dev=2.0):
    """
    计算布林带指标
    :param prices: 价格序列
    :param period: 布林带周期
    :param std_dev: 标准差倍数
    :return: 中轨、上轨、下轨
    """
    if len(prices) < period:
        return [], [], []
    
    # 初始化结果数组
    middle_band = np.zeros(len(prices))
    upper_band = np.zeros(len(prices))
    lower_band = np.zeros(len(prices))
    
    # 计算布林带
    for i in range(period - 1, len(prices)):
        # 取最近period天的数据
        window = prices[i-period+1:i+1]
        
        # 计算中轨（简单移动平均）
        middle = np.mean(window)
        
        # 计算标准差
        std = np.std(window)
        
        # 计算上轨和下轨
        upper = middle + std_dev * std
        lower = middle - std_dev * std
        
        middle_band[i] = middle
        upper_band[i] = upper
        lower_band[i] = lower
    
    # 只返回有效数据
    return middle_band[period-1:], upper_band[period-1:], lower_band[period-1:]

# 检查布林带过滤条件
def check_bollinger_filter(etf, current_price, lookback_days=5, period=20, std_dev=2.0):
    """
    检查布林带过滤条件
    :param etf: ETF代码
    :param current_price: 当前价格
    :param lookback_days: 检查突破的天数
    :param period: 布林带周期
    :param std_dev: 标准差倍数
    :return: 是否通过布林带过滤，详细信息
    """
    try:
        # 获取历史价格数据
        # 需要获取足够的天数来计算布林带和检查突破
        needed_days = max(period, lookback_days) + 10  # 多取一些数据
        price_data = attribute_history(etf, needed_days, '1d', ['close', 'high'])
        
        if len(price_data) < period:
            return True, f"数据不足{period}天，无法计算布林带"
        
        # 获取收盘价序列
        close_prices = price_data['close'].values
        
        # 计算布林带
        middle_band, upper_band, lower_band = calculate_bollinger_bands(
            close_prices, period, std_dev
        )
        
        if len(upper_band) < lookback_days:
            return True, f"布林带数据不足{lookback_days}天"
        
        # 检查近lookback_days日内是否曾经突破上轨
        # 取最近lookback_days天的布林带上轨和对应的收盘价
        recent_upper_band = upper_band[-lookback_days:]
        recent_close_prices = close_prices[-(len(middle_band)-len(upper_band)+lookback_days):][-lookback_days:]
        
        # 检查是否有任何一天收盘价突破上轨
        breakthrough_occurred = False
        breakthrough_day = None
        breakthrough_price = 0
        breakthrough_upper = 0
        
        for i in range(len(recent_close_prices)):
            if recent_close_prices[i] > recent_upper_band[i]:
                breakthrough_occurred = True
                breakthrough_day = i
                breakthrough_price = recent_close_prices[i]
                breakthrough_upper = recent_upper_band[i]
                break
        
        # 计算MA5（使用最近5天的收盘价）
        if len(close_prices) >= 5:
            ma5 = np.mean(close_prices[-5:])
        else:
            ma5 = np.mean(close_prices)
        
        # 判断是否满足过滤条件
        # 条件：近lookback_days日价格曾经突破布林带上轨，且当前价格低于MA5
        if breakthrough_occurred and current_price < ma5:
            return False, f"近{lookback_days}日曾突破布林带上轨(第{breakthrough_day+1}日:{breakthrough_price:.3f}>{breakthrough_upper:.3f})，且当前价{current_price:.3f}<MA5({ma5:.3f})"
        else:
            if breakthrough_occurred:
                return True, f"近{lookback_days}日曾突破布林带上轨(第{breakthrough_day+1}日:{breakthrough_price:.3f}>{breakthrough_upper:.3f})，但当前价{current_price:.3f}≥MA5({ma5:.3f})，未触发过滤"
            else:
                return True, f"近{lookback_days}日未突破布林带上轨，当前价{current_price:.3f}，MA5={ma5:.3f}"
    
    except Exception as e:
        log.warn(f"检查{etf}布林带时出错: {e}")
        return True, f"检查出错:{str(e)}"

# 计算成交量异常指标
def check_volume_anomaly(etf, lookback_days=10, threshold=2.0, exclude_defensive=False, defensive_etf=""):
    """
    检查成交量是否异常
    :param etf: ETF代码
    :param lookback_days: 成交量计算周期
    :param threshold: 成交量异常倍数
    :param exclude_defensive: 防御ETF是否豁免
    :param defensive_etf: 防御ETF代码
    :return: 是否通过成交量过滤，成交量比值，近1日成交量，近N日均成交量
    """
    # 防御ETF豁免检查
    if exclude_defensive and etf == defensive_etf:
        return True, 0.0, 0, 0, "防御ETF豁免成交量检查"
    
    try:
        # 获取历史成交量数据，需要足够的天数
        volume_lookback = lookback_days + 5  # 多取几天作为缓冲
        volume_data = attribute_history(etf, volume_lookback, '1d', ['volume'])
        
        if len(volume_data) < lookback_days:
            return True, 0.0, 0, 0, f"数据不足{lookback_days}天"
        
        # 获取近1日成交量
        recent_volume = volume_data['volume'].iloc[-1]
        
        # 获取近lookback_days日成交量均值（排除最近1日）
        if len(volume_data) >= lookback_days + 1:
            # 取前lookback_days日的成交量（排除最近1日）
            avg_volume = volume_data['volume'].iloc[-(lookback_days+1):-1].mean()
        else:
            # 数据不足时，使用所有可用数据（排除最近1日）
            avg_volume = volume_data['volume'].iloc[:-1].mean()
        
        # 避免除零错误
        if avg_volume <= 0:
            return True, 0.0, recent_volume, avg_volume, f"历史均量异常:{avg_volume:.0f}"
        
        # 计算成交量比值
        volume_ratio = recent_volume / avg_volume
        
        # 检查是否超过阈值
        if volume_ratio > threshold:
            return False, volume_ratio, recent_volume, avg_volume, f"成交量异常:近1日{recent_volume:.0f} > 近{lookback_days}日均值{avg_volume:.0f}的{threshold}倍"
        else:
            return True, volume_ratio, recent_volume, avg_volume, f"成交量正常:比值{volume_ratio:.2f}"
    
    except Exception as e:
        log.warn(f"检查{etf}成交量时出错: {e}")
        return True, 0.0, 0, 0, f"检查出错:{str(e)}"

# 计算RSI指标
def calculate_rsi(prices, period=6):
    """
    计算RSI指标
    :param prices: 价格序列
    :param period: RSI计算周期
    :return: RSI值列表
    """
    if len(prices) < period + 1:
        return []
    
    # 计算价格变化
    deltas = np.diff(prices)
    
    # 分离上涨和下跌
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    
    # 计算平均增益和平均损失（简单移动平均）
    avg_gains = np.zeros_like(prices)
    avg_losses = np.zeros_like(prices)
    
    # 初始化第一个平均值
    avg_gains[period] = np.mean(gains[:period])
    avg_losses[period] = np.mean(losses[:period])
    
    # 计算后续的RSI值
    rsi_values = np.zeros(len(prices))
    rsi_values[:period] = 50  # 初始值设为50
    
    for i in range(period + 1, len(prices)):
        avg_gains[i] = (avg_gains[i-1] * (period - 1) + gains[i-1]) / period
        avg_losses[i] = (avg_losses[i-1] * (period - 1) + losses[i-1]) / period
        
        if avg_losses[i] == 0:
            rsi_values[i] = 100
        else:
            rs = avg_gains[i] / avg_losses[i]
            rsi_values[i] = 100 - (100 / (1 + rs))
    
    return rsi_values[period:]

# 计算MACD指标
def calculate_macd(prices, fast_period=12, slow_period=26, signal_period=9):
    """
    计算MACD指标
    :param prices: 价格序列
    :param fast_period: 快线周期
    :param slow_period: 慢线周期
    :param signal_period: 信号线周期
    :return: MACD指标值 (DIF, DEA, MACD柱)
    """
    if len(prices) < slow_period + signal_period:
        return [], [], []
    
    # 计算EMA
    def calculate_ema(data, period):
        ema = np.zeros_like(data)
        ema[0] = data[0]
        alpha = 2 / (period + 1)
        
        for i in range(1, len(data)):
            ema[i] = alpha * data[i] + (1 - alpha) * ema[i-1]
        
        return ema
    
    # 计算快线EMA和慢线EMA
    ema_fast = calculate_ema(prices, fast_period)
    ema_slow = calculate_ema(prices, slow_period)
    
    # 计算DIF（差离值）
    dif = ema_fast - ema_slow
    
    # 计算DEA（DIF的EMA）
    dea = calculate_ema(dif, signal_period)
    
    # 计算MACD柱（DIF-DEA）
    macd_bar = dif - dea
    
    # 只返回有效数据（去掉前面不够计算的部分）
    start_idx = slow_period + signal_period - 1
    return dif[start_idx:], dea[start_idx:], macd_bar[start_idx:]

# 检查持仓状态
def check_positions(context):
    """每日开盘后检查持仓状态"""
    g.audit_current_dt = str(context.current_dt)
    current_data = get_current_data()
    for security in context.portfolio.positions:
        position = context.portfolio.positions[security]
        if position.total_amount > 0:
            security_name = get_security_name(security)
            log.info(f"📊 持仓检查: {security} {security_name}, 数量: {position.total_amount}, 成本: {position.avg_cost:.3f}, 当前价: {position.price:.3f}")
    audit_portfolio_state(context, 'daily_position_check', {
        'rule': '每日09:30检查当前持仓、现金、收益和回撤',
    })

# 计算ETF动量得分（添加短期动量和MA计算）
def calculate_momentum_metrics(etf):
    try:
        # 获取历史价格数据 - 使用attribute_history避免未来函数
        # 获取足够多的数据用于长期和短期动量计算
        lookback = max(g.lookback_days, g.short_lookback_days, g.ma_long_period, 
                      g.rsi_period + g.rsi_lookback_days, 
                      g.macd_slow_period + g.macd_signal_period,
                      g.volume_lookback_days,
                      g.bollinger_period + g.bollinger_lookback_days) + 20  # 加20天保证有足够数据
        prices = attribute_history(etf, lookback, '1d', ['close', 'high'])
        current_data = get_current_data()
        
        # 检查数据是否足够
        if len(prices) < lookback:
            return None
            
        # 策略1的关键：获取当前价格并添加到价格序列中
        current_price = current_data[etf].last_price
        price_series = np.append(prices["close"].values, current_price)
        
        # ========== 新增：计算MA指标 ==========
        if len(price_series) >= g.ma_long_period:
            # 计算MA5和MA25
            ma5 = np.mean(price_series[-g.ma_short_period:])
            ma25 = np.mean(price_series[-g.ma_long_period:])
            
            # 判断MA过滤条件是否满足
            if g.ma_filter_condition == "above":
                ma_condition_met = ma5 >= ma25
                condition_desc = f"MA{g.ma_short_period}>={g.ma_long_period}"
            else:
                ma_condition_met = ma5 <= ma25
                condition_desc = f"MA{g.ma_short_period}<={g.ma_long_period}"
            
            ma_ratio = ma5 / ma25 - 1  # MA相对比值
        else:
            ma5 = 0
            ma25 = 0
            ma_condition_met = True  # 数据不足时默认满足条件
            ma_ratio = 0
            condition_desc = "数据不足"
        # =====================================
        
        # ========== 新增：计算RSI指标并检查过滤条件 ==========
        rsi_filter_pass = True  # 默认通过RSI过滤
        
        if g.use_rsi_filter and len(price_series) >= g.rsi_period + g.rsi_lookback_days:
            # 计算RSI指标
            rsi_values = calculate_rsi(price_series, g.rsi_period)
            
            if len(rsi_values) >= g.rsi_lookback_days:
                # 获取最近g.rsi_lookback_days日的RSI值
                recent_rsi = rsi_values[-g.rsi_lookback_days:]
                
                # 检查是否曾经超过阈值
                rsi_ever_above_threshold = np.any(recent_rsi > g.rsi_threshold)
                
                # 检查当前价格是否在MA5之下
                #current_below_ma5 = current_price < ma5 if ma5 > 0 else False
                current_below_ma5 = True
                # 如果近N日RSI曾经大于阈值且当前价格在MA5之下，则过滤掉
                if rsi_ever_above_threshold and current_below_ma5:
                    rsi_filter_pass = False
                    
                    # 获取最大RSI值和当前RSI值
                    max_rsi = np.max(recent_rsi)
                    current_rsi = recent_rsi[-1] if len(recent_rsi) > 0 else 0
                    rsi_info = f"RSI过滤(max={max_rsi:.1f}, current={current_rsi:.1f})"
                else:
                    # 记录RSI信息但不过滤
                    max_rsi = np.max(recent_rsi) if len(recent_rsi) > 0 else 0
                    current_rsi = recent_rsi[-1] if len(recent_rsi) > 0 else 0
                    rsi_info = f"RSI(max={max_rsi:.1f}, current={current_rsi:.1f})"
            else:
                rsi_info = "RSI数据不足"
                current_rsi = 0
                max_rsi = 0
        else:
            rsi_info = "未启用RSI过滤或数据不足"
            current_rsi = 0
            max_rsi = 0
        # ===================================================
        
        # ========== 新增：计算MACD指标并检查过滤条件 ==========
        macd_filter_pass = True  # 默认通过MACD过滤
        dif_value = 0
        dea_value = 0
        macd_bar = 0
        macd_info = "未启用MACD过滤或数据不足"
        
        if g.use_macd_filter and len(price_series) >= g.macd_slow_period + g.macd_signal_period:
            # 计算MACD指标
            dif_values, dea_values, macd_bars = calculate_macd(
                price_series, 
                g.macd_fast_period, 
                g.macd_slow_period, 
                g.macd_signal_period
            )
            
            if len(dif_values) > 0:
                # 获取最新的MACD值
                dif_value = dif_values[-1] if len(dif_values) > 0 else 0
                dea_value = dea_values[-1] if len(dea_values) > 0 else 0
                macd_bar = macd_bars[-1] if len(macd_bars) > 0 else 0
                
                # 判断MACD过滤条件是否满足
                if g.macd_filter_condition == "bullish":
                    # 看多条件：DIF > DEA（金叉或保持多头）
                    macd_condition_met = dif_value > dea_value
                    condition_desc = f"DIF({dif_value:.4f})>DEA({dea_value:.4f})"
                else:
                    # 看空条件：DIF < DEA（死叉或保持空头）
                    macd_condition_met = dif_value < dea_value
                    condition_desc = f"DIF({dif_value:.4f})<DEA({dea_value:.4f})"
                
                macd_filter_pass = macd_condition_met
                macd_info = f"MACD(DIF={dif_value:.4f}, DEA={dea_value:.4f}, BAR={macd_bar:.4f})"
                
                if not macd_filter_pass:
                    pass
            else:
                macd_info = "MACD数据不足"
        # ===================================================
        
        # ========== 新增：检查成交量异常 ==========
        volume_filter_pass = True  # 默认通过成交量过滤
        volume_ratio = 0
        recent_volume = 0
        avg_volume = 0
        volume_info = "未启用成交量过滤"
        
        if g.use_volume_filter:
            volume_filter_pass, volume_ratio, recent_volume, avg_volume, volume_info = check_volume_anomaly(
                etf, 
                g.volume_lookback_days, 
                g.volume_threshold,
                g.volume_exclude_defensive,
                g.defensive_etf
            )
            
        # =====================================
        
        # ========== 新增：检查布林带过滤条件 ==========
        bollinger_filter_pass = True  # 默认通过布林带过滤
        bollinger_info = "未启用布林带过滤"
        
        if g.use_bollinger_filter:
            bollinger_filter_pass, bollinger_info = check_bollinger_filter(
                etf,
                current_price,
                g.bollinger_lookback_days,
                g.bollinger_period,
                g.bollinger_std
            )
            
        # ============================================
        
        # ========== 计算短期动量 ==========
        short_current_price = None
        short_10d_ago_price = None
        if len(price_series) >= g.short_lookback_days + 1:
            short_current_price = price_series[-1]
            short_10d_ago_price = price_series[-(g.short_lookback_days + 1)]
            # 计算短期动量：近N天的收益率
            short_return = short_current_price / short_10d_ago_price - 1
            # 转换为年化收益率
            short_annualized = (1 + short_return) ** (250 / g.short_lookback_days) - 1
        else:
            short_return = 0
            short_annualized = 0
        # =====================================

        # 使用策略1的线性权重计算方式计算长期动量
        # 使用最后g.lookback_days+1天的数据（包括当前价格）
        recent_price_series = price_series[-(g.lookback_days + 1):]
        y = np.log(recent_price_series)
        x = np.arange(len(y))
        weights = np.linspace(1, 2, len(y))  # 线性权重1-2，近期权重更高

        # 计算年化收益率（完全复制策略1）
        slope, intercept = np.polyfit(x, y, 1, w=weights)
        annualized_returns = math.exp(slope * 250) - 1  # 年化处理

        # 计算R²（拟合优度，值越高趋势越稳定）- 使用加权计算（策略1方式）
        ss_res = np.sum(weights * (y - (slope * x + intercept)) ** 2)
        ss_tot = np.sum(weights * (y - np.mean(y)) ** 2)
        r_squared = 1 - ss_res / ss_tot if ss_tot else 0

        # 综合得分 = 年化收益率 * 趋势稳定性（策略1的核心公式）
        score = annualized_returns * r_squared

        # 策略1的短期风控：过滤近3日跌幅超过N%的ETF
        if len(price_series) >= 4:
            # 检查最近3个交易日的连续表现（策略1的严格风控）
            day1_ratio = price_series[-1] / price_series[-2]  # 今日/昨日
            day2_ratio = price_series[-2] / price_series[-3]  # 昨日/前日  
            day3_ratio = price_series[-3] / price_series[-4]  # 前日/大前日
            
            # 如果任意一日跌幅超过N%，排除该ETF（策略1的逻辑）
            if min(day1_ratio, day2_ratio, day3_ratio) < g.loss:
                score = 0  # 设为0分，不会被选中

        return {
            'etf': etf,
            'annualized_returns': annualized_returns,
            'r_squared': r_squared,
            'score': score,
            'slope': slope,
            'current_price': current_price,
            'short_return': short_return,
            'short_annualized': short_annualized,
            'short_momentum_pass': short_return >= g.short_momentum_threshold,
            'short_current_price': short_current_price,    # 新增
            'short_10d_ago_price': short_10d_ago_price,    # 新增
            'ma5': ma5,
            'ma25': ma25,
            'ma_condition_met': ma_condition_met,
            'ma_ratio': ma_ratio,
            'ma_condition_desc': condition_desc,
            'rsi_filter_pass': rsi_filter_pass,
            'current_rsi': current_rsi,
            'max_recent_rsi': max_rsi,
            'rsi_info': rsi_info,
            'macd_filter_pass': macd_filter_pass,
            'dif': dif_value,
            'dea': dea_value,
            'macd_bar': macd_bar,
            'macd_info': macd_info,
            'volume_filter_pass': volume_filter_pass,
            'volume_ratio': volume_ratio,
            'recent_volume': recent_volume,
            'avg_volume': avg_volume,
            'volume_info': volume_info,
            'bollinger_filter_pass': bollinger_filter_pass,
            'bollinger_info': bollinger_info
        }
    except Exception as e:
        log.warn(f"计算{etf}动量指标时出错: {e}")
        return None

# 获取ETF排名（添加短期动量和MA过滤）
def get_ranked_etfs():
    reset_filter_summary()
    etf_metrics = []
    for etf in g.etf_pool:
        metrics = calculate_momentum_metrics(etf)
        if metrics is not None:
            g.audit_filter_summary['metric_ok_count'] += 1
            # 应用短期动量过滤（如果启用）
            if g.use_short_momentum_filter and not metrics['short_momentum_pass']:
                audit_count_rejected(metrics, 'short_momentum', 'short_return_below_threshold')
                continue
            
            # 应用MA过滤（如果启用）
            if g.use_ma_filter and not metrics['ma_condition_met']:
                audit_count_rejected(metrics, 'ma', 'ma_condition_not_met')
                continue
            
            # 应用RSI过滤（如果启用）
            if g.use_rsi_filter and not metrics['rsi_filter_pass']:
                audit_count_rejected(metrics, 'rsi', 'recent_rsi_above_threshold')
                continue
            
            # 应用MACD过滤（如果启用）
            if g.use_macd_filter and not metrics['macd_filter_pass']:
                audit_count_rejected(metrics, 'macd', 'macd_condition_not_met')
                continue
            
            # 应用成交量过滤（如果启用）
            if g.use_volume_filter and not metrics['volume_filter_pass']:
                audit_count_rejected(metrics, 'volume', 'volume_anomaly')
                continue
            
            # 应用布林带过滤（如果启用）
            if g.use_bollinger_filter and not metrics['bollinger_filter_pass']:
                audit_count_rejected(metrics, 'bollinger', 'bollinger_breakthrough_and_price_below_ma5')
                continue
            
            # 过滤掉得分异常的ETF（得分过高可能是数据异常）
            if 0 < metrics['score'] < g.max_score_threshold:
                etf_metrics.append(metrics)
                audit_count_accepted(metrics)
            else:
                audit_count_rejected(metrics, 'score_range', 'score_out_of_allowed_range')
    
    # 按得分降序排序
    etf_metrics.sort(key=lambda x: x['score'], reverse=True)
    return etf_metrics

# 获取基金名称
def get_security_name(security):
    """获取证券名称"""
    current_data = get_current_data()
    return current_data[security].name if security in current_data else security

# 自定义下单函数（完善交易执行控制，参考策略1的交易逻辑）
def smart_order_target_value(security, target_value, context):
    """
    智能下单函数，检查交易条件并执行下单
    参考策略1的交易控制逻辑
    """
    current_data = get_current_data()
    security_name = get_security_name(security)
    current_position = context.portfolio.positions.get(security, None)
    current_amount = current_position.total_amount if current_position else 0
    
    # 检查标的是否停牌
    if current_data[security].paused:
        log.info(f"{security} {security_name}: 今日停牌，跳过交易")
        audit_log(context, {
            'event': 'order_decision',
            'security': security,
            'name': security_name,
            'target_value': target_value,
            'position_before': current_amount,
            'action': 'skip_order',
            'order_sent': False,
            'reason': 'paused',
            'rule': '停牌标的不交易',
        })
        return False

    # 检查涨停（策略1的涨停检查）
    if current_data[security].last_price >= current_data[security].high_limit:
        log.info(f"{security} {security_name}: 当前涨停，跳过买入")
        audit_log(context, {
            'event': 'order_decision',
            'security': security,
            'name': security_name,
            'target_value': target_value,
            'position_before': current_amount,
            'current_price': current_data[security].last_price,
            'high_limit': current_data[security].high_limit,
            'action': 'skip_order',
            'order_sent': False,
            'reason': 'high_limit',
            'rule': '涨停时跳过交易',
        })
        return False

    # 检查跌停（策略1的跌停检查）
    if current_data[security].last_price <= current_data[security].low_limit:
        log.info(f"{security} {security_name}: 当前跌停，跳过卖出")
        audit_log(context, {
            'event': 'order_decision',
            'security': security,
            'name': security_name,
            'target_value': target_value,
            'position_before': current_amount,
            'current_price': current_data[security].last_price,
            'low_limit': current_data[security].low_limit,
            'action': 'skip_order',
            'order_sent': False,
            'reason': 'low_limit',
            'rule': '跌停时跳过交易',
        })
        return False

    # 获取当前价格
    current_price = current_data[security].last_price
    if current_price == 0:
        log.info(f"{security} {security_name}: 当前价格为0，跳过交易")
        audit_log(context, {
            'event': 'order_decision',
            'security': security,
            'name': security_name,
            'target_value': target_value,
            'position_before': current_amount,
            'current_price': current_price,
            'action': 'skip_order',
            'order_sent': False,
            'reason': 'zero_price',
            'rule': '当前价格为0不交易',
        })
        return False

    # 计算目标数量
    target_amount = int(target_value / current_price)
    
    # 对于ETF，按100股整数倍调整（实盘交易要求）
    target_amount = (target_amount // 100) * 100
    if target_amount <= 0 and target_value > 0:
        target_amount = 100  # 至少买100股
    
    # 计算需要调整的数量
    amount_diff = target_amount - current_amount
    
    # 检查最小交易金额
    trade_value = abs(amount_diff) * current_price
    if 0 < trade_value < g.min_money:
        log.info(f"{security} {security_name}: 交易金额{trade_value:.2f}小于最小交易额{g.min_money}，跳过交易")
        audit_log(context, {
            'event': 'order_decision',
            'security': security,
            'name': security_name,
            'target_value': target_value,
            'target_amount': target_amount,
            'position_before': current_amount,
            'amount_diff': amount_diff,
            'current_price': current_price,
            'trade_value': trade_value,
            'min_money': g.min_money,
            'action': 'skip_order',
            'order_sent': False,
            'reason': 'trade_value_below_min_money',
            'rule': '交易金额低于最小交易金额时跳过',
        })
        return False

    # 检查T+1限制（策略1的关键风控）
    if amount_diff < 0:  # 卖出操作
        closeable_amount = current_position.closeable_amount if current_position else 0
        if closeable_amount == 0:
            log.info(f"{security} {security_name}: 当天买入不可卖出(T+1)")
            audit_log(context, {
                'event': 'order_decision',
                'security': security,
                'name': security_name,
                'target_value': target_value,
                'target_amount': target_amount,
                'position_before': current_amount,
                'amount_diff': amount_diff,
                'current_price': current_price,
                'closeable_amount': closeable_amount,
                'action': 'skip_order',
                'order_sent': False,
                'reason': 't_plus_1_not_closeable',
                'rule': 'T+1可卖数量为0时跳过卖出',
            })
            return False
        # 确保卖出数量不超过可卖数量
        amount_diff = -min(abs(amount_diff), closeable_amount)

    # 执行下单
    if amount_diff != 0:
        audit_log(context, {
            'event': 'order_decision',
            'security': security,
            'name': security_name,
            'target_value': target_value,
            'target_amount': target_amount,
            'position_before': current_amount,
            'amount_diff': amount_diff,
            'current_price': current_price,
            'trade_value': abs(amount_diff) * current_price,
            'action': 'send_order',
            'order_sent': True,
            'reason': 'target_amount_diff_nonzero',
            'rule': '按目标金额换算为100股整数倍后下单',
        })
        # 使用order函数下单，让聚宽处理具体交易细节
        order_result = order(security, amount_diff)
        if order_result:
            # 更新持仓记录（参考策略1的持仓管理）
            if security not in g.positions:
                g.positions[security] = 0
            g.positions[security] = target_amount
            
            # 新增：如果买入操作，初始化最高价记录和ATR止损价
            if amount_diff > 0 and security in g.etf_pool:
                g.position_highs[security] = current_price
                
                # 计算ATR止损价
                if g.use_atr_stop_loss and not (g.atr_exclude_defensive and security == g.defensive_etf):
                    current_atr, _, success, _ = calculate_atr(security, g.atr_period)
                    if success:
                        if g.atr_trailing_stop:
                            g.position_stop_prices[security] = current_price - g.atr_multiplier * current_atr
                        else:
                            g.position_stop_prices[security] = current_price - g.atr_multiplier * current_atr
            
            if amount_diff > 0:
                log.info(f"📥 买入 {security} {security_name}，数量: {amount_diff}，价格: {current_price:.3f}，金额: {trade_value:.2f}")
            else:
                log.info(f"📤 卖出 {security} {security_name}，数量: {abs(amount_diff)}，价格: {current_price:.3f}，金额: {trade_value:.2f}")
            audit_log(context, {
                'event': 'order_result',
                'security': security,
                'name': security_name,
                'target_value': target_value,
                'target_amount': target_amount,
                'position_before': current_amount,
                'amount_diff': amount_diff,
                'current_price': current_price,
                'trade_value': trade_value,
                'action': 'buy' if amount_diff > 0 else 'sell',
                'order_sent': True,
                'order_success': True,
                'reason': 'order_returned_truthy',
                'position_record_after': g.positions.get(security, None),
                'atr_stop_price': g.position_stop_prices.get(security, None),
                'portfolio_total_value_after_order': context.portfolio.total_value,
                'available_cash_after_order': context.portfolio.available_cash,
                'position_after': get_position_amount(context, security),
            })
            return True
        else:
            log.warn(f"下单失败: {security} {security_name}，数量: {amount_diff}")
            audit_log(context, {
                'event': 'order_result',
                'security': security,
                'name': security_name,
                'target_value': target_value,
                'target_amount': target_amount,
                'position_before': current_amount,
                'amount_diff': amount_diff,
                'current_price': current_price,
                'trade_value': trade_value,
                'action': 'order_failed',
                'order_sent': True,
                'order_success': False,
                'reason': 'order_returned_false',
                'portfolio_total_value_after_order': context.portfolio.total_value,
                'available_cash_after_order': context.portfolio.available_cash,
                'position_after': get_position_amount(context, security),
            })
            return False
    
    audit_log(context, {
        'event': 'order_decision',
        'security': security,
        'name': security_name,
        'target_value': target_value,
        'target_amount': target_amount,
        'position_before': current_amount,
        'amount_diff': amount_diff,
        'current_price': current_price,
        'action': 'skip_order',
        'order_sent': False,
        'reason': 'already_at_target_amount',
        'rule': '目标股数与当前持仓一致时不下单',
    })
    return False

# 检查防御性ETF是否可交易
def is_defensive_etf_available():
    """检查黄金ETF是否可交易"""
    current_data = get_current_data()
    defensive_etf = g.defensive_etf
    
    if defensive_etf not in g.etf_pool:
        return False
        
    if current_data[defensive_etf].paused:
        log.info(f"防御性ETF {defensive_etf} {get_security_name(defensive_etf)} 今日停牌")
        return False
        
    if current_data[defensive_etf].last_price >= current_data[defensive_etf].high_limit:
        log.info(f"防御性ETF {defensive_etf} {get_security_name(defensive_etf)} 当前涨停")
        return False
        
    if current_data[defensive_etf].last_price <= current_data[defensive_etf].low_limit:
        log.info(f"防御性ETF {defensive_etf} {get_security_name(defensive_etf)} 当前跌停")
        return False
        
    return True

# ETF轮动交易主函数
def etf_trade(context):
    g.audit_current_dt = str(context.current_dt)

    # 获取ETF排名和指标（已过滤异常值）
    ranked_etfs = get_ranked_etfs()
    audit_log(context, {
        'event': 'rebalance_universe_summary',
        'universe_size': len(g.etf_pool),
        'ranked_count': len(ranked_etfs),
        'filter_summary': getattr(g, 'audit_filter_summary', None),
        'top_candidates': [metric_audit_payload(m, rank=i + 1) for i, m in enumerate(ranked_etfs[:AUDIT_TOP_CANDIDATE_COUNT])],
        'rule': 'summary_only：候选ETF经过动量、过滤器和异常得分过滤后按score降序排序，只记录过滤摘要和前几名候选',
    })
    
    log.info(f"HUMAN|候选摘要：通过数={len(ranked_etfs)}，过滤摘要={getattr(g, 'audit_filter_summary', {}).get('rejected_by_filter', {})}")
    for metrics in ranked_etfs[:AUDIT_TOP_CANDIDATE_COUNT]:
        etf_name = get_security_name(metrics['etf'])
        # 构造短期动量显示文本（带计算过程）
        if metrics['short_current_price'] is not None and metrics['short_10d_ago_price'] is not None:
            short_info = f"{metrics['short_return']:.4f}({metrics['short_current_price']:.3f}/{metrics['short_10d_ago_price']:.3f}-1)"
        else:
            short_info = f"{metrics['short_return']:.4f}"
        bollinger_status = metrics['bollinger_info'] if g.use_bollinger_filter else "未启用"
        log.info(f"HUMAN|候选TOP: {metrics['etf']} {etf_name}, 得分={metrics['score']:.4f}, 年化={metrics['annualized_returns']:.4f}, R²={metrics['r_squared']:.4f}, 短期动量={short_info}, RSI={metrics['current_rsi']:.1f}, 当前价={metrics['current_price']:.3f}")
    
    # 如果没有通过过滤条件的ETF，记录日志
    filter_conditions = []
    if g.use_short_momentum_filter:
        filter_conditions.append(f"短期动量<{g.short_momentum_threshold}")
    if g.use_ma_filter:
        if g.ma_filter_condition == "above":
            ma_desc = f"MA{g.ma_short_period}<MA{g.ma_long_period}"
        else:
            ma_desc = f"MA{g.ma_short_period}>MA{g.ma_long_period}"
        filter_conditions.append(ma_desc)
    if g.use_rsi_filter:
        filter_conditions.append(f"RSI过滤(近{g.rsi_lookback_days}日曾>{g.rsi_threshold}且现价<MA5)")
    if g.use_macd_filter:
        if g.macd_filter_condition == "bullish":
            macd_desc = f"MACD不满足看多条件(DIF>DEA)"
        else:
            macd_desc = f"MACD不满足看空条件(DIF<DEA)"
        filter_conditions.append(macd_desc)
    if g.use_volume_filter:
        filter_conditions.append(f"成交量>近{g.volume_lookback_days}日均{g.volume_threshold}倍")
    if g.use_bollinger_filter:
        filter_conditions.append(f"布林带过滤(近{g.bollinger_lookback_days}日曾突破上轨且现价<MA5)")
    
    if (g.use_short_momentum_filter or g.use_ma_filter or g.use_rsi_filter or g.use_macd_filter or g.use_volume_filter or g.use_bollinger_filter) and not ranked_etfs:
        log.info(f"📊 所有ETF均未通过过滤条件({', '.join(filter_conditions)})，将进入防御模式或空仓")

    # 确定目标ETF - 只选择得分最高的一只
    target_etf = None
    selection_mode = None
    selection_reason = None
    top_metrics = None
    if ranked_etfs and ranked_etfs[0]['score'] >= g.min_score_threshold:
        # 正常模式：选择得分最高的一只ETF
        target_etf = ranked_etfs[0]['etf']
        top_metrics = ranked_etfs[0]
        selection_mode = 'normal'
        selection_reason = 'top_score_above_min_score_threshold'
        etf_name = get_security_name(target_etf)
        # 最终选择日志也显示短期动量计算过程
        if top_metrics['short_current_price'] is not None and top_metrics['short_10d_ago_price'] is not None:
            short_info = f"{top_metrics['short_return']:.4f}({top_metrics['short_current_price']:.3f}/{top_metrics['short_10d_ago_price']:.3f}-1)"
        else:
            short_info = f"{top_metrics['short_return']:.4f}"
        log.info(f"🎯 正常模式，选择得分最高的ETF: {target_etf} {etf_name}，得分: {top_metrics['score']:.4f}，短期动量: {short_info}，MA比率: {top_metrics['ma_ratio']:.4f}，成交量比: {top_metrics['volume_ratio']:.2f}，RSI: {top_metrics['current_rsi']:.1f}，MACD柱: {top_metrics['macd_bar']:.4f}，布林带: {top_metrics['bollinger_info']}")
    else:
        # 防御模式：检查是否可买入防御ETF
        # 注意：防御性ETF可以豁免过滤条件，因为它是在市场不好时的避险选择
        if is_defensive_etf_available():
            target_etf = g.defensive_etf
            selection_mode = 'defensive'
            selection_reason = 'no_candidate_above_min_score_or_no_ranked_candidate'
            etf_name = get_security_name(target_etf)
            log.info(f"🛡️ 进入防御模式，选择防御ETF: {target_etf} {etf_name}")
        else:
            selection_mode = 'cash'
            selection_reason = 'defensive_etf_unavailable'
            log.info("💤 进入空仓模式，所有ETF得分均不达标且防御ETF不可用")

    audit_log(context, {
        'event': 'target_selection',
        'mode': selection_mode,
        'target': target_etf,
        'target_name': get_security_name(target_etf) if target_etf else None,
        'reason': selection_reason,
        'min_score_threshold': g.min_score_threshold,
        'top_candidate': metric_audit_payload(top_metrics, rank=1) if top_metrics else None,
        'ranked_count': len(ranked_etfs),
        'rule': '若最高score达到阈值则持有第一名，否则尝试防御ETF，否则空仓',
    })
    
    target_etfs = [target_etf] if target_etf else []
    
    # 检查并执行固定百分比止损
    for security in list(context.portfolio.positions.keys()):
        position = context.portfolio.positions[security]
        # 确保只处理ETF池中的标的且当前有持仓
        if security in g.etf_pool and position.total_amount > 0:
            current_price = position.price
            cost_price = position.avg_cost
            # 止损检查
            if current_price <= cost_price * g.stop_loss:
                # 使用智能下单函数执行止损
                audit_log(context, {
                    'event': 'risk_event',
                    'risk_type': 'fixed_stop_loss',
                    'security': security,
                    'name': get_security_name(security),
                    'current_price': current_price,
                    'cost_price': cost_price,
                    'stop_loss': g.stop_loss,
                    'stop_price': cost_price * g.stop_loss,
                    'position_before': position.total_amount,
                    'action': 'sell_to_zero',
                    'reason': 'current_price_below_fixed_stop_price',
                    'rule': '当前价 <= 成本价 * 固定止损线时清仓',
                })
                success = smart_order_target_value(security, 0, context)
                if success:
                    security_name = get_security_name(security)
                    loss_percent = (current_price/cost_price-1)*100
                    log.info(f"🚨 固定百分比止损卖出: {security} {security_name}，成本: {cost_price:.3f}，现价: {current_price:.3f}，亏损: {loss_percent:.2f}%")
                    
                    # 清除记录
                    if security in g.position_highs:
                        del g.position_highs[security]
                    if security in g.position_stop_prices:
                        del g.position_stop_prices[security]

    # 计算目标持仓金额
    total_value = context.portfolio.total_value
    target_value = total_value if target_etfs else 0
    audit_log(context, {
        'event': 'rebalance_plan',
        'target_etfs': target_etfs,
        'target_value_each': target_value,
        'total_value': total_value,
        'current_positions': [
            {
                'security': security,
                'name': get_security_name(security),
                'amount': context.portfolio.positions[security].total_amount,
                'price': context.portfolio.positions[security].price,
                'value': context.portfolio.positions[security].total_amount * context.portfolio.positions[security].price,
            }
            for security in context.portfolio.positions
            if context.portfolio.positions[security].total_amount > 0
        ],
        'rule': '只持有目标ETF；若无目标ETF则目标仓位为0',
    })
    
    # 调仓逻辑
    current_positions = set(context.portfolio.positions.keys())
    target_etfs_set = set(target_etfs)
    
    # 卖出不在目标列表中的ETF
    for security in current_positions:
        if security in g.etf_pool and security not in target_etfs_set:
            position = context.portfolio.positions[security]
            if position.total_amount > 0:  # 确保有持仓才卖出
                success = smart_order_target_value(security, 0, context)
                if success:
                    security_name = get_security_name(security)
                    log.info(f"📤 卖出: {security} {security_name} (不在目标列表中)")
                    
                    # 清除记录
                    if security in g.position_highs:
                        del g.position_highs[security]
                    if security in g.position_stop_prices:
                        del g.position_stop_prices[security]

    # 调整目标ETF的仓位
    for etf in target_etfs:
        # 获取该ETF的指标用于日志显示
        etf_metrics = next((m for m in ranked_etfs if m['etf'] == etf), None)
        
        # 计算当前持仓价值
        current_value = 0
        if etf in context.portfolio.positions:
            position = context.portfolio.positions[etf]
            if position.total_amount > 0:
                current_value = position.total_amount * position.price
        
        # 判断是否需要调仓（5%容差）
        if abs(current_value - target_value) > target_value * 0.05 or current_value == 0:
            audit_log(context, {
                'event': 'position_adjustment_needed',
                'security': etf,
                'name': get_security_name(etf),
                'current_value': current_value,
                'target_value': target_value,
                'deviation': current_value - target_value,
                'tolerance': target_value * 0.05,
                'reason': 'current_value_outside_5pct_tolerance_or_zero',
                'rule': '目标ETF当前市值偏离目标市值超过5%或当前无持仓时调仓',
            })
            success = smart_order_target_value(etf, target_value, context)
            if success and etf_metrics:
                action = "买入" if current_value < target_value else "调仓"
                etf_name = get_security_name(etf)
                log.info(f"📦 {action}: {etf} {etf_name}，目标金额: {target_value:.2f}，年化: {etf_metrics['annualized_returns']:.4f}，R²: {etf_metrics['r_squared']:.4f}，得分: {etf_metrics['score']:.4f}，短期动量: {etf_metrics['short_return']:.4f}，MA比率: {etf_metrics['ma_ratio']:.4f}，成交量比: {etf_metrics['volume_ratio']:.2f}，RSI: {etf_metrics['current_rsi']:.1f}，MACD柱: {etf_metrics['macd_bar']:.4f}，布林带: {etf_metrics['bollinger_info']}")
        else:
            pass

    audit_portfolio_state(context, 'after_rebalance', {
        'target_etfs': target_etfs,
        'selection_mode': selection_mode,
        'selection_reason': selection_reason,
        'rule': 'ETF轮动调仓后组合状态，用于评估收益、回撤、现金占比和持仓暴露',
    })

# 每日交易执行函数（保持兼容性）
def trade(context):
    """主交易函数，为了兼容性保留"""
    etf_trade(context)
















































# #coding=gbk
# """
# 标题：四季发财适应性改造
# 聚宽ETF轮动策略适应性改造 → QMT移植版（等比前复权修正 + 防重复 + 资金安全优化 + 黑名单与缓存增强 + 状态打印）
# 原聚宽策略：https://www.joinquant.com/post/65759 (ETF收益率稳定性轮动策略)
# 转写作者：Ai夸我像真人

# 修改说明：
#   - 复权方式：统一改为等比前复权 front_ratio，与聚宽 use_real_price 底层一致
#   - 成交量过滤均值计算修正（排除最近一日，严格按 lookback 天数取均值）
#   - 固定止损豁免防御 ETF 改为参数控制，默认不豁免
#   - 调仓时间改为 14:19 起每 5 分钟至 14:56，卖出后延迟 1 分钟买入，每日最多一次
#   - 止损仅在 9:30-14:19 每分钟执行，卖出后不立即买入，等待下次调仓
#   - 持仓停牌标的需卖出时暂停至 10:30
#   - 防御 ETF 可用性检查增加涨跌停判断
#   - 总资产为 0 时返回实际现金
#   - 下单均为 1 型（立即交易），买入预留 1% 缓冲，保护价降至 1.015 防止资金冻结超额
#   - 固定止损和 ATR 止损同一分钟仅执行一次，防止重复触发
#   - 黑名单机制：当日卖出后不再买回同一标的
#   - 数据缓存优化：批量拉取失败后单品重试，确保数据完整
#   - 策略状态打印：调仓时输出持仓、候选ETF排名详情、止损状况
# """
# import pandas as pd
# import numpy as np
# import math
# from datetime import datetime, timedelta
# from typing import Any, Dict, List, Optional

# # ======================== 通用交易类 ========================
# class HoldingSnapshot:
#     __slots__ = ('m_nVolume', 'm_nCanUseVolume', 'm_dOpenPrice')
#     def __init__(self, vol: int, can_use: int, cost: float):
#         self.m_nVolume = int(vol)
#         self.m_nCanUseVolume = int(can_use)
#         self.m_dOpenPrice = float(cost)

# def _holding_snapshot_from_counter_row(dt: Any) -> HoldingSnapshot:
#     return HoldingSnapshot(
#         int(getattr(dt, 'm_nVolume', 0) or 0),
#         int(getattr(dt, 'm_nCanUseVolume', 0) or 0),
#         float(getattr(dt, 'm_dOpenPrice', 0) or 0),
#     )

# class QMTTrader:
#     def __init__(
#         self,
#         context_info,
#         strategy_name: str = 'ETF轮动策略',
#         *,
#         strategy_initial_capital: Optional[float] = None,
#         account: Optional[str] = 'None',
#         accountType: Optional[str] = 'STOCK',
#         runMode: Optional[str] = None,
#         daily_fields_preset: Optional[List[str]] = None,
#         dividend_type: str = 'front_ratio',   # 等比前复权
#     ):
#         self.acct_id = account
#         self.acct_type = accountType
#         self.is_backtesting = context_info.do_back_test
#         self.strategy_name = strategy_name
#         self.run_mode = 'backtest' if self.is_backtesting else runMode
#         self.dividend_type = dividend_type
#         self.contextInfo = context_info
#         self.stock_info_cache = {}
#         self.last_date = None
#         self.stock_code = context_info.stockcode + '.' + context_info.market

#         if self.is_backtesting:
#             self.strategy_initial_capital = float(context_info.capital) if context_info.capital is not None else 100000.0
#         else:
#             self.strategy_initial_capital = float(strategy_initial_capital) if strategy_initial_capital is not None else 100000.0

#         if self.is_backtesting:
#             download_history_data(self.stock_code, context_info.period, '', '')
#             print(f'[init][回测][资金:{self.strategy_initial_capital}][复权:{self.dividend_type}]')
#         else:
#             print(f'[init][实盘][账号:{self.acct_id}][类型:{self.acct_type}][复权:{self.dividend_type}]')

#         self.buy_code = 23 if self.acct_type == 'STOCK' else 33
#         self.sell_code = 24 if self.acct_type == 'STOCK' else 34
#         self._daily_data_cache: dict = {}
#         self._daily_fields_preset: List[str] = list(daily_fields_preset or ['close', 'amount', 'volume', 'high'])

#     # ---------- 资金与持仓 ----------
#     def get_broker_available_cash(self) -> float:
#         for obj in get_trade_detail_data(self.acct_id, self.acct_type, 'ACCOUNT'):
#             if obj.m_dAvailable > 0:
#                 return float(obj.m_dAvailable)
#         return 0.0

#     def get_strategy_available_cash(self) -> float:
#         return self.get_broker_available_cash()

#     def get_strategy_total_value(self, context_info) -> float:
#         cash = self.get_strategy_available_cash()
#         holdings = self.get_holdings()
#         pos_val = 0.0
#         for code, snap in holdings.items():
#             if snap.m_nVolume > 0:
#                 price = self.get_price(context_info, stock_code=code) or 0
#                 pos_val += price * snap.m_nVolume
#         total = cash + pos_val
#         return total if total > 0 else cash

#     def get_holdings(self, print_holdings=False) -> Dict[str, HoldingSnapshot]:
#         holdinglist: Dict[str, HoldingSnapshot] = {}
#         for dt in get_trade_detail_data(self.acct_id, self.acct_type, 'POSITION'):
#             key = dt.m_strInstrumentID + '.' + dt.m_strExchangeID
#             holdinglist[key] = _holding_snapshot_from_counter_row(dt)
#             if print_holdings:
#                 h = holdinglist[key]
#                 print(key, h.m_nVolume, h.m_nCanUseVolume, h.m_dOpenPrice)
#         return holdinglist

#     def get_stock_info(self, symbol, field=None):
#         try:
#             if symbol not in self.stock_info_cache:
#                 info = self.contextInfo.get_instrument_detail(symbol)
#                 if info: self.stock_info_cache[symbol] = info
#             info = self.stock_info_cache[symbol]
#             return info.get(field) if field and info else (info if info else {})
#         except:
#             return {} if field is None else None

#     def get_price(self, context_info, stock_code=None, is_last_price=True):
#         if stock_code is None: stock_code = self.stock_code
#         if self.is_backtesting or not is_last_price:
#             timetag = context_info.get_bar_timetag(context_info.barpos)
#             endtime = timetag_to_datetime(timetag, '%Y%m%d%H%M%S')
#             df = context_info.get_market_data_ex(
#                 ['close', 'lastPrice'], [stock_code],
#                 end_time=endtime, count=1, period=context_info.period,
#                 dividend_type=self.dividend_type, fill_data=True, subscribe=True
#             )
#             if not df or stock_code not in df or df[stock_code].empty:
#                 return None
#             price = None
#             if 'lastPrice' in df[stock_code].columns and not df[stock_code]['lastPrice'].empty:
#                 price = df[stock_code]['lastPrice'].iloc[-1]
#             if (price is None or math.isnan(price)) and 'close' in df[stock_code].columns and not df[stock_code]['close'].empty:
#                 price = df[stock_code]['close'].iloc[-1]
#             return float(price) if price is not None and not math.isnan(price) else None
#         else:
#             tick = context_info.get_full_tick([stock_code])
#             if stock_code in tick and tick[stock_code]['lastPrice'] > 0:
#                 return tick[stock_code]['lastPrice']
#         return None

#     def get_current_time(self, context_info, fmt='%H%M%S') -> str:
#         return timetag_to_datetime(context_info.get_bar_timetag(context_info.barpos), fmt)

#     def is_new_calendar_day(self, context_info, curdate='') -> bool:
#         if curdate == '': curdate = self.get_current_time(context_info, '%Y%m%d')
#         changed = curdate != self.last_date
#         self.last_date = curdate
#         return changed

#     def is_trading_time(self, context_info, curtime='') -> bool:
#         if not curtime: curtime = self.get_current_time(context_info)
#         return '093000' <= curtime <= '145700'

#     # ---------- 日线数据缓存（增强：单品重试） ----------
#     def get_daily_data_cached(
#         self, fields: List[str], codes: List[str], count: int,
#         end_time: Optional[str] = '', start_time: Optional[str] = '',
#         subscribe: bool = False,
#     ) -> Dict[str, Dict[str, pd.Series]]:
#         cache = self._daily_data_cache
#         if not end_time: end_time = self.get_current_time(self.contextInfo, '%Y%m%d')
#         fetch_fields = list(set(fields) | set(self._daily_fields_preset))
#         codes_needed = []
#         today = datetime.now()
#         end_time_dt = datetime.strptime(end_time, '%Y%m%d')
#         fetch_count = max(count + (today - end_time_dt).days, 500)

#         for code in codes:
#             entry = cache.get(code)
#             if entry is None or entry.get('count', 0) < fetch_count or \
#               not all(f in entry.get('data', {}) for f in fields):
#                 codes_needed.append(code)

#         if codes_needed:
#             fetch_codes = list(set(codes_needed))
#             # 批量拉取
#             try:
#                 raw = self.contextInfo.get_market_data_ex(
#                     fetch_fields, fetch_codes, period='1d', count=fetch_count,
#                     end_time='', subscribe=False, dividend_type=self.dividend_type)
#                 for code, df in raw.items():
#                     if df is not None and not df.empty:
#                         cache[code] = {'data': {f: df[f] for f in fetch_fields if f in df}, 'count': len(df)}
#             except Exception as e:
#                 print(f'[日线缓存] 批量拉取失败: {e}')
#             # 单品重试（确保数据完整）
#             for code in codes_needed:
#                 if code not in cache:
#                     try:
#                         single = self.contextInfo.get_market_data_ex(
#                             fetch_fields, [code], period='1d', count=fetch_count,
#                             end_time='', subscribe=False, dividend_type=self.dividend_type)
#                         if single and code in single and not single[code].empty:
#                             data_dict = {f: single[code][f] for f in fetch_fields if f in single[code]}
#                             cache[code] = {'data': data_dict, 'count': len(single[code])}
#                     except Exception as e2:
#                         pass

#         result = {}
#         for code in codes:
#             entry = cache.get(code)
#             if entry is None: continue
#             data = entry['data']
#             result[code] = {}
#             for f in fields:
#                 ser = data.get(f)
#                 if ser is not None and len(ser) > 0:
#                     if not isinstance(ser.index, pd.DatetimeIndex):
#                         ser.index = pd.to_datetime(ser.index, format='%Y%m%d', errors='coerce')
#                     if end_time:
#                         ser = ser[[x.strftime('%Y%m%d') <= end_time for x in ser.index]]
#                     ser = ser.iloc[-count:] if len(ser) > 0 else ser
#                     result[code][f] = ser
#         return result

# # ======================== 全局变量 ========================
# trader: QMTTrader = None
# period = 1
# g = None

# def init_global_vars(ContextInfo):
#     global g
#     g = {}

#     g['etf_pool'] = [
#         "518880.SH", "159980.SZ", "159985.SZ", "501018.SH",
#         "513100.SH", "513500.SH", "513520.SH", "513030.SH", "513080.SH",
#         "159920.SZ", "510300.SH", "510500.SH", "510050.SH", "510210.SH",
#         "159915.SZ", "588080.SH", "159995.SZ", "513050.SH", "159852.SZ",
#         "159845.SZ", "515030.SH", "159806.SZ", "516160.SH", "159928.SZ",
#         "511010.SH", "511880.SH",
#     ]
#     g['defensive_etf'] = "511880.SH"

#     # ---------- 核心参数 ----------
#     g['lookback_days'] = 25
#     g['holdings_num'] = 1
#     g['min_money'] = 5000
#     g['stop_loss'] = 0.95
#     g['loss'] = 0.97

#     g['min_score_threshold'] = 0.0
#     g['max_score_threshold'] = 5.0

#     # ---------- 短期动量过滤 ----------
#     g['use_short_momentum_filter'] = True
#     g['short_lookback_days'] = 10
#     g['short_momentum_threshold'] = 0.0

#     # ---------- MA过滤（默认关闭）----------
#     g['use_ma_filter'] = False
#     g['ma_short_period'] = 5
#     g['ma_long_period'] = 25
#     g['ma_filter_condition'] = "above"

#     # ---------- RSI过滤 ----------
#     g['use_rsi_filter'] = True
#     g['rsi_period'] = 6
#     g['rsi_lookback_days'] = 1
#     g['rsi_threshold'] = 95

#     # ---------- MACD过滤（关闭）----------
#     g['use_macd_filter'] = False
#     g['macd_fast_period'] = 12
#     g['macd_slow_period'] = 26
#     g['macd_signal_period'] = 9
#     g['macd_filter_condition'] = "bullish"

#     # ---------- 成交量异常过滤（关闭）----------
#     g['use_volume_filter'] = False
#     g['volume_lookback_days'] = 7
#     g['volume_threshold'] = 2.0
#     g['volume_exclude_defensive'] = True

#     # ---------- 布林带过滤（关闭）----------
#     g['use_bollinger_filter'] = False
#     g['bollinger_period'] = 20
#     g['bollinger_std'] = 2.0
#     g['bollinger_lookback_days'] = 3

#     # ---------- ATR动态止损 ----------
#     g['use_atr_stop_loss'] = True
#     g['atr_period'] = 14
#     g['atr_multiplier'] = 2
#     g['atr_trailing_stop'] = False
#     g['atr_exclude_defensive'] = True

#     # ---------- 固定止损 ----------
#     g['use_fixed_stop_loss'] = True
#     g['fixed_stop_loss_ratio'] = 0.95
#     g['stop_loss_exclude_defensive'] = False

#     # 运行时变量
#     g['rankings_cache_date'] = None
#     g['rankings_cache_data'] = None
#     g['profit_protection_sold_today'] = []    # 当日卖出黑名单
#     g['last_monitor_time'] = ''
#     g['daily_buy_done'] = False
#     g['blocked_until'] = ''
#     g['pending_buy'] = False
#     g['pending_buy_time'] = ''
#     g['pending_buy_targets'] = []
#     g['just_sold_codes'] = set()
#     g['yesterday_close_cache'] = {}
#     g['position_highs'] = {}
#     g['position_stop_prices'] = {}

#     # 防重复记录
#     g['last_fixed_stop_time'] = ''
#     g['last_atr_stop_time'] = ''

# def init(ContextInfo):
#     global trader
#     trader = QMTTrader(
#         ContextInfo,
#         strategy_name='ETF轮动策略v1.0',
#         account=account if 'account' in globals() else '39100001240801',
#         accountType=accountType if 'accountType' in globals() else 'STOCK',
#         strategy_initial_capital=init_capital if 'init_capital' in globals() else 1000000.0,
#         runMode='real',
#         dividend_type='front_ratio',
#     )
#     init_global_vars(ContextInfo)
#     print("=" * 60)
#     print("ETF收益率稳定性轮动策略 V1.0 - QMT等比前复权修正版 (黑名单/缓存/打印增强) 已初始化")
#     print("=" * 60)
#     for code in g['etf_pool']:
#         ContextInfo.subscribe_quote(code, period='1m')
#     download_hist_data_all(ContextInfo)

# def download_hist_data_all(context):
#     if context.do_back_test: return
#     for code in g['etf_pool']:
#         try:
#             download_history_data(code, '1m', '', '')
#             download_history_data(code, '1d', '', '')
#         except: pass
#     _ = trader.get_daily_data_cached([], g['etf_pool'], count=300)

# # ======================== 主循环 ========================
# def handlebar(ContextInfo):
#     global trader
#     cur_datetime = trader.get_current_time(ContextInfo, '%Y%m%d%H%M%S')
#     cur_date = cur_datetime[:8]
#     cur_time_hm = cur_datetime[8:12]
#     cur_time_hms = cur_datetime[8:14]

#     if not trader.is_backtesting:
#         if cur_date != datetime.now().strftime('%Y%m%d'):
#             return
#         if not ContextInfo.is_last_bar():
#             return

#     if trader.is_new_calendar_day(ContextInfo, cur_date):
#         g['rankings_cache_date'] = None
#         g['rankings_cache_data'] = None
#         g['profit_protection_sold_today'] = []
#         g['pending_buy'] = False
#         g['pending_buy_targets'] = []
#         g['just_sold_codes'] = set()
#         g['yesterday_close_cache'] = {}
#         g['last_monitor_time'] = ''
#         g['daily_buy_done'] = False
#         g['blocked_until'] = ''
#         g['last_fixed_stop_time'] = ''
#         g['last_atr_stop_time'] = ''
#         print(f'★ {cur_date} 新交易日 ★')
#         download_hist_data_all(ContextInfo)

#     check_pending_buy(ContextInfo, cur_datetime)

#     # 09:10 持仓检查
#     if cur_time_hm == '0910':
#         check_positions(ContextInfo)

#     # 分钟级止损（仅在9:30-14:19执行，且同一分钟只执行一次）
#     if '0930' <= cur_time_hm <= '1419':
#         if cur_time_hm != g.get('last_fixed_stop_time', ''):
#             g['last_fixed_stop_time'] = cur_time_hm
#             minute_level_stop_loss(ContextInfo, cur_date, cur_time_hms)
#         if cur_time_hm != g.get('last_atr_stop_time', ''):
#             g['last_atr_stop_time'] = cur_time_hm
#             minute_atr_stop_loss(ContextInfo, cur_date, cur_time_hms)

#     # 调仓监控：14:19 起每5分钟至14:56
#     if '1419' <= cur_time_hm <= '1456' and not g.get('daily_buy_done', False):
#         if g['blocked_until'] and cur_time_hm < g['blocked_until']:
#             return
#         try:
#             h = int(cur_time_hm[:2]); m = int(cur_time_hm[2:4])
#             base = 14 * 60 + 19
#             diff = (h * 60 + m) - base
#         except:
#             diff = -1
#         if diff >= 0 and diff % 5 == 0:
#             if g['last_monitor_time'] != cur_datetime:
#                 g['last_monitor_time'] = cur_datetime
#                 monitor_and_trade(ContextInfo, cur_date, cur_time_hms)

# def check_pending_buy(ContextInfo, cur_datetime_str):
#     if not g.get('pending_buy'): return
#     if g.get('daily_buy_done', False):
#         g['pending_buy'] = False
#         return
#     pending_time = g['pending_buy_time']
#     if cur_datetime_str < pending_time: return
#     cur_time_hm = cur_datetime_str[8:12]
#     print(f"[{cur_time_hm}] 延迟买入触发")
#     g['just_sold_codes'].clear()
#     g['target_etfs_list'] = list(g['pending_buy_targets'])
#     old_pos = set(trader.get_holdings().keys())
#     execute_buy_trades(ContextInfo)
#     new_pos = set(trader.get_holdings().keys())
#     g['pending_buy'] = False
#     g['pending_buy_time'] = ''
#     g['pending_buy_targets'] = []
#     if new_pos != old_pos:
#         g['daily_buy_done'] = True
#         print(f"[{cur_time_hm}] 买入完成，今日不再调仓")
#     else:
#         print(f"[{cur_time_hm}] 买入未改变持仓，下一轮监控会继续尝试")

# # ======================== 止损函数 ========================
# def minute_level_stop_loss(ContextInfo, cur_date, cur_time):
#     if not g['use_fixed_stop_loss'] or not trader.is_trading_time(ContextInfo, cur_time):
#         return
#     try:
#         holdings = trader.get_holdings()
#         for sec, pos in holdings.items():
#             if pos.m_nVolume <= 0 or pos.m_nCanUseVolume <= 0:
#                 continue
#             if g['stop_loss_exclude_defensive'] and sec == g['defensive_etf']:
#                 continue
#             cur_price = trader.get_price(ContextInfo, sec)
#             if not cur_price or cur_price <= 0: continue
#             cost = pos.m_dOpenPrice
#             if cost <= 0: continue
#             if cur_price <= cost * g['fixed_stop_loss_ratio']:
#                 print(f"[止损] {sec} 固定止损触发 现价{cur_price:.3f} 成本{cost:.3f}")
#                 if smart_order_target_value(sec, 0, ContextInfo):
#                     add_to_blacklist(sec)  # 黑名单记录
#     except Exception as e:
#         print(f"止损异常: {e}")

# def minute_atr_stop_loss(ContextInfo, cur_date, cur_time):
#     if not g['use_atr_stop_loss'] or not trader.is_trading_time(ContextInfo, cur_time):
#         return
#     try:
#         holdings = trader.get_holdings()
#         for sec, pos in holdings.items():
#             if pos.m_nVolume <= 0 or pos.m_nCanUseVolume <= 0:
#                 continue
#             if g['atr_exclude_defensive'] and sec == g['defensive_etf']:
#                 continue
#             cur_price = trader.get_price(ContextInfo, sec)
#             if not cur_price or cur_price <= 0: continue
#             cost = pos.m_dOpenPrice

#             if sec not in g['position_highs']:
#                 g['position_highs'][sec] = cur_price
#             else:
#                 g['position_highs'][sec] = max(g['position_highs'][sec], cur_price)

#             daily = trader.get_daily_data_cached(['high', 'low', 'close'], [sec], count=g['atr_period']+5, end_time=cur_date)
#             if sec not in daily or 'high' not in daily[sec] or 'low' not in daily[sec] or 'close' not in daily[sec]:
#                 continue
#             high_vals = daily[sec]['high'].values
#             low_vals = daily[sec]['low'].values
#             close_vals = daily[sec]['close'].values
#             if len(close_vals) < g['atr_period'] + 1:
#                 continue
#             atr = calc_atr(high_vals, low_vals, close_vals, g['atr_period'])
#             if atr is None or atr == 0:
#                 continue

#             if g['atr_trailing_stop']:
#                 stop_price = g['position_highs'][sec] - g['atr_multiplier'] * atr
#             else:
#                 stop_price = cost - g['atr_multiplier'] * atr

#             if cur_price <= stop_price:
#                 print(f"[ATR止损] {sec} 触发 现价{cur_price:.3f} 止损价{stop_price:.3f}")
#                 if smart_order_target_value(sec, 0, ContextInfo):
#                     add_to_blacklist(sec)
#                     if sec in g['position_highs']:
#                         del g['position_highs'][sec]
#     except Exception as e:
#         print(f"ATR止损异常: {e}")

# def calc_atr(high_prices, low_prices, close_prices, period=14):
#     tr = np.zeros(len(close_prices))
#     for i in range(1, len(close_prices)):
#         tr[i] = max(high_prices[i]-low_prices[i], abs(high_prices[i]-close_prices[i-1]), abs(low_prices[i]-close_prices[i-1]))
#     atr = np.zeros(len(tr))
#     if len(tr) > period:
#         atr[period] = np.mean(tr[1:period+1])
#         for i in range(period+1, len(tr)):
#             atr[i] = (atr[i-1] * (period-1) + tr[i]) / period
#         return atr[-1]
#     return None

# # ======================== 排名与动量计算 ========================
# def get_cached_rankings(ContextInfo):
#     cur_date = trader.get_current_time(ContextInfo, '%Y%m%d')
#     if g['rankings_cache_date'] != cur_date:
#         print("重新计算ETF排名...")
#         ranked = get_ranked_etfs(ContextInfo, cur_date)
#         g['rankings_cache_date'] = cur_date
#         g['rankings_cache_data'] = ranked
#     return g['rankings_cache_data']

# def get_ranked_etfs(ContextInfo, cur_date):
#     etf_metrics = []
#     for etf in g['etf_pool']:
#         tick = ContextInfo.get_full_tick([etf]).get(etf)
#         if tick and tick.get('status') in ['停牌', 'ST停牌']:
#             continue
#         metrics = calculate_momentum_metrics(ContextInfo, etf, cur_date)
#         if metrics and g['min_score_threshold'] < metrics['score'] < g['max_score_threshold']:
#             etf_metrics.append(metrics)
#     etf_metrics.sort(key=lambda x: x['score'], reverse=True)
#     return etf_metrics

# def calculate_momentum_metrics(ContextInfo, etf, cur_date):
#     try:
#         name = get_stock_name(etf)
#         max_lookback = max(g['lookback_days'], g['short_lookback_days'], g['ma_long_period'],
#                           g['rsi_period'] + g['rsi_lookback_days'],
#                           g['macd_slow_period'] + g['macd_signal_period'],
#                           g['volume_lookback_days'],
#                           g['bollinger_period'] + g['bollinger_lookback_days']) + 20
#         daily = trader.get_daily_data_cached(['close', 'high', 'volume'], [etf], count=max_lookback, end_time=cur_date)
#         if etf not in daily or 'close' not in daily[etf] or len(daily[etf]['close']) < g['lookback_days']:
#             return None

#         close_ser = daily[etf]['close']
#         if not isinstance(close_ser.index, pd.DatetimeIndex):
#             close_ser.index = pd.to_datetime(close_ser.index, format='%Y%m%d', errors='coerce')
#         mask = [idx.strftime('%Y%m%d') != cur_date for idx in close_ser.index]
#         hist_close = close_ser[mask].values
#         if len(hist_close) < g['lookback_days']:
#             return None

#         cur_price = trader.get_price(ContextInfo, etf)
#         if not cur_price:
#             return None

#         price_series = np.append(hist_close, cur_price)

#         # ---- 1. 近3日跌幅过滤 ----
#         if len(price_series) >= 4:
#             d1, d2, d3 = price_series[-1]/price_series[-2], price_series[-2]/price_series[-3], price_series[-3]/price_series[-4]
#             if min(d1, d2, d3) < g['loss']:
#                 return None

#         # ---- 2. 短期动量过滤 ----
#         short_ret = 0.0
#         if len(price_series) >= g['short_lookback_days'] + 1:
#             short_ret = price_series[-1] / price_series[-(g['short_lookback_days']+1)] - 1
#         short_annual = (1+short_ret)**(250/g['short_lookback_days']) - 1 if short_ret != 0 else 0.0
#         if g['use_short_momentum_filter'] and short_annual < g['short_momentum_threshold']:
#             return None

#         # ---- 3. MA过滤 ----
#         ma5 = np.mean(price_series[-g['ma_short_period']:]) if len(price_series) >= g['ma_short_period'] else 0
#         ma25 = np.mean(price_series[-g['ma_long_period']:]) if len(price_series) >= g['ma_long_period'] else 0
#         ma_pass = True
#         if g['use_ma_filter'] and ma5 > 0 and ma25 > 0:
#             if g['ma_filter_condition'] == 'above':
#                 ma_pass = ma5 >= ma25
#             else:
#                 ma_pass = ma5 <= ma25
#         if not ma_pass:
#             return None

#         # ---- 4. RSI过滤 ----
#         rsi_pass = True
#         if g['use_rsi_filter'] and len(price_series) >= g['rsi_period'] + g['rsi_lookback_days']:
#             rsi_vals = calculate_rsi(price_series, g['rsi_period'])
#             if len(rsi_vals) >= g['rsi_lookback_days']:
#                 recent_rsi = rsi_vals[-g['rsi_lookback_days']:]
#                 if np.any(recent_rsi > g['rsi_threshold']):
#                     if ma5 > 0 and cur_price < ma5:
#                         rsi_pass = False
#         if not rsi_pass:
#             return None

#         # ---- 5. MACD过滤 ----
#         macd_pass = True
#         if g['use_macd_filter'] and len(price_series) >= g['macd_slow_period'] + g['macd_signal_period']:
#             dif, dea, _ = calculate_macd(price_series, g['macd_fast_period'], g['macd_slow_period'], g['macd_signal_period'])
#             if len(dif) > 0:
#                 if g['macd_filter_condition'] == 'bullish':
#                     macd_pass = dif[-1] > dea[-1]
#                 else:
#                     macd_pass = dif[-1] < dea[-1]
#         if not macd_pass:
#             return None

#         # ---- 6. 成交量过滤（修正：严格按 lookback 天均值且排除最近一日） ----
#         vol_pass = True
#         if g['use_volume_filter']:
#             hist_volumes = daily[etf].get('volume')
#             if hist_volumes is not None and len(hist_volumes) > 0:
#                 vol_ser = hist_volumes[mask]
#                 if len(vol_ser) > 0:
#                     lookback = g['volume_lookback_days']
#                     recent_vol = vol_ser.iloc[-1]
#                     if len(vol_ser) >= lookback + 1:
#                         avg_vol = vol_ser.iloc[-(lookback+1):-1].mean()
#                     else:
#                         avg_vol = vol_ser.iloc[:-1].mean()
#                     if avg_vol > 0 and recent_vol > avg_vol * g['volume_threshold']:
#                         vol_pass = False
#         if not vol_pass:
#             return None

#         # ---- 7. 布林带过滤 ----
#         boll_pass = True
#         if g['use_bollinger_filter'] and len(price_series) >= g['bollinger_period']:
#             mid, upper, lower = calculate_bollinger_bands(price_series, g['bollinger_period'], g['bollinger_std'])
#             if len(upper) >= g['bollinger_lookback_days']:
#                 recent_close = price_series[-g['bollinger_lookback_days']:]
#                 recent_upper = upper[-g['bollinger_lookback_days']:]
#                 if np.any(recent_close > recent_upper) and cur_price < np.mean(price_series[-5:]):
#                     boll_pass = False
#         if not boll_pass:
#             return None

#         # ---- 长期动量得分 ----
#         recent = price_series[-(g['lookback_days']+1):]
#         y = np.log(recent)
#         x = np.arange(len(y))
#         weights = np.linspace(1, 2, len(y))
#         slope, intercept = np.polyfit(x, y, 1, w=weights)
#         annual_ret = math.exp(slope * 250) - 1
#         ss_res = np.sum(weights * (y - (slope*x + intercept))**2)
#         ss_tot = np.sum(weights * (y - np.mean(y))**2)
#         r2 = 1 - ss_res/ss_tot if ss_tot else 0
#         score = annual_ret * r2

#         return {
#             'etf': etf, 'name': name, 'score': score,
#             'annualized_returns': annual_ret, 'r_squared': r2,
#             'current_price': cur_price, 'short_annual': short_annual,
#         }
#     except Exception as e:
#         return None

# # ======================== 技术指标函数 ========================
# def calculate_rsi(prices, period=6):
#     deltas = np.diff(prices)
#     gains = np.where(deltas > 0, deltas, 0)
#     losses = np.where(deltas < 0, -deltas, 0)
#     avg_gain = np.mean(gains[:period])
#     avg_loss = np.mean(losses[:period])
#     rsi = np.zeros(len(prices))
#     rsi[:period] = 50
#     for i in range(period, len(prices)):
#         avg_gain = (avg_gain * (period-1) + gains[i-1]) / period
#         avg_loss = (avg_loss * (period-1) + losses[i-1]) / period
#         if avg_loss == 0:
#             rsi[i] = 100
#         else:
#             rs = avg_gain / avg_loss
#             rsi[i] = 100 - 100/(1+rs)
#     return rsi[period:]

# def calculate_macd(prices, fast=12, slow=26, signal=9):
#     def ema(data, period):
#         ema_arr = np.zeros(len(data))
#         ema_arr[0] = data[0]
#         alpha = 2/(period+1)
#         for i in range(1, len(data)):
#             ema_arr[i] = alpha*data[i] + (1-alpha)*ema_arr[i-1]
#         return ema_arr
#     ema_fast = ema(prices, fast)
#     ema_slow = ema(prices, slow)
#     dif = ema_fast - ema_slow
#     dea = ema(dif, signal)
#     macd_bar = dif - dea
#     start = slow + signal - 1
#     return dif[start:], dea[start:], macd_bar[start:]

# def calculate_bollinger_bands(prices, period=20, std_dev=2.0):
#     mid = np.zeros(len(prices))
#     upper = np.zeros(len(prices))
#     lower = np.zeros(len(prices))
#     for i in range(period-1, len(prices)):
#         window = prices[i-period+1:i+1]
#         m = np.mean(window)
#         s = np.std(window)
#         mid[i] = m
#         upper[i] = m + std_dev * s
#         lower[i] = m - std_dev * s
#     return mid[period-1:], upper[period-1:], lower[period-1:]

# # ======================== 黑名单辅助函数 ========================
# def add_to_blacklist(security):
#     """将卖出标的加入当日黑名单，防止再次买入"""
#     if security not in g['profit_protection_sold_today']:
#         g['profit_protection_sold_today'].append(security)
#         print(f"?? 黑名单记录: {security} {get_stock_name(security)}，当日不再买入")

# # ======================== 交易执行 ========================
# def monitor_and_trade(ContextInfo, cur_date, cur_time):
#     if g.get('daily_buy_done', False):
#         return
#     if g.get('pending_buy', False):
#         return

#     g['just_sold_codes'].clear()
#     old_holdings = {sec: pos.m_nVolume for sec, pos in trader.get_holdings().items() if pos.m_nVolume > 0}

#     # ---- 打印当前持仓 ----
#     print("=== 当前持仓 ===")
#     if old_holdings:
#         for sec, vol in old_holdings.items():
#             print(f"  {sec} {get_stock_name(sec)} 数量{vol}")
#     else:
#         print("  空仓")

#     ranked = get_cached_rankings(ContextInfo)
#     g['rankings_cache_data'] = ranked

#     # ---- 打印候选ETF排名前5 ----
#     print("=== ETF 动量排名前5 ===")
#     for i, m in enumerate(ranked[:5]):
#         print(f"  排名{i+1}: {m['etf']} {m['name']} 得分{m['score']:.4f} 年化{m['annualized_returns']*100:.2f}% R2={m['r_squared']:.4f} 短期动量{m['short_annual']*100:.2f}%")

#     # ---- 打印黑名单 ----
#     if g['profit_protection_sold_today']:
#         print(f"  ?? 今日已卖出（黑名单）: {g['profit_protection_sold_today']}")

#     # 确定目标（排除黑名单）
#     target_etfs = []
#     for m in ranked:
#         if len(target_etfs) >= g['holdings_num']:
#             break
#         etf = m['etf']
#         if etf in g['profit_protection_sold_today']:
#             print(f"  ? 黑名单跳过: {etf} {m['name']}")
#             continue
#         target_etfs.append(etf)

#     if not target_etfs:
#         if check_defensive_etf_available(ContextInfo):
#             target_etfs = [g['defensive_etf']]
#             print("进入防御模式，目标: 511880")
#         else:
#             print("无可用标的，保持空仓")
#             g['daily_buy_done'] = True
#             return

#     g['target_etfs_list'] = target_etfs

#     for sec in list(trader.get_holdings().keys()):
#         if sec in target_etfs or sec not in g['etf_pool']:
#             continue
#         tick = ContextInfo.get_full_tick([sec]).get(sec)
#         if tick and tick.get('status') in ['停牌', 'ST停牌']:
#             print(f"? {sec} 停牌，暂停调仓至 10:30")
#             g['blocked_until'] = '1030'
#             return

#     sell_triggered = False
#     for sec, pos in trader.get_holdings().items():
#         if pos.m_nVolume <= 0: continue
#         if sec not in target_etfs:
#             if smart_order_target_value(sec, 0, ContextInfo):
#                 print(f"卖出 {sec}")
#                 g['just_sold_codes'].add(sec)
#                 add_to_blacklist(sec)  # 黑名单记录
#                 sell_triggered = True

#     if sell_triggered:
#         cur_dt = cur_date + cur_time[:4]
#         next_min = (datetime.strptime(cur_dt, '%Y%m%d%H%M') + timedelta(minutes=1)).strftime('%Y%m%d%H%M%S')
#         g['pending_buy'] = True
#         g['pending_buy_time'] = next_min
#         g['pending_buy_targets'] = list(target_etfs)
#         print(f"[{cur_time[:4]}] 卖出完成，买入安排在 {next_min[8:14]}")
#         return

#     execute_buy_trades(ContextInfo)
#     new_holdings = {sec: pos.m_nVolume for sec, pos in trader.get_holdings().items() if pos.m_nVolume > 0}
#     if set(old_holdings.keys()) != set(new_holdings.keys()) or any(old_holdings.get(k) != new_holdings.get(k) for k in old_holdings):
#         g['daily_buy_done'] = True
#         print(f"[{cur_time[:4]}] 买入完成，今日不再调仓")
#     else:
#         print(f"[{cur_time[:4]}] 买入未改变持仓，下一轮继续尝试")

# def execute_buy_trades(ContextInfo):
#     target_etfs = g.get('target_etfs_list', [])
#     if not target_etfs: return
#     if g.get('daily_buy_done', False): return

#     current_holds = set()
#     for sec, pos in trader.get_holdings().items():
#         if pos.m_nVolume > 0 and sec not in g['just_sold_codes']:
#             current_holds.add(sec)
#     to_buy = [e for e in target_etfs if e not in current_holds]
#     max_buy = max(0, g['holdings_num'] - len(current_holds))
#     to_buy = to_buy[:max_buy]

#     if not to_buy:
#         print("无需买入")
#         return

#     # 过滤黑名单
#     to_buy = [e for e in to_buy if e not in g['profit_protection_sold_today']]
#     if not to_buy:
#         print("所有目标均被黑名单屏蔽，无法买入")
#         return

#     cash = trader.get_strategy_available_cash()
#     per = cash * 0.99 / len(to_buy)
#     if per < g['min_money']:
#         print("资金不足")
#         return

#     success = False
#     for etf in to_buy:
#         if smart_order_target_value(etf, per, ContextInfo):
#             success = True

#     if success:
#         g['daily_buy_done'] = True
#     else:
#         print("买入失败，等待下一轮监控尝试")

# def check_positions(ContextInfo):
#     g['profit_protection_sold_today'] = []
#     for sec, pos in trader.get_holdings().items():
#         if pos.m_nVolume > 0:
#             print(f"持仓 {sec} {get_stock_name(sec)} 数量{pos.m_nVolume} 成本{pos.m_dOpenPrice:.3f}")

# def smart_order_target_value(security, target_value, ContextInfo):
#     name = get_stock_name(security)
#     if not trader.is_backtesting:
#         tick = ContextInfo.get_full_tick([security])
#         if not tick or security not in tick:
#             return False
#         info = tick[security]
#         if info.get('status') in ['停牌', 'ST停牌']:
#             return False
#         cur_price = info.get('lastPrice', 0)
#         if cur_price <= 0: return False
#         last_close = info.get('lastClose', 0)
#         high_limit = (last_close * 1.1) if last_close > 0 else (cur_price * 1.1)
#         low_limit = (last_close * 0.9) if last_close > 0 else (cur_price * 0.9)
#         if target_value > 0 and cur_price >= high_limit: return False
#         if target_value == 0 and cur_price <= low_limit: return False
#     else:
#         cur_price = trader.get_price(ContextInfo, security)
#         if not cur_price: return False

#     if target_value > 0:
#         calc_price = cur_price * 1.0099
#         target_vol = int(target_value / calc_price)
#     else:
#         target_vol = 0
#     target_vol = (target_vol // 100) * 100
#     if target_vol <= 0 and target_value > 0:
#         if 100 * calc_price > target_value: return False
#         target_vol = 100

#     pos = trader.get_holdings().get(security)
#     cur_vol = pos.m_nVolume if pos else 0
#     closeable = pos.m_nCanUseVolume if pos else 0
#     diff = target_vol - cur_vol
#     if diff == 0: return True

#     if 0 < abs(diff) * cur_price < g['min_money']: return False
#     if diff < 0 and closeable == 0:
#         print(f"{security} T+1限制")
#         return False
#     diff = max(diff, -closeable)

#     market = 'SH' if security.endswith('.SH') else 'SZ'
#     prType = 42 if market == 'SH' else 47
#     protect = (cur_price * 1.015) if diff > 0 else (cur_price * 0.92)

#     try:
#         passorder(23 if diff>0 else 24, 1101, trader.acct_id, security,
#                   prType, protect, abs(diff),
#                   trader.strategy_name, 1, f"轮动_{security}", ContextInfo)
#         print(f"{'买入' if diff>0 else '卖出'} {security} {abs(diff)}股")
#         return True
#     except Exception as e:
#         print(f"下单失败 {security}: {e}")
#         return False

# def check_defensive_etf_available(ContextInfo):
#     code = g['defensive_etf']
#     if trader.is_backtesting:
#         return trader.get_price(ContextInfo, code) is not None
#     tick = ContextInfo.get_full_tick([code]).get(code)
#     if not tick or tick.get('status') in ['停牌', 'ST停牌']:
#         return False
#     last_close = tick.get('lastClose', 0)
#     cur_price = tick.get('lastPrice', 0)
#     if last_close > 0 and cur_price >= last_close * 1.1:
#         print(f"防御ETF {code} 涨停，不可买入")
#         return False
#     if last_close > 0 and cur_price <= last_close * 0.9:
#         print(f"防御ETF {code} 跌停，不可买入")
#         return False
#     return True

# def get_stock_name(symbol) -> str:
#     info = trader.get_stock_info(symbol)
#     return info.get('InstrumentName', symbol) if info else symbol
