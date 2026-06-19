---
title: 量化交易知识域
type: concept
created: 2026-06-19
updated: 2026-06-19
domain: 量化交易
tags: [quant-trading, backtesting, strategy]
sources:
  - raw/api/joinquant/joinquant-api-2026-06-19.md
  - _meta/extraction-notes/joinquant-api-2026-06-19/coverage-matrix.md
status: active
---

# 量化交易知识域

本知识域沉淀量化交易平台、策略实现、回测兼容、数据 API、交易 API、风险检查和 Agent 写策略规范。

## 平台

- [[domains/量化交易/01-聚宽/index|聚宽 JoinQuant]]：面向聚宽回测/模拟环境的策略写作、API 能力地图和报错排查。

## Agent 入口

- [[queries/joinquant-strategy-agent-entry|聚宽策略 Agent 使用入口]]

## 维护规则

- 平台官方 API 文档和真实回测报错都应先进入本知识域。
- 可稳定复用的写法和坑点应同步回写 Codex skill：`/Users/pechen/.codex/skills/joinquant-strategy`。
