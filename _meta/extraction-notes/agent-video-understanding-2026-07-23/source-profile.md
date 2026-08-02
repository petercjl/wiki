---
title: Agent 视频理解开源资料来源档案
type: source-summary
created: 2026-07-23
updated: 2026-07-23
domain: meta
tags: [llm-wiki, video-understanding, agent]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
status: active
---

# Agent 视频理解开源资料来源档案

## 来源范围

- 来源类型：11 个 GitHub 项目 README、9 篇对应或互补论文 PDF、9 份逐页文本抽取。
- 适配器：Markdown 文档与网页剪藏的混合资料包；PDF 使用本地 `pypdf` 逐页抽取。
- 抓取日期：2026-07-23。
- 语言：英文为主，LongVideoAgent 含中文 README。
- 原始归档：`raw/articles/agent-video-understanding-2026-07-23/`。
- 工作副本：`/Users/pechen/AI/Video/research/agent-video-understanding-2026-07-23/`。

## 用户问题

用户需要同一套 Agent 方法覆盖三类视频：

1. 1—15 分钟的抖音/视频号教学短视频；
2. 1—2 小时以上的长教学视频；
3. 自制故事广告片和产品广告片。

目标环境同时包括 Codex 和 SealSeek（封装 OpenClaw），因此正式知识不能绑定单一模型或单一 Agent 框架，而应定义稳定的中间产物、工具契约、证据结构和按任务选择深度的路由。

## 核心判断

“读视频”不是把整段视频直接扔给视觉模型，而是把视频编译成一套带时间坐标的可核查证据：

- 容器与流元数据；
- 镜头/场景边界；
- 音频转写和字幕；
- 画面文字/OCR；
- 代表帧和按问题追加的证据帧；
- 对象、人物、产品的跨帧轨迹；
- 事件、因果和叙事结构；
- 每个结论所引用的时间段和证据类型。

短教学视频强调多通道交叉校正；长教学视频强调先索引、后检索、再局部精读；广告片强调叙事意图、镜头语言、连续性、产品一致性和质量目标。

## 本机既有条件

- 已有 FFmpeg/ffprobe。
- 已有本地 `whisper-cli`。
- 已有 Whisper 模型 `/Users/pechen/.local/share/whisper.cpp/models/ggml-large-v3-turbo.bin`，无需重复下载语音模型。
- 既有抖音案例已验证：仅靠 ASR 会把“白模”识别成“白毛”，必须用画面字幕和语境修正。

## 时效与边界

- GitHub README、依赖版本、模型 API 与 benchmark 排名均是 2026-07-23 快照。
- 论文结论用于架构原则，不把论文榜单当成本机实测结果。
- 本批只下载源码/文档/论文，不含权重和数据集。
- 当前尚未创建正式知识页；等待用户确认落点。
