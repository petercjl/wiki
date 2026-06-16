# Agent Operating Protocol

This repository is Peter's personal LLM Wiki.

## Mandatory Orientation

Before any edit, every agent must read:

1. `AGENTS.md`
2. `SCHEMA.md`
3. `index.md`
4. Recent entries in `log.md`

Then search existing pages before creating a new page.

## Core Rules

- This is a Markdown knowledge codebase, not a chat log.
- Raw sources under `raw/` are immutable. Do not edit them.
- Temporary notes go to `inbox/` first.
- Formal pages must include YAML frontmatter.
- Every formal page must be listed in `index.md`.
- Every meaningful edit must append `log.md`.
- Use `[[wikilinks]]` for internal references.
- Do not create duplicate pages.
- Prefer concise Chinese unless code/API context requires English.

## One Vault, Multiple Domains

Use:

- `domains/ecommerce-ops/` for 电商运营。
- `domains/visual-production/` for 视觉制作。
- `domains/brand-strategy/` for 品牌策划。
- `shared/` for cross-domain knowledge.
- `projects/` for project-specific context.
