---
title: 快递100实时快递单号查询技术文档 Source Inventory
type: source-summary
created: 2026-06-26
updated: 2026-06-26
domain: meta
tags: [llm-wiki, source-inventory, api, kuaidi100]
sources:
  - raw/api/kuaidi100/realtime-query-api-2026-06-26.md
status: active
---

# Source Inventory

| source_unit_id | source_location | source_unit | disposition |
| --- | --- | --- | --- |
| KUAI100-RT-001 | §一 实时快递查询接口 | Interface purpose: submit courier company code and tracking number to return latest logistics traces, state and time. | formalized |
| KUAI100-RT-002 | Notice before §1.1 | Query each waybill at least 30 minutes apart, otherwise the waybill may be locked. | formalized |
| KUAI100-RT-003 | §1.1-1.2 | Endpoint `https://poll.kuaidi100.com/poll/query.do`, POST. | formalized |
| KUAI100-RT-004 | §1.3 header | `Content-Type: application/x-www-form-urlencoded`. | formalized |
| KUAI100-RT-005 | §1.3 body auth | Required `customer`, `sign`; sign is `MD5(param + key + customer)` upper-case 32 chars by default. | formalized |
| KUAI100-RT-006 | §1.3 body `signType` | Optional `signType`; supports MD5, SHA256, SM3, SM3-HMAC. | formalized |
| KUAI100-RT-007 | §1.3 body `param.com` | Required lowercase courier company code. | formalized |
| KUAI100-RT-008 | §1.3 body `param.num` | Required tracking number, length 6-32 chars. | formalized |
| KUAI100-RT-009 | §1.3 body `param.phone` | Optional generally, but required for 顺丰速运、顺丰快运、中通快递; accepts receiver or sender phone, one value only. | formalized |
| KUAI100-RT-010 | §1.3 body `from/to` | Optional standard province-city-district origin/destination; improves delivery-state judgment; `to` required for resultv2=8 ETA. | formalized |
| KUAI100-RT-011 | §1.3 body `resultv2` | `1` adds status names, `4` adds advanced status/location fields, `8` adds ETA and predicted route. | formalized |
| KUAI100-RT-012 | §1.3 body `show/order/lang/needCourierInfo` | Output format, sort order, language and courier-info extraction options. | formalized |
| KUAI100-RT-013 | §1.4 | Example request payload structure. | formalized |
| KUAI100-RT-014 | §1.5 | Top-level response fields: `message`, `state`, `status`, `ischeck`, `com`, `nu`, `data`. | formalized |
| KUAI100-RT-015 | §1.5 `data[]` | Trace fields: `context`, `time`, `ftime`, `status`, `statusCode`, area/location fields. | formalized |
| KUAI100-RT-016 | §1.5 resultv2=8 | ETA fields and `predictedRoute[]`. | formalized |
| KUAI100-RT-017 | §1.5 `courierInfo` | Optional courier name/phone extraction when `needCourierInfo=True`; privacy-sensitive and not needed for user's monitoring goal. | formalized |
| KUAI100-RT-018 | §1.6 | State and advanced status matrix. | formalized |
| KUAI100-RT-019 | §1.7 | Correct JSON response example. | merged |
| KUAI100-RT-020 | §1.8 | Error response example and info code table. | formalized |
| KUAI100-RT-021 | §二 | Courier company code table can be downloaded; contact support if missing. | formalized |
| KUAI100-RT-022 | Page navigation/header/footer | Product menus, marketing links and site chrome. | raw-only |
