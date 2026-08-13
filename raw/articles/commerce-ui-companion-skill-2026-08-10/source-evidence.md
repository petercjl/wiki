# Commerce UI CLI、伴生 Skill 与嵌套 Skill 组合证据

采集日期：2026-08-10

## 用户要求

1. `compact-commerce-ui` 不以 Codex 安装目录为源码，而应与 `commerce-ui` CLI 绑定。
2. CLI 内的 Skill 是唯一更新源；Codex 与其他 Agent 只安装或更新这个来源。
3. 任意 Agent 发现 CLI 后，应能发现其伴生 Skill、判断是否安装并执行安装或更新。
4. Codex 未来创建“一个 Skill 调用另一个 Skill”时，应自动遵守统一组合规范。
5. 将上述架构和操作边界写入个人 Wiki。

## 规范与实现证据

- Agent Skills 规范定义元数据、激活和渐进加载，但截至采集日没有标准化的 Skill 依赖字段或自动依赖注入协议：https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- 社区依赖 RFC 正在讨论版本、依赖清单和锁文件，说明该能力仍处于设计阶段：https://github.com/agentskills/agentskills/discussions/210
- OpenClaw 的组合 Skill RFC 提议 `requires.skills`、接口和继承，但尚不是通用既成标准：https://github.com/openclaw/openclaw/issues/11919
- AWS CLI Agent Orchestrator 采用显式 `load_skill`，证明宿主可以实现按名称加载，但这是运行时实现，不是 `SKILL.md` 自动依赖：https://github.com/awslabs/cli-agent-orchestrator/blob/main/docs/skills.md

## 本机隔离实验

- 自动声明实验：调用 Skill 只写明依赖名称，并禁止主动定位被调用 Skill。干净上下文结果为 `AUTO_DEPENDENCY_NOT_LOADED`。
- 显式组合实验：调用 Skill 按精确名称定位、完整读取被调用 Skill，并相对其根目录运行脚本。干净上下文成功返回标记 `ORCHID-7421`。
- 结论：Skill 可以编排 Skill，但必须由宿主或调用方执行显式加载；只写依赖名称不能作为可靠执行协议。

## 落地实现

- `commerce-ui` 从 1.0.0 升级到 1.1.0，报告 contract 仍为 `compact-workbench@1.0`。
- CLI 新增：`skill source`、`skill status`、`skill install`、`skill update`。
- `doctor` 返回伴生 Skill 名称、唯一源码、摘要和安装提示。
- CLI 安装目录内的 `skill/compact-commerce-ui/` 是唯一 Skill 源码。
- Codex 安装位置改为指向唯一源码的符号链接。
- Unix-like 系统默认链接；不支持链接的宿主可使用带管理清单的副本。
- `update` 只更新 CLI 管理的副本，拒绝覆盖未受管的用户内容。
- Codex 全局 `AGENTS.md` 新增嵌套 Skill 组合和 CLI 伴生 Skill 规则。

## 验证

- CLI Python 语法检查通过。
- `commerce-ui doctor` 与 `commerce-ui self-test` 通过。
- Codex 链接状态为 `current`，解析到 CLI 内唯一源码。
- 通用目标目录的 copy 安装、状态和无变更 update 通过。
- 对未受管目标执行 update 被正确拒绝。
- `compact-commerce-ui` 格式验证通过；shareable 可移植性扫描 0 error、0 warning。

## 边界

- CLI 的存在不能主动向所有 Agent 推送 Skill。Agent 至少需要运行 CLI 的 `help`、`doctor` 或 `skill source`，或者由上游 Skill/全局规则执行发现步骤。
- 链接安装可即时读取唯一源码；受管副本必须显式执行 update。
- 宿主若按会话快照 Skill 元数据，安装或更新后仍需刷新 Skill catalog 或开启新会话。
- CLI 兼容更新可自动流入旧调用方；破坏性 contract 变更需要保留旧版本或显式迁移。
