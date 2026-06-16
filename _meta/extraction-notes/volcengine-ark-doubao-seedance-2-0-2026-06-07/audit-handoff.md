# Audit Handoff

- Source slug: `volcengine-ark-domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡-2026-06-07`
- Adapter used: `llm-wiki-ingest/adapters/web-clipping.md`; API-doc modeling applied only to endpoint/model-ID facts.
- Raw source: `raw/webpages/volcengine/volcengine-ark-domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡-2026-06-07.md`
- Formal page: `domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡.md`
- Source inventory: `_meta/extraction-notes/volcengine-ark-domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡-2026-06-07/source-inventory.md`
- Coverage matrix: `_meta/extraction-notes/volcengine-ark-domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡-2026-06-07/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/volcengine-ark-domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡-2026-06-07/omission-audit.md`

## Audit Questions

- Does the formal page preserve every factual source value: model ID, endpoint, pricing, resolutions, frame rate, modalities, tasks, and model variants?
- Are the three demo prompts recoverable and reusable without reopening raw?
- Are the `raw-only` and `unresolved` dispositions reasonable?
- Is the page useful for future AI video planning agents, or should it be split into a separate API reference after full API docs are ingested?

## Known Unresolved Items

- `SD20-NUM-001`: unlabeled `3` and `0.18k`.
- Full Contents Generations schema and SDK examples were not present in this clipping.
- Pricing and availability require live Volcengine Ark recheck before commercial cost decisions.

## Expected Future Agent Use Cases

- Choose whether Seedance 2.0 fits a commercial video workflow.
- Build a Seedance prompt from video/image/audio references.
- Convert a product replacement edit into a structured prompt.
- Plan video extension prompts with continuity, audio, atmosphere, and physical constraints.
- Know when to open the full Volcengine API docs before coding.
