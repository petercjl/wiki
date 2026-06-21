---
title: GitHub 量化理论资料 omission audit
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, omission-audit, quant-trading]
sources:
  - raw/github/quant-theory-github-sources-2026-06-20/
status: active
---

# Omission Audit

| item | disposition | reason |
| --- | --- | --- |
| GitHub badges, install commands, community links | raw-only | 不是量化理论知识；保留在 raw 中即可。 |
| README 中的长代码示例 | raw-only | 当前目标是研究理论，不是复现这些工具；代码细节日后需要接入工具时再单独入库。 |
| 图片链接与徽章 | raw-only | 多为工具展示或装饰；不影响理论页使用。 |
| 具体 benchmark 数值 | merged | 只抽取“成本前后要分开评估、指标应包含年化/IR/回撤”等原则，具体数字可能随版本和数据变化，不作为 Peter 策略结论。 |
| purged-cross-validation 的医学/工程示例 | raw-only | 示例领域不是金融策略本体；其时间序列泄漏原则已 formalized。 |

## Unresolved

- 无必须用户判断的未决项。
- 若未来要把 Qlib/Alphalens/Pyfolio 实际接入本地分析工具，需要重新读取对应 API 文档和代码示例。

