---
title: Agent 视频理解遗漏审计
type: source-summary
created: 2026-07-23
updated: 2026-07-23
domain: meta
tags: [llm-wiki, omission-audit, video-understanding]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
status: active
---

# 遗漏审计

## 有意不进入正式页

- 项目宣传、star、贡献者、社区二维码和 citation 样板：原始 README 已保存，不构成 Agent 执行知识。
- 训练命令、checkpoint 下载、数据集下载：本次没有训练或部署这些研究模型的目标，且用户不希望无必要下载模型。
- 官方 benchmark 排名：只作为来源背景保存，不冒充当前本机模型表现。
- 逐平台安装细节：依赖和命令时效强，正式页只记录“何时选它、输入输出是什么、执行前如何核验”。

## 当前未解决

- 正式知识归属尚待用户确认。
- Codex 与 SealSeek 的最终 CLI 命令名还未固化；正式页先定义中立协议，后续真实使用中再演进 CLI。
- 尚未对三类视频构建完整回归集。当前只有一个抖音短教学案例的本地证据。
- Qwen3-VL、VideoITG、LongVideoAgent、VideoRAG、OmAgent、SAM 2 尚未在本机安装权重或端到端运行，因此不能写成“已验证生产能力”。

## 覆盖检查

- 工具层：解封装、ASR、镜头切分、OCR、VLM、时间定位、对象跟踪、RAG/Agent 均有来源。
- 三类视频：短教学、长教学、故事/产品广告均有独立知识单元。
- Agent 层：中间产物、证据引用、迭代停止条件、失败回退和 CLI 演进均已纳入。
- 质量层：理解能力与广告质量使用不同评测维度，没有混成单一分数。
