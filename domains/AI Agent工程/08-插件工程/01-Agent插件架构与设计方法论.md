---
title: Agent 插件架构与设计方法论
type: concept
created: 2026-07-14
updated: 2026-07-14
domain: AI Agent工程
tags: [ai-agent, plugin, skill, cli, mcp, connector, hooks, architecture]
sources:
  - raw/webpages/agent-plugin-engineering-2026-07-14/research-notes.md
  - _meta/extraction-notes/agent-plugin-engineering-2026-07-14/coverage-matrix.md
status: active
---

# Agent 插件架构与设计方法论

<!-- coverage: KU01 KU02 KU03 KU04 KU05 KU06 KU07 KU08 KU09 KU10 KU11 KU12 KU13 KU14 KU15 KU18 KU19 KU20 KU22 -->

## 一句话定义

Agent Plugin 不是另一种执行工具，而是把 Agent 完成一类任务所需的认知、执行、连接、治理和分发能力，封装成一个可安装、可版本化、可启停、可审计的产品单元。

- CLI 负责执行。
- Skill 负责让 Agent 知道何时以及如何执行。
- MCP/Connector 负责结构化连接外部系统。
- Hook 负责生命周期中的机械触发与约束。
- Plugin 负责把它们作为一个整体交付。

## 1. Plugin 的五面模型

### 1.1 认知面：Agent 如何理解任务

典型组件是 Skill、reference、模板、案例和路由说明。认知面回答：用户说什么时触发能力，主线和分支是什么，调用哪个工具，失败后回到哪里，输出满足什么契约。

Skill 采用渐进披露：系统先看到名称和描述，匹配任务后读取 `SKILL.md`，执行中再加载 references/scripts。这使插件可以携带多个专项 Skill，而不会一次把全部知识塞进上下文。

### 1.2 执行面：真正完成动作的确定性能力

执行面可以是 CLI、本地脚本、原生 Runtime、API client、浏览器自动化、MCP Tool 或 Connector 动作。

Plugin 不要求统一为某一种。GitHub 插件同时使用 Connector、`git` 和 `gh`；Sites 同时包含脚本、本地 MCP 和 Connector；Computer Use 携带本地原生 Runtime。执行面的核心标准是输入输出明确、错误可观察、行为可测试、危险动作可识别。

### 1.3 连接面：身份、会话和外部系统

| 方式 | 适合 | 优势 | 代价 |
| --- | --- | --- | --- |
| CLI 内置连接 | 本机系统、浏览器登录态、文件和 OS | 直接、可调试、复用已有代码 | Agent 需解析进程输出，跨宿主发现较弱 |
| 本地 MCP | 将本机 CLI/Runtime 暴露给多个 Agent Host | Tool schema、动态发现、统一调用 | 多一层协议和进程生命周期 |
| 远程 MCP | SaaS、团队服务、跨机器共享 | 标准 Tool/Resource、HTTP/OAuth | 部署、认证和可用性治理成本 |
| Connector/App | 托管授权、平台连接管理、可选 UI | 用户授权体验完整 | 依赖平台能力和审核流程 |
| 浏览器/CDP | 只有 Web 登录态或缺少稳定开放 API | 复用真实用户会话 | 页面和风控脆弱，需限速与停止规则 |

连接不一定独立于 CLI。`tbcli` 把 CDP、登录态和淘宝页面内请求封装在 CLI 中，这本身是合法的连接层设计；插件化不要求把它拆掉。

### 1.4 治理面：权限、生命周期与安全

治理面包括认证边界、只读/写入/破坏性动作、用户确认、dry-run、Hook 审查、日志审计、限速停止、第三方 Skill/脚本/MCP/二进制来源，以及卸载后的授权处理。

Hook 只适合必须在固定生命周期机械发生的动作，例如写入后 lint、工具调用前阻断、会话结束归档。需要语义判断的业务主线仍属于 Skill。

### 1.5 分发面：把内部能力变成可安装产品

分发面包括：

- Manifest：名称、版本、描述、作者、组件入口；
- 命名空间：避免 Skill、Tool、Hook 冲突；
- Assets 与默认 Prompt：帮助用户理解和启动能力；
- Marketplace：发现、安装、升级、启停和卸载；
- 版本与缓存：确保升级可判断、旧版本可追踪；
- 发布材料：隐私、条款、权限、测试和变更说明。

只有补上这一面，“CLI + Skill + 连接”才从本机工程组合升级为 Plugin。

## 2. 组件边界

| 组件 | 核心问题 | 是否直接执行 | 是否负责分发 |
| --- | --- | --- | --- |
| Prompt/Thread | 这一次怎么做 | 否 | 否 |
| AGENTS/Rules | 这个项目长期遵守什么 | 否 | 否 |
| Skill | Agent 如何完成某类任务 | 可调度执行器 | 通常由 Plugin 分发 |
| Workflow/Script | 固定步骤如何确定性运行 | 是 | 否 |
| CLI | 人和 Agent 如何稳定调用本地能力 | 是 | 只负责程序自身分发 |
| MCP | Host 如何发现并结构化调用工具/资源 | 是 | 协议不等于 Plugin 分发 |
| Connector/App | 平台如何连接授权服务并提供工具/UI | 是 | 通常由平台管理 |
| Hook | 生命周期节点如何自动触发或阻断 | 是 | 可由 Plugin 携带 |
| Plugin | 如何把以上能力整体安装、版本化和治理 | 间接 | 是 |

## 3. 四种成熟插件模式

### A. Skill-only Plugin

适合已有稳定外部工具，插件只分发工作方法、模板和路由。简单且跨平台潜力高，但依赖用户预装 CLI 或已有服务。

### B. Connector-first + CLI fallback

GitHub 插件是典型案例：Connector 处理 PR/Issue/评论等远程结构化数据，本地 `git`/`gh` 处理分支、提交、推送和 Actions 日志。原则是让每个执行面承担最合适的职责。

### C. 共享 MCP + 多专项 Skills

Figma 插件用同一个 Connector/MCP 提供通用工具面，再由多个 Skill 处理设计读取、文件创建、设计系统、Code Connect、SwiftUI 和 Motion。适合“一个平台连接、多个高层任务”。

### D. 本地 Runtime + MCP/Skill

Sites 和 Computer Use 表明，插件可以带本地 Node server、Shell script 或原生 App，再通过 Skill 或 MCP 交给 Agent 使用。适合本机能力、专用依赖和需要 Tool schema 的场景。

## 4. 能力成熟度阶梯

```text
一次性脚本 -> 稳定 CLI -> Skill 封装 -> 多执行面组合
            -> Plugin 打包 -> Marketplace / 团队治理 / 公开发布
```

1. 脚本验证“能不能做”。
2. CLI 稳定“如何重复调用”。
3. Skill 解决“Agent 会不会正确调用”。
4. 多执行面解决“不同信息和动作如何组合”。
5. Plugin 解决“如何整体安装和升级”。
6. Marketplace/治理解决“如何让更多人安全使用”。

不要为了拥有 Manifest 而过早插件化。Manifest 只能包装成熟度，不能替代稳定契约。

## 5. Plugin Readiness Gate

满足越多，越适合从 Skill 升级为 Plugin：

- 同一能力需要跨项目、跨 Agent 或跨用户复用。
- 已有稳定 CLI/API/MCP 契约，不依赖设计者在场救火。
- 需要同时交付多个 Skill、脚本、连接或 Hook。
- 需要统一安装、启停、升级、卸载和版本追踪。
- 需要明确权限、认证、隐私和破坏性操作。
- 需要默认 Prompt、品牌资产或用户可发现入口。
- 已有正向、负向、安装、升级和干净会话测试。

以下情况继续本地 Skill 更好：业务主线仍频繁变化、只有个人单项目实验、CLI 输出/错误码未稳定、连接经常手工修复、没有真实分发需求。

## 6. 安全和供应链原则

1. 把 Plugin 当作“代码 + 操作说明 + 外部权限”的供应链包。
2. 审核 Manifest、Skill、Hook、MCP 配置、脚本、二进制和网络访问。
3. 默认最小权限；查询和写入拆开；破坏性动作显式确认。
4. 认证材料留在密钥库、OAuth 或专用配置，不写进 Skill、Manifest 和日志。
5. Tool 描述必须准确说明副作用。
6. Hook 比 Skill 更接近强制执行，启用前审查触发时机和命令。
7. Marketplace 升级要做差异审查，版本和变更说明反映权限变化。
8. 卸载 Plugin 不一定注销 Connector，要分开检查代码卸载和授权撤销。

## 7. 测试矩阵

| 层 | 测试 |
| --- | --- |
| Manifest | schema、相对路径、组件注册、命名冲突 |
| CLI/Runtime | 输入输出、错误码、超时、幂等、脱敏 |
| MCP/Connector | Tool schema、认证失败、权限不足、网络中断、副作用标注 |
| Skill | 触发、分支、工具选择、失败回主线、输出契约 |
| Hook | 触发条件、退出码、阻断/放行、重复执行 |
| 安装 | 新环境安装、首次认证、依赖检查 |
| 升级 | 旧配置兼容、迁移、缓存、回滚 |
| 安全 | 正向、负向、越权请求、破坏性确认 |

复用 [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|干净子 Agent Skill 回归]]，并增加安装、认证、启停、升级和卸载测试。

## 8. 跨平台可移植性

Skill、CLI、MCP 和业务测试可尽量平台无关；Manifest、Connector ID、Hook schema、Marketplace 和 UI 元数据通常平台特有。

```text
可移植核心
├── CLI / Runtime
├── Skills / references / scripts
├── MCP server（可选）
└── 业务契约测试

平台适配壳
├── .codex-plugin/plugin.json
├── .app.json / Codex hooks / marketplace
├── .claude-plugin/plugin.json（如需要）
└── 其他平台注册文件
```

共享能力核心，分别维护薄适配壳，不强行让不同平台共用一个 Manifest schema。

## 相关记忆

- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
- [[domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件|从 CLI 与 Skill 演进为 Codex 插件]]
- [[domains/AI Agent工程/07-评测与调试/01-AI Agent执行链路审计方法|AI Agent 执行链路审计方法]]
