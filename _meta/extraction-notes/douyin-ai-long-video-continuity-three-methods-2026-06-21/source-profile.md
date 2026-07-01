# Source Profile

| Field | Value |
| --- | --- |
| Source title | 别再硬续15秒了！AI长视频丝滑连贯的3个方法 |
| Source slug | `douyin-ai-long-video-continuity-three-methods-2026-06-21` |
| Source type | Douyin short video, downloaded via `dycli` detail video URL |
| Platform id | `7653852870844464113` |
| Author | 李一帆 |
| Published | 2026-06-21 22:18 |
| Captured | 2026-07-01 |
| Duration | 329.28 seconds |
| Adapter | `llm-wiki-ingest/adapters/transcript.md` + video-course branch |
| Language | Chinese |
| Domain placement | `domains/视觉制作/06-AI视频/` |
| Existing memory searched | AI视频 index, 导演式镜头设计方法, 商业短视频摄影与运镜语法, 故事板铁三角AI视频控制法, 导演知识系统 |
| Fusion disposition | create one focused playbook and link it into the existing AI 视频 learning path |
| Query entry decision | no new `queries/` page; existing `08-Agent使用模板：AI视频导演分镜.md` is the operational routing page and was updated |
| Sensitivity | Public educational Douyin video; raw media preserved for personal wiki evidence |
| Time sensitivity | Tool UI details such as LibTV buttons may change; formal page abstracts method rather than hard-coding UI |

## Raw Sources

- `raw/videos/douyin-ai-long-video-continuity-three-methods-2026-06-21/source-0.mp4`
- `raw/videos/douyin-ai-long-video-continuity-three-methods-2026-06-21/dycli-detail.json`
- `raw/videos/douyin-ai-long-video-continuity-three-methods-2026-06-21/dycli-raw-full.jsonl`
- `raw/videos/douyin-ai-long-video-continuity-three-methods-2026-06-21/page-text.txt`
- `raw/transcripts/douyin-ai-long-video-continuity-three-methods-2026-06-21/source.raw.txt`
- `raw/transcripts/douyin-ai-long-video-continuity-three-methods-2026-06-21/source.raw.srt`
- `raw/transcripts/douyin-ai-long-video-continuity-three-methods-2026-06-21/source.raw.json`
- `raw/assets/douyin-ai-long-video-continuity-three-methods-2026-06-21/keyframes/`
- `raw/assets/douyin-ai-long-video-continuity-three-methods-2026-06-21/keyframes-ocr.raw.txt`

## Extraction Tools

- `dycli video cdp-detail 7653852870844464113 --port 9228`
- `ffprobe` for media inspection
- `ffmpeg` for 16 kHz mono WAV and keyframes
- `whisper-cli` with `/Users/pechen/.local/share/whisper.cpp/models/ggml-large-v3-turbo.bin`
- `tesseract -l chi_sim+eng` for sampled keyframe OCR
