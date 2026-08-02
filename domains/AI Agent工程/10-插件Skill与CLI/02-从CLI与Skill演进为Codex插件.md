---
title: 从 CLI 与 Skill 演进为 Codex 插件
type: playbook
created: 2026-07-14
updated: 2026-07-14
domain: AI Agent工程
tags: [ai-agent, plugin, codex, cli, skill, mcp, migration, playbook]
sources:
  - raw/webpages/agent-plugin-engineering-2026-07-14/research-notes.md
  - _meta/extraction-notes/agent-plugin-engineering-2026-07-14/coverage-matrix.md
status: active
---

# 从 CLI 与 Skill 演进为 Codex 插件

<!-- coverage: KU16 KU17 KU18 KU20 KU21 KU22 -->

## 目标

把已经运行的“CLI + Skill + 外部连接”体系升级为 Codex 可安装能力包，同时保留 CLI 作为稳定执行面，不为插件化重写成熟业务代码。

本手册是《Agent 驱动型电商 CLI 设计与开发规范》的下游产品化阶段。前者负责把业务能力做成稳定、安全、可测试的执行核心；本手册负责在核心稳定后，增加 Skill 认知、Plugin 组件和 Marketplace 分发。虽然前置规范以电商 CLI 为主要案例，其能力自描述、进程契约、测试和交接门也适用于其他 Agent 驱动型 CLI。

## 1. 先画出现状，不急着建 Manifest

| 项目 | 要回答的问题 |
| --- | --- |
| 用户任务 | 用户安装的是哪类结果？ |
| Skills | 哪些任务需要不同 Skill？是否有总入口？ |
| CLI 命令 | 输入、输出、副作用和错误是什么？ |
| 外部连接 | API、CDP、OAuth、Cookie、文件或数据库在哪里？ |
| 编排 | 哪些由 Agent 判断，哪些由脚本固定执行？ |
| 权限 | 哪些只读、写入、开放世界或破坏性？ |
| 状态 | 配置、缓存、登录态和输出在哪里？ |
| 依赖 | Node/Python/浏览器/系统 App/第三方 CLI 是否必需？ |

这一阶段的产物是能力地图，不是插件目录。

## 2. 通过 CLI 到 Plugin 的交接门

插件化前，先按《Agent 驱动型电商 CLI 设计与开发规范》的 Plugin Readiness Gate 检查执行核心。至少应满足：

- `capabilities --json` 是能力清单的单一事实源；
- command/subcommand、`--help`、`--json`、schema version 和错误码稳定；
- stdout/stderr、超时、重试、限速、脱敏、dry-run和确认策略可验证；
- `doctor --json` 能让 Skill 判断依赖、版本、浏览器和认证前置状态；
- 正向、负向、契约、打包和全新安装测试通过。

Skill 不应猜测自然语言日志。若所需信息不在正式 JSON 或文件契约中，先扩展 CLI 命令或字段，再更新 Skill。没有通过交接门时，继续修复 CLI；Manifest、MCP 和 Hook 不能弥补执行层契约漂移。

## 3. 选择 CLI 交付策略

### A. 外部依赖

插件只分发 Skills 和配置，运行前检查 CLI 和版本。适合 CLI 已有独立安装/升级和用户群，或涉及大型系统依赖。需提供最低版本、安装说明和 doctor 命令。

### B. 随插件打包

把 Node/Python/原生 Runtime 放在插件根目录的 scripts/bin/runtime，由 Skill 从自身路径解析 Plugin Root 后调用。适合能力只服务该插件、依赖可控、希望一键安装。必须使用相对路径并处理平台架构、可执行权限和升级。

### C. 增加 MCP Adapter

保留 CLI/Library 作为业务核心，MCP server 将稳定能力包装成 Tool schema。适合多 Host 复用、动态发现、复杂结构化结果、远程化或 OAuth。MCP 负责协议适配，不重新实现业务。

## 4. 重构 Skill 为插件认知层

```text
skills/
├── domain-entry/SKILL.md       # 总入口、上下文解析、路由
├── task-a/SKILL.md             # 专项任务
├── task-b/SKILL.md
└── task-c/SKILL.md
```

总入口负责识别上下文、分类意图、决定 Connector/MCP/CLI 优先级并尽快路由。专项 Skill 负责一条清晰主线、最小 references、精确工具调用、风险确认、输出契约和 QA。

不要原样堆叠多个 Skill 而没有总入口，也不要压成一个巨大 `SKILL.md`。

## 5. 决定 MCP、Connector 和 Hook

增加 MCP 的信号：多个 Host 使用同一工具、需要 Tool discovery、返回结构复杂、远程服务需要 OAuth、CLI 进程输出成为集成摩擦。

继续 CLI-only 的信号：只在本机使用、依赖当前目录/浏览器 Profile/系统 App、CLI JSON 已稳定、没有跨宿主需求。

需要平台托管授权、ChatGPT 连接管理、远程 SaaS 或自定义 UI 时再加入 Connector/App。只有在固定生命周期必须发生时才用 Hook；需要语义判断和用户沟通的流程仍属于 Skill。

## 6. Codex Plugin 目录

```text
my-plugin/
├── .codex-plugin/
│   └── plugin.json
├── skills/
├── scripts/                    # 可选
├── runtime/                    # 可选
├── .mcp.json                   # 可选
├── .app.json                   # 可选
├── hooks/                      # 可选
├── assets/                     # 可选
├── README.md
└── tests/
```

最小 Manifest：

```json
{
  "name": "my-plugin",
  "version": "0.1.0",
  "description": "What reusable outcome this plugin provides",
  "skills": "./skills/"
}
```

按需添加 `mcpServers`、`apps`、`hooks` 和 `interface`。Manifest 不声明尚未测试的能力。

## 7. 安装与配置契约

插件安装后必须能回答：

1. 是否要额外安装 CLI/Runtime？
2. 首次认证在哪里完成？
3. 配置存在哪里，是否跨版本保留？
4. 如何运行 doctor/status？
5. 如何启停、升级和卸载？
6. 卸载后是否需撤销 OAuth、Connector 或浏览器 Profile？

优先提供 `mycli doctor --json`，让 Skill 读取诊断结果，而不是用零散 shell 猜环境状态。

## 8. 测试金字塔

测试责任按层划分：

1. CLI 执行层：命令、schema、错误码、认证、安全策略、分页、数据完整性、交付格式、打包和全新安装。
2. Skill 认知层：干净上下文触发、意图路由、输入收集、工具选择、风险确认和异常回主线。
3. Plugin 组件层：Manifest、相对路径、CLI发现、版本门、MCP、Hook、assets和组件注册。
4. 安装生命周期：Plugin全新安装、首次授权、启停、升级、回滚和卸载。
5. 端到端正负测试：典型任务，以及缺认证、版本不符、权限不足、风控验证、危险操作和非目标平台。

CLI测试不应在插件测试中重复实现；插件测试应验证它调用的是正确版本和正式契约。

## 9. Marketplace 路线

1. 本地 plugin directory 开发。
2. 个人 Marketplace 安装测试。
3. 新任务验证组件加载。
4. 小范围 repo/team Marketplace。
5. 版本升级和回滚演练。
6. 准备隐私、条款、权限和测试后再公开。

Marketplace 是分发层，不是开发工作区。Codex 可能从安装缓存加载插件，修改源目录后要按安装机制刷新，并在新任务验证。

这里的 Marketplace 发布与 CLI 自身发布是两条相关但独立的链路：

- npm、GitHub Release、OIDC和CLI语义化版本属于CLI分发；
- Plugin版本、组件注册、安装缓存和Marketplace属于插件分发；
- Plugin依赖外部CLI时，Manifest、README或doctor必须声明兼容版本；
- Plugin随包携带Runtime时，仍应复用同一CLI/Library核心，避免出现两套业务逻辑。

## 10. tbcli 的未来映射

tbcli 已经从单一物流命令演进为具有能力自描述、浏览器会话、安全请求策略和商品列表交付等能力的独立 CLI。其当前能力不得在本手册中手工维护，应始终以运行时结果为准：

```bash
tbcli capabilities --json
tbcli doctor --json
```

如果某个版本尚未提供 `doctor --json`，应先把它补成正式 CLI 能力，再让 Skill 或 Plugin 读取；不能由插件用零散 Shell 检查替代长期契约。

未来先决定：

1. 产品边界是通用“淘宝卖家助手”、单项业务插件，还是跨系统工作流。
2. `tbcli` 是独立 npm 依赖、随插件交付的 Runtime，还是由 MCP Adapter 暴露。
3. 专用浏览器 Profile 和 CDP 登录态是否继续作为主要连接方式。
4. 多 Host、远程化或复杂 Tool discovery 是否足以支持增加 Taobao MCP Adapter。
5. `wdtcli`、`dws` 等其他执行面属于同一产品边界还是外部依赖。

淘宝卖家助手形态可能是：

```text
taobao-seller-operations/
├── .codex-plugin/plugin.json
├── skills/taobao/SKILL.md
├── skills/logistics-review/SKILL.md
├── runtime/tbcli/              # 若选择随包
├── scripts/doctor.mjs
├── .mcp.json                   # 只有决定加 MCP 时才需要
├── assets/
└── tests/
```

跨系统物流看板形态可能是：

```text
ecommerce-logistics-dashboard/
├── skills/dashboard-update/
├── adapters/wdtcli
├── adapters/tbcli
├── adapters/dws
└── tests/contracts + tests/e2e
```

真正实施前先修复 CLI/Skill 契约漂移，再做 Manifest。插件化不会自动解决 README、默认配置和 JSON 输出不一致。

## 11. 完成定义

- 可从 Marketplace 安装并在新任务发现。
- Skill 使用相对路径或可发现的外部 CLI。
- CLI/MCP 返回稳定结构化结果。
- 权限、认证和危险动作边界清楚。
- 正向、负向、安装、升级、卸载测试通过。
- README、Manifest、默认 Prompt、Skill 和真实行为一致。
- 失败经验写回 CLI/Skill/测试，不只在当前对话补救。

## 相关记忆

- [[domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范|Agent 驱动型电商 CLI 设计与开发规范]]
- [[domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论|Agent 插件架构与设计方法论]]
- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
- [[domains/AI Agent工程/07-评测与调试/01-AI Agent执行链路审计方法|AI Agent 执行链路审计方法]]
