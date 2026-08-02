---
title: AI Agent 评测与调试
type: concept
created: 2026-07-13
updated: 2026-07-13
domain: AI Agent工程
tags: [ai-agent, ai-agent-engineering, research, playbook]
sources: []
status: active
---

# AI Agent 评测与调试

本目录沉淀 AI Agent 的结果评测、执行链路审计、故障定位和回归验证方法。重点不是只看最终回答，而是把 Agent 的工具调用、命令结果、文件副作用、降级路径和验证过程纳入质量判断。

## 核心页面

- [[domains/AI Agent工程/07-评测与调试/01-AI Agent执行链路审计方法|AI Agent 执行链路审计方法]]：用“结果验收 + 过程验收”发现绕路、静默降级、契约绕过和假成功。
- [[domains/AI Agent工程/07-评测与调试/02-Agent执行链路审计报告模板|Agent 执行链路审计报告模板]]：统一记录预期主线、实际轨迹、发现、输出物验证、最终分类和回归要求。

## 相关记忆

- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
- [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|主对话与干净子 Agent 的 Skill 回归测试方法]]
- [[domains/AI Agent工程/06-自动化工作流/01-Loop Engineering个人方法论|Loop Engineering 个人方法论]]
