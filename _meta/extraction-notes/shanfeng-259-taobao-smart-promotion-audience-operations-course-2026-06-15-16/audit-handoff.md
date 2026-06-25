---
title: 山峰组259期6-15/6-16课程审计交接
type: source-summary
created: 2026-06-26
updated: 2026-06-26
domain: meta
tags: [llm-wiki, ingest, transcript, audit-handoff, ecommerce, taobao]
status: active
---

# Audit Handoff

## Source

- Source identity: 山峰组259期6-15/6-16课程
- Adapter: `llm-wiki-ingest/adapters/transcript.md`
- Raw:
  - `raw/transcripts/shanfeng-259-taobao-smart-promotion-audience-operations-course-2026-06-15-16/part1-2026-06-15-259.md`
  - `raw/transcripts/shanfeng-259-taobao-smart-promotion-audience-operations-course-2026-06-15-16/part2-2026-06-16-259.md`

## Extraction Notes

- `source-profile.md`
- `source-inventory.md`
- `course-reconstruction.md`
- `coverage-matrix.md`
- `omission-audit.md`
- `formal-page-plan.md`

## Formal Outputs Expected

- `domains/电商运营/02-淘宝天猫/06-淘宝智能推广与人群运营系统/`
- `queries/淘宝智能推广与人群运营诊断.md`

## Completeness Contract

- Coverage matrix contains 63 units.
- Every formalized unit has a formal target.
- Raw-only items are limited to decorative artifacts, classroom interaction, repeated oral prompts, and ASR drift with unclear meaning.

## Known Unresolved Items

- Some backend field names are transcript-derived and may be ASR-drifted; formal pages should mark exact current UI labels as待确认.
- 淘宝/万相台/生意参谋 tool paths can change; route future tactical answers through current backend verification if exact clicks are needed.

## Future Agent Use Cases

- Diagnose why a 淘宝 smart promotion plan burns spend.
- Decide whether a product should use standard plan, smart plan, search card, audience promotion, or traffic gold card.
- Determine whether a store is 拉新驱动、潜客回访驱动、均衡型 or 老客驱动.
- Compute exposure value and plan audience concentration from available backend reports.
- Choose metrics based on conversion cycle: direct transaction, add-cart, or inquiry.

