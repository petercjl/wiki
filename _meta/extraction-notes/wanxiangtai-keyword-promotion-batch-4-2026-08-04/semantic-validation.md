# 语义校验

- Status: passed
- Raw evidence preserved: yes
- Validation scope: 10 个结构化钉钉文档的正文、表格、数值、版本词和图片语义
- Evidence sources: content.md、document-package.json、tables.json、images.json 与已归档图片
- Systematic variant search: passed；检查 100/1.5/7/500/4/8、内测、灰度、默认开启、采纳/复制等变体
- Formal text checked against normalized anchors: passed；正式页数值与边界逐项回查来源

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | S02 | threshold | 日预算≥100元 | 100 元为初步解锁门槛 | 正文与 IMG-01 | high | accepted-as-is | 标注灰度和非保证 |
| A02 | S03 | budget-rule | 单日0至1.5倍，7日不超7倍 | 单日弹性与周期总额同时成立 | 正文、表格、IMG-01 | high | accepted-as-is | 不把单日超均值误判为超预算 |
| A03 | S04 | eligibility | 人群溢价500%权限申请 | 高溢价属于资格能力 | 标题与正文 | medium | accepted-as-is | 不写成全账户默认上限 |
| A04 | S05 | limit | 4个；部分类目8个 | 单创意素材常规/类目上限 | 正文与 IMG-07 | high | accepted-as-is | 要求以当前后台为准 |
| A05 | S05 | relationship | 采纳同步、复制不同步 | 创意库关联与独立副本 | 正文与 IMG-06 | high | accepted-as-is | 明确后续修改关系 |
| A06 | S08 | versioning | 流量智选2.0（原搜索超车） | 原能力并入智能词包底层能力 | 正文与界面图 | high | accepted-as-is | 当前/历史报表分开写 |
| A07 | S10 | rollout | 净成交优化目标（内测中） | 非全量能力 | 标题与正文 | high | accepted-as-is | 先核对资格并考虑数据延迟 |
