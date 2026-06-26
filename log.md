# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-06-14] reorganize | 品牌策略与视觉制作知识域边界改造
- Created: `_meta/reorganization/brand-strategy-domains/视觉制作-boundary-reorganization-plan-2026-06-14.md`
- Renamed: `domains/brand-strategy/` to `domains/品牌策略/`; `domains/视觉制作/` to `domains/视觉制作/`.
- Moved: 品牌策略 pages into ordered Chinese directories for 品牌基础、品类心智、产品战略、品牌视觉资产 and 样本.
- Moved: 视觉制作 pages into ordered Chinese directories for 电商视觉基础、品牌视觉标准化、AI商业视觉、AI生图风格库、小红书风格AI生图 and AI视频.
- Recompiled: `AI 在商业视觉设计中的应用方法与实践` 7 shell pages from raw transcript, preserving cases, numbers, workflows, and Agent-use template.
- Added: `品牌视觉资产与视觉制作边界` bridge page to keep strategy and production knowledge linked but not merged.
- Updated: `AGENTS.md`, `SCHEMA.md`, `domains/视觉制作/05-小红书风格AI生图/index.md`, query/shared pages, internal wikilinks, and LLM Wiki skill placement rules.

## [2026-06-14] reorganize | 电商运营知识域平台优先改造
- Created: `_meta/reorganization/ecommerce-ops-platform-first-reorganization-plan-2026-06-14.md`
- Renamed: `domains/ecommerce-ops/` to `domains/电商运营/`.
- Moved: 通用咨询交付、平台入驻、平台结算、淘宝运营、淘宝营销工具、京东自营、跨境电商、旺店通 API into ordered Chinese platform-first directories.
- Added: major domains/视觉制作/05-小红书风格AI生图/index pages for `01-通用电商方法/`, `02-淘宝天猫/`, `03-京东/`, `04-拼多多/`, `05-抖音/`, `06-小红书/`, `20-跨境电商/`, and `30-ERP与系统工具/`.
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`, `SCHEMA.md`, `AGENTS.md`, query pages, extraction notes, and internal wikilinks to the new Chinese paths.
- Updated: LLM Wiki ingest skill placement rules so future ecommerce ingestion first distinguishes platform-specific knowledge from platform-independent methods and system/API tooling.

## [2026-06-14] reorganize | AI Agent 工程知识域一级目录中文化
- Renamed: top-level domain directory from `domains/ai-agent-engineering/` to `domains/AI Agent工程/`.
- Updated: wiki domains/视觉制作/05-小红书风格AI生图/indexes, schema, AGENTS protocol, extraction notes, formal-page links, and skill registry generated links to the new Chinese domain path.
- Updated: LLM Wiki skills to state explicitly that top-level human-facing domain directories under `domains/` should also be Chinese-readable by default.
- Updated: `ai-agent-skill-registry-sync` source and installed skill so future registry sync writes to `domains/AI Agent工程/90-Skill注册表/`.

## [2026-06-14] compile | 同步跨 Agent Skill 注册库
- Updated: `domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库.md`
- Updated: `domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库.md`
- Updated: agent-specific skill registry pages under `domains/AI Agent工程/90-Skill注册表/`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Updated: `domains/AI Agent工程/index.md`
- Notes: 扫描系统中 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 `SKILL.md`，当前总计 376 个 skill，其中个人/项目自定义 158 个；Codex 18, Hermes 166, Lark Agent 28, OpenClaw 4, SealSeek 134, Claude Code 26。Touched: domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库.md, domains/AI Agent工程/90-Skill注册表/05-Lark Agent Skill注册页.md, domains/AI Agent工程/index.md。

## [2026-06-14] reorganize | AI Agent 工程知识域中文序号化改造
- Created: `_meta/reorganization/ai-agent-engineering-memory-reorganization-plan-2026-06-14.md`
- Renamed: `domains/AI Agent工程/` child folders to ordered Chinese names including `01-知识系统/`, `03-Skill设计/`, `05-工具链/`, and `90-Skill注册表/`.
- Moved: LLM Wiki operating loop, LLM Wiki skill source package, infinite canvas skill writing knowledge base, OpenAI image generation API guide, and all skill registry pages into the new ordered Chinese structure.
- Updated: `ai-agent-skill-registry-sync` source and installed skill so generated registry pages now write to `domains/AI Agent工程/90-Skill注册表/` with numeric Chinese filenames.
- Updated: root visual-production, domain visual-production, extraction notes, and internal links to the new paths.
- Notes: 采用“正式知识页 / 工具链页 / 生成型注册表”分层；注册表由脚本维护，不再混在 Skill 设计方法论目录中。

## [2026-06-14] compile | 同步跨 Agent Skill 注册库
- Updated: `domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库.md`
- Updated: `domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库.md`
- Updated: agent-specific skill registry pages under `domains/AI Agent工程/90-Skill注册表/`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Updated: `domains/AI Agent工程/index.md`
- Notes: 扫描系统中 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 `SKILL.md`，当前总计 373 个 skill，其中个人/项目自定义 158 个；Codex 18, Hermes 166, Lark Agent 25, OpenClaw 4, SealSeek 134, Claude Code 26。Touched: domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库.md, domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库.md, domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页.md, domains/AI Agent工程/90-Skill注册表/04-Hermes Skill注册页.md, domains/AI Agent工程/90-Skill注册表/05-Lark Agent Skill注册页.md, domains/AI Agent工程/90-Skill注册表/06-OpenClaw Skill注册页.md, domains/AI Agent工程/90-Skill注册表/07-SealSeek Skill注册页.md, domains/AI Agent工程/90-Skill注册表/08-Claude Code Skill注册页.md, domains/AI Agent工程/index.md。

## [2026-06-14] plan | 财税股权 28 期知识库迁移融合计划
- Created: `_meta/reorganization/ecommerce-tax-equity-strategic-finance-memory-fusion-plan-2026-06-14.md`
- Notes: 按 Memory-First 原则为 `ecommerce-tax-equity-strategic-finance` 生成迁移融合表；建议新增 `domains/财税与经营财务/` 一级知识域，并将原 learning path 降级为课程包/来源包，等待 用户确认后再执行批量迁移和改链。

## [2026-06-14] reorganize | 财税与经营财务知识域试点迁移
- Created: `domains/财税与经营财务/index.md`
- Created: `domains/财税与经营财务/90-课程包/01-财税股权28期/index.md`
- Moved: `domains/电商运营/learning-paths/ecommerce-tax-equity-strategic-finance/` formal pages into `domains/财税与经营财务/` Chinese content-domain directories.
- Moved: `domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略/11-Agent使用模板：心智产品力与大单品诊断.md` to `queries/电商企业财税股权诊断.md`
- Merged: `20-incentive-mechanism-bonus-pool-and-equity-conditions.md` into `domains/财税与经营财务/03-股权与激励/04-电商团队激励、分红与预算联动.md`
- Updated: `AGENTS.md`, `SCHEMA.md`, `domains/视觉制作/05-小红书风格AI生图/index.md`, `domains/电商运营/index.md`
- Notes: 采用“关联式融合”而非破坏性合并；旧电商运营、淘宝运营、平台入驻知识保留原体系，新财税知识页通过“相关记忆”链接进行印证和追溯。

## [2026-06-14] reorganize | 财税与经营财务知识域序号化命名
- Renamed: `domains/财税与经营财务/` child folders to ordered Chinese names such as `01-电商财税合规/`, `02-经营财务与业财一体/`, `03-股权与激励/`, `04-战略财务/`, `05-内控与组织能力/`, and `90-课程包/`.
- Renamed: formal knowledge pages under each folder to `01-...md`, `02-...md` style names so Obsidian and file browsers show the intended reading order.
- Updated: internal links, domains/视觉制作/05-小红书风格AI生图/indexes, extraction notes, schema references, and query entry links to the new numbered paths.
- Updated: LLM Wiki skills to require Chinese human-facing names plus numeric prefixes when reading order matters.
- QA: no residual old English domain path or unnumbered `domains/财税与经营财务/...` paths found in markdown outside exports; link existence check passed; placeholder scan remains `SHELL: 0`, `THIN: 0`, `OK: 27`.

## [2026-06-14] recompile | 财税股权 28 期课程深度反浓缩重编译
- Trigger: 用户 confirmed that two days of finance course recordings must be compiled by understanding and expanding knowledge units, not by condensing into a few outline pages.
- Updated: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/micro-segment-plan.md`
- Updated: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/coverage-matrix.md`
- Updated: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/formal-page-plan.md`
- Updated: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/omission-audit.md`
- Updated: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/audit-handoff.md`
- Updated: `domains/财税与经营财务/90-课程包/01-财税股权28期/index.md`
- Created: formal topic pages `12-27` under `domains/财税与经营财务/90-课程包/01-财税股权28期/`
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将原 35 个宽泛 KU 扩展为 120+ 个课程知识单元，并新增收入确认/退货补贴、平台利润与边际贡献、资金库存权限内控、进销项发票、企业所得税、主体拆分代销、股东取钱、控股架构、激励条件、商业模式税负承载、预算经营分析、财务 BP、四类业务税务规划、存货现金流 ROE、案例锚点库和合规转型路线图等专题页。课堂组织、招生销售和不可还原 ASR 噪声仅保留 raw 或在 omission audit 中说明。

## [2026-06-13] ingest | 跨境电商赋能中小企业出海
- Source: `raw/books/cross-border-ecommerce-sme-globalization-2026/source.epub`
- Adapter: `llm-wiki-ingest/adapters/book.md`
- Created: `raw/books/cross-border-ecommerce-sme-globalization-2026/` raw EPUB archive with 9 extracted chapter files and 82 image assets.
- Created: `_meta/extraction-notes/cross-border-ecommerce-sme-globalization-2026/` source profile, source inventory, segment plan, knowledge architecture plan, chapter inventory, knowledge-unit inventory, coverage matrix, omission audit, source-to-page map, formal page plan, and audit handoff.
- Created: `domains/电商运营/20-跨境电商/01-中小企业跨境出海/` domains/视觉制作/05-小红书风格AI生图/index and 8 formal pages.
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将洪勇 2026 年《跨境电商：赋能中小企业出海》重构为中小企业跨境出海 learning path，覆盖机会判断、市场调研、产品本地化、数字营销、物流、本地化运营、知识产权、支付、合规和风险管理；平台、支付、物流与合规规则均标注为当前执行前需实时复核。

## [2026-06-13] ingest | 电商企业财税股权与战略财务管理
- Source: `raw/transcripts/ecommerce-tax-equity-course-28-2026-04/` four transcript raw files from 财税股权 28 期.
- Adapter: `llm-wiki-ingest/adapters/transcript.md`
- Created: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/` source profile, inventory, segment plan, micro-segment plan, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/财税与经营财务/90-课程包/01-财税股权28期/` domains/视觉制作/05-小红书风格AI生图/index and 11 formal pages.
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将 4 份录音转写作为一个课程源包重构，不按 D1/D2 时间顺序归档，而按税务合规、四本账、税负模型、多主体架构、业财一体、股权控制、激励治理、股权资源整合和战略财务组织；税率、政策阈值、股权架构、代持和税务整改动作均标注为执行前需专业复核。

## [2026-06-14] recompile | 电商企业财税股权与战略财务管理反浓缩修复
- Trigger: 用户 reviewed the first compile and pointed out that the two-day transcript had been over-compressed into outline-like knowledge.
- Created: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/recompile-standard.md`
- Created: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/recompile-audit-2026-06-14.md`
- Rewritten: all 12 formal pages under `domains/财税与经营财务/90-课程包/01-财税股权28期/` as expanded method-article style pages.
- Added back detailed reasoning chains and anchors: 股东借款/注册资本/违规分红、收入确认/退货/好评返现、刷单/恶意分拆/服务费代销、价税分离/2026 新增值税法/滚动12个月/追溯登记、小型微利/汇算清缴、奖金包/阿米巴/虚拟股、四层架构/资金池、河北低价模型/涨价能力/供应链地位/存货虚增等。
- QA: placeholder scan remains `SHELL: 0`, `THIN: 0`, `OK: 12`.
- Note: This correction establishes a durable rule for transcript ingest: do not condense course transcripts into outline pages; compile them into expanded, evidence-backed, Agent-callable knowledge.

## [2026-06-13] audit | 电商企业财税股权与战略财务管理
- Skill: `llm-wiki-audit-and-optimization`
- Target: `domains/财税与经营财务/90-课程包/01-财税股权28期/`
- Mechanical scan: `SHELL: 0`, `THIN: 0`, `OK: 12`.
- Audited: compile quality, route quality, reasoning readiness, raw/formal evidence-anchor coverage.
- Patched: added missing case and number anchors into formal pages 03/04/06/07/08/09/10, including 山东暖宝宝补税、小规模天猫 1100 万/350 万、四平台边际贡献、2.5 亿/4 万单/13% 退货率、李子柒/微念、罗振宇/申音、雷士照明、良品铺子、石家庄 200 万供应链绑定、代理型业务财务风险等。
- Created: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/qa-audit-report.md`
- Verdict: no P0 blockers; post-patch state is usable as a structured Agent-callable learning path. Remaining improvements are optional P2 route conveniences such as a dedicated query entry and cross-linking with platform settlement accounting.


## [2026-06-12] compile | 同步跨 Agent Skill 注册库
- Updated: `domains/AI Agent工程/skill-design/ai-agent-skill-registry.md`
- Updated: `domains/AI Agent工程/skill-design/personal-ai-agent-skill-registry.md`
- Updated: agent-specific skill registry pages under `domains/AI Agent工程/skill-design/`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Updated: `domains/AI Agent工程/index.md`
- Notes: 扫描系统中 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 `SKILL.md`，当前总计 363 个 skill，其中个人/项目自定义 153 个；Codex 18, Hermes 166, Lark Agent 25, OpenClaw 4, SealSeek 124, Claude Code 26。Touched: domains/AI Agent工程/skill-design/ai-agent-skill-registry.md, domains/AI Agent工程/skill-design/personal-ai-agent-skill-registry.md, domains/AI Agent工程/skill-design/codex-skill-inventory.md, domains/AI Agent工程/skill-design/hermes-skill-registry.md, domains/AI Agent工程/skill-design/lark-agent-skill-registry.md, domains/AI Agent工程/skill-design/openclaw-skill-registry.md, domains/AI Agent工程/skill-design/sealseek-skill-registry.md, domains/AI Agent工程/skill-design/claude-code-skill-registry.md, domains/视觉制作/05-小红书风格AI生图/index.md, domains/AI Agent工程/index.md。

## [2026-06-11] audit | 无限画板 Skill 写作知识库
- Target: `domains/AI Agent工程/skill-design/infinite-canvas-skill-writing/`
- Skill: `llm-wiki-audit-and-optimization`
- Mechanical scan: `SHELL: 0`, `THIN: 0`, `OK: 8`.
- Verified: raw source exists, extraction notes exist, formal pages exist, main/domain domains/视觉制作/05-小红书风格AI生图/indexes route to the knowledge base, wikilinks have zero missing targets.
- Patched: corrected `log.md` ordering so the ingest entry is not embedded inside the previous 2026-06-10 book-ingest entry.
- Remaining issues: no P0/P1 issue found; optional P2 future improvement is to split brand-specific examples such as 杉居/静谧剧场 into domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index case pages if case-level retrieval becomes necessary.

## [2026-06-11] ingest | 无限画板 Skill 写作知识库
- Source: `raw/my-temp-data/infinite-canvas-skill.md`
- Adapter: `llm-wiki-ingest/adapters/markdown-doc.md`
- Created: `_meta/extraction-notes/infinite-canvas-skill-writing-2026-06-11/` source profile, source inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/AI Agent工程/skill-design/infinite-canvas-skill-writing/` domains/视觉制作/05-小红书风格AI生图/index and 7 formal pages covering core rules, tool specs, task patterns, prompt patterns, common pitfalls, quality checklist, and Agent usage template.
- Updated: `domains/AI Agent工程/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将 15 个无限画板 skill 汇总从原文案例重构为面向未来 Agent 写 `skill.md` 的可检索规则库，重点沉淀产品保真、风格迁移、营销真实性、批量处理、工具参数和历史反坑项。

## [2026-06-10] ingest | 品牌视觉：可复制的电商视觉终极玩法
- Source: `raw/books/domains/视觉制作/02-品牌视觉标准化/01-可复制的电商品牌视觉玩法-2018/source.epub`
- Adapter: `llm-wiki-ingest/adapters/book.md`

- Created: `raw/books/domains/视觉制作/02-品牌视觉标准化/01-可复制的电商品牌视觉玩法-2018/` raw EPUB archive with 46 extracted chapter files and 249 image assets.
- Created: `_meta/extraction-notes/domains/视觉制作/02-品牌视觉标准化/01-可复制的电商品牌视觉玩法-2018/` source profile, source inventory, segment plan, knowledge architecture plan, chapter inventory, knowledge-unit inventory, coverage matrix, omission audit, source-to-page map, formal page plan, and audit handoff.
- Created: `domains/视觉制作/02-品牌视觉标准化/01-可复制的电商品牌视觉玩法/` domains/视觉制作/05-小红书风格AI生图/index and 8 formal pages.
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将朱华杰 2018 年电商品牌视觉书籍重构为视觉标准化 learning path，覆盖老板/运营/美工协作、品牌视觉/产品视觉/营销视觉三系统、差异化与统一、12 项品牌视觉标准、记忆符号、摄影包装接触点和 Agent 诊断模板；淘宝/天猫平台工具名均按历史语境处理。

## [2026-06-10] refactor | 营销学理论在电商图片中的应用 canonical 迁移
- Moved canonical concept page to `domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用.md`.
- Converted `shared/business-frameworks/domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用.md` into a bridge page for old-link compatibility and cross-domain orientation.
- Updated primary domains/视觉制作/05-小红书风格AI生图/index and major cross-domain references to point at the domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index canonical page.
- Rationale: the theory uses shared marketing frameworks, but its core application domain is ecommerce image planning, visual conversion, and AI image prompt production.

## [2026-06-09] ingest | 营销学理论在电商图片中的应用补编
- Source: `raw/articles/domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用-2026-05-22.md`
- Requested source: `/Users/pechen/AI/MarketingTheoryEcomImage/docs/营销学理论在电商图片中的应用.md`
- Created: `_meta/extraction-notes/domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用-2026-06-09/`
- Updated: `shared/business-frameworks/domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用.md`
- Created: `domains/视觉制作/01-电商视觉基础/02-电商图片营销策划与AI生图Playbook.md`
- Created: `queries/ecommerce-image-marketing-planning.md`
- Updated: `shared/business-frameworks/index.md`
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/电商运营/index.md`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 请求源与 2026-05-22 已归档 raw 文件 SHA256 一致，本次不重复归档 raw，而是将原总纲页补编为更完整的电商图片营销框架，并新增面向主图、详情页、证据图、场景图和 AI 生图 prompt 的执行 Playbook 与查询入口。

## [2026-06-08] ingest | 淘宝运营速成指南：电商军规81讲
- Source: `raw/books/taobao-operation-quick-guide-81-rules-2018/source.epub`
- Adapter: `llm-wiki-ingest/adapters/book.md`
- Created: `raw/books/taobao-operation-quick-guide-81-rules-2018/` raw EPUB archive and 88 extracted chapter files.
- Created: `_meta/extraction-notes/taobao-operation-quick-guide-81-rules-2018/` source profile, source inventory, segment plan, chapter inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, source-to-page map, and audit handoff.
- Created: `domains/电商运营/02-淘宝天猫/01-淘宝运营速成指南/` domains/视觉制作/05-小红书风格AI生图/index and 12 formal method pages.
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将 2018 年淘宝平台工具和排名规则标为历史语境/待当前复核；正式页沉淀定位、选品、搜索、视觉、流量、客服、促销、供应链、财务、团队和六部曲成功模型。

## [2026-06-08] ingest | 杉居轻厨房生活风品牌变体
- Source asset: `raw/assets/visual-style/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/shanju-moodboard.png`
- Source draft: `inbox/notes/shanju-brand-style-variant-draft-2026-06-08.md`
- Created: `_meta/extraction-notes/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living-2026-06-08/`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/index.md`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/moodboard-analysis.md`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/brand-style-system.md`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/visual-worldbook.md`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook.md`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/copywriting-voice.md`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/reference-gallery.md`
- Created: `queries/domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living-image-generation.md`
- Updated: `domains/视觉制作/04-AI生图风格库/index.md`
- Updated: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/index.md`
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将杉居情绪板与品牌策略推演正式入库为极简北欧风的品牌变体。核心定义为“厨房工具跨室内厨房、露台、庭院、野餐和户外轻料理的北欧轻生活品牌风格”，重点保留浅蓝衬衫女性、橘猫、烧烤盘、调味罐、自然光、鼠尾草绿小物和 `live gently.` 文案系统，并明确排除粗犷露营、夜市烧烤、重烟雾油脂和强促销方向。

## [2026-06-08] ingest | 极简北欧风 AI 生图风格库
- Source: `raw/webpages/visual-style/domains/视觉制作/04-AI生图风格库/01-极简北欧风-style-image-generation-2026-06-08.md`
- Source: `raw/webpages/visual-style/domains/视觉制作/04-AI生图风格库/01-极简北欧风-web-research-2026-06-08.md`
- Assets: `raw/assets/visual-style/domains/视觉制作/04-AI生图风格库/01-极简北欧风/user-product-references/`
- Assets: `raw/assets/visual-style/domains/视觉制作/04-AI生图风格库/01-极简北欧风/zcool-case/`
- Created: `_meta/extraction-notes/domains/视觉制作/04-AI生图风格库/01-极简北欧风-style-image-generation-2026-06-08/`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/index.md`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/01-极简北欧风AI生图Playbook.md`
- Created: `domains/视觉制作/04-AI生图风格库/01-极简北欧风/02-极简北欧风参考图索引.md`
- Created: `queries/domains/视觉制作/04-AI生图风格库/01-极简北欧风-image-generation.md`
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将站酷“极简北欧风”剪藏、7 张用户产品参考图、25 张站酷案例/相关图和联网理论资料编译成面向 AI 生图的风格知识库，重点沉淀色彩、材质、光线、空间、构图、负向约束、参考图权重和 prompt 模板。生成扩展参考图时生图服务返回服务端错误，本次改为保留可复现 prompt 样例。

## [2026-06-08] refactor | AI 生图风格库目录结构
- Created: `domains/视觉制作/04-AI生图风格库/index.md`
- Moved: `domains/视觉制作/04-AI生图风格库/01-极简北欧风-style.md` -> `domains/视觉制作/04-AI生图风格库/01-极简北欧风/index.md`
- Moved: `domains/视觉制作/04-AI生图风格库/01-极简北欧风-image-generation-domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook.md` -> `domains/视觉制作/04-AI生图风格库/01-极简北欧风/01-极简北欧风AI生图Playbook.md`
- Moved: `domains/视觉制作/04-AI生图风格库/01-极简北欧风-domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/reference-gallery.md` -> `domains/视觉制作/04-AI生图风格库/01-极简北欧风/02-极简北欧风参考图索引.md`
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Updated: `queries/domains/视觉制作/04-AI生图风格库/01-极简北欧风-image-generation.md`
- Notes: 将风格库从平铺文件改为“每个风格一个目录”的结构，固定 `domains/视觉制作/05-小红书风格AI生图/index.md`、`domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook.md`、`domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/reference-gallery.md` 三件套，便于后续增加更多视觉风格。

## [2026-06-08] ingest | 电商平台结算时间口径财务核算 XMind
- Source: `raw/data/ecommerce-platform-settlement-accounting-xmind-2026-02-06/`
- Created: `_meta/extraction-notes/ecommerce-platform-settlement-accounting-xmind-2026-02-06/` note set
- Created: `domains/电商运营/01-通用电商方法/03-平台结算与经营财务/01-电商平台结算时间口径财务核算方法.md`
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 使用 `llm-wiki-ingest` 的 XMind adapter 处理三份核算方法 XMind。先识别淘宝 2.6 为 101 节点 superset，再将碎片重构为平台结算时间确认收入、快麦成本匹配、保证金/特殊账户/推广费处理和抖音、拼多多、小红书、视频号、淘宝平台核对方法。28 个截图节点已归档并标记为待 OCR/视觉审计。

## [2026-06-07] ingest | 火山方舟 Doubao-Seedance-2.0 控制台 clipping
- Source: `raw/webpages/volcengine/volcengine-ark-domains/视觉制作/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡-2026-06-07.md`
- Created: `_meta/extraction-notes/volcengine-ark-domains/视觉制作/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡-2026-06-07/` note set
- Created: `domains/视觉制作/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡.md`
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 使用新的 `llm-wiki-ingest` 覆盖契约处理 clipping，保留模型 ID、API endpoint、价格快照、分辨率/帧率、任务类型、能力说明和三段 demo prompt；将无标签数值标记为 unresolved，并生成 audit handoff 供质检 skill 继续检查。

## [2026-06-07] update | OpenAI image generation API example extraction
- Updated: `domains/AI Agent工程/toolchain/openai-image-generation-api.md`
- Source: `raw/webpages/openai/openai-image-generation-api-2026-06-07.md`
- Notes: 补充原文中的代码模板、案例索引、多轮生成、流式 partial images、参考图输入、File ID/base64、mask 编辑、revised prompt、安全错误处理和示例价格表，避免正式页只保留决策摘要。

## [2026-06-07] audit | OpenAI image generation API coverage rerun
- Source: `raw/webpages/openai/openai-image-generation-api-2026-06-07.md`
- Created: `_meta/extraction-notes/openai-image-generation-api-2026-06-07/coverage-checklist.md`
- Updated: `domains/AI Agent工程/toolchain/openai-image-generation-api.md`
- Notes: 按更新后的无遗漏入库标准重跑覆盖审计，并用 OpenAI 官方 docs MCP 补回 raw clipping 未捕获的 JS/curl/CLI 与 Image API direct edit/stream 示例；gallery/decorative images 标为 raw-only。

## [2026-06-07] ingest | Clippings batch: OpenAI image generation API
- Source: `raw/webpages/openai/openai-image-generation-api-2026-06-07.md`
- Created: `domains/AI Agent工程/toolchain/openai-image-generation-api.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Cleaned: `Clippings/Image generation  OpenAI API.md`
- Notes: 使用 wiki-clippings-ingest 的 Product / Tool Documentation profile，并用 OpenAI 官方 docs MCP 校验当前图像生成文档，将剪藏编译为 API 选择、参数、编辑、流式、错误处理和成本判断指南。

## [2026-06-06] repair | 品牌视觉记忆感知与可视化体系 learning path 重编译修复
- Source: `raw/transcripts/domains/品牌策略/04-品牌视觉资产/01-品牌视觉记忆感知与可视化体系-2026-06-03.md`
- Updated: `domains/品牌策略/04-品牌视觉资产/01-品牌视觉记忆感知与可视化体系/` domains/视觉制作/05-小红书风格AI生图/index and 10 chapter pages.
- Updated: `_meta/extraction-notes/domains/品牌策略/04-品牌视觉资产/01-品牌视觉记忆感知与可视化体系-2026-06-03/` note set.
- Created: `_meta/extraction-notes/domains/品牌策略/04-品牌视觉资产/01-品牌视觉记忆感知与可视化体系-2026-06-03/micro-segments/` 10 micro-segment records.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- QA: `placeholder_scan.py` on this learning path returned `SHELL: 0 THIN: 0 OK: 11`; template/process residue grep returned no hits.
- Notes: 将原占位骨架修复为正式可用知识路径，重点补强视觉资产传承、记忆感知三要素、英式辅食/爱眼饮品/凯瑞斯/梦百合/F 运动服饰案例、ABC 视觉分层、可视化世界观四模块与 AI 生图执行模板。该路径已从 brand-strategy 路由表的“重编译中”移出。

## [2026-06-06] repair | 电商品牌心智产品力与大单品战略 learning path 重编译修复
- Source: `raw/transcripts/domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略-2026-06-03.md`
- Updated: `domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略/` domains/视觉制作/05-小红书风格AI生图/index and 11 chapter pages.
- Updated: `_meta/extraction-notes/domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略-2026-06-03/` note set.
- Created: `_meta/extraction-notes/domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略-2026-06-03/micro-segments/` 11 micro-segment records.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- QA: `placeholder_scan.py` on this learning path returned `SHELL: 0 THIN: 0 OK: 12`; template/process residue grep returned no hits.
- Notes: 将原占位骨架修复为正式可用知识路径，重点沉淀用户经营、心智产品力、高定价高佣金 KOC 起盘、大单品第一性原理、爆品/大单品/战略大单品分级、后手与英雄系列、战略大单品五大价值、燕之屋年轻化即食燕窝企划和 Agent 诊断模板。品牌产品营销与拓品策略经单独扫描也已确认无 shell，路由状态同步改为已编译。

## [2026-06-06] repair | 品牌大单品打造与产品企划营销 learning path 重编译修复
- Source: `raw/transcripts/domains/品牌策略/03-产品战略与大单品/02-品牌大单品打造与产品企划营销-2026-06-03.md`
- Updated: `domains/品牌策略/03-产品战略与大单品/02-品牌大单品打造与产品企划营销/` domains/视觉制作/05-小红书风格AI生图/index and 10 chapter pages.
- Updated: `_meta/extraction-notes/domains/品牌策略/03-产品战略与大单品/02-品牌大单品打造与产品企划营销-2026-06-03/` note set.
- Created: `_meta/extraction-notes/domains/品牌策略/03-产品战略与大单品/02-品牌大单品打造与产品企划营销-2026-06-03/micro-segments/` 10 micro-segment records.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- QA: `placeholder_scan.py` on this learning path returned `SHELL: 0 THIN: 0 OK: 11`; template/process residue grep returned no hits.
- Notes: 将原占位骨架修复为正式可用知识路径，重点沉淀大单品企划链路、燕之屋鲜炖防守、小燕农燕窝粥第二增长曲线、产品矩阵角色分工、差异化创新、加体验/减负担、卖点可视化、昵称化命名、爆品心智分阶段策略和 Agent 企划模板。brand-strategy 路由表中的“重编译中”状态已清空。

## [2026-06-05] compile | 重编译 品牌产品营销与拓品策略 04-09 章
- Updated: `domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略/04-不同渠道表达规则.md`
- Updated: `domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略/05-望山楂案例：场景重构.md`
- Updated: `domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略/06-拓品逻辑与边界.md`
- Updated: `domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略/07-增量市场与存量市场拓品路径.md`
- Updated: `domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略/08-非标品企划先行逻辑.md`
- Updated: `domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略/09-品牌识别统一与全渠道协同.md`
- Removed: 旧占位骨架 `06-product-expansion-three-valid-paths.md`, `07-growth-paths-haiguibaba-and-aulaike.md`, `08-brand-mindshare-productization-with-kelu.md`, `09-domains/视觉制作/05-小红书风格AI生图/09-Agent使用模板：小红书风格生图.md`
- Updated: 路径 `domains/视觉制作/05-小红书风格AI生图/index.md`、`domains/品牌策略/index.md`、根 `domains/视觉制作/05-小红书风格AI生图/index.md` 的章节链接与文件名
- Notes: 按统一标准（摘要/核心问题/方法框架/推导逻辑/判断标准/常见误区/Agent提示词/相关页面/来源）重编译后半段。核对原文锚点：东鹏特饮双人群、王小五追剧、望山楂吃辣场景裂变与谐音梗SKU、活力28乱拓反例 vs 保洁多品牌隔离 + 参半美白拓品、海龟爸爸（增量·以点穿面）vs 欧莱克速简美学（存量·多点渗透）完整品类链、潮趣袜企划（曹老师留学生PM、大成产品课）、freestyle"偏见"独立人格、可露轻珠宝（探索/自我/快乐、Smiley联名、2024探索关系、凯琳/FA奖）。把原 09 Agent 模板拆解到各章的"可用于 Agent 的提示词"小节。

## [2026-06-05] compile | 同步跨 Agent Skill 注册库
- Updated: `domains/AI Agent工程/skill-design/ai-agent-skill-registry.md`
- Updated: `domains/AI Agent工程/skill-design/personal-ai-agent-skill-registry.md`
- Updated: agent-specific skill registry pages under `domains/AI Agent工程/skill-design/`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Updated: `domains/AI Agent工程/index.md`
- Notes: 扫描系统中 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 `SKILL.md`，当前总计 356 个 skill，其中个人/项目自定义 146 个；Codex 16, Hermes 167, Lark Agent 25, OpenClaw 4, SealSeek 118, Claude Code 26。Touched: domains/AI Agent工程/skill-design/ai-agent-skill-registry.md, domains/AI Agent工程/skill-design/personal-ai-agent-skill-registry.md, domains/AI Agent工程/skill-design/hermes-skill-registry.md。

## [2026-06-05] compile | 同步跨 Agent Skill 注册库
- Updated: `domains/AI Agent工程/skill-design/ai-agent-skill-registry.md`
- Updated: `domains/AI Agent工程/skill-design/personal-ai-agent-skill-registry.md`
- Updated: agent-specific skill registry pages under `domains/AI Agent工程/skill-design/`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Updated: `domains/AI Agent工程/index.md`
- Notes: 扫描系统中 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 `SKILL.md`，当前总计 356 个 skill，其中个人/项目自定义 167 个；Codex 16, Hermes 167, Lark Agent 25, OpenClaw 4, SealSeek 118, Claude Code 26。Touched: domains/AI Agent工程/skill-design/ai-agent-skill-registry.md, domains/AI Agent工程/skill-design/personal-ai-agent-skill-registry.md, domains/AI Agent工程/skill-design/codex-skill-inventory.md, domains/AI Agent工程/skill-design/hermes-skill-registry.md, domains/AI Agent工程/skill-design/lark-agent-skill-registry.md, domains/AI Agent工程/skill-design/openclaw-skill-registry.md, domains/AI Agent工程/skill-design/sealseek-skill-registry.md, domains/AI Agent工程/skill-design/claude-code-skill-registry.md, domains/视觉制作/05-小红书风格AI生图/index.md, domains/AI Agent工程/index.md。

## [2026-06-05] compile | 同步跨 Agent Skill 注册库
- Updated: `domains/AI Agent工程/skill-design/ai-agent-skill-registry.md`
- Updated: agent-specific skill registry pages under `domains/AI Agent工程/skill-design/`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Updated: `domains/AI Agent工程/index.md`
- Notes: 扫描系统中 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 `SKILL.md`，当前总计 356 个 skill；Codex 16, Hermes 167, Lark Agent 25, OpenClaw 4, SealSeek 118, Claude Code 26。Touched: domains/AI Agent工程/skill-design/ai-agent-skill-registry.md, domains/AI Agent工程/skill-design/codex-skill-inventory.md, domains/AI Agent工程/skill-design/hermes-skill-registry.md, domains/AI Agent工程/skill-design/lark-agent-skill-registry.md, domains/AI Agent工程/skill-design/openclaw-skill-registry.md, domains/AI Agent工程/skill-design/sealseek-skill-registry.md, domains/AI Agent工程/skill-design/claude-code-skill-registry.md。

## [2026-05-22] create | Wiki initialized
- Path: `/Users/pechen/wiki`
- Architecture: one vault, multiple domains, shared layer, projects layer.
- Created core files: README.md, SCHEMA.md, AGENTS.md, CLAUDE.md, HERMES.md, OPENCLAW.md, SEALSEEK.md, domains/视觉制作/05-小红书风格AI生图/index.md, log.md.

## [2026-05-22] ingest | Karpathy LLM Wiki gist
- Source: `raw/articles/karpathy-llm-wiki-2026-05-22.md`
- Created: `shared/knowledge-management/llm-wiki.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: First formal knowledge page. Used to test the LLM Wiki workflow.

## [2026-05-22] ingest | 营销学理论在电商图片中的应用
- Source: `raw/articles/domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用-2026-05-22.md`
- Created: `shared/business-frameworks/domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用.md`
- Updated: `shared/business-frameworks/index.md`
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 首篇业务方法论 ingest 测试。作为电商运营、视觉制作、品牌策划共享的图片营销理论总纲页。

## [2026-05-22] ingest | 18期品牌战略课程转写知识萃取
- Source: `raw/transcripts/brand-strategy-methodology-course-opening-2026-05-22.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening-extraction-2026-05-22.md`
- Created: `domains/品牌策略/concepts/brand-building-methodology.md`
- Created: `domains/品牌策略/concepts/brand-three-capabilities-model.md`
- Created: `domains/品牌策略/concepts/ecommerce-brand-case-analysis-framework.md`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 使用 course-transcript-to-knowledge skill，从课程录音转写中去课程化提炼品牌战略理论、三能力模型和案例拆解框架。

## [2026-05-22] rewrite | 品牌战略课程知识复现重做
- Source: `raw/transcripts/brand-strategy-methodology-course-opening-2026-05-22.md`
- Removed: previous over-compressed brand strategy extraction pages.
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening-reconstruction-2026-05-22.md`
- Created: `domains/品牌策略/concepts/brand-strategy-knowledge-system.md`
- Created: `domains/品牌策略/concepts/brand-energy-accumulation-framework.md`
- Created: `domains/品牌策略/concepts/brand-case-reconstruction-patterns.md`
- Created: `domains/品牌策略/concepts/brand-strategy-application-templates.md`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 根据 用户 反馈，正式知识页应做课堂知识理论复现、分析、归纳和扩充，而不是摘要式提炼。

## [2026-05-22] rewrite | 品牌战略课程分段知识复现
- Source: `raw/transcripts/brand-strategy-methodology-course-opening-2026-05-22.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/segment-plan.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/coverage-matrix.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/segments/segment-*.md`
- Created formal pages: 9 brand-strategy knowledge reconstruction pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 按新版 course-transcript-to-knowledge skill 重跑，采用分段复现、覆盖矩阵和总融合机制；正式页已去除来源语气。

## [2026-05-22] update | 品牌战略课程 micro-segment 重跑
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/micro-segment-plan.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/micro-coverage-matrix.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening/micro-segments/MS-*.md`
- Updated: selected formal brand strategy pages with micro-segment coverage notes and richer case/action chains.
- Notes: Skill test iteration. Added knowledge-point-level processing to avoid segment-level tiger-head-snake-tail loss.

## [2026-05-22] create | 泰兰尼斯品牌案例深度复现
- Created: `domains/品牌策略/cases/tailanisi-brand-reconstruction.md`
- Sources: `raw/transcripts/brand-strategy-methodology-course-opening-2026-05-22.md`, micro-segments `MS-027` 至 `MS-037`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 使用 micro-segment 机制测试案例深度复现，将泰兰尼斯从动作链扩展为完整品牌蓄能案例。

## [2026-05-22] create | 剩余品牌案例深度复现
- Created: `domains/品牌策略/cases/pggu-wedding-shoes-brand-reconstruction.md`
- Created: `domains/品牌策略/cases/dopamine-sports-bra-brand-reconstruction.md`
- Created: `domains/品牌策略/cases/pet-brand-product-tier-strategy-reconstruction.md`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 按泰兰尼斯深度复现样式，完成 PGGU、运动内衣、宠物品牌问答三个案例页。

## [2026-05-22] sample | PGGU 战略选择逐段知识复现
- Deleted: previous over-structured brand strategy transcript outputs, preserving raw transcript.
- Created: `domains/品牌策略/90-样本/01-PGGU战略选择知识复现样本.md`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 根据 用户 反馈，测试新版流程：清洗原文、解释含义、用大模型扩展推理、再整理为知识库文章；重点验证“结论如何得出”而不是只保留结论。

## [2026-05-23] create | 电商品牌增长方法论顺序知识页
- Source: `raw/transcripts/brand-strategy-methodology-course-opening-2026-05-22.md`
- Created: `domains/品牌策略/01-品牌基础与增长方法/01-电商品牌增长方法论/index.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening-v2/coverage-matrix.md`
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将品牌战略长资料融合为按知识发展顺序阅读的正式理论文章，并修正 PGGU 样本索引描述。

## [2026-05-23] update | 电商品牌增长方法论深度补充
- Updated: `domains/品牌策略/01-品牌基础与增长方法/01-电商品牌增长方法论/index.md`
- Updated: `_meta/extraction-notes/brand-strategy-methodology-course-opening-v2/coverage-matrix.md`
- Notes: 续处理网络中断前的品牌战略长资料，将首版总纲进一步补成更完整的案例推导和方法论文章，补入德佑风险、名品/精品/爆品、泰兰尼斯推导链、PGGU 完整动作链、运动内衣女性议题和四模块优先级诊断。
## [2026-05-23] validate | course-transcript-to-knowledge Skill 品牌战略案例验收
- Updated Skill outside wiki: `course-transcript-to-knowledge` now explicitly requires classification map and segment knowledge-unit consolidation before formal synthesis.
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening-v2/segment-knowledge-inventory.md`
- Created: `_meta/extraction-notes/brand-strategy-methodology-course-opening-v2/skill-test-report.md`
- Notes: Confirmed the brand strategy transcript workflow: segment, understand, enrich with LLM analysis, form segment knowledge units, classify/merge, then archive into the formal wiki page.
## [2026-05-23] restructure | 电商品牌增长方法论按章节拆分
- Updated: `domains/品牌策略/01-品牌基础与增长方法/01-电商品牌增长方法论/index.md` as a chapter directory instead of a mega-page.
- Created: `domains/品牌策略/01-品牌基础与增长方法/01-电商品牌增长方法论/01-*.md` through `12-*.md`.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 根据 用户 反馈，长录音入库应按知识发展顺序拆成带编号的章节文件，避免一个总纲页或无序碎片页影响后续阅读和 Agent 检索。

## [2026-05-24] update | 品牌战略课程知识库漏项回补
- Updated: `domains/品牌策略/01-品牌基础与增长方法/01-电商品牌增长方法论/01-为什么电商企业必须重新理解品牌.md`
- Updated: `domains/品牌策略/01-品牌基础与增长方法/01-电商品牌增长方法论/07-运动内衣：用多巴胺运动美学错开巨头.md`
- Updated: `_meta/extraction-notes/brand-strategy-methodology-course-opening-v2/coverage-matrix.md`
- Notes: 回补原录音中的生命周期对照数字、安德玛竞品举例，并修正 coverage matrix 对章节化正式输出的说明；确认“高端款”已被更稳妥的理论表达吸收。
## [2026-05-24] ingest | 电商品牌竞争战略下午场知识重构
- Source: `raw/transcripts/domains/品牌策略/02-品类心智与差异化/01-电商品牌竞争战略：品类心智与品牌打造-2026-05-23.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/01-电商品牌竞争战略：品类心智与品牌打造-2026-05-23/segment-plan.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/01-电商品牌竞争战略：品类心智与品牌打造-2026-05-23/micro-segment-plan.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/01-电商品牌竞争战略：品类心智与品牌打造-2026-05-23/coverage-matrix.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/01-电商品牌竞争战略：品类心智与品牌打造-2026-05-23/segment-knowledge-inventory.md`
- Created: `domains/品牌策略/02-品类心智与差异化/01-电商品牌竞争战略：品类心智与品牌打造/` domains/视觉制作/05-小红书风格AI生图/index and 8 chapter pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 按 course-transcript-to-knowledge skill 完成下午场长转写分段、微分段、知识单元合并和正式章节化入库；现场事务与服务销售信息按覆盖矩阵说明省略。
## [2026-05-24] ingest | 细分品类品牌升级与执行力落地知识重构
- Source: `raw/transcripts/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-23.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-23/segment-plan.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-23/micro-segment-plan.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-23/coverage-matrix.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-23/segment-knowledge-inventory.md`
- Created: `domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地/` domains/视觉制作/05-小红书风格AI生图/index and 8 chapter pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 按 course-transcript-to-knowledge skill 完成细分品类品牌升级与执行力课程的长转写重构，保留方法、案例和组织执行机制，省略课堂组织与噪音内容。

## [2026-05-25] ingest | 抖音链接入库：Obsidian 插件武装知识库
- Source: `raw/webpages/douyin-obsidian-plugin-stack-knowledge-base-2026-05-25.md`
- Source: `raw/transcripts/douyin-obsidian-plugin-stack-knowledge-base-2026-05-25.md`
- Created: `_meta/extraction-notes/douyin-obsidian-plugin-stack-knowledge-base-2026-05-25.md`
- Created: `shared/knowledge-management/obsidian-plugin-stack-for-knowledge-base.md`
- Updated: `shared/knowledge-management/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 借鉴 luminote 后端的抖音链接解析与视频处理方式完成第一轮测试；成功解析并下载视频，完成前半段可用转录与正式知识重构，后半段转录重复漂移已在 extraction notes 中标注并纳入 omission audit。

## [2026-05-24] ingest | 细分品类品牌升级与执行力落地知识重构（复跑）
- Source: `raw/transcripts/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-24.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-24/segment-plan.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-24/micro-segment-plan.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-24/coverage-matrix.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地-2026-05-24/segment-knowledge-inventory.md`
- Created: `domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地/` domains/视觉制作/05-小红书风格AI生图/index and 8 chapter pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 按 course-transcript-to-knowledge skill 完成分段、微分段、知识单元合并和正式章节化入库；事务信息按覆盖矩阵省略。

## [2026-05-28] create | AI Agent 工程知识域
- Created: `domains/AI Agent工程/index.md`
- Created: `domains/AI Agent工程/knowledge-systems/index.md`
- Created directories: `domains/AI Agent工程/knowledge-systems/`, `agent-architecture/`, `skill-design/`, `toolchain/`, `prompt-and-context/`, `automation-workflows/`, `evaluation-and-debugging/`
- Updated: `SCHEMA.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Updated: `shared/knowledge-management/index.md`
- Updated: `shared/ai-agent-workflows/index.md`
- Notes: 将 AI 方法、知识系统、Skill、工具链与自动化工作流从 shared/project 混合状态中抽出为长期能力域，保持个人 Wiki 的一库多域结构。

## [2026-05-28] ingest | 抖音链接入库：用 AI 打造一个永不烂尾的知识库
- Source: `raw/webpages/douyin-ai-never-abandoned-personal-knowledge-base-2026-05-28.md`
- Source: `raw/transcripts/douyin-ai-never-abandoned-personal-knowledge-base-2026-05-28.md`
- Created: `raw/assets/douyin/ai-never-abandoned-personal-knowledge-base-2026-05-28/video.mp4`
- Created: `_meta/extraction-notes/douyin-ai-never-abandoned-personal-knowledge-base-2026-05-28.md`
- Created: `_meta/extraction-notes/douyin-ai-never-abandoned-personal-knowledge-base-2026-05-28-pipeline-report.json`
- Created: `domains/AI Agent工程/knowledge-systems/llm-wiki-personal-knowledge-base-operating-loop.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 使用 DashScope qwen-vl-max video chunk pipeline 完成真实 API 转录与 QC，沉淀 LLM Wiki 在个人知识库中的运行闭环、三层结构与 Ingest / Query / Lint 操作模式。

## [2026-06-01] ingest | 咨询逻辑 XMind 知识库化
- Source: `raw/data/consulting-logic-xmind-2026-03-02.xmind`
- Source: `raw/data/consulting-logic-xmind-2026-03-02-content.json`
- Created assets: `raw/assets/consulting-logic-xmind-2026-03-02/`
- Created: `_meta/extraction-notes/consulting-logic-xmind-2026-06-01/original-outline.md`
- Created: `_meta/extraction-notes/consulting-logic-xmind-2026-06-01/coverage-matrix.md`
- Created: `domains/电商运营/01-通用电商方法/01-电商企业咨询与交付/` domains/视觉制作/05-小红书风格AI生图/index and 11 chapter pages.
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将 770 节点、最大 14 层的 XMind 脑图按 LLM Wiki 方式入库：raw 保留原件与 content.json，正式知识按咨询场景重构为可供 Agent 检索和调用的章节化页面。

## [2026-06-03] ingest | Clippings batch: 淘宝营销工具规则
- Source: `raw/webpages/taobao/taobao-coupon-settings-merchant-ops-2026-06-02.md`
- Source: `raw/webpages/taobao/taobao-shop-promotion-stacking-rule-upgrade-2026-04-14.md`
- Source: `raw/webpages/taobao/taobao-super-discount-registration-whitepaper-2026-05-19.md`
- Created: `domains/电商运营/02-淘宝天猫/02-淘宝营销工具/01-淘宝营销工具：优惠券.md`
- Created: `domains/电商运营/02-淘宝天猫/02-淘宝营销工具/02-淘宝营销工具：超级立减.md`
- Created: `domains/电商运营/02-淘宝天猫/02-淘宝营销工具/03-淘宝营销工具叠加与互斥规则.md`
- Created: `domains/电商运营/02-淘宝天猫/02-淘宝营销工具/04-淘宝营销工具选择Playbook.md`
- Created: `queries/taobao-marketing-tool-planning.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Cleaned: `Clippings/商家服务大厅-淘宝网Taobao.com-淘！我喜欢.md`
- Cleaned: `Clippings/商家服务大厅-淘宝网Taobao.com-淘！我喜欢 1.md`
- Cleaned: `Clippings/商家服务大厅-淘宝网Taobao.com-淘！我喜欢 2.md`
- Notes: 使用 wiki-clippings-ingest 的 rule/reference profile，将淘宝营销工具剪藏编译为工具卡、互斥矩阵、选择 domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook 和 AI 查询入口。

## [2026-06-03] ingest | 旺店通开放平台 API 文档
- Source: `https://open.wangdian.cn/Y/open/apidoc`
- Created: `raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json`
- Created: `raw/api/wangdian-openapi/wangdian-openapi-full-archive-2026-06-03.md`
- Created: `raw/api/wangdian-openapi/wangdian-openapi-compact-domains/视觉制作/05-小红书风格AI生图/index-2026-06-03.json`
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/index.md`
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/01-旺店通API能力地图.md`
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/02-旺店通API Skill创建指南.md`
- Created: `queries/wangdian-api-skill-creation.md`
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 使用 Chrome DevTools MCP 抓取 77 个旺店通 ERP API 详情，按订单、库存、货品、基础、售后、采购编译为接口目录、能力地图和 Skill 创建入口。

## [2026-06-03] update | 旺店通 API 分类使用手册
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/03-旺店通订单类API使用手册.md`
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/04-旺店通库存类API使用手册.md`
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/05-旺店通货品类API使用手册.md`
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/06-旺店通基础类API使用手册.md`
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/07-旺店通售后类API使用手册.md`
- Created: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/08-旺店通采购类API使用手册.md`
- Updated: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/index.md`
- Updated: `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/02-旺店通API Skill创建指南.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将 77 个接口按 6 个业务分类补充为可直接写代码的使用手册，覆盖请求地址、公共参数、业务参数、响应字段和示例。

## [2026-06-09] ingest | 天猫超市介绍与京东自营入驻全解析
- Sources: `raw/platforms/tmall-supermarket-introduction-2012/source.pptx`, `raw/platforms/jd-self-operated-entry-guide-2026/source.pdf`
- Created: `raw/platforms/tmall-supermarket-introduction-2012/extracted-slides.md`
- Created: `raw/platforms/jd-self-operated-entry-guide-2026/extracted-text.md`
- Created: `_meta/extraction-notes/tmall-supermarket-introduction-2012/` note set
- Created: `_meta/extraction-notes/jd-self-operated-entry-guide-2026/` note set
- Created: `domains/电商运营/01-通用电商方法/02-平台渠道与入驻合作/index.md`
- Created: `domains/电商运营/02-淘宝天猫/03-天猫超市入驻合作/01-天猫超市合作与入驻说明.md`
- Created: `domains/电商运营/03-京东/01-京东自营入驻解析.md`
- Created: `domains/电商运营/01-通用电商方法/02-平台渠道与入驻合作/01-天猫超市与京东自营合作模式对比.md`
- Created: `domains/电商运营/01-通用电商方法/02-平台渠道与入驻合作/02-平台入驻与自营合作诊断模板.md`
- Updated: `domains/电商运营/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将两份平台入驻资料编译为电商平台入驻与自营合作知识库，沉淀天猫超市供应商模式、京东自营 B2B2C 模式、费用/资质来源口径、平台合作对比和 Agent 诊断模板；强时效数据均标注需官方复核。质检时补充识别天猫 PPT 第 8 页 6 个合作案例 Logo，并标注其仅为案例线索。

## [2026-06-03] ingest | 电商品牌差异化感知系统课程知识重构
- Source: `raw/transcripts/domains/品牌策略/02-品类心智与差异化/02-品牌差异化感知系统-2026-05-24.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/02-品牌差异化感知系统-2026-05-24/segment-plan.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/02-品牌差异化感知系统-2026-05-24/micro-segment-plan.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/02-品牌差异化感知系统-2026-05-24/coverage-matrix.md`
- Created: `_meta/extraction-notes/domains/品牌策略/02-品类心智与差异化/02-品牌差异化感知系统-2026-05-24/segment-knowledge-inventory.md`
- Created: `domains/品牌策略/02-品类心智与差异化/02-品牌差异化感知系统/` domains/视觉制作/05-小红书风格AI生图/index and 10 chapter pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 按 course-transcript-to-knowledge skill 将品牌差异化感知系统课程重构为章节化理论路径，重点沉淀免费广告位、心向感知、品类情绪、双品牌差异化案例与记忆感知三标准。


## [2026-06-05] compile | 扩展 SealSeek Skill 注册来源
- Updated: `domains/AI Agent工程/skill-design/ai-agent-skill-registry.md`
- Updated: `domains/AI Agent工程/skill-design/sealseek-skill-registry.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将 SealSeek skill 来源从单一 `/Users/pechen/.sealseek/skill_pool` 扩展为多来源，新增 `/Users/pechen/.sealseek/workspace/skills`、`/Users/pechen/.sealseek/workspaces/default/skills`、`active_skills`、`customized_skills`、`backups`、`/Users/pechen/sealseek`、`/Users/pechen/hermes/xc-sealseek-aicoding-skill`。SealSeek 记录从 12 增至 118；跨 Agent 注册库总量从 249 增至 355。

## [2026-06-12] refactor | LLM Wiki Skill 同源化与 Obsidian CLI 集成
- Source: `/Users/pechen/.codex/skills/.llmwiki-source`
- Source: `git@github.com:petercjl/LLMWiki.git`
- Created: `domains/AI Agent工程/skill-design/llm-wiki-skill-source-package.md`
- Updated: `domains/AI Agent工程/skill-design/personal-ai-agent-skill-registry.md`
- Updated: `domains/AI Agent工程/skill-design/ai-agent-skill-registry.md`
- Updated: `domains/AI Agent工程/skill-design/codex-skill-inventory.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将 LLM Wiki skill 收敛为 Codex 源头维护、GitHub 分发的 5 个发布入口；API docs、web clipping、book、course transcript 的旧独立入口并入 `llm-wiki-ingest` adapters；新增 Obsidian CLI query-pack、route-audit、health-check 协议与脚本。SealSeek/Hermes 旧副本不在本次直接清理，应后续从 GitHub 重新安装同源包。

## [2026-06-05] compile | 跨 Agent Skill 注册库重构
- Created: `domains/AI Agent工程/skill-design/ai-agent-skill-registry.md`
- Created: `domains/AI Agent工程/skill-design/hermes-skill-registry.md`
- Created: `domains/AI Agent工程/skill-design/lark-agent-skill-registry.md`
- Created: `domains/AI Agent工程/skill-design/openclaw-skill-registry.md`
- Created: `domains/AI Agent工程/skill-design/sealseek-skill-registry.md`
- Created: `domains/AI Agent工程/skill-design/claude-code-skill-registry.md`
- Updated: `domains/AI Agent工程/skill-design/codex-skill-inventory.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 将原 Codex 单页清单升级为跨 Agent skill 注册库，按 agent 分类但支持全局检索；覆盖 Codex 15、Hermes 167、Lark Agent 25、OpenClaw 4、SealSeek 12、Claude Code 26，共 249 个 skill，并记录原始 `SKILL.md` 文件位置。

## [2026-06-04] compile | Codex Skill 清单
- Created: `domains/AI Agent工程/skill-design/codex-skill-inventory.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 按名称、功能介绍和输入方式整理 Codex 本地业务 skill 与系统 skill，并明确不同 AI Agent 的 skill 需要分开维护。

## [2026-06-03] ingest | 品牌视觉记忆感知与可视化体系搭建课程知识重构
- Source: `raw/transcripts/domains/品牌策略/04-品牌视觉资产/01-品牌视觉记忆感知与可视化体系-2026-06-03.md`
- Created: `_meta/extraction-notes/domains/品牌策略/04-品牌视觉资产/01-品牌视觉记忆感知与可视化体系-2026-06-03/` note set
- Created: `domains/品牌策略/04-品牌视觉资产/01-品牌视觉记忆感知与可视化体系/` domains/视觉制作/05-小红书风格AI生图/index and 10 chapter pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 重点沉淀品牌视觉主线、传承/特色/效率三要素、ABC 分层、可视化世界观与 AI 团队重构方法。

## [2026-06-03] ingest | AI在商业视觉设计中的应用方法与实践分享
- Source: `raw/transcripts/domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践-2026-06-03.md`
- Created: `_meta/extraction-notes/domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践-2026-06-03/` note set
- Created: `domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践/` domains/视觉制作/05-小红书风格AI生图/index and 7 chapter pages.
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 重点沉淀 AI 商业视觉的真实降本增效案例、图片/视频工作流、品牌上限与团队重构逻辑。

## [2026-06-03] ingest | 电商品牌心智产品力与大单品战略打造课程
- Source: `raw/transcripts/domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略-2026-06-03.md`
- Created: `_meta/extraction-notes/domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略-2026-06-03/` note set
- Created: `domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略/` domains/视觉制作/05-小红书风格AI生图/index and 11 chapter pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 重点沉淀用户经营时代、心智产品力、大单品分级、系列资产与燕之屋即食燕窝企划案例。

## [2026-06-03] ingest | 品牌大单品打造与产品企划营销课程分享
- Source: `raw/transcripts/domains/品牌策略/03-产品战略与大单品/02-品牌大单品打造与产品企划营销-2026-06-03.md`
- Created: `_meta/extraction-notes/domains/品牌策略/03-产品战略与大单品/02-品牌大单品打造与产品企划营销-2026-06-03/` note set
- Created: `domains/品牌策略/03-产品战略与大单品/02-品牌大单品打造与产品企划营销/` domains/视觉制作/05-小红书风格AI生图/index and 10 chapter pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 重点沉淀燕之屋防守战、第二增长曲线、差异化创新、卖点可视化、昵称化命名与爆品心智打造方法。

## [2026-06-03] ingest | 品牌产品营销与拓品策略分享
- Source: `raw/transcripts/domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略-2026-06-03.md`
- Created: `_meta/extraction-notes/domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略-2026-06-03/` note set
- Created: `domains/品牌策略/03-产品战略与大单品/03-品牌产品营销与拓品策略/` domains/视觉制作/05-小红书风格AI生图/index and 9 chapter pages.
- Updated: `domains/品牌策略/index.md`
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`
- Notes: 重点沉淀场景营销、渠道表达规则、合理拓品三路径与可露的品牌心智产品化方法。

## [2026-06-11] collect | 钉钉文档：01-人群推广（原引力魔方）
- Source: `https://alidocs.dingtalk.com/i/nodes/Obva6QBXJwxNZoMOCgk2GZge8n4qY5Pr`
- Created: `raw/webpages/taobao/taobao-wanxiang-audience-promotion-yinlimofang-alidocs-2026-06-11.md`
- Notes: 先按原始网页采集保存，未正式编译入 LLM Wiki；页面为钉钉文档 iframe/虚拟滚动，已标注采集完整性与评论区广告噪声。

## [2026-06-11] clean-test | 钉钉文档：01-人群推广（原引力魔方）
- Source: `raw/webpages/taobao/taobao-wanxiang-audience-promotion-yinlimofang-alidocs-2026-06-11.md`
- Created: `raw/webpages/taobao/taobao-wanxiang-audience-promotion-yinlimofang-cleaned-2026-06-11.md`
- Notes: 手工测试“抓取时清洗理解”的中间层流程：删除虚拟滚动重复、评论广告和字数统计，将正文整理为可等待入脑的干净 raw，并记录图片 URL 未稳定获取时的处理策略。

## [2026-06-11] asset-capture | 钉钉文档：01-人群推广（原引力魔方）截图资产
- Source: `https://alidocs.dingtalk.com/i/nodes/Obva6QBXJwxNZoMOCgk2GZge8n4qY5Pr`
- Created: `raw/assets/taobao/taobao-wanxiang-audience-promotion-yinlimofang-2026-06-11/viewport-01.png` through `viewport-10.png`
- Updated: `raw/webpages/taobao/taobao-wanxiang-audience-promotion-yinlimofang-cleaned-2026-06-11.md`
- Notes: 原始图片 URL 未稳定暴露，改用内置浏览器逐屏截图保留可展示图片资产，覆盖人群推广概览、竞争突破、信息流资源位、新建流程、选品、预算、人群设置等操作图。

## [2026-06-11] asset-capture-test | 钉钉文档图片预览层裁剪
- Source: `https://alidocs.dingtalk.com/i/nodes/Obva6QBXJwxNZoMOCgk2GZge8n4qY5Pr`
- Created: `raw/assets/taobao/taobao-wanxiang-audience-promotion-yinlimofang-2026-06-11/original-image-crops/image-setup-manual-bid-resource-position.png`
- Updated: `raw/webpages/taobao/taobao-wanxiang-audience-promotion-yinlimofang-cleaned-2026-06-11.md`
- Notes: 验证更合适的图片采集方式：双击钉钉文档内图片打开预览层，再裁剪预览图片本体；整页截图仅作为调试备份，不作为正式知识库展示图。
## [2026-06-13] ingest | 小红书生图提示词库
- Source: `raw/articles/xiaohongshu-image-prompt-library-2026-06-13.md`
- Created: `_meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/` note set.
- Created: `domains/视觉制作/05-小红书风格AI生图/` domains/视觉制作/05-小红书风格AI生图/index and 9 formal pages.
- Created: `queries/domains/视觉制作/05-小红书风格AI生图/index.md`.
- Updated: `domains/视觉制作/index.md`.
- Updated: `domains/视觉制作/05-小红书风格AI生图/index.md`.
- Notes: 将小红书生图提示词库编译为内容场景、封面类型、组图结构、卖点转译、变量库、模板库、QA 和 Agent 使用入口。
## [2026-06-14] compile | 品牌策略案例库补全

- 将 `domains/品牌策略/90-样本/` 从单一 PGGU 样本扩展为品牌案例库。
- 基于品牌课程 raw transcript 与已编译理论页，新增 15 个案例页：泰兰尼斯、运动内衣、宠物品类、参半、绵竹屋、音速猫、芝凡与李旭、燕之屋、中式膏方、望山楂、英式辅食、爱眼饮品、凯瑞斯、梦百合、F 运动服饰。
- 更新品牌策略 domain index 与根 `index.md`，让 Agent 可以按品牌问题调用案例。
- QA：`90-样本` placeholder scan 结果为 `SHELL:0 THIN:0 OK:17`，内部 wikilink `missing_count:0`。
## [2026-06-15] ingest | Codex-Photoshop 协作自动化能力边界

- Source: `raw/articles/codex-photoshop-toolkit-validation-2026-06-15.md`
- Created: `domains/视觉制作/03-AI商业视觉/02-Codex与Photoshop协作自动化能力边界.md`
- Updated: `domains/视觉制作/03-AI商业视觉/index.md`
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `index.md`
- Notes: 复测 Codex-PS 工具链：Photoshop probe 11/12 通过，失败项为无 UI 内容识别填充；Apple Vision OCR 对样图 6 行文字全识别；记录 JSX bridge、OCR、psd-tools、ImageMagick、ExifTool、UPIA 插件状态，以及 UXP/Alchemist/IOPaint-LaMa 的后续安装边界。

## [2026-06-15] compile | 可编辑海报 PSD 重建 Skill

- Created: `domains/视觉制作/03-AI商业视觉/03-可编辑海报PSD重建Skill.md`
- Updated: `domains/视觉制作/03-AI商业视觉/index.md`
- Updated: `domains/视觉制作/index.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页.md`
- Updated: `domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库.md`
- Updated: `index.md`
- Notes: 登记 Codex skill `editable-poster-psd-rebuild`，用于将 GPT Image 2 等 AI 带字电商海报重建为无文案底图、隐藏原图参考层和授权字体可编辑文字层 PSD；默认字体为思源宋体 CN Regular / 思源黑体 CN Regular，英文 tracking 默认 200，字体缺失时必须停止。

## [2026-06-16] ingest | 成品油零售交易即开票政策解读
- Source: `raw/webpages/chinatax/chinatax-refined-oil-retail-transaction-invoice-2026.md` from 国家税务总局政策法规库.
- Adapter: `llm-wiki-ingest/adapters/web-clipping.md`
- Created: `_meta/extraction-notes/chinatax-refined-oil-retail-transaction-invoice-2026/` source profile, source inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/财税与经营财务/01-电商财税合规/09-成品油零售交易即开票规则.md`
- Updated: `domains/财税与经营财务/index.md`, `index.md`
- Notes: 将官方 Q&A 编译为发票合规与系统需求拆解 playbook，覆盖乐企自用/联用、交易/支付即开票、加油卡、现金/对公交易、换开、汇总开票和 2026-11-01 过渡期；执行前需复核最新税务机关口径。

## [2026-06-16] optimize | 成品油零售交易即开票入库记录按 Memory-First 规则补强
- Updated: `_meta/extraction-notes/chinatax-refined-oil-retail-transaction-invoice-2026/source-profile.md`
- Updated: `_meta/extraction-notes/chinatax-refined-oil-retail-transaction-invoice-2026/formal-page-plan.md`
- Updated: `_meta/extraction-notes/chinatax-refined-oil-retail-transaction-invoice-2026/audit-handoff.md`
- Notes: 根据新版 `llm-wiki-ingest` 的 Memory-First Placement And Fusion 约束，补充知识域分类、备选域判断、既有记忆搜索结果、`create-new` 融合处置、关联式融合说明和 audit handoff contract 字段；正式页路径和正文结构无需调整。

## [2026-06-17] compile | Skill 世界观
- Created: `domains/AI Agent工程/03-Skill设计/00-Skill世界观.md`
- Updated: `domains/AI Agent工程/index.md`
- Updated: `index.md`
- Notes: 沉淀 用户 对 skill 的上位理解：skill 是大模型执行复杂任务的说明书、定向知识库和可演化执行知识体；其结构应包含主线、节点、分支、工具/脚本、补丁、QA 和回主线机制，并明确 skill 与固定工作流的差异和组合关系。

## [2026-06-17] optimize | Skill 世界观补充测试原则
- Updated: `domains/AI Agent工程/03-Skill设计/00-Skill世界观.md`
- Notes: 增补 skill 测试世界观：区分设计会话冒烟测试、落盘验证、干净会话回归测试和问题回写，防止上下文污染与“对话中手动补救但未修改 SKILL.md”的假阳性。

## [2026-06-18] ingest | 电商运营与选品策略深度解析
- Source: `raw/transcripts/ecommerce-ops-selection-strategy-2026-06-18/transcript.md` and original docx archive.
- Adapter: `llm-wiki-ingest/adapters/transcript.md`.
- Created: `_meta/extraction-notes/ecommerce-ops-selection-strategy-2026-06-18/` source profile, segment plan, micro-segment plan, inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/电商运营/01-通用电商方法/04-选品与运营增长/` index and `01-电商运营与选品策略深度解析/` learning path with 5 formal pages.
- Updated: `domains/电商运营/index.md`, `index.md`.
- Notes: 将 171 分钟左右的噪声课程转写重构为主图诊断、卖点证据链、市场分层、选品库、AB/S款、运营助理三个月训练和 Agent 诊断模板；课堂组织和不可还原 ASR 噪声仅保留 raw。

## [2026-06-18] audit-patch | 电商运营与选品策略深度解析反浓缩补强
- Trigger: 用户 reminded that LLM Wiki ingest must not omit information and should enrich unclear source logic rather than condense it.
- Patched: `domains/电商运营/01-通用电商方法/04-选品与运营增长/01-电商运营与选品策略深度解析/01-主图诊断与卖点证据链.md` with 营销力 and 客户定义 sections.
- Patched: `02-市场分层与选品策略.md` with 免费搜索变少、付费占比、双率达标 and numeric anchors including 1000万-1500万, 150万, 5-10万/day, S款 10万+.
- Patched: `03-选品库与月度打款机制.md` with S/A/B 款分层、选品库体量、渠道数据、店铺基数、品类线完善度、费比 and 毛利率 logic.
- Patched: `04-运营助理三个月训练SOP.md` with annual SOP and operator/assistant responsibility split.
- Patched: `05-Agent使用模板：选品与运营增长诊断.md` with SKU price-combination and AI research-to-action checks.
- Updated: coverage matrix, knowledge-unit inventory, omission audit, and audit handoff with audit addendum.
- QA: placeholder scan remains `SHELL: 0`, `THIN: 0`, `OK: 7`; route audit target has no warnings.

## [2026-06-21] ingest | Loop Engineering 个人方法论
- Source: `raw/articles/loop-engineering-2026-06-21/loop-engineering-research-2026-06-21.md` from local research notes and current web/doc research on loop engineering, evaluator-optimizer, agent harnesses, Codex Goals, telemetry/eval loops, and token-cost risks.
- Adapter: `llm-wiki-ingest/adapters/web-clipping.md` plus `llm-wiki-ingest/adapters/unknown-source.md`.
- Created: `_meta/extraction-notes/loop-engineering-2026-06-21/` source profile, source inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/AI Agent工程/06-自动化工作流/index.md`.
- Created: `domains/AI Agent工程/06-自动化工作流/01-Loop Engineering个人方法论.md`.
- Created: `domains/AI Agent工程/06-自动化工作流/02-Loop项目规划模板.md`.
- Created: `queries/Loop项目启动入口.md`.
- Updated: `domains/AI Agent工程/index.md`, `index.md`.
- Notes: 将 用户已在使用的代码工具开发、DMP 竞品分析、聚宽策略优化三类循环统一抽象为“目标契约 -> 工作基座 -> 执行 -> 证据采集 -> 独立评审 -> 决策 -> 下一轮或停止 -> 总结入库”的个人 loop engineering 方法论；新增启动入口要求未来 Agent 先规划 loop 场景、证据面、轮数预算、停止条件和经验回写，再开始项目。
- Patch: 根据 用户 反馈补充范围规则，明确代码工具、DMP、电商运营、聚宽量化和视觉制作只是案例/线索，不限制知识库和方法论的使用范围；新领域仍按目标、证据、执行、评审、回流和停止条件抽象 loop。

## [2026-06-19] ingest | 聚宽 API 文档与策略写作 Skill
- Source: `raw/webpages/joinquant/joinquant-api-2026-06-19.md` and `raw/api/joinquant/joinquant-api-2026-06-19.md` from JoinQuant official API clipping.
- Adapter: `llm-wiki-ingest/adapters/web-clipping.md` plus `llm-wiki-ingest/adapters/api-docs.md`.
- Created: `_meta/extraction-notes/joinquant-api-2026-06-19/` source profile, source inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/量化交易/index.md`, `domains/量化交易/01-聚宽/index.md`, `01-聚宽策略写作与回测兼容规范.md`, `02-聚宽API能力地图.md`, `03-聚宽策略报错与排查.md`, and `queries/joinquant-strategy-agent-entry.md`.
- Created: Codex skill `/Users/pechen/.codex/skills/joinquant-strategy` with rules reference and static checker script.
- Updated: `SCHEMA.md`, `index.md`.
- Notes: 将聚宽 API 文档编译为“本地写策略后复制到聚宽回测”的执行层，覆盖策略生命周期、调度函数、真实价格、防未来函数、数据 API、交易 API、研究/回测环境边界和常见报错；详细期货/Tick/融资融券手册待真实策略需求触发后继续拆分。

## [2026-06-19] ingest | JoinQuant 凯利公式与量化仓位管理
- Source: `raw/webpages/joinquant/joinquant-kelly-position-sizing-2026-06-19.md` from JoinQuant 量化课堂 clipping.
- Adapter: `llm-wiki-ingest/adapters/web-clipping.md`.
- Created: `_meta/extraction-notes/joinquant-kelly-position-sizing-2026-06-19/` source profile, source inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/量化交易/02-策略风控与资金管理/index.md`.
- Created: `domains/量化交易/02-策略风控与资金管理/01-凯利公式与量化仓位管理.md`.
- Updated: `domains/量化交易/index.md`, `index.md`.
- Notes: 将凯利公式文章编译为量化仓位管理 playbook，覆盖赌博特殊公式、交易一般公式、股票信号到下注模型的转换、信号频率、杠杆折扣、黑天鹅与止损执行、可承受损失本金口径，以及年度高低点等错误强假设的审计。

## [2026-06-19] compile | 股票量化知识地图与社区策略入库框架
- Created: `domains/量化交易/00-股票量化知识地图.md`.
- Updated: `domains/量化交易/index.md`, `index.md`.
- Notes: 为后续聚宽社区策略入库建立股票量化知识槽位，覆盖市场与标的池、数据与特征、信号假设、组合构建、交易执行、风控资金管理、回测评估和工程可复现；明确社区 `.py` 策略应先原始保留、语义冻结、只增强 `HUMAN|`/`JQ_AUDIT|` 日志，经聚宽回测日志验证后再沉淀为策略卡、方法页、平台经验或评估样本。

## [2026-06-19] ingest | QMT四季发财v3 ETF轮动策略案例
- Source: `raw/quant-strategies/qmt-four-seasons-v3/` from local JoinQuant strategy workspace, r3 summary script, exported backtest summaries, transaction/position-derived analysis, and log completeness check.
- Adapter: `llm-wiki-ingest/adapters/markdown-doc.md` plus `llm-wiki-ingest/adapters/spreadsheet-report.md`.
- Created: `_meta/extraction-notes/qmt-four-seasons-v3/` source profile, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/量化交易/03-策略案例/index.md`.
- Created: `domains/量化交易/03-策略案例/01-QMT四季发财ETF轮动策略案例.md`.
- Created: `domains/量化交易/01-聚宽/04-聚宽社区策略取证与日志瘦身方法.md`.
- Updated: `domains/量化交易/index.md`, `domains/量化交易/01-聚宽/index.md`, `index.md`.
- Notes: 将 QMT四季发财v3 编译为可复用策略案例，覆盖 ETF 单标的轮动、长期动量稳定性得分、短期动量/RSI/ATR 风控、2020-2025 回测绩效、标的贡献、订单失败边界；同时沉淀 r3 summary-only 日志方法，明确收益/交易/持仓导出负责结果，`JQ_AUDIT` 只负责关键决策路径。

## [2026-06-19] audit-patch | QMT四季发财v3 策略规则反浓缩补强
- Patched: `domains/量化交易/03-策略案例/01-QMT四季发财ETF轮动策略案例.md`.
- Patched: `_meta/extraction-notes/qmt-four-seasons-v3/coverage-matrix.md`.
- Patched: `_meta/extraction-notes/qmt-four-seasons-v3/knowledge-unit-inventory.md`.
- Notes: 根据 用户 反馈补强策略页，新增实际 ETF 池、信号计算顺序、候选过滤顺序、买入策略、卖出策略、固定止损、ATR 止损、止盈边界、仓位资金管理、下单保护、已实现但未启用模块和复盘问题清单，避免知识页只保留绩效摘要。

## [2026-06-20] ingest | GitHub 量化理论资料与 ETF 策略研究方法
- Source: `raw/github/quant-theory-github-sources-2026-06-20/` from GitHub repositories including Alphalens, Pyfolio, Qlib, PyPortfolioOpt, ml4t/backtest, and purged-cross-validation.
- Adapter: `llm-wiki-ingest` web/GitHub source capture plus markdown formal compilation.
- Created: `_meta/extraction-notes/quant-theory-github-sources-2026-06-20/` source profile, source inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/量化交易/04-量化理论基础/` index plus five formal pages on 策略收益来源分解、选池/信号/组合构建、买卖器执行风控、策略评估归因、避免过拟合与回测陷阱.
- Updated: `domains/量化交易/index.md`, `index.md`.
- Notes: 将开源量化工具背后的方法论编译为 用户 ETF 策略研究主线：先验证动态 ETF 池和 alpha 信号，再优化买卖器；实验必须记录历史时点选池、成本前后、换手、分组收益、IC、参数搜索空间和样本外/滚动验证，避免人工预选 ETF 池和多重试验带来的回测幻觉。

## [2026-06-20] audit-patch | 量化理论基础从 ETF 研究提示升级为完整基础框架
- Trigger: 用户 指出上一版知识库过于粗糙，且不应只围绕 ETF，应先补完整量化基础知识。
- Source: `raw/github/quant-foundations-github-sources-2026-06-20/` with 12 shallow-cloned GitHub repositories: Zipline, Backtrader, bt, Alphalens, Pyfolio, Empyrical, ffn, PyPortfolioOpt, Riskfolio-Lib, Qlib, Machine Learning for Trading, and purged-cross-validation.
- Created: `_meta/extraction-notes/quant-foundations-github-sources-2026-06-20/` source profile, source inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Replaced: `domains/量化交易/04-量化理论基础/` old ETF-centered five-page structure with a 12-page quant foundations sequence covering market/assets, data/features, return/risk statistics, strategy hypotheses, alpha research, portfolio construction, execution/costs, backtesting, performance attribution, overfitting/leakage, and research workflow.
- Updated: `domains/量化交易/index.md`, root `index.md`, and `queries/joinquant-strategy-agent-entry.md`.
- QA: ingest contract OK; placeholder scan `SHELL:0 THIN:0 OK:13`; route audit target warnings none.
- Notes: 新结构把 ETF 轮动降级为策略类型中的一个案例，不再作为理论基础的中心；后续策略研究必须先明确市场资产、数据口径、信号假设、组合/仓位、执行成本、回测真实性和样本外验证。

## [2026-06-20] ingest | 市场状态识别、策略失效与状态自适应
- Source: `raw/github/regime-adaptation-sources-2026-06-20/`, `raw/articles/quant-regime-adaptation-2026-06-20/`, and `raw/papers/quant-regime-adaptation-2026-06-20/`.
- Adapter: `llm-wiki-ingest` with GitHub/Markdown and web clipping source handling.
- Created: `_meta/extraction-notes/regime-adaptation-sources-2026-06-20/` source profile, inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/量化交易/04-量化理论基础/13-市场状态识别与策略失效.md`.
- Created: `domains/量化交易/04-量化理论基础/14-状态自适应策略与动态资产配置.md`.
- Created: `domains/量化交易/04-量化理论基础/15-策略失效监控与滚动验证.md`.
- Updated: `domains/量化交易/04-量化理论基础/index.md`, `domains/量化交易/index.md`, `index.md`.
- Notes: 将固定策略在某些年份失效的问题从项目语境中抽离，编译为通用量化方法论，覆盖 HMM/GMM/KMeans/Jump Model、regime filter、strategy router、expert models、dynamic allocation、no-trade regime、现金替代资产、主评估周期和 walk-forward 验证纪律；MDPI 页面下载返回 403，记录为 unresolved，未作为正式来源。

## [2026-06-20] ingest | 达摩盘 AI 内部工具与竞品数据挖掘能力
- Source: `raw/data/dmp-ai-internal-tools-2026-06-20/DMP_AI_internal_tools.md` from local research document `/Users/pechen/AI/Research/DMP_AI_internal_tools.md`.
- Adapter: `llm-wiki-ingest/adapters/markdown-doc.md`.
- Created: `_meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/` source profile, source inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created: `domains/电商运营/02-淘宝天猫/04-达摩盘AI/index.md`.
- Created: `domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册.md`.
- Created: `queries/达摩盘AI竞品数据挖掘.md`.
- Updated: `domains/电商运营/index.md`, `domains/电商运营/02-淘宝天猫/index.md`, `domains/电商运营/02-淘宝天猫/02-淘宝营销工具/index.md`, `index.md`.
- Notes: 将 3627 行 DMP AI 内部工具研究文档完整保留到 raw，并在正式手册中嵌入完整原文结构，覆盖 `tool_item_benchmark_dataquery`、`tool_crowd_audience_insight`、`tool_e_commerce_crowd_advertising_dataquery`、`tool_sql_query` 等工具及 VIEW/DEEPLINK 数据资产；新增查询入口用于未来继续挖掘竞品销售、搜索词、推广和人群数据。

## [2026-06-22] compile | 主对话与干净子 Agent 的 Skill 回归测试方法
- Source: user-stated principles in Codex conversation on skill creation, false landing, context pollution, sub-agent validation, fork thread, and new thread tradeoffs.
- Created: `domains/AI Agent工程/03-Skill设计/index.md`.
- Created: `domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法.md`.
- Created: Codex skill `/Users/pechen/.codex/skills/skill-forward-test`.
- Updated: `domains/AI Agent工程/03-Skill设计/00-Skill世界观.md`, `domains/AI Agent工程/index.md`, `index.md`.
- Notes: 将 skill 验证框架沉淀为“主 Agent 设计/落盘 + 干净子 Agent 回归 + 失败分类回写 + 再验证”的闭环；明确 `spawn_agent` + `fork_context:false` 适合自动化干净验证，`create_thread` 适合可见测试，`fork_thread` 适合带上下文设计分支。
- QA: 使用干净子 Agent 回归 `skill-forward-test` 本身；首轮暴露“验证子 Agent 未必有 spawn 工具”和“skill 目录可能不在 git 仓库”两个缺口，已回写 fallback，并经第二轮干净子 Agent 验证通过。
- Patch: 将方法论从 Codex 专用表述泛化为跨 Agent 工具通用框架，补充 SealSeek/OpenClaw 和其他 Agent 工具的等价实现映射；将活跃 Skill 设计页面中的个人姓名表述改为中性表述，并将 Skill 世界观页面改为中性文件名。

## [2026-06-22] ingest | 达摩盘 AI 对话挖掘竞品数据案例
- Source: local DMP AI prompt manual, full-dimension workflow, and clean run evidence summary for base base item `{BASE_ITEM_ID}`.
- Adapter: `llm-wiki-ingest/adapters/markdown-doc.md`.
- Created: `raw/data/dmp-ai-dialogue-case-product-id-template-2026-06-22/` with prompt manual, workflow copy, and case evidence summary.
- Created: `_meta/extraction-notes/dmp-ai-dialogue-case-product-id-template-2026-06-22/` source profile, coverage matrix, and audit handoff.
- Created: `domains/电商运营/02-淘宝天猫/04-达摩盘AI/02-达摩盘AI对话挖掘竞品数据案例.md`.
- Updated: `domains/电商运营/02-淘宝天猫/04-达摩盘AI/index.md`, `index.md`.
- Notes: 将“通过 DMP AI 对话挖掘前台不可见数据”的方法沉淀为案例，按提问目录、提示词、预期数据和案例结果组织，覆盖主体识别、竞品发现、关系验证、同行经营/推广精确数据、免费流量 SQL、竞品区间、人群画像、VIEW 流转、成功路径、店铺竞争和下载限制；同时保留“获取到维度不等于全量落盘”的 QA 规则。

## [2026-06-22] compile | 卖点转炸点方法
- Source: Codex conversation analyzing 麦拉贝拉“可以吃的哈衣”提示词 and applying it to a phone shooting stand main image.
- Created: `domains/视觉制作/01-电商视觉基础/03-卖点转炸点方法.md`.
- Updated: `domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用.md`, `domains/视觉制作/01-电商视觉基础/02-电商图片营销策划与AI生图Playbook.md`, `domains/视觉制作/01-电商视觉基础/index.md`, `queries/ecommerce-image-marketing-planning.md`, `index.md`.
- Notes: 将“产品事实 -> 用户痛点场景 -> 行业同质化表达 -> 可感知结果 -> 心智钩子”沉淀为主图爆点方法，收录麦拉贝拉儿童哈衣和手机拍摄支架两个案例，并补充真实性、场景感、传播性和合规边界 QA。

## 2026-06-24

- 更新 `domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践/04-图片工作流：提示词结构与参考控制.md`：新增“产品参考图保真：不要把视觉识别结果写成产品重绘提示词”。沉淀包袋详情页生图案例：Skill 自动把“正面两颗黑色磁扣”等视觉识别结果写进 Prompt，导致模型按文字重构商品。新增规则：产品细节只用于内部识别，进入生图 Prompt 的应是“以参考图为准、不新增、不删减、不移动”的锁定规则。

## 2026-06-24

- 更新 `domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/`：将“产品视觉识别结果不能直接写进生图 Prompt，应转换为参考图锁定规则”的经验沉淀到无限画板 Skill 写作知识库。涉及文件：`05-常见反坑库.md` 新增“把产品视觉识别结果写进生图 Prompt”反坑；`04-Prompt模板.md` 新增“产品细节锁定模板”；`06-质量检查清单.md` 新增产品识别信息与 Prompt 锁定规则检查项；`index.md` 增加入口提醒。

## [2026-06-25] ingest | 白泽阿里巴巴国际站运营实战系统课前 4 章

- Source: `/Users/pechen/alibaba/白泽/` 4 个本地 MP4 视频。
- Adapter: `llm-wiki-ingest/adapters/transcript.md` with video keyframe/OCR supplement.
- Installed: Homebrew `whisper-cpp`; downloaded `ggml-large-v3-turbo.bin` to `/Users/pechen/.local/share/whisper.cpp/models/`.
- Created raw archive: `raw/videos/baize-alibaba-international-station-course-2026-06-25/`.
- Created raw transcripts: `raw/transcripts/baize-alibaba-international-station-course-2026-06-25/`.
- Created raw keyframes: `raw/assets/baize-alibaba-international-station-course-2026-06-25/`.
- Created extraction notes: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/`.
- Created formal pages: `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/` index plus 国际站运营能力框架、运营思维框架与跨行业迁移、运营实战技能迭代方法。
- Created query entry: `queries/阿里巴巴国际站运营诊断.md`.
- Notes: 将前 4 章课程从视频转写和关键帧 OCR 编译为国际站运营能力框架，保留平台规则、指标概念、流量/买家思维、实战应用、成功案例打造、自主学习、学习渠道、测试模型和复盘复制。ASR 明显误听如 `循环量`、`万物首页`、`学习局道` 已在 extraction notes 中记录并校正；`奥义加`、`报品/报增` 保留为待确认。

## [2026-06-25] ingest | 白泽阿里巴巴国际站运营实战系统课第 5 章

- Source: `/Users/pechen/alibaba/白泽/5_这章节你将会获得哪些技能-_ev.mp4`.
- Adapter: `llm-wiki-ingest/adapters/transcript.md` with video keyframe/OCR supplement.
- Updated raw archive: `raw/videos/baize-alibaba-international-station-course-2026-06-25/`.
- Created raw transcript: `raw/transcripts/baize-alibaba-international-station-course-2026-06-25/ch05-whisper-large-v3-turbo-prompted.raw.*`.
- Created raw keyframes/OCR: `raw/assets/baize-alibaba-international-station-course-2026-06-25/ch05/keyframes/`.
- Updated extraction notes: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/` plus `ch05/` chapter coverage.
- Created formal page: `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/04-店铺基础技能学习与知识体系梳理.md`.
- Updated: course index, cross-border/domain/root indexes, query entry, coverage matrix, omission audit, and audit handoff.
- Notes: CH05 是“店铺基础技能学习”导入章，核心知识是区分新手学习迷茫与老运营知识体系混乱，把运营知识从听课/收藏转为店铺动作、指标结果、复盘经验和可迁移技能。ASR 质量高；OCR 可确认封面和课程承诺，但字幕存在错字，已作为 raw-only/merged 处理。

## [2026-06-25] ingest | 白泽阿里巴巴国际站运营实战系统课第 6-9 章

- Source: `/Users/pechen/alibaba/白泽/6_1学习前-做好这3件事-1天就能入门_ev.mp4`, `/Users/pechen/alibaba/白泽/7_210个关键词构建成独立的运营系统_ev.mp4`, `/Users/pechen/alibaba/白泽/8_3PC和APP首页介绍_ev.mp4`, `/Users/pechen/alibaba/白泽/9_4店铺SEO巧布局-让流量更精准_ev.mp4`.
- Adapter: `llm-wiki-ingest/adapters/transcript.md` with video keyframe/OCR supplement.
- Updated raw archive: `raw/videos/baize-alibaba-international-station-course-2026-06-25/`.
- Created raw transcripts: `raw/transcripts/baize-alibaba-international-station-course-2026-06-25/ch06-...` through `ch09-...`.
- Created raw keyframes/OCR: `raw/assets/baize-alibaba-international-station-course-2026-06-25/ch06/` through `ch09/`.
- Updated extraction notes: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/` plus chapter-level `ch06/` through `ch09/` segment, coverage, and omission files.
- Updated formal page: `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/04-店铺基础技能学习与知识体系梳理.md`.
- Created formal pages: `05-国际站后台十关键词运营系统.md`, `06-国际站首页流量入口地图.md`, `07-店铺SEO基础布局.md`.
- Updated: course index, cross-border/domain/root indexes, query entry, coverage matrix, omission audit, formal plan, source inventory, audit handoff.
- Notes: CH06 将“入门”落为后台问号概念、板块关联、板块位置三件事；CH07 用店铺、产品、客户、内容、营销、数据、商机、订单、资金、物流构建后台系统；CH08 把 PC 首页产品入口、制造商入口、榜单、新品、汇采购和场景入口整理为流量地图；CH09 把标题核心词、长尾词、关键词相关性、属性详情页、店铺层级、页面布局、更新和基础资料整理为店铺 SEO 检查法。

## [2026-06-25] ingest | 白泽阿里巴巴国际站运营实战系统课第 10-19 章

- Source: `/Users/pechen/alibaba/白泽/10_学习这章节你将掌握平台规则-构建个人运营框架_ev.mp4` through `/Users/pechen/alibaba/白泽/19_9怎样提升单品权重-_ev.mp4`.
- Adapter: `llm-wiki-ingest/adapters/transcript.md` with video keyframe/OCR supplement.
- Updated raw archive: `raw/videos/baize-alibaba-international-station-course-2026-06-25/`.
- Created raw transcripts: `raw/transcripts/baize-alibaba-international-station-course-2026-06-25/ch10-...` through `ch19-...`.
- Created raw keyframes/OCR: `raw/assets/baize-alibaba-international-station-course-2026-06-25/ch10/` through `ch19/`.
- Updated extraction notes: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/` plus chapter-level `ch10/` through `ch19/` segment, coverage, and omission files.
- Created formal pages: `08-平台规则与搜索排序机制.md`, `09-店铺综合实力与搜索排名指标.md`, `10-买家喜好度与千人千面标签匹配.md`, `11-一级引擎与橱窗搜索加权.md`, `12-店铺权重与单品权重提升.md`.
- Updated: course index, cross-border/domain/root indexes, query entry, coverage matrix, omission audit, formal plan, source inventory, audit handoff.
- Notes: CH10-CH19 构成搜索规则模块，覆盖买家导向、严惩作弊、模糊匹配、类目/文本相关性、供应商信息、店铺综合实力、买家喜好度、千人千面、一级/二级引擎、橱窗加权、更多产品曝光机会、店铺权重和单品权重。ASR 明显误听如 `一起引擎`、`汝窗/除窗`、`顶掌/顶站`、`Pap`、`循环率` 已在 extraction notes 中校正为 `一级引擎`、`橱窗`、`顶展`、`P4P`、`询盘率`。

## [2026-06-25] ingest | 白泽阿里巴巴国际站运营实战系统课第 20-29 章

- Source: `/Users/pechen/alibaba/白泽/20_10避坑！违规处罚规则_ev.mp4` through `/Users/pechen/alibaba/白泽/29_9精细化产品线布局+直通车推广策略-全面提升流量_ev.mp4`.
- Adapter: `llm-wiki-ingest/adapters/transcript.md` with video keyframe/OCR supplement.
- Updated raw archive: `raw/videos/baize-alibaba-international-station-course-2026-06-25/`.
- Created raw transcripts: `raw/transcripts/baize-alibaba-international-station-course-2026-06-25/ch20-...` through `ch29-...`.
- Created raw keyframes/OCR: `raw/assets/baize-alibaba-international-station-course-2026-06-25/ch20/` through `ch29/`.
- Updated extraction notes: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/` plus chapter-level `ch20/` through `ch29/` segment, coverage, and omission files.
- Created formal pages: `13-违规处罚与店铺运营风控.md`, `14-店铺规划与定位方法.md`, `15-赛道选择与四大流量入口.md`, `16-主打产品切入与产品线布局.md`, `17-目标国家与买家画像分析.md`, `18-公司优势表达与信任转化.md`, `19-出口通与金品店铺应用.md`.
- Updated: course index, cross-border/domain/root indexes, query entry, coverage matrix, omission audit, formal plan, source inventory, source profile, knowledge-unit inventory, and audit handoff.
- Notes: CH20-CH29 构成店铺规划与定位模块，覆盖违规处罚风控、五维店铺定位、四大流量入口、贸易型/工厂型主打产品选择、目标国家、买家画像、公司优势表达、出口通与金品店铺、精细化产品线和直通车单点突破。ASR 明显误听如 `清权`、`现全`、`寻盘/巡盘/循环`、`内幕/类幕`、`自动车/直动车`、`搭贴时/搭贴室`、`半拖`、`NOQ`、`新品/精品店铺` 已在 extraction notes 中校正为 `侵权`、`限权`、`询盘`、`类目`、`直通车`、`RTS`、`半托管`、`MOQ`、`金品店铺`。

## [2026-06-25] ingest | 山峰组253期6-14课程：淘宝付费投放与全站推广

- Source: `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-14 253期.md`.
- Source identity: 山峰组253期6-14课程.
- Adapter: `llm-wiki-ingest/adapters/transcript.md`.
- Created raw transcript: `raw/transcripts/shanfeng-253-taobao-paid-traffic-course-2026-06-14/transcript.md`.
- Created extraction notes: `_meta/extraction-notes/shanfeng-253-taobao-paid-traffic-course-2026-06-14/` with source profile, segment plan, micro-segment plan, knowledge inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created formal pages: `domains/电商运营/02-淘宝天猫/05-淘宝付费投放与全站推广/` index plus 全站推广打款放量流程、链接发散与人群素材测试、拉新收割与短视频内容配合、Agent 使用模板。
- Created query entry: `queries/淘宝全站推广诊断.md`.
- Updated: `domains/电商运营/02-淘宝天猫/index.md`, `domains/电商运营/index.md`, `index.md`.
- Notes: 将课程中的 23 个知识单元完整覆盖，保留多链接发散、前期成交打标、最大化到目标投产切换、预算和 ROI 阶梯、8-24 小时观察、搜索占比 20%-30%、计划效率复盘、拉新收割配合、短视频前三秒与人群排除、A/B/C 款梯队和 AI/COC 标准化等锚点。ASR 不确定工具名仅保留业务逻辑并标注需后台复核。

## [2026-06-25] ingest | 山峰组256期6-15课程：产品类型与爆款运营系统

- Source: `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-15 256期2.md`, `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-15 256期3.md`, `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-15 256期.md`.
- Source identity: 山峰组256期6-15课程.
- Adapter: `llm-wiki-ingest/adapters/transcript.md` batch course compile.
- Created raw transcript batch: `raw/transcripts/shanfeng-256-ecommerce-product-operations-course-2026-06-15/`.
- Created extraction notes: `_meta/extraction-notes/shanfeng-256-ecommerce-product-operations-course-2026-06-15/` with source profile, source inventory, course reconstruction, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created formal pages: `domains/电商运营/01-通用电商方法/04-选品与运营增长/02-产品类型与爆款运营系统/` index plus 经营定位与核心优势、产品类型与行业模型、产品生命周期与阶段指标、爆款递增与数据化放大、ToB定制与高客单信任业务、电锅炉壁挂炉店铺执行案例、Agent 使用模板。
- Created query entry: `queries/产品类型与爆款运营诊断.md`.
- Updated: `domains/电商运营/01-通用电商方法/04-选品与运营增长/index.md`, `domains/电商运营/01-通用电商方法/index.md`, `domains/电商运营/index.md`, `index.md`.
- Notes: 将三段课程重构为“企业优势 -> 产品类型 -> 行业结构 -> 生命周期阶段 -> 指标选择 -> 流量端口 -> 组织执行 -> 复盘迭代”模型，覆盖 41 个知识单元，保留标品/非标/半标、高频/低频/高客单/ToB、销量寡头/搜索寡头/动销趋势型、S/A/B 产品分层、20%-30% 日预算递增、客服 10 秒/14 秒响应、Top20/Top10 竞品复制、主图 30%/70% 测试、趋势低谷前 45 天启动和 6/18-8/15 行动节奏等锚点。

## [2026-06-26] query | 旺店通 API 知识检索

- Query: 找一下 wiki 知识库中关于旺店通 API 部分的知识。
- Read: `SCHEMA.md`, `index.md`, `queries/wangdian-api-skill-creation.md`, `domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/` core pages and manual outlines.
- Filed: no new query page; existing `queries/wangdian-api-skill-creation.md` already covers the recurring entry route.

## [2026-06-26] audit | 白泽阿里巴巴国际站运营实战系统课第 20-29 章复检

- Skill: `llm-wiki-audit-and-optimization`.
- Target: `domains/电商运营/20-跨境电商/02-阿里巴巴国际站运营实战系统课/` and `queries/阿里巴巴国际站运营诊断.md`.
- QA: placeholder scan `SHELL:0 THIN:0 OK:20`; ingest contract OK; Obsidian route audit shows course index 3 backlinks / 22 outgoing links and query entry 14 backlinks / 19 outgoing links, with no target warnings.
- Fixed: aligned CH20 chapter-level coverage and knowledge-unit inventory with main coverage by splitting complaint risk, TRO risk, penalty ladder, and rule-learning units through `BZ-CH20-U06`.
- Notes: full source path existence check returned `missing_sources 0`; formal source-unit references all exist in main coverage. Root `index.md` formal-page count appears stale relative to current raw file count, but this is a wiki-wide indexing hygiene issue outside the Baize course path.

## [2026-06-26] ingest | 白泽阿里巴巴国际站运营实战系统课第 30-39 章

- Source: `/Users/pechen/alibaba/白泽/30_10店铺规划怎么做-3个阶段快速实现询盘目标_ev.mp4` through `/Users/pechen/alibaba/白泽/39_1什么是关键词-怎样确定词根-关键词覆盖率100%_ev.mp4`.
- Adapter: `llm-wiki-ingest/adapters/transcript.md` with video keyframe/OCR supplement.
- Updated raw archive: `raw/videos/baize-alibaba-international-station-course-2026-06-25/`.
- Created raw transcripts: `raw/transcripts/baize-alibaba-international-station-course-2026-06-25/ch30-...` through `ch39-...`.
- Created raw keyframes/OCR: `raw/assets/baize-alibaba-international-station-course-2026-06-25/ch30/` through `ch39/`.
- Updated extraction notes: `_meta/extraction-notes/baize-alibaba-international-station-course-2026-06-25/` plus chapter-level `ch30/` through `ch39/` segment, coverage, and omission files.
- Created formal pages: `20-三阶段店铺规划与第二曲线增长.md`, `21-RTS与定制店铺差异化运营.md`, `22-国际站选品价值与爆品思路.md`, `23-关键词趋势选品与涨幅词选品.md`, `24-对标同行选品与市场参谋爆品案例.md`, `25-关键词词根与覆盖率.md`.
- Updated: course index, cross-border/domain/root indexes, query entry, coverage matrix, omission audit, formal plan, source inventory, source profile, knowledge-unit inventory, and audit handoff.
- QA: raw completeness `missing_raw 0`; strict placeholder scan `STRICT_PLACEHOLDER_ISSUES 0`; ingest contract OK with expected verbatim-match warnings; Obsidian route audit shows course index 3 backlinks / 28 outgoing links and query entry 14 backlinks / 25 outgoing links, with no target warnings.
- Notes: CH30-CH39 cover second-curve store planning, RTS/custom differentiated operations, product-selection value, onion-path product selection, keyword trend selection, rising-keyword selection, peer-store borrowing, Market Advisor product-country-keyword case workflow, order closed loop, and keyword-root coverage. ASR corrections include `寻盘/光盘/熏` -> `询盘`, `铁齿` -> `RTS`, `自动车/直动车` -> `直通车`, `热池榜` -> `热词榜`, `内幕` -> `类目`, `池根` -> `词根`, `词操` -> `实操`.

## [2026-06-26] ingest | 山峰组259期6-15/6-16课程：淘宝智能推广与人群运营系统

- Source: `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-15 259期.md`, `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-16 259期.md`.
- Source identity: 山峰组259期6-15/6-16课程.
- Adapter: `llm-wiki-ingest/adapters/transcript.md` batch course compile.
- Created raw transcript batch: `raw/transcripts/shanfeng-259-taobao-smart-promotion-audience-operations-course-2026-06-15-16/`.
- Created extraction notes: `_meta/extraction-notes/shanfeng-259-taobao-smart-promotion-audience-operations-course-2026-06-15-16/` with source profile, source inventory, course reconstruction, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created formal pages: `domains/电商运营/02-淘宝天猫/06-淘宝智能推广与人群运营系统/` index plus 淘宝运营趋势与增长底层逻辑、店铺模型与新老客增长结构、人群资产与计划健康诊断、转化周期归因与流量渠道选择、标准计划智能计划与出价模型、搜索卡位流量金卡与活动资源、测图测款动销与低价引流计划、相似品跟投竞品分析与人群推广、推广空烧互抢与报表优化、Agent 使用模板。
- Created query entry: `queries/淘宝智能推广与人群运营诊断.md`.
- Updated: `domains/电商运营/02-淘宝天猫/index.md`, `domains/电商运营/index.md`, `index.md`.
- Notes: 将两份转文字重构为“平台趋势 -> 店铺模型 -> 产品转化周期 -> 人群资产 -> 流量渠道 -> 计划类型 -> 指标归因 -> 放量/纠偏”模型，覆盖 63 个知识单元，保留 721/172/333/127 店铺模型、O/A/I/P/L 人群流转、成交机会、人群流转效率、TA 人群浓度、计划人群浓度、双高人群、搜索曝光价值、转化周期归因、标准/智能计划、低出高溢、搜索卡位、流量金卡、测图测款动销、相似品跟投、人群推广、空烧和互抢诊断等锚点。后台字段名或口播中不确定的英文缩写已在 extraction notes 中标注待复核。

## [2026-06-26] ingest | 18期品牌课转写查漏补缺

- Source: `/Users/pechen/知识库/18期品牌/18期-D1 天蓬_原文.md`, `/Users/pechen/知识库/18期品牌/18期 D2太白-1_原文.md`, `/Users/pechen/知识库/18期品牌/18期D2太白_原文.md`, `/Users/pechen/知识库/18期品牌/18期品牌D3赤壁_原文.md`, `/Users/pechen/知识库/18期品牌/D3魔布_原文.md`, `/Users/pechen/知识库/18期品牌/D4上午AKEN_原文.md`, `/Users/pechen/知识库/18期品牌/D4-奥利可_原文.md`.
- Adapter: `llm-wiki-ingest/adapters/transcript.md`.
- Created raw transcript archive: `raw/transcripts/brand-class-18-gap-fill-2026-06-26/`.
- Created extraction notes: `_meta/extraction-notes/brand-class-18-gap-fill-2026-06-26/` with source profile, source inventory, knowledge-unit inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created formal pages: `08-定位配称四模块`, `10-内容营销资产化与内容中台`, `11-AI时代品牌专属视觉体系`, plus case pages `17-稳健医疗`, `18-巴厘高`, `19-良品铺子与李宁`, `20-蕉内与朱砂饰品`.
- Updated: `domains/品牌策略/index.md`, relevant brand sub-indexes, `domains/品牌策略/90-样本/index.md`, and root `index.md`.
- Notes: 本次按“查漏补缺”处理，不重建平行课程包；主要补定位配称、内容中台、AI 时代专属视觉体系和四个可调用案例。平台人群 taxonomy 和年度预算倒推细节因需后台/PDF 复核，保留 raw-only。

## [2026-06-26] ingest | 山峰组研修4班6-23/6-24课程：产品开发与供应链管理系统

- Source: `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-23 研修4班.md`, `/Users/pechen/知识库/6月山峰组课程录音文件/2026-06-24 研修4班.md`.
- Source identity: 山峰组研修4班6-23/6-24课程.
- Adapter: `llm-wiki-ingest/adapters/transcript.md` batch course compile.
- Created raw transcript batch: `raw/transcripts/shanfeng-yanxiu4-product-development-supply-chain-course-2026-06-23-24/`.
- Created extraction notes: `_meta/extraction-notes/shanfeng-yanxiu4-product-development-supply-chain-course-2026-06-23-24/` with source profile, source inventory, coverage matrix, omission audit, formal page plan, and audit handoff.
- Created formal pages: `domains/电商运营/01-通用电商方法/05-产品开发与供应链管理系统/` index plus 产品开发思维与市场机会判断、供应商开发与分级管理、供应商谈判打样与品质管理、成本结构利润模型与SKU角色、库存周转补货与跨部门协同、Agent 使用模板。
- Created query entry: `queries/产品开发与供应链管理诊断.md`.
- Updated: `domains/电商运营/01-通用电商方法/index.md`, `domains/电商运营/index.md`, `index.md`.
- Notes: 将两份研修4班课程重构为“竞争困局 -> 产品开发思维 -> 市场机会判断 -> 供应商开发与分级 -> 谈判打样品质 -> 成本穿透与 SKU 角色 -> 库存周转、补货与部门协同”模型，覆盖 65 个知识单元，保留产品是 1、五大产品开发原则、机会四象限、供应链四能力、灭火器箱净亏 8%、供应商开发七步、评估八维、战略/核心/合格/临时分级、四大谈判维度、OEM/ODM/自有品牌、净利模型、SKU 角色、爆款库存 70%-80%、动销补 15 天、7/14/21 天补货阈值、睡袋 8 个月生产周期、退货未入库导致重复采购等锚点。CUC 工具和课程提到的完整表格字段因源文件未给出细项，保留为待后续补充。

## [2026-06-26] update | 量化交易知识库拆分

- Moved active quant-trading wiki content to separate private Obsidian/Git repository: `/Users/pechen/quant-trading-wiki`.
- New GitHub repository: `petercjl/quant-trading-wiki` (private).
- Removed current-version quant-trading formal pages, raw quant/API/source files, extraction notes, and JoinQuant query entry from this general wiki.
- Updated routing rules in `/Users/pechen/.codex/AGENTS.md`, `AGENTS.md`, `SCHEMA.md`, and `index.md`.
- Note: original GitHub history is intentionally left untouched; old commits may still contain quant-trading records.
