---
title: 量化策略案例库
type: concept
created: 2026-06-19
updated: 2026-06-19
domain: 量化交易
tags: [quant-trading, strategy, backtesting, case-library]
sources:
  - _meta/extraction-notes/qmt-four-seasons-v3/coverage-matrix.md
status: active
---

# 量化策略案例库

本目录收录已经完成“策略代码 + 回测导出 + 审计日志 + 本地分析”的策略案例。案例页不是投资建议，而是用于沉淀策略结构、信号假设、执行经验、回测证据、失效边界和可复用 Agent 工作流。

## 策略案例

- [[domains/量化交易/03-策略案例/01-QMT四季发财ETF轮动策略案例|01｜QMT四季发财 ETF 轮动策略案例]]：基于聚宽社区策略的 ETF 单标的轮动案例，覆盖长期动量稳定性得分、短期动量/RSI/ATR 风控、2020-2025 回测证据和日志瘦身经验。

## 入库原则

- 不直接把社区策略收益当作结论；必须记录回测区间、基准、成本、滑点、订单失败和日志完整性。
- 策略逻辑页和平台方法页分开：策略页回答“这个策略做了什么、表现如何、边界是什么”，平台方法页回答“如何让 Agent 复盘和取证”。
- 如果策略暴露通用风险或平台坑点，应同步回链到 [[domains/量化交易/01-聚宽/index|聚宽 JoinQuant]] 和 [[domains/量化交易/00-股票量化知识地图|股票量化知识地图]]。

