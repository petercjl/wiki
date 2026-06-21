---
title: DMP AI Internal Tools audit handoff
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, audit-handoff, dmp-ai]
sources:
  - raw/data/dmp-ai-internal-tools-2026-06-20/DMP_AI_internal_tools.md
status: active
---

# DMP AI Internal Tools Audit Handoff

## Source

- Adapter: `llm-wiki-ingest/adapters/markdown-doc.md`
- Raw path: `raw/data/dmp-ai-internal-tools-2026-06-20/DMP_AI_internal_tools.md`
- Original path: `/Users/pechen/AI/Research/DMP_AI_internal_tools.md`
- Capture date: 2026-06-20
- Current-doc verification: local Markdown source read from workspace on 2026-06-20; no web/current platform re-query performed during ingest.

## Outputs

- Source profile: `_meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/source-profile.md`
- Source inventory: `_meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/source-inventory.md`
- Knowledge-unit inventory: `_meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/formal-page-plan.md`
- Formal pages: `domains/电商运营/02-淘宝天猫/04-达摩盘AI/index.md`, `domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册.md`, `queries/达摩盘AI竞品数据挖掘.md`

## Coverage Summary

- Source headings: 116
- Tool units: 8
- Data asset units: 15
- formalized: all inventoried units
- merged: none
- raw-only: none
- omitted-with-reason: none
- unresolved: only source-level future validation leads; preserved in formal manual

## Expected Agent Use

- Future questions this source should support: DMP AI internal tool discovery, competitor sales/ad/search/audience data mining, tool parameter prompt writing, SQL-over-data_id deepening, and boundary selection among tools.
- Pages an Agent should read first: [[queries/达摩盘AI竞品数据挖掘]], then [[domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册]].
- Query/playbook entries: [[queries/达摩盘AI竞品数据挖掘]] and [[domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册]].

## Known Risks

- Time-sensitive claims: high; DMP AI internal tool registry and permissions may change after 2026-06-20.
- Sensitive data removed: no raw deletion; own advertiser/member ID remains masked as in source.
- Weak source areas: tool/data assets marked pending validation or direct query failed in the source need future live DMP AI testing.
- User confirmation needed: none for ingestion.

## Self-Validation

- Ingest contract: `llm-wiki-ingest contract OK`; validator emitted mechanical verbatim warnings for coverage rows because the rows contain audit phrasing, while the formal manual embeds the source body verbatim.
- Raw comparison: original source and raw archive match exactly (`cmp` exit code `0`).
- Embedded source comparison: formal manual contains the full source body after `# DMP AI Internal Tools` (`fullSourceEmbedded: true`).
- Placeholder scan: DMP AI formal pages `SHELL:0 THIN:0 OK:2`; extraction notes `SHELL:0 THIN:0 OK:7`; queries directory `SHELL:0 THIN:0 OK:9`.
- Representative term search: found `tool_item_benchmark_dataquery`, `tool_crowd_audience_insight`, `tool_e_commerce_crowd_advertising_dataquery`, `商品VIEW人群资产流入流出明细-同行优秀品视角`, `1517898925200113664`, `734065650463`, `868,983`, and `9,024,472` in formal/query/extraction outputs.
- Route audit: target pages exist, have backlinks and outgoing links, with target `warnings: []`.
- Index/log check: root index, 电商运营 index, 淘宝天猫 index, 淘宝营销工具 index, and log updated.
- Remaining gaps: none expected beyond source-declared validation backlog.
