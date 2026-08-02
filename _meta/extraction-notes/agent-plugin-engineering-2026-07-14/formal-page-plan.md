# Formal Page Plan

| page | disposition | purpose |
| --- | --- | --- |
| `domains/AI Agent工程/08-插件工程/index.md` | create-new | 插件工程入口 |
| `01-Agent插件架构与设计方法论.md` | create-new | 五面模型、组件边界、成熟度和治理 |
| `domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md` | move-and-extend | CLI-first 改造主线、与上游 CLI 规范的交接门和模板 |
| `queries/Agent插件设计与CLI改造.md` | create-new | 未来 Agent 路由入口 |
| `03-Skill设计/00-Skill世界观.md` | preserve-and-link | 不重写，建立相关记忆 |
| `domains/AI Agent工程/index.md` | extend-existing | 增加主题导航 |
| `/index.md` | extend-existing | 增加全库入口 |

Query Entry Gate: required。该知识支持反复出现的架构诊断、插件设计、CLI 改造、连接选择和发布规划，并跨越多个正式页面。

## 2026-07-29 分类调整

- 用户确认把 CLI 开发规范与本手册共同移动到 `domains/AI Agent工程/10-插件Skill与CLI/`，形成独立、可继续扩展的功能模块。
- `08-插件工程/01-Agent插件架构与设计方法论.md` 继续保留通用插件架构理论。
- 本手册改为稳定 CLI 的下游产品化阶段，并以 Plugin Readiness Gate 连接两篇知识。
