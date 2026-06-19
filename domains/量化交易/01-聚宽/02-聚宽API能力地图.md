---
title: 聚宽 API 能力地图
type: concept
created: 2026-06-19
updated: 2026-06-19
domain: 量化交易
tags: [joinquant, jqdata, api-docs, backtesting]
sources:
  - raw/api/joinquant/joinquant-api-2026-06-19.md
  - _meta/extraction-notes/joinquant-api-2026-06-19/coverage-matrix.md
status: active
---

# 聚宽 API 能力地图

## 策略生命周期

| 任务 | 主要 API | 注意 |
| --- | --- | --- |
| 初始化策略 | `initialize(context)` | 整个回测/模拟开始时执行一次。 |
| 进程重启初始化 | `process_initialize(context)` | 适合初始化不能持久化保存的对象。 |
| 修改模拟盘代码后处理 | `after_code_changed(context)` | 模拟盘替换代码不会重新执行 `initialize`。 |
| 开盘前逻辑 | `before_trading_start(context)` 或 `run_daily(..., '09:00')` | 可选，空函数会降低速度。 |
| 盘中逻辑 | `run_daily` 或 `handle_data(context, data)` | 普通策略优先定时函数。 |
| 收盘后逻辑 | `after_trading_end(context)` 或 `run_daily(..., '15:30')` | 用于记录、复盘、清理状态。 |

## 调度能力

| 任务 | API | 关键约束 |
| --- | --- | --- |
| 每日定时 | `run_daily(func, time='9:30')` | `func(context)`，不能传 `data`。 |
| 每周定时 | `run_weekly(func, weekday, time='9:30', force=False)` | `weekday` 可为负数。 |
| 每月定时 | `run_monthly(func, monthday, time='9:30', force=False)` | `monthday` 可为负数。 |
| 清理旧定时任务 | `unschedule_all()` | 修改定时计划前使用。 |

## 设置能力

| 任务 | API | 默认建议 |
| --- | --- | --- |
| 设置基准 | `set_benchmark` | A 股常用 `000300.XSHG`。 |
| 动态复权/真实价格 | `set_option('use_real_price', True)` | 常规股票策略建议开启。 |
| 避免未来数据 | `set_option('avoid_future_data', True)` | 常规回测建议开启。 |
| 成交量比例 | `set_option('order_volume_ratio', value)` | 用于限制订单成交量。 |
| 滑点 | `set_slippage` | 不设置时系统有默认滑点。 |
| 交易成本 | `set_order_cost` | 用于模拟佣金、印花税等。 |
| 关闭缓存 | `disable_cache()` | 仅在内存压力严重时考虑。 |

## 数据获取能力

| 场景 | 首选 API | 返回形态/风险 |
| --- | --- | --- |
| 单标的多字段历史 | `attribute_history` | 默认 DataFrame；日线不含当天。 |
| 多标的单字段历史 | `history` | DataFrame 或 `df=False` dict。 |
| 指定区间行情 | `get_price` | 多标的建议 `panel=False`。 |
| 当前行情状态 | `get_current_data` | 过滤停牌、ST、涨跌停常用。 |
| 财务估值数据 | `get_fundamentals`、`get_valuation` | 注意默认日期在研究/回测不同。 |
| 指数成分 | `get_index_stocks` | 支持历史任意时刻，降低幸存者偏差。 |
| 行业/概念成分 | `get_industry_stocks`、`get_concept_stocks` | 用于股票池。 |
| Tick/Bar | `get_ticks`、`get_bars` | Tick 需要权限和对应回测频率。 |

## 交易能力

| 场景 | API | 说明 |
| --- | --- | --- |
| 调整到目标市值 | `order_target_value` | 组合调仓最常用。 |
| 调整到目标数量 | `order_target` | 适合明确股数/合约数。 |
| 按金额买卖 | `order_value` | 正数买入，负数卖出。 |
| 按数量买卖 | `order` | 更底层。 |
| 撤单 | `cancel_order` | 配合未完成订单查询。 |
| 查询未完成订单 | `get_open_orders` | 日终未完成订单会撤销。 |

## 文件与研究环境边界

| 能力 | API | 边界 |
| --- | --- | --- |
| 读私有文件 | `read_file(path)` | 读的是聚宽研究/私有空间，不是本地电脑。 |
| 写私有文件 | `write_file(path, content)` | 写入后可在研究模块看到。 |
| 自定义库 | 研究根目录 `.py` 文件 | 暂不支持子目录 import。 |
| 创建回测 | `create_backtest` | 研究环境 API，不用于普通回测策略。 |

## 资产类别分支

- A 股/ETF：使用标准行情、财务、交易 API。
- 期货：需要期货账户、参考标的、保证金、`side`、`pindex`、平今/平昨等处理。
- Tick：需要 Tick 权限，并使用 Tick 频率回测。
- 融资融券：需要初始化融资融券账户并使用专用 API。
- 多账户/组合：使用子账户和 `pindex` 管理。

## Agent 使用提示

当用户说“写一个聚宽策略”时，优先读取：

1. [[domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范|聚宽策略写作与回测兼容规范]]
2. 本页
3. [[domains/量化交易/01-聚宽/03-聚宽策略报错与排查|聚宽策略报错与排查]]

需要具体 API 签名时，再检索 `raw/api/joinquant/joinquant-api-2026-06-19.md`。
