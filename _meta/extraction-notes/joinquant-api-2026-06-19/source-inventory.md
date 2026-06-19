---
title: 聚宽 API 文档 source inventory
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [llm-wiki, api-docs, joinquant, source-inventory]
sources:
  - raw/api/joinquant/joinquant-api-2026-06-19.md
status: active
---

# 聚宽 API 文档 source inventory

This inventory records the documentation structure at heading level for the first ingest pass. Detailed endpoint/function-level extraction is intentionally routed through the raw API archive and the formal capability map.

## Major Sections

| Source section | Knowledge disposition | Formal target |
| --- | --- | --- |
| API 文档说明 | formalized | `02-聚宽API能力地图.md` |
| 开始写策略 | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| 策略引擎介绍：安全、数据、运行频率、运行时间、订单处理 | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| 撮合流程、非交易时段下单、拆分合并与分红、真实价格模式 | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| 滑点、交易税费、风险指标 | merged | `02-聚宽API能力地图.md` |
| 回测环境、回测过程、模拟盘注意事项、模拟交易和回测差别 | formalized | `01-聚宽策略写作与回测兼容规范.md`, `03-聚宽策略报错与排查.md` |
| 策略程序架构 | formalized | `01-聚宽策略写作与回测兼容规范.md` |
| 策略设置函数 | formalized | `02-聚宽API能力地图.md` |
| 数据获取函数 | formalized | `02-聚宽API能力地图.md` |
| 数据处理函数、组合优化函数、jqlib | merged | `02-聚宽API能力地图.md` |
| 交易函数 | formalized | `02-聚宽API能力地图.md` |
| 对象、其他函数、文件读写、自定义库 | formalized | `02-聚宽API能力地图.md`, `03-聚宽策略报错与排查.md` |
| 策略组合、多个账户、Tick、融资融券、期货、归因分析 | merged | `02-聚宽API能力地图.md` |
| 策略示例 | formalized | `01-聚宽策略写作与回测兼容规范.md` |

## High-Value Function Families

- Strategy lifecycle: `initialize`, `process_initialize`, `after_code_changed`, `before_trading_start`, `handle_data`, `after_trading_end`
- Scheduling: `run_daily`, `run_weekly`, `run_monthly`, `unschedule_all`
- Options: `set_option`, `set_benchmark`, `set_slippage`, `set_order_cost`, `set_commission`, `disable_cache`
- Data: `get_price`, `history`, `attribute_history`, `get_bars`, `get_current_data`, `get_fundamentals`, `get_index_stocks`, `get_industry_stocks`, `get_concept_stocks`
- Trading: `order`, `order_value`, `order_target`, `order_target_value`, `cancel_order`, `get_open_orders`, `get_orders`, `get_trades`
- Diagnostics: `record`, `log.set_level`, `enable_profile`
- File/research boundary: `read_file`, `write_file`, `create_backtest`, backtest result APIs

## Inventory Gap

The first pass creates the Agent-usable execution layer. Future work should split detailed API manuals by asset class when repeated strategy work requires it:

- A股/ETF data and trading APIs
- Futures and night-session APIs
- Tick-level APIs
- Margin trading APIs
- Research-only batch backtest APIs
