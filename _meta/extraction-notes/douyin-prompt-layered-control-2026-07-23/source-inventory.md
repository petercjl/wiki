# Source Inventory

| source_id | durable_path | type | units | notes |
| --- | --- | --- | ---: | --- |
| S01 | `raw/videos/douyin-prompt-layered-control-2026-07-23/original.mp4` | 原始视频 | 1 | 281.658 秒，原样保留 |
| S02 | `raw/transcripts/douyin-prompt-layered-control-2026-07-23/transcript.raw.txt` | 原始 ASR 文本 | 57 段 | 不修改，包含可纠正错词 |
| S03 | `raw/transcripts/douyin-prompt-layered-control-2026-07-23/transcript.raw.srt` | 原始 ASR 字幕 | 57 段 | 带时间码 |
| S04 | `raw/transcripts/douyin-prompt-layered-control-2026-07-23/transcript.raw.json` | Whisper 完整 JSON | 57 段 | 包含 token 和置信信息 |
| S05 | `raw/assets/douyin-prompt-layered-control-2026-07-23/keyframes/` | 关键帧 | 56 | 每 5 秒 1 帧 |
| S06 | `raw/assets/douyin-prompt-layered-control-2026-07-23/ocr/` | 逐帧 OCR | 56 | 原始 OCR，不做人工覆盖 |
| S07 | `raw/transcripts/douyin-prompt-layered-control-2026-07-23/ocr.raw.txt` | 合并 OCR | 56 帧 | 保留文件名与逐帧文本 |

## Semantic Segments

| segment_id | time_range | topic | primary_evidence |
| --- | --- | --- | --- |
| SEG01 | 00:00–00:38 | 短 Prompt 稳定、细节堆叠后失控；问题在于未分层 | ASR + frame 002–007 |
| SEG02 | 00:38–01:34 | 约束满足、Prompt 服从度、文本编码与高维语义向量 | ASR + frame 007–016 |
| SEG03 | 01:34–02:06 | 多目标优化、注意力资源与条件冲突 | ASR + frame 020–025 |
| SEG04 | 02:06–02:36 | 第一层技术压力：文本编码压缩损失 | ASR + frame 027–031 |
| SEG05 | 02:36–03:03 | 第二层技术压力：条件引导与画面质量张力 | ASR + frame 032–035 |
| SEG06 | 03:03–03:36 | 第三层技术压力：视频时间一致性 | ASR + frame 039–041 |
| SEG07 | 03:36–04:11 | 三层 Prompt 写法：硬约束、关键细节、风格 | ASR + frame 043–050 |
| SEG08 | 04:11–04:40 | 复杂镜头拆镜头/拆阶段及辅助控制手段 | ASR + frame 052–054 |
| SEG09 | 04:40–04:41 | 结束语 | ASR |

