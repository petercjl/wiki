# Portable Skill Creator 方法论覆盖清单

本文件同时承担小型来源的 source inventory、knowledge-unit inventory、coverage matrix、omission audit 和 formal page plan。

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| KU01 | 用户问题 | Skill 泄漏本机信息，无法分享 | 问题定义 | 04-可分享跨Agent Skill创建方法 | formalized | 转化为隐私与机器独立门 |
| KU02 | 用户问题 | Skill 需要跨 Codex、SealSeek、Hermes、OpenClaw | 目标 | 04-可分享跨Agent Skill创建方法 | formalized | 转化为可移植核心与适配层 |
| KU03 | 形成的决策 1 | 不修改或复制系统 creator | 架构决策 | 04-可分享跨Agent Skill创建方法 | formalized | 防覆盖与分叉 |
| KU04 | 形成的决策 2-3 | 用户扩展只保存增量规则，并组合当前基础 creator | 主线 | 04-可分享跨Agent Skill创建方法 | formalized | 近似继承但不是继承 |
| KU05 | 形成的决策 4-5 | 全局规则默认 portable，显式例外才单独使用系统 creator | 路由规则 | 04-可分享跨Agent Skill创建方法；Skill设计与回归测试入口 | formalized | 区分默认与例外 |
| KU06 | 形成的决策 6 | 可移植核心加可选平台适配层 | 结构模式 | 04-可分享跨Agent Skill创建方法 | formalized | 平台元数据不得成为核心依赖 |
| KU07 | 形成的决策 7 | 格式、隐私扫描、干净上下文测试 | QA | 04-可分享跨Agent Skill创建方法 | formalized | 三道质量门 |
| KU08 | 关键边界 | Skill 无正式继承，组合仍需冲突检查 | 限制 | 04-可分享跨Agent Skill创建方法 | formalized | 防止错误承诺自动同步 |

## Omission audit

- raw-only: 0
- omitted-with-reason: 0
- unresolved: 0

## Formal page plan

- Create: `domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md`
- Extend: `domains/AI Agent工程/03-Skill设计/index.md`
- Extend: `queries/Skill设计与回归测试入口.md`
- Update routing: AI Agent domain index and root index.
