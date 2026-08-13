---
title: Codex Skill 注册页
type: concept
created: 2026-08-10
updated: 2026-08-10
domain: AI Agent工程
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
- 当前记录数量：60

归属分类统计：

- 个人/项目自定义: 52
- 系统/内置: 6
- 归档/备份: 2

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 知识库 / 知识管理 / LLM Wiki

- `openai-docs` (系统/内置 / system)：Use for Codex models/pricing, scheduled tasks, skills, settings, setup, troubleshooting, customization, automations, and…
- `skill-creator` (系统/内置 / system)：Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an exist…
- `ai-agent-skill-registry-sync` (个人/项目自定义 / local)：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, …
- `brand-planning-report` (个人/项目自定义 / local)：Generate a user-facing ecommerce brand planning HTML report from a standard 店铺商品 Excel workbook, using Peter's brand-str…
- `dws` (个人/项目自定义 / local)：管理钉钉产品能力(AI表格/AI搜问/日历/通讯录/群聊与机器人/待办/审批/考勤/日志/DING消息/开放平台文档/钉钉文档/钉钉云盘/AI听记/邮箱/在线电子表格/知识库等)。当用户需要操作表格数据、管理日程会议、模糊找人/查谁负责某事…
- `lark-structured-doc-writer` (个人/项目自定义 / local)：Create or substantially rewrite clear, complete, highly readable Lark/Feishu project and knowledge documents. Use when a…
- `llm-wiki` (个人/项目自定义 / local)：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question tha…
- `llm-wiki-audit-and-optimization` (个人/项目自定义 / local)：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and…
- `llm-wiki-bootstrap` (个人/项目自定义 / local)：Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set …
- `llm-wiki-ingest` (个人/项目自定义 / local)：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the…
- `sealseek-course-doc-writer` (个人/项目自定义 / local)：Write and maintain SealSeek/玺虾 learner-facing course documents, Feishu handbooks, chapter sub-documents, and copyable pr…

### 视觉 / 内容 / 课件生产

- `imagegen` (系统/内置 / system)：Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, text…
- `1688-opportunity-sourcing-research` (个人/项目自定义 / local)：Research products and suppliers on 1688 with category-first sourcing across market-proven, novel, aesthetic, scenario, p…
- `1688-opportunity-sourcing-research` (归档/备份 / archived-or-backup)：Research products and suppliers on 1688 with category-first sourcing across market-proven, novel, aesthetic, scenario, p…
- `ai-story-video-studio` (个人/项目自定义 / local)：Create complete story-driven AI video plans from either product inputs or non-product story/theme ideas. Use when the us…
- `alibaba-review-report` (个人/项目自定义 / local)：Generate an Alibaba.com International store-review report from a product-detail URL by calling the stable alicli CLI to …
- `character-reference-turnaround` (个人/项目自定义 / local)：Create consistent character references and three-view turnaround sheets for AI visual/video production. Use when the use…
- `compact-commerce-ui` (个人/项目自定义 / local)：Orchestrate the system-wide commerce-ui CLI to create or redesign readable, modular HTML business reports, ecommerce das…
- `course-deck-factory` (个人/项目自定义 / local)：Build editable course slide decks from a standardized deck spec using Node.js, PptxGenJS, local fonts, structured page t…
- `dycli` (个人/项目自定义 / local)：Use when the user wants an Agent to operate dycli, automate read-only Douyin Web data collection, search or download Dou…
- `ecommerce-shop-growth-diagnosis` (个人/项目自定义 / local)：Diagnose one ecommerce target shop from a standard product-ranking or shop-product .xlsx workbook plus user-confirmed bu…
- `editable-poster-psd-rebuild` (个人/项目自定义 / local)：Rebuild a flattened AI-generated ecommerce poster as a layered Photoshop PSD with a text-free background, hidden origina…
- `image-detail-page` (个人/项目自定义 / local)：根据产品白底图和品类，全自动推断模型、人群、风格，并一站式生成13个策划文件及对应电商图片。 当用户提到主图详情页、电商策划、白底图出方案、主图设计、详情页设计、电商视觉方案时触发。
- `无限画板 Skill 生成器` (个人/项目自定义 / local)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生…
- `libtv-cli` (个人/项目自定义 / local)：>- LibTV 官方 CLI（libtv）：在命令行里完整操作 / 运行 LibTV 画布。 凡是和 LibTV 画布 / 项目 / 节点 / 模型 / 素材相关的操作，一律通过 libtv CLI 完成， 包括在提供 `libtv vi…
- `sealseek-canvas` (个人/项目自定义 / local)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authen…
- `seedance-commerce-video` (个人/项目自定义 / local)：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn p…
- `seedance-video` (个人/项目自定义 / local)：Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedan…
- `seedaudiocli` (个人/项目自定义 / local)：Use the local `seedaudiocli` system CLI to generate audio with EvoLink Doubao Seed-Audio 1.0. Use when an Agent needs ba…
- `shop-product-diagnosis` (个人/项目自定义 / local)：Diagnose an ecommerce shop from a standard 店铺商品 Excel workbook and produce a tabbed HTML report plus an XMind action map…
- `无限画板 Skill 生成器` (归档/备份 / archived-or-backup)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生…
- `skill-forward-test` (个人/项目自定义 / local)：Validate newly created or updated Codex skills with a clean sub-agent regression loop. Use when the user asks to test, v…
- `workctl-operator` (个人/项目自定义 / local)：安装、升级、认证、发现并使用 Work Agent CLI (`workctl`)。适用于通过 `workctl schema` 发现并调用阿里巴巴国际站商家经营工具，处理店铺经营数据、广告、发品、商品优化、AI 图片/视频、旺铺、选品、物…

### 电商 / 商品 / 品牌运营

- `dmp-ai-competitor-research` (个人/项目自定义 / local)：自动执行 DMP/达摩盘 AI 竞品研究。输入用户自己的淘宝/天猫商品编号，复用或打开可调试 Chrome，检查达摩盘智能对话是否已打开，等待登录/导航，向达摩盘 AI 提问内部工具提示词，收集竞品销售、搜索、推广、人群、人群资产和店铺层数…
- `dmp-ai-prompt-pack` (个人/项目自定义 / local)：Generate a copy-ready HTML prompt manual for DMP/达摩盘 AI competitor research from one Taobao/Tmall item ID. Use when the …
- `ecommerce-profit-statement-automation` (个人/项目自定义 / local)：Automate ecommerce platform profit statement workbooks from settlement/funds/account bills. Use when the user wants to t…
- `international-station-seller-assistant` (个人/项目自定义 / local)：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data throug…
- `market-ranking-growth-report` (个人/项目自定义 / local)：Generate a Word growth strategy report from 12 months of marketplace ranking spreadsheets for any ecommerce shop and cat…
- `product-story-ad-video` (个人/项目自定义 / local)：Create and run a project-style workflow for story-driven ecommerce product video ads. Use when the user wants to promote…
- `script-writing-studio` (个人/项目自定义 / local)：端到端中文剧本创作工作室。用于剧本、竖屏短剧、动画脚本、动态漫画脚本、完整剧本扩写、台词稿、项目资产库、AI 视频分镜、Seedance 2.0 视频提示词、后期 BGM/配乐/声音设计的完整开发流程。用户想从灵感写故事、生成大纲或项目档案…
- `story-driven-product-ad` (个人/项目自定义 / local)：Use when creating emotionally driven short-video story ads, Douyin/TikTok product-placement stories, product-in-story sc…
- `wdt-dingtalk-logistics-dashboard` (个人/项目自定义 / local)：Maintain a DingTalk AI table logistics anomaly dashboard for ecommerce orders. Use when the user asks to initialize or u…
- `wdt-logistics-anomaly-report` (个人/项目自定义 / local)：End-to-end 旺店通/WDT order logistics anomaly analysis. Use when the user asks to analyze ecommerce order logistics, find a…
- `yuce-product-list-export` (个人/项目自定义 / local)：Use when the user wants to export 行情高手/预策平台 “商品列表” data after they have already logged in and manually navigated to the …

### Agent 工程 / Skill / Plugin / MCP

- `plugin-creator` (系统/内置 / system)：Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/fi…
- `review-agent` (系统/内置 / system)：Perform a read-only, defect-first review of a specified code change and return every actionable finding. Use when anothe…
- `skill-installer` (系统/内置 / system)：Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list ins…
- `ai-dianjing-growth-opportunity` (个人/项目自定义 / local)：Analyze an Alibaba Wanxiangtai AI点睛 keyword-promotion plan from a one.alimama.com plan link. Use when the user wants a p…
- `goal-driven-video-qa` (个人/项目自定义 / local)：Inspect a video against quality goals inferred from the current conversation, explicit user request, prompt, script, sto…
- `internal-plugin-workflow` (个人/项目自定义 / local)：Use when the user wants to build or iterate an internal Chrome browser extension against a page they have already opened…
- `joinquant-strategy` (个人/项目自定义 / local)：Write, review, debug, and validate JoinQuant/JQData 聚宽 quantitative trading strategy scripts that will be copied into th…
- `jqcli` (个人/项目自定义 / local)：Use when Codex needs to operate or maintain the jqcli JoinQuant project: authenticate, inspect strategies, list or run b…
- `mac-no-reboot-rescue` (个人/项目自定义 / local)：Diagnose and relieve recurring macOS slowdowns without rebooting. Use when the user says their Mac is slow, stuck, beach…
- `portable-skill-creator` (个人/项目自定义 / local)：Create, update, review, or test shareable Agent Skills without leaking author-machine information or binding the core wo…
- `quant-local-research` (个人/项目自定义 / local)：Use when Peter asks to research, backtest, validate, optimize, compare, or port ETF/stock quantitative trading strategie…
- `sealseek-chat-control` (个人/项目自定义 / local)：Control and inspect the user's running SealSeek/SealClaw conversations through the local `sealseek-chat` CLI. Use when C…
- `sealseek-execution-auditor` (个人/项目自定义 / local)：Audit SealSeek conversation execution traces to reconstruct tool calls, retries, fallbacks, side effects, skipped valida…
- `ths-rebalance-planner` (个人/项目自定义 / local)：Generate a rebalance plan for the currently selected Tonghuashun 同花顺 account from pasted JoinQuant/模拟策略 target holdings.…
- `wdt-inventory-replenishment` (个人/项目自定义 / local)：Run Wangdian ERP inventory replenishment monitoring with wdtcli, derive SKU warning thresholds from historical sales, ge…
- `workctl` (个人/项目自定义 / local)：管理 Work Agent 平台能力。通过 `workctl schema` 发现动态产品和命令，再用结构化输出执行操作。

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
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/.system/openai-docs/SKILL.md`
- 功能检索描述：Use for Codex models/pricing, scheduled tasks, skills, settings, setup, troubleshooting, customization, automations, and self-knowledge—including 'you,' 'your,' 'this app,' or 'this coding agent' when they refer to Codex—and for OpenAI APIs/products and ChatGPT Work. Also use for model choice/migration, prompting, SDKs, Responses, Realtime, agents, evals, and Chat/Work/Codex comparisons. Do not use for generic app/software tasks that merely mention Codex.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：openai-docs OpenAI Docs Use for Codex models/pricing, scheduled tasks, skills, settings, setup, troubleshooting, customization, automations, and self-knowledge—including 'you,' 'your,' 'this app,' or 'this coding agent' when they refer to Codex—and for OpenAI APIs/products and ChatGPT Work. Also use for model choice/migration, prompting, SDKs, Responses, Realtime, agents, evals, and Chat/Work/Codex comparisons. Do not use for generic app/software tasks that merely mention Codex. .system/openai-docs/SKILL.md system

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

### `review-agent`

- Agent / 环境：Codex
- 归属分类：系统/内置
- 归属依据：Codex `.system` 内置 skill。
- 来源类型：system
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/.system/review-agent/SKILL.md`
- 功能检索描述：Perform a read-only, defect-first review of a specified code change and return every actionable finding. Use when another agent delegates review of uncommitted changes, a base-branch diff, a commit, or custom review instructions.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：review-agent Review Agent Perform a read-only, defect-first review of a specified code change and return every actionable finding. Use when another agent delegates review of uncommitted changes, a base-branch diff, a commit, or custom review instructions. .system/review-agent/SKILL.md system

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

### `1688-opportunity-sourcing-research`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/1688-opportunity-sourcing-research/SKILL.md`
- 功能检索描述：Research products and suppliers on 1688 with category-first sourcing across market-proven, novel, aesthetic, scenario, premium, and bundle strategies, using installed 1688 CLI evidence, URL-based image review, a clickable HTML portfolio report, and a traceable candidate JSON. Use this Skill whenever the user asks to use 1688 to find products, source products, select styles, explore product opportunities, or research suppliers, including workflows that start from an upstream AI点睛 `product-opportunities.json` handoff.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：1688-opportunity-sourcing-research 1688分类机会选品研究 Research products and suppliers on 1688 with category-first sourcing across market-proven, novel, aesthetic, scenario, premium, and bundle strategies, using installed 1688 CLI evidence, URL-based image review, a clickable HTML portfolio report, and a traceable candidate JSON. Use this Skill whenever the user asks to use 1688 to find products, source products, select styles, explore product opportunities, or research suppliers, including workflows that start from an upstream AI点睛 product-opportunities.json handoff. 1688-opportunity-sourcing-research/SKILL.md local

### `1688-opportunity-sourcing-research`

- Agent / 环境：Codex
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/1688-opportunity-sourcing-research.backup-20260806-1420/SKILL.md`
- 功能检索描述：Research products and suppliers on 1688 with category-first sourcing across market-proven, novel, aesthetic, scenario, premium, and bundle strategies, using installed 1688 CLI evidence, URL-based image review, a clickable HTML portfolio report, and a traceable candidate JSON. Use this Skill whenever the user asks to use 1688 to find products, source products, select styles, explore product opportunities, or research suppliers, including workflows that start from an upstream AI点睛 `product-opportunities.json` handoff.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：1688-opportunity-sourcing-research 1688分类机会选品研究 Research products and suppliers on 1688 with category-first sourcing across market-proven, novel, aesthetic, scenario, premium, and bundle strategies, using installed 1688 CLI evidence, URL-based image review, a clickable HTML portfolio report, and a traceable candidate JSON. Use this Skill whenever the user asks to use 1688 to find products, source products, select styles, explore product opportunities, or research suppliers, including workflows that start from an upstream AI点睛 product-opportunities.json handoff. 1688-opportunity-sourcing-research.backup-20260806-1420/SKILL.md archived-or-backup

### `ai-agent-skill-registry-sync`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/ai-agent-skill-registry-sync/SKILL.md`
- 功能检索描述：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under $WIKI_ROOT. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ai-agent-skill-registry-sync AI Agent Skill Registry Sync Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under $WIKI_ROOT. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents. ai-agent-skill-registry-sync/SKILL.md local

### `ai-dianjing-growth-opportunity`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/ai-dianjing-growth-opportunity/SKILL.md`
- 功能检索描述：Analyze an Alibaba Wanxiangtai AI点睛 keyword-promotion plan from a one.alimama.com plan link. Use when the user wants a past-7-day AI点睛 plan diagnosis, demand/search-query/audience evaluation, advertising direction decisions, product-expansion ideas, a self-contained HTML report, and a structured JSON handoff containing read-only 1688 product and supplier search tasks for a downstream sourcing Skill.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ai-dianjing-growth-opportunity AI点睛增长机会诊断 Analyze an Alibaba Wanxiangtai AI点睛 keyword-promotion plan from a one.alimama.com plan link. Use when the user wants a past-7-day AI点睛 plan diagnosis, demand/search-query/audience evaluation, advertising direction decisions, product-expansion ideas, a self-contained HTML report, and a structured JSON handoff containing read-only 1688 product and supplier search tasks for a downstream sourcing Skill. ai-dianjing-growth-opportunity/SKILL.md local

### `ai-story-video-studio`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/ai-story-video-studio/SKILL.md`
- 功能检索描述：Create complete story-driven AI video plans from either product inputs or non-product story/theme ideas. Use when the user wants a short story, emotional short film, product marketing video ad, AI video story plan, story directions, creative script, visual style plan, storyboard, or model-ready prompt package. Supports product-image inputs that need audience/selling-point/scene analysis and pure story inputs such as holidays, family, friendship, love, conflict, or life observations.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：ai-story-video-studio AI Story Video Studio Create complete story-driven AI video plans from either product inputs or non-product story/theme ideas. Use when the user wants a short story, emotional short film, product marketing video ad, AI video story plan, story directions, creative script, visual style plan, storyboard, or model-ready prompt package. Supports product-image inputs that need audience/selling-point/scene analysis and pure story inputs such as holidays, family, friendship, love, conflict, or life observations. ai-story-video-studio/SKILL.md local

### `alibaba-review-report`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/alibaba-review-report/SKILL.md`
- 功能检索描述：Generate an Alibaba.com International store-review report from a product-detail URL by calling the stable alicli CLI to export the shop's reviews to Excel, then transforming that workbook into a self-contained, filterable HTML dashboard with review images and product filtering. Use when a user provides an Alibaba.com product link and asks to collect, export, inspect, visualize, or report store reviews in Excel and HTML.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：alibaba-review-report Alibaba Review Report Generate an Alibaba.com International store-review report from a product-detail URL by calling the stable alicli CLI to export the shop's reviews to Excel, then transforming that workbook into a self-contained, filterable HTML dashboard with review images and product filtering. Use when a user provides an Alibaba.com product link and asks to collect, export, inspect, visualize, or report store reviews in Excel and HTML. alibaba-review-report/SKILL.md local

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

### `character-reference-turnaround`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/character-reference-turnaround/SKILL.md`
- 功能检索描述：Create consistent character references and three-view turnaround sheets for AI visual/video production. Use when the user needs to define a person or role from a brief, product story, ad concept, existing reference images, age transformation, wardrobe direction, or wants outputs such as a character description, approved single reference image, front/side/back turnaround, or reusable character prompts.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：character-reference-turnaround Character Reference Turnaround Create consistent character references and three-view turnaround sheets for AI visual/video production. Use when the user needs to define a person or role from a brief, product story, ad concept, existing reference images, age transformation, wardrobe direction, or wants outputs such as a character description, approved single reference image, front/side/back turnaround, or reusable character prompts. character-reference-turnaround/SKILL.md local

### `compact-commerce-ui`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/compact-commerce-ui/SKILL.md`
- 功能检索描述：Orchestrate the system-wide commerce-ui CLI to create or redesign readable, modular HTML business reports, ecommerce dashboards, SaaS workbenches, analytics panels, and plugin interfaces. Use when an Agent needs HTML generation, report UI, compact commerce styling, independent sidebar views, responsive business components, self-contained image delivery, or deterministic HTML validation. This Skill owns business-to-ViewModel planning; the commerce-ui CLI is the only HTML renderer.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：compact-commerce-ui Compact Commerce UI CLI Orchestration Orchestrate the system-wide commerce-ui CLI to create or redesign readable, modular HTML business reports, ecommerce dashboards, SaaS workbenches, analytics panels, and plugin interfaces. Use when an Agent needs HTML generation, report UI, compact commerce styling, independent sidebar views, responsive business components, self-contained image delivery, or deterministic HTML validation. This Skill owns business-to-ViewModel planning; the commerce-ui CLI is the only HTML renderer. compact-commerce-ui/SKILL.md local

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

### `dmp-ai-competitor-research`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/dmp-ai-competitor-research/SKILL.md`
- 功能检索描述：自动执行 DMP/达摩盘 AI 竞品研究。输入用户自己的淘宝/天猫商品编号，复用或打开可调试 Chrome，检查达摩盘智能对话是否已打开，等待登录/导航，向达摩盘 AI 提问内部工具提示词，收集竞品销售、搜索、推广、人群、人群资产和店铺层数据，并生成运营可读 HTML 主报告、中文 Excel 证据包和标准 JSON。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：dmp-ai-competitor-research DMP AI Competitor Research 自动执行 DMP/达摩盘 AI 竞品研究。输入用户自己的淘宝/天猫商品编号，复用或打开可调试 Chrome，检查达摩盘智能对话是否已打开，等待登录/导航，向达摩盘 AI 提问内部工具提示词，收集竞品销售、搜索、推广、人群、人群资产和店铺层数据，并生成运营可读 HTML 主报告、中文 Excel 证据包和标准 JSON。 dmp-ai-competitor-research/SKILL.md local

### `dmp-ai-prompt-pack`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/dmp-ai-prompt-pack/SKILL.md`
- 功能检索描述：Generate a copy-ready HTML prompt manual for DMP/达摩盘 AI competitor research from one Taobao/Tmall item ID. Use when the user wants a reusable HTML file of DMP AI prompts, not live browser automation, covering competitor discovery, exact benchmark sales/promotion/free-traffic data, SQL over data_id, audience, VIEW flow, success path, keyword assets, shop competition, and download attempts. Markdown output remains available only when explicitly requested.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：dmp-ai-prompt-pack DMP AI Prompt Pack Generate a copy-ready HTML prompt manual for DMP/达摩盘 AI competitor research from one Taobao/Tmall item ID. Use when the user wants a reusable HTML file of DMP AI prompts, not live browser automation, covering competitor discovery, exact benchmark sales/promotion/free-traffic data, SQL over data_id, audience, VIEW flow, success path, keyword assets, shop competition, and download attempts. Markdown output remains available only when explicitly requested. dmp-ai-prompt-pack/SKILL.md local

### `dws`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/dws/SKILL.md`
- 功能检索描述：管理钉钉产品能力(AI表格/AI搜问/日历/通讯录/群聊与机器人/待办/审批/考勤/日志/DING消息/开放平台文档/钉钉文档/钉钉云盘/AI听记/邮箱/在线电子表格/知识库等)。当用户需要操作表格数据、管理日程会议、模糊找人/查谁负责某事项、查询通讯录、管理群聊、机器人发消息、创建待办、提交审批、查看考勤、提交日报周报（钉钉日志模版）、读写钉钉文档、上传下载云盘文件、查询听记纪要、收发邮件、读写在线电子表格(axls)、管理钉钉知识库时使用。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：dws 钉钉全产品 Skill 管理钉钉产品能力(AI表格/AI搜问/日历/通讯录/群聊与机器人/待办/审批/考勤/日志/DING消息/开放平台文档/钉钉文档/钉钉云盘/AI听记/邮箱/在线电子表格/知识库等)。当用户需要操作表格数据、管理日程会议、模糊找人/查谁负责某事项、查询通讯录、管理群聊、机器人发消息、创建待办、提交审批、查看考勤、提交日报周报（钉钉日志模版）、读写钉钉文档、上传下载云盘文件、查询听记纪要、收发邮件、读写在线电子表格(axls)、管理钉钉知识库时使用。 dws/SKILL.md local

### `dycli`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/dycli/SKILL.md`
- 功能检索描述：Use when the user wants an Agent to operate dycli, automate read-only Douyin Web data collection, search or download Douyin videos, export favorites or collections, download 巨量百应/精选联盟 product images, manage Chrome DevTools ports, install dycli skills into Agent systems, or continue developing dycli commands and workflows.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：dycli dycli Skill Use when the user wants an Agent to operate dycli, automate read-only Douyin Web data collection, search or download Douyin videos, export favorites or collections, download 巨量百应/精选联盟 product images, manage Chrome DevTools ports, install dycli skills into Agent systems, or continue developing dycli commands and workflows. dycli/SKILL.md local

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

### `ecommerce-shop-growth-diagnosis`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/ecommerce-shop-growth-diagnosis/SKILL.md`
- 功能检索描述：Diagnose one ecommerce target shop from a standard product-ranking or shop-product .xlsx workbook plus user-confirmed business context. Use when the user supplies a 店铺商品表、销量 TOP 市场数据分析表 or similar workbook and wants a tabbed HTML report that first shows the objective product situation with source images, then identifies evidence-bounded problems, applies five confirmed business genes to choose responses, and ends with a 30/60/90-day plan. Business genes come from the user; the Skill must not let the gene profile replace product analysis or invent traffic, paid-media, profit, lifecycle, association, or causal conclusions that the workbook cannot support.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ecommerce-shop-growth-diagnosis 店铺增长诊断 Diagnose one ecommerce target shop from a standard product-ranking or shop-product .xlsx workbook plus user-confirmed business context. Use when the user supplies a 店铺商品表、销量 TOP 市场数据分析表 or similar workbook and wants a tabbed HTML report that first shows the objective product situation with source images, then identifies evidence-bounded problems, applies five confirmed business genes to choose responses, and ends with a 30/60/90-day plan. Business genes come from the user; the Skill must not let the gene profile replace product analysis or invent traffic, paid-media, profit, lifecycle, association, or causal conclusions that the workbook cannot support. ecommerce-shop-growth-diagnosis/SKILL.md local

### `editable-poster-psd-rebuild`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/editable-poster-psd-rebuild/SKILL.md`
- 功能检索描述：Rebuild a flattened AI-generated ecommerce poster as a layered Photoshop PSD with a text-free background, hidden original reference, and editable native text layers using user-approved or commercially safe fonts. Use when the user asks to remove generated poster copy, preserve the reference layout, rebuild typography in PSD, hand off editable text to a designer, or reduce unknown-font licensing risk.
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：editable-poster-psd-rebuild Editable Poster PSD Rebuild Rebuild a flattened AI-generated ecommerce poster as a layered Photoshop PSD with a text-free background, hidden original reference, and editable native text layers using user-approved or commercially safe fonts. Use when the user asks to remove generated poster copy, preserve the reference layout, rebuild typography in PSD, hand off editable text to a designer, or reduce unknown-font licensing risk. editable-poster-psd-rebuild/SKILL.md local

### `goal-driven-video-qa`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/goal-driven-video-qa/SKILL.md`
- 功能检索描述：Inspect a video against quality goals inferred from the current conversation, explicit user request, prompt, script, storyboard, reference media, prior test results, and delivery requirements. Use for 视频质检, AI-generated video review, casting or age checks, character/product/scene consistency, action and spatial continuity, subtitles or unwanted text, dialogue/audio/accent review, pacing, technical specifications, prompt adherence, or A/B generation loops. Dynamically choose inspection modalities and sampling depth, produce timestamped evidence and coverage limits, and remain read-only unless the user separately authorizes changes or regeneration.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：goal-driven-video-qa Goal-Driven Video QA Inspect a video against quality goals inferred from the current conversation, explicit user request, prompt, script, storyboard, reference media, prior test results, and delivery requirements. Use for 视频质检, AI-generated video review, casting or age checks, character/product/scene consistency, action and spatial continuity, subtitles or unwanted text, dialogue/audio/accent review, pacing, technical specifications, prompt adherence, or A/B generation loops. Dynamically choose inspection modalities and sampling depth, produce timestamped evidence and coverage limits, and remain read-only unless the user separately authorizes changes or regeneration. goal-driven-video-qa/SKILL.md local

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

### `无限画板 Skill 生成器`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/infinite-canvas-skill-generator/SKILL.md`
- 功能检索描述：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优化这个无限画板 skill、根据反馈修改 skill.md。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：无限画板 Skill 生成器 无限画板 · Skill 生成器 根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优化这个无限画板 skill、根据反馈修改 skill.md。 infinite-canvas-skill-generator/SKILL.md local

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

### `international-station-seller-assistant`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/international-station-seller-assistant/SKILL.md`
- 功能检索描述：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl CLI, including 店铺经营数据, 询盘, TM/IM conversations, 客服诊断, 广告, 商品, 发品, 选品, RFQ, 物流, 交易, 旺铺, or 国际站生意助手 workflows.
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：international-station-seller-assistant International Station Seller Assistant Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl CLI, including 店铺经营数据, 询盘, TM/IM conversations, 客服诊断, 广告, 商品, 发品, 选品, RFQ, 物流, 交易, 旺铺, or 国际站生意助手 workflows. international-station-seller-assistant/SKILL.md local

### `joinquant-strategy`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/joinquant-strategy/SKILL.md`
- 功能检索描述：Write, review, debug, and validate JoinQuant/JQData 聚宽 quantitative trading strategy scripts that will be copied into the JoinQuant backtest or simulation platform. Use when the user asks for 聚宽策略, JoinQuant 回测代码, jqdata API usage, A股量化策略脚本, strategy compatibility checks before copying to 聚宽, or fixes for 聚宽 platform runtime errors.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：joinquant-strategy JoinQuant Strategy Write, review, debug, and validate JoinQuant/JQData 聚宽 quantitative trading strategy scripts that will be copied into the JoinQuant backtest or simulation platform. Use when the user asks for 聚宽策略, JoinQuant 回测代码, jqdata API usage, A股量化策略脚本, strategy compatibility checks before copying to 聚宽, or fixes for 聚宽 platform runtime errors. joinquant-strategy/SKILL.md local

### `jqcli`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/jqcli/SKILL.md`
- 功能检索描述：Use when Codex needs to operate or maintain the jqcli JoinQuant project: authenticate, inspect strategies, list or run backtests, archive community posts, validate jqcli API behavior, run local tests, perform live JoinQuant smoke checks, or troubleshoot jqcli CLI/API workflows.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：jqcli jqcli Use when Codex needs to operate or maintain the jqcli JoinQuant project: authenticate, inspect strategies, list or run backtests, archive community posts, validate jqcli API behavior, run local tests, perform live JoinQuant smoke checks, or troubleshoot jqcli CLI/API workflows. jqcli/SKILL.md local

### `lark-structured-doc-writer`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/lark-structured-doc-writer/SKILL.md`
- 功能检索描述：Create or substantially rewrite clear, complete, highly readable Lark/Feishu project and knowledge documents. Use when an agent must organize repositories, products, research, methods, tutorials, comparisons, or fragmented source material into a rich Lark document without losing important facts, evidence, caveats, examples, or implementation detail. This skill governs content architecture, fidelity, visual language, QA, and iteration; use the current lark-doc capability as the execution adapter for live document operations.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-structured-doc-writer Lark Structured Document Writer Create or substantially rewrite clear, complete, highly readable Lark/Feishu project and knowledge documents. Use when an agent must organize repositories, products, research, methods, tutorials, comparisons, or fragmented source material into a rich Lark document without losing important facts, evidence, caveats, examples, or implementation detail. This skill governs content architecture, fidelity, visual language, QA, and iteration; use the current lark-doc capability as the execution adapter for live document operations. lark-structured-doc-writer/SKILL.md local

### `libtv-cli`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/libtv-cli/SKILL.md`
- 功能检索描述：>- LibTV 官方 CLI（libtv）：在命令行里完整操作 / 运行 LibTV 画布。 凡是和 LibTV 画布 / 项目 / 节点 / 模型 / 素材相关的操作，一律通过 libtv CLI 完成， 包括在提供 `libtv video` 扩展时查看或下载公开作品详情页中的成片。 当用户要逆向学习社区画板、导出节点快照或整理视频与参考图生产链时，也使用本 Skill。 不要自己捏造 HTTP 请求或绕到网页端步骤。本 skill 内即包含完整的 CLI 命令操作手册； 常见场景见 examples/，安装/更新见 scripts/install.md。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：libtv-cli LibTV CLI（ libtv ） >- LibTV 官方 CLI（libtv）：在命令行里完整操作 / 运行 LibTV 画布。 凡是和 LibTV 画布 / 项目 / 节点 / 模型 / 素材相关的操作，一律通过 libtv CLI 完成， 包括在提供 libtv video 扩展时查看或下载公开作品详情页中的成片。 当用户要逆向学习社区画板、导出节点快照或整理视频与参考图生产链时，也使用本 Skill。 不要自己捏造 HTTP 请求或绕到网页端步骤。本 skill 内即包含完整的 CLI 命令操作手册； 常见场景见 examples/，安装/更新见 scripts/install.md。 libtv-cli/SKILL.md local

### `llm-wiki`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/llm-wiki/SKILL.md`
- 功能检索描述：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from their Wiki, wants to find existing knowledge, compare compiled pages, trace which Wiki pages or embedded image evidence support an answer, display a relevant stored screenshot or diagram, or make small explicit updates to indexes and query entry pages. Delegate new-source ingestion and all quality audit, optimization, repair, and recompilation work to the corresponding LLM Wiki skills.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：llm-wiki LLM Wiki Query And Routine Maintenance Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from their Wiki, wants to find existing knowledge, compare compiled pages, trace which Wiki pages or embedded image evidence support an answer, display a relevant stored screenshot or diagram, or make small explicit updates to indexes and query entry pages. Delegate new-source ingestion and all quality audit, optimization, repair, and recompilation work to the corresponding LLM Wiki skills. llm-wiki/SKILL.md local

### `llm-wiki-audit-and-optimization`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/llm-wiki-audit-and-optimization/SKILL.md`
- 功能检索描述：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-readiness. Use when the user asks to check Wiki quality, verify a recent ingest, find why knowledge or embedded images cannot be found or delivered, diagnose a question-and-answer result, optimize or repair the Wiki, rebuild weak pages, fix routes or taxonomy, or recompile existing source material. By default, continue from audit findings into evidence-backed optimization and re-audit; remain read-only only when the user explicitly says not to modify files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit And Optimization Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-readiness. Use when the user asks to check Wiki quality, verify a recent ingest, find why knowledge or embedded images cannot be found or delivered, diagnose a question-and-answer result, optimize or repair the Wiki, rebuild weak pages, fix routes or taxonomy, or recompile existing source material. By default, continue from audit findings into evidence-backed optimization and re-audit; remain read-only only when the user explicitly says not to modify files. llm-wiki-audit-and-optimization/SKILL.md local

### `llm-wiki-bootstrap`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/llm-wiki-bootstrap/SKILL.md`
- 功能检索描述：Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set up an LLM Wiki from scratch, configure WIKI_ROOT, prepare Obsidian App and its bundled CLI, install the media/OCR tools needed by wiki ingestion, create the initial domains/index/schema/log structure, or verify readiness on macOS, Windows, or Linux.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；MCP server、工具配置、连接或封装需求
- 检索关键词：llm-wiki-bootstrap LLM Wiki Bootstrap Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set up an LLM Wiki from scratch, configure WIKI_ROOT, prepare Obsidian App and its bundled CLI, install the media/OCR tools needed by wiki ingestion, create the initial domains/index/schema/log structure, or verify readiness on macOS, Windows, or Linux. llm-wiki-bootstrap/SKILL.md local

### `llm-wiki-ingest`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/llm-wiki-ingest/SKILL.md`
- 功能检索描述：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or dynamic webpages, Obsidian Clippings, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces memory-first classification, text and image evidence preservation, semantic image anchoring, lossless knowledge-unit coverage, formal pages, index/log updates, route audit, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or dynamic webpages, Obsidian Clippings, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces memory-first classification, text and image evidence preservation, semantic image anchoring, lossless knowledge-unit coverage, formal pages, index/log updates, route audit, and audit handoff. llm-wiki-ingest/SKILL.md local

### `mac-no-reboot-rescue`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/mac-no-reboot-rescue/SKILL.md`
- 功能检索描述：Diagnose and relieve recurring macOS slowdowns without rebooting. Use when the user says their Mac is slow, stuck, beachballing, high load, memory pressure is high, WindowServer/syspolicyd/opendirectoryd/trustd are hot, or they explicitly want a no-reboot rescue workflow for preserving an active work environment.
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求
- 检索关键词：mac-no-reboot-rescue Mac No-Reboot Rescue Diagnose and relieve recurring macOS slowdowns without rebooting. Use when the user says their Mac is slow, stuck, beachballing, high load, memory pressure is high, WindowServer/syspolicyd/opendirectoryd/trustd are hot, or they explicitly want a no-reboot rescue workflow for preserving an active work environment. mac-no-reboot-rescue/SKILL.md local

### `market-ranking-growth-report`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/market-ranking-growth-report/SKILL.md`
- 功能检索描述：Generate a Word growth strategy report from 12 months of marketplace ranking spreadsheets for any ecommerce shop and category. Use when the user provides monthly market ranking Excel files, a folder, or a compressed archive such as .rar/.zip and asks for market analysis, 生意参谋排行分析, 市场排行包分析, 竞店排行分析, 店铺增长诊断, category strategy, shop growth planning, expansion planning, Taobao/Tmall/store growth diagnosis, or a Word report based on market ranking data.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：market-ranking-growth-report Market Ranking Growth Report Generate a Word growth strategy report from 12 months of marketplace ranking spreadsheets for any ecommerce shop and category. Use when the user provides monthly market ranking Excel files, a folder, or a compressed archive such as .rar/.zip and asks for market analysis, 生意参谋排行分析, 市场排行包分析, 竞店排行分析, 店铺增长诊断, category strategy, shop growth planning, expansion planning, Taobao/Tmall/store growth diagnosis, or a Word report based on market ranking data. market-ranking-growth-report/SKILL.md local

### `portable-skill-creator`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/portable-skill-creator/SKILL.md`
- 功能检索描述：Create, update, review, or test shareable Agent Skills without leaking author-machine information or binding the core workflow to one Agent. Use by default for any Skill authoring task that should compose the current base skill-creator workflow, enforce privacy and machine independence, separate portable core instructions from optional Codex, SealSeek, Hermes, OpenClaw, or other platform adapters, run portability validation, and report tested compatibility honestly. Do not use only when the user explicitly requests the bundled/system skill-creator alone.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：portable-skill-creator Portable Skill Creator Create, update, review, or test shareable Agent Skills without leaking author-machine information or binding the core workflow to one Agent. Use by default for any Skill authoring task that should compose the current base skill-creator workflow, enforce privacy and machine independence, separate portable core instructions from optional Codex, SealSeek, Hermes, OpenClaw, or other platform adapters, run portability validation, and report tested compatibility honestly. Do not use only when the user explicitly requests the bundled/system skill-creator alone. portable-skill-creator/SKILL.md local

### `product-story-ad-video`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/product-story-ad-video/SKILL.md`
- 功能检索描述：Create and run a project-style workflow for story-driven ecommerce product video ads. Use when the user wants to promote a product with a narrative video, build AI video control assets, plan storyboard/Seedance prompts, maintain project state, or launch the real-time dashboard for an existing product video project.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：product-story-ad-video Product Story Ad Video Create and run a project-style workflow for story-driven ecommerce product video ads. Use when the user wants to promote a product with a narrative video, build AI video control assets, plan storyboard/Seedance prompts, maintain project state, or launch the real-time dashboard for an existing product video project. product-story-ad-video/SKILL.md local

### `quant-local-research`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/quant-local-research/SKILL.md`
- 功能检索描述：Use when Peter asks to research, backtest, validate, optimize, compare, or port ETF/stock quantitative trading strategies using the local QuantTrading framework, local Parquet market data, or JoinQuant/聚宽 calibration workflow. Trigger for requests about ETF策略、本地回测、量化验证系统、策略优化、夏普、回撤、选池、聚宽迁移、JoinQuant simulation, or QuantTrading data under /Users/pechen/QuantTrading.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：quant-local-research Quant Local Research Use when Peter asks to research, backtest, validate, optimize, compare, or port ETF/stock quantitative trading strategies using the local QuantTrading framework, local Parquet market data, or JoinQuant/聚宽 calibration workflow. Trigger for requests about ETF策略、本地回测、量化验证系统、策略优化、夏普、回撤、选池、聚宽迁移、JoinQuant simulation, or QuantTrading data under /Users/pechen/QuantTrading. quant-local-research/SKILL.md local

### `script-writing-studio`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/script-writing-studio/SKILL.md`
- 功能检索描述：端到端中文剧本创作工作室。用于剧本、竖屏短剧、动画脚本、动态漫画脚本、完整剧本扩写、台词稿、项目资产库、AI 视频分镜、Seedance 2.0 视频提示词、后期 BGM/配乐/声音设计的完整开发流程。用户想从灵感写故事、生成大纲或项目档案、把项目档案和大纲扩写成完整剧本、会诊已有剧本、精修台词、建立角色/场景/道具资产库、整理参考图、生成 AI 视频分镜，输出 Sora/Kling/Veo/Runway/Pixverse/Seedance 2.0/豆包视频/火山方舟视频生成提示词，或在视频生成/粗剪后设计 BGM、音乐搜索词、AI 音乐生成提示词、音效、静默点和后期声音方案时使用。
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：script-writing-studio 剧本创作工作室 端到端中文剧本创作工作室。用于剧本、竖屏短剧、动画脚本、动态漫画脚本、完整剧本扩写、台词稿、项目资产库、AI 视频分镜、Seedance 2.0 视频提示词、后期 BGM/配乐/声音设计的完整开发流程。用户想从灵感写故事、生成大纲或项目档案、把项目档案和大纲扩写成完整剧本、会诊已有剧本、精修台词、建立角色/场景/道具资产库、整理参考图、生成 AI 视频分镜，输出 Sora/Kling/Veo/Runway/Pixverse/Seedance 2.0/豆包视频/火山方舟视频生成提示词，或在视频生成/粗剪后设计 BGM、音乐搜索词、AI 音乐生成提示词、音效、静默点和后期声音方案时使用。 script-writing-studio/SKILL.md local

### `sealseek-canvas`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/sealseek-canvas/SKILL.md`
- 功能检索描述：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or manage an 无限画板, generate/retrieve/place/arrange `gpt-image-2` images, generate/retrieve/place `seedance2-0` videos, add explanatory text, inspect supported parameters, download assets, or lay out labeled media tightly in blank board space. Prefer this CLI over browser clicking, Agent-mode generation, or ad hoc HTTP calls.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：sealseek-canvas SealSeek Infinite Canvas CLI Operate SealSeek Infinite Canvas through the browserless-capable sealseek-canvas CLI. Use when the user asks to authenticate, create or manage an 无限画板, generate/retrieve/place/arrange gpt-image-2 images, generate/retrieve/place seedance2-0 videos, add explanatory text, inspect supported parameters, download assets, or lay out labeled media tightly in blank board space. Prefer this CLI over browser clicking, Agent-mode generation, or ad hoc HTTP calls. sealseek-canvas/SKILL.md local

### `sealseek-chat-control`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/sealseek-chat-control/SKILL.md`
- 功能检索描述：Control and inspect the user's running SealSeek/SealClaw conversations through the local `sealseek-chat` CLI. Use when Codex needs to create, attach to, send commands to, wait for, inspect, trace, audit, export, or read back SealSeek conversations; when using SealSeek as a sub-agent; or when the user asks Codex to automate or diagnose SealSeek/OpenClaw dialogue from another agent environment.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-chat-control SealSeek Chat Control Control and inspect the user's running SealSeek/SealClaw conversations through the local sealseek-chat CLI. Use when Codex needs to create, attach to, send commands to, wait for, inspect, trace, audit, export, or read back SealSeek conversations; when using SealSeek as a sub-agent; or when the user asks Codex to automate or diagnose SealSeek/OpenClaw dialogue from another agent environment. sealseek-chat-control/SKILL.md local

### `sealseek-course-doc-writer`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.codex/skills/sealseek-course-doc-writer/SKILL.md`
- 功能检索描述：Write and maintain SealSeek/玺虾 learner-facing course documents, Feishu handbooks, chapter sub-documents, and copyable prompt-based class materials. Use when the user asks to continue, refine, split, format, or write SealSeek course content, especially learner handouts, chapter documents, Feishu docs, prompt examples, or the Wiki-Skill-SOP training materials.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-course-doc-writer SealSeek Course Doc Writer Write and maintain SealSeek/玺虾 learner-facing course documents, Feishu handbooks, chapter sub-documents, and copyable prompt-based class materials. Use when the user asks to continue, refine, split, format, or write SealSeek course content, especially learner handouts, chapter documents, Feishu docs, prompt examples, or the Wiki-Skill-SOP training materials. sealseek-course-doc-writer/SKILL.md local

### `sealseek-execution-auditor`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/sealseek-execution-auditor/SKILL.md`
- 功能检索描述：Audit SealSeek conversation execution traces to reconstruct tool calls, retries, fallbacks, side effects, skipped validation, and false-success risks. Use when the user asks how SealSeek actually completed a task, wants to inspect a conversation's scheduling or intermediate process, suspects detours or silent degradation, needs a process-compliance report, or wants regression evidence before and after a SealSeek product, tool, prompt, or Skill fix.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-execution-auditor SealSeek Execution Auditor Audit SealSeek conversation execution traces to reconstruct tool calls, retries, fallbacks, side effects, skipped validation, and false-success risks. Use when the user asks how SealSeek actually completed a task, wants to inspect a conversation's scheduling or intermediate process, suspects detours or silent degradation, needs a process-compliance report, or wants regression evidence before and after a SealSeek product, tool, prompt, or Skill fix. sealseek-execution-auditor/SKILL.md local

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

### `seedance-video`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/seedance-video/SKILL.md`
- 功能检索描述：Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedance 2.0 through the system-level `seedancecli` CLI and Volcengine Ark. Trigger for text-to-video, image/video/audio reference-to-video, first-frame or first-last-frame video, video editing, video extension, Ark video task polling, and Seedance payload dry-runs.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：seedance-video Seedance Video Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedance 2.0 through the system-level seedancecli CLI and Volcengine Ark. Trigger for text-to-video, image/video/audio reference-to-video, first-frame or first-last-frame video, video editing, video extension, Ark video task polling, and Seedance payload dry-runs. seedance-video/SKILL.md local

### `seedaudiocli`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/seedaudiocli/SKILL.md`
- 功能检索描述：Use the local `seedaudiocli` system CLI to generate audio with EvoLink Doubao Seed-Audio 1.0. Use when an Agent needs background music, product-video BGM, speech, voice/preset audio, reference-audio voice cloning, reference-image-guided audio, task polling, or downloading generated Seed Audio files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：seedaudiocli Seed Audio CLI Use the local seedaudiocli system CLI to generate audio with EvoLink Doubao Seed-Audio 1.0. Use when an Agent needs background music, product-video BGM, speech, voice/preset audio, reference-audio voice cloning, reference-image-guided audio, task polling, or downloading generated Seed Audio files. seedaudiocli/SKILL.md local

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

### `无限画板 Skill 生成器`

- Agent / 环境：Codex
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/skill-builder.backup-20260630-093000/SKILL.md`
- 功能检索描述：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优化这个无限画板 skill、根据反馈修改 skill.md。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：无限画板 Skill 生成器 无限画板 · Skill 生成器 根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优化这个无限画板 skill、根据反馈修改 skill.md。 skill-builder.backup-20260630-093000/SKILL.md archived-or-backup

### `skill-forward-test`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/skill-forward-test/SKILL.md`
- 功能检索描述：Validate newly created or updated Codex skills with a clean sub-agent regression loop. Use when the user asks to test, verify, forward-test, regression-test, or confirm that a skill change really landed on disk and works outside the design conversation; especially for skill creation and optimization workflows.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：skill-forward-test Skill Forward Test Validate newly created or updated Codex skills with a clean sub-agent regression loop. Use when the user asks to test, verify, forward-test, regression-test, or confirm that a skill change really landed on disk and works outside the design conversation; especially for skill creation and optimization workflows. skill-forward-test/SKILL.md local

### `story-driven-product-ad`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/story-driven-product-ad/SKILL.md`
- 功能检索描述：Use when creating emotionally driven short-video story ads, Douyin/TikTok product-placement stories, product-in-story scripts, or story-first ecommerce promotion concepts. The skill outputs a Markdown file with three distinct story versions, each suitable for a sub-2-minute short video and a naturally embedded product.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：story-driven-product-ad Story Driven Product Ad Use when creating emotionally driven short-video story ads, Douyin/TikTok product-placement stories, product-in-story scripts, or story-first ecommerce promotion concepts. The skill outputs a Markdown file with three distinct story versions, each suitable for a sub-2-minute short video and a naturally embedded product. story-driven-product-ad/SKILL.md local

### `ths-rebalance-planner`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/ths-rebalance-planner/SKILL.md`
- 功能检索描述：Generate a rebalance plan for the currently selected Tonghuashun 同花顺 account from pasted JoinQuant/模拟策略 target holdings. Use when the user provides simulated strategy positions and asks how the current manually selected brokerage account should adjust, including buy/sell quantities, post-adjustment stock weights, and estimated cash. The skill reads current holdings with a bundled macOS Accessibility reader and uses a bundled deterministic calculator.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ths-rebalance-planner 同花顺调仓规划 Generate a rebalance plan for the currently selected Tonghuashun 同花顺 account from pasted JoinQuant/模拟策略 target holdings. Use when the user provides simulated strategy positions and asks how the current manually selected brokerage account should adjust, including buy/sell quantities, post-adjustment stock weights, and estimated cash. The skill reads current holdings with a bundled macOS Accessibility reader and uses a bundled deterministic calculator. ths-rebalance-planner/SKILL.md local

### `wdt-dingtalk-logistics-dashboard`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/wdt-dingtalk-logistics-dashboard/SKILL.md`
- 功能检索描述：Maintain a DingTalk AI table logistics anomaly dashboard for ecommerce orders. Use when the user asks to initialize or update the logistics dashboard, sync WDT/旺店通 suspected abnormal orders to DingTalk, review Taobao/Tmall logistics through tbcli, exclude false positives, or create run logs for ongoing logistics monitoring.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：wdt-dingtalk-logistics-dashboard WDT DingTalk Logistics Dashboard Maintain a DingTalk AI table logistics anomaly dashboard for ecommerce orders. Use when the user asks to initialize or update the logistics dashboard, sync WDT/旺店通 suspected abnormal orders to DingTalk, review Taobao/Tmall logistics through tbcli, exclude false positives, or create run logs for ongoing logistics monitoring. wdt-dingtalk-logistics-dashboard/SKILL.md local

### `wdt-inventory-replenishment`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/wdt-inventory-replenishment/SKILL.md`
- 功能检索描述：Run Wangdian ERP inventory replenishment monitoring with wdtcli, derive SKU warning thresholds from historical sales, generate a purchase report, and send it to a DingTalk purchasing group through a bot. Use for daily inventory alerts, stockout-risk reports, replenishment quantities, purchasing notifications, or testing the WDT inventory-to-DingTalk workflow.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：wdt-inventory-replenishment 旺店通库存采购预警 Run Wangdian ERP inventory replenishment monitoring with wdtcli, derive SKU warning thresholds from historical sales, generate a purchase report, and send it to a DingTalk purchasing group through a bot. Use for daily inventory alerts, stockout-risk reports, replenishment quantities, purchasing notifications, or testing the WDT inventory-to-DingTalk workflow. wdt-inventory-replenishment/SKILL.md local

### `wdt-logistics-anomaly-report`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.codex/skills/wdt-logistics-anomaly-report/SKILL.md`
- 功能检索描述：End-to-end 旺店通/WDT order logistics anomaly analysis. Use when the user asks to analyze ecommerce order logistics, find abnormal shipments, classify delayed pickup/in-transit/problem orders, or create a logistics Excel report. The skill should call the local `wdtcli` CLI itself to export ERP logistics anomaly data, then generate a polished Excel workbook with 判定规则, 异常订单分类, 汇总透视, and readable formatting.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：wdt-logistics-anomaly-report WDT Logistics Anomaly Report End-to-end 旺店通/WDT order logistics anomaly analysis. Use when the user asks to analyze ecommerce order logistics, find abnormal shipments, classify delayed pickup/in-transit/problem orders, or create a logistics Excel report. The skill should call the local wdtcli CLI itself to export ERP logistics anomaly data, then generate a polished Excel workbook with 判定规则, 异常订单分类, 汇总透视, and readable formatting. wdt-logistics-anomaly-report/SKILL.md local

### `workctl`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.codex/skills/workctl/SKILL.md`
- 功能检索描述：管理 Work Agent 平台能力。通过 `workctl schema` 发现动态产品和命令，再用结构化输出执行操作。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：workctl Work Agent CLI Skill 管理 Work Agent 平台能力。通过 workctl schema 发现动态产品和命令，再用结构化输出执行操作。 workctl/SKILL.md local

### `workctl-operator`

- Agent / 环境：Codex
- 归属分类：个人/项目自定义
- 归属依据：Codex 非 `.system` 本地 skill，按个人/项目自定义处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.codex/skills/workctl/workctl-operator/SKILL.md`
- 功能检索描述：安装、升级、认证、发现并使用 Work Agent CLI (`workctl`)。适用于通过 `workctl schema` 发现并调用阿里巴巴国际站商家经营工具，处理店铺经营数据、广告、发品、商品优化、AI 图片/视频、旺铺、选品、物流、交易、IM、知识问答、深度研究等场景。 也适用于配置 workctl、登录认证、排查 token/cache/schema/runtime/async task/recovery 问题，编排多个 workctl 工具，或为新业务域接入 registry/discovery/detail/tools/call 协议。执行业务命令时必须以当前 `workctl schema` 和 `workctl <command> --help` 为准，不照搬旧 MCP/CLI 命令。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：workctl-operator Workctl Operator 安装、升级、认证、发现并使用 Work Agent CLI ( workctl )。适用于通过 workctl schema 发现并调用阿里巴巴国际站商家经营工具，处理店铺经营数据、广告、发品、商品优化、AI 图片/视频、旺铺、选品、物流、交易、IM、知识问答、深度研究等场景。 也适用于配置 workctl、登录认证、排查 token/cache/schema/runtime/async task/recovery 问题，编排多个 workctl 工具，或为新业务域接入 registry/discovery/detail/tools/call 协议。执行业务命令时必须以当前 workctl schema 和 workctl <command> --help 为准，不照搬旧 MCP/CLI 命令。 workctl/workctl-operator/SKILL.md local

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

