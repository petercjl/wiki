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
  - raw/webpages/joinquant/joinquant-kelly-position-sizing-2026-06-19.md
  - _meta/extraction-notes/joinquant-kelly-position-sizing-2026-06-19/coverage-matrix.md
status: active
---

# 量化交易知识域

本知识域沉淀量化交易平台、策略实现、回测兼容、数据 API、交易 API、资金管理、风险检查和 Agent 写策略规范。

## 基础地图

- [[domains/量化交易/00-股票量化知识地图|股票量化知识地图]]：股票量化策略的市场、数据、信号、组合、执行、风控、评估和知识入库框架。

## 平台

- [[domains/量化交易/01-聚宽/index|聚宽 JoinQuant]]：面向聚宽回测/模拟环境的策略写作、API 能力地图和报错排查。

## 策略风控与资金管理

- [[domains/量化交易/02-策略风控与资金管理/index|策略风控与资金管理]]：量化策略中的仓位、资金管理、止盈止损、黑天鹅和模型假设审计。
- [[domains/量化交易/02-策略风控与资金管理/01-凯利公式与量化仓位管理|凯利公式与量化仓位管理]]：把交易信号转成可下注模型，并用凯利公式估算理论仓位和实盘折扣。

## Agent 入口

- [[queries/joinquant-strategy-agent-entry|聚宽策略 Agent 使用入口]]

## 维护规则

- 平台官方 API 文档和真实回测报错都应先进入本知识域。
- 可稳定复用的写法和坑点应同步回写 Codex skill：`/Users/pechen/.codex/skills/joinquant-strategy`。
