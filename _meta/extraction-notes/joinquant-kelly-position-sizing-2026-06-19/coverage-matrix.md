---
title: JoinQuant 凯利公式量化仓位文章 coverage matrix
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, joinquant, quant-trading, coverage]
sources:
  - raw/webpages/joinquant/joinquant-kelly-position-sizing-2026-06-19.md
status: active
---

# JoinQuant 凯利公式量化仓位文章 coverage matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| JK-COV-001 | frontmatter | title, source URL, created date | traceability | `source-profile.md` | formalized | Preserved in source profile and raw. |
| JK-COV-002 | 导语/写作背景 | Kelly is often misused; correct methodology matters | orientation | `01-凯利公式与量化仓位管理.md` | merged | Converted into page problem statement. |
| JK-COV-003 | 一、背景 | Kelly found optimal fraction for repeated betting; later linked to finance | concept background | `01-凯利公式与量化仓位管理.md` | merged | Historical names are not the durable point. |
| JK-COV-004 | 二、赌博公式 | `f=(p_win*b-p_loss)/b`, terms and 60/40 example | formula/example | `01-凯利公式与量化仓位管理.md` | formalized | Formula, variables, and 20% example represented. |
| JK-COV-005 | 二、注意两点 | negative expected edge, no full-bet except certainty, fractional protection | decision rule | `01-凯利公式与量化仓位管理.md` | formalized | Converted into trading rules. |
| JK-COV-006 | 三、股票转赌博 | random walk, take-profit/stop-loss boundaries, signal shifts distribution | modeling method | `01-凯利公式与量化仓位管理.md` | formalized | Preserves conversion workflow. |
| JK-COV-007 | 四、一般公式 | `f=p_win/c-p_loss/b`, variables, 57/43 and 20%/20% example | formula/example | `01-凯利公式与量化仓位管理.md` | formalized | Includes 70% result and interpretation. |
| JK-COV-008 | 四、蒙特卡洛 | repeated trades T=100/500/1000 show Kelly edge emerges with frequency | statistical caveat | `01-凯利公式与量化仓位管理.md` | formalized | Rewritten as signal-frequency requirement. |
| JK-COV-009 | 加杠杆 | high win rate and small stop loss can imply 20x leverage; reality constrains it | leverage caveat | `01-凯利公式与量化仓位管理.md` | formalized | Includes financing friction and overbetting warning. |
| JK-COV-010 | 黑天鹅 | historical tails underestimated; stop-loss may fail under limit-down/liquidity events | risk caveat | `01-凯利公式与量化仓位管理.md` | formalized | Includes stock crash example logic without long quote. |
| JK-COV-011 | 真正的本金 | Kelly base is tolerable loss capital; private fund liquidation line example | capital base rule | `01-凯利公式与量化仓位管理.md` | formalized | Preserves 1000w/0.8 liquidation example. |
| JK-COV-012 | 错误例子 | equal high/low hit probability assumption is invalid; one-symbol backtest can mislead | anti-pattern | `01-凯利公式与量化仓位管理.md` | formalized | Converted into assumption audit checklist. |
| JK-COV-013 | 彩蛋 | fixed boundary model controls payoff but loses time control | model limitation | `01-凯利公式与量化仓位管理.md` | formalized | Added to limitations. |
| JK-COV-014 | comments | praise and stop-loss execution question | reader tail | `01-凯利公式与量化仓位管理.md` | merged | Only the execution-risk question adds knowledge. |
| JK-COV-015 | copyright notice and decorative wording | source legal/decorative text | raw trace | raw source | raw-only | Preserved in raw; not repeated in formal page. |

## Coverage Result

All meaningful source units are represented in formal knowledge, merged into broader reusable rules, or preserved raw-only with reason.
