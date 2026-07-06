---
title: 微信视频号岩井俊二风格青春片解析 source inventory
type: source-summary
created: 2026-07-05
updated: 2026-07-05
domain: meta
tags: [llm-wiki, source-inventory, ai-video]
sources:
  - raw/videos/wechat-channels-aofyh73igj-h264-2026-07-05/wechat_channels_AOFyh73IgJ_h264.mp4
status: active
---

# Source Inventory

| source_item | path | notes |
| --- | --- | --- |
| raw video | `raw/videos/wechat-channels-aofyh73igj-h264-2026-07-05/wechat_channels_AOFyh73IgJ_h264.mp4` | Original local MP4 preserved unchanged. |
| raw ASR txt | `raw/transcripts/wechat-channels-aofyh73igj-h264-2026-07-05/ch01.raw.txt` | Whisper raw Chinese transcript. Contains ASR errors such as `严谨君二` for `岩井俊二`. |
| raw ASR srt | `raw/transcripts/wechat-channels-aofyh73igj-h264-2026-07-05/ch01.raw.srt` | Timestamped transcript. |
| raw ASR json | `raw/transcripts/wechat-channels-aofyh73igj-h264-2026-07-05/ch01.raw.json` | Whisper JSON output. |
| keyframes | `raw/assets/wechat-channels-aofyh73igj-h264-2026-07-05/ch01/keyframes/` | 20 frames sampled at 1 frame per 8 seconds. |
| OCR text | `raw/assets/wechat-channels-aofyh73igj-h264-2026-07-05/ch01/keyframe-ocr.raw.txt` | Tesseract OCR. Noisy but confirms `岩井俊二风格解析` and `Interpretation of Shunji Iwai's Aesthetic Style`. |
| contact sheet | `raw/assets/wechat-channels-aofyh73igj-h264-2026-07-05/ch01/contact-sheet.jpg` | Visual overview of generated青春片 frames and prompt overlays. |
| prompt frames | `raw/assets/wechat-channels-aofyh73igj-h264-2026-07-05/ch01/prompt-frames/` | 79 frames sampled at 1 frame per 2 seconds to capture prompt overlays more completely. |
| Vision OCR text | `raw/assets/wechat-channels-aofyh73igj-h264-2026-07-05/ch01/vision-ocr.raw.txt` | macOS Vision OCR output. Stronger evidence for prompt extraction than Tesseract; still contains OCR noise and is treated as raw evidence. |

## Semantic Source Sections

| section_id | time_range | description | evidence |
| --- | --- | --- | --- |
| S01 | 00:00-00:15 | Opens with a recreated summer/youth film and frames the theme as unspoken farewell and first-love regret. | ASR, contact sheet |
| S02 | 00:15-00:43 | Names the analyzed aesthetic as Shunji Iwai style and lists core visual signs: natural light, soft color, empty space, sky, field, grain, Tyndall-like light, memory, letters, narration, non-linear narrative, restrained emotion. | ASR, OCR |
| S03 | 00:43-00:57 | States the reconstruction lens: composition, light, and color grading as the three bottom logics. | ASR |
| S04 | 00:57-01:07 | Composition logic: simple background, sky/mountain/negative space above the character, less as respect for emotion. | ASR, frames |
| S05 | 01:07-01:20 | Light logic: backlight from behind the subject, flare/halo/natural overflow, countering flat front-light logic. | ASR, frames |
| S06 | 01:20-01:36 | Color logic: beige/yellow, blue, pale green, white, low-saturation faded film, cyan suppression, avoiding plastic high saturation. | ASR, frames |
| S07 | 01:36-01:54 | Motion and scene logic: slow motion, long takes, handheld micro-shake, alleys, campus, rain, narration and temporal interweaving. | ASR, frames |
| S08 | 01:54-02:20 | Emotional rule: restraint, unspoken love, unresolved regret, single glance/light spot as emotional carrier. | ASR |
| S09 | 02:20-02:38 | End watermark/noise. | ASR |
| V01 | whole video | Visual overlays provide prompt-like scene breakdowns with shot duration, focal length, composition, lighting, action, and texture cues. | OCR, keyframes |
| V02 | whole video | Dense prompt overlays include multiple reusable prompt groups: rain eaves, classroom secret love, library same-book scene, rice-field boy, classroom curtains, night cycling, tree-hole letter, and rural-road running. | Vision OCR, prompt frames |
