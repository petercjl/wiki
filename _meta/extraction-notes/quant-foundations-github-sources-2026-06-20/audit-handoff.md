---
title: GitHub 量化基础资料 audit handoff
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, audit-handoff, quant-trading]
sources:
  - raw/github/quant-foundations-github-sources-2026-06-20/
status: active
---

# GitHub 量化基础资料 Audit Handoff

## Source

- Adapter: GitHub repository capture + markdown formal compilation.
- Raw path: `raw/github/quant-foundations-github-sources-2026-06-20/`
- Original URLs: see `raw/github/quant-foundations-github-sources-2026-06-20/source-map.md`
- Capture date: 2026-06-20
- Current-doc verification: repositories shallow-cloned on 2026-06-20.

## Outputs

- Source profile: `_meta/extraction-notes/quant-foundations-github-sources-2026-06-20/source-profile.md`
- Source inventory: `_meta/extraction-notes/quant-foundations-github-sources-2026-06-20/source-inventory.md`
- Knowledge-unit inventory: `_meta/extraction-notes/quant-foundations-github-sources-2026-06-20/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/quant-foundations-github-sources-2026-06-20/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/quant-foundations-github-sources-2026-06-20/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/quant-foundations-github-sources-2026-06-20/formal-page-plan.md`
- Formal pages: `domains/量化交易/04-量化理论基础/`

## Coverage Summary

- Source groups: 11 rows in coverage matrix.
- formalized: 10
- raw-only: 1
- omitted-with-reason: 0
- unresolved: 2 future-work notes.

## Expected Agent Use

- Future questions this source should support: 量化基础学习、策略分类、因子研究、组合构建、回测评估、交易执行、过拟合治理、聚宽策略研究前置阅读。
- Pages an Agent should read first: `domains/量化交易/04-量化理论基础/index.md`.

## Known Risks

- Time-sensitive claims: GitHub repositories may change.
- Weak source areas: 本批偏开源工具方法论，不替代系统金融教材、交易所规则或中国市场制度细则。
- User confirmation needed: none.

## Self-Validation

- Placeholder scan: `SHELL: 0`, `THIN: 0`, `OK: 13`.
- Ingest contract: `llm-wiki-ingest contract OK`; warnings were verbatim-match warnings because formal pages compile source units into Chinese knowledge rather than copying coverage row phrases.
- Route audit: active vault `/Users/pechen/wiki`; target page exists, has backlinks from `domains/量化交易/index.md`, root `index.md`, `queries/joinquant-strategy-agent-entry.md`, and `12-量化研究工作流与实验纪律.md`; target warnings: none.
- Representative term search: passed for Zipline, Backtrader, Alphalens, Pyfolio, Empyrical, Riskfolio, Qlib, purge, embargo, walk-forward, 市场冲击, 因子, Alpha, 组合构建, 回测系统, 点时正确, 过拟合.
- Repo archive check: 12 GitHub repositories shallow-cloned under `raw/github/quant-foundations-github-sources-2026-06-20/repos/`.
