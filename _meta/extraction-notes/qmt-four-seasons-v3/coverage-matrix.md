---
title: QMT四季发财v3 覆盖矩阵
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [coverage, quant-trading, joinquant]
sources:
  - raw/quant-strategies/qmt-four-seasons-v3/qmt四季发财v3-r3-summary.py
  - raw/quant-strategies/qmt-four-seasons-v3/analysis_summary-r3.json
status: active
---

# QMT四季发财v3 覆盖矩阵

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| QMT-001 | strategy script metadata | 策略来源、名称、版本、社区来源和 `strategy_metadata` | provenance | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 保留策略身份、版本和来源边界 |
| QMT-002 | strategy parameters | ETF 池、持仓数量、lookback、短期动量、RSI、ATR、止损、min_money | rule/parameter | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 参数是复现策略的核心 |
| QMT-003 | score formula | 长期动量年化收益 * R²，25 日窗口、线性递增权重 | signal | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 策略核心信号假设 |
| QMT-004 | filters | 短期动量、RSI、近 3 日单日跌幅、异常高分过滤；MA/MACD/成交量/布林带默认关闭 | filter logic | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 解释候选为何被接受/拒绝 |
| QMT-005 | rebalance and execution | 14:29 调仓，09:30 持仓检查，09:35 ATR 检查，只持有 1 只 ETF | execution | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 与导出交易记录对齐 |
| QMT-006 | risk controls | 固定止损、ATR 动态止损、防御 ETF、停牌/涨跌停/T+1/min_money 检查 | risk | `01-QMT四季发财ETF轮动策略案例.md`, `04-聚宽社区策略取证与日志瘦身方法.md` | formalized | 分成策略风险和平台执行风险 |
| QMT-007 | r2 failure | 旧日志因 candidate 明细过多被 100000 条上限截断，且发现 `rsi_info` 未赋值异常 | failure mode | `04-聚宽社区策略取证与日志瘦身方法.md` | formalized | 转化为日志瘦身原则 |
| QMT-008 | r3 logging | summary-only 日志：9503 条 JQ_AUDIT，HTML unescape 后 0 解析失败，未截断 | evidence method | `04-聚宽社区策略取证与日志瘦身方法.md` | formalized | 可复用为 future skill 默认模板 |
| QMT-009 | performance | 2020-2025 总收益、年化、波动、Sharpe、最大回撤、年度收益 | backtest evidence | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 绩效结论必须带区间和口径 |
| QMT-010 | trade data | 876 笔订单、439 买、437 卖、手续费 111.71 万、卖出胜率 53.09% | trade evidence | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 用交易导出而不是日志承载结果 |
| QMT-011 | attribution | 主要正贡献：软件ETF、南方原油、黄金ETF、创业板ETF、日经ETF等；主要负贡献：法国ETF等 | attribution | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 标的贡献用于理解收益来源 |
| QMT-012 | execution defects | 3 次可用资金不足订单失败，末期可用现金可轻微为负 | caveat | `01-QMT四季发财ETF轮动策略案例.md`, `04-聚宽社区策略取证与日志瘦身方法.md` | formalized | 不能静默包装成“可实盘” |
| QMT-013 | local project artifacts | 完整 zip、日志、CSV、分析脚本过程保存在 QuantTrading 项目目录 | source preservation | raw plus source-profile | raw-only | wiki raw 保存核心摘要和派生数据；完整大文件保留在项目归档目录 |
| QMT-014 | actual ETF universe | 实际使用的 26 只 ETF 池按商品、国际、港股、A股、防御资产分组 | universe | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 区分实际 `g.etf_pool` 和备用池 |
| QMT-015 | buy rules | 14:29 选择第一名或防御 ETF、目标金额为总资产、5% 偏离才调仓、100 股整数倍和最小交易额 | buy/execution | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 回答“什么时候买、怎么买” |
| QMT-016 | sell rules | 换仓卖出、固定止损卖出、ATR 止损卖出、跌停/T+1/closeable 限制 | sell/risk | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 回答“什么时候卖、怎么卖” |
| QMT-017 | take-profit behavior | 无显式止盈，盈利退出主要来自排名变化、换仓和再平衡 | exit logic | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 避免误判为固定止盈策略 |
| QMT-018 | enabled vs implemented modules | MA/MACD/成交量/布林带有实现但默认关闭 | implementation caveat | `01-QMT四季发财ETF轮动策略案例.md` | formalized | 防止把未启用模块纳入收益解释 |
