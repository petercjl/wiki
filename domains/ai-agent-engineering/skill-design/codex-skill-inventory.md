---
title: Codex Skill 注册页
type: concept
created: 2026-06-12
updated: 2026-06-12
domain: ai-agent-engineering
tags: [ai-agent, codex, skill, registry]
sources:
  - /Users/pechen/.codex/skills
status: active
---
# Codex Skill 注册页

本页记录 Codex 环境中的 skill，用于 AI Agent 检索“是否已有类似 skill”并定位原始 SKILL.md。

## 维护范围

来源目录：

- `/Users/pechen/.codex/skills`

- 说明：Codex local business skills and system skills.
- 当前记录数量：18

归属分类统计：

- 个人/项目自定义: 13
- 系统/内置: 5

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/ai-agent-engineering/skill-design/personal-ai-agent-skill-registry|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 知识库 / 知识管理 / LLM Wiki

- `skill-creator` (系统/内置 / system)：Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an exist…
- `ai-agent-skill-registry-sync` (个人/项目自定义 / local)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, the…
- `brand-planning-report` (个人/项目自定义 / local)：Generate a user-facing ecommerce brand planning HTML report from a standard 店铺商品 Excel workbook, using Peter's brand-str…
- `llm-wiki` (个人/项目自定义 / local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compil…
- `llm-wiki-audit-and-optimization` (个人/项目自定义 / local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or w…
- `llm-wiki-ingest` (个人/项目自定义 / local)：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled int…
- `llm-wiki-recompile-runner` (个人/项目自定义 / local)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit find…

### 视觉 / 内容 / 课件生产

- `imagegen` (系统/内置 / system)：Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, text…
- `course-deck-factory` (个人/项目自定义 / local)：Build editable course slide decks from a standardized deck spec using Node.js, PptxGenJS, local fonts, structured page t…
- `image-detail-page` (个人/项目自定义 / local)：根据产品白底图和品类，全自动推断模型、人群、风格，并一站式生成13个策划文件及对应电商图片。 当用户提到主图详情页、电商策划、白底图出方案、主图设计、详情页设计、电商视觉方案时触发。
- `seedance-commerce-video` (个人/项目自定义 / local)：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn p…
- `shop-product-diagnosis` (个人/项目自定义 / local)：Diagnose an ecommerce shop from a standard 店铺商品 Excel workbook and produce a tabbed HTML report plus an XMind action map…

### 电商 / 商品 / 品牌运营

- `ecommerce-profit-statement-automation` (个人/项目自定义 / local)：Automate ecommerce platform profit statement workbooks from settlement/funds/account bills. Use when the user wants to t…
- `yuce-product-list-export` (个人/项目自定义 / local)：Use when the user wants to export 行情高手/预策平台 “商品列表” data after they have already logged in and manually navigated to the …

### Agent 工程 / Skill / Plugin / MCP

- `openai-docs` (系统/内置 / system)：Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citati…
- `plugin-creator` (系统/内置 / system)：Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/fi…
- `skill-installer` (系统/内置 / system)：Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list ins…
- `internal-plugin-workflow` (个人/项目自定义 / local)：Use when the user wants to build or iterate an internal Chrome browser extension against a page they have already opened…

## Skill 详情

### `imagegen`

- Agent / 环境：Codex
- 归属分类：系统/内置
- 归属依据：Codex `.system` 内置 skill。
- 来源类型：system
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/.system/imagegen/SKILL.md`
- 功能检索描述：Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：imagegen Image Generation Skill Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas. .system/imagegen/SKILL.md system

### `openai-docs`

- Agent / 环境：Codex
- 归属分类：系统/内置
- 归属依据：Codex `.system` 内置 skill。
- 来源类型：system
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/.system/openai-docs/SKILL.md`
- 功能检索描述：Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求
- 检索关键词：openai-docs OpenAI Docs Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains. .system/openai-docs/SKILL.md system

### `plugin-creator`

- Agent / 环境：Codex
- 归属分类：系统/内置
- 归属依据：Codex `.system` 内置 skill。
- 来源类型：system
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/.system/plugin-creator/SKILL.md`
- 功能检索描述：Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, valid manifest defaults, and personal-marketplace entries by default. Use when Codex needs to create a new personal plugin, add optional plugin structure, generate or update marketplace entries for plugin ordering and availability metadata, or update an existing local plugin during development with the CLI-driven cachebuster and reinstall flow.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：plugin-creator Plugin Creator Create and scaffold plugin directories for Codex with a required .codex-plugin/plugin.json , optional plugin folders/files, valid manifest defaults, and personal-marketplace entries by default. Use when Codex needs to create a new personal plugin, add optional plugin structure, generate or update marketplace entries for plugin ordering and availability metadata, or update an existing local plugin during development with the CLI-driven cachebuster and reinstall flow. .system/plugin-creator/SKILL.md system

### `skill-creator`

- Agent / 环境：Codex
- 归属分类：系统/内置
- 归属依据：Codex `.system` 内置 skill。
- 来源类型：system
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/.system/skill-creator/SKILL.md`
- 功能检索描述：Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：skill-creator Skill Creator Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations. .system/skill-creator/SKILL.md system

### `skill-installer`

- Agent / 环境：Codex
- 归属分类：系统/内置
- 归属依据：Codex `.system` 内置 skill。
- 来源类型：system
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/.system/skill-installer/SKILL.md`
- 功能检索描述：Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：skill-installer Skill Installer Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos). .system/skill-installer/SKILL.md system

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

