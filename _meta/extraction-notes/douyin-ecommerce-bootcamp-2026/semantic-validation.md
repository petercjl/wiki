# Semantic Validation
- Status: passed
- Raw evidence preserved: yes
- Validation scope: mixed ASR + OCR
- Evidence sources: raw TXT/SRT/JSON, 706 keyframes, 706 OCR files, targeted visual review
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 00:39–01:10 | formula/name | 虚贡比、虚共比 | 需供比 | OCR 多帧及课程板书明确写“需供比” | high | corrected | 使用规范名，并保留公式 |
| A02 | 00:30–00:39 | product name | 巨量算术 | 巨量算数；课程称其现为抖音指数 | ASR 语境+界面/板书 | medium | corrected | 作为 2026-01 课程称谓，现行入口待核验 |
| A03 | 00:40–01:08 | UI path | 内幕概况、类目盖矿 | 类目概况 | OCR 多帧 | high | corrected | 路径标注为课程快照 |
| A04 | 00:42–00:54 | UI path | 搜索榜单 | 搜索榜单→产品 | OCR+ASR | high | accepted-as-is | 当前后台待核验 |
| A05 | 01:00–02:40 | UI path | 商品榜单 | 罗盘→市场→商品榜单 | OCR+ASR | high | accepted-as-is | 当前后台待核验 |
| A06 | 01:06–01:16 | UI path | 类目挖掘 | 罗盘→市场→类目挖掘 | OCR+ASR | high | accepted-as-is | 当前后台待核验 |
| A07 | 01:53–02:17 | UI path | 商机中心 | 商品→商机中心 | OCR+ASR | high | accepted-as-is | 当前后台待核验 |
| A08 | 01:54–01:58 | label | 印记/应记 | 应季 | 板书清晰写“应季” | high | corrected | 使用“应季” |
| A09 | 01:54–01:58 | label | 中小商家一报 | 中小卖家爆单 | 板书/OCR | high | corrected | 使用板书用语，当前标签待核验 |
| A10 | 01:58–02:01 | benefit labels | 搜索扶持、流量券赠送、上新扶持 | 同左 | 板书/OCR | high | accepted-as-is | 只作课程快照，现行权益待核验 |
| A11 | 02:03–02:08 | thresholds | 30天5、7天2、1天0.5 | 需供比：30 天≥5、7 天≥2、1 天≥0.5 | frame_0513/0514 | high | accepted-as-is | 标注教师筛选启发式，不冒充平台规则 |
| A12 | 02:03–02:08 | threshold | 发布时间两个月内 | 上架/发布时间≤2个月 | 板书/OCR | high | accepted-as-is | 类目化校准 |
| A13 | 02:03–02:08 | threshold | 日均交易5000以上 | 日成交额≥5,000 元 | 板书/OCR | high | accepted-as-is | 课程阈值，不作通用硬门槛 |
| A14 | 00:53–02:40 | threshold | 转化率5%以上 | 转化率≥5% | 多次板书/OCR | high | accepted-as-is | 使用类目基准校准 |
| A15 | 01:16–02:14 | threshold | 30%以上利润空间 | 售价相对货品+运费保留≥30%毛利缓冲 | 板书+ASR | high | accepted-as-is | 强制用完整利润模型复算 |
| A16 | 02:31–02:40 | formula | UV价值=营业额/点击数 | 同左 | 板书/OCR | high | accepted-as-is | 正式页注明口径依后台字段定义 |
| A17 | 多处 | UI paths | 罗盘/市场/榜单/竞争对比等 | 课程演示路径集合 | ASR+OCR+画面 | high | unresolved | 正式页统一挂“2026-01 快照”，当前核验前不写成逐点击指令 |
| A18 | 01:27:40–01:53:14 | ASR anomaly | 大段与课程无关连续文本 | 课间，无知识内容 | 静态画面+前后教师口述+ASR突变 | high | excluded-from-formal | 全段 raw-only |
| A19 | 约00:28–00:33 | statistic | 女装转化0.2%、退货85% | 教师引用的特定活动期案例 | ASR；缺乏可核验来源 | low | unresolved | 不进入现行行业基准，待权威数据核验 |
| A20 | 02:14–02:16 | tool name | 小风上货/小峰工具/小峰出货 | 第三方批量发布工具名未稳定识别 | 相邻 ASR 两种写法；抽帧未显示名称 | low | unresolved | 正式页不写具体名称，仅写“第三方批量发布工具”，或核验后补名 |
| A21 | 01:58–02:02 | benefit numbers | 2–3千曝光、14–28天、150元流量券 | 课程中的权益数值 | ASR，画面未形成完整同证 | low | unresolved | 不进入现行操作步骤 |
| A22 | 02:47–02:51 | eligibility | 约30单/月才有体验分/可竞争分析 | 教师所述门槛 | ASR | low | unresolved | 当前后台/官方文档核验后再用 |
| A23 | 02:52–02:54 | algorithm claim | 平台只给5家流量 | 教师对流量集中度的概括 | ASR，无官方证据 | low | unresolved | 不写成平台机制；仅保留“先发与排序竞争”风险提示 |
| A24 | 02:17–02:31 | lifecycle | 潜力品、爆发品、热卖品、衰退品 | 销量×增长四象限 | 板书+ASR | high | accepted-as-is | 编译为跟款生命周期框架 |
| A25 | 01:18、02:13 | tool | 1688采购助手 | 同左 | 板书+ASR+浏览器画面 | high | accepted-as-is | 作为课程工具示例，安装/可用性待核验 |
| A26 | 02:41–02:47 | tool | 蝉妈妈 | 同左 | ASR+画面 | high | accepted-as-is | 作为第三方付费工具示例，不背书数据准确性 |
| A27 | 02:41–02:47 | dependency | 精选联盟内商品才能查看部分数据 | 选品广场数据可见性限制 | ASR+OCR | medium | unresolved | 当前账号和后台核验前不写成固定限制 |
| A28 | 02:09–02:12 | audience claim | 老年人产品不要做 | 教师个人化建议 | ASR；缺乏品类/履约边界 | low | excluded-from-formal | 不正式化；替换为“校验目标人群与平台匹配度” |

## Gate Decision

语义门通过的含义是：关键术语、公式、路径、标签、数字和异常段均有明确处置。它不代表所有平台规则已经过当前官方验证；A02、A10、A17、A20–A23、A25–A27 仍需在正式页中保持时效隔离。
