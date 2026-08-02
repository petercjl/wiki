# Portable Skill Creator 方法论原始决策

日期：2026-07-15
来源：用户与 Codex 的设计讨论

## 用户问题

- 创建的 Skill 经常带入本机信息，导致无法对外分享。
- 希望 Skill 不与单一 Agent 绑定，可以用于 Codex、SealSeek、Hermes、OpenClaw 等环境。
- 需要判断约束应写入全局 `AGENTS.md`，还是修改系统 `skill-creator`。

## 形成的决策

1. 不直接复制或修改系统内置 `skill-creator`，避免系统升级覆盖修改或副本长期分叉。
2. 新建用户拥有的 `portable-skill-creator`，只保存隐私、可分享性、机器无关性和跨 Agent 兼容的增量规则。
3. `portable-skill-creator` 以组合方式使用当前系统 `skill-creator`：基础 Skill 负责通用创建流程，扩展 Skill 负责可移植性覆盖和额外 QA。
4. 在全局 `AGENTS.md` 中把 `portable-skill-creator` 设为创建、更新、审查和测试 Skill 的默认入口。
5. 只有用户明确要求单独使用系统内置 `skill-creator` 时，才跳过 `portable-skill-creator`。
6. 通用 Skill 采用“可移植核心 + 可选平台适配层”结构；平台专属元数据不得成为核心工作流的运行前提。
7. 创建完成后必须执行格式校验、隐私与机器依赖扫描，以及干净上下文前向测试。

## 关键边界

- Skill 系统没有正式的继承或自动合并机制。
- “组合式扩展”能在每次运行时继续使用当前系统 `skill-creator`，从而获得它的新流程，但仍需检查新版本是否与扩展规则冲突。
- 跨 Agent 可移植性不等于所有平台文件完全相同；目标是核心工作流中立，平台接入差异隔离。
