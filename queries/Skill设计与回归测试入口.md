---
title: Skill设计与回归测试入口
type: query
created: 2026-07-02
updated: 2026-07-02
domain: AI Agent工程
tags: [skill, ai-agent, context-engineering, workflow]
sources:
  - domains/AI Agent工程/03-Skill设计/index.md
status: active
---

# Skill设计与回归测试入口

当用户要求创建、优化、审查、迁移、注册或回归测试 Agent skill 时，先读这个入口，而不是只凭当前对话写一个 prompt。

## 先读哪些页面

1. [[domains/AI Agent工程/03-Skill设计/index|Skill 设计]]
2. [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
3. [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|主对话与干净子 Agent 的 Skill 回归测试方法]]
4. [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]
5. [[domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库|跨 Agent Skill 注册库]]

## 分支读取

- 如果是 LLM Wiki 相关 skill，读 [[domains/AI Agent工程/03-Skill设计/01-LLM Wiki Skill同源包|LLM Wiki Skill 同源包]]。
- 如果是无限画板 skill，读 [[domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/index|无限画板 Skill 写作知识库]]。
- 如果用户要判断某个平台是否已有可复用 skill，按注册库页面继续读取对应平台注册页。

## 工作边界

- 不要把 skill 当作一次性提示词；它必须有主线、工具使用、分支、错误处理、QA 和演化规则。
- 不要把一次成功运行当作 skill 有效；复杂 skill 必须用干净上下文验证。
- 修改 skill 后，必须确认文件已写入磁盘，并用 diff 或文件读取检查。

## 标准输出

```text
1. 当前任务是否需要 skill
2. 现有可复用 skill 或空缺
3. Skill 主线与关键节点
4. 工具/脚本/API 节点
5. 分支、补丁和回主线规则
6. QA 与干净上下文测试方案
7. 文件落盘和注册表更新事项
```
