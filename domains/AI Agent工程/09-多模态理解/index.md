---
title: Agent 多模态理解
type: concept
created: 2026-07-23
updated: 2026-07-23
domain: AI Agent工程
tags: [ai-agent, video-understanding, multimodal, evidence]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
  - _meta/extraction-notes/agent-video-understanding-2026-07-23/coverage-matrix.md
status: active
---

# Agent 多模态理解

本目录回答一个实际问题：Codex、SealSeek/OpenClaw 等 Agent 怎样把视频读成可检索、可验证、可继续推理的证据，而不只是生成一段似是而非的摘要。

## 按任务进入

- 第一次建立“读视频”能力：[[domains/AI Agent工程/09-多模态理解/01-Agent读懂视频的证据化架构|Agent 读懂视频的证据化架构]]
- 抖音、视频号、1—15 分钟教程：[[domains/AI Agent工程/09-多模态理解/02-短教学视频读取工作流|短教学视频读取工作流]]
- 1—2 小时课程、会议或跨视频资料：[[domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索|长教学视频分层索引与检索]]
- 故事广告、产品广告、AI 成片验收：[[domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检|广告故事与产品视频质检]]
- 在 Codex/SealSeek 中落地：[[domains/AI Agent工程/09-多模态理解/05-Codex与SealSeek视频读取实现协议|Codex 与 SealSeek 视频读取实现协议]]
- 选择 GitHub 项目或模型：[[domains/AI Agent工程/09-多模态理解/06-开源项目与技术选型|开源项目与技术选型]]

## 默认原则

1. 先确定问题和读取深度，再决定抽多少帧、是否 OCR、是否跟踪对象。
2. 先用确定性工具拆解视频，再让视觉语言模型解释局部证据。
3. 每个结论应能回到时间范围、字幕、画面或声音。
4. 长视频先索引后局部精读；短视频可以一次生成完整证据包。
5. 广告片按目标和失败模式验收，不用开放式摘要代替质检。

## Agent 入口

[[queries/Agent读懂视频入口|Agent 读懂视频入口]]
