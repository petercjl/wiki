---
title: HTML 生成 CLI 与伴生 Skill 组合规范
type: playbook
created: 2026-08-10
updated: 2026-08-10
domain: AI Agent工程
tags: [html, cli, skill, workflow, ai-agent-engineering]
sources:
  - raw/articles/commerce-ui-companion-skill-2026-08-10/source-evidence.md
  - _meta/extraction-notes/commerce-ui-companion-skill-2026-08-10/coverage-matrix.md
status: active
---

# HTML 生成 CLI 与伴生 Skill 组合规范

本页解决两个工程问题：如何让多个 Agent 共用同一套 HTML 生成能力，以及一个业务 Skill 如何稳定调用另一个 Skill 而不复制旧版本。

## 一、先区分“可以组合”和“自动注入”

Skill 可以编排另一个 Skill，但当前开放 Agent Skills 格式不保证：调用方只写出另一个 Skill 的名字，宿主就会自动安装或加载它。

可靠组合必须由宿主或调用方显式完成：

1. 按精确名称解析被调用 Skill。
2. 读取被调用 Skill 当前完整的 `SKILL.md`。
3. 从被调用 Skill 根目录解析其相对脚本、references 和 assets。
4. 执行被调用 Skill 的主线和 QA。
5. 完成后返回调用方主线。

不得模糊匹配相似名称，也不得把被调用 Skill 的说明和代码复制进调用方。复制会形成独立分叉，失去自动继承更新的能力。

## 二、四层架构

```text
业务 Skill
  └─ 运行时按名称加载 compact-commerce-ui
       └─ 读取实时 CLI 版本、Schema 与 contract
            └─ commerce-ui 确定性渲染和验证
                 └─ ViewModel JSON + 自包含 HTML
```

职责边界：

| 层 | 负责 | 不负责 |
| --- | --- | --- |
| 业务 Skill | 数据获取、业务分析、报告意图、领域判断 | HTML/CSS/JS 模板 |
| 伴生 Skill | 把业务证据映射为 ViewModel，编排 CLI 与 QA | 固定渲染实现 |
| CLI | Schema、模板、组件、路由、响应式、渲染、验证 | 开放式业务推理 |
| contract | 业务 Skill 与 CLI 的稳定数据边界 | 自动兼容破坏性变化 |

## 三、CLI 是伴生 Skill 的唯一源码

稳定 CLI 的安装目录必须同时包含伴生 Skill。CLI 内的 Skill 是唯一可编辑源码；Codex、SealSeek、OpenClaw 或其他 Agent 的 Skill 目录只是安装目标。

推荐两种投影：

- **链接**：Agent 目录链接到 CLI 内源码；源码一更新，下次加载立即生效。
- **受管副本**：用于不支持链接的宿主；副本带管理清单，通过 CLI 检测和更新。

禁止把 Agent 安装目录当成第二源码。更新器不得覆盖没有管理标记的现有 Skill。

## 四、发现与安装协议

Agent 找到 CLI 后，应先运行：

```bash
command -v commerce-ui
commerce-ui version --json
commerce-ui doctor
commerce-ui skill source --json
```

然后针对自己的 Skill 根目录执行：

```bash
commerce-ui skill status --target-dir <agent-skill-root>
commerce-ui skill install --target-dir <agent-skill-root>
```

已知宿主可使用 `--agent codex`、`--agent agents`、`--agent openclaw` 或 `--agent sealseek`。受管副本更新时使用：

```bash
commerce-ui skill update --target-dir <agent-skill-root>
```

边界是：CLI 不会主动向所有 Agent 推送自己。Agent 至少要检查 `help`、`doctor`、`skill source`，或者由上游 Skill/全局规则执行发现步骤。宿主若按会话缓存 Skill catalog，安装或更新后需要刷新目录或开启新会话。

## 五、嵌套 Skill 的调用合同

未来创建一个会调用其他 Skill 的 Skill 时，必须写清以下字段；它们可以是正文中的合同，不依赖尚未标准化的 frontmatter：

```yaml
logical_dependency: compact-commerce-ui
resolution: exact-name-runtime-load
required_cli: commerce-ui
required_contract: compact-workbench@1.0
input_handoff: business evidence + report intent
output_handoff: ViewModel JSON + HTML + validation result
failure: DEPENDENCY_UNAVAILABLE | CLI_UNAVAILABLE | CONTRACT_UNSUPPORTED
return_to_main_line: caller validation and delivery step
```

调用方主线必须包含：

1. 检测 CLI 与被调用 Skill。
2. 缺少 Skill 时使用其官方安装面，而不是重写替代品。
3. 每次执行都加载当前 Skill，并查询实时 CLI 能力。
4. 交接输入与预期输出。
5. 接收结果后回到调用方自己的数据核对、验收和交付。

## 六、版本与更新规则

| 变化 | 旧业务 Skill 是否自动受益 | 条件 |
| --- | --- | --- |
| CLI 修复渲染 bug | 是 | 入口仍在 PATH，contract 兼容 |
| CLI 增加可选组件 | 是 | 伴生 Skill 运行时读取 live schema |
| 伴生 Skill 改进编排说明 | 是 | 调用方每次重新加载，不复制旧说明 |
| Agent 使用受管副本 | 否，需 update | 执行 `skill status/update` |
| contract 破坏性变化 | 否 | 保留旧 contract 或显式迁移调用方 |
| 宿主缓存 Skill catalog | 延迟生效 | 刷新 catalog 或新会话 |

版本号与 contract 应分开管理。CLI 可以升级而继续支持旧 contract；旧业务 Skill 不应被迫追随不兼容 schema。

## 七、创建和验收清单

创建嵌套 Skill 时检查：

- [ ] 依赖使用精确名称，不用模糊描述。
- [ ] 调用方没有复制被调用方正文、脚本或模板。
- [ ] 写明解析方法、版本/contract、输入、输出、失败和返回主线。
- [ ] 能发现官方安装入口，并对缺失依赖明确失败。
- [ ] 自动声明实验与显式加载实验分开做。
- [ ] 干净上下文能真正读取被调用 Skill 并运行关键命令。
- [ ] CLI 的 doctor/self-test 和 Skill 的格式、可移植性验证通过。
- [ ] 未受管的用户 Skill 不会被更新器覆盖。

一次成功运行不等于协议成立。测试必须证明：没有设计对话背景时，调用方仍能找到正确依赖、获得当前版本并完成主线。

## 八、Commerce UI 已验证实例

`commerce-ui 1.1.0` 提供 `skill source/status/install/update`；报告 contract 继续使用 `compact-workbench@1.0`。Codex 的 `compact-commerce-ui` 采用链接安装，实际读取 CLI 内唯一源码；通用 copy 安装与未受管内容拒绝也已测试。

HTML 报告任务的执行顺序是：先读取本页，再使用 [[domains/AI Agent工程/11-网页设计规范/01-网页UI设计总则|网页 UI 设计总则]]、布局/组件/内容规则，最后按 [[domains/AI Agent工程/11-网页设计规范/06-验收与反模式|验收与反模式]] 验收。

## 相关记忆

- [[domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法|可分享跨 Agent Skill 创建方法]]
- [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|主对话与干净子 Agent 的 Skill 回归测试方法]]
- [[domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范|Agent 驱动型电商 CLI 设计与开发规范]]
- [[queries/网页报告与SaaS界面设计入口|网页报告与 SaaS 界面设计入口]]

## 来源覆盖

本页覆盖 KU01—KU12；逐项映射见 `_meta/extraction-notes/commerce-ui-companion-skill-2026-08-10/coverage-matrix.md`。
