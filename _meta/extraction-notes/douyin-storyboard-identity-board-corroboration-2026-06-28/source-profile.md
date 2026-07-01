# Source Profile: 抖音故事板/身份板补充搜索

- Source type: Douyin search corpus plus selected short videos.
- Capture date: 2026-06-28.
- Tooling: `dycli search cdp`, `dycli video cdp-detail`, `ffmpeg`, `whisper-cli`.
- Search keywords:
  - `AI视频 故事板`
  - `故事板 身份板`
  - `AI短剧 身份板` (0 valid items)
  - `AI视频 角色板 故事板` (interrupted, 0 valid items)
- Candidate pool: 93 unique candidates after deduplication and removal of the previously ingested `7648163855390149888`.
- Selection rule: prioritize likes and comments, then preserve conceptual coverage for storyboards, identity boards, Image2/Seedance workflows, and director-space control.
- Formal disposition: extend existing page `domains/视觉制作/06-AI视频/07-故事板铁三角AI视频控制法.md`.

## Selected Sources

| aweme_id | Author | Publish Time (CST) | Captured Engagement | Source Role |
| --- | --- | --- | --- | --- |
| `7643404202686020081` | 居鲁仕 | 2026-05-24 18:32 | 20733 likes, 754 comments, 17778 collections, 3128 shares | Strong corroboration of original triangle model. |
| `7651618528713871355` | 李一帆 | 2026-06-15 21:47 | 10624 likes, 323 comments, 9176 collections, 1796 shares | Adds director table / spatial staging layer. |
| `7647464806470962447` | 隋校长 AIGC | 2026-06-04 17:09 | 6132 likes, 102 comments, 5576 collections, 1816 shares | Adds commercial-video reverse-engineering workflow. |
| `7649315926764827322` | Eliot学长 | 2026-06-09 16:52 | 407 likes, 12 comments, 425 collections, 65 shares | Adds identity-board aesthetic / character-card layer. |

## Raw Package

- Search ranking: `raw/videos/douyin-storyboard-identity-board-corroboration-2026-06-28/ranked-candidates.json`
- Selected source summary: `raw/videos/douyin-storyboard-identity-board-corroboration-2026-06-28/selected-source-summaries.json`
- Detail JSON and page text: `raw/videos/douyin-storyboard-identity-board-corroboration-2026-06-28/details/`
- MP4 videos: `raw/videos/douyin-storyboard-identity-board-corroboration-2026-06-28/*.mp4`
- ASR transcripts: `raw/transcripts/douyin-storyboard-identity-board-corroboration-2026-06-28/`
- Keyframes: `raw/assets/douyin-storyboard-identity-board-corroboration-2026-06-28/keyframes/`

## Safety Note

During this run, valid detail responses were captured and video files were downloaded from returned Douyin video URLs. If Douyin verification, CAPTCHA, login failure, or abnormal empty responses occur in future runs, stop immediately and ask the user to handle the browser state.
