---
title: 市场状态识别与策略自适应资料包 knowledge unit inventory
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, quant-trading, research]
sources:
  - _meta/extraction-notes/regime-adaptation-sources-2026-06-20/source-inventory.md
status: active
---

# Knowledge Unit Inventory

| unit_id | knowledge_unit | target_pages | disposition |
| --- | --- | --- | --- |
| KU-01 | 市场状态是收益均值、波动率、相关性、序列相关、流动性和尾部风险等统计性质的阶段性变化。 | `13-市场状态识别与策略失效.md` | formalized |
| KU-02 | 状态标签可以按方向、波动、风险偏好、normal/crash、calm/transition/crisis 等方式定义。 | `13-市场状态识别与策略失效.md` | formalized |
| KU-03 | HMM、GMM、KMeans、change point 和 Jump Model 是状态识别的主要方法谱系。 | `13-市场状态识别与策略失效.md` | formalized |
| KU-04 | HMM 把市场状态视为隐藏变量，通过状态转移概率和发射概率解释可观察收益/特征。 | `13-市场状态识别与策略失效.md` | formalized |
| KU-05 | 状态识别特征包括收益、波动、回撤、相关性、广度、流动性和尾部风险。 | `13-市场状态识别与策略失效.md` | formalized |
| KU-06 | 状态检测可以作为风险管理器，在不利状态下降仓、禁开仓或停止交易。 | `14-状态自适应策略与动态资产配置.md` | formalized |
| KU-07 | Strategy router 根据状态启用趋势、均值回复、防御等不同策略，避免策略和环境错配。 | `14-状态自适应策略与动态资产配置.md` | formalized |
| KU-08 | Expert models 为不同状态训练不同模型，但需要严格 walk-forward，避免样本切小后的过拟合。 | `14-状态自适应策略与动态资产配置.md` | formalized |
| KU-09 | Dynamic allocation 将状态映射到资产权重，例如风险状态下提高债券、黄金或现金。 | `14-状态自适应策略与动态资产配置.md` | formalized |
| KU-10 | No-trade regime 是合法动作；极端波动或不可预测状态下，不交易可能优于换复杂模型。 | `14-状态自适应策略与动态资产配置.md` | formalized |
| KU-11 | 现金替代资产是降仓后的第二层问题，现金、短债、长债、黄金和低波权益各有不同风险。 | `14-状态自适应策略与动态资产配置.md` | formalized |
| KU-12 | 状态策略必须测试交易延迟、交易成本、状态持续性和切换次数。 | `15-策略失效监控与滚动验证.md` | formalized |
| KU-13 | Walk-forward 验证要求只用过去数据选择规则，再在未来验证。 | `15-策略失效监控与滚动验证.md` | formalized |
| KU-14 | 固定长周期是主裁判，但还必须拆年度、拆状态、拆资产/类别贡献。 | `15-策略失效监控与滚动验证.md` | formalized |
| KU-15 | 策略失效处理应先判断短期回撤、状态错配、执行成本、参数脆弱、选池/信号失效，再决定继续、暂停或转为组合组件。 | `15-策略失效监控与滚动验证.md` | formalized |
| KU-16 | HMM 与神经网络、Black-Litterman 或 RL 可以组合，但复杂系统必须被样本外、延迟和成本约束。 | `14-状态自适应策略与动态资产配置.md` | merged |
| KU-17 | MDPI regime-switching factor investing 页面下载受限，未进入正式知识。 | `omission-audit.md` | unresolved |

