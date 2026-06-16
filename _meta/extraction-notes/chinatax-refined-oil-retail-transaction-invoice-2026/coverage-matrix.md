# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 一、发布背景 | 公告发布背景：打击加油机作弊、账外经营、隐匿销售收入，全面推广交易即开票。 | policy rationale | `domains/财税与经营财务/01-电商财税合规/09-成品油零售交易即开票规则.md` | formalized | 监管目标与业务影响 |
| S2 | 二、乐企平台 | 乐企平台定义及接入申请、能力订阅、测试验证、规则应用、授权管理等功能。 | concept definition | 同上 | formalized | 核心概念表 |
| S3 | 三、乐企自用 | 乐企自用定义与集团下属加油站例子。 | access mode | 同上 | formalized | 接入方式判断 |
| S4 | 四、乐企联用 | 乐企联用定义与不具备自用能力加油站接入联用平台例子。 | access mode | 同上 | formalized | 接入方式判断 |
| S5 | 五、系统改造 | 联用接入需改造收银系统或零售管理系统，传输加油机报税口、屏显、编码器等交易数据。 | system requirement | 同上 | formalized | 数据链路拆解 |
| S6 | 五、例3 | 零售管理系统嵌入式改造，通过接口读取并传输报税口数据，扫码支付后调用联用平台开票。 | implementation example | 同上 | formalized | 系统改造路径表 |
| S7 | 五、例4 | 无零售管理系统时改造收银系统，配置加油枪、油品、单价对应关系，支付后开票。 | implementation example | 同上 | formalized | 系统改造路径表 |
| S8 | 六、场景总述 | 第三方支付/互联网平台通过支付即开票；加油卡、现金等通过交易即开票。 | scenario taxonomy | 同上 | formalized | 交易场景矩阵 |
| S9 | 六、场景一/例5 | 第三方支付平台支付后，根据交易数据和支付金额自动生成普通发票。 | scenario rule | 同上 | formalized | 场景矩阵 |
| S10 | 六、场景二/例6 | 互联网平台支付后自动生成销售方为加油站、价税合计匹配支付额的发票。 | scenario rule | 同上 | formalized | 场景矩阵 |
| S11 | 六、场景三/例7-8 | 加油卡充值开不征税普通发票，或加油时逐笔开普通/专用发票，二者只能选其一。 | compliance rule | 同上 | formalized | 防重复开票规则 |
| S12 | 六、场景四/例9-10 | 现金、赊销、对公转账等完成交易后按实际交易数据开票；联用可能需人工补录支付信息。 | scenario rule | 同上 | formalized | 线下交易规则 |
| S13 | 七、换开 | 自动开票后抬头线上变更仅 1 次；普票换专票需线下资料；个人加油卡单位抬头不得开/换专票。 | aftersales rule | 同上 | formalized | 换开规则 |
| S14 | 八、汇总开票 | 单位/个体工商户且通过对公账户支付可汇总；非对公和自然人不得汇总，自然人不得开专票。 | compliance boundary | 同上 | formalized | 汇总开票矩阵 |
| S15 | 九、完成时限 | 过渡期至 2026-11-01，结束前全面实现交易即开票。 | implementation deadline | 同上 | formalized | 时间敏感风险 |

No meaningful source unit is omitted. Decorative website chrome was not present in extracted source and is raw-only by absence.
