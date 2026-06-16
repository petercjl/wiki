# Omission Audit｜财税股权 28 期课程知识系统

## Raw-only / Omitted Types

| type | disposition | reason |
| --- | --- | --- |
| 主持串场、签到、课间休息、拍照提醒 | raw-only | 课堂组织信息，不形成可复用知识 |
| 课程销售、俱乐部招募、价格优惠、报名流程 | raw-only | 营销信息，不进入正式知识 |
| 现场寒暄、掌声、情绪性评价 | raw-only | 无知识增量 |
| 明显 ASR 错字、重复口头禅、无法还原片段 | omitted-with-reason | 语义不可稳定还原 |
| 视频台词、戏剧片段 | raw-only | 仅课堂调动氛围，非财税股权知识 |
| 具体企业/个人隐私细节 | merged/omitted | 方法价值保留，身份信息匿名化 |

## High-risk Claims Requiring Verification

- “低于 90% 申报一定跳风险”：正式页改写为经验性风险阈值，执行前需复核当地税务口径。
- 刷单、不申报、收入性质转换、税收洼地、代持分散风险等内容：只作为风险警示，不作为操作建议。
- 小规模、一般纳税人、小型微利企业、个体户核定、专票抵扣、技术转让税收优惠等政策口径：正式页均标注需按最新法规复核。
- 公司持公司分红免税、家族公司/控股公司架构、有限合伙平台、代持协议、控制权比例：需结合法律和税务专业意见。

## Anchor Sampling Result

- 案例锚点：已覆盖佛山家具、长沙羽绒服、义乌 200 万应收、四平台边际贡献、仓库盗货、运营仅退款套货、代销被否、渔具转型、跨境运营 4000 万、良品铺子、石家庄 200 万供应链绑定、雷士照明、HK 美妆工具、河北低价模型、荣美、钢制家具收购工厂等案例。
- 数字锚点：已覆盖 90%、200 万、500 万、300 万、13%、6%、20%、67/51/34、15%、40% 到 30%、50 万固定成本、5%/18% 边际贡献、10% 净利、1.98 亿、1.27 亿、6.7%、32 人、73% 退货率、792 万出生人口等数字，并在正式页标注适用边界。
- 后半段结论：战略、预算、竞争战略、财务指标、ROE、存货周转、财务团队、财务 BP、月度经营分析和组织能力已拆入页面 21-25。

## Recompile Omission Check

| sampled anchor | disposition | target |
| --- | --- | --- |
| D1 上午课间、合照、外卖提醒 | raw-only | `ALL-KU001` |
| 财税俱乐部收费、申请表、招生名额 | raw-only | `ALL-KU003` |
| 无法还原的会场闲聊和 ASR 残片 | omitted-with-reason | `ALL-KU002` |
| 代销、刷单、税收洼地类高风险做法 | formalized as warning only | `17-subject-splitting-consignment-and-income-nature.md` |
| 政策性税率和优惠口径 | unresolved/current verification required | pages 15-17, 24, 27 |
