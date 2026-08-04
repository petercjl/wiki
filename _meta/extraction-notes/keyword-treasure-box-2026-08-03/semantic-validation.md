# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: structured DingTalk document text + image-contained Chinese text and visual relations
- Evidence sources: content.md, document-package.json, six original PNG files, surrounding headings, repeated labels across images
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | IMG-01 | product-concept | 搜索关键词=消费者搜索意图=用户购买意向 | 搜索关键词承载消费者搜索意图与购买意向 | 图片标题 + 意向层级示意 + 周边解释 | high | accepted-as-is | 保留概念关系，但不把“购买意向越来越强”写成对个体用户的确定性结论 |
| A02 | IMG-02 | feature-name | 自选词:精准匹配 / 自选词:广泛匹配 / 关键词组合 / 流量智选词包 | 自选词精确匹配、自选词广泛匹配、关键词组合、流量智选词包 | 四类并列标签 + IMG-03 重复标签 | high | accepted-as-is | 作为四种官方投放机制 |
| A03 | IMG-03 | feature-claim | 完全基于卖点主题词进行中心词扩展，匹配流量更精准 | 基于卖点主题词进行中心词扩展；官方称匹配流量更精准 | 标题、说明和保湿套装示例 | high | accepted-as-is | 将“更精准”标注为官方机制说明，不承诺效果 |
| A04 | IMG-03/IMG-05 | metrics | 高点击、高转化、点击成本低 | 高点击、高转化、低点击成本词 | 两张图重复出现 | high | accepted-as-is | 只作为系统筛选方向，来源未给阈值和计算口径 |
| A05 | IMG-04 | bidding | 前期按词包建议出价为初始价格，后期根据预算、投放效果优化调整 | 建议出价用于初始测试，后续按预算和效果调整 | 图片“出价”区 | high | accepted-as-is | 不把建议出价视为保效价格 |
| A06 | IMG-05 | stage-label | 新品期 / 成长期 / 爆款期 | 新品期、成长期、爆款期 | 阶段策略表表头 | high | accepted-as-is | 保留三阶段框架；来源没有定义阶段划分阈值 |
| A07 | IMG-05 | feature-name | 捡漏 / 类目优选 / 好词优选 | 捡漏、类目优选、好词优选 | 阶段目标行 | high | accepted-as-is | 保留官方标签，提醒后台名称可能更新 |
| A08 | content.md | matching-rule | 完全相同或者是同义词 | 完全相同或同义词 | 结构化正文 + 正反示例 | high | accepted-as-is | 原样保留精确匹配定义和示例 |
| A09 | content.md | matching-rule | 相同或者与之相关 | 相同或相关 | 结构化正文 + 正反示例 | high | accepted-as-is | 原样保留广泛匹配定义和示例 |
| A10 | IMG-06 | decision-rule | 预算不多/宝贝销量差；流量瓶颈/宝贝销量上升期；不知道投放什么词 | 三类商家痛点及对应方案 | 图中连接关系 + 前文四类机制 | high | accepted-as-is | 转写为决策表，并注明属于官方建议而非强制规则 |

## Validation Notes

- 6 张图片均以原始分辨率人工检查，未依赖 OCR 文本作为唯一依据。
- 文档标题中的“覆盖全部消费者搜索意图”是产品方法表述；正式页解释为四类机制构成分层覆盖，不写成字面上的 100% 覆盖保证。
- “新品期、成长期、爆款期”没有数值划分标准，正式页不自行补造销量或日期阈值。
