---
title: JoinQuant 凯利公式量化仓位文章 knowledge unit inventory
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, joinquant, quant-trading, knowledge-units]
sources:
  - raw/webpages/joinquant/joinquant-kelly-position-sizing-2026-06-19.md
status: active
---

# JoinQuant 凯利公式量化仓位文章 knowledge unit inventory

| ID | Unit | Disposition | Target |
| --- | --- | --- | --- |
| JK-KU-001 | Kelly criterion maximizes long-run geometric capital growth across repeated bets under known probabilities and payoffs. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-002 | Gambling special case: `f = (p_win * b - p_loss) / b`. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-003 | Negative expected edge produces negative `f`; trading action should be no trade or the opposite side if feasible. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-004 | Except for certainty, Kelly does not recommend betting all capital; shrinking capital automatically shrinks absolute bet size. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-005 | Stock returns are continuous distributions, so a trade must be converted into a repeatable bet by defining entry signal and exit boundaries. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-006 | A signal is useful only if it shifts the probability distribution so hitting take-profit becomes more likely than hitting stop-loss. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-007 | General trading Kelly: `f = p_win / c - p_loss / b`, with gain rate `b` and loss rate `c`. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-008 | Example: `p_win=0.57`, `b=0.20`, `c=0.20` implies `f=70%`. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-009 | Kelly advantage becomes clearer as independent or sufficiently repeated signal count grows; sparse signals leave random variation dominant. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-010 | Small stop-loss widths plus high win rate can imply extreme leverage, but financing cost, leverage access, and model error constrain real usage. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-011 | Historical estimates often understate tail events; limit-down or liquidity failure can invalidate assumed stop-loss losses. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-012 | The capital base for Kelly should be tolerable loss capital above liquidation or psychological drawdown floor, not nominal account assets. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-013 | Assuming equal probability of hitting annual high/low from arbitrary current price is an invalid strong assumption and can overfit one asset. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-014 | Fixed price boundaries control payoff but give up time control; trades that never touch either boundary are a model weakness. | formalized | `01-凯利公式与量化仓位管理.md` |
| JK-KU-015 | Article comments are mostly reader feedback; one stop-loss execution concern reinforces the liquidity caveat. | merged | `01-凯利公式与量化仓位管理.md` |
