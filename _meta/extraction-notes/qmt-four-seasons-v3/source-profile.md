---
title: QMT四季发财v3 策略入库源资料画像
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [quant-trading, joinquant, strategy, backtesting]
sources:
  - raw/quant-strategies/qmt-four-seasons-v3/qmt四季发财v3-r3-summary.py
  - raw/quant-strategies/qmt-four-seasons-v3/qmt四季发财v3-r3导出检查-2026-06-19.md
status: active
---

# QMT四季发财v3 策略入库源资料画像

## Source Profile

- source title: QMT四季发财v3 / ETF收益率稳定性轮动策略。
- source type: 聚宽社区策略脚本 + 本地日志增强脚本 + 聚宽回测导出 CSV/日志 + 本地结构化分析报告。
- source slug: `qmt-four-seasons-v3`。
- capture/compile date: 2026-06-19。
- language: Chinese / Python。
- adapters: `markdown-doc` for strategy README/report/script, `spreadsheet-report` for exported CSV analysis.
- primary domain: `domains/量化交易/03-策略案例/`。
- secondary domain: `domains/量化交易/01-聚宽/`，用于沉淀社区策略取证和日志瘦身方法。

## Raw Archive

- `raw/quant-strategies/qmt-four-seasons-v3/qmt四季发财v3-r3-summary.py`
- `raw/quant-strategies/qmt-four-seasons-v3/qmt四季发财v3-r3导出检查-2026-06-19.md`
- `raw/quant-strategies/qmt-four-seasons-v3/analysis_summary-r3.json`
- `raw/quant-strategies/qmt-four-seasons-v3/yearly_returns-r3.csv`
- `raw/quant-strategies/qmt-four-seasons-v3/security_realized_pnl-r3.csv`

Full local project archive remains under:

- `/Users/pechen/AI/QuantTrading/strategies/qmt四季发财v3/`

## Existing Memory Search

- `domains/量化交易/00-股票量化知识地图.md` already defines the community strategy ingestion mainline.
- `domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范.md` defines JoinQuant script/logging compatibility.
- `domains/量化交易/01-聚宽/03-聚宽策略报错与排查.md` stores platform failure modes.
- `domains/量化交易/02-策略风控与资金管理/01-凯利公式与量化仓位管理.md` is related but not the primary home, because QMT四季发财v3 is an ETF rotation strategy, not a sizing formula page.

Disposition:

- create new strategy case page under `03-策略案例/`。
- create reusable JoinQuant evidence/logging method page under `01-聚宽/`。
- update quant indexes and global index.

