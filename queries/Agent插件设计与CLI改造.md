---
title: Agent 插件设计与 CLI 改造
type: query
created: 2026-07-14
updated: 2026-07-14
domain: AI Agent工程
tags: [ai-agent, plugin, cli, skill, mcp, query, architecture]
sources:
  - raw/webpages/agent-plugin-engineering-2026-07-14/research-notes.md
  - _meta/extraction-notes/agent-plugin-engineering-2026-07-14/coverage-matrix.md
status: active
---

# Agent 插件设计与 CLI 改造

## 何时使用

- “把这个 CLI/Skill 封装成插件。”
- “要不要把 CLI 改成 MCP？”
- “Skill、Plugin、Connector、Hook 怎么分层？”
- “如何建立个人或团队 Agent Plugin Marketplace？”
- “现有 CLI-first 系统是否具备插件化条件？”

## 必读顺序

1. [[domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论|Agent 插件架构与设计方法论]]
2. 如果执行核心是电商或浏览器 CLI，先检查：[[domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范|Agent 驱动型电商 CLI 设计与开发规范]]
3. [[domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件|从 CLI 与 Skill 演进为 Codex 插件]]
4. 复杂 Skill：[[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
5. 测试：[[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|Skill 干净回归测试方法]]

## 标准诊断步骤

1. 定义插件用户结果和产品边界。
2. 画出认知、执行、连接、治理、分发五面现状。
3. 检查 CLI/API/MCP 契约是否稳定。
4. 判断继续 Skill-only，还是通过 Plugin Readiness Gate。
5. 为每个外部能力选择 CLI、浏览器、MCP 或 Connector，不默认重写。
6. 决定 CLI 是外部依赖、随包 Runtime，还是 MCP Adapter。
7. 设计插件内总入口 Skill 和专项 Skills。
8. 设计 Manifest、相对路径、版本、配置、认证和 Marketplace。
9. 建立 CLI、Skill、组件、安装生命周期和安全测试。
10. 在新任务/干净环境验证后再发布。

## 标准输出

- 当前架构图；
- 插件产品边界；
- 保留、移动、新增和删除项；
- CLI/MCP/Connector 决策表；
- 插件目录和 Manifest 草案；
- 权限与认证模型；
- 依赖、配置和迁移策略；
- 测试矩阵；
- 分阶段实施路线。

## 边界

- 不因“插件更高级”而重写稳定 CLI。
- 不用 Manifest 掩盖不稳定契约。
- 不把 Token、Cookie、绝对私人路径写入插件。
- 不把业务主线塞进 Hook 或 MCP server。
- 不假设 Codex、Claude、Hermes 等平台 Manifest 相同；共享核心，分开维护适配壳。
- 涉及当前 Codex Manifest、Marketplace 或公开发布时，重新核对官方文档和本机 `codex plugin --help`。
