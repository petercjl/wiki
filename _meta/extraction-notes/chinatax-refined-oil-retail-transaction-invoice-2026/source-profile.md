---
title: 成品油零售领域交易即开票政策解读来源档案
type: source-summary
created: 2026-06-16
updated: 2026-06-16
domain: meta
tags: [llm-wiki, tax-compliance, invoice, chinatax, 成品油零售]
sources:
  - raw/webpages/chinatax/chinatax-refined-oil-retail-transaction-invoice-2026.md
status: active
---

# Source Profile

## Source identity

- Source title: 成品油零售领域“交易即开票”政策解读
- Source slug: `chinatax-refined-oil-retail-transaction-invoice-2026`
- Original URL: https://fgk.chinatax.gov.cn/zcfgk/c100015/c5250350/content.html
- Raw path: `raw/webpages/chinatax/chinatax-refined-oil-retail-transaction-invoice-2026.md`
- Source type: webpage / policy interpretation Q&A
- Adapter: `llm-wiki-ingest/adapters/web-clipping.md`
- Capture date: 2026-06-16
- Language: 中文

## Memory-first classification

- Primary durable domain: `domains/财税与经营财务/01-电商财税合规/`
- Alternative candidate domains:
  - `domains/电商运营/01-通用电商方法/`：可承接商户经营流程影响，但本源材料的核心是发票合规与税务监管，不是平台运营方法。
  - `domains/电商运营/30-ERP与系统工具/`：可承接 POS/零售系统改造方法，但本源材料没有给出通用 ERP/API 技术规范，系统部分应作为财税合规页中的软件需求拆解。
  - `projects/`：不属于某个具体项目资料。
- Final placement decision: create a new formal playbook page under 财税与经营财务 / 电商财税合规.
- Classification rationale: source knowledge primarily answers “成品油零售交易如何合规开票、什么情况下可即时/汇总/换开发票、系统应满足什么合规链路”，属于发票合规与税务执行规则。

## Existing memory search

Search terms used:

- `交易即开票`
- `乐企平台`
- `乐企自用`
- `乐企联用`
- `成品油零售`
- `加油卡`

Search result before this ingest:

- No existing formal wiki page was found for `交易即开票` / `乐企平台` / `成品油零售`.
- Existing related pages in the same domain:
  - `domains/财税与经营财务/01-电商财税合规/04-增值税进销项与发票管理.md`
  - `domains/财税与经营财务/01-电商财税合规/02-电商税务合规路径与红线.md`
- Obsidian CLI probe after page creation routes the new page as the only detail page for this concept.

## Fusion disposition

- Proposed disposition: `create-new`
- Reason: no suitable existing page specifically covered 成品油零售“交易即开票”、乐企自用/联用、加油卡充值/消费开票二选一、自然人/单位汇总开票边界、以及 2026-11-01 过渡期。
- Associative fusion used:
  - The new page links to `增值税进销项与发票管理` as the broader invoice-management concept.
  - The new page links to `电商税务合规路径与红线` as the broader tax-compliance risk context.
  - Domain index and root index include the new durable page.
- Destructive merge: not used. Existing invoice/tax pages remain as broader concepts.

## Sensitivity and currentness

- Sensitivity: public policy content; no private or credential data.
- Time sensitivity: high.
- Current-doc verification requirement: execution before business/system rollout must verify State Taxation Administration notices, 乐企平台 technical standards, and local tax bureau implementation requirements.

## Expected formal artifacts

- Raw archive under `raw/webpages/chinatax/`.
- Extraction notes under `_meta/extraction-notes/chinatax-refined-oil-retail-transaction-invoice-2026/`.
- Formal playbook page: `domains/财税与经营财务/01-电商财税合规/09-成品油零售交易即开票规则.md`.
- Index/log updates.
