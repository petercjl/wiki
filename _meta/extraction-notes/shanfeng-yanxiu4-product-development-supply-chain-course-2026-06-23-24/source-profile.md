---
title: 山峰组研修4班6-23/6-24课程 source profile
type: source-summary
created: 2026-06-26
updated: 2026-06-26
domain: meta
tags: [llm-wiki, ingest, transcript, ecommerce, supply-chain]
status: active
---

# Source Profile

## Source Identity

- Source title: 山峰组研修4班6-23/6-24课程：产品开发与供应链管理
- Source files:
  - `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-23 研修4班.md`
  - `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-24 研修4班.md`
- Raw archive:
  - `raw/transcripts/shanfeng-yanxiu4-product-development-supply-chain-course-2026-06-23-24/part1-2026-06-23-yanxiu4.md`
  - `raw/transcripts/shanfeng-yanxiu4-product-development-supply-chain-course-2026-06-23-24/part2-2026-06-24-yanxiu4.md`
- Source type: course transcript / AI minutes.
- Adapter: `llm-wiki-ingest/adapters/transcript.md`.
- Language: Chinese.
- Date: 2026-06-23 and 2026-06-24.
- Duration in source:
  - 2026-06-23: 5 hours 22 minutes.
  - 2026-06-24: 1 hour 10 minutes.

## Hashes

| Part | Original SHA-256 | Raw SHA-256 | Status |
| --- | --- | --- | --- |
| 2026-06-23 | `51c16e61dbb9d7e767211f5c87346cdd33a35036acad59751eb8b6571ad0494b` | `51c16e61dbb9d7e767211f5c87346cdd33a35036acad59751eb8b6571ad0494b` | matched |
| 2026-06-24 | `e57c475eed133e835712f007839c073cd9cbe1699259aeebab65c38c3b5b4d62` | `e57c475eed133e835712f007839c073cd9cbe1699259aeebab65c38c3b5b4d62` | matched |

## Placement Decision

Primary domain:

- `domains/电商运营/01-通用电商方法/05-产品开发与供应链管理系统/`

Reason:

- The course is platform-independent ecommerce operating knowledge.
- The core problem is not Taobao ad operation or brand positioning alone, but the operating backbone behind products: product development, supplier development, cost structure, sampling, quality control, inventory turnover, replenishment, slow-moving inventory, and cross-functional collaboration.
- It should link to, but not merge into, `产品类型与爆款运营系统`, because that existing package focuses on product type, lifecycle, and explosive growth mechanics; this course adds supply-chain execution depth.

Related memory:

- `domains/电商运营/01-通用电商方法/04-选品与运营增长/02-产品类型与爆款运营系统/`
- `domains/电商运营/01-通用电商方法/04-选品与运营增长/01-电商运营与选品策略深度解析/`
- `domains/电商运营/02-淘宝天猫/01-淘宝运营速成指南/09-供应链、仓储与财务控制.md`
- `domains/财税与经营财务/05-内控与组织能力/02-资金、库存与权限内控.md`

## Formal Output Plan

- `index.md`: learning path and model overview.
- `01-产品开发思维与市场机会判断.md`.
- `02-供应商开发与分级管理.md`.
- `03-供应商谈判打样与品质管理.md`.
- `04-成本结构利润模型与SKU角色.md`.
- `05-库存周转补货与跨部门协同.md`.
- `06-Agent使用模板：产品开发与供应链诊断.md`.
- `queries/产品开发与供应链管理诊断.md`.

## Transcript Quality

- The files are AI minutes rather than verbatim transcript.
- They contain useful structured summaries, examples, numbers, and action items.
- Some image links point to external OSS screenshots; the text already includes the extractable knowledge, so image URLs are preserved in raw only.
- Classroom logistics and AIGC export metadata are raw-only.

## Source Identity Requirement

Every formal page must mark:

```yaml
source_title: 山峰组研修4班6-23/6-24课程
```

