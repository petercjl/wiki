---
title: LLM Wiki Skill 同源包
type: concept
created: 2026-06-12
updated: 2026-06-14
domain: AI Agent工程
tags: [ai-agent, skill, llm-wiki, codex, sealseek, hermes, obsidian]
sources:
  - /Users/pechen/.codex/skills/.llmwiki-source
  - git@github.com:petercjl/LLMWiki.git
status: active
---
# LLM Wiki Skill 同源包

LLM Wiki 相关 skill 采用“Codex 维护、GitHub 分发、其他 Agent 安装使用”的同源模式。

## Source of Truth

- Codex 本地源仓库：`/Users/pechen/.codex/skills/.llmwiki-source`
- GitHub 仓库：`git@github.com:petercjl/LLMWiki.git`
- Codex 可触发安装目录：`/Users/pechen/.codex/skills`

Codex 是唯一维护源。SealSeek、Hermes 等其他 Agent 不直接改这些 skill；需要更新时，从 GitHub 拉取并重新安装。

## Published Skills

当前发布 5 个入口：

- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|llm-wiki]]：总入口，负责 orientation、query-pack、轻量查询和健康检查。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|llm-wiki-ingest]]：唯一入库入口，承接网页、剪藏、API、书籍、课程转写、PPT、XMind、表格、Markdown 等来源。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|llm-wiki-audit-and-optimization]]：编译、路由、推理质量审阅，包含 Obsidian Route Audit。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|llm-wiki-recompile-runner]]：修复 shell/thin pages 和重编译 learning path。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|ai-agent-skill-registry-sync]]：同步跨 Agent skill 注册页。

## Removed Standalone Entries

以下旧入口不再作为独立 skill 维护：

- `api-docs-wiki-ingest`
- `wiki-clippings-ingest`
- `book-to-llm-wiki`
- `course-transcript-to-knowledge`

它们的能力已经合并到 `llm-wiki-ingest` 的 adapters：

- API docs → `adapters/api-docs.md`
- Obsidian Clippings / webpages → `adapters/web-clipping.md`
- books / EPUB / PDF → `adapters/book.md`
- course/audio transcripts → `adapters/transcript.md`

如果其他 Agent 环境中仍有这些旧入口，应删除后从 GitHub 安装同源包，避免 metadata 触发旧流程。

## Obsidian CLI Layer

同源包引入 Obsidian CLI 作为机械路由和健康检查层：

- 入库前：搜索已有页面，避免重复创建。
- 入库后：检查 unresolved links、backlinks、outgoing links、outline、orphan/deadend signals。
- 使用时：构造 query-pack，按 `queries/`、Agent 使用模板、domains/视觉制作/05-小红书风格AI生图/index、细页的顺序路由。

CLI 只是增强层，不替代 raw preservation、coverage matrix、formal compilation、omission audit 或 deterministic filesystem scripts。

## Agent Usage Rule

当 Agent 需要构建或查询 LLM Wiki：

1. 优先使用这 5 个发布入口。
2. 不要调用 removed standalone entries。
3. 不要让业务 Agent 直接读某个目录后回答；先构造 query-pack。
4. 如果 Obsidian CLI 当前 active vault 不是 `/Users/pechen/wiki`，降级为文件系统检索并说明 route audit 是部分验证。
