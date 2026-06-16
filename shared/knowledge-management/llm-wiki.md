---
title: LLM Wiki 个人知识库
type: concept
created: 2026-05-22
updated: 2026-05-22
domain: shared
tags: [llm-wiki, knowledge-base, ai-agent, obsidian, workflow]
sources:
  - raw/articles/karpathy-llm-wiki-2026-05-22.md
status: active
---

# LLM Wiki 个人知识库

## 摘要

LLM Wiki 是一种由 AI Agent 持续维护的个人知识库模式。它不同于传统 RAG：不是每次提问时重新检索和拼接原始资料，而是让 Agent 在资料进入时就把知识整理、交叉引用并沉淀到 Markdown Wiki 中。

在 Peter 的场景中，LLM Wiki 应作为多个 Agent 共享的长期知识底座，服务于电商运营、视觉制作、品牌策划、AI Agent 研发和具体项目交付。

## 核心观点

- LLM Wiki 是“持久化、可累积”的知识代码库。
- 原始资料保存在 `raw/`，正式知识沉淀在 `domains/`、`shared/`、`projects/` 等目录。
- Agent 负责维护页面、索引、日志和交叉链接。
- Obsidian 是浏览和人工校阅界面。
- Git 是版本控制和回滚机制。
- Peter 当前适合采用“一库多域”架构，而不是多个独立 Vault。

## 和传统 RAG 的区别

传统 RAG 的问题是，每次提问都要临时从原始资料中重新检索、拼接、综合。这个过程不自然积累知识，也不保证上一次的理解会被下一次复用。

LLM Wiki 的做法是：

1. 新资料进入时，Agent 先阅读和理解。
2. Agent 将资料中的知识更新到已有页面。
3. 如果出现新概念、新实体或新方法，Agent 创建新页面。
4. Agent 更新 `domains/视觉制作/index.md` 和 `log.md`。
5. 后续提问先读取 Wiki，再必要时追溯 raw source。

## Peter 的一库多域架构

Peter 的知识不应按工具拆分，也不应过早拆成多个 Vault。

推荐结构是：

- [[domains/电商运营/index|电商运营知识域]]
- [[domains/视觉制作/index|视觉制作知识域]]
- [[domains/品牌策略/index|品牌策划知识域]]
- [[shared/ai-agent-workflows/index|AI Agent 共享工作流]]
- [[projects/sealseek/index|SealSeek 项目知识]]

原因是电商运营、视觉制作和品牌策划虽然大部分内容独立，但底层概念高度交叉，例如人群画像、卖点提炼、平台规则、主图点击率、品牌调性等。

## 核心操作

### Ingest

1. 保存原始资料到 `raw/`。
2. 提取核心观点。
3. 搜索已有页面，避免重复。
4. 创建或更新正式页面。
5. 添加 wikilink。
6. 更新 `domains/视觉制作/index.md`。
7. 追加 `log.md`。

### Query

1. 先读 `domains/视觉制作/index.md`。
2. 搜索相关页面。
3. 阅读相关页面。
4. 综合回答并引用页面。
5. 有复用价值的答案沉淀到 `queries/` 或 `comparisons/`。

### Lint

- 坏链接。
- 孤岛页。
- 重复页。
- 缺少 domains/视觉制作/05-小红书风格AI生图/index 登记。
- 缺少 frontmatter。
- 标签不规范。
- 过期或冲突信息。

## 当前决策

- 使用单一公共 Vault：`~/wiki`。
- 不放在当前项目目录下。
- 使用 `AGENTS.md` 作为多 Agent 通用协议。
- 使用 `SCHEMA.md` 作为结构和写作规则。
- 使用 `domains/视觉制作/index.md` 和 `log.md` 作为导航与操作记录。

## 相关页面

- [[AGENTS]]
- [[SCHEMA]]
- [[shared/ai-agent-workflows/index|AI Agent 共享工作流]]
- [[shared/knowledge-management/index|知识管理索引]]

## 来源

- `raw/articles/karpathy-llm-wiki-2026-05-22.md`
- Andrej Karpathy, “LLM Wiki” Gist

## 待确认问题

- [ ] 是否将 `~/wiki` 固定为所有 Agent 的默认知识库路径。
- [ ] Obsidian 是否直接打开 `~/wiki` 作为 Vault。
- [ ] 是否为 Wiki 建立私有 Git 仓库。
