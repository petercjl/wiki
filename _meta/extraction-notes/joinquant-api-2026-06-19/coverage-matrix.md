---
title: 聚宽 API 文档 coverage matrix
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, joinquant, coverage]
sources:
  - raw/api/joinquant/joinquant-api-2026-06-19.md
status: active
---

# 聚宽 API 文档 coverage matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| JQ-COV-001 | 开始写策略 | Strategy entry examples | runnable strategy structure | `domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范.md` | formalized | Reconstructed into strategy-writing rules and skill skeleton. |
| JQ-COV-002 | 策略引擎介绍/安全/回测环境 | Engine safety and environment | platform boundary | `domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范.md` | formalized | Captures local-vs-platform constraints. |
| JQ-COV-003 | 运行频率/运行时间/策略程序架构 | Frequency and scheduling | callback contract | `domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范.md` | formalized | Includes callback signature and scheduler pitfalls. |
| JQ-COV-004 | 撮合流程/订单处理 | Order matching and execution | trading behavior | `domains/量化交易/01-聚宽/02-聚宽API能力地图.md` | formalized | Capability map routes order APIs and matching caveats. |
| JQ-COV-005 | 拆分合并与分红/use_real_price/avoid_future_data | Real price mode and future data | anti-future-data rule | `domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范.md` | formalized | Converted into hard writing rules. |
| JQ-COV-006 | 回测过程/模拟盘注意事项/模拟交易和回测的差别 | Backtest and simulation differences | troubleshooting | `domains/量化交易/01-聚宽/03-聚宽策略报错与排查.md` | formalized | Includes persistence and simulation update issues. |
| JQ-COV-007 | 策略程序架构 | Strategy architecture APIs | lifecycle map | `domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范.md` | formalized | Main functions represented in lifecycle rules. |
| JQ-COV-008 | 数据获取函数 | Data retrieval APIs | data API map | `domains/量化交易/01-聚宽/02-聚宽API能力地图.md` | formalized | Includes history/attribute_history/get_price risks. |
| JQ-COV-009 | 交易函数 | Trading APIs | order API map | `domains/量化交易/01-聚宽/02-聚宽API能力地图.md` | formalized | Includes target/value/amount interface choice. |
| JQ-COV-010 | 对象 | Objects and context fields | runtime objects | `domains/量化交易/01-聚宽/02-聚宽API能力地图.md` | merged | Merged into lifecycle and API map. |
| JQ-COV-011 | read_file/write_file/自定义python库/create_backtest | File I/O and custom imports | environment boundary | `domains/量化交易/01-聚宽/03-聚宽策略报错与排查.md` | formalized | Separates research-only and backtest-safe usage. |
| JQ-COV-012 | 策略组合/Tick/融资融券/期货 | Futures/tick/margin/multi-account APIs | asset-class branches | `domains/量化交易/01-聚宽/02-聚宽API能力地图.md` | merged | Detailed manuals deferred until active strategy demand. |
| JQ-COV-013 | 归因分析说明 | Attribution analysis | analysis reference | raw source | raw-only | Preserved in raw; not needed for first strategy-writing skill. |
| JQ-COV-014 | 策略示例 | Long official code examples | examples/templates | `/Users/pechen/.codex/skills/joinquant-strategy/SKILL.md` | merged | Reconstructed into reusable template and checker rules. |

## Coverage Result

First pass coverage is sufficient for Agent strategy writing and compatibility checking. It is not yet a complete endpoint-by-endpoint JoinQuant API manual.
