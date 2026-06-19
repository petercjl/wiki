---
title: JoinQuant 凯利公式量化仓位文章 omission audit
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, joinquant, quant-trading, omission-audit]
sources:
  - raw/webpages/joinquant/joinquant-kelly-position-sizing-2026-06-19.md
status: active
---

# JoinQuant 凯利公式量化仓位文章 omission audit

| Unit | Disposition | Reason |
| --- | --- | --- |
| Article jokes, rhetorical flourishes, author chat | raw-only | Preserved in raw; not durable trading knowledge. |
| Copyright notice and reposting instruction | raw-only | Legal/source notice preserved in raw; not formalized as trading knowledge. |
| Image files themselves | raw-only | Image meanings are represented; original URLs remain in raw clipping. |
| Reader praise comments | raw-only | No reusable knowledge beyond feedback. |
| Reader question about continuous limit-down inability to sell | merged | Integrated into black swan and stop-loss execution caveat. |
| Exact backtest screenshots | merged | Formal page preserves the anti-pattern and conclusion rather than copying screenshots. |

## Unresolved Items

- None requiring user judgment.
- If this page is later used for a live strategy, the strategy must estimate `p_win`, `b`, `c`, transaction costs, liquidity failure, and serial correlation from current data rather than reusing source examples.
