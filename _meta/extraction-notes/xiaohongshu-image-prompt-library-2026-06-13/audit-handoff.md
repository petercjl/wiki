---
title: 小红书生图提示词库 audit handoff
type: source-summary
created: 2026-06-13
updated: 2026-06-13
domain: meta
tags: [llm-wiki, audit-handoff, xiaohongshu]
sources:
  - raw/articles/xiaohongshu-image-prompt-library-2026-06-13.md
status: active
---

# 小红书生图提示词库 Audit Handoff

## Source

- Adapter: markdown-doc
- Raw path: `raw/articles/xiaohongshu-image-prompt-library-2026-06-13.md`
- Original URL/path: `/Users/pechen/Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files/wxid_jyxo3zp0419o12_413d/msg/file/2026-06/小红书生图提示词库.md`
- Capture date: 2026-06-13
- Current-doc verification: not applicable; local prompt library/method document, not an official platform policy.

## Outputs

- Source profile: `_meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/source-profile.md`
- Source inventory: `_meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/source-inventory.md`
- Knowledge-unit inventory: `_meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/formal-page-plan.md`
- Formal pages:
  - `domains/visual-production/xiaohongshu-image-generation/index.md`
  - `domains/visual-production/xiaohongshu-image-generation/xiaohongshu-image-generation-principles.md`
  - `domains/visual-production/xiaohongshu-image-generation/feed-vs-search-image-strategy.md`
  - `domains/visual-production/xiaohongshu-image-generation/cover-image-types.md`
  - `domains/visual-production/xiaohongshu-image-generation/image-set-structure.md`
  - `domains/visual-production/xiaohongshu-image-generation/selling-point-translation.md`
  - `domains/visual-production/xiaohongshu-image-generation/prompt-formula-and-variable-library.md`
  - `domains/visual-production/xiaohongshu-image-generation/prompt-templates.md`
  - `domains/visual-production/xiaohongshu-image-generation/qa-checklist.md`
  - `domains/visual-production/xiaohongshu-image-generation/agent-usage-template.md`
  - `queries/xiaohongshu-image-generation.md`

## Coverage Summary

- Source units: 20
- formalized: 20
- merged: 0
- raw-only: 0
- omitted-with-reason: 0
- unresolved: 0

## Expected Agent Use

- Future questions this source should support:
  - Generate Xiaohongshu-style cover prompts.
  - Generate Xiaohongshu 6-image post structures.
  - Translate product selling points into Xiaohongshu visual language.
  - Decide feed vs search image strategy.
  - Audit Xiaohongshu generated images.
- Pages an Agent should read first:
  - `queries/xiaohongshu-image-generation.md`
  - `domains/visual-production/xiaohongshu-image-generation/index.md`
  - `domains/visual-production/xiaohongshu-image-generation/agent-usage-template.md`
- Query/playbook entries:
  - `queries/xiaohongshu-image-generation.md`

## Known Risks

- Time-sensitive claims: Xiaohongshu content style may change; review if platform aesthetics or search behavior shift.
- Sensitive data removed: none found.
- Weak source areas: source provides templates, not platform data validation or performance benchmarks.
- User confirmation needed: none for first version; future expansion can add category-specific prompt variants.

## Self-Validation

- Placeholder scan: passed for `domains/visual-production/xiaohongshu-image-generation/` and `queries/` (no mechanical shells detected).
- Ingest contract: passed; validator produced non-blocking warnings because source unit IDs are not intended to appear verbatim in formal pages.
- Representative term search: passed for 信息流、搜索承接、痛点型封面、关键词封面、评论区转化.
- Obsidian route audit: target query page has backlinks from root index, visual-production index, directory index, and Agent usage template; outgoing links resolve in active `/Users/pechen/wiki` vault, with global pre-existing unresolved warnings outside this ingest.
- Index/log check: root index, visual-production index, and log updated.
- Remaining gaps: no source coverage gaps known; future enrichment can add product-category examples and performance-tested 小红书 case data.
