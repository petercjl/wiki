---
title: JoinQuant 凯利公式量化仓位文章 audit handoff
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, joinquant, quant-trading, audit-handoff]
sources:
  - raw/webpages/joinquant/joinquant-kelly-position-sizing-2026-06-19.md
status: active
---

# JoinQuant 凯利公式量化仓位文章 Audit Handoff

## Source

- Adapter: `llm-wiki-ingest/adapters/web-clipping.md`
- Raw path: `raw/webpages/joinquant/joinquant-kelly-position-sizing-2026-06-19.md`
- Original URL/path: `https://www.joinquant.com/view/community/detail/469e185e2c1967938290223520a6eb9d?type=1`
- Capture date: 2026-06-19
- Current-doc verification: not required for historical concept article; live strategy use must re-estimate assumptions.

## Outputs

- Source profile: `_meta/extraction-notes/joinquant-kelly-position-sizing-2026-06-19/source-profile.md`
- Source inventory: `_meta/extraction-notes/joinquant-kelly-position-sizing-2026-06-19/source-inventory.md`
- Knowledge-unit inventory: `_meta/extraction-notes/joinquant-kelly-position-sizing-2026-06-19/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/joinquant-kelly-position-sizing-2026-06-19/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/joinquant-kelly-position-sizing-2026-06-19/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/joinquant-kelly-position-sizing-2026-06-19/formal-page-plan.md`
- Formal pages:
  - `domains/量化交易/02-策略风控与资金管理/index.md`
  - `domains/量化交易/02-策略风控与资金管理/01-凯利公式与量化仓位管理.md`

## Coverage Summary

- Source units: 15
- formalized: 11
- merged: 3
- raw-only: 1
- omitted-with-reason: 0
- unresolved: 0

## Expected Agent Use

- Future questions this source should support:
  - 如何用凯利公式做量化仓位？
  - 如何把股票交易信号转换成可套用凯利公式的赌博模型？
  - 为什么凯利仓位在实盘中要打折？
  - 如何审核一个用年度高低点套凯利公式的回测假设？
- Pages an Agent should read first:
  - `domains/量化交易/02-策略风控与资金管理/01-凯利公式与量化仓位管理.md`
- Query/playbook entries: none created; quant domain index routes this page.

## Known Risks

- Time-sensitive claims: source examples are historical; no current market parameters should be reused.
- Sensitive data removed: none.
- Weak source areas: source is educational and does not prove the formulas; it does not handle serial correlation, transaction costs, or portfolio covariance in depth.
- User confirmation needed: none.

## Self-Validation

- Ingest contract: `llm-wiki-ingest contract OK`; mechanical warnings were verbatim-match warnings for paraphrased coverage rows, not missing formal representation.
- Placeholder scan: `SHELL: 0`, `THIN: 0`, `OK: 2` for `domains/量化交易/02-策略风控与资金管理`.
- Route audit: target page has backlinks from `domains/量化交易/02-策略风控与资金管理/index.md`, `domains/量化交易/index.md`, and `index.md`; no target warnings.
- Representative term search: confirmed `凯利公式`, `p_win`, `p_loss`, `可承受损失`, `黑天鹅`, `年度最高价`, and `固定边界` appear in formal/extraction/index/log outputs.
- Placeholder term scan: no `TODO/TBD/待补/占位/placeholder/FIXME` hits in the new formal and extraction-note paths.
- Index/log check: updated `domains/量化交易/index.md`, `index.md`, and `log.md`.
- Remaining gaps: no source-coverage gaps expected.
