---
title: 聚宽 API 文档 omission audit
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, joinquant, omission-audit]
sources:
  - raw/api/joinquant/joinquant-api-2026-06-19.md
status: active
---

# 聚宽 API 文档 omission audit

## Raw-Only Or Deferred Units

| Unit | Disposition | Reason |
| --- | --- | --- |
| Large screenshots and diagrams | raw-only | Text meaning was captured where relevant; images remain in raw clipping links. |
| Full long sample strategies | merged | Reusable structure was extracted into formal pages and the skill skeleton; raw preserves full examples. |
| Attribution analysis details | raw-only | Not needed for writing runnable strategy scripts in the first pass. |
| Full futures/tick/margin endpoint details | merged/deferred | Formal API map routes future work; detailed manuals should be created when the user begins those asset classes. |
| Exact third-party library support list | unresolved | Source links to community page; needs current verification before strong claims. |

## Unresolved Items

- Verify the latest JoinQuant Python runtime and supported third-party package list before relying on obscure packages.
- Verify whether any API signatures changed after the 2026-06-19 clipping.
- Split detailed asset-class manuals after actual strategies require futures, tick, or margin trading.
