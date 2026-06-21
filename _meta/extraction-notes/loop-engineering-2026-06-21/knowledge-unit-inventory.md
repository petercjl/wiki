---
title: Loop Engineering 2026 knowledge unit inventory
type: source-summary
created: 2026-06-21
updated: 2026-06-21
domain: meta
tags: [llm-wiki, knowledge-unit, loop-engineering]
sources:
  - raw/articles/loop-engineering-2026-06-21/loop-engineering-research-2026-06-21.md
status: active
---

# Loop Engineering 2026 Knowledge Unit Inventory

| unit_id | knowledge_unit | role |
| --- | --- | --- |
| KU01 | Loop engineering means designing the system that prompts agents, not manually prompting each step. | definition |
| KU02 | Prompt engineering remains useful but becomes a lower-level component inside loop design. | relation |
| KU03 | A loop should find work, assign work, check work, record work, and decide the next step. | workflow |
| KU04 | Common building blocks: automation, worktrees, skills, plugins/connectors, subagents, state tracking. | architecture |
| KU05 | Evaluator-optimizer separates generation from evaluation and is suitable when criteria are clear and iteration adds measurable value. | pattern |
| KU06 | Agents need environment ground truth such as tool results, code execution, test output, data, traces, screenshots, or backtests. | evidence |
| KU07 | Maximum iterations, budget, blocker, human checkpoint, or success evidence must stop the loop. | control |
| KU08 | Codex Goals are scoped completion contracts, not unbounded background autonomy. | OpenAI-Codex |
| KU09 | Strong goals define outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop condition. | template |
| KU10 | Long-running experimental loops need durable tracking files such as plan, experiment log, and scratchpad. | traceability |
| KU11 | Harness engineering treats prompts, tools, context policies, hooks, sandbox, subagents, feedback loops, and observability as the real artifact. | architecture |
| KU12 | Telemetry, traces, and evals make self-improving loops evidence-based; without them, the loop is guessing. | evaluation |
| KU13 | Naive loops can accumulate context and cost; use scope limiting, state reset, summary files, and coordinator-specialist separation. | cost |
| KU14 | Loop risk includes unattended mistakes, comprehension debt, cognitive surrender, overfitting, data drift, and destructive actions. | risk |
| KU15 | Peter's coding loop maps to plan -> implement -> test -> independent review -> revise -> final report. | case |
| KU16 | Peter's DMP loop maps to tool discovery -> data capture -> report -> operations review -> return to capture. | case |
| KU17 | Peter's quant loop maps to baseline backtest -> diagnosis -> single hypothesis change -> backtest -> anti-overfit review. | case |
| KU18 | Stable loop experiences should be written back into Skill, wiki, tools, and templates. | memory |

