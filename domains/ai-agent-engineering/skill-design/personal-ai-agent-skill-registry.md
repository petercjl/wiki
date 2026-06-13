---
title: 个人/项目 Skill 注册库
type: concept
created: 2026-06-12
updated: 2026-06-12
domain: ai-agent-engineering
tags: [ai-agent, skill, registry, personal, project]
sources:
  - /Users/pechen/.codex/skills
  - /Users/pechen/.hermes/skills
  - /Users/pechen/.agents/skills
  - /Users/pechen/.openclaw/workspace/skills
  - /Users/pechen/.sealseek/skill_pool
  - /Users/pechen/.sealseek/workspace/skills
  - /Users/pechen/.sealseek/workspaces/default/skills
  - /Users/pechen/.sealseek/workspaces/default/active_skills
  - /Users/pechen/.sealseek/workspaces/default/customized_skills
  - /Users/pechen/.sealseek/backups
  - /Users/pechen/sealseek
  - /Users/pechen/hermes/xc-sealseek-aicoding-skill
  - /Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak
status: active
---
# 个人/项目 Skill 注册库

本页只收录 Peter 自己创建、让 Agent 为项目定制、或明显服务于 Peter 项目/业务流程的 skill。它是日常检索“以前有没有做过类似 skill”的优先入口。

不收录 Codex/Claude/Lark/SealSeek 等 Agent 的系统内置 skill、底层工具 skill、运行时副本和备份条目；这些仍保留在 [[domains/ai-agent-engineering/skill-design/ai-agent-skill-registry|跨 Agent Skill 注册库]]。

当前个人/项目 skill 数量：153。

## 分类规则

- Codex 非 `.system` 本地 skill：视为个人/项目自定义。
- OpenClaw workspace skill：视为项目自定义。
- SealSeek workspace/default/customized/standalone/migration skill：视为个人/项目自定义；`skill_pool` 和 `active_skills` 不进入本页。
- Hermes skill：命中 Peter 项目、电商、视觉、课程、LLM Wiki、Sealseek/OpenClaw/玺承等关键词时进入本页；否则归入通用安装/不确定。
- Claude Code 官方 marketplace、Codex `.system`、Lark 通用工具 skill：作为系统/底层能力，只在全量库中保留。

## Agent 快速索引

### Codex

- `ai-agent-skill-registry-sync` (local)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wik… 位置：`/Users/pechen/.codex/skills/ai-agent-skill-registry-sync/SKILL.md`
- `brand-planning-report` (local)：Generate a user-facing ecommerce brand planning HTML report from a standard 店铺商品 Excel workbook, using Peter's brand-strategy LLM Wiki for p… 位置：`/Users/pechen/.codex/skills/brand-planning-report/SKILL.md`
- `course-deck-factory` (local)：Build editable course slide decks from a standardized deck spec using Node.js, PptxGenJS, local fonts, structured page types, and a mixed vi… 位置：`/Users/pechen/.codex/skills/course-deck-factory/SKILL.md`
- `ecommerce-profit-statement-automation` (local)：Automate ecommerce platform profit statement workbooks from settlement/funds/account bills. Use when the user wants to turn Taobao or other … 位置：`/Users/pechen/.codex/skills/ecommerce-profit-statement-automation/SKILL.md`
- `image-detail-page` (local)：根据产品白底图和品类，全自动推断模型、人群、风格，并一站式生成13个策划文件及对应电商图片。 当用户提到主图详情页、电商策划、白底图出方案、主图设计、详情页设计、电商视觉方案时触发。 位置：`/Users/pechen/.codex/skills/image-detail-page/SKILL.md`
- `internal-plugin-workflow` (local)：Use when the user wants to build or iterate an internal Chrome browser extension against a page they have already opened, especially when th… 位置：`/Users/pechen/.codex/skills/internal-plugin-workflow/SKILL.md`
- `llm-wiki` (local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and li… 位置：`/Users/pechen/.codex/skills/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answe… 位置：`/Users/pechen/.codex/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `llm-wiki-ingest` (local)：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, includin… 位置：`/Users/pechen/.codex/skills/llm-wiki-ingest/SKILL.md`
- `llm-wiki-recompile-runner` (local)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages,… 位置：`/Users/pechen/.codex/skills/llm-wiki-recompile-runner/SKILL.md`
- `seedance-commerce-video` (local)：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selli… 位置：`/Users/pechen/.codex/skills/seedance-commerce-video/SKILL.md`
- `shop-product-diagnosis` (local)：Diagnose an ecommerce shop from a standard 店铺商品 Excel workbook and produce a tabbed HTML report plus an XMind action map. Use when Codex rec… 位置：`/Users/pechen/.codex/skills/shop-product-diagnosis/SKILL.md`
- `yuce-product-list-export` (local)：Use when the user wants to export 行情高手/预策平台 “商品列表” data after they have already logged in and manually navigated to the target report page. … 位置：`/Users/pechen/.codex/skills/yuce-product-list-export/SKILL.md`

### Hermes

- `baoyu-article-illustrator` (local)：Article illustrations: type × style × palette consistency. 位置：`/Users/pechen/.hermes/skills/creative/baoyu-article-illustrator/SKILL.md`
- `baoyu-comic` (local)：Knowledge comics (知识漫画): educational, biography, tutorial. 位置：`/Users/pechen/.hermes/skills/creative/baoyu-comic/SKILL.md`
- `baoyu-infographic` (local)：Infographics: 21 layouts x 21 styles (信息图, 可视化). 位置：`/Users/pechen/.hermes/skills/creative/baoyu-infographic/SKILL.md`
- `ecommerce-image-skill-architecture` (local)：Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use when designing or ref… 位置：`/Users/pechen/.hermes/skills/creative/ecommerce-image-skill-architecture/SKILL.md`
- `evolink-gpt-image-2` (local)：Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and test script locations… 位置：`/Users/pechen/.hermes/skills/creative/evolink-gpt-image-2/SKILL.md`
- `gpt-image-2-12api` (local)：Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavior, reproducible prob… 位置：`/Users/pechen/.hermes/skills/creative/gpt-image-2-12api/SKILL.md`
- `gpt生图` (local)：Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, design, or produce any… 位置：`/Users/pechen/.hermes/skills/creative/gpt生图/SKILL.md`
- `shopping-basket-visual-planning` (local)：Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the user needs to know what… 位置：`/Users/pechen/.hermes/skills/creative/shopping-basket-visual-planning/SKILL.md`
- `single-image-optimization` (local)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimiz… 位置：`/Users/pechen/.hermes/skills/creative/single-image-optimization/SKILL.md`
- `taobao-gpt-image-creative-main-image` (local)：Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably via post-processing … 位置：`/Users/pechen/.hermes/skills/creative/taobao-gpt-image-creative-main-image/SKILL.md`
- `toapis-gpt-image-2` (local)：Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working request formats, task pol… 位置：`/Users/pechen/.hermes/skills/creative/toapis-gpt-image-2/SKILL.md`
- `conference-static-html-courseware-review-loop` (local)：Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review, Git-backed iteratio… 位置：`/Users/pechen/.hermes/skills/productivity/conference-static-html-courseware-review-loop/SKILL.md`
- `course-html-ppt-16x9-image-pages` (local)：Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy slide layouts. 位置：`/Users/pechen/.hermes/skills/productivity/course-html-ppt-16x9-image-pages/SKILL.md`
- `douyin-link-to-knowledge` (local)：Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transc… 位置：`/Users/pechen/.hermes/skills/productivity/douyin-link-to-knowledge/SKILL.md`
- `dual-source-chapterized-html-ppt-courseware` (local)：Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to avoid renumbering casc… 位置：`/Users/pechen/.hermes/skills/productivity/dual-source-chapterized-html-ppt-courseware/SKILL.md`
- `ecommerce-bi-operation-skill-planning` (local)：Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡检 SOPs, priority eng… 位置：`/Users/pechen/.hermes/skills/productivity/ecommerce-bi-operation-skill-planning/SKILL.md`
- `feishu-cli-isolated-config` (local)：Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentials; use an isolated … 位置：`/Users/pechen/.hermes/skills/productivity/feishu-cli-isolated-config/SKILL.md`
- `feishu-product-feature-doc` (local)：Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-oriented copy, callouts, … 位置：`/Users/pechen/.hermes/skills/productivity/feishu-product-feature-doc/SKILL.md`
- `goal-driven-daily-report-templates` (local)：Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use when Peter asks to desi… 位置：`/Users/pechen/.hermes/skills/productivity/goal-driven-daily-report-templates/SKILL.md`
- `hermes-feishu-gateway-setup` (local)：Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credentials; use isolated FEIS… 位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-gateway-setup/SKILL.md`
- `hermes-feishu-session-debugging` (local)：Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session JSON files, and tool… 位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-session-debugging/SKILL.md`
- `html-ppt-conference-review-loop` (local)：Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with explicit readability a… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-conference-review-loop/SKILL.md`
- `html-ppt-course-deck` (local)：Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid or visually weak. Use… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-course-deck/SKILL.md`
- `html-ppt-font-standardization` (local)：Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run an overflow audit af… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-font-standardization/SKILL.md`
- `html-ppt-screenshot-review-loop` (local)：Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-style decks where rea… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-screenshot-review-loop/SKILL.md`
- `html-ppt-stage-fit-and-background-cleanup` (local)：Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds with clean backgrounds … 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-stage-fit-and-background-cleanup/SKILL.md`
- `html-ppt` (local)：HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by templates. Use when t… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-studio-agentskill/SKILL.md`
- `macos-wechat-cli` (local)：Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to install or troubleshoot… 位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-cli/SKILL.md`
- `macos-wechat-history-decrypt` (local)：Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process existing WeChat chat hi… 位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-history-decrypt/SKILL.md`
- `official-lark-cli-feishu-workflows` (local)：Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenClaw setup already uses… 位置：`/Users/pechen/.hermes/skills/productivity/official-lark-cli-feishu-workflows/SKILL.md`
- `real-chrome-web-reader` (local)：使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。 位置：`/Users/pechen/.hermes/skills/productivity/real-chrome-web-reader/SKILL.md`
- `reduce-paid-ratio-link-agent-mvp` (local)：Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for close, reduce, keep, … 位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-link-agent-mvp/SKILL.md`
- `reduce-paid-ratio-plan-evaluator` (local)：Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from two source reports, th… 位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-plan-evaluator/SKILL.md`
- `review-driven-static-html-courseware` (local)：Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML-native presentation… 位置：`/Users/pechen/.hermes/skills/productivity/review-driven-static-html-courseware/SKILL.md`
- `sealseek-feature-compare-doc` (local)：Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” document where each cor… 位置：`/Users/pechen/.hermes/skills/productivity/sealseek-feature-compare-doc/SKILL.md`
- `sealseek-static-html-courseware-workflow` (local)：Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server dependency, and conference… 位置：`/Users/pechen/.hermes/skills/productivity/sealseek-static-html-courseware-workflow/SKILL.md`
- `shopping-basket-visual-reference-discovery` (local)：docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual reference sources for an… 位置：`/Users/pechen/.hermes/skills/productivity/shopping-basket-visual-reference-discovery/SKILL.md`
- `single-file-static-html-courseware` (local)：Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live editable served HTM… 位置：`/Users/pechen/.hermes/skills/productivity/single-file-static-html-courseware/SKILL.md`
- `static-html-courseware-feedback-loop` (local)：Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review standards instead of c… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-feedback-loop/SKILL.md`
- `static-html-courseware-review-loop` (local)：Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of service-based editing… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop/SKILL.md`
- `static-html-courseware-review-loop-v2` (local)：Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimized for Sealseek-styl… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop-v2/SKILL.md`
- `static-html-courseware-shared-assets-and-merge` (local)：Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapters into one final H… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-shared-assets-and-merge/SKILL.md`
- `static-html-deck-to-editable-ppt` (local)：Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into truly editable PowerPoi… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-deck-to-editable-ppt/SKILL.md`
- `taobao-native-search-to-excel` (local)：使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 位置：`/Users/pechen/.hermes/skills/productivity/taobao-native-search-to-excel/SKILL.md`
- `taobao-search-to-excel` (local)：使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 位置：`/Users/pechen/.hermes/skills/productivity/taobao-search-to-excel/SKILL.md`
- `xicheng-bi-feishu-feature-doc` (local)：Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise sales-conversion-orie… 位置：`/Users/pechen/.hermes/skills/productivity/xicheng-bi-feishu-feature-doc/SKILL.md`
- `llm-wiki` (local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and li… 位置：`/Users/pechen/.hermes/skills/research/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answe… 位置：`/Users/pechen/.hermes/skills/research/llm-wiki-audit-and-optimization/SKILL.md`
- `cross-agent-skill-packaging` (local)：Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when publishing to git, syn… 位置：`/Users/pechen/.hermes/skills/software-development/cross-agent-skill-packaging/SKILL.md`
- `sealseek-gpt-image-skill-migration` (local)：Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use when migrating imag… 位置：`/Users/pechen/.hermes/skills/software-development/sealseek-gpt-image-skill-migration/SKILL.md`
- `sealseek-skill-sync-and-toolcall-fix` (local)：Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-promotion bug in Agen… 位置：`/Users/pechen/.hermes/skills/software-development/sealseek-skill-sync-and-toolcall-fix/SKILL.md`

### OpenClaw

- `ecom-market-rank` (local)：电商市场排行榜数据分析。适用于用户上传商品排行榜 Excel/CSV 文件（如淘宝生意参谋市场排行导出）时触发。输入：商品排行榜表格文件（xlsx/csv）。输出：文本分析总结 + 离线 HTML 可视化报告。触发场景：用户发送表格并要求分析市场排行、商品排行、品类分析、竞品分析… 位置：`/Users/pechen/.openclaw/workspace/skills/ecom-market-rank/SKILL.md`
- `mcporter` (local)：Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio). 位置：`/Users/pechen/.openclaw/workspace/skills/mcporter/SKILL.md`
- `taobao-native` (local)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check ord… 位置：`/Users/pechen/.openclaw/workspace/skills/taobao-native/SKILL.md`
- `web-reader` (local)：用真实 Chrome 浏览器（保留登录态）读取网页并压缩 DOM，供 AI 高效分析。适用于需要访问需要登录的网站（淘宝、生意参谋、千牛、飞书等）时抓取页面数据、进行页面操作（点击、填表、滚动）。核心优势：真实 Chrome 不被反爬识别，DOM 压缩后 token 消耗降低 9… 位置：`/Users/pechen/.openclaw/workspace/skills/web-reader/SKILL.md`

### SealSeek

- `detail-page-batch-optimization` (workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography… 位置：`/Users/pechen/.sealseek/workspace/skills/detail-page-batch-optimization/SKILL.md`
- `docx` (workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \… 位置：`/Users/pechen/.sealseek/workspace/skills/docx/SKILL.md`
- `ecommerce-visual-plan` (workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows… 位置：`/Users/pechen/.sealseek/workspace/skills/ecommerce-visual-plan/SKILL.md`
- `gpt生图` (workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GP… 位置：`/Users/pechen/.sealseek/workspace/skills/gpt生图/SKILL.md`
- `image-understanding` (workspace-skills)：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。 位置：`/Users/pechen/.sealseek/workspace/skills/image-understanding/SKILL.md`
- `keyword-assistant` (workspace-skills)：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键… 位置：`/Users/pechen/.sealseek/workspace/skills/keyword-assistant/SKILL.md`
- `keyword-data-export` (workspace-skills)：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。 位置：`/Users/pechen/.sealseek/workspace/skills/keyword-data-export/SKILL.md`
- `keyword-traffic` (workspace-skills)：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时… 位置：`/Users/pechen/.sealseek/workspace/skills/keyword-traffic/SKILL.md`
- `lark-cli-doc-reader` (workspace-skills)：使用用户本机 /opt/homebrew/bin/lark-cli 读取飞书云文档。适用于按文档标题/文件名搜索并读取飞书 Docx/Doc/Wiki，或用户给出飞书文档 URL/token 时读取内容。重点规避 OpenClaw/SealClaw 环境变量导致的 lark-cl… 位置：`/Users/pechen/.sealseek/workspace/skills/lark-cli-doc-reader/SKILL.md`
- `market-analysis` (workspace-skills)：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspace/skills/market-analysis/SKILL.md`
- `market-trend` (workspace-skills)：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市… 位置：`/Users/pechen/.sealseek/workspace/skills/market-trend/SKILL.md`
- `qa-merge-clean` (workspace-skills)：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出… 位置：`/Users/pechen/.sealseek/workspace/skills/qa-merge-clean/SKILL.md`
- `review-cleaning-assistant` (workspace-skills)：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除… 位置：`/Users/pechen/.sealseek/workspace/skills/review-cleaning-assistant/SKILL.md`
- `search-term-blue-ocean-report` (workspace-skills)：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需… 位置：`/Users/pechen/.sealseek/workspace/skills/search-term-blue-ocean-report/SKILL.md`
- `search-term-relevance-scorer` (workspace-skills)：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“… 位置：`/Users/pechen/.sealseek/workspace/skills/search-term-relevance-scorer/SKILL.md`
- `shop-product-diagnosis` (workspace-skills)：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex re… 位置：`/Users/pechen/.sealseek/workspace/skills/shop-product-diagnosis/SKILL.md`
- `single-image-optimization` (workspace-skills)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimiz… 位置：`/Users/pechen/.sealseek/workspace/skills/single-image-optimization/SKILL.md`
- `taobao-item` (workspace-skills)：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看… 位置：`/Users/pechen/.sealseek/workspace/skills/taobao-item/SKILL.md`
- `taobao-market-analysis` (workspace-skills)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspace/skills/taobao-market-analysis/SKILL.md`
- `taobao-native` (workspace-skills)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check ord… 位置：`/Users/pechen/.sealseek/workspace/skills/taobao-native/SKILL.md`
- `taobao-search-parser` (workspace-skills)：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”… 位置：`/Users/pechen/.sealseek/workspace/skills/taobao-search-parser/SKILL.md`
- `web-image-extractor` (workspace-skills)：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器… 位置：`/Users/pechen/.sealseek/workspace/skills/web-image-extractor/SKILL.md`
- `work-browser` (workspace-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复… 位置：`/Users/pechen/.sealseek/workspace/skills/work-browser/SKILL.md`
- `work-browser2` (workspace-skills)：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适… 位置：`/Users/pechen/.sealseek/workspace/skills/work-browser2/SKILL.md`
- `xmind-cli` (workspace-skills)：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/.sealseek/workspace/skills/xmind-cli/SKILL.md`
- `关键词助手` (workspace-skills)：生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长… 位置：`/Users/pechen/.sealseek/workspace/skills/关键词助手/SKILL.md`
- `关键词流量解析` (workspace-skills)：万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户… 位置：`/Users/pechen/.sealseek/workspace/skills/关键词流量解析/SKILL.md`
- `商品静态四象限分析` (workspace-skills)：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数… 位置：`/Users/pechen/.sealseek/workspace/skills/商品静态四象限分析/SKILL.md`
- `市场排行趋势` (workspace-skills)：生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排… 位置：`/Users/pechen/.sealseek/workspace/skills/市场排行趋势/SKILL.md`
- `快递超重补差对账` (workspace-skills)：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 … 位置：`/Users/pechen/.sealseek/workspace/skills/快递超重补差对账/SKILL.md`
- `成套视觉生成` (workspace-skills)：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片… 位置：`/Users/pechen/.sealseek/workspace/skills/成套视觉生成/SKILL.md`
- `推广管理助手` (workspace-skills)：万相台无界版推广计划的自动化管理 Skill。通过 API 直接调用万相台后端，支持 P0+P1 全场景： - 货品全站推广（onebpSite）：选品 + 投产比 + 预算，一键创建 - 关键词推广（onebpSearch）：搜索卡位 / 趋势明星 / 流量金卡 / 自定义推广… 位置：`/Users/pechen/.sealseek/workspace/skills/推广管理助手/SKILL.md`
- `无限画板 Skill 生成器` (workspace-skills)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 … 位置：`/Users/pechen/.sealseek/workspace/skills/无限画板 Skill 生成器.backup-20260609-1118/SKILL.md`
- `淘宝商品助手` (workspace-skills)：淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞… 位置：`/Users/pechen/.sealseek/workspace/skills/淘宝商品助手/SKILL.md`
- `生意参谋搜索词排行下载` (workspace-skills)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”… 位置：`/Users/pechen/.sealseek/workspace/skills/生意参谋搜索词排行下载/SKILL.md`
- `电商凭证管理` (workspace-skills)：多平台电商登录凭证管理。支持淘系(生意参谋/淘宝/1688)、抖音(抖店/千川)、拼多多、京东等平台。 全平台统一通过CDP交互式登录提取Cookie(绕过App-Bound Encryption)。自动检测有效性，失效自动刷新，兜底引导手动提供。 触发：用户首次使用任何电商Sk… 位置：`/Users/pechen/.sealseek/workspace/skills/电商凭证管理/SKILL.md`
- `电商视觉全套生成` (workspace-skills)：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块… 位置：`/Users/pechen/.sealseek/workspace/skills/电商视觉全套生成/SKILL.md`
- `商品静态四象限分析` (customized-skills)：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数… 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/商品静态四象限分析/SKILL.md`
- `image-understanding` (customized-skills)：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/图片理解/SKILL.md`
- `market-analysis` (customized-skills)：市场分析 skill。适合“帮我看看手机的趋势”“分析耳机市场”“查下女装在浙江发货的情况”这类需求。 默认行为对齐当前插件项目里的市场分析功能：综合排序、关键词来自用户输入、发货地默认留空，并自动获取一批靠前商品做分析。 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/市场分析/SKILL.md`
- `快递超重补差对账` (customized-skills)：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 … 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/快递超重补差对账/SKILL.md`
- `work-browser` (customized-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复… 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/浏览器接管/SKILL.md`
- `taobao-market-analysis` (customized-skills)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/淘宝商品市场分析_原始备份/SKILL.md`
- `ai-agent-skill-registry-sync` (default-workspace-skills)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wik… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ai-agent-skill-registry-sync/SKILL.md`
- `detail-page-batch-optimization` (default-workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/detail-page-batch-optimization/SKILL.md`
- `docx` (default-workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/docx/SKILL.md`
- `成套视觉生成` (default-workspace-skills)：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-generation/SKILL.md`
- `ecommerce-visual-plan` (default-workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-plan/SKILL.md`
- `电商视觉全套生成` (default-workspace-skills)：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-suite/SKILL.md`
- `gpt生图` (default-workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GP… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/gpt-image-generation/SKILL.md`
- `keyword-assistant` (default-workspace-skills)：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-assistant/SKILL.md`
- `keyword-data-export` (default-workspace-skills)：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-data-export/SKILL.md`
- `keyword-traffic` (default-workspace-skills)：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-traffic/SKILL.md`
- `llm-wiki` (default-workspace-skills)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and li… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (default-workspace-skills)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answe… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `llm-wiki-ingest` (default-workspace-skills)：Unified LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidia… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-ingest/SKILL.md`
- `llm-wiki-recompile-runner` (default-workspace-skills)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages,… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-recompile-runner/SKILL.md`
- `market-analysis` (default-workspace-skills)：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-analysis/SKILL.md`
- `market-trend` (default-workspace-skills)：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-trend/SKILL.md`
- `qa-merge-clean` (default-workspace-skills)：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/qa-merge-clean/SKILL.md`
- `review-cleaning-assistant` (default-workspace-skills)：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/review-cleaning-assistant/SKILL.md`
- `search-term-blue-ocean-report` (default-workspace-skills)：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-blue-ocean-report/SKILL.md`
- `search-term-relevance-scorer` (default-workspace-skills)：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-relevance-scorer/SKILL.md`
- `shop-product-diagnosis` (default-workspace-skills)：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex re… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/shop-product-diagnosis/SKILL.md`
- `single-image-optimization` (default-workspace-skills)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimiz… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/single-image-optimization/SKILL.md`
- `无限画板 Skill 生成器` (default-workspace-skills)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 … 位置：`/Users/pechen/.sealseek/workspaces/default/skills/skill-builder/SKILL.md`
- `生意参谋搜索词排行下载` (default-workspace-skills)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/sycm-search-rank-download/SKILL.md`
- `taobao-item` (default-workspace-skills)：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-item/SKILL.md`
- `taobao-native` (default-workspace-skills)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check ord… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-native/SKILL.md`
- `taobao-search-parser` (default-workspace-skills)：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-search-parser/SKILL.md`
- `web-image-extractor` (default-workspace-skills)：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/web-image-extractor/SKILL.md`
- `work-browser` (default-workspace-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser/SKILL.md`
- `work-browser2` (default-workspace-skills)：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser2/SKILL.md`
- `xmind-cli` (default-workspace-skills)：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/xmind-cli/SKILL.md`
- `detail-page-batch-optimization` (migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/hermes/SKILL.md`
- `detail-page-batch-optimization` (migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/sealseek/SKILL.md`
- `guanshu-review` (migration-bundle)：观数浏览器扩展前端代码评审工具。对分支代码进行规范检查，生成评审报告。检查项：P0-颜色硬编码、内联样式、if嵌套、重复造轮子、Content Script挂载方式；P1-BEM命名、魔法数字、第三方库引入；P2-文件职责单一、长文件拆分。仅适用于 xc-sealseek-ext… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/fe-guanshu-review/SKILL.md`
- `gemini-image` (migration-bundle)：Generate, edit, and iterate on images using Gemini image models via 12API. Use when the user asks to create, generate, draw, design, or prod… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/gemini-image/SKILL.md`
- `outline-paper-builder` (migration-bundle)：Reconstruct complete teaching-grade knowledge from mm/xmind outlines and output reviewable artifacts: lecture notes, optional long-form pape… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/outline-paper-builder/SKILL.md`
- `single-image-optimization` (migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimiz… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/hermes/SKILL.md`
- `single-image-optimization` (migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimiz… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/sealseek/SKILL.md`
- `xmind-cli` (standalone-local)：XMind 脑图输出助手 —— 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/sealseek/XMindCLI交付包V2/package/skills/xmind-cli/SKILL.md`
- `taobao-market-analysis` (standalone-local)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/sealseek/backup/淘宝商品市场分析_20260418_210055/SKILL.md`
- `商品成套视觉规划skill` (standalone-local)：把一个商品的多源证据（搜索词、评价、问大家、商品图）整理成**可执行的成套视觉规划**，输出给后续设计、生图、详情页优化或投放团队直接使用的规划结果。 位置：`/Users/pechen/sealseek/商品成套视觉规划skill/SKILL.md`
- `货号跨店铺表现差异分析` (standalone-local)：🎯 任务目标 基于指定货号或全量数据，分析并识别同一货号在不同店铺/链接间销售表现差异显著的商品，帮助商家发现潜在的分销优化机会。 位置：`/Users/pechen/sealseek/货号跨店铺表现差异分析/SKILL.md`

## 能力分类索引

### 知识库 / 知识管理 / LLM Wiki

- `ai-agent-skill-registry-sync` (Codex, local)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill re… 位置：`/Users/pechen/.codex/skills/ai-agent-skill-registry-sync/SKILL.md`
- `brand-planning-report` (Codex, local)：Generate a user-facing ecommerce brand planning HTML report from a standard 店铺商品 Excel workbook, using Peter's brand-strategy LLM Wiki for positioning… 位置：`/Users/pechen/.codex/skills/brand-planning-report/SKILL.md`
- `llm-wiki` (Codex, local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for con… 位置：`/Users/pechen/.codex/skills/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (Codex, local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result n… 位置：`/Users/pechen/.codex/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `llm-wiki-ingest` (Codex, local)：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian… 位置：`/Users/pechen/.codex/skills/llm-wiki-ingest/SKILL.md`
- `llm-wiki-recompile-runner` (Codex, local)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplet… 位置：`/Users/pechen/.codex/skills/llm-wiki-recompile-runner/SKILL.md`
- `baoyu-comic` (Hermes, local)：Knowledge comics (知识漫画): educational, biography, tutorial. 位置：`/Users/pechen/.hermes/skills/creative/baoyu-comic/SKILL.md`
- `douyin-link-to-knowledge` (Hermes, local)：Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transcribing/val… 位置：`/Users/pechen/.hermes/skills/productivity/douyin-link-to-knowledge/SKILL.md`
- `llm-wiki` (Hermes, local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for con… 位置：`/Users/pechen/.hermes/skills/research/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (Hermes, local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result n… 位置：`/Users/pechen/.hermes/skills/research/llm-wiki-audit-and-optimization/SKILL.md`
- `lark-cli-doc-reader` (SealSeek, workspace-skills)：使用用户本机 /opt/homebrew/bin/lark-cli 读取飞书云文档。适用于按文档标题/文件名搜索并读取飞书 Docx/Doc/Wiki，或用户给出飞书文档 URL/token 时读取内容。重点规避 OpenClaw/SealClaw 环境变量导致的 lark-cli config b… 位置：`/Users/pechen/.sealseek/workspace/skills/lark-cli-doc-reader/SKILL.md`
- `ai-agent-skill-registry-sync` (SealSeek, default-workspace-skills)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill re… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ai-agent-skill-registry-sync/SKILL.md`
- `llm-wiki` (SealSeek, default-workspace-skills)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for con… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (SealSeek, default-workspace-skills)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result n… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `llm-wiki-ingest` (SealSeek, default-workspace-skills)：Unified LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clipping… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-ingest/SKILL.md`
- `llm-wiki-recompile-runner` (SealSeek, default-workspace-skills)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplet… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-recompile-runner/SKILL.md`
- `outline-paper-builder` (SealSeek, migration-bundle)：Reconstruct complete teaching-grade knowledge from mm/xmind outlines and output reviewable artifacts: lecture notes, optional long-form paper, and lec… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/outline-paper-builder/SKILL.md`

### 视觉 / 内容 / 课件生产

- `course-deck-factory` (Codex, local)：Build editable course slide decks from a standardized deck spec using Node.js, PptxGenJS, local fonts, structured page types, and a mixed visual pipel… 位置：`/Users/pechen/.codex/skills/course-deck-factory/SKILL.md`
- `image-detail-page` (Codex, local)：根据产品白底图和品类，全自动推断模型、人群、风格，并一站式生成13个策划文件及对应电商图片。 当用户提到主图详情页、电商策划、白底图出方案、主图设计、详情页设计、电商视觉方案时触发。 位置：`/Users/pechen/.codex/skills/image-detail-page/SKILL.md`
- `seedance-commerce-video` (Codex, local)：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selling points,… 位置：`/Users/pechen/.codex/skills/seedance-commerce-video/SKILL.md`
- `shop-product-diagnosis` (Codex, local)：Diagnose an ecommerce shop from a standard 店铺商品 Excel workbook and produce a tabbed HTML report plus an XMind action map. Use when Codex receives file… 位置：`/Users/pechen/.codex/skills/shop-product-diagnosis/SKILL.md`
- `baoyu-article-illustrator` (Hermes, local)：Article illustrations: type × style × palette consistency. 位置：`/Users/pechen/.hermes/skills/creative/baoyu-article-illustrator/SKILL.md`
- `baoyu-infographic` (Hermes, local)：Infographics: 21 layouts x 21 styles (信息图, 可视化). 位置：`/Users/pechen/.hermes/skills/creative/baoyu-infographic/SKILL.md`
- `ecommerce-image-skill-architecture` (Hermes, local)：Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use when designing or refactoring a… 位置：`/Users/pechen/.hermes/skills/creative/ecommerce-image-skill-architecture/SKILL.md`
- `evolink-gpt-image-2` (Hermes, local)：Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and test script locations. 位置：`/Users/pechen/.hermes/skills/creative/evolink-gpt-image-2/SKILL.md`
- `gpt-image-2-12api` (Hermes, local)：Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavior, reproducible probing, and k… 位置：`/Users/pechen/.hermes/skills/creative/gpt-image-2-12api/SKILL.md`
- `gpt生图` (Hermes, local)：Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, design, or produce any image, il… 位置：`/Users/pechen/.hermes/skills/creative/gpt生图/SKILL.md`
- `shopping-basket-visual-planning` (Hermes, local)：Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the user needs to know what other pro… 位置：`/Users/pechen/.hermes/skills/creative/shopping-basket-visual-planning/SKILL.md`
- `single-image-optimization` (Hermes, local)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization rout… 位置：`/Users/pechen/.hermes/skills/creative/single-image-optimization/SKILL.md`
- `taobao-gpt-image-creative-main-image` (Hermes, local)：Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably via post-processing to avoid A… 位置：`/Users/pechen/.hermes/skills/creative/taobao-gpt-image-creative-main-image/SKILL.md`
- `toapis-gpt-image-2` (Hermes, local)：Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working request formats, task polling, loca… 位置：`/Users/pechen/.hermes/skills/creative/toapis-gpt-image-2/SKILL.md`
- `conference-static-html-courseware-review-loop` (Hermes, local)：Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review, Git-backed iteration, and exp… 位置：`/Users/pechen/.hermes/skills/productivity/conference-static-html-courseware-review-loop/SKILL.md`
- `course-html-ppt-16x9-image-pages` (Hermes, local)：Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy slide layouts. 位置：`/Users/pechen/.hermes/skills/productivity/course-html-ppt-16x9-image-pages/SKILL.md`
- `dual-source-chapterized-html-ppt-courseware` (Hermes, local)：Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to avoid renumbering cascades. 位置：`/Users/pechen/.hermes/skills/productivity/dual-source-chapterized-html-ppt-courseware/SKILL.md`
- `ecommerce-bi-operation-skill-planning` (Hermes, local)：Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡检 SOPs, priority engines, or p… 位置：`/Users/pechen/.hermes/skills/productivity/ecommerce-bi-operation-skill-planning/SKILL.md`
- `feishu-product-feature-doc` (Hermes, local)：Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-oriented copy, callouts, comparison… 位置：`/Users/pechen/.hermes/skills/productivity/feishu-product-feature-doc/SKILL.md`
- `goal-driven-daily-report-templates` (Hermes, local)：Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use when Peter asks to design job-spe… 位置：`/Users/pechen/.hermes/skills/productivity/goal-driven-daily-report-templates/SKILL.md`
- `hermes-feishu-session-debugging` (Hermes, local)：Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session JSON files, and tool availabil… 位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-session-debugging/SKILL.md`
- `html-ppt-conference-review-loop` (Hermes, local)：Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with explicit readability and layout … 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-conference-review-loop/SKILL.md`
- `html-ppt-course-deck` (Hermes, local)：Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid or visually weak. Use slides.js… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-course-deck/SKILL.md`
- `html-ppt-font-standardization` (Hermes, local)：Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run an overflow audit after replac… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-font-standardization/SKILL.md`
- `html-ppt-screenshot-review-loop` (Hermes, local)：Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-style decks where readability, … 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-screenshot-review-loop/SKILL.md`
- `html-ppt-stage-fit-and-background-cleanup` (Hermes, local)：Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds with clean backgrounds plus a sep… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-stage-fit-and-background-cleanup/SKILL.md`
- `html-ppt` (Hermes, local)：HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by templates. Use when the user as… 位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-studio-agentskill/SKILL.md`
- `review-driven-static-html-courseware` (Hermes, local)：Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML-native presentation instead o… 位置：`/Users/pechen/.hermes/skills/productivity/review-driven-static-html-courseware/SKILL.md`
- `sealseek-static-html-courseware-workflow` (Hermes, local)：Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server dependency, and conference-first rea… 位置：`/Users/pechen/.hermes/skills/productivity/sealseek-static-html-courseware-workflow/SKILL.md`
- `shopping-basket-visual-reference-discovery` (Hermes, local)：docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual reference sources for an e-commerc… 位置：`/Users/pechen/.hermes/skills/productivity/shopping-basket-visual-reference-discovery/SKILL.md`
- `single-file-static-html-courseware` (Hermes, local)：Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live editable served HTML. Optimiz… 位置：`/Users/pechen/.hermes/skills/productivity/single-file-static-html-courseware/SKILL.md`
- `static-html-courseware-feedback-loop` (Hermes, local)：Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review standards instead of code-only j… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-feedback-loop/SKILL.md`
- `static-html-courseware-review-loop` (Hermes, local)：Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of service-based editing. 位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop/SKILL.md`
- `static-html-courseware-review-loop-v2` (Hermes, local)：Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimized for Sealseek-style dark-the… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop-v2/SKILL.md`
- `static-html-courseware-shared-assets-and-merge` (Hermes, local)：Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapters into one final HTML withou… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-shared-assets-and-merge/SKILL.md`
- `static-html-deck-to-editable-ppt` (Hermes, local)：Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into truly editable PowerPoint, instea… 位置：`/Users/pechen/.hermes/skills/productivity/static-html-deck-to-editable-ppt/SKILL.md`
- `xicheng-bi-feishu-feature-doc` (Hermes, local)：Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise sales-conversion-oriented but u… 位置：`/Users/pechen/.hermes/skills/productivity/xicheng-bi-feishu-feature-doc/SKILL.md`
- `sealseek-gpt-image-skill-migration` (Hermes, local)：Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use when migrating image-generati… 位置：`/Users/pechen/.hermes/skills/software-development/sealseek-gpt-image-skill-migration/SKILL.md`
- `sealseek-skill-sync-and-toolcall-fix` (Hermes, local)：Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-promotion bug in AgentScope. 位置：`/Users/pechen/.hermes/skills/software-development/sealseek-skill-sync-and-toolcall-fix/SKILL.md`
- `detail-page-batch-optimization` (SealSeek, workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constrain… 位置：`/Users/pechen/.sealseek/workspace/skills/detail-page-batch-optimization/SKILL.md`
- `docx` (SealSeek, workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\… 位置：`/Users/pechen/.sealseek/workspace/skills/docx/SKILL.md`
- `ecommerce-visual-plan` (SealSeek, workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows. 位置：`/Users/pechen/.sealseek/workspace/skills/ecommerce-visual-plan/SKILL.md`
- `gpt生图` (SealSeek, workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GPT 生图能力，不再使… 位置：`/Users/pechen/.sealseek/workspace/skills/gpt生图/SKILL.md`
- `image-understanding` (SealSeek, workspace-skills)：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。 位置：`/Users/pechen/.sealseek/workspace/skills/image-understanding/SKILL.md`
- `search-term-relevance-scorer` (SealSeek, workspace-skills)：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“给搜索词表做相关度评… 位置：`/Users/pechen/.sealseek/workspace/skills/search-term-relevance-scorer/SKILL.md`
- `shop-product-diagnosis` (SealSeek, workspace-skills)：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex receives a s… 位置：`/Users/pechen/.sealseek/workspace/skills/shop-product-diagnosis/SKILL.md`
- `single-image-optimization` (SealSeek, workspace-skills)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization rout… 位置：`/Users/pechen/.sealseek/workspace/skills/single-image-optimization/SKILL.md`
- `taobao-item` (SealSeek, workspace-skills)：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品… 位置：`/Users/pechen/.sealseek/workspace/skills/taobao-item/SKILL.md`
- `web-image-extractor` (SealSeek, workspace-skills)：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器代码并写入 skil… 位置：`/Users/pechen/.sealseek/workspace/skills/web-image-extractor/SKILL.md`
- `xmind-cli` (SealSeek, workspace-skills)：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/.sealseek/workspace/skills/xmind-cli/SKILL.md`
- `成套视觉生成` (SealSeek, workspace-skills)：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片生成。 位置：`/Users/pechen/.sealseek/workspace/skills/成套视觉生成/SKILL.md`
- `无限画板 Skill 生成器` (SealSeek, workspace-skills)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优… 位置：`/Users/pechen/.sealseek/workspace/skills/无限画板 Skill 生成器.backup-20260609-1118/SKILL.md`
- `淘宝商品助手` (SealSeek, workspace-skills)：淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析" 位置：`/Users/pechen/.sealseek/workspace/skills/淘宝商品助手/SKILL.md`
- `电商视觉全套生成` (SealSeek, workspace-skills)：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块先规划、用户确认后再… 位置：`/Users/pechen/.sealseek/workspace/skills/电商视觉全套生成/SKILL.md`
- `image-understanding` (SealSeek, customized-skills)：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/图片理解/SKILL.md`
- `detail-page-batch-optimization` (SealSeek, default-workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constrain… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/detail-page-batch-optimization/SKILL.md`
- `docx` (SealSeek, default-workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/docx/SKILL.md`
- `成套视觉生成` (SealSeek, default-workspace-skills)：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片生成。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-generation/SKILL.md`
- `ecommerce-visual-plan` (SealSeek, default-workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows. 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-plan/SKILL.md`
- `电商视觉全套生成` (SealSeek, default-workspace-skills)：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块先规划、用户确认后再… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-suite/SKILL.md`
- `gpt生图` (SealSeek, default-workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GPT 生图能力，不再使… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/gpt-image-generation/SKILL.md`
- `search-term-relevance-scorer` (SealSeek, default-workspace-skills)：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“给搜索词表做相关度评… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-relevance-scorer/SKILL.md`
- `shop-product-diagnosis` (SealSeek, default-workspace-skills)：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex receives a s… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/shop-product-diagnosis/SKILL.md`
- `single-image-optimization` (SealSeek, default-workspace-skills)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization rout… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/single-image-optimization/SKILL.md`
- `无限画板 Skill 生成器` (SealSeek, default-workspace-skills)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/skill-builder/SKILL.md`
- `taobao-item` (SealSeek, default-workspace-skills)：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-item/SKILL.md`
- `web-image-extractor` (SealSeek, default-workspace-skills)：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器代码并写入 skil… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/web-image-extractor/SKILL.md`
- `xmind-cli` (SealSeek, default-workspace-skills)：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/xmind-cli/SKILL.md`
- `detail-page-batch-optimization` (SealSeek, migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constrain… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/hermes/SKILL.md`
- `detail-page-batch-optimization` (SealSeek, migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constrain… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/sealseek/SKILL.md`
- `gemini-image` (SealSeek, migration-bundle)：Generate, edit, and iterate on images using Gemini image models via 12API. Use when the user asks to create, generate, draw, design, or produce any im… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/gemini-image/SKILL.md`
- `single-image-optimization` (SealSeek, migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization rout… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/hermes/SKILL.md`
- `single-image-optimization` (SealSeek, migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization rout… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/sealseek/SKILL.md`
- `xmind-cli` (SealSeek, standalone-local)：XMind 脑图输出助手 —— 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/sealseek/XMindCLI交付包V2/package/skills/xmind-cli/SKILL.md`
- `商品成套视觉规划skill` (SealSeek, standalone-local)：把一个商品的多源证据（搜索词、评价、问大家、商品图）整理成**可执行的成套视觉规划**，输出给后续设计、生图、详情页优化或投放团队直接使用的规划结果。 位置：`/Users/pechen/sealseek/商品成套视觉规划skill/SKILL.md`

### 电商 / 商品 / 品牌运营

- `ecommerce-profit-statement-automation` (Codex, local)：Automate ecommerce platform profit statement workbooks from settlement/funds/account bills. Use when the user wants to turn Taobao or other ecommerce … 位置：`/Users/pechen/.codex/skills/ecommerce-profit-statement-automation/SKILL.md`
- `yuce-product-list-export` (Codex, local)：Use when the user wants to export 行情高手/预策平台 “商品列表” data after they have already logged in and manually navigated to the target report page. The skill … 位置：`/Users/pechen/.codex/skills/yuce-product-list-export/SKILL.md`
- `real-chrome-web-reader` (Hermes, local)：使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。 位置：`/Users/pechen/.hermes/skills/productivity/real-chrome-web-reader/SKILL.md`
- `taobao-native-search-to-excel` (Hermes, local)：使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 位置：`/Users/pechen/.hermes/skills/productivity/taobao-native-search-to-excel/SKILL.md`
- `taobao-search-to-excel` (Hermes, local)：使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 位置：`/Users/pechen/.hermes/skills/productivity/taobao-search-to-excel/SKILL.md`
- `ecom-market-rank` (OpenClaw, local)：电商市场排行榜数据分析。适用于用户上传商品排行榜 Excel/CSV 文件（如淘宝生意参谋市场排行导出）时触发。输入：商品排行榜表格文件（xlsx/csv）。输出：文本分析总结 + 离线 HTML 可视化报告。触发场景：用户发送表格并要求分析市场排行、商品排行、品类分析、竞品分析、市场洞察等。不适用… 位置：`/Users/pechen/.openclaw/workspace/skills/ecom-market-rank/SKILL.md`
- `taobao-native` (OpenClaw, local)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, reque… 位置：`/Users/pechen/.openclaw/workspace/skills/taobao-native/SKILL.md`
- `web-reader` (OpenClaw, local)：用真实 Chrome 浏览器（保留登录态）读取网页并压缩 DOM，供 AI 高效分析。适用于需要访问需要登录的网站（淘宝、生意参谋、千牛、飞书等）时抓取页面数据、进行页面操作（点击、填表、滚动）。核心优势：真实 Chrome 不被反爬识别，DOM 压缩后 token 消耗降低 95%。触发场景：抓取… 位置：`/Users/pechen/.openclaw/workspace/skills/web-reader/SKILL.md`
- `keyword-assistant` (SealSeek, workspace-skills)：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长… 位置：`/Users/pechen/.sealseek/workspace/skills/keyword-assistant/SKILL.md`
- `keyword-data-export` (SealSeek, workspace-skills)：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。 位置：`/Users/pechen/.sealseek/workspace/skills/keyword-data-export/SKILL.md`
- `keyword-traffic` (SealSeek, workspace-skills)：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户… 位置：`/Users/pechen/.sealseek/workspace/skills/keyword-traffic/SKILL.md`
- `market-analysis` (SealSeek, workspace-skills)：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspace/skills/market-analysis/SKILL.md`
- `market-trend` (SealSeek, workspace-skills)：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名… 位置：`/Users/pechen/.sealseek/workspace/skills/market-trend/SKILL.md`
- `qa-merge-clean` (SealSeek, workspace-skills)：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出统一结果 3. 从文… 位置：`/Users/pechen/.sealseek/workspace/skills/qa-merge-clean/SKILL.md`
- `review-cleaning-assistant` (SealSeek, workspace-skills)：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除其他列，仅保留“评价… 位置：`/Users/pechen/.sealseek/workspace/skills/review-cleaning-assistant/SKILL.md`
- `search-term-blue-ocean-report` (SealSeek, workspace-skills)：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需求。 位置：`/Users/pechen/.sealseek/workspace/skills/search-term-blue-ocean-report/SKILL.md`
- `taobao-market-analysis` (SealSeek, workspace-skills)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspace/skills/taobao-market-analysis/SKILL.md`
- `taobao-native` (SealSeek, workspace-skills)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, reque… 位置：`/Users/pechen/.sealseek/workspace/skills/taobao-native/SKILL.md`
- `taobao-search-parser` (SealSeek, workspace-skills)：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”这类需求。 位置：`/Users/pechen/.sealseek/workspace/skills/taobao-search-parser/SKILL.md`
- `work-browser` (SealSeek, workspace-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出… 位置：`/Users/pechen/.sealseek/workspace/skills/work-browser/SKILL.md`
- `work-browser2` (SealSeek, workspace-skills)：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适合继续交给模型或下游… 位置：`/Users/pechen/.sealseek/workspace/skills/work-browser2/SKILL.md`
- `关键词助手` (SealSeek, workspace-skills)：生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标… 位置：`/Users/pechen/.sealseek/workspace/skills/关键词助手/SKILL.md`
- `关键词流量解析` (SealSeek, workspace-skills)：万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流… 位置：`/Users/pechen/.sealseek/workspace/skills/关键词流量解析/SKILL.md`
- `商品静态四象限分析` (SealSeek, workspace-skills)：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数和付费占比给商品分层… 位置：`/Users/pechen/.sealseek/workspace/skills/商品静态四象限分析/SKILL.md`
- `市场排行趋势` (SealSeek, workspace-skills)：生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、… 位置：`/Users/pechen/.sealseek/workspace/skills/市场排行趋势/SKILL.md`
- `快递超重补差对账` (SealSeek, workspace-skills)：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 1 元安检费 - 新… 位置：`/Users/pechen/.sealseek/workspace/skills/快递超重补差对账/SKILL.md`
- `推广管理助手` (SealSeek, workspace-skills)：万相台无界版推广计划的自动化管理 Skill。通过 API 直接调用万相台后端，支持 P0+P1 全场景： - 货品全站推广（onebpSite）：选品 + 投产比 + 预算，一键创建 - 关键词推广（onebpSearch）：搜索卡位 / 趋势明星 / 流量金卡 / 自定义推广 - 人群推广（on… 位置：`/Users/pechen/.sealseek/workspace/skills/推广管理助手/SKILL.md`
- `生意参谋搜索词排行下载` (SealSeek, workspace-skills)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋… 位置：`/Users/pechen/.sealseek/workspace/skills/生意参谋搜索词排行下载/SKILL.md`
- `电商凭证管理` (SealSeek, workspace-skills)：多平台电商登录凭证管理。支持淘系(生意参谋/淘宝/1688)、抖音(抖店/千川)、拼多多、京东等平台。 全平台统一通过CDP交互式登录提取Cookie(绕过App-Bound Encryption)。自动检测有效性，失效自动刷新，兜底引导手动提供。 触发：用户首次使用任何电商Skill、提到"登录/… 位置：`/Users/pechen/.sealseek/workspace/skills/电商凭证管理/SKILL.md`
- `商品静态四象限分析` (SealSeek, customized-skills)：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数和付费占比给商品分层… 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/商品静态四象限分析/SKILL.md`
- `market-analysis` (SealSeek, customized-skills)：市场分析 skill。适合“帮我看看手机的趋势”“分析耳机市场”“查下女装在浙江发货的情况”这类需求。 默认行为对齐当前插件项目里的市场分析功能：综合排序、关键词来自用户输入、发货地默认留空，并自动获取一批靠前商品做分析。 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/市场分析/SKILL.md`
- `快递超重补差对账` (SealSeek, customized-skills)：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 1 元安检费 - 新… 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/快递超重补差对账/SKILL.md`
- `work-browser` (SealSeek, customized-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出… 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/浏览器接管/SKILL.md`
- `taobao-market-analysis` (SealSeek, customized-skills)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/淘宝商品市场分析_原始备份/SKILL.md`
- `keyword-assistant` (SealSeek, default-workspace-skills)：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-assistant/SKILL.md`
- `keyword-data-export` (SealSeek, default-workspace-skills)：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-data-export/SKILL.md`
- `keyword-traffic` (SealSeek, default-workspace-skills)：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-traffic/SKILL.md`
- `market-analysis` (SealSeek, default-workspace-skills)：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-analysis/SKILL.md`
- `market-trend` (SealSeek, default-workspace-skills)：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-trend/SKILL.md`
- `qa-merge-clean` (SealSeek, default-workspace-skills)：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出统一结果 3. 从文… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/qa-merge-clean/SKILL.md`
- `review-cleaning-assistant` (SealSeek, default-workspace-skills)：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除其他列，仅保留“评价… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/review-cleaning-assistant/SKILL.md`
- `search-term-blue-ocean-report` (SealSeek, default-workspace-skills)：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-blue-ocean-report/SKILL.md`
- `生意参谋搜索词排行下载` (SealSeek, default-workspace-skills)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/sycm-search-rank-download/SKILL.md`
- `taobao-native` (SealSeek, default-workspace-skills)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, reque… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-native/SKILL.md`
- `taobao-search-parser` (SealSeek, default-workspace-skills)：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-search-parser/SKILL.md`
- `work-browser` (SealSeek, default-workspace-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser/SKILL.md`
- `work-browser2` (SealSeek, default-workspace-skills)：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适合继续交给模型或下游… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser2/SKILL.md`
- `guanshu-review` (SealSeek, migration-bundle)：观数浏览器扩展前端代码评审工具。对分支代码进行规范检查，生成评审报告。检查项：P0-颜色硬编码、内联样式、if嵌套、重复造轮子、Content Script挂载方式；P1-BEM命名、魔法数字、第三方库引入；P2-文件职责单一、长文件拆分。仅适用于 xc-sealseek-extension-syc… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/fe-guanshu-review/SKILL.md`
- `taobao-market-analysis` (SealSeek, standalone-local)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/sealseek/backup/淘宝商品市场分析_20260418_210055/SKILL.md`
- `货号跨店铺表现差异分析` (SealSeek, standalone-local)：🎯 任务目标 基于指定货号或全量数据，分析并识别同一货号在不同店铺/链接间销售表现差异显著的商品，帮助商家发现潜在的分销优化机会。 位置：`/Users/pechen/sealseek/货号跨店铺表现差异分析/SKILL.md`

### Agent 工程 / Skill / Plugin / MCP

- `internal-plugin-workflow` (Codex, local)：Use when the user wants to build or iterate an internal Chrome browser extension against a page they have already opened, especially when the work inc… 位置：`/Users/pechen/.codex/skills/internal-plugin-workflow/SKILL.md`
- `feishu-cli-isolated-config` (Hermes, local)：Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentials; use an isolated config fil… 位置：`/Users/pechen/.hermes/skills/productivity/feishu-cli-isolated-config/SKILL.md`
- `hermes-feishu-gateway-setup` (Hermes, local)：Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credentials; use isolated FEISHU_CONFIG … 位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-gateway-setup/SKILL.md`
- `macos-wechat-cli` (Hermes, local)：Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to install or troubleshoot a WeChat … 位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-cli/SKILL.md`
- `macos-wechat-history-decrypt` (Hermes, local)：Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process existing WeChat chat history, lis… 位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-history-decrypt/SKILL.md`
- `official-lark-cli-feishu-workflows` (Hermes, local)：Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenClaw setup already uses ~/.lark-c… 位置：`/Users/pechen/.hermes/skills/productivity/official-lark-cli-feishu-workflows/SKILL.md`
- `reduce-paid-ratio-link-agent-mvp` (Hermes, local)：Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for close, reduce, keep, or observe… 位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-link-agent-mvp/SKILL.md`
- `reduce-paid-ratio-plan-evaluator` (Hermes, local)：Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from two source reports, then exporti… 位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-plan-evaluator/SKILL.md`
- `sealseek-feature-compare-doc` (Hermes, local)：Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” document where each core module g… 位置：`/Users/pechen/.hermes/skills/productivity/sealseek-feature-compare-doc/SKILL.md`
- `cross-agent-skill-packaging` (Hermes, local)：Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when publishing to git, syncing into … 位置：`/Users/pechen/.hermes/skills/software-development/cross-agent-skill-packaging/SKILL.md`
- `mcporter` (OpenClaw, local)：Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio). 位置：`/Users/pechen/.openclaw/workspace/skills/mcporter/SKILL.md`

## Skill 详情

### `ai-agent-skill-registry-sync`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/ai-agent-skill-registry-sync/SKILL.md`
- 功能检索描述：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under /Users/pechen/wiki. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ai-agent-skill-registry-sync AI Agent Skill Registry Sync Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under /Users/pechen/wiki. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents. ai-agent-skill-registry-sync/SKILL.md local

### `brand-planning-report`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/brand-planning-report/SKILL.md`
- 功能检索描述：Generate a user-facing ecommerce brand planning HTML report from a standard 店铺商品 Excel workbook, using Peter's brand-strategy LLM Wiki for positioning, mindshare product power, hero-product planning, visual-memory system, product-line strategy, channel expression, and AI visual reference generation. Use when files match 销量TOP0-市场数据分析-{店铺名称}_{日期}.xlsx and the desired output is a complete brand planning report, not just a product diagnosis.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；代码仓库、文件路径、PR/Issue、调试或开发任务；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：brand-planning-report Brand Planning Report Generate a user-facing ecommerce brand planning HTML report from a standard 店铺商品 Excel workbook, using Peter's brand-strategy LLM Wiki for positioning, mindshare product power, hero-product planning, visual-memory system, product-line strategy, channel expression, and AI visual reference generation. Use when files match 销量TOP0-市场数据分析-{店铺名称}_{日期}.xlsx and the desired output is a complete brand planning report, not just a product diagnosis. brand-planning-report/SKILL.md local

### `course-deck-factory`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/course-deck-factory/SKILL.md`
- 功能检索描述：Build editable course slide decks from a standardized deck spec using Node.js, PptxGenJS, local fonts, structured page types, and a mixed visual pipeline including screenshots, SVG diagrams, icon libraries, and Gemini image generation. Use when the input is already researched and organized into a course outline or per-slide content, and the task is to produce or refine a high-quality training deck rather than do the research itself.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：course-deck-factory Course Deck Factory Build editable course slide decks from a standardized deck spec using Node.js, PptxGenJS, local fonts, structured page types, and a mixed visual pipeline including screenshots, SVG diagrams, icon libraries, and Gemini image generation. Use when the input is already researched and organized into a course outline or per-slide content, and the task is to produce or refine a high-quality training deck rather than do the research itself. course-deck-factory/SKILL.md local

### `ecommerce-profit-statement-automation`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/ecommerce-profit-statement-automation/SKILL.md`
- 功能检索描述：Automate ecommerce platform profit statement workbooks from settlement/funds/account bills. Use when the user wants to turn Taobao or other ecommerce platform raw Excel bills into a formatted monthly profit statement, reconcile it against a manually prepared statement, normalize one-file or multi-file inputs, or build reusable Python-based profit-report automation.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-profit-statement-automation Ecommerce Profit Statement Automation Automate ecommerce platform profit statement workbooks from settlement/funds/account bills. Use when the user wants to turn Taobao or other ecommerce platform raw Excel bills into a formatted monthly profit statement, reconcile it against a manually prepared statement, normalize one-file or multi-file inputs, or build reusable Python-based profit-report automation. ecommerce-profit-statement-automation/SKILL.md local

### `image-detail-page`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/image-detail-page/SKILL.md`
- 功能检索描述：根据产品白底图和品类，全自动推断模型、人群、风格，并一站式生成13个策划文件及对应电商图片。 当用户提到主图详情页、电商策划、白底图出方案、主图设计、详情页设计、电商视觉方案时触发。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：image-detail-page 电商主图详情页策划 (全自动版) 根据产品白底图和品类，全自动推断模型、人群、风格，并一站式生成13个策划文件及对应电商图片。 当用户提到主图详情页、电商策划、白底图出方案、主图设计、详情页设计、电商视觉方案时触发。 image-detail-page/SKILL.md local

### `internal-plugin-workflow`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/internal-plugin-workflow/SKILL.md`
- 功能检索描述：Use when the user wants to build or iterate an internal Chrome browser extension against a page they have already opened, especially when the work includes injecting page UI, reverse engineering fetch/xhr APIs, reading page runtime state, building a modal/table UI, exporting Excel, and packaging the extension for coworkers. Trigger on requests such as “创建内部插件”, “在这个页面注入一个按钮”, “抓这个页面的 API”, “做一个弹窗展示数据”, “导出 Excel”, or “把插件打包给同事”.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：internal-plugin-workflow Internal Plugin Workflow Use when the user wants to build or iterate an internal Chrome browser extension against a page they have already opened, especially when the work includes injecting page UI, reverse engineering fetch/xhr APIs, reading page runtime state, building a modal/table UI, exporting Excel, and packaging the extension for coworkers. Trigger on requests such as “创建内部插件”, “在这个页面注入一个按钮”, “抓这个页面的 API”, “做一个弹窗展示数据”, “导出 Excel”, or “把插件打包给同事”. internal-plugin-workflow/SKILL.md local

### `llm-wiki`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/llm-wiki/SKILL.md`
- 功能检索描述：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki Karpathy's LLM Wiki Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency. llm-wiki/SKILL.md local

### `llm-wiki-audit-and-optimization`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/llm-wiki-audit-and-optimization/SKILL.md`
- 功能检索描述：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit and Optimization Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base. llm-wiki-audit-and-optimization/SKILL.md local

### `llm-wiki-ingest`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/llm-wiki-ingest/SKILL.md`
- 功能检索描述：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal pages, index/log updates, Obsidian route audit, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal pages, index/log updates, Obsidian route audit, and audit handoff. llm-wiki-ingest/SKILL.md local

### `llm-wiki-recompile-runner`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/llm-wiki-recompile-runner/SKILL.md`
- 功能检索描述：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：llm-wiki-recompile-runner LLM Wiki Recompile Runner Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality. llm-wiki-recompile-runner/SKILL.md local

### `seedance-commerce-video`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/seedance-commerce-video/SKILL.md`
- 功能检索描述：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selling points, target audience, price, brand assets, or competitor references into Douyin/Taobao/Kuaishou/Xiaohongshu commercial videos, Seedance all-purpose reference prompts, shot plans, API request payloads, or batch ad variants.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：seedance-commerce-video Seedance Commerce Video Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selling points, target audience, price, brand assets, or competitor references into Douyin/Taobao/Kuaishou/Xiaohongshu commercial videos, Seedance all-purpose reference prompts, shot plans, API request payloads, or batch ad variants. seedance-commerce-video/SKILL.md local

### `shop-product-diagnosis`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/shop-product-diagnosis/SKILL.md`
- 功能检索描述：Diagnose an ecommerce shop from a standard 店铺商品 Excel workbook and produce a tabbed HTML report plus an XMind action map. Use when Codex receives files like 销量TOP0-市场数据分析-{店铺名称}_{日期}.xlsx and needs product-line diagnosis, growth direction, Top20 image audience/style inference, brand opportunity, organization design, staged execution recommendations, or gpt-image-2 style reference prompts/images.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：shop-product-diagnosis Shop Product Diagnosis Diagnose an ecommerce shop from a standard 店铺商品 Excel workbook and produce a tabbed HTML report plus an XMind action map. Use when Codex receives files like 销量TOP0-市场数据分析-{店铺名称}_{日期}.xlsx and needs product-line diagnosis, growth direction, Top20 image audience/style inference, brand opportunity, organization design, staged execution recommendations, or gpt-image-2 style reference prompts/images. shop-product-diagnosis/SKILL.md local

### `yuce-product-list-export`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/yuce-product-list-export/SKILL.md`
- 功能检索描述：Use when the user wants to export 行情高手/预策平台 “商品列表” data after they have already logged in and manually navigated to the target report page. The skill uses Chrome DevTools MCP to capture the `POST /api/reportFormItem/getCardData` request, replays that API across all pages, and writes the full 商品列表 to an Excel file.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：yuce-product-list-export Yuce Product List Export Use when the user wants to export 行情高手/预策平台 “商品列表” data after they have already logged in and manually navigated to the target report page. The skill uses Chrome DevTools MCP to capture the POST /api/reportFormItem/getCardData request, replays that API across all pages, and writes the full 商品列表 to an Excel file. yuce-product-list-export/SKILL.md local

### `baoyu-article-illustrator`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-article-illustrator/SKILL.md`
- 功能检索描述：Article illustrations: type × style × palette consistency.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：baoyu-article-illustrator Article Illustrator Article illustrations: type × style × palette consistency. creative/baoyu-article-illustrator/SKILL.md local

### `baoyu-comic`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-comic/SKILL.md`
- 功能检索描述：Knowledge comics (知识漫画): educational, biography, tutorial.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：baoyu-comic Knowledge Comic Creator Knowledge comics (知识漫画): educational, biography, tutorial. creative/baoyu-comic/SKILL.md local

### `baoyu-infographic`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-infographic/SKILL.md`
- 功能检索描述：Infographics: 21 layouts x 21 styles (信息图, 可视化).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：baoyu-infographic Infographic Generator Infographics: 21 layouts x 21 styles (信息图, 可视化). creative/baoyu-infographic/SKILL.md local

### `ecommerce-image-skill-architecture`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/ecommerce-image-skill-architecture/SKILL.md`
- 功能检索描述：Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use when designing or refactoring agent skills for product-image analysis, route selection, prompt planning, and staged image generation.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-image-skill-architecture E-commerce Image Skill Architecture Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use when designing or refactoring agent skills for product-image analysis, route selection, prompt planning, and staged image generation. creative/ecommerce-image-skill-architecture/SKILL.md local

### `evolink-gpt-image-2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/evolink-gpt-image-2/SKILL.md`
- 功能检索描述：Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and test script locations.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：evolink-gpt-image-2 Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and test script locations. creative/evolink-gpt-image-2/SKILL.md local

### `gpt-image-2-12api`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/gpt-image-2-12api/SKILL.md`
- 功能检索描述：Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavior, reproducible probing, and known channel quirks.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：gpt-image-2-12api Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavior, reproducible probing, and known channel quirks. creative/gpt-image-2-12api/SKILL.md local

### `gpt生图`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/gpt生图/SKILL.md`
- 功能检索描述：Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, design, or produce any image, illustration, photo, artwork, diagram, infographic, logo, poster, or visual content. Also use when asked to edit, modify, restyle, or transform an existing image. GPT Image 2 is the primary and only generation model in this skill. Supports text-to-image, reference-image generation, local-reference upload, transparent PNG output, and multi-turn iteration. Outputs PNG files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：gpt生图 GPT Image 2 Generation Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, design, or produce any image, illustration, photo, artwork, diagram, infographic, logo, poster, or visual content. Also use when asked to edit, modify, restyle, or transform an existing image. GPT Image 2 is the primary and only generation model in this skill. Supports text-to-image, reference-image generation, local-reference upload, transparent PNG output, and multi-turn iteration. Outputs PNG files. creative/gpt生图/SKILL.md local

### `shopping-basket-visual-planning`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/shopping-basket-visual-planning/SKILL.md`
- 功能检索描述：Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the user needs to know what other products, brands, scenes, or content to study BEFORE visual collection, visual decomposition, or shooting planning.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：shopping-basket-visual-planning Shopping Basket Visual Reference Discovery Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the user needs to know what other products, brands, scenes, or content to study BEFORE visual collection, visual decomposition, or shooting planning. creative/shopping-basket-visual-planning/SKILL.md local

### `single-image-optimization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/single-image-optimization/SKILL.md`
- 功能检索描述：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：single-image-optimization Single Image Optimization Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page. creative/single-image-optimization/SKILL.md local

### `taobao-gpt-image-creative-main-image`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/taobao-gpt-image-creative-main-image/SKILL.md`
- 功能检索描述：Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably via post-processing to avoid AI text乱码.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-gpt-image-creative-main-image Add tag pills as needed... Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably via post-processing to avoid AI text乱码. creative/taobao-gpt-image-creative-main-image/SKILL.md local

### `toapis-gpt-image-2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/toapis-gpt-image-2/SKILL.md`
- 功能检索描述：Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working request formats, task polling, local-image upload flow, supported sizes/quality/background, and known limitations discovered by live testing.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：toapis-gpt-image-2 Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working request formats, task polling, local-image upload flow, supported sizes/quality/background, and known limitations discovered by live testing. creative/toapis-gpt-image-2/SKILL.md local

### `conference-static-html-courseware-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/conference-static-html-courseware-review-loop/SKILL.md`
- 功能检索描述：Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review, Git-backed iteration, and explicit review standards instead of ad-hoc CSS tweaking.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：conference-static-html-courseware-review-loop 大会版静态 HTML 课件重建与审阅闭环 Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review, Git-backed iteration, and explicit review standards instead of ad-hoc CSS tweaking. productivity/conference-static-html-courseware-review-loop/SKILL.md local

### `course-html-ppt-16x9-image-pages`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/course-html-ppt-16x9-image-pages/SKILL.md`
- 功能检索描述：Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy slide layouts.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：course-html-ppt-16x9-image-pages Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy slide layouts. productivity/course-html-ppt-16x9-image-pages/SKILL.md local

### `douyin-link-to-knowledge`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/douyin-link-to-knowledge/SKILL.md`
- 功能检索描述：Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transcribing/validating content, and reconstructing durable knowledge pages. Trigger on natural-language requests like “帮我把这个抖音内容整理到知识库”.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：douyin-link-to-knowledge Douyin Link to Knowledge Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transcribing/validating content, and reconstructing durable knowledge pages. Trigger on natural-language requests like “帮我把这个抖音内容整理到知识库”. productivity/douyin-link-to-knowledge/SKILL.md local

### `dual-source-chapterized-html-ppt-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/dual-source-chapterized-html-ppt-courseware/SKILL.md`
- 功能检索描述：Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to avoid renumbering cascades.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：dual-source-chapterized-html-ppt-courseware Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to avoid renumbering cascades. productivity/dual-source-chapterized-html-ppt-courseware/SKILL.md local

### `ecommerce-bi-operation-skill-planning`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/ecommerce-bi-operation-skill-planning/SKILL.md`
- 功能检索描述：Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡检 SOPs, priority engines, or product-level diagnostic skills for Taobao/e-commerce operations.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-bi-operation-skill-planning E-commerce BI Operation Skill Planning Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡检 SOPs, priority engines, or product-level diagnostic skills for Taobao/e-commerce operations. productivity/ecommerce-bi-operation-skill-planning/SKILL.md local

### `feishu-cli-isolated-config`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/feishu-cli-isolated-config/SKILL.md`
- 功能检索描述：Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentials; use an isolated config file via FEISHU_CONFIG because the CLI's built-in account support is incomplete.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：feishu-cli-isolated-config Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentials; use an isolated config file via FEISHU_CONFIG because the CLI's built-in account support is incomplete. productivity/feishu-cli-isolated-config/SKILL.md local

### `feishu-product-feature-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/feishu-product-feature-doc/SKILL.md`
- 功能检索描述：Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-oriented copy, callouts, comparison tables, and embedded images via official lark-cli.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：feishu-product-feature-doc 玺承BI特色功能介绍 Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-oriented copy, callouts, comparison tables, and embedded images via official lark-cli. productivity/feishu-product-feature-doc/SKILL.md local

### `goal-driven-daily-report-templates`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/goal-driven-daily-report-templates/SKILL.md`
- 功能检索描述：Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use when Peter asks to design job-specific daily/weekly report templates or examples for e-commerce, operations, design, video,客服,外贸,亚马逊等岗位.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：goal-driven-daily-report-templates Goal-Driven Daily Report Templates Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use when Peter asks to design job-specific daily/weekly report templates or examples for e-commerce, operations, design, video,客服,外贸,亚马逊等岗位. productivity/goal-driven-daily-report-templates/SKILL.md local

### `hermes-feishu-gateway-setup`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-gateway-setup/SKILL.md`
- 功能检索描述：Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credentials; use isolated FEISHU_CONFIG for CLI and FEISHU_* env vars plus platforms.feishu for Hermes gateway.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-feishu-gateway-setup Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credentials; use isolated FEISHU_CONFIG for CLI and FEISHU_* env vars plus platforms.feishu for Hermes gateway. productivity/hermes-feishu-gateway-setup/SKILL.md local

### `hermes-feishu-session-debugging`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-session-debugging/SKILL.md`
- 功能检索描述：Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session JSON files, and tool availability. Use when Feishu shows long-running “Still working...”, when a user says a message got no reply, or when uploaded image+text prompts seem to arrive incorrectly.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求
- 检索关键词：hermes-feishu-session-debugging Hermes Feishu Session Debugging Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session JSON files, and tool availability. Use when Feishu shows long-running “Still working...”, when a user says a message got no reply, or when uploaded image+text prompts seem to arrive incorrectly. productivity/hermes-feishu-session-debugging/SKILL.md local

### `html-ppt-conference-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-conference-review-loop/SKILL.md`
- 功能检索描述：Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with explicit readability and layout standards for large venue projection.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt-conference-review-loop HTML-PPT Conference Review Loop Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with explicit readability and layout standards for large venue projection. productivity/html-ppt-conference-review-loop/SKILL.md local

### `html-ppt-course-deck`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-course-deck/SKILL.md`
- 功能检索描述：Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid or visually weak. Use slides.json/slides.yaml for content, CSS for fixed templates, browser full-screen for presenting, and optional in-page editing/export. Especially useful when a mandated PPT template must be reproduced as fixed HTML backgrounds.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：html-ppt-course-deck HTML-PPT Course Deck Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid or visually weak. Use slides.json/slides.yaml for content, CSS for fixed templates, browser full-screen for presenting, and optional in-page editing/export. Especially useful when a mandated PPT template must be reproduced as fixed HTML backgrounds. productivity/html-ppt-course-deck/SKILL.md local

### `html-ppt-font-standardization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-font-standardization/SKILL.md`
- 功能检索描述：Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run an overflow audit after replacement.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：html-ppt-font-standardization HTML-PPT 字体规范方案 Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run an overflow audit after replacement. productivity/html-ppt-font-standardization/SKILL.md local

### `html-ppt-screenshot-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-screenshot-review-loop/SKILL.md`
- 功能检索描述：Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-style decks where readability, layout balance, and consistency matter more than code-level aesthetics.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt-screenshot-review-loop Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-style decks where readability, layout balance, and consistency matter more than code-level aesthetics. productivity/html-ppt-screenshot-review-loop/SKILL.md local

### `html-ppt-stage-fit-and-background-cleanup`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-stage-fit-and-background-cleanup/SKILL.md`
- 功能检索描述：Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds with clean backgrounds plus a separate sharp logo layer, and verify stage safety in browser.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：html-ppt-stage-fit-and-background-cleanup HTML-PPT 固定画布适配与背景去 Logo Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds with clean backgrounds plus a separate sharp logo layer, and verify stage safety in browser. productivity/html-ppt-stage-fit-and-background-cleanup/SKILL.md local

### `html-ppt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-studio-agentskill/SKILL.md`
- 功能检索描述：HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by templates. Use when the user asks for a presentation, PPT, slides, keynote, deck, slideshow, "幻灯片", "演讲稿", "做一份 PPT", "做一份 slides", a reveal-style HTML deck, a 小红书 图文, or any kind of multi-slide pitch/report/sharing document that should look tasteful and be usable with keyboard navigation. Triggers include keywords like "presentation", "ppt", "slides", "deck", "keynote", "reveal", "slideshow", "幻灯片", "演讲稿", "分享稿", "小红书图文", "talk slides", "pitch deck", "tech sharing", "technical presentation".
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt html-ppt — HTML PPT Studio HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by templates. Use when the user asks for a presentation, PPT, slides, keynote, deck, slideshow, "幻灯片", "演讲稿", "做一份 PPT", "做一份 slides", a reveal-style HTML deck, a 小红书 图文, or any kind of multi-slide pitch/report/sharing document that should look tasteful and be usable with keyboard navigation. Triggers include keywords like "presentation", "ppt", "slides", "deck", "keynote", "reveal", "slideshow", "幻灯片", "演讲稿", "分享稿", "小红书图文", "talk slides", "pitch deck", "tech sharing", "technical presentation". productivity/html-ppt-studio-agentskill/SKILL.md local

### `macos-wechat-cli`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-cli/SKILL.md`
- 功能检索描述：Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to install or troubleshoot a WeChat CLI on macOS.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：macos-wechat-cli macOS WeChat CLI Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to install or troubleshoot a WeChat CLI on macOS. productivity/macos-wechat-cli/SKILL.md local

### `macos-wechat-history-decrypt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-history-decrypt/SKILL.md`
- 功能检索描述：Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process existing WeChat chat history, list sessions/groups, search old messages, or export historical chats rather than monitor new messages.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：macos-wechat-history-decrypt macOS WeChat History Decryption Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process existing WeChat chat history, list sessions/groups, search old messages, or export historical chats rather than monitor new messages. productivity/macos-wechat-history-decrypt/SKILL.md local

### `official-lark-cli-feishu-workflows`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/official-lark-cli-feishu-workflows/SKILL.md`
- 功能检索描述：Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenClaw setup already uses ~/.lark-cli. Prefer this over third-party feishu-cli packages for stable bot/user identity handling and less confusing auth behavior.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：official-lark-cli-feishu-workflows Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenClaw setup already uses ~/.lark-cli. Prefer this over third-party feishu-cli packages for stable bot/user identity handling and less confusing auth behavior. productivity/official-lark-cli-feishu-workflows/SKILL.md local

### `real-chrome-web-reader`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/real-chrome-web-reader/SKILL.md`
- 功能检索描述：使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：real-chrome-web-reader 使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。 productivity/real-chrome-web-reader/SKILL.md local

### `reduce-paid-ratio-link-agent-mvp`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-link-agent-mvp/SKILL.md`
- 功能检索描述：Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for close, reduce, keep, or observe actions.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：reduce-paid-ratio-link-agent-mvp 单链接推广花费占比优化 Agent（MVP） Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for close, reduce, keep, or observe actions. productivity/reduce-paid-ratio-link-agent-mvp/SKILL.md local

### `reduce-paid-ratio-plan-evaluator`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-plan-evaluator/SKILL.md`
- 功能检索描述：Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from two source reports, then exporting a decision Excel.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：reduce-paid-ratio-plan-evaluator 降低店铺付费占比：推广计划关停评估 Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from two source reports, then exporting a decision Excel. productivity/reduce-paid-ratio-plan-evaluator/SKILL.md local

### `review-driven-static-html-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/review-driven-static-html-courseware/SKILL.md`
- 功能检索描述：Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML-native presentation instead of service-based editable HTML-PPT or PPT-first thinking.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：review-driven-static-html-courseware Review-driven static HTML courseware Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML-native presentation instead of service-based editable HTML-PPT or PPT-first thinking. productivity/review-driven-static-html-courseware/SKILL.md local

### `sealseek-feature-compare-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/sealseek-feature-compare-doc/SKILL.md`
- 功能检索描述：Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” document where each core module gets its own 3-column comparison table versus traditional tools.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-feature-compare-doc Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” document where each core module gets its own 3-column comparison table versus traditional tools. productivity/sealseek-feature-compare-doc/SKILL.md local

### `sealseek-static-html-courseware-workflow`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/sealseek-static-html-courseware-workflow/SKILL.md`
- 功能检索描述：Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server dependency, and conference-first readability rules.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-static-html-courseware-workflow Sealseek 静态 HTML 课件工作流 Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server dependency, and conference-first readability rules. productivity/sealseek-static-html-courseware-workflow/SKILL.md local

### `shopping-basket-visual-reference-discovery`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/shopping-basket-visual-reference-discovery/SKILL.md`
- 功能检索描述：docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual reference sources for an e-commerce product. Stops at “what should we look at for visual references”; does not produce shooting plans, design plans, copy, or image-generation prompts. ---
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：shopping-basket-visual-reference-discovery Shopping Basket Visual Reference Discovery docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual reference sources for an e-commerce product. Stops at “what should we look at for visual references”; does not produce shooting plans, design plans, copy, or image-generation prompts. --- productivity/shopping-basket-visual-reference-discovery/SKILL.md local

### `single-file-static-html-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/single-file-static-html-courseware/SKILL.md`
- 功能检索描述：Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live editable served HTML. Optimized for polished HTML delivery rather than PPT conversion.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：single-file-static-html-courseware Single-file Static HTML Courseware Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live editable served HTML. Optimized for polished HTML delivery rather than PPT conversion. productivity/single-file-static-html-courseware/SKILL.md local

### `static-html-courseware-feedback-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-feedback-loop/SKILL.md`
- 功能检索描述：Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review standards instead of code-only judgment.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-feedback-loop 静态 HTML 课件反馈闭环 Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review standards instead of code-only judgment. productivity/static-html-courseware-feedback-loop/SKILL.md local

### `static-html-courseware-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop/SKILL.md`
- 功能检索描述：Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of service-based editing.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-review-loop Static HTML 课件重建与审阅循环 Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of service-based editing. productivity/static-html-courseware-review-loop/SKILL.md local

### `static-html-courseware-review-loop-v2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop-v2/SKILL.md`
- 功能检索描述：Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimized for Sealseek-style dark-theme courseware, file:// review, large-font conference display, and screenshot-based QA instead of in-page editing.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：static-html-courseware-review-loop-v2 Static HTML Courseware Review Loop v2 Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimized for Sealseek-style dark-theme courseware, file:// review, large-font conference display, and screenshot-based QA instead of in-page editing. productivity/static-html-courseware-review-loop-v2/SKILL.md local

### `static-html-courseware-shared-assets-and-merge`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-shared-assets-and-merge/SKILL.md`
- 功能检索描述：Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapters into one final HTML without CSS collisions.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-shared-assets-and-merge When to use Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapters into one final HTML without CSS collisions. productivity/static-html-courseware-shared-assets-and-merge/SKILL.md local

### `static-html-deck-to-editable-ppt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-deck-to-editable-ppt/SKILL.md`
- 功能检索描述：Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into truly editable PowerPoint, instead of relying on served HTML decks or screenshot-only PPT export.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：static-html-deck-to-editable-ppt Static HTML Deck → Editable PPT workflow Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into truly editable PowerPoint, instead of relying on served HTML decks or screenshot-only PPT export. productivity/static-html-deck-to-editable-ppt/SKILL.md local

### `taobao-native-search-to-excel`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/taobao-native-search-to-excel/SKILL.md`
- 功能检索描述：使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-native-search-to-excel 使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 productivity/taobao-native-search-to-excel/SKILL.md local

### `taobao-search-to-excel`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/taobao-search-to-excel/SKILL.md`
- 功能检索描述：使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-search-to-excel 使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 productivity/taobao-search-to-excel/SKILL.md local

### `xicheng-bi-feishu-feature-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/xicheng-bi-feishu-feature-doc/SKILL.md`
- 功能检索描述：Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise sales-conversion-oriented but user-appropriate language, callouts, images, and whiteboard diagrams.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：xicheng-bi-feishu-feature-doc Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise sales-conversion-oriented but user-appropriate language, callouts, images, and whiteboard diagrams. productivity/xicheng-bi-feishu-feature-doc/SKILL.md local

### `llm-wiki`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/llm-wiki/SKILL.md`
- 功能检索描述：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki Karpathy's LLM Wiki Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency. research/llm-wiki/SKILL.md local

### `llm-wiki-audit-and-optimization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/llm-wiki-audit-and-optimization/SKILL.md`
- 功能检索描述：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit and Optimization Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base. research/llm-wiki-audit-and-optimization/SKILL.md local

### `cross-agent-skill-packaging`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/cross-agent-skill-packaging/SKILL.md`
- 功能检索描述：Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when publishing to git, syncing into Sealseek, or building a full test bundle with runtime credentials.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：cross-agent-skill-packaging Cross-Agent Skill Packaging Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when publishing to git, syncing into Sealseek, or building a full test bundle with runtime credentials. software-development/cross-agent-skill-packaging/SKILL.md local

### `sealseek-gpt-image-skill-migration`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/sealseek-gpt-image-skill-migration/SKILL.md`
- 功能检索描述：Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use when migrating image-generation capability from another skill (e.g. gemini-image), configuring Sealseek skill manifests, or debugging EvoLink async GPT Image 2 workflows.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-gpt-image-skill-migration Sealseek GPT 生图 Skill 迁移与维护 Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use when migrating image-generation capability from another skill (e.g. gemini-image), configuring Sealseek skill manifests, or debugging EvoLink async GPT Image 2 workflows. software-development/sealseek-gpt-image-skill-migration/SKILL.md local

### `sealseek-skill-sync-and-toolcall-fix`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/sealseek-skill-sync-and-toolcall-fix/SKILL.md`
- 功能检索描述：Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-promotion bug in AgentScope.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-skill-sync-and-toolcall-fix Sealseek skill sync and tool-call fix Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-promotion bug in AgentScope. software-development/sealseek-skill-sync-and-toolcall-fix/SKILL.md local

### `ecom-market-rank`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/ecom-market-rank/SKILL.md`
- 功能检索描述：电商市场排行榜数据分析。适用于用户上传商品排行榜 Excel/CSV 文件（如淘宝生意参谋市场排行导出）时触发。输入：商品排行榜表格文件（xlsx/csv）。输出：文本分析总结 + 离线 HTML 可视化报告。触发场景：用户发送表格并要求分析市场排行、商品排行、品类分析、竞品分析、市场洞察等。不适用于：非商品排行类数据（如财务报表、物流数据、用户行为数据等）。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecom-market-rank 电商市场排行分析 Skill 电商市场排行榜数据分析。适用于用户上传商品排行榜 Excel/CSV 文件（如淘宝生意参谋市场排行导出）时触发。输入：商品排行榜表格文件（xlsx/csv）。输出：文本分析总结 + 离线 HTML 可视化报告。触发场景：用户发送表格并要求分析市场排行、商品排行、品类分析、竞品分析、市场洞察等。不适用于：非商品排行类数据（如财务报表、物流数据、用户行为数据等）。 ecom-market-rank/SKILL.md local

### `mcporter`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/mcporter/SKILL.md`
- 功能检索描述：Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio).
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求
- 检索关键词：mcporter mcporter Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio). mcporter/SKILL.md local

### `taobao-native`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/taobao-native/SKILL.md`
- 功能检索描述：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, request shipping, or perform any Taobao/Tmall shopping operation.
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-native 淘宝桌面客户端购物助手 Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, request shipping, or perform any Taobao/Tmall shopping operation. taobao-native/SKILL.md local

### `web-reader`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/web-reader/SKILL.md`
- 功能检索描述：用真实 Chrome 浏览器（保留登录态）读取网页并压缩 DOM，供 AI 高效分析。适用于需要访问需要登录的网站（淘宝、生意参谋、千牛、飞书等）时抓取页面数据、进行页面操作（点击、填表、滚动）。核心优势：真实 Chrome 不被反爬识别，DOM 压缩后 token 消耗降低 95%。触发场景：抓取淘宝商品数据、读取生意参谋报表、操控任何需要登录的网页、替代 Clawome 或 Chrome DevTools MCP 的浏览器任务。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；MCP server、工具配置、连接或封装需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：web-reader web-reader 用真实 Chrome 浏览器（保留登录态）读取网页并压缩 DOM，供 AI 高效分析。适用于需要访问需要登录的网站（淘宝、生意参谋、千牛、飞书等）时抓取页面数据、进行页面操作（点击、填表、滚动）。核心优势：真实 Chrome 不被反爬识别，DOM 压缩后 token 消耗降低 95%。触发场景：抓取淘宝商品数据、读取生意参谋报表、操控任何需要登录的网页、替代 Clawome 或 Chrome DevTools MCP 的浏览器任务。 web-reader/SKILL.md local

### `detail-page-batch-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/detail-page-batch-optimization/SKILL.md`
- 功能检索描述：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：detail-page-batch-optimization Detail Page Batch Optimization Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent. detail-page-batch-optimization/SKILL.md workspace-skills

### `docx`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/docx/SKILL.md`
- 功能检索描述：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\", \"word document\", \".docx\", or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a \"report\", \"memo\", \"letter\", \"template\", or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spre…
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：docx DOCX creation, editing, and analysis Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\", \"word document\", \".docx\", or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a \"report\", \"memo\", \"letter\", \"template\", or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spre… docx/SKILL.md workspace-skills

### `ecommerce-visual-plan`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/ecommerce-visual-plan/SKILL.md`
- 功能检索描述：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-visual-plan 商品成套视觉规划（ecommerce-visual-plan） Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows. ecommerce-visual-plan/SKILL.md workspace-skills

### `gpt生图`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/gpt生图/SKILL.md`
- 功能检索描述：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GPT 生图能力，不再使用 Gemini 生图。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：gpt生图 gpt生图 使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GPT 生图能力，不再使用 Gemini 生图。 gpt生图/SKILL.md workspace-skills

### `image-understanding`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/image-understanding/SKILL.md`
- 功能检索描述：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：image-understanding 图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。 image-understanding/SKILL.md workspace-skills

### `keyword-assistant`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/keyword-assistant/SKILL.md`
- 功能检索描述：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标题优化、查看热搜排行、提到"关键词分析/挖掘/蓝海词/供需比/热搜榜/飙升词"
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：keyword-assistant Step 0: 登录获取 Cookie（首次使用必做） 关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标题优化、查看热搜排行、提到"关键词分析/挖掘/蓝海词/供需比/热搜榜/飙升词" keyword-assistant/SKILL.md workspace-skills

### `keyword-data-export`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/keyword-data-export/SKILL.md`
- 功能检索描述：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：keyword-data-export Step 0: 环境准备 关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。 keyword-data-export/SKILL.md workspace-skills

### `keyword-traffic`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/keyword-traffic/SKILL.md`
- 功能检索描述：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流量趋势/13个月数据/月度趋势/展现指数/竞争指数/市场均价"，或在使用关键词分析助手后想深入分析某个词的长期走势。 排除：关键词拓展/排行榜（用关键词助手）、创建推广计划（用推广管理助手）。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：keyword-traffic Step 0: 登录获取 Cookie（首次使用必做） 关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流量趋势/13个月数据/月度趋势/展现指数/竞争指数/市场均价"，或在使用关键词分析助手后想深入分析某个词的长期走势。 排除：关键词拓展/排行榜（用关键词助手）、创建推广计划（用推广管理助手）。 keyword-traffic/SKILL.md workspace-skills

### `lark-cli-doc-reader`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/lark-cli-doc-reader/SKILL.md`
- 功能检索描述：使用用户本机 /opt/homebrew/bin/lark-cli 读取飞书云文档。适用于按文档标题/文件名搜索并读取飞书 Docx/Doc/Wiki，或用户给出飞书文档 URL/token 时读取内容。重点规避 OpenClaw/SealClaw 环境变量导致的 lark-cli config bind 误判。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-cli-doc-reader Lark CLI Doc Reader 使用用户本机 /opt/homebrew/bin/lark-cli 读取飞书云文档。适用于按文档标题/文件名搜索并读取飞书 Docx/Doc/Wiki，或用户给出飞书文档 URL/token 时读取内容。重点规避 OpenClaw/SealClaw 环境变量导致的 lark-cli config bind 误判。 lark-cli-doc-reader/SKILL.md workspace-skills

### `market-analysis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/market-analysis/SKILL.md`
- 功能检索描述：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：market-analysis 默认方式：综合排序 + 发货地不限 淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 market-analysis/SKILL.md workspace-skills

### `market-trend`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/market-trend/SKILL.md`
- 功能检索描述：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、持续上升商品、提到"市场排行/趋势分析/排名变化/新上榜/跌出榜" 排除：关键词分析 → 用关键词助手 Skill
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：market-trend 重要：命令格式 市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、持续上升商品、提到"市场排行/趋势分析/排名变化/新上榜/跌出榜" 排除：关键词分析 → 用关键词助手 Skill market-trend/SKILL.md workspace-skills

### `qa-merge-clean`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/qa-merge-clean/SKILL.md`
- 功能检索描述：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出统一结果 3. 从文件名中提取商品ID，新增“商品ID”列 4. 删除“昵称”“回答昵称”“时间”“回答时间”列 5. 调整列宽并冻结首行
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：qa-merge-clean 目标 问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出统一结果 3. 从文件名中提取商品ID，新增“商品ID”列 4. 删除“昵称”“回答昵称”“时间”“回答时间”列 5. 调整列宽并冻结首行 qa-merge-clean/SKILL.md workspace-skills

### `review-cleaning-assistant`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/review-cleaning-assistant/SKILL.md`
- 功能检索描述：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除其他列，仅保留“评价”列 4. 先抽样观察评价内容，再人工判断并删除系统模板、占位文本、与商品无关/无实际商品信息的评价 5. 输出清洗后的 Excel，并附带“已删除评价”sheet 供复核
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：review-cleaning-assistant 目标 评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除其他列，仅保留“评价”列 4. 先抽样观察评价内容，再人工判断并删除系统模板、占位文本、与商品无关/无实际商品信息的评价 5. 输出清洗后的 Excel，并附带“已删除评价”sheet 供复核 review-cleaning-assistant/SKILL.md workspace-skills

### `search-term-blue-ocean-report`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/search-term-blue-ocean-report/SKILL.md`
- 功能检索描述：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；代码仓库、文件路径、PR/Issue、调试或开发任务；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：search-term-blue-ocean-report 适用场景 搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需求。 search-term-blue-ocean-report/SKILL.md workspace-skills

### `search-term-relevance-scorer`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/search-term-relevance-scorer/SKILL.md`
- 功能检索描述：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“给搜索词表做相关度评分”“筛出与本品高相关/低相关的词”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：search-term-relevance-scorer 搜索词相关度评分器 搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“给搜索词表做相关度评分”“筛出与本品高相关/低相关的词”这类需求。 search-term-relevance-scorer/SKILL.md workspace-skills

### `shop-product-diagnosis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/shop-product-diagnosis/SKILL.md`
- 功能检索描述：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex receives a shop product-list spreadsheet and needs product-line diagnosis, growth direction, industry trend, audience inference, brand opportunity, organization design, or staged execution recommendations.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：shop-product-diagnosis Shop Product Diagnosis Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex receives a shop product-list spreadsheet and needs product-line diagnosis, growth direction, industry trend, audience inference, brand opportunity, organization design, or staged execution recommendations. shop-product-diagnosis/SKILL.md workspace-skills

### `single-image-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/single-image-optimization/SKILL.md`
- 功能检索描述：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image detail pages that must stay visually consistent.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：single-image-optimization Single Image Optimization Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image detail pages that must stay visually consistent. single-image-optimization/SKILL.md workspace-skills

### `taobao-item`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/taobao-item/SKILL.md`
- 功能检索描述：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析"
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-item 能力说明 淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析" taobao-item/SKILL.md workspace-skills

### `taobao-market-analysis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/taobao-market-analysis/SKILL.md`
- 功能检索描述：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-market-analysis 默认方式：综合排序 + 发货地不限 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 taobao-market-analysis/SKILL.md workspace-skills

### `taobao-native`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/taobao-native/SKILL.md`
- 功能检索描述：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, request shipping, or perform any Taobao/Tmall shopping operation.
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-native 淘宝桌面客户端购物助手 Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, request shipping, or perform any Taobao/Tmall shopping operation. taobao-native/SKILL.md workspace-skills

### `taobao-search-parser`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/taobao-search-parser/SKILL.md`
- 功能检索描述：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-search-parser 淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”这类需求。 taobao-search-parser/SKILL.md workspace-skills

### `web-image-extractor`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/web-image-extractor/SKILL.md`
- 功能检索描述：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器代码并写入 skill 适合：采集站酷作品图、淘宝商品图、小红书笔记图等
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：web-image-extractor Web Image Extractor 网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器代码并写入 skill 适合：采集站酷作品图、淘宝商品图、小红书笔记图等 web-image-extractor/SKILL.md workspace-skills

### `work-browser`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/work-browser/SKILL.md`
- 功能检索描述：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出适合继续喂给模型的压缩 DOM。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：work-browser 工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出适合继续喂给模型的压缩 DOM。 work-browser/SKILL.md workspace-skills

### `work-browser2`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/work-browser2/SKILL.md`
- 功能检索描述：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适合继续交给模型或下游 parser 的压缩 DOM。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：work-browser2 工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适合继续交给模型或下游 parser 的压缩 DOM。 work-browser2/SKILL.md workspace-skills

### `xmind-cli`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/xmind-cli/SKILL.md`
- 功能检索描述：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：xmind-cli XMind 脑图输出助手 XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 xmind-cli/SKILL.md workspace-skills

### `关键词助手`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/关键词助手/SKILL.md`
- 功能检索描述：生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标题优化、查看热搜排行、提到"关键词分析/挖掘/蓝海词/供需比/热搜榜/飙升词"
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：关键词助手 Step 0: 登录获取 Cookie（首次使用必做） 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标题优化、查看热搜排行、提到"关键词分析/挖掘/蓝海词/供需比/热搜榜/飙升词" 关键词助手/SKILL.md workspace-skills

### `关键词流量解析`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/关键词流量解析/SKILL.md`
- 功能检索描述：万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流量趋势/13个月数据/月度趋势/展现指数/竞争指数/市场均价"，或在使用关键词分析助手后想深入分析某个词的长期走势。 排除：关键词拓展/排行榜（用关键词助手）、创建推广计划（用推广管理助手）。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：关键词流量解析 Step 0: 登录获取 Cookie（首次使用必做） 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流量趋势/13个月数据/月度趋势/展现指数/竞争指数/市场均价"，或在使用关键词分析助手后想深入分析某个词的长期走势。 排除：关键词拓展/排行榜（用关键词助手）、创建推广计划（用推广管理助手）。 关键词流量解析/SKILL.md workspace-skills

### `商品静态四象限分析`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/商品静态四象限分析/SKILL.md`
- 功能检索描述：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数和付费占比给商品分层并准备分析资料”这类需求。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：商品静态四象限分析 输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数和付费占比给商品分层并准备分析资料”这类需求。 商品静态四象限分析/SKILL.md workspace-skills

### `市场排行趋势`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/市场排行趋势/SKILL.md`
- 功能检索描述：生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、持续上升商品、提到"市场排行/趋势分析/排名变化/新上榜/跌出榜" 排除：关键词分析 → 用关键词助手 Skill
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：市场排行趋势 重要：命令格式 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、持续上升商品、提到"市场排行/趋势分析/排名变化/新上榜/跌出榜" 排除：关键词分析 → 用关键词助手 Skill 市场排行趋势/SKILL.md workspace-skills

### `快递超重补差对账`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/快递超重补差对账/SKILL.md`
- 功能检索描述：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 1 元安检费 - 新疆/西藏：0.5kg 以内 5 元；超过 0.5kg 后按“max(floor(重量), 1) × 15”计算 额外输出： - 省份城市统计（按对账明细聚合，支持省份折叠查看城市） - 店铺统计（按对账明细聚合） 适用于“快递超重补差对账”“核对快递公司超重收费”“根据报价单和账单自动对账”场景。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：快递超重补差对账 用途 读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 1 元安检费 - 新疆/西藏：0.5kg 以内 5 元；超过 0.5kg 后按“max(floor(重量), 1) × 15”计算 额外输出： - 省份城市统计（按对账明细聚合，支持省份折叠查看城市） - 店铺统计（按对账明细聚合） 适用于“快递超重补差对账”“核对快递公司超重收费”“根据报价单和账单自动对账”场景。 快递超重补差对账/SKILL.md workspace-skills

### `成套视觉生成`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/成套视觉生成/SKILL.md`
- 功能检索描述：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片生成。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：成套视觉生成 成套视觉生成 基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片生成。 成套视觉生成/SKILL.md workspace-skills

### `推广管理助手`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/推广管理助手/SKILL.md`
- 功能检索描述：万相台无界版推广计划的自动化管理 Skill。通过 API 直接调用万相台后端，支持 P0+P1 全场景： - 货品全站推广（onebpSite）：选品 + 投产比 + 预算，一键创建 - 关键词推广（onebpSearch）：搜索卡位 / 趋势明星 / 流量金卡 / 自定义推广 - 人群推广（onebpDisplay）：高效拉新 / 常客转化 / 人群超市 / 自定义推广 - 计划/广告组查询与启停 - 关键词增删改查 + 质量分查询 - 报表数据查询 触发：用户提到"万相台/推广计划/创建计划/管理计划/广告组/关键词推广/人群推广/货品全站推广/出价/报表"。 排除：纯生意参谋数据分析（用关键词助手）、纯市场排行（用市场排行趋势）。 安全边界：创建/变更类操作必须显式传 `--confirm_submit YES`。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：推广管理助手 Step 0: 登录获取 Cookie（首次使用必做） 万相台无界版推广计划的自动化管理 Skill。通过 API 直接调用万相台后端，支持 P0+P1 全场景： - 货品全站推广（onebpSite）：选品 + 投产比 + 预算，一键创建 - 关键词推广（onebpSearch）：搜索卡位 / 趋势明星 / 流量金卡 / 自定义推广 - 人群推广（onebpDisplay）：高效拉新 / 常客转化 / 人群超市 / 自定义推广 - 计划/广告组查询与启停 - 关键词增删改查 + 质量分查询 - 报表数据查询 触发：用户提到"万相台/推广计划/创建计划/管理计划/广告组/关键词推广/人群推广/货品全站推广/出价/报表"。 排除：纯生意参谋数据分析（用关键词助手）、纯市场排行（用市场排行趋势）。 安全边界：创建/变更类操作必须显式传 --confirm_submit YES 。 推广管理助手/SKILL.md workspace-skills

### `无限画板 Skill 生成器`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/无限画板 Skill 生成器.backup-20260609-1118/SKILL.md`
- 功能检索描述：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优化这个无限画板 skill、根据反馈修改 skill.md。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：无限画板 Skill 生成器 无限画板 · Skill 生成器 根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优化这个无限画板 skill、根据反馈修改 skill.md。 无限画板 Skill 生成器.backup-20260609-1118/SKILL.md workspace-skills

### `淘宝商品助手`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/淘宝商品助手/SKILL.md`
- 功能检索描述：淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析"
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：淘宝商品助手 能力说明 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析" 淘宝商品助手/SKILL.md workspace-skills

### `生意参谋搜索词排行下载`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/生意参谋搜索词排行下载/SKILL.md`
- 功能检索描述：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋排行榜链接”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：生意参谋搜索词排行下载 生意参谋搜索词排行下载 输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋排行榜链接”这类需求。 生意参谋搜索词排行下载/SKILL.md workspace-skills

### `电商凭证管理`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/电商凭证管理/SKILL.md`
- 功能检索描述：多平台电商登录凭证管理。支持淘系(生意参谋/淘宝/1688)、抖音(抖店/千川)、拼多多、京东等平台。 全平台统一通过CDP交互式登录提取Cookie(绕过App-Bound Encryption)。自动检测有效性，失效自动刷新，兜底引导手动提供。 触发：用户首次使用任何电商Skill、提到"登录/Cookie/凭证/过期/重新登录"、业务Skill报Cookie无效 排除：具体业务数据查询 → 用对应业务Skill
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：电商凭证管理 支持平台 多平台电商登录凭证管理。支持淘系(生意参谋/淘宝/1688)、抖音(抖店/千川)、拼多多、京东等平台。 全平台统一通过CDP交互式登录提取Cookie(绕过App-Bound Encryption)。自动检测有效性，失效自动刷新，兜底引导手动提供。 触发：用户首次使用任何电商Skill、提到"登录/Cookie/凭证/过期/重新登录"、业务Skill报Cookie无效 排除：具体业务数据查询 → 用对应业务Skill 电商凭证管理/SKILL.md workspace-skills

### `电商视觉全套生成`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/电商视觉全套生成/SKILL.md`
- 功能检索描述：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块先规划、用户确认后再生成，风格语言在三个模块间统一传承。 触发：帮我生成一套电商视觉、出主图和详情页、做一套完整的电商图片、主图加详情页全套出一下。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：电商视觉全套生成 无限画板 · 电商视觉全套生成 Skill 电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块先规划、用户确认后再生成，风格语言在三个模块间统一传承。 触发：帮我生成一套电商视觉、出主图和详情页、做一套完整的电商图片、主图加详情页全套出一下。 电商视觉全套生成/SKILL.md workspace-skills

### `商品静态四象限分析`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：customized-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/商品静态四象限分析/SKILL.md`
- 功能检索描述：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数和付费占比给商品分层并准备分析资料”这类需求。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：商品静态四象限分析 输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数和付费占比给商品分层并准备分析资料”这类需求。 商品静态四象限分析/SKILL.md customized-skills

### `image-understanding`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：customized-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/图片理解/SKILL.md`
- 功能检索描述：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：image-understanding 图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。 图片理解/SKILL.md customized-skills

### `market-analysis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：customized-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/市场分析/SKILL.md`
- 功能检索描述：市场分析 skill。适合“帮我看看手机的趋势”“分析耳机市场”“查下女装在浙江发货的情况”这类需求。 默认行为对齐当前插件项目里的市场分析功能：综合排序、关键词来自用户输入、发货地默认留空，并自动获取一批靠前商品做分析。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：market-analysis 默认方式：综合排序 + 发货地不限 市场分析 skill。适合“帮我看看手机的趋势”“分析耳机市场”“查下女装在浙江发货的情况”这类需求。 默认行为对齐当前插件项目里的市场分析功能：综合排序、关键词来自用户输入、发货地默认留空，并自动获取一批靠前商品做分析。 市场分析/SKILL.md customized-skills

### `快递超重补差对账`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：customized-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/快递超重补差对账/SKILL.md`
- 功能检索描述：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 1 元安检费 - 新疆/西藏：0.5kg 以内 5 元；超过 0.5kg 后按“max(floor(重量), 1) × 15”计算 额外输出： - 省份城市统计（按对账明细聚合，支持省份折叠查看城市） - 店铺统计（按对账明细聚合） 适用于“快递超重补差对账”“核对快递公司超重收费”“根据报价单和账单自动对账”场景。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：快递超重补差对账 用途 读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 1 元安检费 - 新疆/西藏：0.5kg 以内 5 元；超过 0.5kg 后按“max(floor(重量), 1) × 15”计算 额外输出： - 省份城市统计（按对账明细聚合，支持省份折叠查看城市） - 店铺统计（按对账明细聚合） 适用于“快递超重补差对账”“核对快递公司超重收费”“根据报价单和账单自动对账”场景。 快递超重补差对账/SKILL.md customized-skills

### `work-browser`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：customized-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/浏览器接管/SKILL.md`
- 功能检索描述：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出适合继续喂给模型的压缩 DOM。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：work-browser 查看所有 profile 工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出适合继续喂给模型的压缩 DOM。 浏览器接管/SKILL.md customized-skills

### `taobao-market-analysis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：customized-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/customized_skills/淘宝商品市场分析_原始备份/SKILL.md`
- 功能检索描述：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-market-analysis 默认方式：综合排序 + 发货地不限 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 淘宝商品市场分析_原始备份/SKILL.md customized-skills

### `ai-agent-skill-registry-sync`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/ai-agent-skill-registry-sync/SKILL.md`
- 功能检索描述：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under /Users/pechen/wiki. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ai-agent-skill-registry-sync AI Agent Skill Registry Sync Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under /Users/pechen/wiki. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents. ai-agent-skill-registry-sync/SKILL.md default-workspace-skills

### `detail-page-batch-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/detail-page-batch-optimization/SKILL.md`
- 功能检索描述：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：detail-page-batch-optimization Detail Page Batch Optimization Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent. detail-page-batch-optimization/SKILL.md default-workspace-skills

### `docx`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/docx/SKILL.md`
- 功能检索描述：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\", \"word document\", \".docx\", or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a \"report\", \"memo\", \"letter\", \"template\", or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spre…
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：docx DOCX creation, editing, and analysis Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\", \"word document\", \".docx\", or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a \"report\", \"memo\", \"letter\", \"template\", or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spre… docx/SKILL.md default-workspace-skills

### `成套视觉生成`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-generation/SKILL.md`
- 功能检索描述：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片生成。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：成套视觉生成 成套视觉生成 基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片生成。 ecommerce-visual-generation/SKILL.md default-workspace-skills

### `ecommerce-visual-plan`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-plan/SKILL.md`
- 功能检索描述：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-visual-plan 商品成套视觉规划（ecommerce-visual-plan） Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows. ecommerce-visual-plan/SKILL.md default-workspace-skills

### `电商视觉全套生成`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-suite/SKILL.md`
- 功能检索描述：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块先规划、用户确认后再生成，风格语言在三个模块间统一传承。 触发：帮我生成一套电商视觉、出主图和详情页、做一套完整的电商图片、主图加详情页全套出一下。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：电商视觉全套生成 无限画板 · 电商视觉全套生成 Skill 电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块先规划、用户确认后再生成，风格语言在三个模块间统一传承。 触发：帮我生成一套电商视觉、出主图和详情页、做一套完整的电商图片、主图加详情页全套出一下。 ecommerce-visual-suite/SKILL.md default-workspace-skills

### `gpt生图`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/gpt-image-generation/SKILL.md`
- 功能检索描述：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GPT 生图能力，不再使用 Gemini 生图。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：gpt生图 gpt生图 使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GPT 生图能力，不再使用 Gemini 生图。 gpt-image-generation/SKILL.md default-workspace-skills

### `keyword-assistant`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-assistant/SKILL.md`
- 功能检索描述：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标题优化、查看热搜排行、提到"关键词分析/挖掘/蓝海词/供需比/热搜榜/飙升词"
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：keyword-assistant Step 0: 登录获取 Cookie（首次使用必做） 关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标题优化、查看热搜排行、提到"关键词分析/挖掘/蓝海词/供需比/热搜榜/飙升词" keyword-assistant/SKILL.md default-workspace-skills

### `keyword-data-export`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-data-export/SKILL.md`
- 功能检索描述：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：keyword-data-export Step 0: 环境准备 关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。 keyword-data-export/SKILL.md default-workspace-skills

### `keyword-traffic`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-traffic/SKILL.md`
- 功能检索描述：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流量趋势/13个月数据/月度趋势/展现指数/竞争指数/市场均价"，或在使用关键词分析助手后想深入分析某个词的长期走势。 排除：关键词拓展/排行榜（用关键词助手）、创建推广计划（用推广管理助手）。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：keyword-traffic Step 0: 登录获取 Cookie（首次使用必做） 关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流量趋势/13个月数据/月度趋势/展现指数/竞争指数/市场均价"，或在使用关键词分析助手后想深入分析某个词的长期走势。 排除：关键词拓展/排行榜（用关键词助手）、创建推广计划（用推广管理助手）。 keyword-traffic/SKILL.md default-workspace-skills

### `llm-wiki`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki/SKILL.md`
- 功能检索描述：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki Karpathy's LLM Wiki Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency. llm-wiki/SKILL.md default-workspace-skills

### `llm-wiki-audit-and-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-audit-and-optimization/SKILL.md`
- 功能检索描述：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit and Optimization Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base. llm-wiki-audit-and-optimization/SKILL.md default-workspace-skills

### `llm-wiki-ingest`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-ingest/SKILL.md`
- 功能检索描述：Unified LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal knowledge pages, index/log updates, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal knowledge pages, index/log updates, and audit handoff. llm-wiki-ingest/SKILL.md default-workspace-skills

### `llm-wiki-recompile-runner`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-recompile-runner/SKILL.md`
- 功能检索描述：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and course-transcript-to-knowledge, then verifies post-ingest quality.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：llm-wiki-recompile-runner LLM Wiki Recompile Runner Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and course-transcript-to-knowledge, then verifies post-ingest quality. llm-wiki-recompile-runner/SKILL.md default-workspace-skills

### `market-analysis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-analysis/SKILL.md`
- 功能检索描述：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：market-analysis 默认方式：综合排序 + 发货地不限 淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 market-analysis/SKILL.md default-workspace-skills

### `market-trend`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-trend/SKILL.md`
- 功能检索描述：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、持续上升商品、提到"市场排行/趋势分析/排名变化/新上榜/跌出榜" 排除：关键词分析 → 用关键词助手 Skill
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：market-trend 重要：命令格式 市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、持续上升商品、提到"市场排行/趋势分析/排名变化/新上榜/跌出榜" 排除：关键词分析 → 用关键词助手 Skill market-trend/SKILL.md default-workspace-skills

### `qa-merge-clean`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/qa-merge-clean/SKILL.md`
- 功能检索描述：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出统一结果 3. 从文件名中提取商品ID，新增“商品ID”列 4. 删除“昵称”“回答昵称”“时间”“回答时间”列 5. 调整列宽并冻结首行
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：qa-merge-clean 目标 问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出统一结果 3. 从文件名中提取商品ID，新增“商品ID”列 4. 删除“昵称”“回答昵称”“时间”“回答时间”列 5. 调整列宽并冻结首行 qa-merge-clean/SKILL.md default-workspace-skills

### `review-cleaning-assistant`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/review-cleaning-assistant/SKILL.md`
- 功能检索描述：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除其他列，仅保留“评价”列 4. 先抽样观察评价内容，再人工判断并删除系统模板、占位文本、与商品无关/无实际商品信息的评价 5. 输出清洗后的 Excel，并附带“已删除评价”sheet 供复核
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：review-cleaning-assistant 目标 评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除其他列，仅保留“评价”列 4. 先抽样观察评价内容，再人工判断并删除系统模板、占位文本、与商品无关/无实际商品信息的评价 5. 输出清洗后的 Excel，并附带“已删除评价”sheet 供复核 review-cleaning-assistant/SKILL.md default-workspace-skills

### `search-term-blue-ocean-report`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-blue-ocean-report/SKILL.md`
- 功能检索描述：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；代码仓库、文件路径、PR/Issue、调试或开发任务；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：search-term-blue-ocean-report 适用场景 搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需求。 search-term-blue-ocean-report/SKILL.md default-workspace-skills

### `search-term-relevance-scorer`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-relevance-scorer/SKILL.md`
- 功能检索描述：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“给搜索词表做相关度评分”“筛出与本品高相关/低相关的词”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：search-term-relevance-scorer 搜索词相关度评分器 搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“给搜索词表做相关度评分”“筛出与本品高相关/低相关的词”这类需求。 search-term-relevance-scorer/SKILL.md default-workspace-skills

### `shop-product-diagnosis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/shop-product-diagnosis/SKILL.md`
- 功能检索描述：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex receives a shop product-list spreadsheet and needs product-line diagnosis, growth direction, industry trend, audience inference, brand opportunity, organization design, or staged execution recommendations.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：shop-product-diagnosis Shop Product Diagnosis Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex receives a shop product-list spreadsheet and needs product-line diagnosis, growth direction, industry trend, audience inference, brand opportunity, organization design, or staged execution recommendations. shop-product-diagnosis/SKILL.md default-workspace-skills

### `single-image-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/single-image-optimization/SKILL.md`
- 功能检索描述：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image detail pages that must stay visually consistent.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：single-image-optimization Single Image Optimization Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image detail pages that must stay visually consistent. single-image-optimization/SKILL.md default-workspace-skills

### `无限画板 Skill 生成器`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/skill-builder/SKILL.md`
- 功能检索描述：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优化这个无限画板 skill、根据反馈修改 skill.md。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：无限画板 Skill 生成器 无限画板 · Skill 生成器 根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优化这个无限画板 skill、根据反馈修改 skill.md。 skill-builder/SKILL.md default-workspace-skills

### `生意参谋搜索词排行下载`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/sycm-search-rank-download/SKILL.md`
- 功能检索描述：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋排行榜链接”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：生意参谋搜索词排行下载 生意参谋搜索词排行下载 输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋排行榜链接”这类需求。 sycm-search-rank-download/SKILL.md default-workspace-skills

### `taobao-item`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-item/SKILL.md`
- 功能检索描述：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析"
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-item 能力说明 淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析" taobao-item/SKILL.md default-workspace-skills

### `taobao-native`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-native/SKILL.md`
- 功能检索描述：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, request shipping, or perform any Taobao/Tmall shopping operation.
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-native 淘宝桌面客户端购物助手 Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, request shipping, or perform any Taobao/Tmall shopping operation. taobao-native/SKILL.md default-workspace-skills

### `taobao-search-parser`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-search-parser/SKILL.md`
- 功能检索描述：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-search-parser 淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”这类需求。 taobao-search-parser/SKILL.md default-workspace-skills

### `web-image-extractor`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/web-image-extractor/SKILL.md`
- 功能检索描述：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器代码并写入 skill 适合：采集站酷作品图、淘宝商品图、小红书笔记图等
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：web-image-extractor Web Image Extractor 网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器代码并写入 skill 适合：采集站酷作品图、淘宝商品图、小红书笔记图等 web-image-extractor/SKILL.md default-workspace-skills

### `work-browser`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser/SKILL.md`
- 功能检索描述：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出适合继续喂给模型的压缩 DOM。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：work-browser 工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出适合继续喂给模型的压缩 DOM。 work-browser/SKILL.md default-workspace-skills

### `work-browser2`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser2/SKILL.md`
- 功能检索描述：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适合继续交给模型或下游 parser 的压缩 DOM。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：work-browser2 工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适合继续交给模型或下游 parser 的压缩 DOM。 work-browser2/SKILL.md default-workspace-skills

### `xmind-cli`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/xmind-cli/SKILL.md`
- 功能检索描述：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：xmind-cli XMind 脑图输出助手 XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 xmind-cli/SKILL.md default-workspace-skills

### `detail-page-batch-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：migration-bundle
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/hermes/SKILL.md`
- 功能检索描述：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：detail-page-batch-optimization Detail Page Batch Optimization Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent. detail-page-batch-optimization/hermes/SKILL.md migration-bundle

### `detail-page-batch-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：migration-bundle
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/sealseek/SKILL.md`
- 功能检索描述：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：detail-page-batch-optimization Detail Page Batch Optimization Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent. detail-page-batch-optimization/sealseek/SKILL.md migration-bundle

### `guanshu-review`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：migration-bundle
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/fe-guanshu-review/SKILL.md`
- 功能检索描述：观数浏览器扩展前端代码评审工具。对分支代码进行规范检查，生成评审报告。检查项：P0-颜色硬编码、内联样式、if嵌套、重复造轮子、Content Script挂载方式；P1-BEM命名、魔法数字、第三方库引入；P2-文件职责单一、长文件拆分。仅适用于 xc-sealseek-extension-sycm 项目。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：guanshu-review 观数前端代码评审工具 观数浏览器扩展前端代码评审工具。对分支代码进行规范检查，生成评审报告。检查项：P0-颜色硬编码、内联样式、if嵌套、重复造轮子、Content Script挂载方式；P1-BEM命名、魔法数字、第三方库引入；P2-文件职责单一、长文件拆分。仅适用于 xc-sealseek-extension-sycm 项目。 fe-guanshu-review/SKILL.md migration-bundle

### `gemini-image`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：migration-bundle
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/gemini-image/SKILL.md`
- 功能检索描述：Generate, edit, and iterate on images using Gemini image models via 12API. Use when the user asks to create, generate, draw, design, or produce any image, illustration, photo, artwork, diagram, infographic, or visual content. Also use when asked to edit, modify, restyle, or transform an existing image. Triggers on phrases like "generate an image", "draw me", "create a picture", "make an illustration", "edit this image", "change the style", "生成图片", "画一张", "做一张图", "修改图片", "P图", "生成一个logo", "设计一张海报". Supports text-to-image, image editing, multi-turn iteration, Google search grounding, and thinking mode control. Outputs PNG files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：gemini-image Gemini Image Generation Generate, edit, and iterate on images using Gemini image models via 12API. Use when the user asks to create, generate, draw, design, or produce any image, illustration, photo, artwork, diagram, infographic, or visual content. Also use when asked to edit, modify, restyle, or transform an existing image. Triggers on phrases like "generate an image", "draw me", "create a picture", "make an illustration", "edit this image", "change the style", "生成图片", "画一张", "做一张图", "修改图片", "P图", "生成一个logo", "设计一张海报". Supports text-to-image, image editing, multi-turn iteration, Google search grounding, and thinking mode control. Outputs PNG files. gemini-image/SKILL.md migration-bundle

### `outline-paper-builder`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：migration-bundle
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/outline-paper-builder/SKILL.md`
- 功能检索描述：Reconstruct complete teaching-grade knowledge from mm/xmind outlines and output reviewable artifacts: lecture notes, optional long-form paper, and lecture-note-derived QA pairs. Use when the user wants high-coverage, non-omitting course knowledge extraction from sparse mindmap outlines.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：outline-paper-builder Outline Paper Builder Reconstruct complete teaching-grade knowledge from mm/xmind outlines and output reviewable artifacts: lecture notes, optional long-form paper, and lecture-note-derived QA pairs. Use when the user wants high-coverage, non-omitting course knowledge extraction from sparse mindmap outlines. outline-paper-builder/SKILL.md migration-bundle

### `single-image-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：migration-bundle
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/hermes/SKILL.md`
- 功能检索描述：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：single-image-optimization Single Image Optimization Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page. single-image-optimization/hermes/SKILL.md migration-bundle

### `single-image-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：migration-bundle
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/sealseek/SKILL.md`
- 功能检索描述：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：single-image-optimization Single Image Optimization Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page. single-image-optimization/sealseek/SKILL.md migration-bundle

### `xmind-cli`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/XMindCLI交付包V2/package/skills/xmind-cli/SKILL.md`
- 功能检索描述：XMind 脑图输出助手 —— 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：xmind-cli 触发规则 XMind 脑图输出助手 —— 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 XMindCLI交付包V2/package/skills/xmind-cli/SKILL.md standalone-local

### `taobao-market-analysis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/sealseek/backup/淘宝商品市场分析_20260418_210055/SKILL.md`
- 功能检索描述：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-market-analysis 默认方式：综合排序 + 发货地不限 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 backup/淘宝商品市场分析_20260418_210055/SKILL.md standalone-local

### `商品成套视觉规划skill`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/商品成套视觉规划skill/SKILL.md`
- 功能检索描述：把一个商品的多源证据（搜索词、评价、问大家、商品图）整理成**可执行的成套视觉规划**，输出给后续设计、生图、详情页优化或投放团队直接使用的规划结果。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：商品成套视觉规划skill 商品成套视觉规划（ecommerce-visual-plan） 把一个商品的多源证据（搜索词、评价、问大家、商品图）整理成**可执行的成套视觉规划**，输出给后续设计、生图、详情页优化或投放团队直接使用的规划结果。 商品成套视觉规划skill/SKILL.md standalone-local

### `货号跨店铺表现差异分析`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/sealseek/货号跨店铺表现差异分析/SKILL.md`
- 功能检索描述：🎯 任务目标 基于指定货号或全量数据，分析并识别同一货号在不同店铺/链接间销售表现差异显著的商品，帮助商家发现潜在的分销优化机会。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：货号跨店铺表现差异分析 货号跨店铺表现差异分析 🎯 任务目标 基于指定货号或全量数据，分析并识别同一货号在不同店铺/链接间销售表现差异显著的商品，帮助商家发现潜在的分销优化机会。 货号跨店铺表现差异分析/SKILL.md standalone-local

