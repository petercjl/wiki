---
title: 故事板铁三角 AI 视频控制法 source profile
type: source-summary
created: 2026-06-28
updated: 2026-06-28
domain: meta
tags: [llm-wiki, source-profile, visual-production, ai-video]
sources:
  - raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/source.mp4
status: active
---

# Source Profile

## Source

- Source title: 别再抽卡式做 AI 视频了！高级感全靠“故事板铁三角”
- Source type: Douyin short video, downloaded and processed as video source.
- Aweme ID: `7648163855390149888`
- Original video URL: `https://www.douyin.com/video/7648163855390149888`
- Author: N次方Ai（华小二团队）
- Author UID: `1488081381519034`
- Co-creator: AIGC玩家, role `编剧`
- Publish time: 2026-06-06 16:27 CST
- Capture date: 2026-06-28
- Duration: 198.834 seconds
- Language: Chinese

## Source Metrics At Capture

- Likes: 1237
- Comments: 81
- Collections: 1329
- Shares: 199
- Platform tags: 个人管理 / 职场技能 / 办公效率
- Hashtags: ai教程, ai短剧, ai创作浪潮计划, 伙伴计划, Image2
- Author follower count at capture: 6674
- Author total favorited at capture: 26884

## Raw Evidence

- Full video: `raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/source.mp4`
- Extracted audio copy: `raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/source-audio.m4a`
- dycli normalized detail: `raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/dycli-detail.json`
- dycli full raw detail: `raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/dycli-detail-raw.jsonl`
- Visible page text: `raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/page-text.txt`
- Structured chapter/source summary: `raw/videos/douyin-storyboard-triangle-ai-video-2026-06-28/source-summary.json`
- Whisper ASR: `raw/transcripts/douyin-storyboard-triangle-ai-video-2026-06-28/storyboard-whisper.raw.txt`
- Keyframes: `raw/assets/douyin-storyboard-triangle-ai-video-2026-06-28/keyframes/`
- Contact sheet: `raw/assets/douyin-storyboard-triangle-ai-video-2026-06-28/contact-sheet.jpg`
- OCR attempt: `raw/assets/douyin-storyboard-triangle-ai-video-2026-06-28/ocr/all-keyframes-ocr.txt`

## Domain Placement

- Primary domain: 视觉制作 / AI 视频.
- Formal page disposition: create new playbook page.
- Existing pages linked:
  - [[domains/视觉制作/06-AI视频/02-AI商业短视频规划方法|AI商业短视频规划方法]]
  - [[domains/视觉制作/06-AI视频/03-导演式镜头设计方法|导演式镜头设计方法]]
  - [[domains/视觉制作/06-AI视频/05-AI视频导演Prompt模板|AI视频导演 Prompt 模板]]
  - [[domains/视觉制作/06-AI视频/20-导演知识系统/02-视觉设计与故事板系统|视觉设计与故事板系统]]

## Extraction Tools

- `dycli favorites cdp-find --query 故事板`
- `dycli video cdp-detail 7648163855390149888 --raw-full --page-text-out`
- `ffmpeg` for full video inspection, audio extraction, and keyframes.
- `whisper-cli` with `ggml-large-v3-turbo.bin` for ASR.
- `tesseract` attempted for keyframe OCR; output was empty, so visual evidence is preserved as images and contact sheet.

## Sensitivity And Restrictions

- Source is from the user's logged-in Douyin browser session and used for personal knowledge-base compilation.
- The platform reports download restrictions for the public item, including an AI-generated-content download restriction. The video was obtained from the logged-in web page as local source evidence and is kept in private raw storage.
- Do not redistribute the raw video or raw response files.
