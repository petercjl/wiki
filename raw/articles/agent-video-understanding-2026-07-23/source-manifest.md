---
title: Agent 视频理解开源资料包清单
type: raw-source
created: 2026-07-23
updated: 2026-07-23
domain: raw
tags: [video-understanding, agent, github, papers]
status: active
---

# Agent 视频理解开源资料包

本目录保存 2026-07-23 为“Codex / SealSeek 如何读懂视频”研究而抓取的原始资料。仅保存论文、论文文本和项目 README；未下载模型权重或数据集。

## GitHub 项目

| 项目 | GitHub | 抓取 commit | 作用 |
| --- | --- | --- | --- |
| whisper.cpp | https://github.com/ggml-org/whisper.cpp | `080bbbe85230f624f0b52127f1ae1218247989f9` | 本地语音识别、时间戳、VAD |
| PySceneDetect | https://github.com/Breakthrough/PySceneDetect | `bba97f59ff082875cf1c41b8ce2cb52a34ed2020` | 镜头边界检测 |
| PaddleOCR | https://github.com/PaddlePaddle/PaddleOCR | `2661c7c0ef5c613e8f93c6e93b2e052399f0f854` | 中文字幕、画面文字、界面 OCR |
| Qwen3-VL | https://github.com/QwenLM/Qwen3-VL | `96588727e44c78b25ba03ea03b8e12f7e64fd0da` | 原生视频/多图视觉语言理解 |
| SAM 2 | https://github.com/facebookresearch/sam2 | `2b90b9f5ceec907a1c18123530e92e794ad901a4` | 视频对象分割与跟踪 |
| VideoITG | https://github.com/NVlabs/VideoITG | `50a60a822c0e362bfd8747c45ba34e66e9c9d650` | 指令驱动的时间定位和按需选帧 |
| LongVideoAgent | https://github.com/longvideoagent/LongVideoAgent | `3a80ba8ac9e8cfde4528c22c86955c2b6d9dbcfc` | 长视频多 Agent 迭代取证 |
| VideoRAG | https://github.com/HKUDS/VideoRAG | `c412a093a820ef7a0e0dda31076ed871136198b3` | 跨长视频结构化索引与检索 |
| OmAgent | https://github.com/om-ai-lab/OmAgent | `c131f82b16beb7740a4291a27775a4ea7dd1a186` | 图工作流、多模态 Agent 与视频 QA |
| Video-MME-v2 | https://github.com/MME-Benchmarks/Video-MME-v2 | `28fc3bcfbd4d162594c8e4bad866b694d9b035aa` | 视频理解能力分解与评测 |
| Q-Bench-Video | https://github.com/Q-Future/Q-Bench-Video | `7d56cd6749a74d101d9d196c969f07d10f8edd13` | 技术、美学、时序和 AIGC 视频质量评测 |

README 快照位于 `projects/`。

## 论文

`papers/` 保存 9 篇 PDF；`paper-text/` 保存逐页文本抽取结果：

- Whisper, arXiv:2212.04356
- Qwen3-VL, arXiv:2511.21631
- VideoITG, arXiv:2507.13353
- LongVideoAgent, arXiv:2512.20618
- VideoRAG, arXiv:2502.01549
- OmAgent, arXiv:2406.16620
- Video-MME-v2, arXiv:2604.05015
- Q-Bench-Video, arXiv:2409.20063
- SAM 2, arXiv:2408.00714

## 采集边界

- Git 仓库采用浅克隆/稀疏检出，工作副本位于 `/Users/pechen/AI/Video/research/agent-video-understanding-2026-07-23/repos/`。
- 未下载任何模型 checkpoint、训练数据或评测数据。
- 项目安装命令与依赖属于时间敏感信息，实际使用时应回查当前 README、release 与 CLI 帮助。

## 本地案例证据

`case-study/` 保存“3D 白模故事板”抖音短教程的 SRT、manifest 和联系表。原始 ASR 中 6 处“白毛”未被覆写；正式知识根据视频标题、画面和上下文校正为“白模”，具体证据见 `semantic-validation.md`。
