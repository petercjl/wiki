---
title: Agent 视频理解正式页面计划
type: source-summary
created: 2026-07-23
updated: 2026-07-23
domain: meta
tags: [llm-wiki, page-plan, video-understanding]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
status: active
---

# 正式页面计划

## 推荐位置

新建：

`domains/AI Agent工程/09-多模态理解/`

原因：用户的主问题是 Codex 与 SealSeek/OpenClaw 如何执行“读视频”、保存证据并复用结果，主体属于 Agent 工程；广告片只是三种输入场景之一。广告制作域建立相关链接即可，避免把 Agent 工具协议埋在视频创作资料中。

## 推荐页面

1. `index.md`：按任务、视频长度和问题类型路由。
2. `01-Agent读懂视频的证据化架构.md`：定义“读懂”、证据层、统一时间轴、深度等级与输出契约。
3. `02-短教学视频读取工作流.md`：抖音/视频号 1—15 分钟视频，含 ASR/OCR/画面交叉校正和案例。
4. `03-长教学视频分层索引与检索.md`：章节化、层级索引、检索、局部精读、跨视频课程。
5. `04-广告故事与产品视频质检.md`：叙事、镜头、声音、连续性、产品一致性和严重度。
6. `05-Codex与SealSeek视频读取实现协议.md`：工具节点、文件型中间产物、evidence ledger、停止条件与降级。
7. `06-开源项目与技术选型.md`：11 个项目按“直接采用/借鉴协议/专项可选/只作评测”分级。

## 路由更新

- 新增查询入口：`queries/Agent读懂视频入口.md`。
- 更新：`domains/AI Agent工程/index.md`。
- 建立相关记忆：`domains/视觉制作/06-AI视频/index.md`。
- 更新根 `index.md` 与 `log.md`。

## 备选方案

- 备选 A：放入 `domains/视觉制作/06-AI视频/`。优点是广告视频邻近；缺点是长教学视频、Agent/RAG 协议和 SealSeek 实现不属于创作知识。
- 备选 B：在 `domains/AI Agent工程/05-工具链/` 写单页。优点是页面少；缺点是三类工作流、评测与工具协议会挤成超长页面，路由性较差。

## 确认与执行

- 用户于 2026-07-23 明确确认：`domains/AI Agent工程/09-多模态理解/`。
- 计划中的 6 个正式页面、分类索引和查询入口已创建。
- AI Agent 工程索引、AI 视频相关记忆、根索引和日志已更新。
