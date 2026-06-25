---
title: 山峰组259期6-15/6-16课程源资料画像
type: source-summary
created: 2026-06-26
updated: 2026-06-26
domain: meta
tags: [llm-wiki, ingest, transcript, ecommerce, taobao]
status: active
---

# 山峰组259期6-15/6-16课程源资料画像

## Source Identity

- Source identity: 山峰组259期6-15/6-16课程
- Working title: 淘宝智能推广与人群运营系统
- Adapter: `llm-wiki-ingest/adapters/transcript.md`
- Batch type: two transcript-derived Markdown files from the same 259期 course sequence.
- Formal language: Chinese.

## Raw Files

| Part | Original path | Raw archive | SHA-256 |
| --- | --- | --- | --- |
| Part 1 | `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-15 259期.md` | `raw/transcripts/shanfeng-259-taobao-smart-promotion-audience-operations-course-2026-06-15-16/part1-2026-06-15-259.md` | `cc3c06078e55f358ef69750b15195b9ef992397a069c8ce615199f607e825db2` |
| Part 2 | `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-16 259期.md` | `raw/transcripts/shanfeng-259-taobao-smart-promotion-audience-operations-course-2026-06-15-16/part2-2026-06-16-259.md` | `a3aca7acfe1e0a6c5ed0ef1dd19256e305812bcac077c40c0e5f49069b90eb34` |

## Source Shape

| Part | Date/time | Approx size | Shape | Main topics |
| --- | --- | ---: | --- | --- |
| Part 1 | 2026-06-15 09:40 | 60,351 chars | Long raw transcript, noisy ASR | 淘宝趋势、全域化/全球化、合规与品牌化、曝光价值公式、721/172/333/127 店铺模型、人群资产流转、成交机会/成交规模、标签市场实操、归因与转化周期、控成本/控投产/最大化/手动出价、标准计划与智能计划 |
| Part 2 | 2026-06-16 09:29 | 5,446 chars | AI meeting-note/course summary | 智能计划测图/测款/动销/低价引流、高投产计划组、相似品跟投、搜索卡位、流量金卡、人群推广、空烧与互抢、报表分析 |

## Domain Placement

- Primary placement: `domains/电商运营/02-淘宝天猫/06-淘宝智能推广与人群运营系统/`
- Related placement:
  - `domains/电商运营/02-淘宝天猫/05-淘宝付费投放与全站推广/`
  - `domains/电商运营/01-通用电商方法/04-选品与运营增长/02-产品类型与爆款运营系统/`
  - `domains/电商运营/02-淘宝天猫/04-达摩盘AI/`

## Existing Memory Found

- `淘宝付费投放与全站推广`: covers 253期 all-site scaling, link dispersion, audience/material testing, short-video 拉新/收割.
- `产品类型与爆款运营系统`: covers 256期 product type, lifecycle, S/A/B, high-ticket and ToB operating logic.
- `达摩盘 AI`: covers DMP/达摩盘 AI data mining and audience analysis, but not this course's operational use of audience assets and plans.

## Fusion Decision

- Create new formal learning path under 淘宝天猫.
- Reason: 259期 is platform-specific and centered on 淘宝后台推广、人群资产、智能计划、搜索卡位、归因 and plan diagnostics. It extends 253 and 256, but is not duplicate.
- Cross-link rather than merge:
  - 253 = all-site paid scaling branch.
  - 256 = product-type and lifecycle decision layer.
  - 259 = 淘宝-specific smart promotion and audience operation layer.

## Sensitivity And Time Risk

- Contains platform backend tool names and UI paths that may change over time.
- Formal pages should preserve business logic and mark backend-specific names as subject to current backend verification.
- ASR has obvious noise:
  - `淘气` likely `淘系/淘宝`.
  - `AHB` likely `AI + ?` unclear; preserve as AI tool trend without relying on exact term.
  - `龙虾` likely AI agent/tool name drift; preserve as AI automation trend only.
  - `MTA/MPI/MTIV/MPA` appear as attribution-related terms; normalize cautiously as multi-touch attribution / MTA-like attribution, mark backend term as待确认.
  - `他人群` likely `TA人群`.
  - `搜索疑似/搜索点击量` likely backend search click conversion path; preserve concept rather than exact UI wording when uncertain.

