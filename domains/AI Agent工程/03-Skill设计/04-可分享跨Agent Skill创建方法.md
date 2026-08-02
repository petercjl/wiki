---
title: 可分享跨 Agent Skill 创建方法
type: playbook
created: 2026-07-15
updated: 2026-07-15
domain: AI Agent工程
tags: [skill, ai-agent, workflow, portability, privacy]
sources:
  - raw/articles/portable-skill-creator-methodology-2026-07-15/source.md
  - _meta/extraction-notes/portable-skill-creator-methodology-2026-07-15/coverage-checklist.md
  - https://agentskills.io/specification
status: active
---

# 可分享跨 Agent Skill 创建方法

本页解决两个反复出现的问题：Skill 在创建过程中带入作者本机信息，以及 Skill 被某一个 Agent 的目录、工具名或元数据锁死。核心方法不是复制系统 `skill-creator`，而是建立一个用户拥有的薄扩展 `portable-skill-creator`，在运行时组合基础创建能力，并追加可移植性质量门。

## 一、为什么不复制系统 Skill Creator

Skill 之间没有正式的继承、版本依赖或自动合并机制。复制系统 Skill 虽然能得到创建当时的全部内容，但副本随后会独立演化：基础 Skill 的新流程、验证规则和错误修复不会自动进入副本。

直接修改系统内置 Skill 也不稳定，升级可能覆盖本地修改。因此应采用：

```text
当前系统 skill-creator
        │ 提供通用创建主线
        ▼
portable-skill-creator
        │ 追加隐私、机器独立、跨 Agent 与 QA 规则
        ▼
可分享 Skill 成品
```

这是一种组合式扩展，不是真正继承。它能在每次创建时使用当前基础 Skill 的最新能力，但基础流程变化后仍需检查规则冲突。

## 二、默认路由与显式例外

全局规则负责选择入口：

1. 创建、更新、审查或测试任何 Agent Skill 时，默认使用用户自己的 `portable-skill-creator`。
2. `portable-skill-creator` 再组合当前环境可用的基础 `skill-creator` 或等价创建能力。
3. 不要把系统 `skill-creator` 当成默认的独立入口。
4. 只有用户明确要求“单独使用系统/内置 skill-creator”时，才跳过 portable 扩展。
5. 用户只说“创建一个 Skill”，或泛称“用 Skill Creator”，不构成例外。

这个路由同时解决两个目标：持续获得基础 creator 的更新，又保证每次创建都经过用户自己的隐私和可移植性标准。

## 三、两层规则的职责

| 层 | 负责内容 | 不负责内容 |
| --- | --- | --- |
| 全局 `AGENTS.md` | 默认入口、强制优先级、显式例外、全局底线 | 具体扫描算法和创建细节 |
| `portable-skill-creator` | 组合基础 creator、分类、架构、扫描、QA、适配层 | 复制基础 creator 的完整正文 |
| 系统 `skill-creator` | 需求理解、资源规划、初始化、编辑、基础验证、迭代 | 用户专属的跨 Agent 隐私策略 |

## 四、可移植核心与平台适配层

跨 Agent 可用不要求所有文件完全相同。应把稳定能力和平台差异分开：

```text
skill-name/
├── SKILL.md                 # Agent Skills 通用核心
├── scripts/                 # 稳定执行接口
├── references/              # 通用方法与按需平台说明
├── assets/                  # 与平台无关的模板/资源
└── agents/                  # 可选平台 UI metadata，不得成为核心依赖
```

通用核心默认只依赖 `SKILL.md` 的 `name` 与 `description`、相对资源路径、明确的输入输出契约，以及运行时可检测的命令/API/MCP 能力。平台专属 metadata、目录和工具名只能作为可选适配，不得成为其他 Agent 无法执行核心工作流的原因。

## 五、机器独立与隐私规则

可分享 Skill 不应携带：

- 作者用户名、主目录、设备名或主机名；
- 本地绝对路径和只在作者机器存在的安装位置；
- 邮箱、私有域名、内网地址、账号 ID；
- token、cookie、API key、密码、私钥或真实配置值；
- 私有知识库、隐藏上下文或未随 Skill 分发的文件；
- 未声明的软件、CLI、MCP、浏览器扩展或系统权限假设。

替代方式：

- Skill 内资源使用相对 Skill 根目录的路径；
- 外部位置使用语义化环境变量或用户配置；
- 密钥从目标 Agent 的 secret/environment 机制读取；
- 依赖在运行时检测，缺失时返回明确的兼容性错误或安装分支；
- 固定、高风险步骤优先封装为带输入输出契约的脚本或稳定 CLI。

## 六、创建主线

1. **加载基础能力**：读取当前可用的基础 Skill 创建流程，不依赖复制的旧版本。
2. **分类目标**：判断成品是通用可分享、组织内部、本机专用还是指定平台专用；未说明时默认通用可分享。
3. **设计边界**：把任务知识和工作流放入核心，把目录、metadata 和专属工具调用隔离为适配层。
4. **实现资源**：使用相对路径、参数、环境变量、能力检测和稳定执行接口。
5. **执行扫描**：扫描全部文本与脚本中的秘密、本机标识、绝对路径和未声明平台耦合。
6. **执行验证**：通过格式验证、脚本测试和依赖检查。
7. **干净上下文测试**：让没有设计对话背景的 Agent 执行真实小任务；失败必须回写主线、分支、错误处理或 QA。
8. **报告兼容性**：区分“规范兼容”“已在某平台实测”和“平台专用”，不得把未测试写成已支持。

任何分支处理完后，都必须回到扫描、验证和兼容性报告这条主线。

## 七、三道完成门

### 1. 格式门

- `SKILL.md` frontmatter 合法；
- 名称、描述和目录结构符合开放 Agent Skills 基础规范；
- 引用文件存在且使用相对路径。

### 2. 可移植性门

- 高置信秘密或作者主目录命中必须失败；
- 私有地址、个人邮箱、平台专属目录等命中必须人工解释或隔离；
- 扫描输出只报告规则、文件和行号，不重复打印可能的秘密内容。

### 3. 独立执行门

- 在干净上下文中读取磁盘上的 Skill；
- 覆盖触发、主线、关键分支、工具节点和 QA；
- 产物型 Skill 必须生成真实可检查产物；
- 失败应修改 Skill 后重测，而不是仅在设计对话中临时补救。

## 八、更新与冲突处理

每次基础 `skill-creator` 更新后，不需要同步复制全文。运行时读取当前版本，并检查：

- 是否改变初始化结构；
- 是否新增必须字段或平台 metadata；
- 是否更换验证器；
- 是否引入新的平台路径或工具假设；
- 是否与 portable 的隐私、核心中立或 QA 规则冲突。

无冲突的基础能力直接继承式享用；发生冲突时，保留通用创建能力，以用户明确设定的隐私与可移植规则覆盖平台绑定部分，并把新的兼容问题写回 `portable-skill-creator`。

## 九、判断标准

一个 Skill 只有同时满足以下条件，才能标记为“可分享”：

- 不依赖作者私有上下文；
- 不包含真实秘密和机器标识；
- 核心工作流不要求特定 Agent 的专属 metadata；
- 所有外部依赖都有声明、检测或降级路径；
- 格式和可移植性扫描通过；
- 至少完成一次干净上下文验证；
- 对尚未实测的平台保持诚实的兼容性标注。

## 相关记忆

- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
- [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|主对话与干净子 Agent 的 Skill 回归测试方法]]
- [[domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论|Agent 插件架构与设计方法论]]
- [[domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库|跨 Agent Skill 注册库]]

## 来源覆盖

本页覆盖来源知识单元 KU01、KU02、KU03、KU04、KU05、KU06、KU07、KU08；逐项映射见 `_meta/extraction-notes/portable-skill-creator-methodology-2026-07-15/coverage-matrix.md`。
