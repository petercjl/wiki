---
title: QMT四季发财v3 Source Inventory
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [source-inventory, quant-trading, joinquant]
sources:
  - raw/quant-strategies/qmt-four-seasons-v3/
status: active
---

# QMT四季发财v3 Source Inventory

| source_id | path | format | role | coverage |
| --- | --- | --- | --- | --- |
| SRC-001 | `raw/quant-strategies/qmt-four-seasons-v3/qmt四季发财v3-r3-summary.py` | Python | 策略脚本、参数、信号、过滤、调仓、日志事件合同 | QMT-001 至 QMT-008、QMT-012 |
| SRC-002 | `raw/quant-strategies/qmt-four-seasons-v3/qmt四季发财v3-r3导出检查-2026-06-19.md` | Markdown | r3 导出完整性、日志瘦身验证、r2/r3 对比 | QMT-007、QMT-008、QMT-009、QMT-012 |
| SRC-003 | `raw/quant-strategies/qmt-four-seasons-v3/analysis_summary-r3.json` | JSON | 回测绩效、交易汇总、日志事件、标的贡献结构化数据 | QMT-008 至 QMT-012 |
| SRC-004 | `raw/quant-strategies/qmt-four-seasons-v3/yearly_returns-r3.csv` | CSV | 年度收益表 | QMT-009 |
| SRC-005 | `raw/quant-strategies/qmt-four-seasons-v3/security_realized_pnl-r3.csv` | CSV | 标的平仓盈亏贡献 | QMT-011 |

## Local Full Archive

Full exported zip files, extracted logs and CSVs are preserved in the QuantTrading project:

- `/Users/pechen/AI/QuantTrading/strategies/qmt四季发财v3/results/backtest-export-2026-06-19-r3/`

The wiki raw folder stores the durable source subset needed for normal future Agent reasoning.

