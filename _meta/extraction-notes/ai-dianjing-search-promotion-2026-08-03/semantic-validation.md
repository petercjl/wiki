# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: CDP structured document extraction + original UI images
- Evidence sources: `document-package.json`, `extracted-text.md`, 16 original PNG images, repeated FAQ/context, visible document title
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

结构化文档包直接来自页面已经加载的官方数据，正文无需 OCR。为防止接口字段、UI 标签、数量和时间限制在解析中丢失，仍按机器提取来源执行高风险锚点校验。原始包与纯文本保持不变。

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 文档标题、全篇 | platform-or-product | AI点睛 | AI点睛 | 文档标题 + 16 张 UI 图中的功能标签 | high | accepted-as-is | 统一使用“AI点睛” |
| A02 | 操作步骤第一步、IMG-03 | UI path | 关键词推广-自定义推广 | 关键词推广—自定义推广 | 结构化正文 + IMG-03 后台截图 | high | accepted-as-is | 作为开通入口 |
| A03 | 操作步骤第二步、FAQ Q2 | feature constraint | 开启后仅支持智能出价 | 开启后仅支持智能出价 | 正文重复说明 + IMG-03/04 的功能入口上下文 | high | accepted-as-is | 写入前置条件和限制表 |
| A04 | 搜索需求管理 | limit | 建议新建时聚焦 3-5 个核心需求 | 建议新建时聚焦 3–5 个核心需求 | 结构化正文 + 需求多选 UI 图 | high | accepted-as-is | 写入首次设置建议 |
| A05 | 新增需求核心说明 | duration | 追加后建议观察2～3天 | 追加后建议观察 2–3 天 | 结构化正文 + 操作顺序上下文 | high | accepted-as-is | 写入稳定期规则 |
| A06 | 删除搜索需求 | duration | 计划投放满3天后 | 计划投放满 3 天后 | 结构化正文 + IMG-14 投放报告入口 | high | accepted-as-is | 作为删除前评估门槛 |
| A07 | 投放指南、FAQ Q3 | scope/risk-boundary | 屏蔽词生效在计划粒度 | 屏蔽词在计划粒度生效 | 正文两次重复 + IMG-10 屏蔽词设置标签 | high | accepted-as-is | 明确不影响其他计划 |
| A08 | FAQ Q9 | reporting metric | 搜索词数据延迟一般不超过5分钟 | 搜索词数据延迟一般不超过 5 分钟 | 官方 FAQ + 搜索需求/报表 UI | high | accepted-as-is | 写入报表异常判断 |
| A09 | FAQ Q10、IMG-15 | reporting rule | 关键词报表中记录为单元汇总数据 | 关键词报表以单元汇总记录 AI点睛 | 官方 FAQ + IMG-15 关键词数据明细 | high | accepted-as-is | 写入报表口径表 |
| A10 | FAQ Q10 | reporting negation | 人群报表中不记录ai点睛的人群数据 | 人群报表不记录 AI点睛人群数据 | 官方 FAQ + 与关键词报表对照 | high | accepted-as-is | 保留否定语义 |
| A11 | FAQ Q11 | feature constraint | 存量AI点睛计划功能无法关闭 | 存量 AI点睛计划不能关闭 | 官方 FAQ + 新建/存量对照 | high | accepted-as-is | 建议调优或暂停，不编造关闭入口 |
| A12 | FAQ Q12 | limit | 一次生成最多10个，一个计划最多20个 | 单次最多生成 10 个，一个计划最多 20 个 | 官方 FAQ + 全文需求管理上下文 | high | accepted-as-is | 写入关键参数表 |
| A13 | 负向案例说明 | risk-boundary | AI投放无法完全屏蔽排除流量 | AI 流量表达不能完全替代屏蔽词 | 正文负向案例 + 屏蔽词操作说明 | high | accepted-as-is | 不承诺完全排除，严格排除用计划级屏蔽词 |
| A14 | 报表与搜索需求 UI | UI labels | 方案解析 / AI点睛设置 / 投放报告 | 方案解析 / AI点睛设置 / 投放报告 | 结构化正文 + IMG-06/07/09/13/14 | high | accepted-as-is | 保持官方 UI 标签 |

## Systematic Checks

- 全文搜索 `AI点睛`、`智能出价`、`屏蔽词`、`2～3天`、`3天`、`5分钟`、`10个`、`20个`，正式页均采用一致表述。
- `ai点睛` 等大小写差异只在解释层统一为 `AI点睛`，未修改 raw。
- 所有否定边界保留：不能完全排除、存量计划不能关闭、人群报表不记录。
- 未发现需要标记 `unresolved` 的高风险锚点。

