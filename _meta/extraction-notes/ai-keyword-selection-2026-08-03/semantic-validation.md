---
title: 关键词推广AI选词语义校验
type: source-summary
created: 2026-08-03
updated: 2026-08-03
domain: meta
tags: [llm-wiki, semantic-validation, taobao]
sources:
  - raw/webpages/taobao/ai-keyword-selection-2026-08-03/document-package.json
  - raw/assets/ai-keyword-selection-2026-08-03/
status: active
---

# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: structured document extraction + original UI images
- Evidence sources: `document-package.json`, `content.md`, IMG-01—IMG-04
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

结构化正文不是 OCR 或 ASR，但操作路径、UI 标签和宣传数字会影响实际使用，因此仍执行高风险锚点校验。

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 标题、全文 | platform-or-product | AI选词 / 小万选词 / AI小万选词 | AI选词（界面可能显示“小万选词”或“AI小万选词”） | 标题、结构化正文、IMG-02、IMG-03 | high | accepted-as-is | 正文统一称 AI选词，操作说明保留界面别名 |
| A02 | 方式一、IMG-02 | UI path | 关键词推广→自定义推广→手动出价/智能出价→添加关键词 | 同原文 | 正文路径与新建计划截图相互支持 | high | accepted-as-is | 写入新建计划入口 |
| A03 | 方式二、IMG-03 | UI path | 关键词推广→自定义推广→手动出价/智能出价计划→单元→添加关键词 | 同原文 | 正文路径与存量计划截图相互支持 | high | accepted-as-is | 写入存量计划入口 |
| A04 | IMG-02 | UI labels | 商品特征推词 / 大盘效果找词 / 相似跟投 / 方法论选词 / 关键词拓写 | 同原图 | 清晰 UI 标签 | high | accepted-as-is | 作为可选选词视角，不扩写不存在的能力 |
| A05 | IMG-01 | metric/marketing claim | 秒级生成100+相关词、省去90%手动操作、手工耗时30分钟+ | 官方宣传口径，未独立验证 | 原始对比图 | high | accepted-as-is | 保留为来源声称，不作为效果保证或硬性参数 |
| A06 | IMG-03 | metric fields | 搜索指数、飙升度、竞争指数、市场点击率、市场点击转化率、市场平均出价 | 同原图 | 存量计划 UI 截图 | high | accepted-as-is | 用于说明生成后仍可查看市场指标，不推导排名算法 |
| A07 | IMG-04 | sensitive contact | 商家群二维码 | 不进入正式知识 | 原始二维码图 | high | excluded-from-formal | 原图仅保留 raw，避免传播时效性群入口 |

## Systematic Checks

- 全文检索 AI选词、小万选词、AI小万选词，正式页明确三者的界面命名关系。
- 两条操作路径按正文与截图交叉核对，均同时支持手动出价和智能出价计划。
- 100+、90%、30 分钟以上均标记为官方对比图宣传口径，不转写为保证。
- 商家群二维码不嵌入正式页。
