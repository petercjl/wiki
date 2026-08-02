---
title: AI Agent 工具链
type: concept
created: 2026-06-14
updated: 2026-07-29
domain: AI Agent工程
tags: [toolchain, ai-agent, index]
sources:
  - raw/articles/company-shared-gpu-worker-2026-07-24/observed-system-evidence.md
  - _meta/extraction-notes/company-shared-gpu-worker-2026-07-24/coverage-matrix.md
  - raw/articles/agent-driven-ecommerce-cli-methodology-2026-07-29/source-evidence.md
  - _meta/extraction-notes/agent-driven-ecommerce-cli-methodology-2026-07-29/coverage-matrix.md
status: active
---

# 工具链

Agent 开发中涉及的外部工具、API、通道和平台的集成方法与配置。

## 页面

- [[domains/AI Agent工程/05-工具链/01-OpenAI图像生成API集成指南|OpenAI 图像生成 API 集成指南]]
- [[domains/AI Agent工程/05-工具链/02-飞书机器人Sealseek通道配置|飞书机器人 Sealseek 通道配置]]
- [[domains/AI Agent工程/05-工具链/03-公司共享GPU工作节点与分时调度方法|公司共享 GPU 工作节点与分时调度方法]]：从远程 GPU 原型演进到多人可治理任务服务的方法；当前超分项目尚处原型阶段。
- [[domains/AI Agent工程/05-工具链/04-Real-ESRGAN远程超分案例|Real-ESRGAN 远程超分案例]]：Tailscale + SSH/SCP + Windows GPU 的已验证初步测试。
- [[queries/公司GPU共享与远程任务调度|公司 GPU 共享与远程任务调度]]：公司 GPU 共享、异地访问和排队调度的 Agent 入口。

## 关联模块

- [[domains/AI Agent工程/10-插件Skill与CLI/index|插件、Skill 与 CLI]]：稳定 CLI、Agent Skill 与 Plugin 产品化的连续工程主线。
- [[queries/Agent驱动型电商CLI开发入口|Agent 驱动型电商 CLI 开发入口]]：新建或扩展 tbcli、dycli、jdcli、alicli 等工具时的查询与执行路由。
