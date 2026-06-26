---
title: 白泽国际站运营实战系统课 audit handoff
type: source-summary
created: 2026-06-25
updated: 2026-06-27
domain: meta
tags: [llm-wiki, audit-handoff, ecommerce, cross-border]
sources:
  - raw/videos/baize-alibaba-international-station-course-2026-06-25/
  - raw/transcripts/baize-alibaba-international-station-course-2026-06-25/
status: active
---

# Audit Handoff｜白泽国际站运营实战系统课

## Source

- Raw source: `raw/videos/baize-alibaba-international-station-course-2026-06-25/`
- Adapter used: `llm-wiki-ingest/adapters/transcript.md` with video keyframe/OCR supplement
- Original path: `/Users/pechen/alibaba/白泽/`
- Capture/ingest date: 2026-06-25
- Current-doc verification: platform-specific backend rules, metric names, and tool names must be checked against the current Alibaba International Station backend before execution.

## Outputs

- Source profile: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/source-profile.md`
- Source inventory: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/source-inventory.md`
- Knowledge unit inventory: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/omission-audit.md`
- Formal pages planned: see `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/formal-page-plan.md`

## Formal Pages Created

- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/index.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/01-国际站运营能力框架.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/02-运营思维框架与跨行业迁移.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/03-运营实战技能迭代方法.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/04-店铺基础技能学习与知识体系梳理.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/05-国际站后台十关键词运营系统.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/06-国际站首页流量入口地图.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/07-店铺SEO基础布局.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/08-平台规则与搜索排序机制.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/09-店铺综合实力与搜索排名指标.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/10-买家喜好度与千人千面标签匹配.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/11-一级引擎与橱窗搜索加权.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/12-店铺权重与单品权重提升.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/13-违规处罚与店铺运营风控.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/14-店铺规划与定位方法.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/15-赛道选择与四大流量入口.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/16-主打产品切入与产品线布局.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/17-目标国家与买家画像分析.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/18-公司优势表达与信任转化.md`
- `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/19-出口通与金品店铺应用.md`
- Latest added formal pages include `61-标题精细化组合与批量覆盖.md` through `67-标题方法选择避坑与爆款矩阵.md`; full current page list is maintained in `formal-page-plan.md` and the course `index.md`.
- `queries/阿里巴巴国际站运营诊断.md`

## Coverage Summary

- Source units in main coverage matrix: 301.
- formalized: 298.
- merged: 1 in the main coverage matrix; repeated CH05 slide promise is classified as `merged` in `ch05/omission-audit.md`, and CH93 is merged with CH94 because the file title and content diverge.
- raw-only: 2 in the main coverage matrix, plus CH05 classroom transition and garbled OCR subtitle fragments in chapter omission audit.
- omitted-with-reason: 0 in the main coverage matrix; CH08 APP-specific detail is marked omitted-with-reason in `ch08/omission-audit.md` because the course explicitly does not cover APP in this chapter.
- unresolved: 2 known ASR terms from earlier chapters (`奥义加`, `报品/报增`) remain in omission audit for optional quote-level verification.

## Current Status

- Raw videos copied for CH01-CH113.
- CH01-CH113 audio extracted.
- CH01-CH113 keyframes extracted; CH06-CH99 OCR captured at 15-second intervals where available and CH100-CH113 at 20-second intervals.
- `whisper-cpp` installed via Homebrew.
- `ggml-large-v3-turbo.bin` downloaded to `/Users/pechen/.local/share/whisper.cpp/models/`.
- CH01-CH113 raw Whisper transcripts archived under `raw/transcripts/baize-alibaba-international-station-course-2026-06-25/`.
- Transcript-derived knowledge units formalized; CH10-CH12 add platform rules and search sorting, CH13 adds comprehensive strength indicators, CH14-CH15 add buyer preference and personalization, CH16-CH17 add first-level engine/showcase weighting, CH18-CH19 add store/product weight improvement, CH20-CH29 add compliance risk, store positioning, traffic track selection, product-line layout, target country, buyer persona, trust conversion, store type, and through-train focus, CH30-CH39 add second-curve store planning, RTS/custom differentiation, product selection, rising-keyword selection, peer-store selection, Market Advisor case workflow, and keyword-root coverage, CH40-CH49 add keyword classification, keyword selection standards, true keyword-product matching, keyword collection tables, high-quality product publishing, product grouping, marketing detail/storefront pages, premium-product models, and strength-product improvement, CH50-CH59 add hot-product quantity growth, premium-product rights, showcase selection/optimization, keyword-ranking validation, store star-level framework, product power and marketing power, CH60-CH69 add transaction power, fulfillment power, product data diagnosis, quadrant optimization, hot-product order conversion, platform traffic structure and traffic-channel growth, CH70-CH79 add market analysis, Market Advisor industry/country workflows, competitor analysis, store diagnosis SOP, comprehensive data analysis, product-level fine diagnosis, and diagnostic data-source selection, CH80-CH89 add inquiry conversion/quality, traffic volatility, P4P repair, activity/scene traffic, campaign planning and new-store staging, CH90-CH99 add new/old-store execution SOPs, store traffic growth strategy, title logic, title rules, K1/K2/K3 and hot-title frameworks, and CH100-CH113 complete the title system with batch title combination, K1/K2/K3补充, RTS/custom title differences, neutral hot titles, competitor borrowing, blue-ocean/model/country-preference titles, 我的词库, potential-product title optimization, method selection, title pitfalls and hot-product matrix thinking.

## Known Unresolved Items

- Need optional quote-level audio review for ASR uncertain words: `奥义加`, `报品/报增`.
- Need determine whether future later chapters contain dense slide pages requiring denser keyframe extraction/OCR.
- Platform-specific operational rules must be treated as course-derived until checked against current Alibaba.com backend behavior.
- CH05 OCR is useful for slide title/outcome confirmation but not clean enough for exact subtitle quotation; ASR is the higher-quality text source.
- CH08 is screen-heavy and OCR is noisy; use raw keyframes only for audit and current UI comparison, not exact current platform instructions.
- CH09 SEO rules should be treated as foundational course guidance, not a guarantee of current ranking mechanics.
- CH10-CH19 search ranking, engine-tier, showcase, P4P, store type, star-level and product-type rules are course-derived and must be checked against the current Alibaba International Station backend before use as SOP.
- CH20-CH29 platform-specific penalty rules, data-tool entrances, product-type entrances, RTS/half-managed definitions, export pass/gold supplier rights, and through-train tactics are course-derived and must be checked against the current Alibaba International Station backend before use as SOP.
- CH30-CH39 platform-specific data-tool entrances, selected-word advisor charts, Market Advisor fields, Buyer Advisor fields, peer-store ranking views, and keyword-index outputs are course-derived and must be checked against the current Alibaba International Station backend before use as SOP.
- CH40-CH49 keyword-index fields, product-publishing scoring rules, logistics-template limits, storefront/detail-page modules, 商品运营工作台 labels, 优品运营 rights, and strength-product thresholds are course-derived and must be checked against the current Alibaba International Station backend before use as SOP.
- CH49 includes risky raw wording around `补询盘/补订单`; formal pages intentionally reframe this as compliant real-customer online conversion and do not recommend false inquiries/orders.
- CH49 OCR has one noted Tesseract frame crash; remaining OCR, keyframes and ASR provide adequate coverage unless quote-level visual verification is required.
- CH50-CH59 platform-specific爆品 thresholds, 优品权益 labels, 橱窗 backend UI, ranking-check tools, 星等级 score/time rules, 商品力/营销力 index definitions and marketing-resource labels are course-derived and must be checked against the current Alibaba International Station backend before use as SOP.
- CH50 includes risky raw wording around `补询盘/补订单/买家账号`; formal pages intentionally reframe this as compliant real-customer online conversion and do not recommend false inquiries/orders.
- CH60-CH69 platform-specific transaction attribution, 发货率 thresholds, product-analysis backend fields, four-quadrant thresholds, Traffic Advisor labels and channel proportions are course-derived and must be checked against the current Alibaba International Station backend before use as SOP.
- CH60-CH61 include risky raw wording around transaction, review and fulfillment manipulation; formal pages intentionally reframe this as compliant real-customer online conversion, true satisfied-customer evaluation, real logistics correction and fulfillment-process repair.
- CH70-CH79 platform-specific Market Advisor fields, supply-demand ratio definition, country preference fields, competitor-analysis tool availability, diagnosis-data entrances and product 360 backend field names are course-derived and must be checked against the current Alibaba International Station backend before use as SOP.
- CH74 discussion of inquiry-count benchmarks is formalized only as competitive benchmark estimation, not as any fake inquiry action.
- CH80-CH89 platform-specific diagnostic entrances, P4P behavior, activity-center labels, scene-traffic thresholds, 新贸节/采购节会场规则 and new-store stage timing are course-derived and must be checked against the current Alibaba International Station backend before operational SOP use.
- CH82 and CH84 order-binding discussion is formalized only as real-customer, real-order and compliant online transaction feedback.
- CH86 wording around offsetting discounts via logistics is not formalized as an action; formal page keeps truthful logistics information and compliant margin/discount controls.
- CH87 `会采购/汇采购` label and thresholds are kept with current-backend verification warnings.
- CH90-CH99 title rules, symbol parsing, character-length guidance, K1/K2/K3 behavior, search-index ordering and hot-title budget examples are course-derived and must be checked against current Alibaba International Station backend and category data before operational SOP use.
- CH90 real-transaction signal guidance is formalized only as true customer, true order, true fulfillment and compliant online transaction feedback.
- CH93 file title/content mismatch is recorded; formal knowledge treats it as a duplicate title-logic source rather than a through-train learning-guide page.
- CH100-CH113 title methods, K1/K2/K3 fields, 我的词库 markers, search-index metrics, country-preference filters, model-number search behavior, 7-14 day optimization cadence and hot-product matrix examples are course-derived and must be checked against current Alibaba International Station backend and category data before operational SOP use.
- CH100 filename/content mismatch (`74个步骤` vs `4个步骤`) and CH113 filename/content mismatch are recorded; formal knowledge follows the transcript content while preserving raw filenames.
- CH109 source audio emitted one AAC decode warning during WAV extraction, but ASR completed the full chapter duration; recheck only if quote-level audio proof is needed.

## Expected Future Agent Use Cases

- Diagnose Alibaba International Station store inquiry-growth bottlenecks.
- Evaluate an operator's capability gaps and learning route.
- Convert platform operation problems into reusable thinking frameworks.
- Build training material or checklists for Alibaba International Station operators.
- Diagnose backend module gaps through the ten-keyword system.
- Diagnose homepage traffic-entry and SEO-layout problems before proposing ads or product changes.
- Diagnose search ranking bottlenecks by splitting platform compliance, search matching, comprehensive strength, buyer preference, first-level engine access, and store/product weight.
- Diagnose store planning, target country, buyer persona, product-line layout, trust conversion, export pass/gold supplier choice, and through-train focus problems.
- Diagnose second-curve product/category expansion, RTS/custom resource allocation, product selection, trend/rising keyword selection, peer-store borrowing, Market Advisor product-country-keyword workflows, and keyword-root coverage.
- Diagnose keyword type selection, P4P keyword waste, keyword-product mismatch, keyword table completeness, 4.5/4.9 product publishing gaps, product grouping, detail page/storefront conversion, premium-product quantity, and strength-product improvement.
- Diagnose hot-product quantity, premium-product rights and thresholds, showcase product selection, showcase weekly optimization, keyword-ranking validation, star-level score bottlenecks, product-power gaps, marketing-power gaps, and high-consumption no-opportunity products.
- Diagnose transaction-power and fulfillment-power star-level bottlenecks, product data chains, eight product-diagnosis factors, CTR/inquiry quadrant optimization, hot products with many inquiries but few orders, platform traffic structure, traffic source quality, and buyer-retention/channel-loss problems.
- Diagnose market/category/country opportunity with Market Advisor, competitor store/product gaps, store-diagnosis four questions, store comprehensive data, product 360 fine diagnosis, visitor validity, country/crowd precision, keyword-product fit and diagnostic data-source choice.
- Diagnose inquiry conversion rate, inquiry quality, traffic spikes/drops, low-inquiry-volume store revival, P4P inquiry decline, official activity/coupon setup, ranking/new-product/sourcing scene traffic, new trade festival/procurement festival planning and new-store three-stage operation.
- Diagnose title batch coverage, K1/K2/K3 supplement strategy, RTS/custom title fit, neutral hot-title stability, competitor-title borrowing, blue-ocean/model/country-preference title opportunities, keyword-library gaps, potential-product title optimization, title method selection and hot-product matrix planning.

## Self-Validation

- Ingest contract after CH10-CH19 update: OK. Script emitted verbatim-match warnings for older coverage rows because formal pages reconstruct source units rather than copying coverage wording.
- Ingest contract: OK. `validate_ingest_contract.py --notes-dir ... --raw ...` returned `llm-wiki-ingest contract OK`. Passing the formal directory to `--formal` is unsupported by the script and raises `IsADirectoryError`, so formal pages were checked separately.
- Placeholder scan: `SHELL:0 THIN:0 OK:8` for formal course pages.
- Representative term search: `十关键词`, `首页流量入口`, `店铺 SEO`, `带问号`, `长尾词`, `制造商入口`, `汇采购`, `首焦图`, `产品入口`, and `核心产品词` route to formal pages, root index, query entry, and extraction notes.
- Representative term search after CH10-CH19 update includes `一级引擎`, `橱窗`, `千人千面`, `买家喜好度`, `店铺权重`, `单品权重`, `P4P`, `顶展`, and `搜索排序机制` in formal pages, query entry, root index, and extraction notes.
- Obsidian route audit: run from `/Users/pechen/.codex/skills/.llmwiki-source/shared/scripts/wiki_cli_route_audit.py` after CH06-CH09 update. Active vault path was `/Users/pechen/wiki`, `trusted: true`; course index target page had 3 backlinks, 10 outgoing links, and no target warnings.
- Obsidian route audit after CH10-CH19 update: active vault path `/Users/pechen/wiki`, `trusted: true`; course index target page had 3 backlinks, 15 outgoing links, and no target warnings. Global unresolved-link output includes pre-existing unrelated vault issues.
- Index/log check: course index, `domains/电商运营/20-跨境电商/index.md`, `domains/电商运营/index.md`, root `index.md`, query entry, and `log.md` updated for CH10-CH19.
- Placeholder scan after CH10-CH19 update: `SHELL:0 THIN:0 OK:13` for formal course pages.
- Ingest contract after CH20-CH29 update: OK. Script emitted expected verbatim-match warnings for older rows when only new formal pages were passed to `--formal`; no errors.
- Placeholder scan after CH20-CH29 update: `SHELL:0 THIN:0 OK:20` for formal course pages.
- Representative term search after CH20-CH29 update includes `违规处罚`, `TRO`, `店铺定位`, `四大流量入口`, `半托管`, `RTS`, `目标国家`, `买家画像`, `出口通`, `金品店铺`, `精细化产品线`, and `直通车推广` in formal pages, query entry, root index, and extraction notes.
- Obsidian route audit after CH20-CH29 update: active vault path `/Users/pechen/wiki`, `trusted: true`; course index target page had 3 backlinks, 22 outgoing links, and no target warnings. Global unresolved-link output includes pre-existing unrelated vault issues.
- Working directory cleanup: `_meta/working/baize-alibaba-international-station-course-2026-06-25` removed after raw transcripts, videos, keyframes, and OCR were archived.
- Ingest contract after CH30-CH39 update: OK. `validate_ingest_contract.py` returned `llm-wiki-ingest contract OK`; verbatim-match warnings are expected because formal pages reconstruct rather than copy source-unit wording, including older chapters not passed as formal pages.
- Raw completeness after CH30-CH39 update: `missing_raw 0` for `.raw.txt`, `.raw.srt`, `.raw.json`, keyframes OCR.
- Strict placeholder scan after CH30-CH39 update: `STRICT_PLACEHOLDER_ISSUES 0` across 26 formal course markdown files.
- Representative term search after CH30-CH39 update includes `第二曲线`, `RTS 与定制`, `七分选品`, `剥洋葱`, `涨幅关键词`, `热词榜`, `趋势榜`, `对标同行`, `市场参谋`, `买家参谋`, `词根`, and `关键词覆盖率` in formal pages, query entry, root index, and extraction notes.
- Obsidian route audit after CH30-CH39 update: active vault path `/Users/pechen/wiki`, `trusted: true`; course index target page has 3 backlinks, 28 outgoing links, no target warnings; query entry has 14 backlinks, 25 outgoing links, no target warnings. Global unresolved-link output includes pre-existing unrelated vault issues.
- Working directory cleanup after CH30-CH39 update: `_meta/working/baize-alibaba-international-station-course-2026-06-25` removed after raw transcripts, videos, keyframes, and OCR were archived.
- Raw completeness after CH40-CH49 update: 30 transcript files for CH40-CH49 (`.raw.txt`, `.raw.srt`, `.raw.json`) present; OCR files present for all ten chapters.
- Ingest contract after CH40-CH49 update: OK. `validate_ingest_contract.py --notes-dir ... --raw ...` returned `llm-wiki-ingest contract OK`.
- Strict placeholder scan after CH40-CH49 update: `STRICT_PLACEHOLDER_ISSUES 0` across 31 formal course markdown files.
- Representative term search after CH40-CH49 update includes `关键词分类`, `精准词`, `长尾词`, `词品匹配`, `关键词收集表`, `4.9`, `产品分组`, `营销型详情页`, `旺铺首页`, `优品总量`, and `实力优品` in formal pages, query entry, root index, and course index.
- Remaining gaps: future later chapters may require denser keyframe extraction if screen content becomes slide-heavy.
- Raw completeness after CH50-CH59 update: 30 transcript files for CH50-CH59 (`.raw.txt`, `.raw.srt`, `.raw.json`) present; OCR files present for all ten chapters.
- Formal pages after CH50-CH59 update: added `31-爆品总量提升与优品权益.md`, `32-橱窗加权与产品选择.md`, `33-橱窗优化与关键词排名提升.md`, `34-店铺星等级价值与指标框架.md`, and `35-商品力与营销力提升方法.md`.
- Ingest contract after CH50-CH59 update: OK. `validate_ingest_contract.py --notes-dir ... --raw ...` returned `llm-wiki-ingest contract OK`.
- Strict placeholder scan after CH50-CH59 update: no unresolved placeholders found in the new five formal pages, query entry and extraction notes. The only normal-language match was “长期占位”.
- Representative term search after CH50-CH59 update includes `爆品总量`, `准爆品`, `优品权益`, `橱窗`, `智能橱窗`, `橱窗卖点`, `关键词排名`, `店铺星等级`, `商品力`, `营销力`, and `高消耗无商机` in formal pages, query entry, course index and extraction notes.
- Raw completeness after CH60-CH69 update: 30 transcript files for CH60-CH69 (`.raw.txt`, `.raw.srt`, `.raw.json`) present; OCR files present for all ten chapters.
- Formal pages after CH60-CH69 update: added `36-交易力与保障力星等级提升.md`, `37-产品数据分析与诊断指标.md`, `38-四象限产品优化SOP.md`, `39-爆款询盘多订单少的运营业务协同.md`, and `40-店铺流量结构与渠道增长分析.md`.
- Ingest contract after CH60-CH69 update: OK. `validate_ingest_contract.py --notes-dir ... --raw ...` returned `llm-wiki-ingest contract OK`.
- Strict placeholder scan after CH60-CH69 update: no unresolved placeholders found in the new five formal pages and query entry; matches in audit handoff were historical validation log text.
- Representative term search after CH60-CH69 update includes `交易力`, `保障力`, `发货率`, `风险健康分`, `产品数据分析`, `产品 360`, `八个诊断`, `四象限`, `高曝光低点击`, `高点击低询盘`, `询盘转化率`, `爆款订单少`, `流量结构`, `流量渠道`, `流量来源`, and `流量承接` in formal pages, query entry, course index and root index.
- Working directory cleanup after CH60-CH69 update: `_meta/working/baize-alibaba-international-station-course-2026-06-25` removed after raw transcripts, videos, keyframes, and OCR were archived.
- Video upload guard after CH60-CH69 update: raw MP4s under `raw/videos/baize-alibaba-international-station-course-2026-06-25/` are ignored by git (`!!`) and remain local raw assets.
- Raw completeness after CH70-CH79 update: 30 transcript files for CH70-CH79 (`.raw.txt`, `.raw.srt`, `.raw.json`) present; OCR files present for all ten chapters.
- Formal pages after CH70-CH79 update: added `41-市场参谋与增量市场分析.md`, `42-竞争对手店铺与产品分析.md`, `43-店铺诊断框架与综合数据SOP.md`, `44-产品数据精细化诊断SOP.md`, and `45-店铺诊断关键数据选择与判断.md`.
- Ingest contract after CH70-CH79 update: OK. `validate_ingest_contract.py --notes-dir ... --raw ...` returned `llm-wiki-ingest contract OK`.
- Placeholder scan after CH70-CH79 update: no unresolved placeholders found in the new five formal pages and query entry; matches in audit handoff were historical validation log text.
- Representative term search after CH70-CH79 update includes `市场分析`, `市场参谋`, `查行业`, `查国家`, `买家规模指数`, `供需比`, `年同比`, `类目综合分析`, `竞争对手`, `同行店铺`, `店铺诊断`, `四个问题`, `访客点击比`, `询盘转化率`, `订单转化率`, `综合数据`, `产品数据`, `产品 360`, `关键词指数`, and `词品匹配` in formal pages, query entry, course index and root index.
- Working directory cleanup after CH70-CH79 update: `_meta/working/baize-alibaba-international-station-course-2026-06-25` removed after raw transcripts, videos, keyframes and OCR were archived.
- Video upload guard after CH70-CH79 update: raw MP4s under `raw/videos/baize-alibaba-international-station-course-2026-06-25/` are ignored by git (`!!`) and remain local raw assets.
- Raw completeness after CH80-CH89 update: 30 transcript files for CH80-CH89 (`.raw.txt`, `.raw.srt`, `.raw.json`) present; OCR files present for all ten chapters.
- Formal pages after CH80-CH89 update: added `46-询盘转化率与询盘质量诊断SOP.md`, `47-店铺流量暴涨暴跌分析SOP.md`, `48-询盘量低于行业均值突破与店铺盘活.md`, `49-直通车询盘下降诊断与修复.md`, `50-营销活动与优惠券免费流量.md`, `51-首页三大场景免费流量获取规则.md`, `52-新贸节采购节大促布局.md`, and `53-新店铺三阶段运营框架.md`.
- Ingest contract after CH80-CH89 update: OK. `validate_ingest_contract.py --notes-dir ... --raw ...` returned `llm-wiki-ingest contract OK`.
- Placeholder scan after CH80-CH89 update: no unresolved placeholders found in the new eight formal pages and query entry.
- Representative term search after CH80-CH89 update includes `询盘转化率`, `询盘质量`, `业务协作`, `流量暴涨`, `流量暴跌`, `行业均值`, `老店铺盘活`, `直通车询盘下降`, `营销活动`, `优惠券`, `三大场景`, `免费流量`, `新贸节`, `采购节`, and `新店铺三阶段` in formal pages, query entry, course index or root index.
- Working directory cleanup after CH80-CH89 update: `_meta/working/baize-alibaba-international-station-course-2026-06-25` removed after raw transcripts, videos, keyframes and OCR were archived.
- Video upload guard after CH80-CH89 update: raw MP4s under `raw/videos/baize-alibaba-international-station-course-2026-06-25/` are ignored by git (`!!`) and remain local raw assets.
- Raw completeness after CH100-CH113 update: 42 transcript files for CH100-CH113 (`.raw.txt`, `.raw.srt`, `.raw.json`) present; OCR files and keyframes present for all fourteen chapters.
- Formal pages after CH100-CH113 update: added `61-标题精细化组合与批量覆盖.md`, `62-K1K2K3流量补充与词库覆盖.md`, `63-RTS与定制产品标题差异化.md`, `64-中性爆款标题与同行借力标题.md`, `65-蓝海型号国家偏好爆款标题.md`, `66-潜力产品标题优化成爆款.md`, and `67-标题方法选择避坑与爆款矩阵.md`.
- Ingest contract after CH100-CH113 update: OK. `validate_ingest_contract.py --notes-dir ... --raw ...` returned `llm-wiki-ingest contract OK`.
- Placeholder scan after CH100-CH113 update: no unresolved placeholders found in the new seven formal pages and query entry; matches in audit handoff were historical validation log text.
- Representative term search after CH100-CH113 update includes `精细化组合标题`, `K1K2K3`, `我的词库`, `RTS 与定制产品标题`, `中性爆款标题`, `同行借力标题`, `蓝海流量`, `通用型号`, `目标国家偏好`, `潜力产品标题`, `标题方法选择`, `三大坑`, and `爆款矩阵` in formal pages, query entry, course index or root index.
- Working directory cleanup after CH100-CH113 update: `_meta/working/baize-alibaba-international-station-course-2026-06-25` removed after raw transcripts, videos, keyframes and OCR were archived.
- Video upload guard after CH100-CH113 update: raw MP4s under `raw/videos/baize-alibaba-international-station-course-2026-06-25/100_*` through `113_*` are ignored by git (`!!`) and remain local raw assets.
