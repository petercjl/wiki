---
title: DMP AI dialogue case evidence summary for item {BASE_ITEM_ID}
source_date: 2026-06-22
source_type: local research run summary
status: raw-source-summary
---

# DMP AI Dialogue Case Evidence Summary

This raw note preserves the evidence shape from the local DMP AI competitor
research run for base base item `{BASE_ITEM_ID}`. The formal wiki page should use this
as a case source together with the prompt manual and full-dimension workflow.

## Run Context

- Base item: `{BASE_ITEM_ID}`
- Product title: 防烫手套隔热加厚硅胶厨房烤箱专用烘焙耐高温防滑防热微波炉烘培
- Main period for sales, traffic, promotion and shop competition: 2026-06-13 to 2026-06-19
- Promotion scene single-day sample: 2026-06-19
- Audience profile period: 近30天
- Execution route: Chrome DevTools MCP controlling DMP AI dialogue.
- Isolation marker: `CLEAN_SKILL_20260622`
- Local output evidence:
  - `/Users/pechen/AI/Research/dmp_ai_competitor_research_{BASE_ITEM_ID}_clean_skill_20260622_full.json`
  - `/Users/pechen/AI/Research/DMP_AI_competitor_research_{BASE_ITEM_ID}_clean_skill_20260622_report.html`
  - `/Users/pechen/AI/Research/DMP_AI_competitor_research_{BASE_ITEM_ID}_clean_skill_20260622_evidence.xlsx`

## Main Dialogue Batches

| Batch | Prompt intent | Main internal route | Data obtained | Limitation |
|---|---|---|---|---|
| B01 | Subject identification | `tool_subject_identification_dataquery` | item, shop id, member id, category id/name | shop name was not returned |
| B02 | Competitor discovery from multiple views | `tool_competitive_detect_mining` | 16 candidate items from niche, keyword and star routes | bidding view had no structured rows |
| B06 | Relationship verification | `tool_competitor_explain_mining` | 4 candidates verified, with keyword, inflow/outflow, niche and star evidence | values are often intervals |
| B03/B03R | Peer operating benchmark | `tool_item_benchmark_dataquery(type=cust_type)` | exact peer item UV, conversion, add-to-cart, transaction amount and order count | peer table returned 4 rows in this run |
| B04 | Peer promotion benchmark | `tool_item_benchmark_dataquery(type=ad)` | exact peer item impressions, clicks, spend, ROI, transaction amount and order count | peer table returned 4 rows in this run |
| B05/B08 | Free traffic details and SQL aggregation | `tool_item_benchmark_dataquery(type=free)` + `tool_sql_query` | raw free-traffic rows and source-level aggregation | DMP returned 19 aggregate rows; report only persisted a 5-row preview before later QA |
| B09 | Competitor webwide and ad intervals | `tool_item_webwide_effect_dataquery` | sales, UV, add-to-cart, collect and ad effect intervals for selected competitors | competitor data is interval-masked |
| B10 | Promotion scene strategy | `商品推广场景策略明细数据` | campaign scene, bid/goal strategy, spend, impressions, clicks, add-to-cart and direct transaction amount | some competitor metrics are interval-masked |
| B07/B07R | Competitor audience profile | `tool_crowd_audience_insight` | buyer-crowd size and profile tag distribution for one competitor | only buyer behavior was deeply completed in this run |
| B11 | VIEW audience asset flow | `商品VIEW人群资产流入流出明细-同行优秀品视角` | V1/V2/I/E flow-in and flow-out between base item and competitors | mixed 3/7/15/30-day rows require careful filtering |
| B12 | Success path strategy | `tool_item_success_path_mining` | growth stage, budget structure, promotion goal, bidding mode and auxiliary tools | strategy is text-like, not a numeric table |
| B13 | Keyword asset | `BEST方法论关键词资产` | advertiser-level B/E/S/T keyword examples | latest partition fallback; not item-level or competitor-level |
| B15 | Shop competition and own ad diagnosis | `tool_shop_compete_analysis`, `tool_e_commerce_crowd_advertising_dataquery` | shop competition rows and empty own-ad-diagnosis result | 20 shop rows were returned but only 5 were persisted before later QA |
| B14 | Download attempt | `tool_download_data` | four dataset download attempts | datasets did not support download |

## Representative Case Data

| Module | Representative result |
|---|---|
| Subject | base item `{BASE_ITEM_ID}`, category `微波炉手套`, second category `厨用工具`, main category `厨房/烹饪用具` |
| Candidate pool | 16 candidate items across niche, keyword and star discovery routes |
| Strong competitor | `688909526916`, high relationship confidence, hit paths include business outflow, business inflow, niche, keyword and star |
| Keyword evidence | `隔热手套`, `微波炉手套`, `烤箱手套防烫加厚`, `防烫手套`, `烤箱手套` |
| Peer operating benchmark | exact 7-day values for base item and peer items, including UV, conversion, add-to-cart rate, GMV and order count |
| Peer promotion benchmark | exact 7-day values for impressions, clicks, spend, transaction amount, orders and ROI |
| Competitor interval data | selected competitors returned 7-day transaction amount, order count, UV, add-to-cart and collect intervals |
| Audience profile | competitor `688909526916` buyer crowd: 9,615 people in recent 30 days, with gender, age, city tier and other tag distributions |
| VIEW flow | base item and selected competitors had V1/V2/I/E flow-in/out rows with raw people counts |
| Strategy path | success path tool returned growth stage and campaign strategy such as full-site product promotion, ROI control and auxiliary tools |

## QA Notes

- The run proved that DMP AI dialogue can expose internal tool names, parameters,
  data IDs, schema fields, SQL-able datasets and data assets not visible in the
  ordinary front-stage UI.
- A report is not full merely because every dimension has a row. QA must compare
  DMP-declared returned row counts with persisted row counts.
- If DMP says 19 aggregate rows or 20 shop rows were returned, the skill/report
  must persist all rows or explicitly mark the table as a preview.
- Audience profile must be treated as a loop over competitor, behavior and tag
  set, not as a single buyer-crowd sample.
