# Agent Operating Protocol

This repository is Peter's general personal LLM Wiki.

Quant trading has been split into a separate private Obsidian/Git wiki at `/Users/pechen/quant-trading-wiki`.

## Mandatory Orientation

Before any edit, every agent must read:

1. `AGENTS.md`
2. `SCHEMA.md`
3. The relevant domain `index.md`
4. Recent entries in `log.md`

Then search existing pages before creating a new page.

## Core Rules

- This is a Markdown knowledge codebase, not a chat log.
- Raw sources under `raw/` are immutable. Do not edit them.
- Temporary notes go to `inbox/` first.
- Formal pages must include YAML frontmatter.
- Every formal page must be listed in the nearest relevant domain or directory `index.md`.
- Every meaningful edit must append `log.md`.
- Use Obsidian-style wikilinks for internal references.
- Do not create duplicate pages.
- Prefer concise Chinese unless code/API context requires English.

## One Vault, Multiple Domains

Use:

- `domains/电商运营/` for 电商运营。
- `domains/财税与经营财务/` for 财税、经营财务、业财一体、股权激励和战略财务。
- `domains/视觉制作/` for 视觉制作。
- `domains/品牌策略/` for 品牌策略。
- `domains/AI Agent工程/` for AI Agent 工程、知识系统、Skill、工具链与自动化工作流。
- `shared/` for cross-domain knowledge.
- `projects/` for project-specific context.

Do not add new quant-trading knowledge here. For 量化交易、聚宽/JoinQuant、QMT、回测、策略、因子、Alpha、仓位、风控、市场状态等内容, use `/Users/pechen/quant-trading-wiki`.
