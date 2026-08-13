# Source Profile

- Source title: 真正的 Prompt 强控，不是写得更长，而是分层级
- Source slug: `douyin-prompt-layered-control-2026-07-23`
- Source type: 抖音短教学视频
- Adapter: `llm-wiki-ingest/adapters/transcript.md`
- Original URL: https://www.douyin.com/video/7660700852612631823
- Author: AIGC制作宝典
- Capture date: 2026-07-23
- Language: 中文
- Duration: 281.658 秒
- Media: H.264 1920×1080 30fps；AAC 44.1kHz
- SHA-256: `1dfdf27e524fea3d92e405a5b223ec84b9ac3808a8dcb12b283f73494ee1b5e9`
- Sensitivity: 无个人隐私、凭据或内部数据
- Time sensitivity: 底层解释和方法不绑定具体模型版本；CFG 与模型架构表述应作为通用解释，不推断所有商业模型均使用同一实现
- Candidate domain: `domains/视觉制作/06-AI视频/`
- Existing pages found:
  - `domains/视觉制作/06-AI视频/05-视频生成/05-AI视频导演Prompt模板.md`
  - `domains/视觉制作/06-AI视频/03-分镜脚本/25-09-AI短视频完整视听分镜Prompt结构.md`
  - `queries/AI视频导演与分镜入口.md`
- Proposed disposition: 新建一页完整的“AI 视频 Prompt 分层强控方法”，从现有 Prompt 模板页和 query 入口建立关联
- Placement confirmation: confirmed by user on 2026-07-23
- Confirmed formal path: `domains/视觉制作/06-AI视频/05-视频生成/12-AI视频Prompt分层强控方法.md`

## Resolved Tooling

- Python launcher: `/opt/homebrew/bin/python3`（Python 3.14.3，probe passed）
- FFmpeg: `/opt/homebrew/bin/ffmpeg`
- FFprobe: `/opt/homebrew/bin/ffprobe`
- Whisper CLI: `/opt/homebrew/bin/whisper-cli`
- Whisper model: `/Users/pechen/.local/share/whisper.cpp/models/ggml-large-v3-turbo.bin`
- Tesseract: `/opt/homebrew/bin/tesseract`
- OCR languages: `chi_sim+eng`

## Extraction Parameters

- Audio: mono PCM 16kHz WAV
- ASR: Whisper large-v3-turbo，中文，带 AIGC/Prompt/视频生成术语初始提示
- Keyframes: 每 5 秒 1 帧，共 56 帧，1280×720
- OCR: Tesseract `chi_sim+eng --psm 6`
- Primary evidence: 语音 + 画面信息图 + 烧录字幕
