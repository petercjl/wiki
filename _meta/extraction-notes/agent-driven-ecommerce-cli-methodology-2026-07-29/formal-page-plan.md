---
title: Agent 驱动型电商 CLI 方法论正式页面计划
type: source-summary
created: 2026-07-29
updated: 2026-07-29
domain: meta
tags: [llm-wiki, cli, ecommerce, ai-agent]
sources:
  - raw/articles/agent-driven-ecommerce-cli-methodology-2026-07-29/source-evidence.md
status: active
---

# 正式页面计划

## 来源理解

这不是淘宝平台操作说明，而是从 tbcli 实践中提炼的跨渠道 Agent CLI 工程方法，涵盖能力发现、浏览器会话、数据获取、风控停止、交付契约、测试、分发和持续演化。

## 查重结论

- 插件工程页面解释 CLI、Skill、MCP 和 Plugin 的架构关系，但没有给出电商 CLI 的完整开发契约。
- 1688 CLI 页面包含平台专属能力和安全契约，但不适合作为淘宝、抖音、京东等渠道的共同母规范。
- 因此建议创建一份通用 playbook，并以相关记忆连接现有页面，不做破坏性合并。

## 推荐落位

- 主页面：`domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范.md`
- 查询入口：`queries/Agent驱动型电商CLI开发入口.md`
- 更新导航：
  - `domains/AI Agent工程/05-工具链/index.md`
  - `domains/AI Agent工程/index.md`
  - `domains/电商运营/index.md`
  - `index.md`
  - `log.md`

## 推荐处置

- 主页面：`create-new`
- 查询入口：`create-new`
- 现有插件工程、1688 CLI安全契约：保留并交叉链接
- Query Entry Gate：需要。该知识支持反复创建、评审和扩展 tbcli、dycli、jdcli、alicli，且未来用户更可能用自然语言触发。

## 为什么以 AI Agent工程 为主域

规范主要回答“如何把电商渠道能力做成 Agent 可发现、可调用、可测试、可发布的 CLI”，核心是工具工程和执行契约，而不是某个平台的运营规则。电商运营域增加桥接入口，保证从业务知识也能找到。

## 备选方案

在 `domains/电商运营/` 新建“电商系统与工具”子目录。当前不推荐，因为现有知识量不足以支撑新的稳定分类，容易产生只有一个页面的薄目录。

## 确认状态

- 用户确认：已确认
- 确认证据：用户于 2026-07-29 回复“可以的，开始入库吧”
- 最终确认路径：`domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范.md`
- 正式页面写入：已完成

## 2026-07-29 分类调整

- 用户进一步确认把 CLI 规范与其下游插件演进手册共同归入 `domains/AI Agent工程/10-插件Skill与CLI/`。
- 调整原因：两篇知识形成“稳定 CLI 执行核心 → Skill 认知与路由 → Plugin 安装与分发”的连续功能模块，后续还会继续扩展。
- 原 `05-工具链` 保留为关联入口，不再作为主页面所在地。
