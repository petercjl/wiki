---
title: GitHub 量化基础资料 coverage matrix
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, coverage, quant-trading]
sources:
  - raw/github/quant-foundations-github-sources-2026-06-20/
status: active
---

# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | Qlib / ML4T README | 数据、模型、回测、执行的完整量化工作流 | 研究总框架 | `01-量化交易全景与研究对象.md`, `12-量化研究工作流与实验纪律.md` | formalized | 从工具链抽象为研究流程。 |
| S2 | Zipline / Backtrader / bt | 事件驱动回测、broker、订单、佣金、滑点、交易日历 | 回测真实性 | `02-市场、资产与交易制度.md`, `08-交易执行、成本与市场冲击.md`, `09-回测系统与真实性检查.md` | formalized | 作为回测系统能力清单。 |
| S3 | Qlib / ML4T | 数据来源、特征、模型训练、任务定义 | 数据与特征工程 | `03-数据体系与特征工程.md` | formalized | 点时正确和特征/标签区分为核心。 |
| S4 | Empyrical / ffn / Riskfolio | 收益、最大回撤、alpha/beta、Sharpe、Sortino、VaR/CVaR | 收益风险统计 | `04-收益、风险与统计基础.md`, `10-绩效评估、归因与报告.md` | formalized | 指标体系化。 |
| S5 | ML4T / Qlib | 策略从数据、alpha、模型到执行 | 策略类型 | `05-策略类型与收益假设.md` | formalized | 补充股票、ETF、期货、机器学习等策略类型。 |
| S6 | Alphalens / Qlib | factor tear sheet、returns、IC、turnover、grouped analysis | 因子验证 | `06-因子、信号与Alpha研究.md` | formalized | 从 ETF 扩展为通用 alpha 研究。 |
| S7 | PyPortfolioOpt / Riskfolio / bt | 均值方差、Black-Litterman、HRP/HERC、多风险度量、约束 | 组合构建 | `07-组合构建与仓位管理.md` | formalized | 强调估计误差和约束。 |
| S8 | Backtrader / Qlib | 订单类型、成本、滑点、市场冲击、执行算法 | 执行层 | `08-交易执行、成本与市场冲击.md` | formalized | 连接信号和真实成交。 |
| S9 | Pyfolio / Empyrical / ffn | tear sheet、风险指标、绩效分析 | 报告归因 | `10-绩效评估、归因与报告.md` | formalized | 形成报告模板。 |
| S10 | purged-cross-validation | purge、embargo、walk-forward、PBO/DSR、标签泄漏 | 防过拟合 | `11-过拟合、数据泄漏与样本外验证.md` | formalized | 时间序列验证规则。 |
| S11 | all repos | install badges, CI badges, contributor/license text | 项目元信息 | raw-only | raw-only | 保留 raw；不构成量化基础知识。 |

