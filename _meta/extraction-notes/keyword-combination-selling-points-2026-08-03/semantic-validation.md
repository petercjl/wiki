# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: mixed structured text and manually inspected image text
- Evidence sources: content.md, tables.json, images 01-07, surrounding document context
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | IMG-01/02 | UI-label | 关键词组合 | 关键词组合 | 页面标签 + 正文入口 | high | accepted-as-is | 作为 2026-08-03 后台快照，执行前复核 |
| A02 | 正文 + IMG-03 | metric-formula | 流量放大系数=整个卖点词包的覆盖PV/卖点主题词精确匹配下的覆盖PV | 词包总覆盖 PV ÷ 主题词精确匹配覆盖 PV | 正文定义 + 图中 PV80、PV60/40/20 算例 | high | accepted-as-is | 保留公式和 2.5 算例，注明是覆盖估算而非成交提升 |
| A03 | IMG-04 | percentage | 20%+ 展现、点击、成交笔数平均提升；5%+ CTR平均提升 | 官方升级宣传口径 | 原图可见文字，无实验样本、周期与对照口径 | high | accepted-as-is | 仅作为官方宣称，不转写为保证或独立实测 |
| A04 | IMG-06 | operational-step | 前期按词包建议出价为初始价格，后期优化调整 | 先参考建议出价测试，再按预算与真实效果调整 | 原图 + 正文上下文 | high | accepted-as-is | 明确建议价不保效 |
| A05 | IMG-07 | date-and-contact | 此二维码365天内有效（2024-09-27前） | 二维码已过来源标注有效期 | 原图明确日期 | high | excluded-from-formal | 原图 raw-only，不提供过期加群入口 |
| A06 | IMG-01/02 | count | 词包（8/8） | 当时界面示例中的选中数量 | 两张截图一致 | high | accepted-as-is | 不固化为长期数量上限 |

## Systematic Variant Check

- 全文检索“关键词组合、卖点主题词、流量放大系数、预估展现量、建议出价、20%+、5%+、CTR、群号、二维码”。
- 正式页统一使用“卖点主题词”“流量放大系数”；不把宣传性“更精准、更优”改写成可保证结果。
- 原始结构化正文和图片保持未改动。

