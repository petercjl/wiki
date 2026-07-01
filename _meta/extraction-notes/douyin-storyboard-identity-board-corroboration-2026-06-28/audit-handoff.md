# Audit Handoff: 抖音故事板/身份板补充搜索

## What Changed

- Extended `domains/视觉制作/06-AI视频/07-故事板铁三角AI视频控制法.md`.
- Added a corroboration section based on four selected Douyin videos.
- Preserved search results, ranking, details, MP4 files, ASR transcripts, and keyframes.
- Added named visual-evidence screenshots for knowledge units that are primarily visual.

## Key Claims To Audit

1. The original triangle model is corroborated by high-engagement videos: style/original image, identity board, and storyboard separate different control variables.
2. Storyboards should behave like construction drawings or director instructions, not final stills.
3. Complex spatial relation needs a director-table / staging layer.
4. Commercial AI video can use storyboard as a structure-transfer tool after decomposing a reference video.
5. Identity boards can be layered: three-view, face three-view, action poses, cinematic character card, and product style sheet.
6. For short-video ingestion, screenshots must be treated as source units when the claim depends on visible layout or visual form.

## Known Limits

- Douyin comments were not scraped; engagement ranking used numeric counts returned by search/detail endpoints.
- ASR may contain homophone errors, especially model names such as Seedance and Image2.
- Page text was archived and named screenshots were extracted; visual OCR over every keyframe was not performed in this pass.
- Search results are time-sensitive and personalized to the current logged-in/browser context.

## Suggested Future Work

- Add a reusable `dycli search cdp-find` command if this search-rank-select workflow repeats often.
- Add keyframe OCR for videos that contain dense prompt templates or UI steps.
- Convert the strengthened method into an Agent template for producing actual storyboards, identity boards, and video prompts from a user script.
