# Source Profile

- Source title: 淘宝批量修改、商品复制与店群同步帮助视频
- Source slug: `taobao-batch-modification-help-videos`
- Source type: Bilibili video tutorial batch
- Adapter: `transcript.md` + `video-course-ingest.md`
- Original source: 1 current Bilibili page plus 13 visible right-side tutorial entries
- Uploader: `bili_92697058599`
- Publication range: 2023-09-10 to 2026-06-16
- Capture date: 2026-08-11
- Language: Chinese
- Media count: 14
- Total duration: 3323.672 seconds / 55.39 minutes
- Primary evidence: spoken explanation + software UI screen recording
- Sensitivity: screenshots contain demo shop/product identifiers; keep original frames in private raw and avoid embedding account-identifying frames unless redacted
- Time sensitivity: high; UI labels, feature availability, synchronization fields, and platform behavior may change
- Existing memory search: no same-topic formal page found; closest category is `domains/电商运营/30-ERP与系统工具/`
- Placement candidate proposed by Agent: `domains/电商运营/30-ERP与系统工具/02-淘宝批量修改与店群同步工具/`
- User correction: this tool does not belong to ERP; place it under Taobao/Tmall ecommerce automation
- Confirmed final location: `domains/电商运营/02-淘宝天猫/电商自动化/批量修改/`
- Confirmed fusion disposition: create-new task-oriented subcategory, split into durable playbooks, and cross-link the 1688 page
- Placement confirmation status: confirmed by user on 2026-08-11

## Resolved Toolchain

- Downloader: `/Users/pechen/.local/bin/yt-dlp` 2026.07.04
- FFmpeg: `/opt/homebrew/bin/ffmpeg`
- FFprobe: `/opt/homebrew/bin/ffprobe`
- ASR: `/opt/homebrew/bin/whisper-cli`
- Whisper model: `/Users/pechen/.sealseek/knowledge-space/toolchain/models/ggml-small.bin`
- OCR: `/opt/homebrew/bin/tesseract` 5.5.2 with `chi_sim+eng`
- Python launcher: `/opt/homebrew/opt/python@3.14/bin/python3.14` 3.14.3

## Durable Raw Paths

- Videos and metadata: `raw/videos/taobao-batch-modification-help-videos/`
- Raw ASR: `raw/transcripts/taobao-batch-modification-help-videos/`
- Keyframes: `raw/assets/taobao-batch-modification-help-videos/`
- Working audio/OCR/contact sheets: `_meta/working/taobao-batch-modification-help-videos/`
