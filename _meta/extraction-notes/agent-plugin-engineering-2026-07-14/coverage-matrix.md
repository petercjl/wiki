# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| KU01 | S1/S2/S5 | Plugin 定义 | 核心定义 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md | formalized | 产品化能力包 |
| KU02 | S3 | Skill 与渐进披露 | 组件定义 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md | formalized | 链接 Skill 世界观 |
| KU03 | S6/S10 | CLI 执行面 | 组件定义 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | CLI 不是 Plugin |
| KU04 | S4 | MCP 架构 | 连接协议 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 包含适用边界 |
| KU05 | S1/S6/S7/S8 | Connector/App | 托管连接 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 与 MCP、CLI 区分 |
| KU06 | S1/S5 | Hook | 生命周期治理 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 机械触发才使用 |
| KU07 | S1/S2 | Manifest | 打包规则 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 三项职责和目录 |
| KU08 | S1/S5 | Marketplace | 分发规则 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 版本和缓存 |
| KU09 | S6 | GitHub 样本 | 模式 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md | formalized | Connector-first + CLI fallback |
| KU10 | S7 | Figma 样本 | 模式 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md | formalized | 共享工具面、多工作流 |
| KU11 | S8 | Sites 样本 | 模式 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md | formalized | 本地 MCP、脚本、Connector |
| KU12 | S9 | Computer Use 样本 | 模式 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md | formalized | 原生 Runtime |
| KU13 | S1-S10 | 五面模型 | 架构推导 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md | formalized | 核心综合结论 |
| KU14 | S1/S3/S5/S10 | 成熟度阶梯 | 演进模型 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 避免过早插件化 |
| KU15 | S4/S6-S10 | 连接面选择 | 决策方法 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 决策表 |
| KU16 | S6/S10 | CLI-first 可保留 | 改造原则 | domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | tbcli 不必重写 |
| KU17 | S1/S8/S9/S10 | CLI 三种交付策略 | 改造分支 | domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 随包、依赖、适配 |
| KU18 | S1/S5 | Plugin readiness | 决策检查 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md; queries/Agent插件设计与CLI改造.md | formalized | 插件化门槛 |
| KU19 | S1/S4/S5 | 安全治理 | 风险 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 最小权限和来源审查 |
| KU20 | S1/S3/S5 | 测试体系 | QA | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 契约、干净会话、安装、升级 |
| KU21 | S10 | tbcli 映射 | 实践 | domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 只形成路线，不实施 |
| KU22 | S1/S5 | 跨平台差异 | 边界 | domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论.md; domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md | formalized | 核心可移植，Manifest 分平台 |
