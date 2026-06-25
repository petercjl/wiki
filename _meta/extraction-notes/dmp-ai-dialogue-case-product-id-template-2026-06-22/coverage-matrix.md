---
title: DMP AI dialogue case {BASE_ITEM_ID} coverage matrix
type: source-summary
created: 2026-06-22
updated: 2026-06-22
domain: meta
tags: [dmp-ai, coverage]
sources:
  - raw/data/dmp-ai-dialogue-case-product-id-template-2026-06-22/DMP_AI_competitor_research_prompts.md
  - raw/data/dmp-ai-dialogue-case-product-id-template-2026-06-22/DMP_AI_full_dimension_competitor_workflow.md
  - raw/data/dmp-ai-dialogue-case-product-id-template-2026-06-22/case-evidence-summary.md
status: active
---

# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
|---|---|---|---|---|---|---|
| U001 | `DMP_AI_competitor_research_prompts.md` / 总体对话规则 | General DMP AI dialogue rule requiring tool, params, fields, `data_id`, failures | prompt contract | [[domains/电商运营/02-淘宝天猫/04-达摩盘AI/02-达摩盘AI对话挖掘竞品数据案例]] | formalized | Preserved as the opening reusable prompt. |
| U002 | `DMP_AI_competitor_research_prompts.md` / 1.1 | Subject identification prompt | execution node | same | formalized | Includes expected entity fields and case result. |
| U003 | `DMP_AI_competitor_research_prompts.md` / 1.2 | Four-view competitor discovery | execution node | same | formalized | Includes niche, keyword, bidding, star routes and case status. |
| U004 | `DMP_AI_competitor_research_prompts.md` / 1.5 | Relationship verification prompt | execution node | same | formalized | Includes method list, hit paths and keyword case. |
| U005 | `DMP_AI_full_dimension_competitor_workflow.md` / 第4层 | Benchmark operating data prompt | data route | same | formalized | Preserves `type=cust_type`, expected metrics and precise-value use. |
| U006 | `DMP_AI_full_dimension_competitor_workflow.md` / 第5层 | Benchmark promotion data prompt | data route | same | formalized | Preserves `type=ad`, expected metrics and precise-value use. |
| U007 | `DMP_AI_full_dimension_competitor_workflow.md` / 第6层 | Free traffic prompt and SQL aggregation | data route + SQL | same | formalized | Preserves SQL pattern and all-row persistence QA. |
| U008 | `DMP_AI_competitor_research_prompts.md` / 2.1-2.2 | Direct competitor webwide/ad interval query | data route | same | formalized | Preserves interval nature and benchmark-vs-direct distinction. |
| U009 | `DMP_AI_competitor_research_prompts.md` / 2.11 | Promotion scene strategy asset | data asset route | same | formalized | Preserves data asset query and expected fields. |
| U010 | `DMP_AI_competitor_research_prompts.md` / 2.7-2.9 | Crowd audience insight | audience route | same | formalized | Preserves 11-label buyer profile and future behavior-loop rule. |
| U011 | `DMP_AI_competitor_research_prompts.md` / 2.12 | VIEW audience asset flow | data asset route | same | formalized | Preserves flow-in/out prompt and V1/V2/I/E fields. |
| U012 | `DMP_AI_competitor_research_prompts.md` / 2.6 | Success path mining | strategy route | same | formalized | Preserves stage, budget, objective and tool fields. |
| U013 | `DMP_AI_full_dimension_competitor_workflow.md` / 店铺层 | Shop competition | shop-level route | same | formalized | Preserves full-row persistence rule. |
| U014 | `case-evidence-summary.md` / Representative Case Data | Case evidence from base item `{BASE_ITEM_ID}` | case evidence | same | formalized | Summarized without exposing full advertiser/member ID. |
| U015 | `case-evidence-summary.md` / QA Notes | QA lessons from partial persistence | QA rule | same | formalized | Turned into explicit future Agent QA rules. |

No meaningful source unit was intentionally omitted. Raw source files preserve the longer prompt/workflow variants.
