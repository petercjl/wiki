---
title: 市场状态识别与策略自适应资料包 coverage matrix
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, quant-trading, research]
sources:
  - _meta/extraction-notes/regime-adaptation-sources-2026-06-20/source-inventory.md
status: active
---

# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| KU-01 | QuantStart intro, QuestDB HMM | Regime 是市场收益均值、波动、相关性、序列相关、尾部风险等统计性质的阶段性变化。 | definition | `13-市场状态识别与策略失效.md` | formalized | 作为市场状态定义。 |
| KU-02 | LSEG README/article | 状态分类可以是 boom/bust、volatility high/low/mid、risk-on/risk-off、normal/crash。 | taxonomy | `13-市场状态识别与策略失效.md` | formalized | 汇总为状态标签谱系。 |
| KU-03 | Sakeeb91, LSEG, QuestDB | HMM/GMM/KMeans/change point 都可用于状态识别，方法假设不同。 | method map | `13-市场状态识别与策略失效.md` | formalized | 形成方法对比表。 |
| KU-04 | QuantStart HMM intro | HMM 用隐藏状态生成可观察收益/特征，包含转移概率和发射概率。 | concept | `13-市场状态识别与策略失效.md` | formalized | 作为 HMM 基本解释。 |
| KU-05 | QuestDB ML | 特征包括收益分布、波动、成交量、相关性、微结构、技术指标、宏观/替代数据。 | feature engineering | `13-市场状态识别与策略失效.md` | formalized | 形成特征清单。 |
| KU-06 | QuantStart QSTrader | 状态检测可作为 risk manager，在高波动状态下禁止或减少交易。 | application | `14-状态自适应策略与动态资产配置.md` | formalized | 作为策略开关模式。 |
| KU-07 | QuantInsti | 可为不同状态训练专门模型，并用当前状态选择对应模型。 | application | `14-状态自适应策略与动态资产配置.md` | formalized | 作为专家模型模式。 |
| KU-08 | regime-allocation, arXiv HMM-RL | 状态可驱动多资产配置，如稳定状态持股、压力状态转债券/黄金。 | application | `14-状态自适应策略与动态资产配置.md` | formalized | 作为动态资产配置模式。 |
| KU-09 | regime-aware-dynamic-allocation | 状态识别可连接组合优化、walk-forward、RL，但复杂度越高越需要样本外约束。 | caveat | `14-状态自适应策略与动态资产配置.md` | formalized | 作为复杂系统边界。 |
| KU-10 | arXiv Jump Model | Jump Model 用跳跃惩罚增强状态持续性，减少频繁切换。 | method | `13-市场状态识别与策略失效.md`, `15-策略失效监控与滚动验证.md` | formalized | 作为 HMM 之外的稳健状态方法。 |
| KU-11 | arXiv Jump Model, HMM-RL | 交易延迟、交易成本、样本外测试是状态策略验证的关键。 | validation | `15-策略失效监控与滚动验证.md` | formalized | 形成验证纪律。 |
| KU-12 | RobotWealth | 极端波动状态可能难以预测，最优动作可能是不交易。 | caveat | `14-状态自适应策略与动态资产配置.md` | formalized | 作为 no-trade regime 原则。 |
| KU-13 | QuantInsti, Sakeeb91 | Walk-forward validation 是避免看未来和适应变化的核心流程。 | validation | `15-策略失效监控与滚动验证.md` | formalized | 形成滚动验证流程。 |
| KU-14 | Existing wiki + sources | 固定策略失效通常来自市场分布漂移、收益假设边界、状态错配、执行成本或过拟合。 | synthesis | `15-策略失效监控与滚动验证.md` | formalized | 结合现有知识综合。 |
| KU-15 | QuestDB, QuantStart, LSEG | 状态检测输出不应直接等同买卖信号，需转成风险预算、策略选择、资产配置或模型路由。 | design rule | `14-状态自适应策略与动态资产配置.md` | formalized | 作为设计原则。 |
| KU-16 | arXiv HMM-NN | HMM 可与神经网络、Black-Litterman、风险模型组合，但复杂系统更难证明泛化。 | caveat | `14-状态自适应策略与动态资产配置.md` | merged | 合并进复杂模型边界。 |
| KU-17 | MDPI page | Regime-switching factor investing source could not be downloaded due HTTP 403. | unresolved | `omission-audit.md` | unresolved | Not used as formal evidence. |

