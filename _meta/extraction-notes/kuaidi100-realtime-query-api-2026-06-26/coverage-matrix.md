---
title: 快递100实时查询 API Coverage Matrix
type: source-summary
created: 2026-06-26
updated: 2026-06-26
domain: meta
tags: [llm-wiki, coverage, api, kuaidi100]
sources:
  - raw/api/kuaidi100/realtime-query-api-2026-06-26.md
status: active
---

# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | endpoint | method | request_fields | response_fields | examples | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KUAI100-RT-001 | §一 | Interface purpose | capability | `/poll/query.do` | POST | `com`, `num` | `data`, `state` | no | [[domains/电商运营/30-ERP与系统工具/02-快递100实时查询API]] | formalized |  |
| KUAI100-RT-002 | Notice | 30-minute minimum per waybill | risk | `/poll/query.do` | POST |  |  | no | same | formalized |  |
| KUAI100-RT-003 | §1.1-1.2 | Endpoint and method | endpoint | `/poll/query.do` | POST |  |  | no | same | formalized |  |
| KUAI100-RT-004 | §1.3 header | Form content type | transport | `/poll/query.do` | POST | header `Content-Type` |  | no | same | formalized |  |
| KUAI100-RT-005 | §1.3 body | customer/sign/param signature | auth | `/poll/query.do` | POST | `customer`, `sign`, `param`, `signType` |  | yes | same | formalized |  |
| KUAI100-RT-006 | §1.3 signType | Alternate algorithms | auth | `/poll/query.do` | POST | `signType` |  | no | same | formalized |  |
| KUAI100-RT-007 | §1.3 com | Courier code | request | `/poll/query.do` | POST | `param.com` | `com` | no | same | formalized |  |
| KUAI100-RT-008 | §1.3 num | Tracking number | request | `/poll/query.do` | POST | `param.num` | `nu` | no | same | formalized |  |
| KUAI100-RT-009 | §1.3 phone | Phone requirement | request/privacy | `/poll/query.do` | POST | `param.phone` |  | no | same | formalized |  |
| KUAI100-RT-010 | §1.3 from/to | Origin/destination | request | `/poll/query.do` | POST | `param.from`, `param.to` | `routeInfo` | no | same | formalized |  |
| KUAI100-RT-011 | §1.3 resultv2 | Result mode | request | `/poll/query.do` | POST | `param.resultv2` | `status`, `statusCode`, `routeInfo`, `arrivalTime`, `predictedRoute` | yes | same | formalized |  |
| KUAI100-RT-012 | §1.3 options | show/order/lang/needCourierInfo | request | `/poll/query.do` | POST | `show`, `order`, `lang`, `needCourierInfo` | `courierInfo` | yes | same | formalized |  |
| KUAI100-RT-013 | §1.4 | Request example | example | `/poll/query.do` | POST | all example fields |  | yes | same | formalized | Reconstructed to avoid exposing credentials. |
| KUAI100-RT-014 | §1.5 | Top-level response | response | `/poll/query.do` | POST |  | `message`, `state`, `status`, `ischeck`, `com`, `nu`, `data` | yes | same | formalized |  |
| KUAI100-RT-015 | §1.5 data[] | Trace node fields | response | `/poll/query.do` | POST |  | `context`, `time`, `ftime`, `status`, `statusCode`, area/location fields | yes | same | formalized |  |
| KUAI100-RT-016 | §1.5 resultv2=8 | ETA and predicted route | response | `/poll/query.do` | POST | `resultv2=8`, `to` | `arrivalTime`, `totalTime`, `remainTime`, `probability`, `predictedRoute` | yes | same | formalized |  |
| KUAI100-RT-017 | §1.5 courierInfo | Courier person extraction | response/privacy | `/poll/query.do` | POST | `needCourierInfo` | `courierInfo` | yes | same | formalized | Marked do-not-enable by default. |
| KUAI100-RT-018 | §1.6 | Basic and advanced status matrix | monitoring | `/poll/query.do` | POST | `resultv2=4/8` | `state`, `statusCode` | no | same | formalized |  |
| KUAI100-RT-019 | §1.7 | Correct response example | example | `/poll/query.do` | POST |  | full JSON shape | yes | same | merged | Example fields integrated into schema and recipes. |
| KUAI100-RT-020 | §1.8 | Error response and codes | error handling | `/poll/query.do` | POST |  | `returnCode`, `message` | yes | same | formalized |  |
| KUAI100-RT-021 | §二 | Courier company code table | integration dependency | n/a | n/a | `com` |  | no | same | formalized |  |
| KUAI100-RT-022 | Page chrome | Navigation and marketing links | noise | n/a | n/a |  |  | no | raw only | raw-only | Site navigation preserved in raw, not domain knowledge. |
