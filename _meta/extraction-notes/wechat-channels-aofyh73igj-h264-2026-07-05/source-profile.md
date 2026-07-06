---
title: 微信视频号岩井俊二风格青春片解析 source profile
type: source-summary
created: 2026-07-05
updated: 2026-07-05
domain: meta
tags: [llm-wiki, source-profile, ai-video]
sources:
  - raw/videos/wechat-channels-aofyh73igj-h264-2026-07-05/wechat_channels_AOFyh73IgJ_h264.mp4
status: active
---

# Source Profile

## Source

- Source title: 微信视频号短视频：岩井俊二风格 AI 短视频制作教程
- Source slug: `wechat-channels-aofyh73igj-h264-2026-07-05`
- Original path: `/Users/pechen/Downloads/wechat_channels_AOFyh73IgJ_h264.mp4`
- Source type: local MP4 short video
- Adapter: `llm-wiki-ingest/adapters/transcript.md` with `video-course-ingest.md`
- Capture/ingest date: 2026-07-05
- Language: Chinese narration with mixed Chinese/English visual prompt text
- Duration: 158.54 seconds
- Resolution: 720x1280, vertical
- Primary evidence: spoken narration, subtitles, prompt text overlays, visual examples

## Tools

- Media inspection: `ffprobe`
- Audio extraction: `ffmpeg`, 16 kHz mono WAV
- ASR: `whisper-cli`, model `/Users/pechen/.local/share/whisper.cpp/models/ggml-large-v3-turbo.bin`
- Keyframes: `ffmpeg`, 1 frame per 8 seconds
- OCR: `tesseract`, `chi_sim+eng`, `--psm 6`
- Prompt-frame extraction: `ffmpeg`, 1 frame per 2 seconds, 79 frames
- Prompt OCR: macOS Vision `VNRecognizeTextRequest`, `zh-Hans` + `en-US`

## Domain Placement

- Primary domain: `domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/`
- Primary formal artifact: film-aesthetic master style AI short-video topic and playbook
- Related pages:
  - `domains/视觉制作/06-AI视频/02-AI商业短视频规划方法.md`
  - `domains/视觉制作/06-AI视频/03-导演式镜头设计方法.md`
  - `domains/视觉制作/06-AI视频/04-商业短视频摄影与运镜语法.md`
  - `domains/视觉制作/06-AI视频/05-AI视频导演Prompt模板.md`
  - `domains/视觉制作/06-AI视频/07-故事板铁三角AI视频控制法.md`
  - `domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/index.md`

## Fusion Disposition

- Disposition: `create-new`
- Reason: existing AI video pages cover commercial video planning, prompt templates, continuity, audio, and several product/cultural cases, but none specifically captures this tutorial pattern: choose a recognizable film aesthetic, extract visual/narrative vocabulary, decompose it into composition/light/color, then turn it into second-level AI short-video storyboard prompts.
- Query entry: `update-existing`. Existing `queries/AI视频导演与分镜入口.md` already routes AI video script, storyboard, prompt, and case-reference tasks; this ingest adds an explicit branch for style-recreation tutorials and second-level shot prompts.

## Sensitivity And Currentness

- No private credentials or user data found.
- The film-maker/style reference is not a platform rule and is not time-sensitive.
- Style imitation should be used as an aesthetic analysis route, not as a claim of authorization or as exact copying of any living creator's protected expression.
