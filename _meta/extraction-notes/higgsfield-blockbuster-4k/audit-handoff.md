---
title: Higgsfield Blockbuster 4K AI电影工作流课程审计交接
type: source-summary
created: 2026-08-12
updated: 2026-08-12
domain: meta
tags: [llm-wiki, audit-handoff, visual-production, ai-video]
sources:
  - raw/webpages/higgsfield/higgsfield-blockbuster-4k-case4k-2026-08-12.md
  - raw/webpages/higgsfield/blockbuster-4k-academy/higgsfield-blockbuster-4k-lessons-02-10-2026-08-12.md
  - raw/videos/higgsfield-blockbuster-4k/01-one-character-many-worlds-watch-the-film.mp4
  - raw/transcripts/higgsfield-blockbuster-4k/ch01-one-character-many-worlds.raw.txt
status: active
---

# Higgsfield Blockbuster 4K AI电影工作流课程审计交接

## Source

- Adapter: web clipping + image knowledge + downloadable-asset inspection, with transcript/video-course as a secondary branch
- Raw paths: `raw/webpages/higgsfield/`, `raw/assets/higgsfield-blockbuster-4k/`, `raw/videos/higgsfield-blockbuster-4k/`
- Primary URL: `https://higgsfield.ai/blog/case4k`
- Secondary URL: `https://higgsfield.ai/academy/courses/blockbuster-4k/`（第 1–10 课）
- Capture date: 2026-08-12
- Current-doc verification: official companion blog located at `https://higgsfield.ai/blog/case4k`; model/UI details remain time-sensitive

## Outputs

- Source profile: `_meta/extraction-notes/higgsfield-blockbuster-4k/source-profile.md`
- Source inventory: `_meta/extraction-notes/higgsfield-blockbuster-4k/source-inventory.md`
- Blog source inventory: `_meta/extraction-notes/higgsfield-blockbuster-4k/blog-source-inventory.md`
- Blog prompt structure analysis: `_meta/extraction-notes/higgsfield-blockbuster-4k/blog-prompt-structure-analysis.md`
- Academy source inventory: `_meta/extraction-notes/higgsfield-blockbuster-4k/academy-source-inventory.md`
- Academy coverage matrix: `_meta/extraction-notes/higgsfield-blockbuster-4k/academy-coverage-matrix.md`
- Scene asset inventory: `_meta/extraction-notes/higgsfield-blockbuster-4k/scene-asset-inventory.md`
- Image inventory: `_meta/extraction-notes/higgsfield-blockbuster-4k/image-inventory.md`
- Image analysis: `_meta/extraction-notes/higgsfield-blockbuster-4k/image-analysis.md`
- Semantic validation: `_meta/extraction-notes/higgsfield-blockbuster-4k/semantic-validation.md` (`passed`)
- Knowledge-unit inventory: `_meta/extraction-notes/higgsfield-blockbuster-4k/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/higgsfield-blockbuster-4k/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/higgsfield-blockbuster-4k/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/higgsfield-blockbuster-4k/formal-page-plan.md`
- Formal pages: 8 页已按生产阶段分布到 `00-生产总览/`、`01-项目定义与剧本/`、`04-图片与控制资产/`、`05-视频生成/` 和 `06-视频剪辑与连续性/`。

## Placement Confirmation

- Source understanding: updated Higgsfield AI-filmmaking course using a multi-world action short to teach script, assets, prompt-building and scene generation.
- Existing category considered: `domains/视觉制作/06-AI视频/`
- Recommended placement at confirmation time: the then-current AI-video root workflow cluster; current placement follows the five production-stage directories listed above.
- Recommended disposition: create ordered end-to-end system; cross-link/extend existing asset, prompt and continuity pages.
- Alternatives considered: merge-only into existing pages; source-course-notes-only.
- User confirmation: confirmed
- Confirmation evidence: user approved the proposed directory and asked for remaining lesson text to supplement it.
- Final confirmed disposition: preserve the complete workflow as 8 formal pages; current exact paths are recorded in `_meta/extraction-notes/ai-video-physical-reorganization-2026-08-12/migration-map.md`.

## Coverage Summary

- Source units: 54 (13 showcase-video units + 32 official-Blog units + 9 Academy written-lesson units)
- formalized or merged: 52
- raw-only: 2 source units plus explicitly marked provenance/decorative images
- omitted-with-reason: 0
- unresolved: 0 knowledge units; current model/UI details remain versioned claims
- Image coverage: 74 archived locally (`33 video frames + 7 article images + 34 scene-pack images`) / 68 formalized or merged / 6 raw-only; 48 additional Academy figure URLs/captions indexed but not downloaded due TLS failure

## Expected Agent Use

- Future questions this source should support: how to structure an AI film pipeline; how to build assets; how to generate shot prompts with a Skill; how to preserve continuity across worlds; how to iterate without random credit burn.
- Pages an Agent should read first: workflow index, asset system, Prompt-Builder protocol and QA/cost page.
- Query/playbook entries: `queries/AI视频导演与分镜入口.md` updated.

## Known Risks

- Time-sensitive claims: Higgsfield course UI, Seedance version, Claude Skill installation UI and downloadable files.
- Sensitive data removed: none encountered.
- Sensitive image handling: no sensitive images detected.
- Weak source areas: film dialogue after 01:26 is not reliable in ASR; visual structure is reliable.
- User confirmation needed: none for the completed knowledge-base phase.

## Self-Validation

- No formal write before placement confirmation: yes
- Placeholder scan: passed; the only matched phrase was an intentional workflow state (`待补资产`), not a page placeholder
- Representative term search: completed during orientation
- Index/log check: AI-video index, query entry and root log updated
- Remaining gaps: optional retry of 48 Academy images and lesson 2 PDF; neither is required by the compiled operating method
- Ingest contract validation: passed; `llm-wiki-ingest contract OK`
- Local wikilink validation for the new module: 0 missing targets
