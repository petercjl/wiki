---
title: 抖音视频《真正的 Prompt 强控，不是写得更长，而是分层级》审计交接
type: source-summary
created: 2026-07-23
updated: 2026-07-23
domain: meta
tags: [llm-wiki, audit-handoff, ai-video, prompt-engineering]
sources:
  - raw/videos/douyin-prompt-layered-control-2026-07-23/original.mp4
  - raw/transcripts/douyin-prompt-layered-control-2026-07-23/transcript.raw.srt
status: active
---

# 抖音视频《真正的 Prompt 强控，不是写得更长，而是分层级》审计交接

## Source

- Adapter: transcript + local video branch
- Raw path: `raw/videos/douyin-prompt-layered-control-2026-07-23/`
- Original URL/path: https://www.douyin.com/video/7660700852612631823
- Capture date: 2026-07-23
- Current-doc verification: 不需要实时产品参数；CFG/架构只按“常见或类似机制”解释

## Outputs

- Source profile: `source-profile.md`
- Source inventory: `source-inventory.md`
- Semantic validation: `semantic-validation.md`（passed）
- Normalized transcript: `normalized-transcript.md`
- Knowledge-unit inventory: `knowledge-unit-inventory.md`
- Coverage matrix: `coverage-matrix.md`
- Omission audit: `omission-audit.md`
- Formal page plan: `formal-page-plan.md`
- Formal pages:
  - `domains/视觉制作/06-AI视频/12-AI视频Prompt分层强控方法.md`
  - `domains/视觉制作/06-AI视频/05-AI视频导演Prompt模板.md`（相关记忆）
  - `queries/AI视频导演与分镜入口.md`（路由扩展）

## Placement Confirmation

- Source understanding: AI 视频 Prompt 的约束竞争原理、三层强控写法和复杂镜头降压工作流
- Existing category considered: `domains/视觉制作/06-AI视频/`
- Recommended placement: `domains/视觉制作/06-AI视频/12-AI视频Prompt分层强控方法.md`
- Recommended disposition: create-new + link from existing Prompt template + extend existing query
- Alternatives considered: merge into `05-AI视频导演Prompt模板.md`
- User confirmation: confirmed
- Confirmation evidence: 用户在 2026-07-23 回复“确定”
- Final confirmed path: `domains/视觉制作/06-AI视频/12-AI视频Prompt分层强控方法.md`

## Coverage Summary

- Source units: 19
- formalized: 17
- merged: 0
- raw-only: 2
- omitted-with-reason: 0
- unresolved: 0

## Expected Agent Use

- Future questions this source should support:
  - 为什么 Prompt 越长越不听话？
  - 如何给 AI 视频 Prompt 排优先级？
  - 多个镜头、角色、动作、光线和风格冲突时怎么拆？
  - 什么时候应改用参考图、首尾帧、遮罩或后期，而不是继续加词？
- Pages an Agent should read first: `12-AI视频Prompt分层强控方法.md`，再读 `05-AI视频导演Prompt模板.md`
- Query/playbook entries: extend `queries/AI视频导演与分镜入口.md`

## Known Risks

- Time-sensitive claims: 不绑定模型版本；闭源模型实现不可由本视频反推
- Sensitive data removed: none
- Weak source areas: 注意力预算百分比图只为示意，无实验依据
- User confirmation needed: no

## Self-Validation

- No formal write before placement confirmation: yes
- Ingest contract: passed (`llm-wiki-ingest contract OK`)
- Placeholder scan: passed by ingest validator
- Representative term search: completed before proposal
- Index/log check: completed
- Route audit: passed; active Obsidian vault equals `/Users/pechen/wiki`, all three target pages have no warnings
- Route evidence: new formal page has 4 backlinks and 5 outgoing related-memory links
- Remaining gaps: none
