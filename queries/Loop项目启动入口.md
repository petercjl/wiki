---
title: Loop 项目启动入口
type: query
created: 2026-06-21
updated: 2026-06-21
domain: AI Agent工程
tags: [ai-agent, automation, workflow, loop-engineering, query]
sources:
  - raw/articles/loop-engineering-2026-06-21/loop-engineering-research-2026-06-21.md
  - domains/AI Agent工程/06-自动化工作流/01-Loop Engineering个人方法论.md
  - domains/AI Agent工程/06-自动化工作流/02-Loop项目规划模板.md
status: active
---

# Loop 项目启动入口

## 何时读取

当用户提到以下意图时，Agent 应先读取本页，再开始工作：

- “做一个 loop”
- “循环优化 N 轮”
- “让 Agent 自己写、自己审、自己改”
- “先定义目标，再多轮执行”
- “跑几轮回测/生成/报告/修复，最后给总结”
- “把这个工作做成可复用的自动化闭环”

## 必读页面

1. [[domains/AI Agent工程/06-自动化工作流/01-Loop Engineering个人方法论|Loop Engineering 个人方法论]]
2. [[domains/AI Agent工程/06-自动化工作流/02-Loop项目规划模板|Loop 项目规划模板]]
3. 如果涉及 skill 创建或沉淀，读取 [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]

## 启动规则

Agent 不应直接进入执行。先输出 Loop 项目规划，至少包含：

- Loop 名称
- 业务目标
- 成功证据
- 工作基座
- 执行节点
- 证据节点
- 评审节点
- 回流规则
- 最大轮数或预算
- 停止条件
- 最终报告格式
- 可写回 wiki/skill 的经验

如果用户已经明确给出最大轮数，按用户轮数执行。如果用户未给出轮数，默认先建议 3 轮用于探索，5 轮用于正式优化，10 轮用于高价值深度优化，并说明成本风险。

## 领域线索

下表只是常见案例的补充阅读线索，不是适用范围限制。若用户的新任务不在表内，仍然先使用 Loop Engineering 方法论抽象目标、证据、执行、评审、回流和停止条件，再按任务需要寻找对应知识页。

| 用户任务线索 | 还应读取 |
| --- | --- |
| CLI、小工具、Agent 工具链 | `domains/AI Agent工程/05-工具链/`，相关项目 README 或 AGENTS.md |
| Skill 设计、Skill 优化 | [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]] |
| DMP 竞品分析 | [[domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册|达摩盘 AI 内部工具与竞品数据挖掘手册]] |
| 聚宽量化策略 | [[queries/joinquant-strategy-agent-entry|聚宽策略 Agent 使用入口]] 和 [[domains/量化交易/04-量化理论基础/12-量化研究工作流与实验纪律|量化研究工作流与实验纪律]] |
| 视觉制作、生图生视频 | `domains/视觉制作/` 下对应视觉、AI 生图、AI 视频页面 |
| 报告、课程、文档 | 相关 source package、写作/报告模板、截图或导出 QA 页面 |

## 给 Agent 的启动提示

```text
你正在启动一个 Loop 项目。先不要执行具体业务动作。

请先读取 Loop Engineering 个人方法论和 Loop 项目规划模板，然后根据用户目标输出一份 Loop 项目规划。

规划必须说明：
1. 目标是否可证据化；
2. 每轮由谁执行、谁评审；
3. 证据来自哪里；
4. 最多执行几轮；
5. 什么时候提前停止；
6. 每轮如何记录；
7. 最终如何报告；
8. 哪些经验写回 wiki、skill 或工具。

只有规划清楚后，才进入第一轮。
```
