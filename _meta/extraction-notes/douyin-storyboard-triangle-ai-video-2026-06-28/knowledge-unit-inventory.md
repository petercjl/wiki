---
title: 故事板铁三角 AI 视频控制法 knowledge-unit inventory
type: source-summary
created: 2026-06-28
updated: 2026-06-28
domain: meta
tags: [llm-wiki, knowledge-unit-inventory, visual-production, ai-video]
sources:
  - raw/transcripts/douyin-storyboard-triangle-ai-video-2026-06-28/storyboard-whisper.raw.txt
  - raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/source-summary.json
status: active
---

# Knowledge Unit Inventory

| unit_id | source_anchor | knowledge_role | reusable knowledge |
| --- | --- | --- | --- |
| KU-001 | CH-001 / ASR 00:00-00:20 | problem framing | Cheap-looking AI video is framed as a control problem, not merely a prompt-writing problem. |
| KU-002 | CH-001 / ASR 00:20-00:24 | framework setup | Correct storyboard should carry only three kinds of information. |
| KU-003 | CH-002 / ASR 00:23-00:44 | storyboard design rule | Storyboard should be minimalist hand-drawn layout, not real-person/detail-heavy images, because detail-heavy grids make the model treat each panel as a new reference. |
| KU-004 | CH-002 / ASR 00:37-00:44 | responsibility split | Storyboard only tells shot scale and character position; character appearance belongs to the identity board. |
| KU-005 | CH-002 / ASR 00:50-00:58 | workflow step | Identity board plus prepared plot can generate a multi-panel storyboard whose role is planning, not final video generation. |
| KU-006 | CH-003 / ASR 01:01-01:18 | motion annotation | Storyboard should mark both character displacement and camera trajectory; red can mark character movement and blue can mark camera movement. |
| KU-007 | CH-004 / ASR 01:19-01:29 | prompt role | Prompt should be auxiliary and concise, used to fill gaps and describe the core visual content of each shot. |
| KU-008 | CH-005 / ASR 01:29-01:40 | style control | Before video generation, create a preview/effect image to unify the visual style of the whole video. |
| KU-009 | CH-006 / ASR 01:41-01:58 | core framework | The iron triangle is storyboard for shots, identity board for character details, and style/effect image for visual tone. |
| KU-010 | CH-007 / ASR 01:59-02:23 | generation workflow | After preparing identity board, story board, plot, and effect image, upload assets and use a concise prompt to generate dialogue/plot and then video. |
| KU-011 | CH-008 / ASR 02:24-02:34 | failure mode | Overfilled storyboard makes the model lose focus. |
| KU-012 | CH-008 / ASR 02:34-02:42 | failure mode | Storyboard and prompt must not conflict; visual and text instruction should stay synchronized. |
| KU-013 | CH-008 / ASR 02:42-02:53 | boundary | Storyboard cannot solve all problems; identity belongs to identity board, scene/style belongs to effect image. |
| KU-014 | CH-008 / ASR 02:54-03:01 | prompt simplification | Once assets are clear, final video prompt can be very simple: one sentence for the core visual intent. |
| KU-015 | CH-009 / ASR 03:01-03:16 | process logic | Storyboard moves quality control before generation, so failures can be found at planning time rather than after rendering. |
| KU-016 | VIS-001-VIS-006 | visual evidence | The video demonstrates the method with costume/character boards, hand-drawn storyboard grids, movement arrows, prompt panels, and final generated shots. |
| KU-017 | SRC-001 | source retrieval | Author, aweme ID, publish time, metrics, tags, source URL, and capture date should be preserved as retrieval metadata. |

## ASR Notes

- ASR used `whisper-cli` with `ggml-large-v3-turbo.bin`.
- "故事版" in ASR/source is normalized to "故事板" in formal pages when referring to storyboard.
- "身份版" is preserved as the source's wording and interpreted as a character identity/reference board.
- "预想效果图" and "风格效果图" are normalized as style/effect reference image.
