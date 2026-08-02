# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| KU01 | S1/用户问题 | Skill 泄漏本机信息，无法分享 | 问题定义 | domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md | formalized | 转化为隐私与机器独立门 |
| KU02 | S1/用户问题 | Skill 需要跨 Codex、SealSeek、Hermes、OpenClaw | 目标 | domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md | formalized | 转化为可移植核心与适配层 |
| KU03 | S1/决策1 | 不修改或复制系统 creator | 架构决策 | domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md | formalized | 防覆盖与分叉 |
| KU04 | S1/决策2-3 | 用户扩展保存增量并组合当前基础 creator | 主线 | domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md | formalized | 近似继承但不是继承 |
| KU05 | S1/决策4-5 | 全局默认 portable，显式例外才单独使用系统 creator | 路由规则 | domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md; queries/Skill设计与回归测试入口.md | formalized | 区分默认与例外 |
| KU06 | S1/决策6 | 可移植核心加可选平台适配层 | 结构模式 | domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md | formalized | 平台元数据不成为核心依赖 |
| KU07 | S1/决策7 | 格式、隐私扫描、干净上下文测试 | QA | domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md | formalized | 三道质量门 |
| KU08 | S1/关键边界 | Skill 无正式继承，组合仍需冲突检查 | 限制 | domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法.md | formalized | 防止错误承诺自动同步 |
