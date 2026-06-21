---
title: GitHub 量化理论资料 audit handoff
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, audit-handoff, quant-trading]
sources:
  - raw/github/quant-theory-github-sources-2026-06-20/
status: active
---

# GitHub 量化理论资料 Audit Handoff

## Source

- Adapter: GitHub/web source capture + markdown formal compilation.
- Raw path: `raw/github/quant-theory-github-sources-2026-06-20/`
- Original URLs: see `raw/github/quant-theory-github-sources-2026-06-20/source-map.md`
- Capture date: 2026-06-20
- Current-doc verification: GitHub pages browsed and raw README snapshots archived on 2026-06-20.

## Outputs

- Source profile: `_meta/extraction-notes/quant-theory-github-sources-2026-06-20/source-profile.md`
- Source inventory: `_meta/extraction-notes/quant-theory-github-sources-2026-06-20/source-inventory.md`
- Knowledge-unit inventory: `_meta/extraction-notes/quant-theory-github-sources-2026-06-20/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/quant-theory-github-sources-2026-06-20/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/quant-theory-github-sources-2026-06-20/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/quant-theory-github-sources-2026-06-20/formal-page-plan.md`
- Formal pages:
  - `domains/量化交易/04-量化理论基础/index.md`
  - `domains/量化交易/04-量化理论基础/01-策略收益来源分解.md`
  - `domains/量化交易/04-量化理论基础/02-选池、信号与组合构建.md`
  - `domains/量化交易/04-量化理论基础/03-买卖器、执行与风控.md`
  - `domains/量化交易/04-量化理论基础/04-策略评估指标与归因.md`
  - `domains/量化交易/04-量化理论基础/05-避免过拟合与回测陷阱.md`

## Coverage Summary

- Source units: 14 rows in coverage matrix plus 13 knowledge units.
- formalized: 13
- merged: 1
- raw-only: repository navigation/install/noise
- omitted-with-reason: 0
- unresolved: 0

## Expected Agent Use

- Future questions this source should support: ETF 池是否科学、策略是否过拟合、回测结果如何拆解、买卖器该优化什么、如何设计下一轮实验。
- Pages an Agent should read first: `04-量化理论基础/index.md`, then `01-策略收益来源分解.md`.
- Query/playbook entries: current quant domain index and JoinQuant agent entry should route to this theory layer.

## Known Risks

- Time-sensitive claims: GitHub repositories may change; tool usage details must be rechecked.
- Sensitive data removed: none.
- Weak source areas: this batch偏方法论，不覆盖中国 ETF 市场制度细节。
- User confirmation needed: none.

## Self-Validation

- Placeholder scan: `SHELL: 0`, `THIN: 0`, `OK: 6`.
- Ingest contract: `llm-wiki-ingest contract OK`; warnings were verbatim-match warnings because formal pages paraphrase source units instead of copying coverage phrases.
- Route audit: active vault `/Users/pechen/wiki`, target page has backlinks from `domains/量化交易/index.md` and `index.md`, no target warnings.
- Representative term search: passed for Alphalens, Qlib, Pyfolio, PyPortfolioOpt, purged, walk-forward, ETF 池, IC, 过拟合, 样本外.
- Index/log check: `domains/量化交易/index.md`, root `index.md`, and `log.md` updated.
- Remaining gaps: future should ingest academic/paper-level materials for more rigorous PBO/DSR and ETF universe construction theory.
