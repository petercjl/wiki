---
title: 主对话与干净子 Agent 的 Skill 回归测试方法
type: playbook
created: 2026-06-22
updated: 2026-06-22
domain: AI Agent工程
tags: [skill, ai-agent, subagent, regression-testing, context-engineering, workflow]
sources:
  - user-stated-principles-2026-06-22
status: active
---

# 主对话与干净子 Agent 的 Skill 回归测试方法

## 一句话定义

主对话负责理解用户意图、设计和修改 skill；干净子 Agent 负责在不继承主对话背景的情况下测试该 skill 是否真的落盘、是否能独立触发、是否能按主线完成任务。主 Agent 读取子 Agent 的结果并回写 skill，形成“设计 -> 落盘 -> 干净验证 -> 失败回写 -> 再验证”的闭环。

## 问题背景

创建 skill 本身并不难。真正高风险的地方在于：主对话中的 Agent 已经知道用户意图、补充解释、临时修正和预期答案，因此即使 skill 文件不完整，主对话也可能跑出正确结果。

这会造成两种假阳性：

- 上下文污染：当前对话能做对，不代表新对话能做对。
- 假落盘：Agent 口头说“已经写入 skill”，但优化内容可能只停留在当前对话的临时理解里，没有进入 `SKILL.md`、reference、script 或目标平台对应的 skill 文件。

因此，skill 验证的核心不是“当前对话能否完成任务”，而是“离开当前对话后，另一个干净 Agent 能否只凭 skill 文件完成任务”。

## 角色分工

| 角色 | 责任 |
| --- | --- |
| 主 Agent | 理解需求、设计 skill、修改文件、验证落盘、创建测试任务、读取子 Agent 结果、判断失败类型、回写 skill。 |
| 干净子 Agent | 不继承主对话背景，只读取主 Agent 给出的最小输入和 skill 文件，像未来真实使用者一样执行测试任务。 |
| 用户 | 提供设计目标、真实使用样本、关键验收标准；在高风险操作或分类不确定时做判断。 |

## 主线流程

### 1. 主对话中设计或优化 skill

主 Agent 可以充分利用上下文，理解用户的真实意图，并把需求沉淀进：

- `SKILL.md` 的使命、触发条件、主线流程、分支规则、工具节点、QA 和演化规则。
- `references/` 中的详细规则、模板、示例或领域知识。
- `scripts/` 中的确定性工具、校验器或转换脚本。
- `agents/openai.yaml` 中的 UI 元数据和默认调用提示。

### 2. 做硬落盘验证

主 Agent 不能只说“已经落盘”，必须给出可检查证据：

- 修改了哪些具体文件。
- `rg` 能否搜到新增规则。
- `git diff` 能否看到规则进入正确位置。
- 新增 reference/script 是否被 `SKILL.md` 引用。
- 新增脚本是否实际运行过，至少跑过代表性样例。

这一关专门拦截“对话里懂了，文件里没写”的情况。

### 3. 创建干净子 Agent 或干净会话

不同 Agent 工具的名字不同，但需要满足同一个抽象条件：测试执行者不能继承主对话的设计背景，只能看到真实任务输入、skill 文件和必要环境。

在 Codex 中，可以使用 `multi_agent_v1.spawn_agent` 创建子 Agent，并设置：

```json
{
  "fork_context": false
}
```

这表示子 Agent 不继承主对话历史，只看到系统/环境基础信息和主 Agent 给出的测试任务。

在 SealSeek/OpenClaw 等基于工作区或多 Agent 结构的工具中，应寻找等价能力：

- 创建不带当前设计对话历史的新 Agent/任务/会话。
- 只传入 skill 路径、真实测试请求、输入样例和操作边界。
- 由主 Agent 或主会话读取测试结果，并负责回写 skill。

在其他 Agent 工具中，如果没有后台子 Agent，也可以用新建干净会话、独立 workspace、临时 profile、无历史运行模式或人工可见新线程替代。只要能切断主对话背景，就可以执行这套方法。

子 Agent 提示词应模拟真实用户请求，而不是暴露主对话中的诊断结论。主 Agent 应提供：

- skill 的绝对路径。
- 一个真实用户未来会说的任务。
- 输入样例或测试材料。
- 允许和禁止的操作。
- 验收标准。
- 要求子 Agent 报告读取了哪些文件、如何理解主线、做了什么、是否缺规则。

不要提供：

- 预期答案。
- 主对话中的设计过程。
- 主 Agent 怀疑缺失的规则。
- “请检查某某问题是否已经修好”这类泄露答案的问题。

### 4. 主 Agent 读取并判断子 Agent 结果

子 Agent 的结果不能只看成功/失败，要看成功来源：

- 是否真的读取了目标 `SKILL.md`。
- 是否读到了必要 reference/script。
- 是否按 skill 主线执行，而不是自由发挥。
- 是否遇到异常后能回到主线。
- 是否输出了 skill 自己要求的交付物。
- 是否暴露出触发条件、主线、分支、工具或 QA 的缺口。

如果任务完成了，但没有依据 skill 执行，应判为假通过。

### 5. 失败分类并回写 skill

干净测试失败后，不要在子 Agent 对话里把任务手动救回来，而要由主 Agent 回到 skill 文件中修正。

| 失败类型 | 回写位置 |
| --- | --- |
| 主线缺失 | `SKILL.md` 主线流程 |
| 输入变体未覆盖 | 分支规则 |
| 工具不会用或命令不稳 | 工具节点、脚本说明、错误处理 |
| 特殊情况可补救但不常见 | 补丁区 |
| 输出不稳定 | 输出模板和 QA |
| Agent 偏离目标 | 回主线检查 |
| 新对话没有触发 skill | frontmatter `description` |
| 主对话已说但文件没有 | 直接写回 `SKILL.md` 或 reference/script |

修完后重新走“落盘验证 -> 干净子 Agent 回归测试”。

## 不同工具中的实现映射

| 抽象能力 | Codex 实现例子 | SealSeek/OpenClaw 实现例子 | 其他 Agent 工具实现例子 |
| --- | --- | --- | --- |
| 后台干净验证者 | `spawn_agent` + `fork_context:false` | 新建不继承当前上下文的子任务/子 Agent | subagent、worker、job、runner |
| 可见干净会话 | `create_thread` | 新建空白会话或独立 workspace 任务 | new chat、new session、isolated run |
| 带上下文分支 | `fork_thread` | 从当前任务分支继续探索 | fork、branch、duplicate session |
| 结果读取与回写 | 主 Agent 读取子 Agent 结果并 patch 文件 | 主控 Agent 汇总子任务输出并改 skill | orchestrator 汇总测试日志并回写 |

严格验证优先选择“后台干净验证者”或“可见干净会话”。带上下文分支适合设计探索，不适合作为最终独立性证明。

## 测试通过标准

一个复杂 skill 至少要同时满足：

1. 主对话能完成设计或修改。
2. 文件确实落盘，`rg` 或 `git diff` 能看到变化。
3. 干净子 Agent 能读取 skill 并按主线执行。
4. 子 Agent 的成功不是来自泄露上下文或主 Agent 提供答案。
5. 暴露的问题已经写回 skill。
6. 写回后再次通过干净上下文测试。

## 推荐工具化实现

每个 Agent 平台都可以实现一个专门的 skill 验证器。它的职责不是代替目标 skill 完成业务任务，而是组织这套验证闭环：

```text
检查目标 skill -> 验证落盘 -> 创建干净子 Agent -> 判断结果 -> 回写目标 skill -> 再测试
```

在 Codex 中，这个实现是 `skill-forward-test`。在 SealSeek/OpenClaw 或其他 Agent 工具中，可以创建同名或同职责的验证 skill，只要保留同一条主线：主控 Agent 设计和落盘，干净验证者独立测试，失败必须回写 skill 文件。

## 与 Skill 世界观的关系

这套方法是 [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]] 中“Skill 测试：防止上下文污染和假修改”的工程化实现。

Skill 世界观定义了原则：skill 必须能脱离设计对话稳定复现。主对话 + 干净子 Agent 方法定义了执行机制：用一个不继承背景的 Agent 逼 skill 文件独立接受验证。

## 相关页面

- [[domains/AI Agent工程/03-Skill设计/index|Skill 设计]]
- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
- [[domains/AI Agent工程/06-自动化工作流/01-Loop Engineering个人方法论|Loop Engineering 个人方法论]]
- [[domains/AI Agent工程/06-自动化工作流/02-Loop项目规划模板|Loop 项目规划模板]]
