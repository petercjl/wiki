# Brand Strategy LLM Wiki Package

This package contains Peter's `brand-strategy` LLM Wiki domain, plus the minimum related files needed for another Codex instance to install it into an Obsidian vault that follows the same LLM Wiki structure.

## Package Layout

```text
brand-strategy-llm-wiki-package-2026-06-13/
├── README_FOR_CODEX_INSTALL.md
├── MANIFEST.md
├── FILE_LIST.txt
└── wiki/
    ├── AGENTS.md
    ├── SCHEMA.md
    ├── README.md
    ├── domains/brand-strategy/
    ├── raw/transcripts/
    ├── shared/business-frameworks/
    └── queries/ecommerce-image-marketing-planning.md
```

## What To Install

Install the contents of `wiki/` into the target Obsidian vault root.

The important path is:

```text
<target-vault>/domains/brand-strategy/
```

The `raw/transcripts/` files are source materials referenced by the brand-strategy pages. Keep them at the same relative paths so frontmatter `sources:` links continue to work.

The `shared/business-frameworks/` and `queries/` files are included because the brand strategy domain cross-references ecommerce image marketing and brand visual planning workflows.

## Install Into A New LLM Wiki Vault

If the target Obsidian vault is new or does not yet have an LLM Wiki structure:

1. Unzip this package.
2. Copy everything inside `wiki/` into the vault root.
3. Open the vault in Obsidian.
4. Ask Codex to read `AGENTS.md`, `SCHEMA.md`, `index.md` if present, and `domains/brand-strategy/index.md`.
5. Ask Codex to create or update the vault-level `index.md` so it links to `[[domains/brand-strategy/index|品牌策划知识域]]`.
6. Ask Codex to append an install note to `log.md` if the vault uses a change log.

Suggested Codex prompt:

```text
请把这个解压后的 LLM Wiki 包安装到我的 Obsidian vault 中。保留包内 wiki/ 下的相对路径，把 domains/brand-strategy、raw/transcripts、shared/business-frameworks 和 queries 合并到 vault 根目录。不要覆盖我已有的同名文件；如果 AGENTS.md、SCHEMA.md、README.md、index.md 或 log.md 已存在，请先读取并合并必要规则和索引链接。安装后检查 wikilink 和 sources 路径是否可解析。
```

## Install Into An Existing LLM Wiki Vault

If the target vault already has `AGENTS.md`, `SCHEMA.md`, `index.md`, or `log.md`, do not blindly overwrite those files.

Use this merge policy:

- Copy or merge `wiki/domains/brand-strategy/` into `<target-vault>/domains/brand-strategy/`.
- Copy the included `wiki/raw/transcripts/*.md` files into `<target-vault>/raw/transcripts/` unless equivalent source files already exist.
- Copy or merge `wiki/shared/business-frameworks/marketing-theory-for-ecommerce-images.md` and its `index.md` if the target vault does not already have those pages.
- Copy or merge `wiki/queries/ecommerce-image-marketing-planning.md` if the target vault uses query entry pages.
- Use the packaged `wiki/AGENTS.md`, `wiki/SCHEMA.md`, and `wiki/README.md` as references, not authoritative replacements, when the target vault already has its own versions.
- Update the target vault `index.md` with a link to `[[domains/brand-strategy/index|品牌策划知识域]]`.
- Append a dated entry to the target vault `log.md`, for example: `2026-06-13: Installed brand-strategy LLM Wiki package.`

## Verification Checklist For Codex

After installation, run these checks from the target vault root:

```bash
test -f domains/brand-strategy/index.md
find domains/brand-strategy -type f -name '*.md' | wc -l
rg -n "raw/transcripts/" domains/brand-strategy
rg -n "\\[\\[domains/brand-strategy" index.md domains/brand-strategy shared queries 2>/dev/null
find domains/brand-strategy raw/transcripts shared/business-frameworks queries -name '.DS_Store'
```

Expected results:

- `domains/brand-strategy/index.md` exists.
- The brand strategy domain contains 88 markdown files.
- Referenced source transcripts exist under `raw/transcripts/`.
- No `.DS_Store` files are installed.

## How To Use The Knowledge Domain

For brand strategy tasks, Codex should start here:

```text
domains/brand-strategy/index.md
```

That page is the routing table. It tells Codex which learning path to read for questions about:

- brand positioning and ecommerce brand growth
- category focus and mindshare positioning
- niche category brand upgrade
- brand differentiation and perception assets
- visual memory, brand symbols, and AI visual systems
- mindshare product power and hero products
- product matrix planning and second growth curves
- scene marketing and product expansion

When a task asks Codex to produce a brand planning report, Codex should read the matching `*-agent-usage-template.md` page inside the relevant learning path before drafting output.

