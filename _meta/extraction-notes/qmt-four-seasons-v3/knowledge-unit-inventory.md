---
title: QMT四季发财v3 Knowledge Unit Inventory
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [knowledge-unit-inventory, quant-trading, strategy]
sources:
  - _meta/extraction-notes/qmt-four-seasons-v3/source-inventory.md
status: active
---

# QMT四季发财v3 Knowledge Unit Inventory

| unit_id | unit_type | unit | formal_target | disposition |
| --- | --- | --- | --- | --- |
| QMT-001 | provenance | QMT四季发财v3 的社区策略来源、JoinQuant 平台、r3 summary 审计版本 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-002 | parameter | ETF 池 26 只、单标的持仓、lookback 25、短期动量 10、RSI 6/95、ATR 14/2、止损 0.95、min_money 5000 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-003 | formula | `score = annualized_returns * r_squared`，用趋势收益和趋势稳定性共同排序 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-004 | filter | 短期动量、RSI、近三日跌幅、异常高分过滤；MA/MACD/成交量/布林带默认关闭 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-005 | execution | 09:30 持仓检查、09:35 ATR 检查、14:29 ETF 轮动调仓 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-006 | risk | 固定止损、ATR 止损、防御 ETF、停牌/涨跌停/T+1/min_money 检查 | strategy page + logging playbook | formalized |
| QMT-007 | failure | r2 全量候选日志导致 100000 条导出上限截断，`rsi_info` 未赋值暴露为策略行为问题 | `04-聚宽社区策略取证与日志瘦身方法.md` | formalized |
| QMT-008 | logging contract | r3 summary-only 事件合同和 HTML unescape 解析注意事项 | `04-聚宽社区策略取证与日志瘦身方法.md` | formalized |
| QMT-009 | performance | 2020-2025 总收益 2538.85%、年化 72.61%、最大回撤 -20.03%、年度收益 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-010 | trading metrics | 876 订单、439 买、437 卖、手续费 111.71 万、卖出行胜率 53.09% | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-011 | attribution | 软件ETF、南方原油、黄金ETF等正贡献；法国ETF等负贡献 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-012 | caveat | 3 次可用资金不足订单失败、高换手、集中持仓、参数稳健性和非投资建议边界 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-013 | source retention | 完整 zip/log/CSV 保留在 QuantTrading 项目，wiki raw 保留核心可复用源 | source profile + omission audit | raw-only |
| QMT-014 | universe | 实际 ETF 池按商品、国际、港股、A股宽基/行业、防御资产分组 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-015 | buy strategy | 最高 score 候选、score 阈值、防御 ETF、目标总资产、5% 容差、100 股取整、最小交易额 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-016 | sell strategy | 目标外持仓卖出、固定止损、ATR 止损、跌停/T+1/可卖数量保护 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-017 | take profit | 无显式止盈，盈利退出依赖趋势轮动和换仓 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
| QMT-018 | module activation | 区分实际启用模块与仅实现但关闭的 MA/MACD/成交量/布林带 | `01-QMT四季发财ETF轮动策略案例.md` | formalized |
