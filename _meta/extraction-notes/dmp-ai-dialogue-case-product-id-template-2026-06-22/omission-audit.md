---
title: DMP AI dialogue case {BASE_ITEM_ID} omission audit
type: source-summary
created: 2026-06-22
updated: 2026-06-22
domain: meta
tags: [dmp-ai, omission-audit]
sources:
  - _meta/extraction-notes/dmp-ai-dialogue-case-product-id-template-2026-06-22/coverage-matrix.md
status: active
---

# Omission Audit

| item | status | reason |
|---|---|---|
| Prompt directory | formalized | Converted into the case page's `提问目录` and reusable prompt sections. |
| Prompt text | formalized | Core prompts preserved in formal page; longer variants remain in raw. |
| Expected data fields | formalized | Each route lists expected data or output fields. |
| Case result | formalized | Representative results summarized in the case recap and raw evidence summary. |
| Full local JSON output | raw-only | Not copied into wiki because it includes large operational output and potentially sensitive advertiser/member details; the case evidence summary preserves the meaningful knowledge units. |
| Sensitive advertiser/member ID | omitted-with-reason | Formal page masks it because future Agent use needs route logic, not full private ID. |
| HTML/Excel report files | raw-only by reference | Large generated deliverables are referenced in raw evidence summary but not copied because this ingest focuses on dialogue method, prompts and QA rules. |

No source unit was omitted because it was unimportant. Privacy-sensitive and bulky run artifacts were represented through a raw evidence summary instead of full raw copying.
