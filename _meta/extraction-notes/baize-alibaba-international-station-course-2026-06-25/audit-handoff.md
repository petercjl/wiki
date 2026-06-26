---
title: 白泽国际站运营实战系统课 audit handoff
type: source-summary
created: 2026-06-25
updated: 2026-06-25
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
- `queries/阿里巴巴国际站运营诊断.md`

## Coverage Summary

- Source units in main coverage matrix: 191.
- formalized: 189.
- merged: 0 in the main coverage matrix; repeated CH05 slide promise is classified as `merged` in `ch05/omission-audit.md`.
- raw-only: 2 in the main coverage matrix, plus CH05 classroom transition and garbled OCR subtitle fragments in chapter omission audit.
- omitted-with-reason: 0 in the main coverage matrix; CH08 APP-specific detail is marked omitted-with-reason in `ch08/omission-audit.md` because the course explicitly does not cover APP in this chapter.
- unresolved: 2 known ASR terms from earlier chapters (`奥义加`, `报品/报增`) remain in omission audit for optional quote-level verification.

## Current Status

- Raw videos copied for CH01-CH49.
- CH01-CH49 audio extracted.
- CH01-CH49 keyframes extracted; CH06-CH49 OCR captured at 15-second intervals where available.
- `whisper-cpp` installed via Homebrew.
- `ggml-large-v3-turbo.bin` downloaded to `/Users/pechen/.local/share/whisper.cpp/models/`.
- CH01-CH49 raw Whisper transcripts archived under `raw/transcripts/baize-alibaba-international-station-course-2026-06-25/`.
- Transcript-derived knowledge units formalized; CH10-CH12 add platform rules and search sorting, CH13 adds comprehensive strength indicators, CH14-CH15 add buyer preference and personalization, CH16-CH17 add first-level engine/showcase weighting, CH18-CH19 add store/product weight improvement, CH20-CH29 add compliance risk, store positioning, traffic track selection, product-line layout, target country, buyer persona, trust conversion, store type, and through-train focus, CH30-CH39 add second-curve store planning, RTS/custom differentiation, product selection, rising-keyword selection, peer-store selection, Market Advisor case workflow, and keyword-root coverage, and CH40-CH49 add keyword classification, keyword selection standards, true keyword-product matching, keyword collection tables, high-quality product publishing, product grouping, marketing detail/storefront pages, premium-product models, and strength-product improvement.

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
