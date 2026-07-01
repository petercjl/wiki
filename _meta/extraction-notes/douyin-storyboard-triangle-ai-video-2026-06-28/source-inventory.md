---
title: 故事板铁三角 AI 视频控制法 source inventory
type: source-summary
created: 2026-06-28
updated: 2026-06-28
domain: meta
tags: [llm-wiki, source-inventory, visual-production, ai-video]
sources:
  - raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/source-summary.json
status: active
---

# Source Inventory

| source_part_id | source_location | content_type | description | extraction_status |
| --- | --- | --- | --- | --- |
| SRC-001 | `dycli-detail.json` | metadata | Title/caption, author, co-creator, publish time, duration, interaction metrics, tags, URLs. | extracted |
| SRC-002 | `source-summary.json` | structured chapters | Chapter abstract and 9 chapter entries with timestamps and details. | extracted |
| SRC-003 | `storyboard-whisper.raw.txt/.srt/.json` | ASR transcript | Spoken explanation of why storyboards reduce random generation, how to build storyboard/identity/effect image assets, and common mistakes. | extracted |
| SRC-004 | `source.mp4` | raw video | Complete video source with visuals, voiceover, examples, and on-screen prompts. | archived |
| SRC-005 | `keyframes/` and `contact-sheet.jpg` | visual evidence | Storyboard examples, identity board examples, "短剧制作铁三角" slide, prompt screen, generated final video frames. | archived |
| SRC-006 | `page-text.txt` | visible page text | Douyin page title, chapter abstract, chapter cards, description, interaction counts, comments visible on page. | extracted |
| SRC-007 | `ocr/all-keyframes-ocr.txt` | OCR attempt | Tesseract OCR produced no usable text; raw keyframes remain the visual evidence. | raw-only |

## Structured Chapter Inventory

| chapter_id | timestamp | title | source detail |
| --- | ---: | --- | --- |
| CH-001 | 00:00 | 引言 | Why prompt-only AI video feels cheap; storyboard is positioned as a control method. |
| CH-002 | 00:23 | 分镜 | Use minimalist hand-drawn storyboard, not detailed real-person images; use storyboard for shot and position, not identity. |
| CH-003 | 01:00 | 运动 | Mark character movement and camera path with different colors. |
| CH-004 | 01:19 | 提示词 | Prompt is auxiliary; describe only core visual content per shot. |
| CH-005 | 01:29 | 预想效果图 | Generate a preview/effect image to unify visual style before video generation. |
| CH-006 | 01:39 | 铁三角 | Storyboard fixes shots, identity board fixes character details, style/effect image fixes visual tone. |
| CH-007 | 01:59 | 生成视频 | Upload identity board, storyboard, style reference/effect image, and concise prompt to generate dialogue/plot and video. |
| CH-008 | 02:24 | 新手常见问题 | Avoid overfilled storyboard, conflict between storyboard and prompt, and expecting storyboard to solve identity/style. |
| CH-009 | 03:00 | 结语 | Storyboard changes AI video from after-the-fact luck to pre-generation global control. |

## Visual Evidence Inventory

| visual_part_id | file | meaning |
| --- | --- | --- |
| VIS-001 | `contact-sheet.jpg` | Shows source video includes final generated scene, hand-drawn storyboard, character/identity sheets, prompt panels, "短剧制作铁三角" slide, and final generated shots. |
| VIS-002 | `keyframes/frame_003.jpg` and neighbors | Shows a hand-drawn storyboard grid used as planning reference. |
| VIS-003 | `keyframes/frame_004.jpg` and neighbors | Shows final generated storyboard-like result and warning that AI treats every grid as a new reference if the storyboard is too detailed. |
| VIS-004 | `keyframes/frame_005.jpg` and neighbors | Shows character identity board / costume reference used to stabilize character details. |
| VIS-005 | `keyframes/frame_011.jpg` and neighbors | Shows "短剧制作铁三角": story board, identity board, final/effect result image. |
| VIS-006 | `keyframes/frame_018.jpg` | Shows video-generation prompt screen; the prompt appears as an execution input after assets are prepared. |
