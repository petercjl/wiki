---
title: AI视频音频与声线一致性入口
type: query
created: 2026-07-04
updated: 2026-07-04
domain: 视觉制作
tags: [visual-production, ai-video, workflow]
sources:
  - domains/视觉制作/06-AI视频/07-声音设计与BGM/10-Seed-Audio短视频音频一致性工作流.md
status: active
---

# AI视频音频与声线一致性入口

当用户要求处理 AI 短视频 BGM、配乐、人物配音、声线参考、一致性、原片去 BGM 保留对白、Seed-Audio 或 `seedaudiocli` 相关任务时，先读：

1. [[domains/视觉制作/06-AI视频/07-声音设计与BGM/10-Seed-Audio短视频音频一致性工作流|Seed-Audio短视频音频一致性工作流]]
2. [[domains/视觉制作/06-AI视频/index|AI视频]]
3. [[domains/视觉制作/06-AI视频/06-视频剪辑与连续性/09-AI长视频连续性组接方法|AI长视频连续性组接方法]]

## 分支读取

- 如果任务是写完整 AI 视频脚本、分镜、首尾帧或图生视频 prompt，同时读 [[queries/AI视频导演与分镜入口|AI视频导演与分镜入口]]。
- 如果任务需要 Seedance 模型能力边界，同时读 [[domains/视觉制作/06-AI视频/80-模型与工具/01-Doubao-Seedance-2.0视频生成模型卡|Doubao-Seedance-2.0 视频生成模型卡]]，并复核当前官方文档。
- 如果任务涉及人物、场景、产品等视觉一致性资产，同时读 [[domains/视觉制作/06-AI视频/04-图片与控制资产/07-故事板铁三角AI视频控制法|AI视频控制资产系统：身份板、故事板、导演台与素材库]]。

## 标准判断步骤

1. 判断音频目标：整段 BGM、对白保留、人物声线参考、环境声/音效，还是多者组合。
2. 如果是 BGM，一般不要在每段视频生成时加入；优先成片后生成整段 BGM。
3. 如果原片有人声和 BGM，先判断是否需要源分离，保留 vocals 后再替换 BGM。
4. 如果是人物声线，先选择符合人物身份的内置 `voice_type`，再用 prompt 微调情绪、语气和说话状态。
5. 为视频模型做声音参考时，输出 3-5 秒干净单人台词，不带 BGM 和音效。
6. 明确哪些能力已经验证，哪些需要继续实验。

## 输出边界

- 不要承诺 Seed-Audio 已经直接理解视频画面并自动配乐，除非当次任务做了 direct video input 验证。
- 不要用一个通用声线硬调所有角色，除非任务只是做边界测试。
- 不要把 EvoLink 当前 voice list 当成永久事实；生产前要复核当前文档。

