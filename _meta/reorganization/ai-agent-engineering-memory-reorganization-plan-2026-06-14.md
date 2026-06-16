---
title: AI Agent 工程知识域记忆优先改造计划
type: decision
created: 2026-06-14
updated: 2026-06-14
domain: AI Agent工程
tags: [ai-agent-engineering, llm-wiki, reorganization, skill, memory-first]
status: approved
---

# AI Agent 工程知识域记忆优先改造计划

## 改造判断

本次目标是 `domains/AI Agent工程/`。

机械扫描结果：

```text
Scanned: 21 markdown pages
SHELL: 0   THIN: 0   OK: 21
```

因此本域不是大面积 shell/thin 或课程反浓缩问题，而是导航与长期检索问题：

- 目录和文件路径以英文为主，不符合 Peter 后续在 Obsidian 中中文浏览的习惯。
- 正式知识页缺少数字前缀，难以表达阅读顺序。
- `skill-design/` 下混有方法论、生成型注册表和具体 skill 写作知识库。
- Skill 注册表页面由 `ai-agent-skill-registry-sync` 生成，不能只移动页面而不更新生成脚本。
- 部分短 wikilink 依赖当前目录解析，机械 Agent 路由不够稳。

## 可用 Skill

- `llm-wiki-recompile-runner`：主导已有知识域改造、迁移融合表、中文序号化、QA。
- `llm-wiki-audit-and-optimization`：运行 shell/thin 扫描和链接路由审计。
- `llm-wiki-ingest`：仅在发现某页需要回到 raw/source 重新补编时使用。
- `ai-agent-skill-registry-sync`：负责跨 Agent skill 注册表生成；注册表迁移必须同步更新该 skill。
- `openai-docs`：仅在复核 OpenAI API 页面时使用官方文档。

## 目标结构

```text
domains/AI Agent工程/
├── 01-知识系统/
├── 02-Agent架构/
├── 03-Skill设计/
├── 04-提示词与上下文/
├── 05-工具链/
├── 06-自动化工作流/
├── 07-评测与调试/
├── 90-Skill注册表/
└── domains/视觉制作/05-小红书风格AI生图/index.md
```

空主题目录可以保留为未来承载位置，但不强行创建空内容页。

## 迁移融合表

| 旧页面 | 当前角色 | 新位置 | 处理方式 | 备注 |
| --- | --- | --- | --- | --- |
| `knowledge-systems/domains/视觉制作/05-小红书风格AI生图/index.md` | 知识系统入口 | `01-知识系统/domains/视觉制作/05-小红书风格AI生图/index.md` | 移动并中文序号化 | 正式导航页 |
| `knowledge-systems/llm-wiki-personal-knowledge-base-operating-loop.md` | LLM Wiki 运行方法 | `01-知识系统/01-LLM Wiki个人知识库运行闭环.md` | 移动并更新链接 | 保持正文深度 |
| `skill-design/llm-wiki-skill-source-package.md` | LLM Wiki skill 发布方法 | `03-Skill设计/01-LLM Wiki Skill同源包.md` | 移动并更新链接 | 与 skill 源仓库关联 |
| `skill-design/infinite-canvas-skill-writing/` | 无限画板 skill 写作知识库 | `03-Skill设计/02-无限画板Skill写作知识库/` | 整目录迁移、内部页面序号化 | 保持来源和正文 |
| `toolchain/openai-image-generation-api.md` | OpenAI 图像 API 工具链 | `05-工具链/01-OpenAI图像生成API集成指南.md` | 移动并更新链接 | 未来执行前需官方文档复核 |
| `skill-design/personal-ai-agent-skill-registry.md` | 个人/项目 skill 生成注册表 | `90-Skill注册表/01-个人与项目Skill注册库.md` | 移动并更新生成脚本 | 日常优先入口 |
| `skill-design/ai-agent-skill-registry.md` | 全量跨 Agent 生成注册表 | `90-Skill注册表/02-跨Agent Skill注册库.md` | 移动并更新生成脚本 | 全量检索入口 |
| `skill-design/codex-skill-inventory.md` | Codex 生成注册页 | `90-Skill注册表/03-Codex Skill注册页.md` | 移动并更新生成脚本 | 生成资产 |
| `skill-design/hermes-skill-registry.md` | Hermes 生成注册页 | `90-Skill注册表/04-Hermes Skill注册页.md` | 移动并更新生成脚本 | 生成资产 |
| `skill-design/lark-agent-skill-registry.md` | Lark Agent 生成注册页 | `90-Skill注册表/05-Lark Agent Skill注册页.md` | 移动并更新生成脚本 | 生成资产 |
| `skill-design/openclaw-skill-registry.md` | OpenClaw 生成注册页 | `90-Skill注册表/06-OpenClaw Skill注册页.md` | 移动并更新生成脚本 | 生成资产 |
| `skill-design/sealseek-skill-registry.md` | SealSeek 生成注册页 | `90-Skill注册表/07-SealSeek Skill注册页.md` | 移动并更新生成脚本 | 生成资产 |
| `skill-design/claude-code-skill-registry.md` | Claude Code 生成注册页 | `90-Skill注册表/08-Claude Code Skill注册页.md` | 移动并更新生成脚本 | 生成资产 |

## 关联式融合原则

本次不把 `OpenAI 图像 API`、`无限画板 Skill 写作`、`Skill 注册表` 强行合并为一个大页。它们分别代表工具链、skill 写作方法、生成型资产索引，保留独立上下文更符合人的记忆结构。

需要融合的是导航和关联：

- `03-Skill设计/` 作为 skill 方法论入口。
- `90-Skill注册表/` 作为生成型资产入口。
- `05-工具链/` 保持 API/toolchain 页面。
- domain domains/视觉制作/05-小红书风格AI生图/index 负责说明这些模块之间的关系。

## QA 要求

改造完成后必须验证：

- `placeholder_scan.py` 仍为 `SHELL: 0`, `THIN: 0`。
- 旧英文路径残留已消除或仅保留在迁移计划/log 中。
- wikilink 和 markdown link 无缺失目标。
- `ai-agent-skill-registry-sync` dry-run 不再写回旧 `skill-design/*registry*` 路径。
- 根 `domains/视觉制作/05-小红书风格AI生图/index.md`、domain `domains/视觉制作/05-小红书风格AI生图/index.md`、`log.md` 已更新。
