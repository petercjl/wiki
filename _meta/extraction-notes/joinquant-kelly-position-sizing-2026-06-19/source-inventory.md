---
title: JoinQuant 凯利公式量化仓位文章 source inventory
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, joinquant, quant-trading, source-inventory]
sources:
  - raw/webpages/joinquant/joinquant-kelly-position-sizing-2026-06-19.md
status: active
---

# JoinQuant 凯利公式量化仓位文章 source inventory

## Major Sections

| Source section | Source content role | Formal disposition |
| --- | --- | --- |
| 导语、作者、写作背景 | explains why incorrect Kelly usage matters | raw-only for article framing; core warning merged |
| 一、凯利公式产生的背景 | historical orientation | raw-only except "continuous betting optimal fraction" concept |
| 二、赌博怎么用凯利公式？ | special Kelly formula, example, negative edge, fractional betting | formalized |
| 三、把股票模型转换为赌博模型 | stock process to repeated bet conversion through signal, take-profit, stop-loss | formalized |
| 四、凯利公式登场以后呢？ | general Kelly formula for gains/losses, signal frequency, Monte Carlo examples | formalized |
| 加杠杆 | high leverage result from small loss rate and high edge | formalized |
| 黑天鹅 | historical probabilities underestimate tail risk; stop-loss may fail during limit-down sequences | formalized |
| 真正的本金是什么？ | Kelly base should be tolerable loss capital, not nominal total assets | formalized |
| 错误例子 | invalid assumption that hitting annual high/low has equal probability from any price | formalized |
| 彩蛋 | fixed take-profit/stop-loss conversion sacrifices time control | formalized |
| 评论区 | reader reactions and repeated question about unexecutable stop-loss | merged into black-swan/liquidity caveat |

## Informative Images

The clipping contains formulas, payoff curves, random-walk diagrams, Monte Carlo net-value diagrams, leverage curves, and backtest screenshots. Image URLs remain in raw. Their meanings are represented as knowledge units rather than copied as images.
