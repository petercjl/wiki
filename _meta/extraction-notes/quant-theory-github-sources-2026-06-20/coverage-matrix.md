---
title: GitHub 量化理论资料 coverage matrix
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, coverage, quant-trading]
sources:
  - raw/github/quant-theory-github-sources-2026-06-20/
status: active
---

# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| S1-U1 | Alphalens README | Alpha factor performance analysis | 因子研究入口 | `02-选池、信号与组合构建.md` | formalized | 用于定义 ETF 选池/信号验证，而非直接回测收益。 |
| S1-U2 | Alphalens README | Returns, IC, turnover, grouped analysis | 信号评估维度 | `02-选池、信号与组合构建.md`, `04-策略评估指标与归因.md` | formalized | 转写为选池/信号的第一层评估清单。 |
| S2-U1 | Pyfolio README | Portfolio performance and risk tear sheet | 策略结果解释 | `04-策略评估指标与归因.md` | formalized | 转写为结果分析页面结构。 |
| S3-U1 | Qlib README | qrun covers dataset, model, backtest, evaluation | 研究流程 | `01-策略收益来源分解.md` | formalized | 转写为量化研究流水线。 |
| S3-U2 | Qlib README | without-cost vs with-cost performance | 成本敏感性 | `04-策略评估指标与归因.md`, `03-买卖器、执行与风控.md` | formalized | 用于强调成本不可省略。 |
| S4-U1 | Qlib benchmark README | Alpha evaluated by correlation with future return and portfolio total return | Alpha 两层验证 | `02-选池、信号与组合构建.md` | formalized | 直接支撑“先验证选池/信号，再上买卖器”。 |
| S5-U1 | PyPortfolioOpt README | Mean-variance, Black-Litterman, shrinkage, HRP | 组合构建方法 | `02-选池、信号与组合构建.md` | formalized | 作为组合构建方法菜单。 |
| S5-U2 | PyPortfolioOpt README | Estimation error and in-sample zero-weight risk | 过拟合风险 | `02-选池、信号与组合构建.md`, `05-避免过拟合与回测陷阱.md` | formalized | 对应 ETF 池权重优化不要过度精细。 |
| S6-U1 | ml4t/backtest README | Event-driven, point-in-time correctness, no look-ahead | 回测真实性 | `03-买卖器、执行与风控.md`, `05-避免过拟合与回测陷阱.md` | formalized | 对应聚宽回测取数和执行约束。 |
| S6-U2 | ml4t/backtest README | stop-loss, take-profit, trailing stops, drawdown limits | 风控执行 | `03-买卖器、执行与风控.md` | formalized | 写成买卖器职责边界。 |
| S6-U3 | ml4t/backtest README | no intrabar stop simulation, calendar overnight assumptions | 回测限制 | `03-买卖器、执行与风控.md` | formalized | 提醒不要过度相信日线止损精度。 |
| S7-U1 | purged CV README | purge, embargo, walk-forward, CPCV | 防泄漏验证 | `05-避免过拟合与回测陷阱.md` | formalized | 转写为时间序列验证原则。 |
| S7-U2 | purged CV README | PBO, probabilistic/deflated Sharpe, effective trials | 选择偏差 | `05-避免过拟合与回测陷阱.md`, `04-策略评估指标与归因.md` | formalized | 对应参数搜索和多策略比较。 |
| S1-S7-NAV | GitHub repository navigation, install commands, badges | 项目导航/安装噪声 | raw-only evidence | `raw/github/quant-theory-github-sources-2026-06-20/` | raw-only | 保留 raw；对 Peter 当前知识目标无正式入库价值。 |
