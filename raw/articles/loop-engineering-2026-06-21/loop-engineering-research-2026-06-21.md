---
title: Loop Engineering 资料收集与个人方法论草稿
created: 2026-06-21
updated: 2026-06-21
type: raw-research-notes
source: /Users/pechen/AI/Research/loop-engineering-research-2026-06-21.md
---

# Loop Engineering 资料收集与个人方法论草稿

本 raw 文件保存本次 loop engineering 资料收集的原始整理稿。正式知识已编译到 `domains/AI Agent工程/06-自动化工作流/`。

## 来源清单

| 来源 | URL | 日期 | 采集要点 |
| --- | --- | --- | --- |
| Addy Osmani, Loop Engineering | https://addyosmani.com/blog/loop-engineering/ | 2026-06 | Loop 是系统替代人提示 agent；五个构件包括 automation、worktrees、skills、plugins/connectors、sub-agents；仍需人负责验证和理解。 |
| Business Insider, Forget prompt engineering | https://www.businessinsider.com/what-are-loops-ai-engineering-tips-2026-6 | 2026-06-20 | 汇总 Boris Cherny、Peter Steinberger、Claire Vo、Addy Osmani 对 loop engineering 的近期公开讨论。 |
| Anthropic, Building effective agents | https://www.anthropic.com/engineering/building-effective-agents | 2024/2025 | evaluator-optimizer、orchestrator-workers、agent loop、ground truth、最大迭代停止条件。 |
| OpenAI Developers, Using Goals in Codex | https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex | 2026-05-09 | Goal 是 scoped, user-controlled completion contract，要求 outcome、verification surface、constraints、boundaries、iteration policy、blocked stop condition。 |
| OpenAI Codex use case, Protein folding architectures | https://developers.openai.com/codex/use-cases/discover-protein-folding-architectures | 2026 | Goal Mode 可用于长时实验循环，强调 PLAN、EXPERIMENTS、EXPERIMENT_NOTES 和证据边界。 |
| Addy Osmani, Agent Harness Engineering | https://addyosmani.com/blog/agent-harness-engineering/ | 2026-04-19 | Agent = Model + Harness；harness 包括 prompts、tools、context policies、hooks、sandboxes、subagents、feedback loops、observability。 |
| Arize, Closing the Loop | https://arize.com/blog/closing-the-loop-coding-agents-telemetry-and-the-path-to-self-improving-software/ | 2026 | 可靠的自我改进循环需要 traces、telemetry、evals，否则没有 ground truth。 |
| Augment Code, AI Agent Loop Token Costs | https://www.augmentcode.com/guides/ai-agent-loop-token-cost-context-constraints | 2026-04, updated 2026-06-18 | 朴素 loop 因上下文累积导致成本接近 O(N^2)，需要 scope limiting、state resets、coordinator-specialist。 |
| Lenny's Newsletter / Claire Vo, How to design AI agent loops | https://www.lennysnewsletter.com/p/how-to-design-ai-agent-loops-schedules | 2026-06-17 | 常见 loop 类型包括 heartbeat、cron、hook、goal；有效 loop 需要 worktrees、skills、plugins/connectors、subagents、state tracking。 |

## 原始综合笔记

Loop engineering 是把“人不断提示 agent 继续工作”的手动过程，改造成“系统按目标、证据、工具、评审和停止条件自动推动 agent”的工程方法。它不是简单的 prompt 技巧，也不是完全无人值守的自动化，而是介于人类管理和 agent 执行之间的工作系统设计。

Peter 当前已经在使用这类模式：CLI 工具开发中，Codex 负责实现，另一个视角负责审核，再回流修改；DMP 竞品分析中，先挖工具和数据，再生成报告，再以运营视角评审并回到数据采集；聚宽策略优化中，先回测基线，再改策略，再回测，再根据量化知识库评估是否真的改善。

这三个场景共同拥有同一个结构：

```text
目标契约 -> 执行节点 -> 证据节点 -> 评审节点 -> 修改节点 -> 停止或继续 -> 总结和沉淀
```

Loop 的质量不取决于“跑了多少轮”，而取决于每轮是否有清晰证据、是否有真实评审、是否避免上下文和成本失控、是否把高频经验沉淀回 skill 和 wiki。

