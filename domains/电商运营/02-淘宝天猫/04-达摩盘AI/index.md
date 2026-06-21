---
title: 达摩盘 AI
type: index
created: 2026-06-20
updated: 2026-06-20
domain: 电商运营
tags: [ecommerce, taobao, tmall, dmp-ai, marketing-data]
sources:
  - raw/data/dmp-ai-internal-tools-2026-06-20/DMP_AI_internal_tools.md
  - _meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/coverage-matrix.md
status: active
---

# 达摩盘 AI

本目录沉淀淘宝/天猫达摩盘 DMP AI 的内部工具、数据资产、竞品挖掘路线、调用话术和边界测试。它归入淘宝天猫平台专属的数据化营销工具，而不是通用 ERP/API。

## 阅读顺序

1. [[domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册|达摩盘 AI 内部工具与竞品数据挖掘手册]]：完整保留内部工具、数据资产、参数、样例、结果和边界测试。
2. [[queries/达摩盘AI竞品数据挖掘|达摩盘 AI 竞品数据挖掘查询入口]]：未来 Agent 处理竞品销售、搜索词、推广、人群数据问题时的入口。

## 能力范围

- 竞品识别与解释：`tool_competitive_detect_mining`、`tool_competitor_explain_mining`、`tool_competitor_mining_busi_flow`。
- 竞品销售/推广基准：`tool_item_benchmark_dataquery`、`tool_item_webwide_effect_dataquery`、`商品推广场景策略明细数据`。
- 竞品人群画像和行为人群：`tool_crowd_audience_insight`、VIEW/DEEPLINK 相关数据资产。
- 自家广告诊断与 SQL 深挖：`tool_e_commerce_crowd_advertising_dataquery`、`tool_sql_query`、`tool_download_data`。
