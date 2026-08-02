---
title: 插件、Skill 与 CLI
type: concept
created: 2026-07-29
updated: 2026-07-29
domain: AI Agent工程
tags: [ai-agent, plugin, skill, cli, toolchain, index]
sources:
  - raw/articles/agent-driven-ecommerce-cli-methodology-2026-07-29/source-evidence.md
  - _meta/extraction-notes/agent-driven-ecommerce-cli-methodology-2026-07-29/coverage-matrix.md
  - raw/webpages/agent-plugin-engineering-2026-07-14/research-notes.md
  - _meta/extraction-notes/agent-plugin-engineering-2026-07-14/coverage-matrix.md
status: active
---

# 插件、Skill 与 CLI

本模块研究如何把业务需求逐步沉淀为稳定 CLI、Agent 可用 Skill 和可安装 Plugin。三者不是互相替代的技术选项，而是认知、执行和产品化分发的协同体系。

```text
业务需求
→ 稳定 CLI 执行核心
→ Skill 认知与编排
→ Plugin 安装、治理与分发
```

## 阅读顺序

1. [[domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范|Agent 驱动型电商 CLI 设计与开发规范]]：先建立可发现、可停止、可测试、可发布的稳定执行核心。
2. [[domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件|从 CLI 与 Skill 演进为 Codex 插件]]：通过交接门后，再组织 Skill、Manifest、MCP 和 Marketplace。
3. [[domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论|Agent 插件架构与设计方法论]]：需要判断组件边界和插件成熟度时，读取五面架构模型。

## 主题边界

- 本模块负责 CLI、Skill 与 Plugin 的连续工程生命周期；
- `03-Skill设计` 负责 Skill 本身的设计、测试和可移植方法；
- `05-工具链` 负责外部工具、API、通道和运行节点；
- `08-插件工程` 保留通用插件架构理论；
- 具体电商渠道的接口、字段和操作规则仍属于相应渠道知识域。

## Agent 查询入口

- [[queries/Agent驱动型电商CLI开发入口|Agent 驱动型电商 CLI 开发入口]]：创建、扩展、评审或发布稳定 CLI。
- [[queries/Agent插件设计与CLI改造|Agent 插件设计与 CLI 改造]]：判断是否插件化，以及设计 Skill、MCP、Manifest 和 Marketplace。
