---
title: 自选词广泛与精准匹配 audit handoff
type: source-summary
created: 2026-08-03
updated: 2026-08-03
domain: meta
tags: [llm-wiki, audit-handoff, taobao, keyword-matching]
sources:
  - raw/webpages/taobao/self-selected-keywords-matching-2026-08-03/content.md
  - raw/webpages/taobao/self-selected-keywords-matching-2026-08-03/document-package.json
  - raw/assets/self-selected-keywords-matching-2026-08-03/
status: active
---

# 自选词广泛与精准匹配 Audit Handoff

## Source

- Adapter: `web-clipping`
- Raw path: `raw/webpages/taobao/self-selected-keywords-matching-2026-08-03/`
- Image path: `raw/assets/self-selected-keywords-matching-2026-08-03/`
- Original URL/path: https://alidocs.dingtalk.com/i/nodes/Obva6QBXJwxNZoMOCgk2jAGe8n4qY5Pr
- Capture date: 2026-08-03
- Current-doc verification: 抓取当日由授权会话返回结构化文档包；页面记录更新时间为 2026-04-16

## Outputs

- Source profile: `source-profile.md`
- Source inventory: `source-inventory.md`
- Semantic validation: `semantic-validation.md`（passed）
- Image inventory: `image-inventory.md`
- Image analysis: `image-analysis.md`
- Knowledge-unit inventory: `knowledge-unit-inventory.md`
- Coverage matrix: `coverage-matrix.md`
- Omission audit: `omission-audit.md`
- Formal page plan: `formal-page-plan.md`
- Formal pages:
  - `domains/电商运营/02-淘宝天猫/万相台无界白皮书/01-关键词推广/03-关键词百宝箱：四类词包与分阶段投放策略.md`
  - `domains/电商运营/02-淘宝天猫/万相台无界白皮书/01-关键词推广/index.md`

## Placement Confirmation

- Source understanding: 自选词入口、匹配标识、五类推荐词和三类买词来源
- Existing category considered: 关键词百宝箱正式页
- Recommended placement: 扩展既有第 3 页的自选词章节
- Recommended disposition: `extend-existing-with-section`
- Alternatives considered: 新建第 4 页；因与既有内容高度重叠而放弃
- User confirmation: 已确认批次 placement
- Confirmation evidence: 用户确认十模块逐篇入库，并在上一份完成后回复“继续”
- Final confirmed path: `domains/电商运营/02-淘宝天猫/万相台无界白皮书/01-关键词推广/03-关键词百宝箱：四类词包与分阶段投放策略.md`

## Coverage Summary

- Source units: 24
- formalized: 20
- merged: 3
- raw-only: 1
- omitted-with-reason: 0
- unresolved: 0
- Image coverage: 5 archived / 5 formalized / 0 merged / 0 raw-only / 0 unresolved / 5 embedded

## Expected Agent Use

- Future questions this source should support: 从哪里添加自选词、怎样识别精准/广泛、五类推荐词是什么、助攻词是什么、自己怎样找关键词
- Pages an Agent should read first: `domains/电商运营/02-淘宝天猫/万相台无界白皮书/01-关键词推广/03-关键词百宝箱：四类词包与分阶段投放策略.md`
- Query/playbook entries: 不新增 query；由关键词推广模块索引路由

## Known Risks

- Time-sensitive claims: UI 路径、标签、0/180 容量、指标字段、匹配术语和规则
- Sensitive data removed: 未保存认证或个人数据
- Sensitive image handling: none
- Weak source areas: 推荐算法、指标更新时间、效果阈值和 MTA 模型细节未披露
- User confirmation needed: none

## Self-Validation

- No formal write before placement confirmation: yes
- Ingest contract validation: passed（`llm-wiki-ingest contract OK`，Python 3.14.3）
- Placeholder scan: passed
- Representative term search: passed（入口、方括号、五类推荐词、MTA、0/180 和三类买词来源均命中）
- Image embedding check: passed（5/5 逻辑图片正式化并嵌入；10 个归档实例均有 disposition）
- Route audit: passed（模块入口 8 条反向链接、7 条出链、无目标页警告）
- Index/log check: passed（既有正式页、模块索引、总索引和日志已更新；正式页总数保持 493）
- Remaining gaps: 当前单篇无未决项；UI 容量、推荐算法、指标口径和 MTA 模型需按当前后台复核
