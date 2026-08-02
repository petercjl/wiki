---
title: Agent 插件工程调研 audit handoff
type: source-summary
created: 2026-07-14
updated: 2026-07-14
domain: meta
tags: [llm-wiki, audit-handoff, plugin, ai-agent]
sources: [raw/webpages/agent-plugin-engineering-2026-07-14/research-notes.md]
status: active
---

# Agent 插件工程调研 Audit Handoff

## Source

- Adapter: unknown-source + markdown-doc interpretation
- Raw path: `raw/webpages/agent-plugin-engineering-2026-07-14/research-notes.md`
- Original URLs/paths: 见 source inventory
- Capture date: 2026-07-14
- Current-doc verification: 新抓取 Codex Manual，并核验本机 `codex plugin --help` 和公开官方资料

## Outputs

- Source profile: `source-profile.md`
- Source inventory: `source-inventory.md`
- Knowledge-unit inventory: `knowledge-unit-inventory.md`
- Coverage matrix: `coverage-matrix.md`
- Omission audit: `omission-audit.md`
- Formal page plan: `formal-page-plan.md`
- Formal pages: 插件工程 index、架构方法论、CLI→Codex Plugin 手册、查询入口
- Current CLI→Plugin manual path: `domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md`
- Taxonomy revision confirmation: 用户于 2026-07-29 同意融合建议，并明确指定新模块目录 `domains/AI Agent工程/10-插件Skill与CLI/`。

## Placement Confirmation

- Source understanding: 现有 CLI 与 Skill 向 Codex Plugin 演进的通用架构、交付、测试和分发方法。
- Existing category considered: `08-插件工程` 适合通用架构理论，但不足以表达 CLI、Skill 与 Plugin 的连续工程生命周期。
- Recommended placement: 架构理论保留在 `08-插件工程`，实操手册移入 `10-插件Skill与CLI`。
- Recommended disposition: move-and-extend，并与上游 CLI 规范建立 Plugin Readiness Gate。
- Alternatives considered: 两篇全文合并；因会混淆执行核心与插件分发责任而未采用。
- User confirmation: confirmed
- Confirmation evidence: 用户于 2026-07-29 回复“你说的修改我同意”，并明确指定目录 `/Users/pechen/wiki/domains/AI Agent工程/10-插件Skill与CLI`。
- Final confirmed path: `domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件.md`

## Coverage Summary

- Source units: 22
- formalized: 22
- merged/raw-only/omitted/unresolved: 0（核心 KU；补充材料处置见 omission audit）

## Expected Agent Use

- 判断 CLI/Skill 是否应该插件化
- 选择 CLI 随包、外部依赖或 MCP 适配
- 设计 Manifest、目录、权限、测试和 Marketplace
- 比较 CLI、MCP、Connector 与 Hook
- First page: `queries/Agent插件设计与CLI改造.md`

## Known Risks

- Time-sensitive: Codex Manifest、Marketplace、公开发布规则
- Sensitive data removed: Connector 实例 ID、认证状态和用户数据
- Weak area: 尚未实际打包 tbcli 并做安装回归
- User confirmation: 改造时再决定 CDP-only、MCP 或托管 Connector

## Self-Validation

- No formal write before placement confirmation: yes；本次分类调整和正文融合均在用户明确确认后执行。
- Ingest contract: passed；22 个 KU 均能在正式页追踪。
- Placeholder scan: 插件工程 3 个 Markdown 页面均为 OK，无机械空壳；Query 页经 `rg` 检查无 TODO/TBD/占位符。
- Representative term search: `Plugin 五面模型`、`Readiness Gate`、`Connector-first`、`MCP Adapter`、`tbcli`、`Marketplace` 均命中正式页。
- Route audit: passed；Query 页有 3 个 backlinks、4 个有效 outgoing wikilinks、无 route warning。
- Obsidian search probe: 查询入口排名第一；共享 search helper 的 vault-status 子命令与当前 Obsidian CLI 版本不兼容，自动使用文件搜索降级，route audit 另行确认 active vault 为 `/Users/pechen/wiki`。
- Index/log check: 新模块 index、插件工程关联入口、domain index、root index、log 均已更新。
- Remaining gaps: 真正打包后的安装、升级、卸载和跨机器回归。
