# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: structured text plus manually inspected UI screenshots
- Evidence sources: content.md, images 01-08, repeated UI labels, existing keyword-treasure-box page
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | IMG-02 | UI-label | 好词优选、捡漏、类目优选 | 三种流量购买目标 | 图中标签 + 正文逐项定义 | high | accepted-as-is | 保留当前标签，执行前复核后台 |
| A02 | IMG-05 | duration | 30/60/90天无展现关键词再移回收至流量智选 | 自动托管回收周期可选 30、60 或 90 天 | 图中单选项 + 无展现托管正文 | high | accepted-as-is | 作为 2026-08-03 UI 快照，不固化为永久选项 |
| A03 | 屏蔽词 FAQ | timing | 第二天才会正式生效 | 屏蔽设置次日生效 | 正文两处重复 + IMG-06说明“设置后隔天生效” | high | accepted-as-is | 明确当天仍可能有流量 |
| A04 | 屏蔽词 FAQ | sampling | 暂时选取其中20%的词进行计算展示 | 屏蔽词较多时可能只展示其中20%的价值数据 | 正文解释 | high | accepted-as-is | 不解读为随机抽样或统计代表性 |
| A05 | 中心/精准屏蔽 | limit | 中心10个、精准50个 | 基础数量上限 10/50 | 正文 + IMG-06/07 UI 数量 | high | accepted-as-is | 标记为当前快照 |
| A06 | 精准词额度 | money-and-limit | 近30天>2000元→100个；>10000元→200个 | 消耗门槛对应可申请额度 | 正文门槛 + 客服工单路径 | high | accepted-as-is | 不是自动扩容，执行前核验资格 |
| A07 | IMG-08 | stage-strategy | 新品/成长/爆款三阶段 | 按商品经营阶段调整目标和出价 | 图中完整策略 + 既有官方总览 | high | accepted-as-is | 来源未给阶段阈值，不自行补造 |

## Systematic Variant Check

- 全文检索：流量智选、好词优选、捡漏、类目优选、潜力词、无展现词托管、屏蔽词、近7天、近30天、20%、第二天、10/50/100/200、2000/10000。
- 未发现术语冲突；“精准词屏蔽”与既有“精准/精确匹配”区分为后台标签与匹配概念。
- 原始结构化正文和图片保持不变。

