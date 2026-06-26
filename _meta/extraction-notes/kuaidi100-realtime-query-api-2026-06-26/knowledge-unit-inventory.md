---
title: 快递100实时查询 API Knowledge Unit Inventory
type: source-summary
created: 2026-06-26
updated: 2026-06-26
domain: meta
tags: [llm-wiki, knowledge-unit-inventory, api, kuaidi100]
sources:
  - raw/api/kuaidi100/realtime-query-api-2026-06-26.md
status: active
---

# Knowledge Unit Inventory

| unit_id | knowledge_unit | role | target |
| --- | --- | --- | --- |
| KUAI100-RT-001 | 实时查询是主动查询接口，适合临时核验或小批量巡检，不适合对同一单号高频轮询。 | capability | [[domains/电商运营/30-ERP与系统工具/02-快递100实时查询API|快递100实时查询 API]] |
| KUAI100-RT-002 | 单号查询频率至少间隔半小时，否则可能锁单。 | risk / rate rule | same |
| KUAI100-RT-003 | 请求方式是 `POST application/x-www-form-urlencoded` 到 `https://poll.kuaidi100.com/poll/query.do`。 | endpoint contract | same |
| KUAI100-RT-004 | 身份参数为 `customer`、`sign`、`param`，默认签名是 `MD5(param + key + customer)` 后转 32 位大写。 | auth / signature | same |
| KUAI100-RT-005 | `param.com` 是小写快递公司编码，`param.num` 是 6-32 位运单号。 | request schema | same |
| KUAI100-RT-006 | 顺丰速运、顺丰快运、中通快递查询时 `phone` 必填，其他快递选填；可传收件或寄件电话。 | privacy / request schema | same |
| KUAI100-RT-007 | `resultv2=1/4/8` 决定是否返回状态名称、高级状态、行政区、当前位置、预计到达时间和预计轨迹。 | request mode | same |
| KUAI100-RT-008 | 订单履约监控建议用 `resultv2=4` 获取 `statusCode`；需要时效预测才用 `8`，且需要目的地。 | implementation decision | same |
| KUAI100-RT-009 | 顶层 `state` 是当前基础物流状态；`data[0]` 是最新轨迹节点。 | response interpretation | same |
| KUAI100-RT-010 | 基础状态：1 揽收，0 在途，5 派件，3 签收，2 疑难，6 退回，4 退签，7 转投，8/10/11/12/13 清关相关，14 拒签。 | status mapping | same |
| KUAI100-RT-011 | 高级异常状态包括 201 超时未签收、202 超时未更新、204 派件异常、205 柜或驿站超时未取、208 滞留等。 | monitoring rule | same |
| KUAI100-RT-012 | 错误码 400、408、500、501、502、503、601 分别对应数据/公司问题、手机号校验、无结果、服务异常、繁忙、签名失败、key 过期/无单量。 | error handling | same |
| KUAI100-RT-013 | 公司编码表需要从快递100开放平台下载；旺店通物流名称需要映射为快递100 `com` 编码。 | integration dependency | same |
| KUAI100-RT-014 | `needCourierInfo=True` 会返回快递员姓名和电话，不符合当前“不需要收件人/人员信息”的监控目标，默认不要开启。 | privacy rule | same |
