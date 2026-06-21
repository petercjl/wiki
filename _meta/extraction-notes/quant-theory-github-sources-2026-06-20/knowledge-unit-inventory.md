---
title: GitHub 量化理论资料 knowledge unit inventory
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, knowledge-unit-inventory, quant-trading]
sources:
  - raw/github/quant-theory-github-sources-2026-06-20/
status: active
---

# Knowledge Unit Inventory

| unit_id | knowledge_unit | disposition | formal_target |
| --- | --- | --- | --- |
| KU-01 | 量化研究应拆成数据/宇宙、信号、组合、回测、评估等流水线，而不是直接调收益曲线。 | formalized | `01-策略收益来源分解.md` |
| KU-02 | Alpha 评估要先看信号与未来收益关系，再看由信号构建的组合收益。 | formalized | `02-选池、信号与组合构建.md` |
| KU-03 | 因子分析至少包含收益分组、IC、换手和类别/分组分析。 | formalized | `02-选池、信号与组合构建.md`, `04-策略评估指标与归因.md` |
| KU-04 | 组合绩效分析应形成 tear-sheet 式结构，覆盖收益、风险、交易、持仓和压力期。 | formalized | `04-策略评估指标与归因.md` |
| KU-05 | 成本前和成本后结果要分开评估，尤其是高换手策略。 | formalized | `03-买卖器、执行与风控.md`, `04-策略评估指标与归因.md` |
| KU-06 | 组合优化方法包括均值方差、Black-Litterman、收缩估计和 HRP，但输入估计误差会放大样本内最优风险。 | formalized | `02-选池、信号与组合构建.md` |
| KU-07 | 事件驱动回测、点时正确性和无前视偏差是策略回测可信度底线。 | formalized | `03-买卖器、执行与风控.md`, `05-避免过拟合与回测陷阱.md` |
| KU-08 | 止损、止盈、跟踪止损、组合回撤约束属于买卖器/执行层，不应替代信号验证。 | formalized | `03-买卖器、执行与风控.md` |
| KU-09 | 日线回测存在盘中止损模拟和隔夜/日历假设限制，不能过度相信止损精度。 | formalized | `03-买卖器、执行与风控.md` |
| KU-10 | 金融时间序列验证应避免标签重叠和序列相关泄漏，可使用 purge、embargo、walk-forward 等思想。 | formalized | `05-避免过拟合与回测陷阱.md` |
| KU-11 | 参数搜索越多，最优夏普越可能来自选择偏差；DSR/PBO 的思想应转化为搜索空间和失败版本记录。 | formalized | `05-避免过拟合与回测陷阱.md`, `04-策略评估指标与归因.md` |
| KU-12 | ETF 池必须历史时点可复现，不能把事后人工挑出的 ETF 池当作科学结论。 | formalized | `02-选池、信号与组合构建.md`, `05-避免过拟合与回测陷阱.md` |
| KU-13 | GitHub 安装命令、badge、导航链接、社区链接不构成 Peter 当前所需的理论知识。 | raw-only | `raw/github/quant-theory-github-sources-2026-06-20/` |

