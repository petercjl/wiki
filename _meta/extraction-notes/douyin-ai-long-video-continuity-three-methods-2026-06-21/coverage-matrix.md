# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| S-001 | `source.raw.txt` 00:00-00:37 | AI 长视频翻车不是模型不强，而是 15 秒段落硬接导致色彩突变、卡顿、动作断掉。 | problem-frame | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | formalized | Reframed as the core problem statement. |
| S-002 | `source.raw.txt` 00:37-02:14 | 学会切换景别和角度；尾帧生成多机位候选，下一段选择不同景别或角度。 | method | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | formalized | “颈别” corrected to “景别”. |
| S-003 | `source.raw.txt` 01:07-01:24; keyframes 004-007 | 以 LibTV 为例：截尾帧、图片、九宫格、多机位九宫格、生成候选首帧。 | tool-workflow | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | merged | Tool UI kept as example, abstracted to reusable method. |
| S-004 | `source.raw.txt` 02:14-03:20; keyframes 011-013 | 在动作中衔接：截取动作起势，下一段写“继续抬起”等重叠动作。 | method | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | formalized | Prompt wording converted into template. |
| S-005 | `source.raw.txt` 03:20-03:37; keyframe 014 | 动作中切利用视觉暂留和运动轨迹连续感，让大脑自动接上前后帧。 | rationale | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | formalized | Numerical visual-persistence claim kept as source-derived rationale, not a scientific deep dive. |
| S-006 | `source.raw.txt` 03:38-05:01; keyframes 016-019 | 不要硬续长镜头；用分镜把剧情拆成 15 秒内的小剧情，再组接。 | method | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | formalized | “阻接” corrected to “组接”. |
| S-007 | `source.raw.txt` 04:00-04:24; keyframes 016-017 | 女生在列车发车前送文件：用脚本生成分镜，前四镜 4+3+3+4 秒合计 14 秒。 | example | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | formalized | Example converted into segment table. |
| S-008 | `source.raw.txt` 05:01-05:27 | 真实限制不是 15 秒，而是硬续长镜头；学会景别角度切换、动作中衔接、分镜拆剧情。 | conclusion | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | formalized | Conclusion integrated into core judgment and checklist. |
| S-009 | `keyframes-ocr.raw.txt` | Keyframes show LibTV-like UI, multi-camera grid, storyboard/script table, subtitles and examples. | visual-evidence | `domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法.md` | merged | OCR was noisy; used only to corroborate visual workflow. |
| S-010 | `page-text.txt`, `dycli-detail.json` | Author, publish time, hashtags, comments and related recommendations from page text. | metadata | `raw/videos/douyin-ai-long-video-continuity-three-methods-2026-06-21/`; `_meta/extraction-notes/douyin-ai-long-video-continuity-three-methods-2026-06-21/source-profile.md` | raw-only | Metadata preserved for traceability, not formal method. |
