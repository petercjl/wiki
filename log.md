# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-05-22] create | Wiki initialized
- Path: `/Users/pechen/wiki`
- Architecture: one vault, multiple domains, shared layer, projects layer.
- Created core files: README.md, SCHEMA.md, AGENTS.md, CLAUDE.md, HERMES.md, OPENCLAW.md, SEALSEEK.md, index.md, log.md.

## [2026-05-22] ingest | Karpathy LLM Wiki gist
- Source: `raw/articles/karpathy-llm-wiki-2026-05-22.md`
- Created: `shared/knowledge-management/llm-wiki.md`
- Updated: `index.md`
- Notes: First formal knowledge page. Used to test the LLM Wiki workflow.

## [2026-05-22] ingest | 营销学理论在电商图片中的应用
- Source: `raw/articles/marketing-theory-for-ecommerce-images-2026-05-22.md`
- Created: `shared/business-frameworks/marketing-theory-for-ecommerce-images.md`
- Updated: `shared/business-frameworks/index.md`
- Updated: `domains/ecommerce-ops/index.md`
- Updated: `domains/visual-production/index.md`
- Updated: `domains/brand-strategy/index.md`
- Updated: `index.md`
- Notes: 首篇业务方法论 ingest 测试。作为电商运营、视觉制作、品牌策划共享的图片营销理论总纲页。

## [2026-05-22] ingest | 18期品牌战略课程转写知识萃取
- Source: `raw/transcripts/brand-strategy-methodology-course-opening-2026-05-22.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening-extraction-2026-05-22.md`
- Created: `domains/brand-strategy/concepts/brand-building-methodology.md`
- Created: `domains/brand-strategy/concepts/brand-three-capabilities-model.md`
- Created: `domains/brand-strategy/concepts/ecommerce-brand-case-analysis-framework.md`
- Updated: `domains/brand-strategy/index.md`
- Updated: `index.md`
- Notes: 使用 course-transcript-to-knowledge skill，从课程录音转写中去课程化提炼品牌战略理论、三能力模型和案例拆解框架。

## [2026-05-22] rewrite | 品牌战略课程知识复现重做
- Source: `raw/transcripts/brand-strategy-methodology-course-opening-2026-05-22.md`
- Removed: previous over-compressed brand strategy extraction pages.
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening-reconstruction-2026-05-22.md`
- Created: `domains/brand-strategy/concepts/brand-strategy-knowledge-system.md`
- Created: `domains/brand-strategy/concepts/brand-energy-accumulation-framework.md`
- Created: `domains/brand-strategy/concepts/brand-case-reconstruction-patterns.md`
- Created: `domains/brand-strategy/concepts/brand-strategy-application-templates.md`
- Updated: `domains/brand-strategy/index.md`
- Updated: `index.md`
- Notes: 根据 Peter 反馈，正式知识页应做课堂知识理论复现、分析、归纳和扩充，而不是摘要式提炼。

## [2026-05-22] rewrite | 品牌战略课程分段知识复现
- Source: `raw/transcripts/brand-strategy-methodology-course-opening-2026-05-22.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/segment-plan.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/coverage-matrix.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/segments/segment-*.md`
- Created formal pages: 9 brand-strategy knowledge reconstruction pages.
- Updated: `domains/brand-strategy/index.md`
- Updated: `index.md`
- Notes: 按新版 course-transcript-to-knowledge skill 重跑，采用分段复现、覆盖矩阵和总融合机制；正式页已去除来源语气。

## [2026-05-22] update | 品牌战略课程 micro-segment 重跑
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/micro-segment-plan.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/micro-coverage-matrix.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/micro-segments/MS-*.md`
- Updated: selected formal brand strategy pages with micro-segment coverage notes and richer case/action chains.
- Notes: Skill test iteration. Added knowledge-point-level processing to avoid segment-level tiger-head-snake-tail loss.
