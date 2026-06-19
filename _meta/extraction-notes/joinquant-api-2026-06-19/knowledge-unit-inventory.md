---
title: 聚宽 API 文档 knowledge unit inventory
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, joinquant, knowledge-units]
sources:
  - raw/api/joinquant/joinquant-api-2026-06-19.md
status: active
---

# 聚宽 API 文档 knowledge unit inventory

## Core Knowledge Units

| ID | Unit | Disposition | Target |
| --- | --- | --- | --- |
| JQ-KU-001 | JoinQuant strategy scripts are event/callback scripts, not standalone local Python programs. | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| JQ-KU-002 | `initialize(context)` is the platform initialization entry and should register schedules and options. | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| JQ-KU-003 | `run_daily`, `run_weekly`, and `run_monthly` callbacks accept only `context`; they should be global functions. | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| JQ-KU-004 | Avoid mixing `run_daily` and `handle_data` unless intentional; never schedule `handle_data` directly. | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| JQ-KU-005 | Daily `history` and `attribute_history` exclude current-day data even after close. | formalized | `02-聚宽API能力地图.md` |
| JQ-KU-006 | `set_option('use_real_price', True)` is strongly recommended to reduce future-function risk from static adjusted prices. | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| JQ-KU-007 | Do not cache data API outputs across dates when real price mode is enabled. | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| JQ-KU-008 | `set_option('avoid_future_data', True)` enables future-data avoidance mode. | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| JQ-KU-009 | Multi-security `get_price` should avoid pandas Panel risk by setting `panel=False`. | formalized | `02-聚宽API能力地图.md` |
| JQ-KU-010 | Backtest/simulation file access is through JoinQuant private/research files, not local machine paths. | formalized | `03-聚宽策略报错与排查.md` |
| JQ-KU-011 | `create_backtest` is research-only and should not be used inside a backtest strategy. | formalized | `03-聚宽策略报错与排查.md` |
| JQ-KU-012 | Simulation persists `g` and `context`; non-serializable objects should not be stored in normal `g` fields. | formalized | `03-聚宽策略报错与排查.md` |
| JQ-KU-013 | Orders may be rejected by paused securities, zero volume, limit prices, insufficient cash, or platform matching rules. | formalized | `03-聚宽策略报错与排查.md` |
| JQ-KU-014 | Futures, tick, margin, and multi-account APIs require separate asset-class handling. | merged | `02-聚宽API能力地图.md` |
| JQ-KU-015 | Performance profiling via `enable_profile()` belongs at the top and should be used only for diagnostic runs. | merged | `03-聚宽策略报错与排查.md` |

## Code Example Units

The source contains multiple official sample strategies. They are represented as reusable structure rather than copied wholesale:

- Single-stock moving average structure.
- Open-before/open/after-market scheduled function pattern.
- Multi-stock holding pattern.
- Momentum/chase example.
- Halloween effect example.

The skill skeleton in `/Users/pechen/.codex/skills/joinquant-strategy/SKILL.md` formalizes the reusable template.
