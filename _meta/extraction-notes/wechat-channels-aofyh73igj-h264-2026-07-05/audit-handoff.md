---
title: 微信视频号岩井俊二风格青春片解析 audit handoff
type: source-summary
created: 2026-07-05
updated: 2026-07-05
domain: meta
tags: [llm-wiki, audit-handoff]
sources:
  - raw/videos/wechat-channels-aofyh73igj-h264-2026-07-05/wechat_channels_AOFyh73IgJ_h264.mp4
status: active
---

# 微信视频号岩井俊二风格青春片解析 Audit Handoff

## Source

- Adapter: `llm-wiki-ingest/adapters/transcript.md` with video-course branch
- Raw path: `raw/videos/wechat-channels-aofyh73igj-h264-2026-07-05/`
- Original URL/path: `/Users/pechen/Downloads/wechat_channels_AOFyh73IgJ_h264.mp4`
- Capture date: 2026-07-05
- Current-doc verification: not required; source is aesthetic/style analysis, not a current platform or API rule.

## Outputs

- Source profile: `_meta/extraction-notes/wechat-channels-aofyh73igj-h264-2026-07-05/source-profile.md`
- Source inventory: `_meta/extraction-notes/wechat-channels-aofyh73igj-h264-2026-07-05/source-inventory.md`
- Knowledge-unit inventory: `_meta/extraction-notes/wechat-channels-aofyh73igj-h264-2026-07-05/knowledge-unit-inventory.md`
- Coverage matrix: `_meta/extraction-notes/wechat-channels-aofyh73igj-h264-2026-07-05/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/wechat-channels-aofyh73igj-h264-2026-07-05/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/wechat-channels-aofyh73igj-h264-2026-07-05/formal-page-plan.md`
- Formal pages:
  - `domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/index.md`
  - `domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/01-岩井俊二风格AI短视频制作方法.md`
- Prompt evidence:
  - `raw/assets/wechat-channels-aofyh73igj-h264-2026-07-05/ch01/prompt-frames/`
  - `raw/assets/wechat-channels-aofyh73igj-h264-2026-07-05/ch01/vision-ocr.raw.txt`

## Coverage Summary

- Source units: 11
- formalized: 10
- merged: 0
- raw-only: 1
- omitted-with-reason: 0 source units; long exact narration omitted as copyright-safe reconstruction and recorded in omission audit
- unresolved: 0

## Expected Agent Use

- Future questions this source should support:
  - 如何写日系青春片风格的 AI 视频 prompt？
  - 为什么“岩井俊二风格”比一长串风格词更有效？
  - 如何把暗恋、毕业、夏天、未说出口做成克制短片？
  - 如何复刻视频中出现的提示词结构？
  - 如何把风格分析变成秒级分镜和镜头表？
- Pages an Agent should read first:
  - `queries/AI视频导演与分镜入口.md`
  - `domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/index.md`
  - `domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/01-岩井俊二风格AI短视频制作方法.md`
  - `domains/视觉制作/06-AI视频/05-AI视频导演Prompt模板.md`
  - `domains/视觉制作/06-AI视频/04-商业短视频摄影与运镜语法.md`
- Query/playbook entries:
  - Updated route: `queries/AI视频导演与分镜入口.md`
  - New query entry: not needed; existing route updated for style-recreation/tutorial tasks.

## Known Risks

- Time-sensitive claims: none.
- Sensitive data removed: none.
- Weak source areas: OCR is noisy; formal claims only use visually confirmed structure and ASR-supported concepts.
- User confirmation needed: none.

## Self-Validation

- Ingest contract: `llm-wiki-ingest contract OK`. Verbatim-match warnings are expected because the formal page reconstructs noisy ASR/OCR into usable prompt drafts and workflow language instead of copying raw OCR/ASR sentences.
- Placeholder scan: `SHELL: 0`, `THIN: 0`, `OK: 2` for `domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/`.
- Route audit: `queries/AI视频导演与分镜入口.md` and `domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/index.md` target reports have no warnings; active Obsidian vault is `/Users/pechen/wiki`.
- Representative term search: old misclassified case-library route is cleared. New route contains `影像美学大师风格AI短视频`, `岩井俊二风格AI短视频制作方法`, `AI 短视频教程`, `风格复刻`, `秒级镜头`, `低饱和`, and `微信视频号`.
- Index/log check: updated AI video index, root index, query entry, log, and removed the misclassified case-library route.
- Remaining gaps: none expected; user clarified source intent as an AI short-video tutorial and notes/formal plan were updated accordingly.
