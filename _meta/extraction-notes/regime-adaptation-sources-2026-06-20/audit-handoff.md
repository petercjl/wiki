---
title: 市场状态识别与策略自适应资料包 audit handoff
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, audit-handoff, quant-trading]
sources:
  - raw/github/regime-adaptation-sources-2026-06-20/
  - raw/articles/quant-regime-adaptation-2026-06-20/
  - raw/papers/quant-regime-adaptation-2026-06-20/
status: active
---

# 市场状态识别与策略自适应资料包 Audit Handoff

## Source

- Adapter: `llm-wiki-ingest/adapters/markdown-doc.md` and `web-clipping.md`.
- Raw path:
  - `raw/github/regime-adaptation-sources-2026-06-20/`
  - `raw/articles/quant-regime-adaptation-2026-06-20/`
  - `raw/papers/quant-regime-adaptation-2026-06-20/`
- Capture date: 2026-06-20.
- Current-doc verification: web search and raw downloads performed on 2026-06-20.

## Outputs

- Source profile: `_meta/extraction-notes/regime-adaptation-sources-2026-06-20/source-profile.md`
- Source inventory: `_meta/extraction-notes/regime-adaptation-sources-2026-06-20/source-inventory.md`
- Coverage matrix: `_meta/extraction-notes/regime-adaptation-sources-2026-06-20/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/regime-adaptation-sources-2026-06-20/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/regime-adaptation-sources-2026-06-20/formal-page-plan.md`
- Formal pages:
  - `domains/量化交易/04-量化理论基础/13-市场状态识别与策略失效.md`
  - `domains/量化交易/04-量化理论基础/14-状态自适应策略与动态资产配置.md`
  - `domains/量化交易/04-量化理论基础/15-策略失效监控与滚动验证.md`

## Coverage Summary

- Source units: 17
- formalized: 15
- merged: 1
- raw-only: installation/navigation/code details
- omitted-with-reason: none
- unresolved: 1 MDPI page blocked by 403

## Expected Agent Use

- Future questions this source should support:
  - 固定策略在某些年份失效怎么办？
  - 如何识别市场状态并切换策略或仓位？
  - 如何验证状态自适应策略没有过拟合？
  - 长周期回测和滚动样本外怎么组织？
- Pages an Agent should read first:
  - `13-市场状态识别与策略失效.md`
  - `14-状态自适应策略与动态资产配置.md`
  - `15-策略失效监控与滚动验证.md`

## Known Risks

- Time-sensitive claims: 2026 arXiv abstract is recent and may change before publication.
- Weak source areas: source package is method-heavy; does not yet contain a large formal survey of all regime-switching econometrics.
- User confirmation needed: none.

## Self-Validation

- Representative term search should include: HMM, GMM, KMeans, Jump Model, walk-forward, regime filter, strategy router, no-trade regime.
- Index/log check required after formal page creation.
