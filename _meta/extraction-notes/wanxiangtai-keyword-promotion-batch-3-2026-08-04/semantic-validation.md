---
title: 万相台无界关键词推广第三批十文档语义校验
type: source-summary
created: 2026-08-04
updated: 2026-08-04
domain: meta
tags: [llm-wiki, semantic-validation]
sources:
  - raw/webpages/taobao/search-intent-retargeting-2026-08-04/content.md
status: active
---

# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: structured DingTalk document extraction + visual cross-check
- Evidence sources: content.md, tables.json, source images, official document tree, existing wiki
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | S01 预警条件 | threshold | 花费/预算>70%；展现<100 | 原样保留为当期触发条件 | 正文重复定义 | high | accepted-as-is | 标记版本快照 |
| A02 | S02 调整日期 | date-and-limit | 2026-02-06；30元→50元 | 新建计划最低日预算逐步调为50元 | 标题、正文、FAQ | high | accepted-as-is | 区分新建与存量 |
| A03 | S03 功能名 | product-version | 搜索人群追投、站外优质媒体合并 | 搜索意图全域追投 | 正文、图片和来源树 | high | accepted-as-is | 老功能作为历史版本 |
| A04 | S03 资源位 | placement | 首页猜你喜欢、购后猜你喜欢、站外优质媒体 | 三类当期资源位 | 正文与操作截图 | high | accepted-as-is | 执行时复核 |
| A05 | S03 效果数字 | promotion-metric | 展现+29%、点击+27%、PPC-11%、成交+15% | 官方近月平均宣称 | 正文重复但无样本 | high | accepted-as-is | 不作为单店保证 |
| A06 | S04 归因 | version-conflict | 旧版不归因关键词；新版归属意图词 | 按版本并列 | 两份官方文档 | high | accepted-as-is | 禁止跨版本混用 |
| A07 | S04 手动出价 | risk-boundary | 低价手动计划可能突破溢价上限 | 历史搜索人群追投风险 | FAQ | high | accepted-as-is | 只标历史版本 |
| A08 | S07 智能选品 | version-conflict | 潜力新品/引流/人群 vs 当前四目标 | 旧版选品方向快照 | 与既有 07 页及新来源对比 | high | accepted-as-is | 不覆盖当前版本 |
| A09 | S08/S09 权益门槛 | conflicting-limit | 3万元、5万元、大促3万元 | 多版本开放门槛冲突 | 两份正文多个位置 | high | unresolved | 只记录历史说法，当前后台复核 |
| A10 | S08 点击率公式 | metric-error | 搜索展现量/搜索点击量 | 来源疑似倒置 | 字段名称与通用定义冲突 | high | excluded-from-formal | 正式页不复制错误公式 |
| A11 | S08 跟投成功率 | formula | 成功展现量/总展现量 | 原样保留 | 正文、报表截图 | high | accepted-as-is | 解释成功与失败 |
| A12 | S09 流失防守 | audience-window | 15天内点击本品、竞品后链路互动、未成交 | 当期策略定义 | 正文 | high | accepted-as-is | 标记当期口径 |
| A13 | S10 成交口径 | formula | 总成交=直接+间接；直接成交=推广宝贝详情页成交 | 原样保留 | 表格与案例 | high | accepted-as-is | 作为决策主轴 |
| A14 | S10 提额建议 | percentage | 效果达标后日预算+10%—20% | 官方历史建议 | tips | high | accepted-as-is | 非硬规则 |
| A15 | S11 周期 | reporting-window | 7日成本、7日ROI、T+1抢位成功率 | 原样保留 | 表格与FAQ | high | accepted-as-is | 不用单日波动决策 |
