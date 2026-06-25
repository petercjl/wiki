---
title: Skill 设计
type: concept
created: 2026-06-22
updated: 2026-06-22
domain: AI Agent工程
tags: [skill, ai-agent, context-engineering, workflow]
sources:
  - user-stated-principles-2026-06-22
status: active
---

# Skill 设计

本目录沉淀 Agent skill 的设计、测试、演化和注册方法。这里的 skill 不是一次性 prompt，而是能指导大模型围绕主线完成复杂任务、处理异常、调用工具并持续进化的执行知识体。

## 核心页面

- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]：定义 skill 的本质、主线、补丁、QA、回主线机制和测试标准。
- [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|主对话与干净子 Agent 的 Skill 回归测试方法]]：用主 agent 设计/修 skill，用干净子 agent 验证落盘和独立执行能力。
- [[domains/AI Agent工程/03-Skill设计/01-LLM Wiki Skill同源包|LLM Wiki Skill 同源包]]：维护 LLM Wiki 相关 skill 的同源发布、迁移和注册规则。
- [[domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/index|无限画板 Skill 写作知识库]]：无限画板 skill 的写作规则、任务范式、工具规范、反坑库和 QA。

## 使用入口

以后创建或优化复杂 skill 时，Agent 应先读取：

1. [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
2. [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|主对话与干净子 Agent 的 Skill 回归测试方法]]
3. 与目标平台或任务类型相关的具体知识库页面

若用户要求验证 skill 是否真正落盘并能脱离主对话运行，Codex 中使用 `skill-forward-test`；SealSeek/OpenClaw 或其他 Agent 工具中使用等价的干净会话/子 Agent 验证 skill。
