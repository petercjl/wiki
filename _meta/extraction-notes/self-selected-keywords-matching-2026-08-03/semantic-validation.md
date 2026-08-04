# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: structured DingTalk document text + image-contained UI labels and visual relations
- Evidence sources: content.md, document-package.json, five original PNG files, repeated labels across text and images, existing keyword-treasure-box page
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | title/content.md | feature-name | 精准匹配 | 精准匹配（同模块另一份官方资料写作“精确匹配”） | 标题、正文、方括号示例 + 既有官方页 | high | accepted-as-is | 说明两种官方写法指向同一自选词匹配方案，执行以当前后台标签为准 |
| A02 | content.md/IMG-02 | UI marker | `[女连衣裙]` | 方括号表示精准匹配 | 结构化正文 + 投放列表截图 | high | accepted-as-is | 写入 UI 识别规则 |
| A03 | content.md/IMG-03 | UI marker | 女连衣裙 | 无方括号表示广泛匹配 | 结构化正文 + 投放列表截图 | high | accepted-as-is | 写入 UI 识别规则 |
| A04 | IMG-01 | UI path | 万相台无界版-关键词推广-添加更多关键词-关键词推荐 | 万相台无界版→关键词推广→添加更多关键词→关键词推荐 | 正文路径 + 截图箭头 | high | accepted-as-is | 原样保留路径并标记时效性 |
| A05 | IMG-01/IMG-04 | UI labels | 综合推荐词、精准引流词、类目优选词、行业机会词、助攻词 | 五类推荐词 | 截图标签 + 正文逐项定义 | high | accepted-as-is | 建立五类定义表 |
| A06 | content.md | attribution | MTA多触点归因 | MTA 多触点归因 | 结构化正文完整定义 | high | accepted-as-is | 仅保留平台归因定义，不解释为严格因果贡献 |
| A07 | IMG-01/IMG-04 | metric-field | 预估展现量、点击率、点击转化率、市场平均出价 | 推荐词辅助指标字段 | 两张截图重复 | high | accepted-as-is | 作为筛选参考；来源未给指标算法和更新时间 |
| A08 | IMG-01/IMG-04 | UI limit | 0/180 | 截图显示已添加关键词容量为 0/180 | 两张界面截图 | medium | accepted-as-is | 仅记录 2026-04-16 界面快照，不写成永久上限 |

## Validation Notes

- 5 张原图均以原始分辨率检查；小图 IMG-02/03 与正文定义相互验证。
- “助攻词”是平台 MTA 归因下的贡献词，不等同于独立因果增量。
- 推荐词的“效果较好”“优质”“机会”均是系统筛选口径，正式页不承诺真实投放结果。
