---
title: QMT四季发财v3 省略审计
type: source-summary
created: 2026-06-19
updated: 2026-06-19
domain: meta
tags: [coverage, omission, quant-trading]
sources:
  - _meta/extraction-notes/qmt-four-seasons-v3/coverage-matrix.md
status: active
---

# QMT四季发财v3 省略审计

| item | disposition | reason |
| --- | --- | --- |
| 完整 `log.txt` | raw-only in project archive | 日志体积较大且有 HTML 转义；wiki raw 保留检查报告和结构化 summary，完整日志留在 `/Users/pechen/AI/QuantTrading/.../backtest-export-2026-06-19-r3/`。 |
| 完整交易/持仓 zip | raw-only in project archive | wiki raw 保留聚合分析与 CSV 派生表；完整 zip 保留在策略项目目录，避免 wiki raw 体积膨胀。 |
| 逐日候选 TOP 明细 | merged | 通过 `rebalance_universe_summary` 的事件设计进入方法页，不逐日展开。 |
| 社区原作者完整历史叙述 | raw-only | 策略脚本头部保留来源；正式页只使用策略逻辑与回测证据。 |
| 投资建议/可实盘推荐 | omitted-with-reason | 回测结果不等于投资建议；仍有现金不足订单失败和过高换手，需要标注边界。 |

