---
title: 个人/项目 Skill 注册库
type: concept
created: 2026-08-10
updated: 2026-08-10
domain: AI Agent工程
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

本页只收录 wiki owner 自己创建、让 Agent 为项目定制、或明显服务于 wiki owner 项目/业务流程的 skill。它是日常检索“以前有没有做过类似 skill”的优先入口。

不收录 Codex/Claude/Lark/SealSeek 等 Agent 的系统内置 skill、底层工具 skill、运行时副本和备份条目；这些仍保留在 [[domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库|跨 Agent Skill 注册库]]。

当前个人/项目 skill 数量：282。

## 分类规则

- Codex 非 `.system` 本地 skill：视为个人/项目自定义。
- OpenClaw workspace skill：视为项目自定义。
- SealSeek workspace/default/customized/standalone/migration skill：视为个人/项目自定义；`skill_pool` 和 `active_skills` 不进入本页。
- Hermes skill：命中用户项目、电商、视觉、课程、LLM Wiki、Sealseek/OpenClaw/玺承等关键词时进入本页；否则归入通用安装/不确定。
- Claude Code 官方 marketplace、Codex `.system`、Lark 通用工具 skill：作为系统/底层能力，只在全量库中保留。

## Agent 快速索引

### Codex

- `1688-opportunity-sourcing-research` (local)：Research products and suppliers on 1688 with category-first sourcing across market-proven, novel, aesthetic, scenario, premium, and bundle s… 位置：`/Users/pechen/.codex/skills/1688-opportunity-sourcing-research/SKILL.md`
- `ai-agent-skill-registry-sync` (local)：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM … 位置：`/Users/pechen/.codex/skills/ai-agent-skill-registry-sync/SKILL.md`
- `ai-dianjing-growth-opportunity` (local)：Analyze an Alibaba Wanxiangtai AI点睛 keyword-promotion plan from a one.alimama.com plan link. Use when the user wants a past-7-day AI点睛 plan … 位置：`/Users/pechen/.codex/skills/ai-dianjing-growth-opportunity/SKILL.md`
- `ai-story-video-studio` (local)：Create complete story-driven AI video plans from either product inputs or non-product story/theme ideas. Use when the user wants a short sto… 位置：`/Users/pechen/.codex/skills/ai-story-video-studio/SKILL.md`
- `alibaba-review-report` (local)：Generate an Alibaba.com International store-review report from a product-detail URL by calling the stable alicli CLI to export the shop's re… 位置：`/Users/pechen/.codex/skills/alibaba-review-report/SKILL.md`
- `brand-planning-report` (local)：Generate a user-facing ecommerce brand planning HTML report from a standard 店铺商品 Excel workbook, using Peter's brand-strategy LLM Wiki for p… 位置：`/Users/pechen/.codex/skills/brand-planning-report/SKILL.md`
- `character-reference-turnaround` (local)：Create consistent character references and three-view turnaround sheets for AI visual/video production. Use when the user needs to define a … 位置：`/Users/pechen/.codex/skills/character-reference-turnaround/SKILL.md`
- `compact-commerce-ui` (local)：Orchestrate the system-wide commerce-ui CLI to create or redesign readable, modular HTML business reports, ecommerce dashboards, SaaS workbe… 位置：`/Users/pechen/.codex/skills/compact-commerce-ui/SKILL.md`
- `course-deck-factory` (local)：Build editable course slide decks from a standardized deck spec using Node.js, PptxGenJS, local fonts, structured page types, and a mixed vi… 位置：`/Users/pechen/.codex/skills/course-deck-factory/SKILL.md`
- `dmp-ai-competitor-research` (local)：自动执行 DMP/达摩盘 AI 竞品研究。输入用户自己的淘宝/天猫商品编号，复用或打开可调试 Chrome，检查达摩盘智能对话是否已打开，等待登录/导航，向达摩盘 AI 提问内部工具提示词，收集竞品销售、搜索、推广、人群、人群资产和店铺层数据，并生成运营可读 HTML 主报告、中… 位置：`/Users/pechen/.codex/skills/dmp-ai-competitor-research/SKILL.md`
- `dmp-ai-prompt-pack` (local)：Generate a copy-ready HTML prompt manual for DMP/达摩盘 AI competitor research from one Taobao/Tmall item ID. Use when the user wants a reusabl… 位置：`/Users/pechen/.codex/skills/dmp-ai-prompt-pack/SKILL.md`
- `dws` (local)：管理钉钉产品能力(AI表格/AI搜问/日历/通讯录/群聊与机器人/待办/审批/考勤/日志/DING消息/开放平台文档/钉钉文档/钉钉云盘/AI听记/邮箱/在线电子表格/知识库等)。当用户需要操作表格数据、管理日程会议、模糊找人/查谁负责某事项、查询通讯录、管理群聊、机器人发消息、… 位置：`/Users/pechen/.codex/skills/dws/SKILL.md`
- `dycli` (local)：Use when the user wants an Agent to operate dycli, automate read-only Douyin Web data collection, search or download Douyin videos, export f… 位置：`/Users/pechen/.codex/skills/dycli/SKILL.md`
- `ecommerce-profit-statement-automation` (local)：Automate ecommerce platform profit statement workbooks from settlement/funds/account bills. Use when the user wants to turn Taobao or other … 位置：`/Users/pechen/.codex/skills/ecommerce-profit-statement-automation/SKILL.md`
- `ecommerce-shop-growth-diagnosis` (local)：Diagnose one ecommerce target shop from a standard product-ranking or shop-product .xlsx workbook plus user-confirmed business context. Use … 位置：`/Users/pechen/.codex/skills/ecommerce-shop-growth-diagnosis/SKILL.md`
- `editable-poster-psd-rebuild` (local)：Rebuild a flattened AI-generated ecommerce poster as a layered Photoshop PSD with a text-free background, hidden original reference, and edi… 位置：`/Users/pechen/.codex/skills/editable-poster-psd-rebuild/SKILL.md`
- `goal-driven-video-qa` (local)：Inspect a video against quality goals inferred from the current conversation, explicit user request, prompt, script, storyboard, reference m… 位置：`/Users/pechen/.codex/skills/goal-driven-video-qa/SKILL.md`
- `image-detail-page` (local)：根据产品白底图和品类，全自动推断模型、人群、风格，并一站式生成13个策划文件及对应电商图片。 当用户提到主图详情页、电商策划、白底图出方案、主图设计、详情页设计、电商视觉方案时触发。 位置：`/Users/pechen/.codex/skills/image-detail-page/SKILL.md`
- `无限画板 Skill 生成器` (local)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 … 位置：`/Users/pechen/.codex/skills/infinite-canvas-skill-generator/SKILL.md`
- `internal-plugin-workflow` (local)：Use when the user wants to build or iterate an internal Chrome browser extension against a page they have already opened, especially when th… 位置：`/Users/pechen/.codex/skills/internal-plugin-workflow/SKILL.md`
- `international-station-seller-assistant` (local)：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl… 位置：`/Users/pechen/.codex/skills/international-station-seller-assistant/SKILL.md`
- `joinquant-strategy` (local)：Write, review, debug, and validate JoinQuant/JQData 聚宽 quantitative trading strategy scripts that will be copied into the JoinQuant backtest… 位置：`/Users/pechen/.codex/skills/joinquant-strategy/SKILL.md`
- `jqcli` (local)：Use when Codex needs to operate or maintain the jqcli JoinQuant project: authenticate, inspect strategies, list or run backtests, archive co… 位置：`/Users/pechen/.codex/skills/jqcli/SKILL.md`
- `lark-structured-doc-writer` (local)：Create or substantially rewrite clear, complete, highly readable Lark/Feishu project and knowledge documents. Use when an agent must organiz… 位置：`/Users/pechen/.codex/skills/lark-structured-doc-writer/SKILL.md`
- `libtv-cli` (local)：>- LibTV 官方 CLI（libtv）：在命令行里完整操作 / 运行 LibTV 画布。 凡是和 LibTV 画布 / 项目 / 节点 / 模型 / 素材相关的操作，一律通过 libtv CLI 完成， 包括在提供 `libtv video` 扩展时查看或下载公开作品详情页… 位置：`/Users/pechen/.codex/skills/libtv-cli/SKILL.md`
- `llm-wiki` (local)：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered… 位置：`/Users/pechen/.codex/skills/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (local)：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, a… 位置：`/Users/pechen/.codex/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `llm-wiki-bootstrap` (local)：Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set up an LLM Wiki from … 位置：`/Users/pechen/.codex/skills/llm-wiki-bootstrap/SKILL.md`
- `llm-wiki-ingest` (local)：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including ima… 位置：`/Users/pechen/.codex/skills/llm-wiki-ingest/SKILL.md`
- `mac-no-reboot-rescue` (local)：Diagnose and relieve recurring macOS slowdowns without rebooting. Use when the user says their Mac is slow, stuck, beachballing, high load, … 位置：`/Users/pechen/.codex/skills/mac-no-reboot-rescue/SKILL.md`
- `market-ranking-growth-report` (local)：Generate a Word growth strategy report from 12 months of marketplace ranking spreadsheets for any ecommerce shop and category. Use when the … 位置：`/Users/pechen/.codex/skills/market-ranking-growth-report/SKILL.md`
- `portable-skill-creator` (local)：Create, update, review, or test shareable Agent Skills without leaking author-machine information or binding the core workflow to one Agent.… 位置：`/Users/pechen/.codex/skills/portable-skill-creator/SKILL.md`
- `product-story-ad-video` (local)：Create and run a project-style workflow for story-driven ecommerce product video ads. Use when the user wants to promote a product with a na… 位置：`/Users/pechen/.codex/skills/product-story-ad-video/SKILL.md`
- `quant-local-research` (local)：Use when Peter asks to research, backtest, validate, optimize, compare, or port ETF/stock quantitative trading strategies using the local Qu… 位置：`/Users/pechen/.codex/skills/quant-local-research/SKILL.md`
- `script-writing-studio` (local)：端到端中文剧本创作工作室。用于剧本、竖屏短剧、动画脚本、动态漫画脚本、完整剧本扩写、台词稿、项目资产库、AI 视频分镜、Seedance 2.0 视频提示词、后期 BGM/配乐/声音设计的完整开发流程。用户想从灵感写故事、生成大纲或项目档案、把项目档案和大纲扩写成完整剧本、会诊已… 位置：`/Users/pechen/.codex/skills/script-writing-studio/SKILL.md`
- `sealseek-canvas` (local)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or ma… 位置：`/Users/pechen/.codex/skills/sealseek-canvas/SKILL.md`
- `sealseek-chat-control` (local)：Control and inspect the user's running SealSeek/SealClaw conversations through the local `sealseek-chat` CLI. Use when Codex needs to create… 位置：`/Users/pechen/.codex/skills/sealseek-chat-control/SKILL.md`
- `sealseek-course-doc-writer` (local)：Write and maintain SealSeek/玺虾 learner-facing course documents, Feishu handbooks, chapter sub-documents, and copyable prompt-based class mat… 位置：`/Users/pechen/.codex/skills/sealseek-course-doc-writer/SKILL.md`
- `sealseek-execution-auditor` (local)：Audit SealSeek conversation execution traces to reconstruct tool calls, retries, fallbacks, side effects, skipped validation, and false-succ… 位置：`/Users/pechen/.codex/skills/sealseek-execution-auditor/SKILL.md`
- `seedance-commerce-video` (local)：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selli… 位置：`/Users/pechen/.codex/skills/seedance-commerce-video/SKILL.md`
- `seedance-video` (local)：Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedance 2.0 through the s… 位置：`/Users/pechen/.codex/skills/seedance-video/SKILL.md`
- `seedaudiocli` (local)：Use the local `seedaudiocli` system CLI to generate audio with EvoLink Doubao Seed-Audio 1.0. Use when an Agent needs background music, prod… 位置：`/Users/pechen/.codex/skills/seedaudiocli/SKILL.md`
- `shop-product-diagnosis` (local)：Diagnose an ecommerce shop from a standard 店铺商品 Excel workbook and produce a tabbed HTML report plus an XMind action map. Use when Codex rec… 位置：`/Users/pechen/.codex/skills/shop-product-diagnosis/SKILL.md`
- `skill-forward-test` (local)：Validate newly created or updated Codex skills with a clean sub-agent regression loop. Use when the user asks to test, verify, forward-test,… 位置：`/Users/pechen/.codex/skills/skill-forward-test/SKILL.md`
- `story-driven-product-ad` (local)：Use when creating emotionally driven short-video story ads, Douyin/TikTok product-placement stories, product-in-story scripts, or story-firs… 位置：`/Users/pechen/.codex/skills/story-driven-product-ad/SKILL.md`
- `ths-rebalance-planner` (local)：Generate a rebalance plan for the currently selected Tonghuashun 同花顺 account from pasted JoinQuant/模拟策略 target holdings. Use when the user p… 位置：`/Users/pechen/.codex/skills/ths-rebalance-planner/SKILL.md`
- `wdt-dingtalk-logistics-dashboard` (local)：Maintain a DingTalk AI table logistics anomaly dashboard for ecommerce orders. Use when the user asks to initialize or update the logistics … 位置：`/Users/pechen/.codex/skills/wdt-dingtalk-logistics-dashboard/SKILL.md`
- `wdt-inventory-replenishment` (local)：Run Wangdian ERP inventory replenishment monitoring with wdtcli, derive SKU warning thresholds from historical sales, generate a purchase re… 位置：`/Users/pechen/.codex/skills/wdt-inventory-replenishment/SKILL.md`
- `wdt-logistics-anomaly-report` (local)：End-to-end 旺店通/WDT order logistics anomaly analysis. Use when the user asks to analyze ecommerce order logistics, find abnormal shipments, c… 位置：`/Users/pechen/.codex/skills/wdt-logistics-anomaly-report/SKILL.md`
- `workctl` (local)：管理 Work Agent 平台能力。通过 `workctl schema` 发现动态产品和命令，再用结构化输出执行操作。 位置：`/Users/pechen/.codex/skills/workctl/SKILL.md`
- `workctl-operator` (local)：安装、升级、认证、发现并使用 Work Agent CLI (`workctl`)。适用于通过 `workctl schema` 发现并调用阿里巴巴国际站商家经营工具，处理店铺经营数据、广告、发品、商品优化、AI 图片/视频、旺铺、选品、物流、交易、IM、知识问答、深度研究等场景… 位置：`/Users/pechen/.codex/skills/workctl/workctl-operator/SKILL.md`
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
- `lark-approval` (local)：飞书审批：查询和处理审批待办/已办/实例，搜索可发起审批定义、查看定义详情并发起原生审批实例。当用户要处理审批任务、查看审批实例、搜索或发起审批时使用。审批待办不是飞书任务；非审批类待办走 lark-task。不负责创建审批定义；三方审批定义不走原生提单。 位置：`/Users/pechen/.hermes/skills/lark-approval/SKILL.md`
- `lark-attendance` (local)：飞书考勤打卡：查询自己的考勤打卡记录 位置：`/Users/pechen/.hermes/skills/lark-attendance/SKILL.md`
- `lark-base` (local)：飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、workflow、角色权限；遇到 Base/多维表格/bitable 或 /base/ 链接时使用。文件导入转 lark-drive，认证/授权转 lark-shared。 位置：`/Users/pechen/.hermes/skills/lark-base/SKILL.md`
- `lark-calendar` (local)：飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走 lark-vc）、待办任务（走 lark-task）。 位置：`/Users/pechen/.hermes/skills/lark-calendar/SKILL.md`
- `lark-contact` (local)：飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名。当用户提到某人姓名要下一步发消息 / 排日程,或拿到 open_id 想查具体信息时使用。不负责部门树遍历、按部门列员工、… 位置：`/Users/pechen/.hermes/skills/lark-contact/SKILL.md`
- `lark-doc` (local)：飞书云文档（Docx / Wiki 文档）：读取和编辑飞书文档内容。当用户给出文档 URL 或 token，或需要查看、创建、编辑文档、插入或下载文档图片附件时使用。文档中嵌入的电子表格、多维表格、画板，先用本 skill 提取 token 再切到对应 skill。当用户给出 d… 位置：`/Users/pechen/.hermes/skills/lark-doc/SKILL.md`
- `lark-drive` (local)：飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、评论/权限/订阅、标题、版本和本地文件导入。用户需要整理云盘目录、处理云空间资源 URL/token，或导入 Word/Markdown/Excel/CSV/PP… 位置：`/Users/pechen/.hermes/skills/lark-drive/SKILL.md`
- `lark-event` (local)：Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <EventKey>` (covers IM … 位置：`/Users/pechen/.hermes/skills/lark-event/SKILL.md`
- `lark-im` (local)：飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive Card）、监听卡片按钮回调（card.action.trigger）。当… 位置：`/Users/pechen/.hermes/skills/lark-im/SKILL.md`
- `lark-mail` (local)：飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for mail/email intent only. Do not use f… 位置：`/Users/pechen/.hermes/skills/lark-mail/SKILL.md`
- `lark-markdown` (local)：飞书 Markdown：查看、创建、上传、编辑和比较 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取、修改、局部 patch 或比较差异时使用。不负责将 Markdown 导入为飞书在线文档，也不负责文件搜索、权限、评论、移动、删除等云空间管理操作。 位置：`/Users/pechen/.hermes/skills/lark-markdown/SKILL.md`
- `lark-minutes` (local)：飞书妙记：搜索妙记、查看妙记基础信息、下载/上传音视频、读取或编辑妙记的产物内容、改标题、替换说话人/关键词。当给出minute_token、本地音视频文件，要查/改/转妙记产物时使用；本地音视频转纪要/逐字稿优先走本 skill，不要用 ffmpeg/whisper 本地转写。… 位置：`/Users/pechen/.hermes/skills/lark-minutes/SKILL.md`
- `lark-okr` (local)：飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标、关键结果、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。不负责：待办任务管理（lark-task）、日程/会议安排（lark-calendar）、绩效评估 位置：`/Users/pechen/.hermes/skills/lark-okr/SKILL.md`
- `lark-openapi-explorer` (local)：飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。 位置：`/Users/pechen/.hermes/skills/lark-openapi-explorer/SKILL.md`
- `lark-shared` (local)：Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain permissions (--domain, including all/docs… 位置：`/Users/pechen/.hermes/skills/lark-shared/SKILL.md`
- `lark-sheets` (local)：飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表、条件格式、筛选器、迷你图、浮动图片等对象的创建与维护。当用户需要创建电子表格、… 位置：`/Users/pechen/.hermes/skills/lark-sheets/SKILL.md`
- `lark-skill-maker` (local)：创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。 位置：`/Users/pechen/.hermes/skills/lark-skill-maker/SKILL.md`
- `lark-slides` (local)：飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/ URL/token 时，也应直接使用本 skill，不要因为域名… 位置：`/Users/pechen/.hermes/skills/lark-slides/SKILL.md`
- `lark-task` (local)：飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务进度、管理项目清单或给他人分配任务、为任… 位置：`/Users/pechen/.hermes/skills/lark-task/SKILL.md`
- `lark-vc` (local)：飞书视频会议：搜索历史会议记录、查询会议纪要（总结/待办/章节/逐字稿）、查询参会人快照。当用户查询已结束的会议、获取会议产物（纪要/妙记）、查看参会人时使用；查询未来日程走 lark-calendar。不负责：Agent 真实入会/离会、会中实时事件（走 lark-vc-age… 位置：`/Users/pechen/.hermes/skills/lark-vc/SKILL.md`
- `lark-whiteboard` (local)：飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此 skill。不负责：飞书云文档内容编辑（lark-doc）、文档内嵌电子表格/Base（lark-sheets /… 位置：`/Users/pechen/.hermes/skills/lark-whiteboard/SKILL.md`
- `lark-wiki` (local)：飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出 doubao.com 的 /wiki/… 位置：`/Users/pechen/.hermes/skills/lark-wiki/SKILL.md`
- `lark-workflow-meeting-summary` (local)：会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。 位置：`/Users/pechen/.hermes/skills/lark-workflow-meeting-summary/SKILL.md`
- `lark-workflow-standup-report` (local)：日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。 位置：`/Users/pechen/.hermes/skills/lark-workflow-standup-report/SKILL.md`
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

- `1688-distribution` (local)：1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。 位置：`/Users/pechen/.openclaw/workspace/skills/1688-distribution/SKILL.md`
- `1688-marketing` (local)：1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、商机、市场机会、找商机、查商机，不要在用… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-marketing/SKILL.md`
- `1688-product-find` (local)：1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以图搜图、选品、批发、找货源、热销、比价、… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-product-find/SKILL.md`
- `1688-shopkeeper` (local)：1688选品铺货 + 商机趋势专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥 (5) 查看即时商机热榜 (6) 查看类目/行业趋势与价格分布 (7) 生成店铺经… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-shopkeeper-official/SKILL.md`
- `1688-source-suppliers` (local)：1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发场景：找商品/选品 → 1688-pro… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-source-suppliers/SKILL.md`
- `1688-sourcing-inquiry` (local)：1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报价。 触发词：询盘、询价、寻源、采购咨询… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-sourcing-inquiry/SKILL.md`
- `ecom-market-rank` (local)：电商市场排行榜数据分析。适用于用户上传商品排行榜 Excel/CSV 文件（如淘宝生意参谋市场排行导出）时触发。输入：商品排行榜表格文件（xlsx/csv）。输出：文本分析总结 + 离线 HTML 可视化报告。触发场景：用户发送表格并要求分析市场排行、商品排行、品类分析、竞品分析… 位置：`/Users/pechen/.openclaw/workspace/skills/ecom-market-rank/SKILL.md`
- `mcporter` (local)：Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio). 位置：`/Users/pechen/.openclaw/workspace/skills/mcporter/SKILL.md`
- `sealseek-canvas` (local)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or ma… 位置：`/Users/pechen/.openclaw/workspace/skills/sealseek-canvas/SKILL.md`
- `taobao-native` (local)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check ord… 位置：`/Users/pechen/.openclaw/workspace/skills/taobao-native/SKILL.md`
- `web-reader` (local)：用真实 Chrome 浏览器（保留登录态）读取网页并压缩 DOM，供 AI 高效分析。适用于需要访问需要登录的网站（淘宝、生意参谋、千牛、飞书等）时抓取页面数据、进行页面操作（点击、填表、滚动）。核心优势：真实 Chrome 不被反爬识别，DOM 压缩后 token 消耗降低 9… 位置：`/Users/pechen/.openclaw/workspace/skills/web-reader/SKILL.md`

### SealSeek

- `ai-agent-skill-registry-sync` (workspace-skills)：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM … 位置：`/Users/pechen/.sealseek/workspace/skills/AI Agent Skill Registry Sync/SKILL.md`
- `llm-wiki` (workspace-skills)：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered… 位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (workspace-skills)：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, a… 位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki Audit and Optimization/SKILL.md`
- `llm-wiki-ingest` (workspace-skills)：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including ima… 位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki Ingest/SKILL.md`
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
- `sealseek-canvas` (workspace-skills)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or ma… 位置：`/Users/pechen/.sealseek/workspace/skills/sealseek-canvas/SKILL.md`
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
- `1688-88syt` (default-workspace-skills)：线下B2B交易的得力帮手，一句话搞定全流程操作！无论您是卖家还是买家，只需一句指令，即可轻松完成电子合约（采购单/合同）创建、签署、确认收货、退款等核心操作，全面支持账号状态查询、实名认证、绑卡及交易，让每一步交易流程更清晰、更可控。通过智能化交互，实现交易流程数字化，提升协作效… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-88syt/SKILL.md`
- `1688-distribution` (default-workspace-skills)：1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-distribution/SKILL.md`
- `1688-marketing` (default-workspace-skills)：1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、商机、市场机会、找商机、查商机，不要在用… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-marketing/SKILL.md`
- `1688-product-find` (default-workspace-skills)：1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以图搜图、选品、批发、找货源、热销、比价、… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-product-find/SKILL.md`
- `1688-shopkeeper` (default-workspace-skills)：1688选品铺货专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥。 触发词：帮我找商品、在1688搜、选品、铺货、上架、查店铺、配置AK、1688找货。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-shopkeeper/SKILL.md`
- `1688-source-suppliers` (default-workspace-skills)：1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发场景：找商品/选品 → 1688-pro… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-source-suppliers/SKILL.md`
- `1688-sourcing-inquiry` (default-workspace-skills)：1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报价。 触发词：询盘、询价、寻源、采购咨询… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-sourcing-inquiry/SKILL.md`
- `ai-agent-skill-registry-sync` (default-workspace-skills)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wik… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ai-agent-skill-registry-sync/SKILL.md`
- `ai-agent-skill-registry-sync` (default-workspace-skills)：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM … 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ai-agent-skill-registry-sync.symlink-bak-20260610154600/SKILL.md`
- `bge-title-creation` (default-workspace-skills)：宝工（bge宝工）品牌专用淘宝标题生成器。输入商品图片和搜索词表 Excel，输出 5 个 59~60 字符候选标题并生成 HTML 报告（制作方法、5个标题、并集覆盖统计、原搜索词表逐条标注）。触发：宝工标题、给宝工商品做标题、生成淘宝标题、根据搜索词表做标题、标题制作、做几个… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/bge-title-creation/SKILL.md`
- `customer-service-diagnosis` (default-workspace-skills)：客服聊天记录诊断工具。输入客服聊天截图或文档，输出客服话术问题诊断、消费者需求甄别分析、推荐话术评估、改善方案及示范回复。 触发：用户提到"客服诊断""聊天记录分析""话术诊断""客服话术""客服聊天""客服培训""客服质检""聊天记录点评""客服回复"或提供客服聊天截图/文档要… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/customer-service-diagnosis/SKILL.md`
- `damopan-product-ranking-selection` (default-workspace-skills)：Analyze DMP/达摩盘 commodity ranking export tables and generate a product-selection HTML report. Use when the user provides a 达摩盘商品榜单/市场榜单导出表 a… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/damopan-product-ranking-selection/SKILL.md`
- `demand-research` (default-workspace-skills)：Use when the user asks for 需求调研, consumer demand research, ecommerce product demand analysis, selling point planning, marketing visual plann… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/demand-research/SKILL.md`
- `detail-page-batch-optimization` (default-workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/detail-page-batch-optimization/SKILL.md`
- `dianshang-browser` (default-workspace-skills)：电商浏览器 Skill。固定端口 9223，修复 CDP 连接问题。 支持复用已运行的 Chrome 实例，或自动启动新实例。 与其他 agent 共享同一 Chrome 配置（~/.dianshang-chrome-profile）。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/dianshang-browser/SKILL.md`
- `docx` (default-workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/docx/SKILL.md`
- `douyin-category-trend-report` (default-workspace-skills)：抖音类目榜单趋势产品 HTML 报告生成 Skill。输入观数/抖音商品榜单趋势分析 Excel（含“趋势分析”sheet 与 4 周商品榜单，字段如 当前排名、趋势、排名变化、商品名称、商品ID、价格带、店铺名称、排名(第1周~第4周)、支付买家数、访客数、商品图片链接、商品链… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/douyin-category-trend-report/SKILL.md`
- `ecommerce-gross-profit-reconciliation` (default-workspace-skills)：多格式电商财务口径毛利核算 Skill。用于用户提供支付宝/聚合支付/平台账单、淘宝/京东/拼多多/其他平台发货明细、货品成本表，要求“按财务到账口径计算毛利”“从账单反查货品和成本”“生成账单维度和产品维度毛利表”“做店铺收入-货物成本核算”时使用。支持一个 Excel 多 s… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-gross-profit-reconciliation/SKILL.md`
- `ecommerce-profit-reconciliation` (default-workspace-skills)：电商资金利润闭合表生成 Skill。输入淘宝/天猫等电商平台下载的资金账单、聚合账户、保证金、推广账户等 Excel/CSV 数据，标准化流水、分类映射、按日核算收入费用与不影响利润项，输出带公式可复核的“按日核算的店铺资金利润闭合表”、规则说明、未识别流水和余额闭合校验。适合“… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-profit-reconciliation/SKILL.md`
- `成套视觉生成` (default-workspace-skills)：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-generation/SKILL.md`
- `ecommerce-visual-plan` (default-workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-plan/SKILL.md`
- `电商视觉全套生成` (default-workspace-skills)：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-suite/SKILL.md`
- `express-bill-reconciliation` (default-workspace-skills)：>- Reconcile express carrier bills against merchant-expected charges for e-commerce shipments. Use when the user provides or wants to proces… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/express-bill-reconciliation/SKILL.md`
- `express-weight-reconciliation` (default-workspace-skills)：Generate and format an Excel reconciliation report comparing express carrier billed weights against internally estimated shipment weights. U… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/express-weight-reconciliation/SKILL.md`
- `gpt生图` (default-workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GP… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/gpt-image-generation/SKILL.md`
- `international-station-seller-assistant` (default-workspace-skills)：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/international-station-seller-assistant/SKILL.md`
- `jd-market-analysis` (default-workspace-skills)：京东搜索市场分析，按关键词采集京东搜索结果并生成 XLSX 数据表与 HTML 分析报告。 触发：用户需要京东市场分析、京东商品数据抓取、京东关键词市场商品结构、价格/销量/品牌/店铺类型分布时使用。 也适用于：分析京东某个品类的竞争格局、品牌排名、价格带分布、标题关键词策略。 … 位置：`/Users/pechen/.sealseek/workspaces/default/skills/jd-market-analysis/SKILL.md`
- `keyword-assistant` (default-workspace-skills)：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-assistant/SKILL.md`
- `keyword-data-export` (default-workspace-skills)：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-data-export/SKILL.md`
- `keyword-traffic` (default-workspace-skills)：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-traffic/SKILL.md`
- `llm-wiki-audit-and-optimization` (default-workspace-skills)：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, a… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-audit-and-optimization.symlink-bak-20260610154600/SKILL.md`
- `llm-wiki-bootstrap` (default-workspace-skills)：Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set up an LLM Wiki from … 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-bootstrap/SKILL.md`
- `llm-wiki-ingest` (default-workspace-skills)：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including ima… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-ingest.symlink-bak-20260610154600/SKILL.md`
- `llm-wiki-recompile-runner` (default-workspace-skills)：Orchestrate repair and memory-first reorganization of existing LLM Wiki domains or learning/source packages that contain shell/thin pages, p… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-recompile-runner/SKILL.md`
- `llm-wiki` (default-workspace-skills)：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki.symlink-bak-20260610154600/SKILL.md`
- `market-analysis` (default-workspace-skills)：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-analysis/SKILL.md`
- `market-trend` (default-workspace-skills)：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-trend/SKILL.md`
- `new-product-launch` (default-workspace-skills)：淘宝新品上架前全套准备。输入商品ID，自动完成：产品分析、竞品价格带、主图策略、详情页结构、标题关键词。串联淘宝商品助手、市场分析、关键词助手，输出可直接执行的上架方案。触发：用户说"新品上架""上架准备""帮我准备上架""新品分析"。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/new-product-launch/SKILL.md`
- `product-grading` (default-workspace-skills)：通用电商产品分级与链接经营诊断。用于用户提供淘宝、天猫或其他电商平台的全店商品 Excel/CSV,要求"产品分级""商品分层""SABC分级""识别同类产品""同类链接对比""逐链接优化建议""付费/点击/转化诊断""责任岗位分配"或"整店产品规划"时。先动态识别任意类目的同类… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-grading/SKILL.md`
- `product-page-seedance-video` (default-workspace-skills)：Build a structured product-page visual asset library from full ecommerce product page images, classify and tag main images/SKU images/detail… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-page-seedance-video/SKILL.md`
- `product-selling-points-extractor` (default-workspace-skills)：商品卖点提炼助手。从商品图片（直接上传、本地路径、网络URL、文本文件中提取的路径）中客观描述商品外观，提炼3-5个核心卖点，区分事实与推测，生成包含图片和卖点文字的HTML报告。Use for 商品卖点提炼, 卖点提取, 商品图片分析, 卖点报告, selling points… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-selling-points-extractor/SKILL.md`
- `qa-merge-clean` (default-workspace-skills)：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/qa-merge-clean/SKILL.md`
- `report-docx-formatter` (default-workspace-skills)：报告文档格式化与内容优化工具。将输入内容（Word/PDF/XMind/Excel或用户文本）进行内容扩写与优化，然后按照玺承经营复盘报告的视觉规范直接生成Word文档。 分两阶段执行： 1. 内容扩写与优化 → 输出结构化JSON 2. 直接生成Word文档 → Node.js… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/report-docx-formatter/SKILL.md`
- `review-cleaning-assistant` (default-workspace-skills)：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/review-cleaning-assistant/SKILL.md`
- `sealseek-skill-creator` (default-workspace-skills)：SealSeek Skill 创建器——创建、更新、审查、测试一般 SealSeek Skill 的增强层。 触发：创建/新建/做一个 Skill、更新/修改/优化 Skill、审查/检查/测试 Skill、帮我写一个 Skill、 这个 Skill 怎么改、帮我做一个 skil… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/sealseek-skill-creator/SKILL.md`
- `search-term-blue-ocean-report` (default-workspace-skills)：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-blue-ocean-report/SKILL.md`
- `search-term-relevance-scorer` (default-workspace-skills)：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-relevance-scorer/SKILL.md`
- `seedance-commerce-video` (default-workspace-skills)：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selli… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/seedance-commerce-video/SKILL.md`
- `seedance-video` (default-workspace-skills)：Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedance 2.0 through the s… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/seedance-video/SKILL.md`
- `shop-product-diagnosis` (default-workspace-skills)：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex re… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/shop-product-diagnosis/SKILL.md`
- `single-image-optimization` (default-workspace-skills)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimiz… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/single-image-optimization/SKILL.md`
- `skill-forward-test` (default-workspace-skills)：用主对话 + 干净子 Agent 回归测试新建或优化后的 Skill。用于 Peter 要求测试、验证、回归测试、确认 skill 是否真实落盘、是否能在无当前对话上下文的新 Agent 中独立触发和执行时；尤其适用于创建/优化 Agent Skill 后防止上下文污染、假落盘、… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/skill-forward-test/SKILL.md`
- `生意参谋搜索词排行下载` (default-workspace-skills)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/sycm-search-rank-download/SKILL.md`
- `taobao-item` (default-workspace-skills)：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-item/SKILL.md`
- `taobao-native` (default-workspace-skills)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check ord… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-native/SKILL.md`
- `taobao-profit-statement` (default-workspace-skills)：淘宝利润表自动生成 Skill。输入包含淘宝资金账单、映射表、聚合账户、保证金等 sheet 的 Excel 工作簿，自动生成“利润表”。适合“生成淘宝利润表”“财税表格处理”“用淘宝账单做利润表”“自动完成利润表”这类需求。生成时必须忽略手工“利润表”sheet，不能读取或复用… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-profit-statement/SKILL.md`
- `taobao-search-parser` (default-workspace-skills)：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-search-parser/SKILL.md`
- `web-image-extractor` (default-workspace-skills)：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/web-image-extractor/SKILL.md`
- `work-browser` (default-workspace-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser/SKILL.md`
- `work-browser2` (default-workspace-skills)：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser2/SKILL.md`
- `xiaobai-category-insight` (default-workspace-skills)：老兵小白 AI智能体工具箱｜类目洞察助手。基于电商老兵小白V的类目洞察选品方法论，用于分析生意参谋「类目挖掘」成交金额/成交单量/需求供给比三张表，以及「类目洞察」价格分析和属性分析表，完成类目机会初筛、子类目价格带/属性下钻、机会分层、报告输出和下一步竞品验证交接。Use wh… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/xiaobai-category-insight/SKILL.md`
- `xmind-cli` (default-workspace-skills)：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/xmind-cli/SKILL.md`
- `detail-page-batch-optimization` (migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/hermes/SKILL.md`
- `detail-page-batch-optimization` (migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/sealseek/SKILL.md`
- `guanshu-review` (migration-bundle)：观数浏览器扩展前端代码评审工具。对分支代码进行规范检查，生成评审报告。检查项：P0-颜色硬编码、内联样式、if嵌套、重复造轮子、Content Script挂载方式；P1-BEM命名、魔法数字、第三方库引入；P2-文件职责单一、长文件拆分。仅适用于 xc-sealseek-ext… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/fe-guanshu-review/SKILL.md`
- `gemini-image` (migration-bundle)：Generate, edit, and iterate on images using Gemini image models via 12API. Use when the user asks to create, generate, draw, design, or prod… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/gemini-image/SKILL.md`
- `outline-paper-builder` (migration-bundle)：Reconstruct complete teaching-grade knowledge from mm/xmind outlines and output reviewable artifacts: lecture notes, optional long-form pape… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/outline-paper-builder/SKILL.md`
- `single-image-optimization` (migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimiz… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/hermes/SKILL.md`
- `single-image-optimization` (migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimiz… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/sealseek/SKILL.md`
- `llm-wiki` (standalone-local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and li… 位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (standalone-local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answe… 位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `llm-wiki-ingest` (standalone-local)：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, includin… 位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-ingest/SKILL.md`
- `llm-wiki-recompile-runner` (standalone-local)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages,… 位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-recompile-runner/SKILL.md`
- `生意参谋搜索词排行下载` (standalone-local)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”… 位置：`/Users/pechen/sealseek/RPA下载原型/SKILL.md`
- `xmind-cli` (standalone-local)：XMind 脑图输出助手 —— 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/sealseek/XMindCLI交付包V2/package/skills/xmind-cli/SKILL.md`
- `taobao-market-analysis` (standalone-local)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/sealseek/backup/淘宝商品市场分析_20260418_210055/SKILL.md`
- `embedded-captions` (standalone-local)：Add captions to a talking-head video. ONE catalog (CATALOG.md) of 32 visual identities behind two engines: column-flow (captions composited … 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/embedded-captions/SKILL.md`
- `faceless-explainer` (standalone-local)：turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video, up to ~3 min (sweet spot 30-90s), where every v… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/faceless-explainer/SKILL.md`
- `general-video` (standalone-local)：The fallback workflow for authoring custom HyperFrames video compositions at any length or format — longer or multi-scene pieces, brand / si… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/general-video/SKILL.md`
- `graphic-overlays` (standalone-local)：Package an existing talking-head / interview / podcast video by layering timed, designed GRAPHIC OVERLAY cards onto the playing video — titl… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/graphic-overlays/SKILL.md`
- `hyperframes` (standalone-local)：READ THIS FIRST for any request to make, create, edit, animate, or render a video, animation, or motion graphic — a promo, explainer, captio… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes/SKILL.md`
- `hyperframes-animation` (standalone-local)：All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techni… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-animation/SKILL.md`
- `hyperframes-cli` (standalone-local)：HyperFrames CLI dev loop. Use when running npx hyperframes init, add, catalog, capture, lint, validate, inspect, layout, snapshot, preview, … 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-cli/SKILL.md`
- `hyperframes-core` (standalone-local)：The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-core/SKILL.md`
- `hyperframes-creative` (standalone-local)：Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narratio… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-creative/SKILL.md`
- `hyperframes-media` (standalone-local)：Audio and media assets for HyperFrames compositions, produced by one shared audio engine (`scripts/audio.mjs`) — multi-provider TTS (HeyGen … 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-media/SKILL.md`
- `hyperframes-registry` (standalone-local)：Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or compo… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-registry/SKILL.md`
- `motion-graphics` (standalone-local)：Use when the user wants a short, design-led motion graphic where motion is the message: kinetic typography, stat or number count-up, chart/d… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/motion-graphics/SKILL.md`
- `music-to-video` (standalone-local)：Use when the user has a music track (an audio file, or a video to pull audio from) and wants a beat-synced HyperFrames video, calm to hard-h… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/music-to-video/SKILL.md`
- `pr-to-video` (standalone-local)：turn a GitHub pull request (a PR URL like github.com/<owner>/<repo>/pull/<N>, an <owner>/<repo>#<N> ref, or 'this PR' in a checked-out repo)… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/pr-to-video/SKILL.md`
- `product-launch-video` (standalone-local)：turn a product or marketing URL, pasted script, or brief into a product launch video, including SaaS promos, feature reveals, app launches, … 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/product-launch-video/SKILL.md`
- `remotion-to-hyperframes` (standalone-local)：Port an existing Remotion (React) composition to HyperFrames HTML. Use ONLY when the user explicitly asks to port/convert/migrate/translate … 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/remotion-to-hyperframes/SKILL.md`
- `slideshow` (standalone-local)：Author a HyperFrames slideshow composition — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branchi… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/slideshow/SKILL.md`
- `website-to-video` (standalone-local)：Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals). Uses h… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/website-to-video/SKILL.md`
- `商品成套视觉规划skill` (standalone-local)：把一个商品的多源证据（搜索词、评价、问大家、商品图）整理成**可执行的成套视觉规划**，输出给后续设计、生图、详情页优化或投放团队直接使用的规划结果。 位置：`/Users/pechen/sealseek/商品成套视觉规划skill/SKILL.md`
- `货号跨店铺表现差异分析` (standalone-local)：🎯 任务目标 基于指定货号或全量数据，分析并识别同一货号在不同店铺/链接间销售表现差异显著的商品，帮助商家发现潜在的分销优化机会。 位置：`/Users/pechen/sealseek/货号跨店铺表现差异分析/SKILL.md`

## 能力分类索引

### 知识库 / 知识管理 / LLM Wiki

- `ai-agent-skill-registry-sync` (Codex, local)：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill… 位置：`/Users/pechen/.codex/skills/ai-agent-skill-registry-sync/SKILL.md`
- `brand-planning-report` (Codex, local)：Generate a user-facing ecommerce brand planning HTML report from a standard 店铺商品 Excel workbook, using Peter's brand-strategy LLM Wiki for positioning… 位置：`/Users/pechen/.codex/skills/brand-planning-report/SKILL.md`
- `dws` (Codex, local)：管理钉钉产品能力(AI表格/AI搜问/日历/通讯录/群聊与机器人/待办/审批/考勤/日志/DING消息/开放平台文档/钉钉文档/钉钉云盘/AI听记/邮箱/在线电子表格/知识库等)。当用户需要操作表格数据、管理日程会议、模糊找人/查谁负责某事项、查询通讯录、管理群聊、机器人发消息、创建待办、提交审批、… 位置：`/Users/pechen/.codex/skills/dws/SKILL.md`
- `lark-structured-doc-writer` (Codex, local)：Create or substantially rewrite clear, complete, highly readable Lark/Feishu project and knowledge documents. Use when an agent must organize reposito… 位置：`/Users/pechen/.codex/skills/lark-structured-doc-writer/SKILL.md`
- `llm-wiki` (Codex, local)：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from thei… 位置：`/Users/pechen/.codex/skills/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (Codex, local)：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-… 位置：`/Users/pechen/.codex/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `llm-wiki-bootstrap` (Codex, local)：Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set up an LLM Wiki from scratch, c… 位置：`/Users/pechen/.codex/skills/llm-wiki-bootstrap/SKILL.md`
- `llm-wiki-ingest` (Codex, local)：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or… 位置：`/Users/pechen/.codex/skills/llm-wiki-ingest/SKILL.md`
- `sealseek-course-doc-writer` (Codex, local)：Write and maintain SealSeek/玺虾 learner-facing course documents, Feishu handbooks, chapter sub-documents, and copyable prompt-based class materials. Us… 位置：`/Users/pechen/.codex/skills/sealseek-course-doc-writer/SKILL.md`
- `baoyu-comic` (Hermes, local)：Knowledge comics (知识漫画): educational, biography, tutorial. 位置：`/Users/pechen/.hermes/skills/creative/baoyu-comic/SKILL.md`
- `lark-doc` (Hermes, local)：飞书云文档（Docx / Wiki 文档）：读取和编辑飞书文档内容。当用户给出文档 URL 或 token，或需要查看、创建、编辑文档、插入或下载文档图片附件时使用。文档中嵌入的电子表格、多维表格、画板，先用本 skill 提取 token 再切到对应 skill。当用户给出 doubao.com … 位置：`/Users/pechen/.hermes/skills/lark-doc/SKILL.md`
- `lark-drive` (Hermes, local)：飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、评论/权限/订阅、标题、版本和本地文件导入。用户需要整理云盘目录、处理云空间资源 URL/token，或导入 Word/Markdown/Excel/CSV/PPTX/.base 为… 位置：`/Users/pechen/.hermes/skills/lark-drive/SKILL.md`
- `lark-wiki` (Hermes, local)：飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出 doubao.com 的 /wiki/ URL/token… 位置：`/Users/pechen/.hermes/skills/lark-wiki/SKILL.md`
- `douyin-link-to-knowledge` (Hermes, local)：Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transcribing/val… 位置：`/Users/pechen/.hermes/skills/productivity/douyin-link-to-knowledge/SKILL.md`
- `llm-wiki` (Hermes, local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for con… 位置：`/Users/pechen/.hermes/skills/research/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (Hermes, local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result n… 位置：`/Users/pechen/.hermes/skills/research/llm-wiki-audit-and-optimization/SKILL.md`
- `1688-distribution` (OpenClaw, local)：1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。 位置：`/Users/pechen/.openclaw/workspace/skills/1688-distribution/SKILL.md`
- `ai-agent-skill-registry-sync` (SealSeek, workspace-skills)：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill… 位置：`/Users/pechen/.sealseek/workspace/skills/AI Agent Skill Registry Sync/SKILL.md`
- `llm-wiki` (SealSeek, workspace-skills)：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from thei… 位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (SealSeek, workspace-skills)：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-… 位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki Audit and Optimization/SKILL.md`
- `llm-wiki-ingest` (SealSeek, workspace-skills)：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or… 位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki Ingest/SKILL.md`
- `lark-cli-doc-reader` (SealSeek, workspace-skills)：使用用户本机 /opt/homebrew/bin/lark-cli 读取飞书云文档。适用于按文档标题/文件名搜索并读取飞书 Docx/Doc/Wiki，或用户给出飞书文档 URL/token 时读取内容。重点规避 OpenClaw/SealClaw 环境变量导致的 lark-cli config b… 位置：`/Users/pechen/.sealseek/workspace/skills/lark-cli-doc-reader/SKILL.md`
- `1688-distribution` (SealSeek, default-workspace-skills)：1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-distribution/SKILL.md`
- `ai-agent-skill-registry-sync` (SealSeek, default-workspace-skills)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill re… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ai-agent-skill-registry-sync/SKILL.md`
- `ai-agent-skill-registry-sync` (SealSeek, default-workspace-skills)：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ai-agent-skill-registry-sync.symlink-bak-20260610154600/SKILL.md`
- `llm-wiki-audit-and-optimization` (SealSeek, default-workspace-skills)：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-audit-and-optimization.symlink-bak-20260610154600/SKILL.md`
- `llm-wiki-bootstrap` (SealSeek, default-workspace-skills)：Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set up an LLM Wiki from scratch, c… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-bootstrap/SKILL.md`
- `llm-wiki-ingest` (SealSeek, default-workspace-skills)：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-ingest.symlink-bak-20260610154600/SKILL.md`
- `llm-wiki-recompile-runner` (SealSeek, default-workspace-skills)：Orchestrate repair and memory-first reorganization of existing LLM Wiki domains or learning/source packages that contain shell/thin pages, poor routin… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-recompile-runner/SKILL.md`
- `llm-wiki` (SealSeek, default-workspace-skills)：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from thei… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki.symlink-bak-20260610154600/SKILL.md`
- `sealseek-skill-creator` (SealSeek, default-workspace-skills)：SealSeek Skill 创建器——创建、更新、审查、测试一般 SealSeek Skill 的增强层。 触发：创建/新建/做一个 Skill、更新/修改/优化 Skill、审查/检查/测试 Skill、帮我写一个 Skill、 这个 Skill 怎么改、帮我做一个 skill、写 skill.… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/sealseek-skill-creator/SKILL.md`
- `outline-paper-builder` (SealSeek, migration-bundle)：Reconstruct complete teaching-grade knowledge from mm/xmind outlines and output reviewable artifacts: lecture notes, optional long-form paper, and lec… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/outline-paper-builder/SKILL.md`
- `llm-wiki` (SealSeek, standalone-local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for con… 位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki/SKILL.md`
- `llm-wiki-audit-and-optimization` (SealSeek, standalone-local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result n… 位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `llm-wiki-ingest` (SealSeek, standalone-local)：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian… 位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-ingest/SKILL.md`
- `llm-wiki-recompile-runner` (SealSeek, standalone-local)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplet… 位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-recompile-runner/SKILL.md`
- `hyperframes-animation` (SealSeek, standalone-local)：All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND … 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-animation/SKILL.md`

### 视觉 / 内容 / 课件生产

- `1688-opportunity-sourcing-research` (Codex, local)：Research products and suppliers on 1688 with category-first sourcing across market-proven, novel, aesthetic, scenario, premium, and bundle strategies,… 位置：`/Users/pechen/.codex/skills/1688-opportunity-sourcing-research/SKILL.md`
- `ai-story-video-studio` (Codex, local)：Create complete story-driven AI video plans from either product inputs or non-product story/theme ideas. Use when the user wants a short story, emotio… 位置：`/Users/pechen/.codex/skills/ai-story-video-studio/SKILL.md`
- `alibaba-review-report` (Codex, local)：Generate an Alibaba.com International store-review report from a product-detail URL by calling the stable alicli CLI to export the shop's reviews to E… 位置：`/Users/pechen/.codex/skills/alibaba-review-report/SKILL.md`
- `character-reference-turnaround` (Codex, local)：Create consistent character references and three-view turnaround sheets for AI visual/video production. Use when the user needs to define a person or … 位置：`/Users/pechen/.codex/skills/character-reference-turnaround/SKILL.md`
- `compact-commerce-ui` (Codex, local)：Orchestrate the system-wide commerce-ui CLI to create or redesign readable, modular HTML business reports, ecommerce dashboards, SaaS workbenches, ana… 位置：`/Users/pechen/.codex/skills/compact-commerce-ui/SKILL.md`
- `course-deck-factory` (Codex, local)：Build editable course slide decks from a standardized deck spec using Node.js, PptxGenJS, local fonts, structured page types, and a mixed visual pipel… 位置：`/Users/pechen/.codex/skills/course-deck-factory/SKILL.md`
- `dycli` (Codex, local)：Use when the user wants an Agent to operate dycli, automate read-only Douyin Web data collection, search or download Douyin videos, export favorites o… 位置：`/Users/pechen/.codex/skills/dycli/SKILL.md`
- `ecommerce-shop-growth-diagnosis` (Codex, local)：Diagnose one ecommerce target shop from a standard product-ranking or shop-product .xlsx workbook plus user-confirmed business context. Use when the u… 位置：`/Users/pechen/.codex/skills/ecommerce-shop-growth-diagnosis/SKILL.md`
- `editable-poster-psd-rebuild` (Codex, local)：Rebuild a flattened AI-generated ecommerce poster as a layered Photoshop PSD with a text-free background, hidden original reference, and editable nati… 位置：`/Users/pechen/.codex/skills/editable-poster-psd-rebuild/SKILL.md`
- `image-detail-page` (Codex, local)：根据产品白底图和品类，全自动推断模型、人群、风格，并一站式生成13个策划文件及对应电商图片。 当用户提到主图详情页、电商策划、白底图出方案、主图设计、详情页设计、电商视觉方案时触发。 位置：`/Users/pechen/.codex/skills/image-detail-page/SKILL.md`
- `无限画板 Skill 生成器` (Codex, local)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生成无限画板 skill、做一个无限画板 skill.md、优… 位置：`/Users/pechen/.codex/skills/infinite-canvas-skill-generator/SKILL.md`
- `libtv-cli` (Codex, local)：>- LibTV 官方 CLI（libtv）：在命令行里完整操作 / 运行 LibTV 画布。 凡是和 LibTV 画布 / 项目 / 节点 / 模型 / 素材相关的操作，一律通过 libtv CLI 完成， 包括在提供 `libtv video` 扩展时查看或下载公开作品详情页中的成片。 当用户要… 位置：`/Users/pechen/.codex/skills/libtv-cli/SKILL.md`
- `sealseek-canvas` (Codex, local)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or manage an 无限… 位置：`/Users/pechen/.codex/skills/sealseek-canvas/SKILL.md`
- `seedance-commerce-video` (Codex, local)：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selling points,… 位置：`/Users/pechen/.codex/skills/seedance-commerce-video/SKILL.md`
- `seedance-video` (Codex, local)：Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedance 2.0 through the system-leve… 位置：`/Users/pechen/.codex/skills/seedance-video/SKILL.md`
- `seedaudiocli` (Codex, local)：Use the local `seedaudiocli` system CLI to generate audio with EvoLink Doubao Seed-Audio 1.0. Use when an Agent needs background music, product-video … 位置：`/Users/pechen/.codex/skills/seedaudiocli/SKILL.md`
- `shop-product-diagnosis` (Codex, local)：Diagnose an ecommerce shop from a standard 店铺商品 Excel workbook and produce a tabbed HTML report plus an XMind action map. Use when Codex receives file… 位置：`/Users/pechen/.codex/skills/shop-product-diagnosis/SKILL.md`
- `skill-forward-test` (Codex, local)：Validate newly created or updated Codex skills with a clean sub-agent regression loop. Use when the user asks to test, verify, forward-test, regressio… 位置：`/Users/pechen/.codex/skills/skill-forward-test/SKILL.md`
- `workctl-operator` (Codex, local)：安装、升级、认证、发现并使用 Work Agent CLI (`workctl`)。适用于通过 `workctl schema` 发现并调用阿里巴巴国际站商家经营工具，处理店铺经营数据、广告、发品、商品优化、AI 图片/视频、旺铺、选品、物流、交易、IM、知识问答、深度研究等场景。 也适用于配置 w… 位置：`/Users/pechen/.codex/skills/workctl/workctl-operator/SKILL.md`
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
- `lark-event` (Hermes, local)：Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <EventKey>` (covers IM messages/r… 位置：`/Users/pechen/.hermes/skills/lark-event/SKILL.md`
- `lark-im` (Hermes, local)：飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive Card）、监听卡片按钮回调（card.action.trigger）。当用户需要发消息、查看… 位置：`/Users/pechen/.hermes/skills/lark-im/SKILL.md`
- `lark-sheets` (Hermes, local)：飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表、条件格式、筛选器、迷你图、浮动图片等对象的创建与维护。当用户需要创建电子表格、管理工作表、批量读写… 位置：`/Users/pechen/.hermes/skills/lark-sheets/SKILL.md`
- `lark-slides` (Hermes, local)：飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 W… 位置：`/Users/pechen/.hermes/skills/lark-slides/SKILL.md`
- `lark-whiteboard` (Hermes, local)：飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此 skill。不负责：飞书云文档内容编辑（lark-doc）、文档内嵌电子表格/Base（lark-sheets / lark-base… 位置：`/Users/pechen/.hermes/skills/lark-whiteboard/SKILL.md`
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
- `1688-product-find` (OpenClaw, local)：1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以图搜图、选品、批发、找货源、热销、比价、最便宜、按销量排序、… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-product-find/SKILL.md`
- `sealseek-canvas` (OpenClaw, local)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or manage an 无限… 位置：`/Users/pechen/.openclaw/workspace/skills/sealseek-canvas/SKILL.md`
- `detail-page-batch-optimization` (SealSeek, workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constrain… 位置：`/Users/pechen/.sealseek/workspace/skills/detail-page-batch-optimization/SKILL.md`
- `docx` (SealSeek, workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\… 位置：`/Users/pechen/.sealseek/workspace/skills/docx/SKILL.md`
- `ecommerce-visual-plan` (SealSeek, workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows. 位置：`/Users/pechen/.sealseek/workspace/skills/ecommerce-visual-plan/SKILL.md`
- `gpt生图` (SealSeek, workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GPT 生图能力，不再使… 位置：`/Users/pechen/.sealseek/workspace/skills/gpt生图/SKILL.md`
- `image-understanding` (SealSeek, workspace-skills)：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。 位置：`/Users/pechen/.sealseek/workspace/skills/image-understanding/SKILL.md`
- `sealseek-canvas` (SealSeek, workspace-skills)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or manage an 无限… 位置：`/Users/pechen/.sealseek/workspace/skills/sealseek-canvas/SKILL.md`
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
- `1688-product-find` (SealSeek, default-workspace-skills)：1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以图搜图、选品、批发、找货源、热销、比价、最便宜、按销量排序、… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-product-find/SKILL.md`
- `bge-title-creation` (SealSeek, default-workspace-skills)：宝工（bge宝工）品牌专用淘宝标题生成器。输入商品图片和搜索词表 Excel，输出 5 个 59~60 字符候选标题并生成 HTML 报告（制作方法、5个标题、并集覆盖统计、原搜索词表逐条标注）。触发：宝工标题、给宝工商品做标题、生成淘宝标题、根据搜索词表做标题、标题制作、做几个标题、标题生成报告。… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/bge-title-creation/SKILL.md`
- `demand-research` (SealSeek, default-workspace-skills)：Use when the user asks for 需求调研, consumer demand research, ecommerce product demand analysis, selling point planning, marketing visual planning, main … 位置：`/Users/pechen/.sealseek/workspaces/default/skills/demand-research/SKILL.md`
- `detail-page-batch-optimization` (SealSeek, default-workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constrain… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/detail-page-batch-optimization/SKILL.md`
- `docx` (SealSeek, default-workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/docx/SKILL.md`
- `douyin-category-trend-report` (SealSeek, default-workspace-skills)：抖音类目榜单趋势产品 HTML 报告生成 Skill。输入观数/抖音商品榜单趋势分析 Excel（含“趋势分析”sheet 与 4 周商品榜单，字段如 当前排名、趋势、排名变化、商品名称、商品ID、价格带、店铺名称、排名(第1周~第4周)、支付买家数、访客数、商品图片链接、商品链接），自动识别趋势产… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/douyin-category-trend-report/SKILL.md`
- `成套视觉生成` (SealSeek, default-workspace-skills)：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 / gpt-image-2 完成整套图片生成。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-generation/SKILL.md`
- `ecommerce-visual-plan` (SealSeek, default-workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design and image workflows. 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-plan/SKILL.md`
- `电商视觉全套生成` (SealSeek, default-workspace-skills)：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3:4，场景叙事，含情绪文案）。 每个模块先规划、用户确认后再… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-visual-suite/SKILL.md`
- `gpt生图` (SealSeek, default-workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、生成logo、设计海报。当前只保留 GPT 生图能力，不再使… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/gpt-image-generation/SKILL.md`
- `jd-market-analysis` (SealSeek, default-workspace-skills)：京东搜索市场分析，按关键词采集京东搜索结果并生成 XLSX 数据表与 HTML 分析报告。 触发：用户需要京东市场分析、京东商品数据抓取、京东关键词市场商品结构、价格/销量/品牌/店铺类型分布时使用。 也适用于：分析京东某个品类的竞争格局、品牌排名、价格带分布、标题关键词策略。 排除：京东商品详情页… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/jd-market-analysis/SKILL.md`
- `new-product-launch` (SealSeek, default-workspace-skills)：淘宝新品上架前全套准备。输入商品ID，自动完成：产品分析、竞品价格带、主图策略、详情页结构、标题关键词。串联淘宝商品助手、市场分析、关键词助手，输出可直接执行的上架方案。触发：用户说"新品上架""上架准备""帮我准备上架""新品分析"。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/new-product-launch/SKILL.md`
- `product-page-seedance-video` (SealSeek, default-workspace-skills)：Build a structured product-page visual asset library from full ecommerce product page images, classify and tag main images/SKU images/detail images, c… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-page-seedance-video/SKILL.md`
- `product-selling-points-extractor` (SealSeek, default-workspace-skills)：商品卖点提炼助手。从商品图片（直接上传、本地路径、网络URL、文本文件中提取的路径）中客观描述商品外观，提炼3-5个核心卖点，区分事实与推测，生成包含图片和卖点文字的HTML报告。Use for 商品卖点提炼, 卖点提取, 商品图片分析, 卖点报告, selling points extractio… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-selling-points-extractor/SKILL.md`
- `report-docx-formatter` (SealSeek, default-workspace-skills)：报告文档格式化与内容优化工具。将输入内容（Word/PDF/XMind/Excel或用户文本）进行内容扩写与优化，然后按照玺承经营复盘报告的视觉规范直接生成Word文档。 分两阶段执行： 1. 内容扩写与优化 → 输出结构化JSON 2. 直接生成Word文档 → Node.js + docx直接生… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/report-docx-formatter/SKILL.md`
- `search-term-relevance-scorer` (SealSeek, default-workspace-skills)：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 适合“根据产品图判断哪些搜索词更相关”“给搜索词表做相关度评… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-relevance-scorer/SKILL.md`
- `seedance-commerce-video` (SealSeek, default-workspace-skills)：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selling points,… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/seedance-commerce-video/SKILL.md`
- `seedance-video` (SealSeek, default-workspace-skills)：Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedance 2.0 through the system-leve… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/seedance-video/SKILL.md`
- `shop-product-diagnosis` (SealSeek, default-workspace-skills)：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action map. Use when Codex receives a s… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/shop-product-diagnosis/SKILL.md`
- `single-image-optimization` (SealSeek, default-workspace-skills)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization rout… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/single-image-optimization/SKILL.md`
- `taobao-item` (SealSeek, default-workspace-skills)：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-item/SKILL.md`
- `web-image-extractor` (SealSeek, default-workspace-skills)：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. **自动进化**：探索成功后自动生成解析器代码并写入 skil… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/web-image-extractor/SKILL.md`
- `xmind-cli` (SealSeek, default-workspace-skills)：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/xmind-cli/SKILL.md`
- `detail-page-batch-optimization` (SealSeek, migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constrain… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/hermes/SKILL.md`
- `detail-page-batch-optimization` (SealSeek, migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constrain… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/detail-page-batch-optimization/sealseek/SKILL.md`
- `gemini-image` (SealSeek, migration-bundle)：Generate, edit, and iterate on images using Gemini image models via 12API. Use when the user asks to create, generate, draw, design, or produce any im… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/gemini-image/SKILL.md`
- `single-image-optimization` (SealSeek, migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization rout… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/hermes/SKILL.md`
- `single-image-optimization` (SealSeek, migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization rout… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/single-image-optimization/sealseek/SKILL.md`
- `xmind-cli` (SealSeek, standalone-local)：XMind 脑图输出助手 —— 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。 位置：`/Users/pechen/sealseek/XMindCLI交付包V2/package/skills/xmind-cli/SKILL.md`
- `embedded-captions` (SealSeek, standalone-local)：Add captions to a talking-head video. ONE catalog (CATALOG.md) of 32 visual identities behind two engines: column-flow (captions composited INTO the s… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/embedded-captions/SKILL.md`
- `faceless-explainer` (SealSeek, standalone-local)：turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video, up to ~3 min (sweet spot 30-90s), where every visual is i… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/faceless-explainer/SKILL.md`
- `graphic-overlays` (SealSeek, standalone-local)：Package an existing talking-head / interview / podcast video by layering timed, designed GRAPHIC OVERLAY cards onto the playing video — titles, lower-… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/graphic-overlays/SKILL.md`
- `hyperframes-creative` (SealSeek, standalone-local)：Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat pl… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-creative/SKILL.md`
- `motion-graphics` (SealSeek, standalone-local)：Use when the user wants a short, design-led motion graphic where motion is the message: kinetic typography, stat or number count-up, chart/data-viz hi… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/motion-graphics/SKILL.md`
- `music-to-video` (SealSeek, standalone-local)：Use when the user has a music track (an audio file, or a video to pull audio from) and wants a beat-synced HyperFrames video, calm to hard-hitting. Th… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/music-to-video/SKILL.md`
- `slideshow` (SealSeek, standalone-local)：Author a HyperFrames slideshow composition — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching sequenc… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/slideshow/SKILL.md`
- `website-to-video` (SealSeek, standalone-local)：Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals). Uses headless Ch… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/website-to-video/SKILL.md`
- `商品成套视觉规划skill` (SealSeek, standalone-local)：把一个商品的多源证据（搜索词、评价、问大家、商品图）整理成**可执行的成套视觉规划**，输出给后续设计、生图、详情页优化或投放团队直接使用的规划结果。 位置：`/Users/pechen/sealseek/商品成套视觉规划skill/SKILL.md`

### 电商 / 商品 / 品牌运营

- `dmp-ai-competitor-research` (Codex, local)：自动执行 DMP/达摩盘 AI 竞品研究。输入用户自己的淘宝/天猫商品编号，复用或打开可调试 Chrome，检查达摩盘智能对话是否已打开，等待登录/导航，向达摩盘 AI 提问内部工具提示词，收集竞品销售、搜索、推广、人群、人群资产和店铺层数据，并生成运营可读 HTML 主报告、中文 Excel 证据… 位置：`/Users/pechen/.codex/skills/dmp-ai-competitor-research/SKILL.md`
- `dmp-ai-prompt-pack` (Codex, local)：Generate a copy-ready HTML prompt manual for DMP/达摩盘 AI competitor research from one Taobao/Tmall item ID. Use when the user wants a reusable HTML fil… 位置：`/Users/pechen/.codex/skills/dmp-ai-prompt-pack/SKILL.md`
- `ecommerce-profit-statement-automation` (Codex, local)：Automate ecommerce platform profit statement workbooks from settlement/funds/account bills. Use when the user wants to turn Taobao or other ecommerce … 位置：`/Users/pechen/.codex/skills/ecommerce-profit-statement-automation/SKILL.md`
- `international-station-seller-assistant` (Codex, local)：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl CLI, incl… 位置：`/Users/pechen/.codex/skills/international-station-seller-assistant/SKILL.md`
- `market-ranking-growth-report` (Codex, local)：Generate a Word growth strategy report from 12 months of marketplace ranking spreadsheets for any ecommerce shop and category. Use when the user provi… 位置：`/Users/pechen/.codex/skills/market-ranking-growth-report/SKILL.md`
- `product-story-ad-video` (Codex, local)：Create and run a project-style workflow for story-driven ecommerce product video ads. Use when the user wants to promote a product with a narrative vi… 位置：`/Users/pechen/.codex/skills/product-story-ad-video/SKILL.md`
- `script-writing-studio` (Codex, local)：端到端中文剧本创作工作室。用于剧本、竖屏短剧、动画脚本、动态漫画脚本、完整剧本扩写、台词稿、项目资产库、AI 视频分镜、Seedance 2.0 视频提示词、后期 BGM/配乐/声音设计的完整开发流程。用户想从灵感写故事、生成大纲或项目档案、把项目档案和大纲扩写成完整剧本、会诊已有剧本、精修台词、建… 位置：`/Users/pechen/.codex/skills/script-writing-studio/SKILL.md`
- `story-driven-product-ad` (Codex, local)：Use when creating emotionally driven short-video story ads, Douyin/TikTok product-placement stories, product-in-story scripts, or story-first ecommerc… 位置：`/Users/pechen/.codex/skills/story-driven-product-ad/SKILL.md`
- `wdt-dingtalk-logistics-dashboard` (Codex, local)：Maintain a DingTalk AI table logistics anomaly dashboard for ecommerce orders. Use when the user asks to initialize or update the logistics dashboard,… 位置：`/Users/pechen/.codex/skills/wdt-dingtalk-logistics-dashboard/SKILL.md`
- `wdt-logistics-anomaly-report` (Codex, local)：End-to-end 旺店通/WDT order logistics anomaly analysis. Use when the user asks to analyze ecommerce order logistics, find abnormal shipments, classify de… 位置：`/Users/pechen/.codex/skills/wdt-logistics-anomaly-report/SKILL.md`
- `yuce-product-list-export` (Codex, local)：Use when the user wants to export 行情高手/预策平台 “商品列表” data after they have already logged in and manually navigated to the target report page. The skill … 位置：`/Users/pechen/.codex/skills/yuce-product-list-export/SKILL.md`
- `lark-minutes` (Hermes, local)：飞书妙记：搜索妙记、查看妙记基础信息、下载/上传音视频、读取或编辑妙记的产物内容、改标题、替换说话人/关键词。当给出minute_token、本地音视频文件，要查/改/转妙记产物时使用；本地音视频转纪要/逐字稿优先走本 skill，不要用 ffmpeg/whisper 本地转写。不负责：获取会议关联… 位置：`/Users/pechen/.hermes/skills/lark-minutes/SKILL.md`
- `real-chrome-web-reader` (Hermes, local)：使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。 位置：`/Users/pechen/.hermes/skills/productivity/real-chrome-web-reader/SKILL.md`
- `taobao-native-search-to-excel` (Hermes, local)：使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 位置：`/Users/pechen/.hermes/skills/productivity/taobao-native-search-to-excel/SKILL.md`
- `taobao-search-to-excel` (Hermes, local)：使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 位置：`/Users/pechen/.hermes/skills/productivity/taobao-search-to-excel/SKILL.md`
- `1688-marketing` (OpenClaw, local)：1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、商机、市场机会、找商机、查商机，不要在用户仅询问非1688业… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-marketing/SKILL.md`
- `1688-shopkeeper` (OpenClaw, local)：1688选品铺货 + 商机趋势专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥 (5) 查看即时商机热榜 (6) 查看类目/行业趋势与价格分布 (7) 生成店铺经营日报并输出主营商品… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-shopkeeper-official/SKILL.md`
- `1688-source-suppliers` (OpenClaw, local)：1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发场景：找商品/选品 → 1688-product-find；… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-source-suppliers/SKILL.md`
- `1688-sourcing-inquiry` (OpenClaw, local)：1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报价。 触发词：询盘、询价、寻源、采购咨询、发布采购需求、我有… 位置：`/Users/pechen/.openclaw/workspace/skills/1688-sourcing-inquiry/SKILL.md`
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
- `1688-marketing` (SealSeek, default-workspace-skills)：1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、商机、市场机会、找商机、查商机，不要在用户仅询问非1688业… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-marketing/SKILL.md`
- `1688-shopkeeper` (SealSeek, default-workspace-skills)：1688选品铺货专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥。 触发词：帮我找商品、在1688搜、选品、铺货、上架、查店铺、配置AK、1688找货。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-shopkeeper/SKILL.md`
- `1688-source-suppliers` (SealSeek, default-workspace-skills)：1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发场景：找商品/选品 → 1688-product-find；… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-source-suppliers/SKILL.md`
- `1688-sourcing-inquiry` (SealSeek, default-workspace-skills)：1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报价。 触发词：询盘、询价、寻源、采购咨询、发布采购需求、我有… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-sourcing-inquiry/SKILL.md`
- `damopan-product-ranking-selection` (SealSeek, default-workspace-skills)：Analyze DMP/达摩盘 commodity ranking export tables and generate a product-selection HTML report. Use when the user provides a 达摩盘商品榜单/市场榜单导出表 and asks fo… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/damopan-product-ranking-selection/SKILL.md`
- `dianshang-browser` (SealSeek, default-workspace-skills)：电商浏览器 Skill。固定端口 9223，修复 CDP 连接问题。 支持复用已运行的 Chrome 实例，或自动启动新实例。 与其他 agent 共享同一 Chrome 配置（~/.dianshang-chrome-profile）。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/dianshang-browser/SKILL.md`
- `ecommerce-gross-profit-reconciliation` (SealSeek, default-workspace-skills)：多格式电商财务口径毛利核算 Skill。用于用户提供支付宝/聚合支付/平台账单、淘宝/京东/拼多多/其他平台发货明细、货品成本表，要求“按财务到账口径计算毛利”“从账单反查货品和成本”“生成账单维度和产品维度毛利表”“做店铺收入-货物成本核算”时使用。支持一个 Excel 多 sheet 或多个 E… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-gross-profit-reconciliation/SKILL.md`
- `ecommerce-profit-reconciliation` (SealSeek, default-workspace-skills)：电商资金利润闭合表生成 Skill。输入淘宝/天猫等电商平台下载的资金账单、聚合账户、保证金、推广账户等 Excel/CSV 数据，标准化流水、分类映射、按日核算收入费用与不影响利润项，输出带公式可复核的“按日核算的店铺资金利润闭合表”、规则说明、未识别流水和余额闭合校验。适合“生成电商利润核算表”… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-profit-reconciliation/SKILL.md`
- `international-station-seller-assistant` (SealSeek, default-workspace-skills)：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl CLI, incl… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/international-station-seller-assistant/SKILL.md`
- `keyword-assistant` (SealSeek, default-workspace-skills)：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-assistant/SKILL.md`
- `keyword-data-export` (SealSeek, default-workspace-skills)：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-data-export/SKILL.md`
- `keyword-traffic` (SealSeek, default-workspace-skills)：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/keyword-traffic/SKILL.md`
- `market-analysis` (SealSeek, default-workspace-skills)：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-analysis/SKILL.md`
- `market-trend` (SealSeek, default-workspace-skills)：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/market-trend/SKILL.md`
- `product-grading` (SealSeek, default-workspace-skills)：通用电商产品分级与链接经营诊断。用于用户提供淘宝、天猫或其他电商平台的全店商品 Excel/CSV,要求"产品分级""商品分层""SABC分级""识别同类产品""同类链接对比""逐链接优化建议""付费/点击/转化诊断""责任岗位分配"或"整店产品规划"时。先动态识别任意类目的同类产品组,再做类内数据… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-grading/SKILL.md`
- `qa-merge-clean` (SealSeek, default-workspace-skills)：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输入多个 Excel 文件，自动合并后输出统一结果 3. 从文… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/qa-merge-clean/SKILL.md`
- `review-cleaning-assistant` (SealSeek, default-workspace-skills)：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“初评”下方，统一为“评价”列 3. 删除其他列，仅保留“评价… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/review-cleaning-assistant/SKILL.md`
- `search-term-blue-ocean-report` (SealSeek, default-workspace-skills)：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数据里找竞争不激烈但体量还可以的词”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/search-term-blue-ocean-report/SKILL.md`
- `生意参谋搜索词排行下载` (SealSeek, default-workspace-skills)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/sycm-search-rank-download/SKILL.md`
- `taobao-native` (SealSeek, default-workspace-skills)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, place orders, check orders, reque… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-native/SKILL.md`
- `taobao-profit-statement` (SealSeek, default-workspace-skills)：淘宝利润表自动生成 Skill。输入包含淘宝资金账单、映射表、聚合账户、保证金等 sheet 的 Excel 工作簿，自动生成“利润表”。适合“生成淘宝利润表”“财税表格处理”“用淘宝账单做利润表”“自动完成利润表”这类需求。生成时必须忽略手工“利润表”sheet，不能读取或复用手工利润表结果。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-profit-statement/SKILL.md`
- `taobao-search-parser` (SealSeek, default-workspace-skills)：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”“从压缩后的淘宝搜索页面里提取商品信息”这类需求。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-search-parser/SKILL.md`
- `work-browser` (SealSeek, default-workspace-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser/SKILL.md`
- `work-browser2` (SealSeek, default-workspace-skills)：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各自登录态，接管页面，小步浏览操作，输出适合继续交给模型或下游… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/work-browser2/SKILL.md`
- `xiaobai-category-insight` (SealSeek, default-workspace-skills)：老兵小白 AI智能体工具箱｜类目洞察助手。基于电商老兵小白V的类目洞察选品方法论，用于分析生意参谋「类目挖掘」成交金额/成交单量/需求供给比三张表，以及「类目洞察」价格分析和属性分析表，完成类目机会初筛、子类目价格带/属性下钻、机会分层、报告输出和下一步竞品验证交接。Use when the use… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/xiaobai-category-insight/SKILL.md`
- `guanshu-review` (SealSeek, migration-bundle)：观数浏览器扩展前端代码评审工具。对分支代码进行规范检查，生成评审报告。检查项：P0-颜色硬编码、内联样式、if嵌套、重复造轮子、Content Script挂载方式；P1-BEM命名、魔法数字、第三方库引入；P2-文件职责单一、长文件拆分。仅适用于 xc-sealseek-extension-syc… 位置：`/Users/pechen/hermes/xc-sealseek-aicoding-skill/fe-guanshu-review/SKILL.md`
- `生意参谋搜索词排行下载` (SealSeek, standalone-local)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋… 位置：`/Users/pechen/sealseek/RPA下载原型/SKILL.md`
- `taobao-market-analysis` (SealSeek, standalone-local)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 位置：`/Users/pechen/sealseek/backup/淘宝商品市场分析_20260418_210055/SKILL.md`
- `general-video` (SealSeek, standalone-local)：The fallback workflow for authoring custom HyperFrames video compositions at any length or format — longer or multi-scene pieces, brand / sizzle reels… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/general-video/SKILL.md`
- `货号跨店铺表现差异分析` (SealSeek, standalone-local)：🎯 任务目标 基于指定货号或全量数据，分析并识别同一货号在不同店铺/链接间销售表现差异显著的商品，帮助商家发现潜在的分销优化机会。 位置：`/Users/pechen/sealseek/货号跨店铺表现差异分析/SKILL.md`

### Agent 工程 / Skill / Plugin / MCP

- `ai-dianjing-growth-opportunity` (Codex, local)：Analyze an Alibaba Wanxiangtai AI点睛 keyword-promotion plan from a one.alimama.com plan link. Use when the user wants a past-7-day AI点睛 plan diagnosis,… 位置：`/Users/pechen/.codex/skills/ai-dianjing-growth-opportunity/SKILL.md`
- `goal-driven-video-qa` (Codex, local)：Inspect a video against quality goals inferred from the current conversation, explicit user request, prompt, script, storyboard, reference media, prio… 位置：`/Users/pechen/.codex/skills/goal-driven-video-qa/SKILL.md`
- `internal-plugin-workflow` (Codex, local)：Use when the user wants to build or iterate an internal Chrome browser extension against a page they have already opened, especially when the work inc… 位置：`/Users/pechen/.codex/skills/internal-plugin-workflow/SKILL.md`
- `joinquant-strategy` (Codex, local)：Write, review, debug, and validate JoinQuant/JQData 聚宽 quantitative trading strategy scripts that will be copied into the JoinQuant backtest or simula… 位置：`/Users/pechen/.codex/skills/joinquant-strategy/SKILL.md`
- `jqcli` (Codex, local)：Use when Codex needs to operate or maintain the jqcli JoinQuant project: authenticate, inspect strategies, list or run backtests, archive community po… 位置：`/Users/pechen/.codex/skills/jqcli/SKILL.md`
- `mac-no-reboot-rescue` (Codex, local)：Diagnose and relieve recurring macOS slowdowns without rebooting. Use when the user says their Mac is slow, stuck, beachballing, high load, memory pre… 位置：`/Users/pechen/.codex/skills/mac-no-reboot-rescue/SKILL.md`
- `portable-skill-creator` (Codex, local)：Create, update, review, or test shareable Agent Skills without leaking author-machine information or binding the core workflow to one Agent. Use by de… 位置：`/Users/pechen/.codex/skills/portable-skill-creator/SKILL.md`
- `quant-local-research` (Codex, local)：Use when Peter asks to research, backtest, validate, optimize, compare, or port ETF/stock quantitative trading strategies using the local QuantTrading… 位置：`/Users/pechen/.codex/skills/quant-local-research/SKILL.md`
- `sealseek-chat-control` (Codex, local)：Control and inspect the user's running SealSeek/SealClaw conversations through the local `sealseek-chat` CLI. Use when Codex needs to create, attach t… 位置：`/Users/pechen/.codex/skills/sealseek-chat-control/SKILL.md`
- `sealseek-execution-auditor` (Codex, local)：Audit SealSeek conversation execution traces to reconstruct tool calls, retries, fallbacks, side effects, skipped validation, and false-success risks.… 位置：`/Users/pechen/.codex/skills/sealseek-execution-auditor/SKILL.md`
- `ths-rebalance-planner` (Codex, local)：Generate a rebalance plan for the currently selected Tonghuashun 同花顺 account from pasted JoinQuant/模拟策略 target holdings. Use when the user provides si… 位置：`/Users/pechen/.codex/skills/ths-rebalance-planner/SKILL.md`
- `wdt-inventory-replenishment` (Codex, local)：Run Wangdian ERP inventory replenishment monitoring with wdtcli, derive SKU warning thresholds from historical sales, generate a purchase report, and … 位置：`/Users/pechen/.codex/skills/wdt-inventory-replenishment/SKILL.md`
- `workctl` (Codex, local)：管理 Work Agent 平台能力。通过 `workctl schema` 发现动态产品和命令，再用结构化输出执行操作。 位置：`/Users/pechen/.codex/skills/workctl/SKILL.md`
- `lark-approval` (Hermes, local)：飞书审批：查询和处理审批待办/已办/实例，搜索可发起审批定义、查看定义详情并发起原生审批实例。当用户要处理审批任务、查看审批实例、搜索或发起审批时使用。审批待办不是飞书任务；非审批类待办走 lark-task。不负责创建审批定义；三方审批定义不走原生提单。 位置：`/Users/pechen/.hermes/skills/lark-approval/SKILL.md`
- `lark-attendance` (Hermes, local)：飞书考勤打卡：查询自己的考勤打卡记录 位置：`/Users/pechen/.hermes/skills/lark-attendance/SKILL.md`
- `lark-base` (Hermes, local)：飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、workflow、角色权限；遇到 Base/多维表格/bitable 或 /base/ 链接时使用。文件导入转 lark-drive，认证/授权转 lark-shared。 位置：`/Users/pechen/.hermes/skills/lark-base/SKILL.md`
- `lark-calendar` (Hermes, local)：飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走 lark-vc）、待办任务（走 lark-task）。 位置：`/Users/pechen/.hermes/skills/lark-calendar/SKILL.md`
- `lark-contact` (Hermes, local)：飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名。当用户提到某人姓名要下一步发消息 / 排日程,或拿到 open_id 想查具体信息时使用。不负责部门树遍历、按部门列员工、组织架构图,这类需求… 位置：`/Users/pechen/.hermes/skills/lark-contact/SKILL.md`
- `lark-mail` (Hermes, local)：飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for mail/email intent only. Do not use for docs/sh… 位置：`/Users/pechen/.hermes/skills/lark-mail/SKILL.md`
- `lark-markdown` (Hermes, local)：飞书 Markdown：查看、创建、上传、编辑和比较 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取、修改、局部 patch 或比较差异时使用。不负责将 Markdown 导入为飞书在线文档，也不负责文件搜索、权限、评论、移动、删除等云空间管理操作。 位置：`/Users/pechen/.hermes/skills/lark-markdown/SKILL.md`
- `lark-okr` (Hermes, local)：飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标、关键结果、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。不负责：待办任务管理（lark-task）、日程/会议安排（lark-calendar）、绩效评估 位置：`/Users/pechen/.hermes/skills/lark-okr/SKILL.md`
- `lark-openapi-explorer` (Hermes, local)：飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。 位置：`/Users/pechen/.hermes/skills/lark-openapi-explorer/SKILL.md`
- `lark-shared` (Hermes, local)：Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain permissions (--domain, including all/docs/drive), m… 位置：`/Users/pechen/.hermes/skills/lark-shared/SKILL.md`
- `lark-skill-maker` (Hermes, local)：创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。 位置：`/Users/pechen/.hermes/skills/lark-skill-maker/SKILL.md`
- `lark-task` (Hermes, local)：飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务进度、管理项目清单或给他人分配任务、为任务上传附件文件、注册… 位置：`/Users/pechen/.hermes/skills/lark-task/SKILL.md`
- `lark-vc` (Hermes, local)：飞书视频会议：搜索历史会议记录、查询会议纪要（总结/待办/章节/逐字稿）、查询参会人快照。当用户查询已结束的会议、获取会议产物（纪要/妙记）、查看参会人时使用；查询未来日程走 lark-calendar。不负责：Agent 真实入会/离会、会中实时事件（走 lark-vc-agent）。 位置：`/Users/pechen/.hermes/skills/lark-vc/SKILL.md`
- `lark-workflow-meeting-summary` (Hermes, local)：会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。 位置：`/Users/pechen/.hermes/skills/lark-workflow-meeting-summary/SKILL.md`
- `lark-workflow-standup-report` (Hermes, local)：日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。 位置：`/Users/pechen/.hermes/skills/lark-workflow-standup-report/SKILL.md`
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
- `1688-88syt` (SealSeek, default-workspace-skills)：线下B2B交易的得力帮手，一句话搞定全流程操作！无论您是卖家还是买家，只需一句指令，即可轻松完成电子合约（采购单/合同）创建、签署、确认收货、退款等核心操作，全面支持账号状态查询、实名认证、绑卡及交易，让每一步交易流程更清晰、更可控。通过智能化交互，实现交易流程数字化，提升协作效率，保障资金流转安全… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-88syt/SKILL.md`
- `customer-service-diagnosis` (SealSeek, default-workspace-skills)：客服聊天记录诊断工具。输入客服聊天截图或文档，输出客服话术问题诊断、消费者需求甄别分析、推荐话术评估、改善方案及示范回复。 触发：用户提到"客服诊断""聊天记录分析""话术诊断""客服话术""客服聊天""客服培训""客服质检""聊天记录点评""客服回复"或提供客服聊天截图/文档要求分析。 排除：纯售… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/customer-service-diagnosis/SKILL.md`
- `express-bill-reconciliation` (SealSeek, default-workspace-skills)：>- Reconcile express carrier bills against merchant-expected charges for e-commerce shipments. Use when the user provides or wants to process three da… 位置：`/Users/pechen/.sealseek/workspaces/default/skills/express-bill-reconciliation/SKILL.md`
- `express-weight-reconciliation` (SealSeek, default-workspace-skills)：Generate and format an Excel reconciliation report comparing express carrier billed weights against internally estimated shipment weights. Use when a … 位置：`/Users/pechen/.sealseek/workspaces/default/skills/express-weight-reconciliation/SKILL.md`
- `skill-forward-test` (SealSeek, default-workspace-skills)：用主对话 + 干净子 Agent 回归测试新建或优化后的 Skill。用于 Peter 要求测试、验证、回归测试、确认 skill 是否真实落盘、是否能在无当前对话上下文的新 Agent 中独立触发和执行时；尤其适用于创建/优化 Agent Skill 后防止上下文污染、假落盘、假通过。 位置：`/Users/pechen/.sealseek/workspaces/default/skills/skill-forward-test/SKILL.md`
- `hyperframes` (SealSeek, standalone-local)：READ THIS FIRST for any request to make, create, edit, animate, or render a video, animation, or motion graphic — a promo, explainer, captioned clip, … 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes/SKILL.md`
- `hyperframes-cli` (SealSeek, standalone-local)：HyperFrames CLI dev loop. Use when running npx hyperframes init, add, catalog, capture, lint, validate, inspect, layout, snapshot, preview, play, rend… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-cli/SKILL.md`
- `hyperframes-core` (SealSeek, standalone-local)：The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tr… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-core/SKILL.md`
- `hyperframes-media` (SealSeek, standalone-local)：Audio and media assets for HyperFrames compositions, produced by one shared audio engine (`scripts/audio.mjs`) — multi-provider TTS (HeyGen / ElevenLa… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-media/SKILL.md`
- `hyperframes-registry` (SealSeek, standalone-local)：Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiri… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-registry/SKILL.md`
- `pr-to-video` (SealSeek, standalone-local)：turn a GitHub pull request (a PR URL like github.com/<owner>/<repo>/pull/<N>, an <owner>/<repo>#<N> ref, or 'this PR' in a checked-out repo) into a co… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/pr-to-video/SKILL.md`
- `product-launch-video` (SealSeek, standalone-local)：turn a product or marketing URL, pasted script, or brief into a product launch video, including SaaS promos, feature reveals, app launches, company pr… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/product-launch-video/SKILL.md`
- `remotion-to-hyperframes` (SealSeek, standalone-local)：Port an existing Remotion (React) composition to HyperFrames HTML. Use ONLY when the user explicitly asks to port/convert/migrate/translate a Remotion… 位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/remotion-to-hyperframes/SKILL.md`

## Skill 详情

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

### `baoyu-article-illustrator`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-article-illustrator/SKILL.md`
- 功能检索描述：Article illustrations: type × style × palette consistency.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：baoyu-article-illustrator Article Illustrator Article illustrations: type × style × palette consistency. creative/baoyu-article-illustrator/SKILL.md local

### `baoyu-comic`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-comic/SKILL.md`
- 功能检索描述：Knowledge comics (知识漫画): educational, biography, tutorial.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：baoyu-comic Knowledge Comic Creator Knowledge comics (知识漫画): educational, biography, tutorial. creative/baoyu-comic/SKILL.md local

### `baoyu-infographic`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-infographic/SKILL.md`
- 功能检索描述：Infographics: 21 layouts x 21 styles (信息图, 可视化).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：baoyu-infographic Infographic Generator Infographics: 21 layouts x 21 styles (信息图, 可视化). creative/baoyu-infographic/SKILL.md local

### `ecommerce-image-skill-architecture`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/ecommerce-image-skill-architecture/SKILL.md`
- 功能检索描述：Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use when designing or refactoring agent skills for product-image analysis, route selection, prompt planning, and staged image generation.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-image-skill-architecture E-commerce Image Skill Architecture Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use when designing or refactoring agent skills for product-image analysis, route selection, prompt planning, and staged image generation. creative/ecommerce-image-skill-architecture/SKILL.md local

### `evolink-gpt-image-2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/evolink-gpt-image-2/SKILL.md`
- 功能检索描述：Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and test script locations.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：evolink-gpt-image-2 Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and test script locations. creative/evolink-gpt-image-2/SKILL.md local

### `gpt-image-2-12api`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/gpt-image-2-12api/SKILL.md`
- 功能检索描述：Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavior, reproducible probing, and known channel quirks.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：gpt-image-2-12api Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavior, reproducible probing, and known channel quirks. creative/gpt-image-2-12api/SKILL.md local

### `gpt生图`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/gpt生图/SKILL.md`
- 功能检索描述：Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, design, or produce any image, illustration, photo, artwork, diagram, infographic, logo, poster, or visual content. Also use when asked to edit, modify, restyle, or transform an existing image. GPT Image 2 is the primary and only generation model in this skill. Supports text-to-image, reference-image generation, local-reference upload, transparent PNG output, and multi-turn iteration. Outputs PNG files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：gpt生图 GPT Image 2 Generation Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, design, or produce any image, illustration, photo, artwork, diagram, infographic, logo, poster, or visual content. Also use when asked to edit, modify, restyle, or transform an existing image. GPT Image 2 is the primary and only generation model in this skill. Supports text-to-image, reference-image generation, local-reference upload, transparent PNG output, and multi-turn iteration. Outputs PNG files. creative/gpt生图/SKILL.md local

### `shopping-basket-visual-planning`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/shopping-basket-visual-planning/SKILL.md`
- 功能检索描述：Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the user needs to know what other products, brands, scenes, or content to study BEFORE visual collection, visual decomposition, or shooting planning.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：shopping-basket-visual-planning Shopping Basket Visual Reference Discovery Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the user needs to know what other products, brands, scenes, or content to study BEFORE visual collection, visual decomposition, or shooting planning. creative/shopping-basket-visual-planning/SKILL.md local

### `single-image-optimization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/single-image-optimization/SKILL.md`
- 功能检索描述：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：single-image-optimization Single Image Optimization Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page. creative/single-image-optimization/SKILL.md local

### `taobao-gpt-image-creative-main-image`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/taobao-gpt-image-creative-main-image/SKILL.md`
- 功能检索描述：Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably via post-processing to avoid AI text乱码.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-gpt-image-creative-main-image Add tag pills as needed... Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably via post-processing to avoid AI text乱码. creative/taobao-gpt-image-creative-main-image/SKILL.md local

### `toapis-gpt-image-2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/toapis-gpt-image-2/SKILL.md`
- 功能检索描述：Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working request formats, task polling, local-image upload flow, supported sizes/quality/background, and known limitations discovered by live testing.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：toapis-gpt-image-2 Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working request formats, task polling, local-image upload flow, supported sizes/quality/background, and known limitations discovered by live testing. creative/toapis-gpt-image-2/SKILL.md local

### `lark-approval`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-approval/SKILL.md`
- 功能检索描述：飞书审批：查询和处理审批待办/已办/实例，搜索可发起审批定义、查看定义详情并发起原生审批实例。当用户要处理审批任务、查看审批实例、搜索或发起审批时使用。审批待办不是飞书任务；非审批类待办走 lark-task。不负责创建审批定义；三方审批定义不走原生提单。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-approval 飞书审批：查询和处理审批待办/已办/实例，搜索可发起审批定义、查看定义详情并发起原生审批实例。当用户要处理审批任务、查看审批实例、搜索或发起审批时使用。审批待办不是飞书任务；非审批类待办走 lark-task。不负责创建审批定义；三方审批定义不走原生提单。 lark-approval/SKILL.md local

### `lark-attendance`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-attendance/SKILL.md`
- 功能检索描述：飞书考勤打卡：查询自己的考勤打卡记录
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-attendance attendance (v1) 飞书考勤打卡：查询自己的考勤打卡记录 lark-attendance/SKILL.md local

### `lark-base`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-base/SKILL.md`
- 功能检索描述：飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、workflow、角色权限；遇到 Base/多维表格/bitable 或 /base/ 链接时使用。文件导入转 lark-drive，认证/授权转 lark-shared。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-base base 飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、workflow、角色权限；遇到 Base/多维表格/bitable 或 /base/ 链接时使用。文件导入转 lark-drive，认证/授权转 lark-shared。 lark-base/SKILL.md local

### `lark-calendar`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-calendar/SKILL.md`
- 功能检索描述：飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走 lark-vc）、待办任务（走 lark-task）。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：lark-calendar calendar (v4) 飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走 lark-vc）、待办任务（走 lark-task）。 lark-calendar/SKILL.md local

### `lark-contact`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-contact/SKILL.md`
- 功能检索描述：飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名。当用户提到某人姓名要下一步发消息 / 排日程,或拿到 open_id 想查具体信息时使用。不负责部门树遍历、按部门列员工、组织架构图,这类需求走原生 OpenAPI。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-contact 飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名。当用户提到某人姓名要下一步发消息 / 排日程,或拿到 open_id 想查具体信息时使用。不负责部门树遍历、按部门列员工、组织架构图,这类需求走原生 OpenAPI。 lark-contact/SKILL.md local

### `lark-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-doc/SKILL.md`
- 功能检索描述：飞书云文档（Docx / Wiki 文档）：读取和编辑飞书文档内容。当用户给出文档 URL 或 token，或需要查看、创建、编辑文档、插入或下载文档图片附件时使用。文档中嵌入的电子表格、多维表格、画板，先用本 skill 提取 token 再切到对应 skill。当用户给出 doubao.com 的 /docx/ 或 /wiki/ URL/token 时，也应直接使用本 skill；路由依据是 URL 路径模式和 token，而不是域名。不负责文档评论管理，也不负责表格或 Base 的数据操作。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：lark-doc docs 飞书云文档（Docx / Wiki 文档）：读取和编辑飞书文档内容。当用户给出文档 URL 或 token，或需要查看、创建、编辑文档、插入或下载文档图片附件时使用。文档中嵌入的电子表格、多维表格、画板，先用本 skill 提取 token 再切到对应 skill。当用户给出 doubao.com 的 /docx/ 或 /wiki/ URL/token 时，也应直接使用本 skill；路由依据是 URL 路径模式和 token，而不是域名。不负责文档评论管理，也不负责表格或 Base 的数据操作。 lark-doc/SKILL.md local

### `lark-drive`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-drive/SKILL.md`
- 功能检索描述：飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、评论/权限/订阅、标题、版本和本地文件导入。用户需要整理云盘目录、处理云空间资源 URL/token，或导入 Word/Markdown/Excel/CSV/PPTX/.base 为 docx/sheet/bitable/slides 时使用；doubao.com 云空间 URL/token 也按资源路径和 token 路由，不回退 WebFetch。不负责：文档内容编辑（走 lark-doc）、表格/Base 表内数据操作（走 lark-sheets/lark-base）、知识空间节点/成员管理（走 lark-wiki）、原生 Markdown 文件读写/patch/diff（走 lark-markdown）。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：lark-drive drive (v1) 飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、评论/权限/订阅、标题、版本和本地文件导入。用户需要整理云盘目录、处理云空间资源 URL/token，或导入 Word/Markdown/Excel/CSV/PPTX/.base 为 docx/sheet/bitable/slides 时使用；doubao.com 云空间 URL/token 也按资源路径和 token 路由，不回退 WebFetch。不负责：文档内容编辑（走 lark-doc）、表格/Base 表内数据操作（走 lark-sheets/lark-base）、知识空间节点/成员管理（走 lark-wiki）、原生 Markdown 文件读写/patch/diff（走 lark-markdown）。 lark-drive/SKILL.md local

### `lark-event`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-event/SKILL.md`
- 功能检索描述：Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <EventKey>` (covers IM messages/reactions/chat changes, Task updates, VC meeting started/joined/ended, Minutes generated, Whiteboard updated, etc.). Use for Lark bots, real-time message processing, long-running subscribers, streaming webhook/push handlers. Supports `--max-events` / `--timeout` bounded runs and a stderr ready-marker contract — designed for AI agents running as subprocesses.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：lark-event Lark Events Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via lark-cli event consume <EventKey> (covers IM messages/reactions/chat changes, Task updates, VC meeting started/joined/ended, Minutes generated, Whiteboard updated, etc.). Use for Lark bots, real-time message processing, long-running subscribers, streaming webhook/push handlers. Supports --max-events / --timeout bounded runs and a stderr ready-marker contract — designed for AI agents running as subprocesses. lark-event/SKILL.md local

### `lark-im`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-im/SKILL.md`
- 功能检索描述：飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive Card）、监听卡片按钮回调（card.action.trigger）。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、搜索群、创建群聊或话题群、管理标记数据、管理 Feed 置顶（添加/移除/查询置顶会话）、管理标签数据、处理卡片回调时使用。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-im im (v1) 飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive Card）、监听卡片按钮回调（card.action.trigger）。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、搜索群、创建群聊或话题群、管理标记数据、管理 Feed 置顶（添加/移除/查询置顶会话）、管理标签数据、处理卡片回调时使用。 lark-im/SKILL.md local

### `lark-mail`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-mail/SKILL.md`
- 功能检索描述：飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for mail/email intent only. Do not use for docs/sheets/calendar/auth setup/pure contact lookup/IM chat tasks.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-mail mail (v1) 飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for mail/email intent only. Do not use for docs/sheets/calendar/auth setup/pure contact lookup/IM chat tasks. lark-mail/SKILL.md local

### `lark-markdown`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-markdown/SKILL.md`
- 功能检索描述：飞书 Markdown：查看、创建、上传、编辑和比较 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取、修改、局部 patch 或比较差异时使用。不负责将 Markdown 导入为飞书在线文档，也不负责文件搜索、权限、评论、移动、删除等云空间管理操作。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-markdown markdown (v1) 飞书 Markdown：查看、创建、上传、编辑和比较 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取、修改、局部 patch 或比较差异时使用。不负责将 Markdown 导入为飞书在线文档，也不负责文件搜索、权限、评论、移动、删除等云空间管理操作。 lark-markdown/SKILL.md local

### `lark-minutes`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-minutes/SKILL.md`
- 功能检索描述：飞书妙记：搜索妙记、查看妙记基础信息、下载/上传音视频、读取或编辑妙记的产物内容、改标题、替换说话人/关键词。当给出minute_token、本地音视频文件，要查/改/转妙记产物时使用；本地音视频转纪要/逐字稿优先走本 skill，不要用 ffmpeg/whisper 本地转写。不负责：获取会议关联妙记，或仅按自然语言标题定位纪要
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：lark-minutes minutes (v1) 飞书妙记：搜索妙记、查看妙记基础信息、下载/上传音视频、读取或编辑妙记的产物内容、改标题、替换说话人/关键词。当给出minute_token、本地音视频文件，要查/改/转妙记产物时使用；本地音视频转纪要/逐字稿优先走本 skill，不要用 ffmpeg/whisper 本地转写。不负责：获取会议关联妙记，或仅按自然语言标题定位纪要 lark-minutes/SKILL.md local

### `lark-okr`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-okr/SKILL.md`
- 功能检索描述：飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标、关键结果、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。不负责：待办任务管理（lark-task）、日程/会议安排（lark-calendar）、绩效评估
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-okr okr (v2) 飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标、关键结果、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。不负责：待办任务管理（lark-task）、日程/会议安排（lark-calendar）、绩效评估 lark-okr/SKILL.md local

### `lark-openapi-explorer`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-openapi-explorer/SKILL.md`
- 功能检索描述：飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-openapi-explorer OpenAPI Explorer 飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。 lark-openapi-explorer/SKILL.md local

### `lark-shared`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-shared/SKILL.md`
- 功能检索描述：Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain permissions (--domain, including all/docs/drive), missing scopes, revoking authorization, or handling _notice JSON.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-shared lark-cli 共享规则 Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain permissions (--domain, including all/docs/drive), missing scopes, revoking authorization, or handling _notice JSON. lark-shared/SKILL.md local

### `lark-sheets`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-sheets/SKILL.md`
- 功能检索描述：飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表、条件格式、筛选器、迷你图、浮动图片等对象的创建与维护。当用户需要创建电子表格、管理工作表、批量读写或编辑数据、统计汇总与可视化、表格美化、公式计算（含 Excel 公式迁移）、金融/财务建模（DCF、三张表、预算、Sensitivity 等）等任务时使用。若用户是想按名称或关键词搜索云空间（云盘/云存储）里的表格文件，请改用 lark-drive 的 drive +search 先定位资源。当用户给出 doubao.com 的 /sheets/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-sheets sheets 飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表、条件格式、筛选器、迷你图、浮动图片等对象的创建与维护。当用户需要创建电子表格、管理工作表、批量读写或编辑数据、统计汇总与可视化、表格美化、公式计算（含 Excel 公式迁移）、金融/财务建模（DCF、三张表、预算、Sensitivity 等）等任务时使用。若用户是想按名称或关键词搜索云空间（云盘/云存储）里的表格文件，请改用 lark-drive 的 drive +search 先定位资源。当用户给出 doubao.com 的 /sheets/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。 lark-sheets/SKILL.md local

### `lark-skill-maker`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-skill-maker/SKILL.md`
- 功能检索描述：创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-skill-maker Skill Maker 创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。 lark-skill-maker/SKILL.md local

### `lark-slides`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-slides/SKILL.md`
- 功能检索描述：飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。不负责：云文档内容编辑（走 lark-doc）、云文档里的独立画板对象（走 lark-whiteboard，注意 slide 内嵌的流程图/架构图仍属本 skill）、上传或下载普通文件（走 lark-drive）。
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-slides slides (v1) 飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。不负责：云文档内容编辑（走 lark-doc）、云文档里的独立画板对象（走 lark-whiteboard，注意 slide 内嵌的流程图/架构图仍属本 skill）、上传或下载普通文件（走 lark-drive）。 lark-slides/SKILL.md local

### `lark-task`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-task/SKILL.md`
- 功能检索描述：飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务进度、管理项目清单或给他人分配任务、为任务上传附件文件、注册注销任务智能体、更新智能体主页数据、写入任务记录时使用。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-task task (v2) 飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务进度、管理项目清单或给他人分配任务、为任务上传附件文件、注册注销任务智能体、更新智能体主页数据、写入任务记录时使用。 lark-task/SKILL.md local

### `lark-vc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-vc/SKILL.md`
- 功能检索描述：飞书视频会议：搜索历史会议记录、查询会议纪要（总结/待办/章节/逐字稿）、查询参会人快照。当用户查询已结束的会议、获取会议产物（纪要/妙记）、查看参会人时使用；查询未来日程走 lark-calendar。不负责：Agent 真实入会/离会、会中实时事件（走 lark-vc-agent）。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：lark-vc vc (v1) 飞书视频会议：搜索历史会议记录、查询会议纪要（总结/待办/章节/逐字稿）、查询参会人快照。当用户查询已结束的会议、获取会议产物（纪要/妙记）、查看参会人时使用；查询未来日程走 lark-calendar。不负责：Agent 真实入会/离会、会中实时事件（走 lark-vc-agent）。 lark-vc/SKILL.md local

### `lark-whiteboard`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-whiteboard/SKILL.md`
- 功能检索描述：飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此 skill。不负责：飞书云文档内容编辑（lark-doc）、文档内嵌电子表格/Base（lark-sheets / lark-base）。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-whiteboard 飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此 skill。不负责：飞书云文档内容编辑（lark-doc）、文档内嵌电子表格/Base（lark-sheets / lark-base）。 lark-whiteboard/SKILL.md local

### `lark-wiki`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-wiki/SKILL.md`
- 功能检索描述：飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出 doubao.com 的 /wiki/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。不负责：上传文件到知识库节点下（走 lark-drive）、编辑文档/表格/Base 内容（走 lark-doc / lark-sheets / lark-base）。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-wiki wiki (v2) 飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出 doubao.com 的 /wiki/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。不负责：上传文件到知识库节点下（走 lark-drive）、编辑文档/表格/Base 内容（走 lark-doc / lark-sheets / lark-base）。 lark-wiki/SKILL.md local

### `lark-workflow-meeting-summary`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-workflow-meeting-summary/SKILL.md`
- 功能检索描述：会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-workflow-meeting-summary 会议纪要汇总工作流 会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。 lark-workflow-meeting-summary/SKILL.md local

### `lark-workflow-standup-report`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/lark-workflow-standup-report/SKILL.md`
- 功能检索描述：日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：lark-workflow-standup-report 日程待办摘要工作流 日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。 lark-workflow-standup-report/SKILL.md local

### `conference-static-html-courseware-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/conference-static-html-courseware-review-loop/SKILL.md`
- 功能检索描述：Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review, Git-backed iteration, and explicit review standards instead of ad-hoc CSS tweaking.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：conference-static-html-courseware-review-loop 大会版静态 HTML 课件重建与审阅闭环 Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review, Git-backed iteration, and explicit review standards instead of ad-hoc CSS tweaking. productivity/conference-static-html-courseware-review-loop/SKILL.md local

### `course-html-ppt-16x9-image-pages`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/course-html-ppt-16x9-image-pages/SKILL.md`
- 功能检索描述：Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy slide layouts.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：course-html-ppt-16x9-image-pages Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy slide layouts. productivity/course-html-ppt-16x9-image-pages/SKILL.md local

### `douyin-link-to-knowledge`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/douyin-link-to-knowledge/SKILL.md`
- 功能检索描述：Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transcribing/validating content, and reconstructing durable knowledge pages. Trigger on natural-language requests like “帮我把这个抖音内容整理到知识库”.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：douyin-link-to-knowledge Douyin Link to Knowledge Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transcribing/validating content, and reconstructing durable knowledge pages. Trigger on natural-language requests like “帮我把这个抖音内容整理到知识库”. productivity/douyin-link-to-knowledge/SKILL.md local

### `dual-source-chapterized-html-ppt-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/dual-source-chapterized-html-ppt-courseware/SKILL.md`
- 功能检索描述：Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to avoid renumbering cascades.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：dual-source-chapterized-html-ppt-courseware Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to avoid renumbering cascades. productivity/dual-source-chapterized-html-ppt-courseware/SKILL.md local

### `ecommerce-bi-operation-skill-planning`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/ecommerce-bi-operation-skill-planning/SKILL.md`
- 功能检索描述：Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡检 SOPs, priority engines, or product-level diagnostic skills for Taobao/e-commerce operations.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-bi-operation-skill-planning E-commerce BI Operation Skill Planning Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡检 SOPs, priority engines, or product-level diagnostic skills for Taobao/e-commerce operations. productivity/ecommerce-bi-operation-skill-planning/SKILL.md local

### `feishu-cli-isolated-config`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/feishu-cli-isolated-config/SKILL.md`
- 功能检索描述：Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentials; use an isolated config file via FEISHU_CONFIG because the CLI's built-in account support is incomplete.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：feishu-cli-isolated-config Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentials; use an isolated config file via FEISHU_CONFIG because the CLI's built-in account support is incomplete. productivity/feishu-cli-isolated-config/SKILL.md local

### `feishu-product-feature-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/feishu-product-feature-doc/SKILL.md`
- 功能检索描述：Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-oriented copy, callouts, comparison tables, and embedded images via official lark-cli.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：feishu-product-feature-doc 玺承BI特色功能介绍 Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-oriented copy, callouts, comparison tables, and embedded images via official lark-cli. productivity/feishu-product-feature-doc/SKILL.md local

### `goal-driven-daily-report-templates`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/goal-driven-daily-report-templates/SKILL.md`
- 功能检索描述：Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use when Peter asks to design job-specific daily/weekly report templates or examples for e-commerce, operations, design, video,客服,外贸,亚马逊等岗位.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：goal-driven-daily-report-templates Goal-Driven Daily Report Templates Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use when Peter asks to design job-specific daily/weekly report templates or examples for e-commerce, operations, design, video,客服,外贸,亚马逊等岗位. productivity/goal-driven-daily-report-templates/SKILL.md local

### `hermes-feishu-gateway-setup`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-gateway-setup/SKILL.md`
- 功能检索描述：Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credentials; use isolated FEISHU_CONFIG for CLI and FEISHU_* env vars plus platforms.feishu for Hermes gateway.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-feishu-gateway-setup Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credentials; use isolated FEISHU_CONFIG for CLI and FEISHU_* env vars plus platforms.feishu for Hermes gateway. productivity/hermes-feishu-gateway-setup/SKILL.md local

### `hermes-feishu-session-debugging`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-session-debugging/SKILL.md`
- 功能检索描述：Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session JSON files, and tool availability. Use when Feishu shows long-running “Still working...”, when a user says a message got no reply, or when uploaded image+text prompts seem to arrive incorrectly.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求
- 检索关键词：hermes-feishu-session-debugging Hermes Feishu Session Debugging Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session JSON files, and tool availability. Use when Feishu shows long-running “Still working...”, when a user says a message got no reply, or when uploaded image+text prompts seem to arrive incorrectly. productivity/hermes-feishu-session-debugging/SKILL.md local

### `html-ppt-conference-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-conference-review-loop/SKILL.md`
- 功能检索描述：Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with explicit readability and layout standards for large venue projection.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt-conference-review-loop HTML-PPT Conference Review Loop Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with explicit readability and layout standards for large venue projection. productivity/html-ppt-conference-review-loop/SKILL.md local

### `html-ppt-course-deck`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-course-deck/SKILL.md`
- 功能检索描述：Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid or visually weak. Use slides.json/slides.yaml for content, CSS for fixed templates, browser full-screen for presenting, and optional in-page editing/export. Especially useful when a mandated PPT template must be reproduced as fixed HTML backgrounds.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：html-ppt-course-deck HTML-PPT Course Deck Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid or visually weak. Use slides.json/slides.yaml for content, CSS for fixed templates, browser full-screen for presenting, and optional in-page editing/export. Especially useful when a mandated PPT template must be reproduced as fixed HTML backgrounds. productivity/html-ppt-course-deck/SKILL.md local

### `html-ppt-font-standardization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-font-standardization/SKILL.md`
- 功能检索描述：Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run an overflow audit after replacement.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：html-ppt-font-standardization HTML-PPT 字体规范方案 Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run an overflow audit after replacement. productivity/html-ppt-font-standardization/SKILL.md local

### `html-ppt-screenshot-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-screenshot-review-loop/SKILL.md`
- 功能检索描述：Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-style decks where readability, layout balance, and consistency matter more than code-level aesthetics.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt-screenshot-review-loop Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-style decks where readability, layout balance, and consistency matter more than code-level aesthetics. productivity/html-ppt-screenshot-review-loop/SKILL.md local

### `html-ppt-stage-fit-and-background-cleanup`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-stage-fit-and-background-cleanup/SKILL.md`
- 功能检索描述：Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds with clean backgrounds plus a separate sharp logo layer, and verify stage safety in browser.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：html-ppt-stage-fit-and-background-cleanup HTML-PPT 固定画布适配与背景去 Logo Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds with clean backgrounds plus a separate sharp logo layer, and verify stage safety in browser. productivity/html-ppt-stage-fit-and-background-cleanup/SKILL.md local

### `html-ppt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-studio-agentskill/SKILL.md`
- 功能检索描述：HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by templates. Use when the user asks for a presentation, PPT, slides, keynote, deck, slideshow, "幻灯片", "演讲稿", "做一份 PPT", "做一份 slides", a reveal-style HTML deck, a 小红书 图文, or any kind of multi-slide pitch/report/sharing document that should look tasteful and be usable with keyboard navigation. Triggers include keywords like "presentation", "ppt", "slides", "deck", "keynote", "reveal", "slideshow", "幻灯片", "演讲稿", "分享稿", "小红书图文", "talk slides", "pitch deck", "tech sharing", "technical presentation".
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt html-ppt — HTML PPT Studio HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by templates. Use when the user asks for a presentation, PPT, slides, keynote, deck, slideshow, "幻灯片", "演讲稿", "做一份 PPT", "做一份 slides", a reveal-style HTML deck, a 小红书 图文, or any kind of multi-slide pitch/report/sharing document that should look tasteful and be usable with keyboard navigation. Triggers include keywords like "presentation", "ppt", "slides", "deck", "keynote", "reveal", "slideshow", "幻灯片", "演讲稿", "分享稿", "小红书图文", "talk slides", "pitch deck", "tech sharing", "technical presentation". productivity/html-ppt-studio-agentskill/SKILL.md local

### `macos-wechat-cli`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-cli/SKILL.md`
- 功能检索描述：Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to install or troubleshoot a WeChat CLI on macOS.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：macos-wechat-cli macOS WeChat CLI Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to install or troubleshoot a WeChat CLI on macOS. productivity/macos-wechat-cli/SKILL.md local

### `macos-wechat-history-decrypt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-history-decrypt/SKILL.md`
- 功能检索描述：Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process existing WeChat chat history, list sessions/groups, search old messages, or export historical chats rather than monitor new messages.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：macos-wechat-history-decrypt macOS WeChat History Decryption Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process existing WeChat chat history, list sessions/groups, search old messages, or export historical chats rather than monitor new messages. productivity/macos-wechat-history-decrypt/SKILL.md local

### `official-lark-cli-feishu-workflows`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/official-lark-cli-feishu-workflows/SKILL.md`
- 功能检索描述：Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenClaw setup already uses ~/.lark-cli. Prefer this over third-party feishu-cli packages for stable bot/user identity handling and less confusing auth behavior.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：official-lark-cli-feishu-workflows Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenClaw setup already uses ~/.lark-cli. Prefer this over third-party feishu-cli packages for stable bot/user identity handling and less confusing auth behavior. productivity/official-lark-cli-feishu-workflows/SKILL.md local

### `real-chrome-web-reader`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/real-chrome-web-reader/SKILL.md`
- 功能检索描述：使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：real-chrome-web-reader 使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。 productivity/real-chrome-web-reader/SKILL.md local

### `reduce-paid-ratio-link-agent-mvp`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-link-agent-mvp/SKILL.md`
- 功能检索描述：Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for close, reduce, keep, or observe actions.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：reduce-paid-ratio-link-agent-mvp 单链接推广花费占比优化 Agent（MVP） Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for close, reduce, keep, or observe actions. productivity/reduce-paid-ratio-link-agent-mvp/SKILL.md local

### `reduce-paid-ratio-plan-evaluator`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-plan-evaluator/SKILL.md`
- 功能检索描述：Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from two source reports, then exporting a decision Excel.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：reduce-paid-ratio-plan-evaluator 降低店铺付费占比：推广计划关停评估 Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from two source reports, then exporting a decision Excel. productivity/reduce-paid-ratio-plan-evaluator/SKILL.md local

### `review-driven-static-html-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/review-driven-static-html-courseware/SKILL.md`
- 功能检索描述：Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML-native presentation instead of service-based editable HTML-PPT or PPT-first thinking.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：review-driven-static-html-courseware Review-driven static HTML courseware Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML-native presentation instead of service-based editable HTML-PPT or PPT-first thinking. productivity/review-driven-static-html-courseware/SKILL.md local

### `sealseek-feature-compare-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/sealseek-feature-compare-doc/SKILL.md`
- 功能检索描述：Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” document where each core module gets its own 3-column comparison table versus traditional tools.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-feature-compare-doc Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” document where each core module gets its own 3-column comparison table versus traditional tools. productivity/sealseek-feature-compare-doc/SKILL.md local

### `sealseek-static-html-courseware-workflow`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/sealseek-static-html-courseware-workflow/SKILL.md`
- 功能检索描述：Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server dependency, and conference-first readability rules.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-static-html-courseware-workflow Sealseek 静态 HTML 课件工作流 Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server dependency, and conference-first readability rules. productivity/sealseek-static-html-courseware-workflow/SKILL.md local

### `shopping-basket-visual-reference-discovery`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/shopping-basket-visual-reference-discovery/SKILL.md`
- 功能检索描述：docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual reference sources for an e-commerce product. Stops at “what should we look at for visual references”; does not produce shooting plans, design plans, copy, or image-generation prompts. ---
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：shopping-basket-visual-reference-discovery Shopping Basket Visual Reference Discovery docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual reference sources for an e-commerce product. Stops at “what should we look at for visual references”; does not produce shooting plans, design plans, copy, or image-generation prompts. --- productivity/shopping-basket-visual-reference-discovery/SKILL.md local

### `single-file-static-html-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/single-file-static-html-courseware/SKILL.md`
- 功能检索描述：Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live editable served HTML. Optimized for polished HTML delivery rather than PPT conversion.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：single-file-static-html-courseware Single-file Static HTML Courseware Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live editable served HTML. Optimized for polished HTML delivery rather than PPT conversion. productivity/single-file-static-html-courseware/SKILL.md local

### `static-html-courseware-feedback-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-feedback-loop/SKILL.md`
- 功能检索描述：Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review standards instead of code-only judgment.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-feedback-loop 静态 HTML 课件反馈闭环 Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review standards instead of code-only judgment. productivity/static-html-courseware-feedback-loop/SKILL.md local

### `static-html-courseware-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop/SKILL.md`
- 功能检索描述：Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of service-based editing.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-review-loop Static HTML 课件重建与审阅循环 Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of service-based editing. productivity/static-html-courseware-review-loop/SKILL.md local

### `static-html-courseware-review-loop-v2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop-v2/SKILL.md`
- 功能检索描述：Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimized for Sealseek-style dark-theme courseware, file:// review, large-font conference display, and screenshot-based QA instead of in-page editing.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：static-html-courseware-review-loop-v2 Static HTML Courseware Review Loop v2 Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimized for Sealseek-style dark-theme courseware, file:// review, large-font conference display, and screenshot-based QA instead of in-page editing. productivity/static-html-courseware-review-loop-v2/SKILL.md local

### `static-html-courseware-shared-assets-and-merge`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-shared-assets-and-merge/SKILL.md`
- 功能检索描述：Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapters into one final HTML without CSS collisions.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-shared-assets-and-merge When to use Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapters into one final HTML without CSS collisions. productivity/static-html-courseware-shared-assets-and-merge/SKILL.md local

### `static-html-deck-to-editable-ppt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-deck-to-editable-ppt/SKILL.md`
- 功能检索描述：Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into truly editable PowerPoint, instead of relying on served HTML decks or screenshot-only PPT export.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：static-html-deck-to-editable-ppt Static HTML Deck → Editable PPT workflow Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into truly editable PowerPoint, instead of relying on served HTML decks or screenshot-only PPT export. productivity/static-html-deck-to-editable-ppt/SKILL.md local

### `taobao-native-search-to-excel`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/taobao-native-search-to-excel/SKILL.md`
- 功能检索描述：使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-native-search-to-excel 使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 productivity/taobao-native-search-to-excel/SKILL.md local

### `taobao-search-to-excel`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/taobao-search-to-excel/SKILL.md`
- 功能检索描述：使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-search-to-excel 使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 productivity/taobao-search-to-excel/SKILL.md local

### `xicheng-bi-feishu-feature-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/xicheng-bi-feishu-feature-doc/SKILL.md`
- 功能检索描述：Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise sales-conversion-oriented but user-appropriate language, callouts, images, and whiteboard diagrams.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：xicheng-bi-feishu-feature-doc Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise sales-conversion-oriented but user-appropriate language, callouts, images, and whiteboard diagrams. productivity/xicheng-bi-feishu-feature-doc/SKILL.md local

### `llm-wiki`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/llm-wiki/SKILL.md`
- 功能检索描述：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki Karpathy's LLM Wiki Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency. research/llm-wiki/SKILL.md local

### `llm-wiki-audit-and-optimization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/llm-wiki-audit-and-optimization/SKILL.md`
- 功能检索描述：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit and Optimization Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base. research/llm-wiki-audit-and-optimization/SKILL.md local

### `cross-agent-skill-packaging`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/cross-agent-skill-packaging/SKILL.md`
- 功能检索描述：Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when publishing to git, syncing into Sealseek, or building a full test bundle with runtime credentials.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：cross-agent-skill-packaging Cross-Agent Skill Packaging Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when publishing to git, syncing into Sealseek, or building a full test bundle with runtime credentials. software-development/cross-agent-skill-packaging/SKILL.md local

### `sealseek-gpt-image-skill-migration`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/sealseek-gpt-image-skill-migration/SKILL.md`
- 功能检索描述：Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use when migrating image-generation capability from another skill (e.g. gemini-image), configuring Sealseek skill manifests, or debugging EvoLink async GPT Image 2 workflows.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-gpt-image-skill-migration Sealseek GPT 生图 Skill 迁移与维护 Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use when migrating image-generation capability from another skill (e.g. gemini-image), configuring Sealseek skill manifests, or debugging EvoLink async GPT Image 2 workflows. software-development/sealseek-gpt-image-skill-migration/SKILL.md local

### `sealseek-skill-sync-and-toolcall-fix`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中用户项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/sealseek-skill-sync-and-toolcall-fix/SKILL.md`
- 功能检索描述：Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-promotion bug in AgentScope.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-skill-sync-and-toolcall-fix Sealseek skill sync and tool-call fix Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-promotion bug in AgentScope. software-development/sealseek-skill-sync-and-toolcall-fix/SKILL.md local

### `1688-distribution`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/1688-distribution/SKILL.md`
- 功能检索描述：1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-distribution 1688 分销 1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。 1688-distribution/SKILL.md local

### `1688-marketing`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/1688-marketing/SKILL.md`
- 功能检索描述：1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、商机、市场机会、找商机、查商机，不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-marketing 1688-marketing-skill 1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、商机、市场机会、找商机、查商机，不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。 1688-marketing/SKILL.md local

### `1688-product-find`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/1688-product-find/SKILL.md`
- 功能检索描述：1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以图搜图、选品、批发、找货源、热销、比价、最便宜、按销量排序、出口、跨境、找供应商。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-product-find 1688-product-find (1688找商品Skill) 1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以图搜图、选品、批发、找货源、热销、比价、最便宜、按销量排序、出口、跨境、找供应商。 1688-product-find/SKILL.md local

### `1688-shopkeeper`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/1688-shopkeeper-official/SKILL.md`
- 功能检索描述：1688选品铺货 + 商机趋势专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥 (5) 查看即时商机热榜 (6) 查看类目/行业趋势与价格分布 (7) 生成店铺经营日报并输出主营商品选品建议。 触发词：帮我找商品、在1688搜、选品、铺货、上架、查店铺、配置AK、商机、热榜、排行榜、趋势、价格分布、经营日报、店铺日报、动销分析、经营分析、选品建议、1688找货。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-shopkeeper 1688-shopkeeper 1688选品铺货 + 商机趋势专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥 (5) 查看即时商机热榜 (6) 查看类目/行业趋势与价格分布 (7) 生成店铺经营日报并输出主营商品选品建议。 触发词：帮我找商品、在1688搜、选品、铺货、上架、查店铺、配置AK、商机、热榜、排行榜、趋势、价格分布、经营日报、店铺日报、动销分析、经营分析、选品建议、1688找货。 1688-shopkeeper-official/SKILL.md local

### `1688-source-suppliers`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/1688-source-suppliers/SKILL.md`
- 功能检索描述：1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发场景：找商品/选品 → 1688-product-find；比价/换供 → 1688-product-compare；下单付款 → 不处理。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-source-suppliers 1688-source-suppliers 1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发场景：找商品/选品 → 1688-product-find；比价/换供 → 1688-product-compare；下单付款 → 不处理。 1688-source-suppliers/SKILL.md local

### `1688-sourcing-inquiry`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/1688-sourcing-inquiry/SKILL.md`
- 功能检索描述：1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报价。 触发词：询盘、询价、寻源、采购咨询、发布采购需求、我有一批XX要采购谁能供货、求报价。 不触发场景：搜索浏览商品/选品/找同款/比价 → 1688-product-find；已选定具体商品要下单/支付/查订单 → 1688-order；找供应商/找工厂 → 1688-source-suppliers。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-sourcing-inquiry 1688 采购询盘寻源 1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报价。 触发词：询盘、询价、寻源、采购咨询、发布采购需求、我有一批XX要采购谁能供货、求报价。 不触发场景：搜索浏览商品/选品/找同款/比价 → 1688-product-find；已选定具体商品要下单/支付/查订单 → 1688-order；找供应商/找工厂 → 1688-source-suppliers。 1688-sourcing-inquiry/SKILL.md local

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

### `sealseek-canvas`

- Agent / 环境：OpenClaw
- 归属分类：个人/项目自定义
- 归属依据：OpenClaw workspace skill，按项目自定义能力处理。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.openclaw/workspace/skills/sealseek-canvas/SKILL.md`
- 功能检索描述：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or manage an 无限画板, generate/retrieve/place/arrange `gpt-image-2` images, generate/retrieve/place `seedance2-0` videos, add explanatory text, inspect supported parameters, download assets, or lay out labeled media tightly in blank board space. Prefer this CLI over browser clicking, Agent-mode generation, or ad hoc HTTP calls.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：sealseek-canvas SealSeek Infinite Canvas CLI Operate SealSeek Infinite Canvas through the browserless-capable sealseek-canvas CLI. Use when the user asks to authenticate, create or manage an 无限画板, generate/retrieve/place/arrange gpt-image-2 images, generate/retrieve/place seedance2-0 videos, add explanatory text, inspect supported parameters, download assets, or lay out labeled media tightly in blank board space. Prefer this CLI over browser clicking, Agent-mode generation, or ad hoc HTTP calls. sealseek-canvas/SKILL.md local

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

### `ai-agent-skill-registry-sync`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/AI Agent Skill Registry Sync/SKILL.md`
- 功能检索描述：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under $WIKI_ROOT. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ai-agent-skill-registry-sync AI Agent Skill Registry Sync Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under $WIKI_ROOT. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents. AI Agent Skill Registry Sync/SKILL.md workspace-skills

### `llm-wiki`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki/SKILL.md`
- 功能检索描述：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from their Wiki, wants to find existing knowledge, compare compiled pages, trace which Wiki pages or embedded image evidence support an answer, display a relevant stored screenshot or diagram, or make small explicit updates to indexes and query entry pages. Delegate new-source ingestion and all quality audit, optimization, repair, and recompilation work to the corresponding LLM Wiki skills.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：llm-wiki LLM Wiki Query And Routine Maintenance Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from their Wiki, wants to find existing knowledge, compare compiled pages, trace which Wiki pages or embedded image evidence support an answer, display a relevant stored screenshot or diagram, or make small explicit updates to indexes and query entry pages. Delegate new-source ingestion and all quality audit, optimization, repair, and recompilation work to the corresponding LLM Wiki skills. LLM Wiki/SKILL.md workspace-skills

### `llm-wiki-audit-and-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki Audit and Optimization/SKILL.md`
- 功能检索描述：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-readiness. Use when the user asks to check Wiki quality, verify a recent ingest, find why knowledge or embedded images cannot be found or delivered, diagnose a question-and-answer result, optimize or repair the Wiki, rebuild weak pages, fix routes or taxonomy, or recompile existing source material. By default, continue from audit findings into evidence-backed optimization and re-audit; remain read-only only when the user explicitly says not to modify files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit And Optimization Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-readiness. Use when the user asks to check Wiki quality, verify a recent ingest, find why knowledge or embedded images cannot be found or delivered, diagnose a question-and-answer result, optimize or repair the Wiki, rebuild weak pages, fix routes or taxonomy, or recompile existing source material. By default, continue from audit findings into evidence-backed optimization and re-audit; remain read-only only when the user explicitly says not to modify files. LLM Wiki Audit and Optimization/SKILL.md workspace-skills

### `llm-wiki-ingest`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/LLM Wiki Ingest/SKILL.md`
- 功能检索描述：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or dynamic webpages, Obsidian Clippings, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces memory-first classification, text and image evidence preservation, semantic image anchoring, lossless knowledge-unit coverage, formal pages, index/log updates, route audit, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or dynamic webpages, Obsidian Clippings, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces memory-first classification, text and image evidence preservation, semantic image anchoring, lossless knowledge-unit coverage, formal pages, index/log updates, route audit, and audit handoff. LLM Wiki Ingest/SKILL.md workspace-skills

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

### `sealseek-canvas`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspace/skills/sealseek-canvas/SKILL.md`
- 功能检索描述：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or manage an 无限画板, generate/retrieve/place/arrange `gpt-image-2` images, generate/retrieve/place `seedance2-0` videos, add explanatory text, inspect supported parameters, download assets, or lay out labeled media tightly in blank board space. Prefer this CLI over browser clicking, Agent-mode generation, or ad hoc HTTP calls.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：sealseek-canvas SealSeek Infinite Canvas CLI Operate SealSeek Infinite Canvas through the browserless-capable sealseek-canvas CLI. Use when the user asks to authenticate, create or manage an 无限画板, generate/retrieve/place/arrange gpt-image-2 images, generate/retrieve/place seedance2-0 videos, add explanatory text, inspect supported parameters, download assets, or lay out labeled media tightly in blank board space. Prefer this CLI over browser clicking, Agent-mode generation, or ad hoc HTTP calls. sealseek-canvas/SKILL.md workspace-skills

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

### `1688-88syt`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-88syt/SKILL.md`
- 功能检索描述：线下B2B交易的得力帮手，一句话搞定全流程操作！无论您是卖家还是买家，只需一句指令，即可轻松完成电子合约（采购单/合同）创建、签署、确认收货、退款等核心操作，全面支持账号状态查询、实名认证、绑卡及交易，让每一步交易流程更清晰、更可控。通过智能化交互，实现交易流程数字化，提升协作效率，保障资金流转安全，助力企业高效运营。专注每一次B2B交易，让生意更稳、更快、更省心！。用户提到 88 生意通、采购单、签署、退款、确认收货、大额、批量、实名、绑卡、主账号、卖家或买家问题时使用。
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：1688-88syt 88生意通-1688线下交易工具 线下B2B交易的得力帮手，一句话搞定全流程操作！无论您是卖家还是买家，只需一句指令，即可轻松完成电子合约（采购单/合同）创建、签署、确认收货、退款等核心操作，全面支持账号状态查询、实名认证、绑卡及交易，让每一步交易流程更清晰、更可控。通过智能化交互，实现交易流程数字化，提升协作效率，保障资金流转安全，助力企业高效运营。专注每一次B2B交易，让生意更稳、更快、更省心！。用户提到 88 生意通、采购单、签署、退款、确认收货、大额、批量、实名、绑卡、主账号、卖家或买家问题时使用。 1688-88syt/SKILL.md default-workspace-skills

### `1688-distribution`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-distribution/SKILL.md`
- 功能检索描述：1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-distribution 1688 分销 1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。 1688-distribution/SKILL.md default-workspace-skills

### `1688-marketing`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-marketing/SKILL.md`
- 功能检索描述：1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、商机、市场机会、找商机、查商机，不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-marketing 1688-marketing-skill 1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、商机、市场机会、找商机、查商机，不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。 1688-marketing/SKILL.md default-workspace-skills

### `1688-product-find`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-product-find/SKILL.md`
- 功能检索描述：1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以图搜图、选品、批发、找货源、热销、比价、最便宜、按销量排序、出口、跨境、找供应商。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-product-find 1688-product-find (1688找商品Skill) 1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以图搜图、选品、批发、找货源、热销、比价、最便宜、按销量排序、出口、跨境、找供应商。 1688-product-find/SKILL.md default-workspace-skills

### `1688-shopkeeper`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-shopkeeper/SKILL.md`
- 功能检索描述：1688选品铺货专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥。 触发词：帮我找商品、在1688搜、选品、铺货、上架、查店铺、配置AK、1688找货。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-shopkeeper 1688-shopkeeper 1688选品铺货专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥。 触发词：帮我找商品、在1688搜、选品、铺货、上架、查店铺、配置AK、1688找货。 1688-shopkeeper/SKILL.md default-workspace-skills

### `1688-source-suppliers`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-source-suppliers/SKILL.md`
- 功能检索描述：1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发场景：找商品/选品 → 1688-product-find；比价/换供 → 1688-product-compare；下单付款 → 不处理。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-source-suppliers 1688-source-suppliers 1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发场景：找商品/选品 → 1688-product-find；比价/换供 → 1688-product-compare；下单付款 → 不处理。 1688-source-suppliers/SKILL.md default-workspace-skills

### `1688-sourcing-inquiry`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/1688-sourcing-inquiry/SKILL.md`
- 功能检索描述：1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报价。 触发词：询盘、询价、寻源、采购咨询、发布采购需求、我有一批XX要采购谁能供货、求报价。 不触发场景：搜索浏览商品/选品/找同款/比价 → 1688-product-find；已选定具体商品要下单/支付/查订单 → 1688-order；找供应商/找工厂 → 1688-source-suppliers。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：1688-sourcing-inquiry 1688 采购询盘寻源 1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报价。 触发词：询盘、询价、寻源、采购咨询、发布采购需求、我有一批XX要采购谁能供货、求报价。 不触发场景：搜索浏览商品/选品/找同款/比价 → 1688-product-find；已选定具体商品要下单/支付/查订单 → 1688-order；找供应商/找工厂 → 1688-source-suppliers。 1688-sourcing-inquiry/SKILL.md default-workspace-skills

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

### `ai-agent-skill-registry-sync`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/ai-agent-skill-registry-sync.symlink-bak-20260610154600/SKILL.md`
- 功能检索描述：Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under $WIKI_ROOT. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ai-agent-skill-registry-sync AI Agent Skill Registry Sync Scan the user's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under $WIKI_ROOT. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents. ai-agent-skill-registry-sync.symlink-bak-20260610154600/SKILL.md default-workspace-skills

### `bge-title-creation`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/bge-title-creation/SKILL.md`
- 功能检索描述：宝工（bge宝工）品牌专用淘宝标题生成器。输入商品图片和搜索词表 Excel，输出 5 个 59~60 字符候选标题并生成 HTML 报告（制作方法、5个标题、并集覆盖统计、原搜索词表逐条标注）。触发：宝工标题、给宝工商品做标题、生成淘宝标题、根据搜索词表做标题、标题制作、做几个标题、标题生成报告。策略按实际商品和搜索词表动态判断，不限于除湿机。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：bge-title-creation 宝工标题制作（bge-title-creation） 宝工（bge宝工）品牌专用淘宝标题生成器。输入商品图片和搜索词表 Excel，输出 5 个 59~60 字符候选标题并生成 HTML 报告（制作方法、5个标题、并集覆盖统计、原搜索词表逐条标注）。触发：宝工标题、给宝工商品做标题、生成淘宝标题、根据搜索词表做标题、标题制作、做几个标题、标题生成报告。策略按实际商品和搜索词表动态判断，不限于除湿机。 bge-title-creation/SKILL.md default-workspace-skills

### `customer-service-diagnosis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/customer-service-diagnosis/SKILL.md`
- 功能检索描述：客服聊天记录诊断工具。输入客服聊天截图或文档，输出客服话术问题诊断、消费者需求甄别分析、推荐话术评估、改善方案及示范回复。 触发：用户提到"客服诊断""聊天记录分析""话术诊断""客服话术""客服聊天""客服培训""客服质检""聊天记录点评""客服回复"或提供客服聊天截图/文档要求分析。 排除：纯售后流程设计（用SOP类工具）、纯客服排班管理。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：customer-service-diagnosis 客服聊天记录诊断 客服聊天记录诊断工具。输入客服聊天截图或文档，输出客服话术问题诊断、消费者需求甄别分析、推荐话术评估、改善方案及示范回复。 触发：用户提到"客服诊断""聊天记录分析""话术诊断""客服话术""客服聊天""客服培训""客服质检""聊天记录点评""客服回复"或提供客服聊天截图/文档要求分析。 排除：纯售后流程设计（用SOP类工具）、纯客服排班管理。 customer-service-diagnosis/SKILL.md default-workspace-skills

### `damopan-product-ranking-selection`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/damopan-product-ranking-selection/SKILL.md`
- 功能检索描述：Analyze DMP/达摩盘 commodity ranking export tables and generate a product-selection HTML report. Use when the user provides a 达摩盘商品榜单/市场榜单导出表 and asks for选品分析、商品机会分层、S/A/B款判断、达摩盘榜单报告、或把达摩盘榜单转成选品库。This skill is intentionally scoped to 达摩盘商品榜单导出表, not arbitrary ranking tables from other platforms.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：damopan-product-ranking-selection 达摩盘商品榜单选品分析 Analyze DMP/达摩盘 commodity ranking export tables and generate a product-selection HTML report. Use when the user provides a 达摩盘商品榜单/市场榜单导出表 and asks for选品分析、商品机会分层、S/A/B款判断、达摩盘榜单报告、或把达摩盘榜单转成选品库。This skill is intentionally scoped to 达摩盘商品榜单导出表, not arbitrary ranking tables from other platforms. damopan-product-ranking-selection/SKILL.md default-workspace-skills

### `demand-research`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/demand-research/SKILL.md`
- 功能检索描述：Use when the user asks for 需求调研, consumer demand research, ecommerce product demand analysis, selling point planning, marketing visual planning, main image/detail page strategy, competitor visual teardown, link planning, launch planning, SKU/title/main-image planning, or a complete pre-launch product marketing action report from search terms, reviews, Q&A, market rankings, product links, images, or spreadsheets for any category.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：demand-research 需求调研 Use when the user asks for 需求调研, consumer demand research, ecommerce product demand analysis, selling point planning, marketing visual planning, main image/detail page strategy, competitor visual teardown, link planning, launch planning, SKU/title/main-image planning, or a complete pre-launch product marketing action report from search terms, reviews, Q&A, market rankings, product links, images, or spreadsheets for any category. demand-research/SKILL.md default-workspace-skills

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

### `dianshang-browser`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/dianshang-browser/SKILL.md`
- 功能检索描述：电商浏览器 Skill。固定端口 9223，修复 CDP 连接问题。 支持复用已运行的 Chrome 实例，或自动启动新实例。 与其他 agent 共享同一 Chrome 配置（~/.dianshang-chrome-profile）。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：dianshang-browser 1. 检查是否已运行 电商浏览器 Skill。固定端口 9223，修复 CDP 连接问题。 支持复用已运行的 Chrome 实例，或自动启动新实例。 与其他 agent 共享同一 Chrome 配置（~/.dianshang-chrome-profile）。 dianshang-browser/SKILL.md default-workspace-skills

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

### `douyin-category-trend-report`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/douyin-category-trend-report/SKILL.md`
- 功能检索描述：抖音类目榜单趋势产品 HTML 报告生成 Skill。输入观数/抖音商品榜单趋势分析 Excel（含“趋势分析”sheet 与 4 周商品榜单，字段如 当前排名、趋势、排名变化、商品名称、商品ID、价格带、店铺名称、排名(第1周~第4周)、支付买家数、访客数、商品图片链接、商品链接），自动识别趋势产品、趋势方向、上升/新上榜/下滑/跌出结构，并输出带图表、商品图片和可点击商品链接的 HTML 报告。适合“从抖音类目表找趋势产品”“商品榜单趋势分析生成报告”“把观数趋势分析表做成 HTML 报告”。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：douyin-category-trend-report 目标 抖音类目榜单趋势产品 HTML 报告生成 Skill。输入观数/抖音商品榜单趋势分析 Excel（含“趋势分析”sheet 与 4 周商品榜单，字段如 当前排名、趋势、排名变化、商品名称、商品ID、价格带、店铺名称、排名(第1周~第4周)、支付买家数、访客数、商品图片链接、商品链接），自动识别趋势产品、趋势方向、上升/新上榜/下滑/跌出结构，并输出带图表、商品图片和可点击商品链接的 HTML 报告。适合“从抖音类目表找趋势产品”“商品榜单趋势分析生成报告”“把观数趋势分析表做成 HTML 报告”。 douyin-category-trend-report/SKILL.md default-workspace-skills

### `ecommerce-gross-profit-reconciliation`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-gross-profit-reconciliation/SKILL.md`
- 功能检索描述：多格式电商财务口径毛利核算 Skill。用于用户提供支付宝/聚合支付/平台账单、淘宝/京东/拼多多/其他平台发货明细、货品成本表，要求“按财务到账口径计算毛利”“从账单反查货品和成本”“生成账单维度和产品维度毛利表”“做店铺收入-货物成本核算”时使用。支持一个 Excel 多 sheet 或多个 Excel/CSV 输入，先识别三类表：账单表、发货表、成本表，再以账单为准匹配发货和成本，输出格式化 Excel、异常清单和 QA。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-gross-profit-reconciliation 电商财务口径毛利核算 Skill 多格式电商财务口径毛利核算 Skill。用于用户提供支付宝/聚合支付/平台账单、淘宝/京东/拼多多/其他平台发货明细、货品成本表，要求“按财务到账口径计算毛利”“从账单反查货品和成本”“生成账单维度和产品维度毛利表”“做店铺收入-货物成本核算”时使用。支持一个 Excel 多 sheet 或多个 Excel/CSV 输入，先识别三类表：账单表、发货表、成本表，再以账单为准匹配发货和成本，输出格式化 Excel、异常清单和 QA。 ecommerce-gross-profit-reconciliation/SKILL.md default-workspace-skills

### `ecommerce-profit-reconciliation`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/ecommerce-profit-reconciliation/SKILL.md`
- 功能检索描述：电商资金利润闭合表生成 Skill。输入淘宝/天猫等电商平台下载的资金账单、聚合账户、保证金、推广账户等 Excel/CSV 数据，标准化流水、分类映射、按日核算收入费用与不影响利润项，输出带公式可复核的“按日核算的店铺资金利润闭合表”、规则说明、未识别流水和余额闭合校验。适合“生成电商利润核算表”“做资金利润闭合表”“根据平台账单核算每日利润”“复现老师利润表逻辑”这类任务。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-profit-reconciliation 电商资金利润闭合表生成 Skill（V1） 电商资金利润闭合表生成 Skill。输入淘宝/天猫等电商平台下载的资金账单、聚合账户、保证金、推广账户等 Excel/CSV 数据，标准化流水、分类映射、按日核算收入费用与不影响利润项，输出带公式可复核的“按日核算的店铺资金利润闭合表”、规则说明、未识别流水和余额闭合校验。适合“生成电商利润核算表”“做资金利润闭合表”“根据平台账单核算每日利润”“复现老师利润表逻辑”这类任务。 ecommerce-profit-reconciliation/SKILL.md default-workspace-skills

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

### `express-bill-reconciliation`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/express-bill-reconciliation/SKILL.md`
- 功能检索描述：>- Reconcile express carrier bills against merchant-expected charges for e-commerce shipments. Use when the user provides or wants to process three data types: carrier pricing/contract/rate card, carrier bill, and merchant order/shipment/weight data. The skill first validates all provided files and sheets, proposes a simple and explainable carrier charging rule based on pricing documents plus bill self-consistency checks, asks the user to confirm that rule, then reconciles weights and amounts and outputs a concise formatted Excel report with a dedicated pricing-assumption sheet marking overcharges, undercharges, unmatched waybills, weight anomalies, and unresolved rules.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：express-bill-reconciliation Express Bill Reconciliation >- Reconcile express carrier bills against merchant-expected charges for e-commerce shipments. Use when the user provides or wants to process three data types: carrier pricing/contract/rate card, carrier bill, and merchant order/shipment/weight data. The skill first validates all provided files and sheets, proposes a simple and explainable carrier charging rule based on pricing documents plus bill self-consistency checks, asks the user to confirm that rule, then reconciles weights and amounts and outputs a concise formatted Excel report with a dedicated pricing-assumption sheet marking overcharges, undercharges, unmatched waybills, weight anomalies, and unresolved rules. express-bill-reconciliation/SKILL.md default-workspace-skills

### `express-weight-reconciliation`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/express-weight-reconciliation/SKILL.md`
- 功能检索描述：Generate and format an Excel reconciliation report comparing express carrier billed weights against internally estimated shipment weights. Use when a workbook has sheets like「快递结算（输出）」with 运单号/重量,「发货数量」with 物流单号/货品编号/数量, and「发货单品重量指标」with 货品编号/重量(g), and the user wants to identify or highlight cases where the carrier over-counted weight.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：express-weight-reconciliation Express Weight Reconciliation Generate and format an Excel reconciliation report comparing express carrier billed weights against internally estimated shipment weights. Use when a workbook has sheets like「快递结算（输出）」with 运单号/重量,「发货数量」with 物流单号/货品编号/数量, and「发货单品重量指标」with 货品编号/重量(g), and the user wants to identify or highlight cases where the carrier over-counted weight. express-weight-reconciliation/SKILL.md default-workspace-skills

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

### `international-station-seller-assistant`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/international-station-seller-assistant/SKILL.md`
- 功能检索描述：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl CLI, including 店铺经营数据, 询盘, TM/IM conversations, 客服诊断, 广告, 商品, 发品, 选品, RFQ, 物流, 交易, 旺铺, or 国际站生意助手 workflows.
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：international-station-seller-assistant International Station Seller Assistant Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl CLI, including 店铺经营数据, 询盘, TM/IM conversations, 客服诊断, 广告, 商品, 发品, 选品, RFQ, 物流, 交易, 旺铺, or 国际站生意助手 workflows. international-station-seller-assistant/SKILL.md default-workspace-skills

### `jd-market-analysis`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/jd-market-analysis/SKILL.md`
- 功能检索描述：京东搜索市场分析，按关键词采集京东搜索结果并生成 XLSX 数据表与 HTML 分析报告。 触发：用户需要京东市场分析、京东商品数据抓取、京东关键词市场商品结构、价格/销量/品牌/店铺类型分布时使用。 也适用于：分析京东某个品类的竞争格局、品牌排名、价格带分布、标题关键词策略。 排除：京东商品详情页分析（用淘宝商品助手 Skill 的京东版本）；京东生意参谋数据（如有对应 Skill）。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：jd-market-analysis 京东搜索市场分析 京东搜索市场分析，按关键词采集京东搜索结果并生成 XLSX 数据表与 HTML 分析报告。 触发：用户需要京东市场分析、京东商品数据抓取、京东关键词市场商品结构、价格/销量/品牌/店铺类型分布时使用。 也适用于：分析京东某个品类的竞争格局、品牌排名、价格带分布、标题关键词策略。 排除：京东商品详情页分析（用淘宝商品助手 Skill 的京东版本）；京东生意参谋数据（如有对应 Skill）。 jd-market-analysis/SKILL.md default-workspace-skills

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

### `llm-wiki-audit-and-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-audit-and-optimization.symlink-bak-20260610154600/SKILL.md`
- 功能检索描述：Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-readiness. Use when the user asks to check Wiki quality, verify a recent ingest, find why knowledge or embedded images cannot be found or delivered, diagnose a question-and-answer result, optimize or repair the Wiki, rebuild weak pages, fix routes or taxonomy, or recompile existing source material. By default, continue from audit findings into evidence-backed optimization and re-audit; remain read-only only when the user explicitly says not to modify files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit And Optimization Audit and optimize an existing Markdown LLM Wiki for compilation depth, text and image evidence coverage, navigation and retrieval routes, and answer-readiness. Use when the user asks to check Wiki quality, verify a recent ingest, find why knowledge or embedded images cannot be found or delivered, diagnose a question-and-answer result, optimize or repair the Wiki, rebuild weak pages, fix routes or taxonomy, or recompile existing source material. By default, continue from audit findings into evidence-backed optimization and re-audit; remain read-only only when the user explicitly says not to modify files. llm-wiki-audit-and-optimization.symlink-bak-20260610154600/SKILL.md default-workspace-skills

### `llm-wiki-bootstrap`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-bootstrap/SKILL.md`
- 功能检索描述：Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set up an LLM Wiki from scratch, configure WIKI_ROOT and related environment variables, prepare Obsidian App and Obsidian CLI access, create the initial domains/index/schema/log structure, or verify that a local LLM Wiki environment is ready on macOS, Windows, or Linux.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki-bootstrap LLM Wiki Bootstrap Initialize a cross-platform LLM Wiki knowledge base for a new user or machine. Use when the user wants to create or set up an LLM Wiki from scratch, configure WIKI_ROOT and related environment variables, prepare Obsidian App and Obsidian CLI access, create the initial domains/index/schema/log structure, or verify that a local LLM Wiki environment is ready on macOS, Windows, or Linux. llm-wiki-bootstrap/SKILL.md default-workspace-skills

### `llm-wiki-ingest`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-ingest.symlink-bak-20260610154600/SKILL.md`
- 功能检索描述：Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or dynamic webpages, Obsidian Clippings, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces memory-first classification, text and image evidence preservation, semantic image anchoring, lossless knowledge-unit coverage, formal pages, index/log updates, route audit, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified and only LLM Wiki ingestion skill for the user's $WIKI_ROOT. Use for any source that should be compiled into the wiki, including image-rich or dynamic webpages, Obsidian Clippings, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces memory-first classification, text and image evidence preservation, semantic image anchoring, lossless knowledge-unit coverage, formal pages, index/log updates, route audit, and audit handoff. llm-wiki-ingest.symlink-bak-20260610154600/SKILL.md default-workspace-skills

### `llm-wiki-recompile-runner`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-recompile-runner/SKILL.md`
- 功能检索描述：Orchestrate repair and memory-first reorganization of existing LLM Wiki domains or learning/source packages that contain shell/thin pages, poor routing, over-compressed pages, or misplaced learning-path knowledge. Use after an audit finds placeholder pages, incomplete extraction notes, stale index status, raw transcripts that need to be recompiled, or source-shaped pages that should be fused into durable content-domain knowledge. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：llm-wiki-recompile-runner LLM Wiki Recompile Runner Orchestrate repair and memory-first reorganization of existing LLM Wiki domains or learning/source packages that contain shell/thin pages, poor routing, over-compressed pages, or misplaced learning-path knowledge. Use after an audit finds placeholder pages, incomplete extraction notes, stale index status, raw transcripts that need to be recompiled, or source-shaped pages that should be fused into durable content-domain knowledge. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality. llm-wiki-recompile-runner/SKILL.md default-workspace-skills

### `llm-wiki`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki.symlink-bak-20260610154600/SKILL.md`
- 功能检索描述：Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from their Wiki, wants to find existing knowledge, compare compiled pages, trace which Wiki pages or embedded image evidence support an answer, display a relevant stored screenshot or diagram, or make small explicit updates to indexes and query entry pages. Delegate new-source ingestion and all quality audit, optimization, repair, and recompilation work to the corresponding LLM Wiki skills.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：llm-wiki LLM Wiki Query And Routine Maintenance Query and perform routine navigation maintenance on an existing Markdown LLM Wiki. Use when the user asks a question that should be answered from their Wiki, wants to find existing knowledge, compare compiled pages, trace which Wiki pages or embedded image evidence support an answer, display a relevant stored screenshot or diagram, or make small explicit updates to indexes and query entry pages. Delegate new-source ingestion and all quality audit, optimization, repair, and recompilation work to the corresponding LLM Wiki skills. llm-wiki.symlink-bak-20260610154600/SKILL.md default-workspace-skills

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

### `new-product-launch`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/new-product-launch/SKILL.md`
- 功能检索描述：淘宝新品上架前全套准备。输入商品ID，自动完成：产品分析、竞品价格带、主图策略、详情页结构、标题关键词。串联淘宝商品助手、市场分析、关键词助手，输出可直接执行的上架方案。触发：用户说"新品上架""上架准备""帮我准备上架""新品分析"。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：new-product-launch 淘宝新品上架准备 Skill 淘宝新品上架前全套准备。输入商品ID，自动完成：产品分析、竞品价格带、主图策略、详情页结构、标题关键词。串联淘宝商品助手、市场分析、关键词助手，输出可直接执行的上架方案。触发：用户说"新品上架""上架准备""帮我准备上架""新品分析"。 new-product-launch/SKILL.md default-workspace-skills

### `product-grading`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-grading/SKILL.md`
- 功能检索描述：通用电商产品分级与链接经营诊断。用于用户提供淘宝、天猫或其他电商平台的全店商品 Excel/CSV,要求"产品分级""商品分层""SABC分级""识别同类产品""同类链接对比""逐链接优化建议""付费/点击/转化诊断""责任岗位分配"或"整店产品规划"时。先动态识别任意类目的同类产品组,再做类内数据对标,输出 S/A/B/C、逐链接问题与动作、运营/助理/总监/设计/产品/客服责任路由和整店30/60/90天规划;不得把不同品类直接横向比较。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：product-grading 产品分级 通用电商产品分级与链接经营诊断。用于用户提供淘宝、天猫或其他电商平台的全店商品 Excel/CSV,要求"产品分级""商品分层""SABC分级""识别同类产品""同类链接对比""逐链接优化建议""付费/点击/转化诊断""责任岗位分配"或"整店产品规划"时。先动态识别任意类目的同类产品组,再做类内数据对标,输出 S/A/B/C、逐链接问题与动作、运营/助理/总监/设计/产品/客服责任路由和整店30/60/90天规划;不得把不同品类直接横向比较。 product-grading/SKILL.md default-workspace-skills

### `product-page-seedance-video`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-page-seedance-video/SKILL.md`
- 功能检索描述：Build a structured product-page visual asset library from full ecommerce product page images, classify and tag main images/SKU images/detail images, create product identity board, storyboard, director board, style reference plan, Seedance prompt, and generate or dry-run a fixed 15s 9:16 product short video through seedancecli. Use when the user provides product page image tables, image URLs, product photos, Taobao/Tmall/JD/PDD detail assets, or asks to turn product page materials into a Seedance ecommerce video.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；音视频链接/文件、转录稿、会议纪要或内容处理需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：product-page-seedance-video Product Page Seedance Video Build a structured product-page visual asset library from full ecommerce product page images, classify and tag main images/SKU images/detail images, create product identity board, storyboard, director board, style reference plan, Seedance prompt, and generate or dry-run a fixed 15s 9:16 product short video through seedancecli. Use when the user provides product page image tables, image URLs, product photos, Taobao/Tmall/JD/PDD detail assets, or asks to turn product page materials into a Seedance ecommerce video. product-page-seedance-video/SKILL.md default-workspace-skills

### `product-selling-points-extractor`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/product-selling-points-extractor/SKILL.md`
- 功能检索描述：商品卖点提炼助手。从商品图片（直接上传、本地路径、网络URL、文本文件中提取的路径）中客观描述商品外观，提炼3-5个核心卖点，区分事实与推测，生成包含图片和卖点文字的HTML报告。Use for 商品卖点提炼, 卖点提取, 商品图片分析, 卖点报告, selling points extraction, product image analysis, 看图提炼卖点, 商品卖点, 核心卖点。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：product-selling-points-extractor 商品卖点提炼助手 商品卖点提炼助手。从商品图片（直接上传、本地路径、网络URL、文本文件中提取的路径）中客观描述商品外观，提炼3-5个核心卖点，区分事实与推测，生成包含图片和卖点文字的HTML报告。Use for 商品卖点提炼, 卖点提取, 商品图片分析, 卖点报告, selling points extraction, product image analysis, 看图提炼卖点, 商品卖点, 核心卖点。 product-selling-points-extractor/SKILL.md default-workspace-skills

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

### `report-docx-formatter`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/report-docx-formatter/SKILL.md`
- 功能检索描述：报告文档格式化与内容优化工具。将输入内容（Word/PDF/XMind/Excel或用户文本）进行内容扩写与优化，然后按照玺承经营复盘报告的视觉规范直接生成Word文档。 分两阶段执行： 1. 内容扩写与优化 → 输出结构化JSON 2. 直接生成Word文档 → Node.js + docx直接生成，跳过Markdown中间格式 触发词：格式化报告、生成复盘报告、按玺承格式输出、排版Word文档、美化报告格式、report formatter、格式化word
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：report-docx-formatter 报告Word文档格式化输出与内容优化 报告文档格式化与内容优化工具。将输入内容（Word/PDF/XMind/Excel或用户文本）进行内容扩写与优化，然后按照玺承经营复盘报告的视觉规范直接生成Word文档。 分两阶段执行： 1. 内容扩写与优化 → 输出结构化JSON 2. 直接生成Word文档 → Node.js + docx直接生成，跳过Markdown中间格式 触发词：格式化报告、生成复盘报告、按玺承格式输出、排版Word文档、美化报告格式、report formatter、格式化word report-docx-formatter/SKILL.md default-workspace-skills

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

### `sealseek-skill-creator`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/sealseek-skill-creator/SKILL.md`
- 功能检索描述：SealSeek Skill 创建器——创建、更新、审查、测试一般 SealSeek Skill 的增强层。 触发：创建/新建/做一个 Skill、更新/修改/优化 Skill、审查/检查/测试 Skill、帮我写一个 Skill、 这个 Skill 怎么改、帮我做一个 skill、写 skill.md、打包 Skill、分享 Skill 给其他人。 每次先动态读取当前系统 skill-creator，再叠加 Wiki-Skill-SOP、跨电脑分享、中文注册和干净回归方法。 不得复制、改名、覆盖或写死系统 creator。
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-skill-creator SealSeek Skill 创建器 SealSeek Skill 创建器——创建、更新、审查、测试一般 SealSeek Skill 的增强层。 触发：创建/新建/做一个 Skill、更新/修改/优化 Skill、审查/检查/测试 Skill、帮我写一个 Skill、 这个 Skill 怎么改、帮我做一个 skill、写 skill.md、打包 Skill、分享 Skill 给其他人。 每次先动态读取当前系统 skill-creator，再叠加 Wiki-Skill-SOP、跨电脑分享、中文注册和干净回归方法。 不得复制、改名、覆盖或写死系统 creator。 sealseek-skill-creator/SKILL.md default-workspace-skills

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

### `seedance-commerce-video`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/seedance-commerce-video/SKILL.md`
- 功能检索描述：Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selling points, target audience, price, brand assets, or competitor references into Douyin/Taobao/Kuaishou/Xiaohongshu commercial videos, Seedance all-purpose reference prompts, shot plans, API request payloads, or batch ad variants.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：seedance-commerce-video Seedance Commerce Video Build product-image-based ecommerce video ads and main-image videos with Seedance 2.0. Use when the user wants to turn product photos, selling points, target audience, price, brand assets, or competitor references into Douyin/Taobao/Kuaishou/Xiaohongshu commercial videos, Seedance all-purpose reference prompts, shot plans, API request payloads, or batch ad variants. seedance-commerce-video/SKILL.md default-workspace-skills

### `seedance-video`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/seedance-video/SKILL.md`
- 功能检索描述：Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedance 2.0 through the system-level `seedancecli` CLI and Volcengine Ark. Trigger for text-to-video, image/video/audio reference-to-video, first-frame or first-last-frame video, video editing, video extension, Ark video task polling, and Seedance payload dry-runs.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：seedance-video Seedance Video Use when an Agent needs to generate, edit, extend, query, wait for, download, validate, or batch-plan videos with Seedance 2.0 through the system-level seedancecli CLI and Volcengine Ark. Trigger for text-to-video, image/video/audio reference-to-video, first-frame or first-last-frame video, video editing, video extension, Ark video task polling, and Seedance payload dry-runs. seedance-video/SKILL.md default-workspace-skills

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

### `skill-forward-test`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/skill-forward-test/SKILL.md`
- 功能检索描述：用主对话 + 干净子 Agent 回归测试新建或优化后的 Skill。用于 Peter 要求测试、验证、回归测试、确认 skill 是否真实落盘、是否能在无当前对话上下文的新 Agent 中独立触发和执行时；尤其适用于创建/优化 Agent Skill 后防止上下文污染、假落盘、假通过。
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：skill-forward-test Skill Forward Test 用主对话 + 干净子 Agent 回归测试新建或优化后的 Skill。用于 Peter 要求测试、验证、回归测试、确认 skill 是否真实落盘、是否能在无当前对话上下文的新 Agent 中独立触发和执行时；尤其适用于创建/优化 Agent Skill 后防止上下文污染、假落盘、假通过。 skill-forward-test/SKILL.md default-workspace-skills

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

### `taobao-profit-statement`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/taobao-profit-statement/SKILL.md`
- 功能检索描述：淘宝利润表自动生成 Skill。输入包含淘宝资金账单、映射表、聚合账户、保证金等 sheet 的 Excel 工作簿，自动生成“利润表”。适合“生成淘宝利润表”“财税表格处理”“用淘宝账单做利润表”“自动完成利润表”这类需求。生成时必须忽略手工“利润表”sheet，不能读取或复用手工利润表结果。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-profit-statement 淘宝利润表自动生成 淘宝利润表自动生成 Skill。输入包含淘宝资金账单、映射表、聚合账户、保证金等 sheet 的 Excel 工作簿，自动生成“利润表”。适合“生成淘宝利润表”“财税表格处理”“用淘宝账单做利润表”“自动完成利润表”这类需求。生成时必须忽略手工“利润表”sheet，不能读取或复用手工利润表结果。 taobao-profit-statement/SKILL.md default-workspace-skills

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

### `xiaobai-category-insight`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/xiaobai-category-insight/SKILL.md`
- 功能检索描述：老兵小白 AI智能体工具箱｜类目洞察助手。基于电商老兵小白V的类目洞察选品方法论，用于分析生意参谋「类目挖掘」成交金额/成交单量/需求供给比三张表，以及「类目洞察」价格分析和属性分析表，完成类目机会初筛、子类目价格带/属性下钻、机会分层、报告输出和下一步竞品验证交接。Use when the user uploads business advisor category mining or category insight Excel files, asks for 类目洞察, 类目机会, 子类目下钻, 价格带分析, 属性分析, category insight, market category screening, subcategory analysis.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：xiaobai-category-insight 老兵小白 AI智能体工具箱｜类目洞察助手 v1.3-private 老兵小白 AI智能体工具箱｜类目洞察助手。基于电商老兵小白V的类目洞察选品方法论，用于分析生意参谋「类目挖掘」成交金额/成交单量/需求供给比三张表，以及「类目洞察」价格分析和属性分析表，完成类目机会初筛、子类目价格带/属性下钻、机会分层、报告输出和下一步竞品验证交接。Use when the user uploads business advisor category mining or category insight Excel files, asks for 类目洞察, 类目机会, 子类目下钻, 价格带分析, 属性分析, category insight, market category screening, subcategory analysis. xiaobai-category-insight/SKILL.md default-workspace-skills

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

### `llm-wiki`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki/SKILL.md`
- 功能检索描述：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki Karpathy's LLM Wiki Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency. LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki/SKILL.md standalone-local

### `llm-wiki-audit-and-optimization`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-audit-and-optimization/SKILL.md`
- 功能检索描述：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit and Optimization Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base. LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-audit-and-optimization/SKILL.md standalone-local

### `llm-wiki-ingest`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-ingest/SKILL.md`
- 功能检索描述：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal pages, index/log updates, Obsidian route audit, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal pages, index/log updates, Obsidian route audit, and audit handoff. LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-ingest/SKILL.md standalone-local

### `llm-wiki-recompile-runner`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-recompile-runner/SKILL.md`
- 功能检索描述：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：llm-wiki-recompile-runner LLM Wiki Recompile Runner Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality. LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-recompile-runner/SKILL.md standalone-local

### `生意参谋搜索词排行下载`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/sealseek/RPA下载原型/SKILL.md`
- 功能检索描述：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋排行榜链接”这类需求。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：生意参谋搜索词排行下载 生意参谋搜索词排行下载 输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹窗 适合“帮我下载这个搜索词排行榜数据”“跑一下这个生意参谋排行榜链接”这类需求。 RPA下载原型/SKILL.md standalone-local

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

### `embedded-captions`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/embedded-captions/SKILL.md`
- 功能检索描述：Add captions to a talking-head video. ONE catalog (CATALOG.md) of 32 visual identities behind two engines: column-flow (captions composited INTO the scene — matte occlusion + mix-blend; cream/ink/editorial/keynote/documentary/loud/neon/glitch/chrome/velocity) and themed constitutions (anchor/ordnance/terminal/neonsign/stardust/stomp/scoreboard/transit/vhs/arcade/dossier/laser/thunder/hologram/biolume/aurora/spectrum/papercut/popup/chalkboard/graffiti/brush/inkwater/ransom/lastpage/nightcity — e.g. a glyph-decode climax, a neon sign WRITTEN stroke by stroke, or the quiet `anchor` rail default). Route by identity, never by mode. Trigger on "captions/subtitles", "embed/cinematic captions", "VFX captions", "炸/特效/酷…
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：embedded-captions Embedded Captions Add captions to a talking-head video. ONE catalog (CATALOG.md) of 32 visual identities behind two engines: column-flow (captions composited INTO the scene — matte occlusion + mix-blend; cream/ink/editorial/keynote/documentary/loud/neon/glitch/chrome/velocity) and themed constitutions (anchor/ordnance/terminal/neonsign/stardust/stomp/scoreboard/transit/vhs/arcade/dossier/laser/thunder/hologram/biolume/aurora/spectrum/papercut/popup/chalkboard/graffiti/brush/inkwater/ransom/lastpage/nightcity — e.g. a glyph-decode climax, a neon sign WRITTEN stroke by stroke, or the quiet anchor rail default). Route by identity, never by mode. Trigger on "captions/subtitles", "embed/cinematic captions", "VFX captions", "炸/特效/酷… github项目-hyperframes/hyperframes/skills/embedded-captions/SKILL.md standalone-local

### `faceless-explainer`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/faceless-explainer/SKILL.md`
- 功能检索描述：turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video, up to ~3 min (sweet spot 30-90s), where every visual is invented (typography, abstract graphics, diagrams, data-viz) rather than captured. There is no URL, no website capture, and no real assets. Use this skill for topic explainers, concept breakdowns, how-tos, listicles, and narrative explainers. Do not use it for a product launch/promo (use /product-launch-video), a tour of a real website (use /website-to-video), a GitHub PR (use /pr-to-video), captions on existing footage (use /embedded-captions), or a short unnarrated motion graphic (use /motion-graphics). If the intent is unclear, route through /hyperframes first.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：faceless-explainer Faceless Explainer to HyperFrames turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video, up to ~3 min (sweet spot 30-90s), where every visual is invented (typography, abstract graphics, diagrams, data-viz) rather than captured. There is no URL, no website capture, and no real assets. Use this skill for topic explainers, concept breakdowns, how-tos, listicles, and narrative explainers. Do not use it for a product launch/promo (use /product-launch-video), a tour of a real website (use /website-to-video), a GitHub PR (use /pr-to-video), captions on existing footage (use /embedded-captions), or a short unnarrated motion graphic (use /motion-graphics). If the intent is unclear, route through /hyperframes first. github项目-hyperframes/hyperframes/skills/faceless-explainer/SKILL.md standalone-local

### `general-video`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/general-video/SKILL.md`
- 功能检索描述：The fallback workflow for authoring custom HyperFrames video compositions at any length or format — longer or multi-scene pieces, brand / sizzle reels, montages, title cards, static loops, and freeform compositions. Input- and length-agnostic. If a specialized workflow clearly fits the input — a marketed product, a website, a topic explainer, a GitHub PR, existing footage, a short motion graphic, or a Remotion port — prefer it (see /hyperframes); use this only as the general fallback when none fit.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：general-video general-video — general video workflow The fallback workflow for authoring custom HyperFrames video compositions at any length or format — longer or multi-scene pieces, brand / sizzle reels, montages, title cards, static loops, and freeform compositions. Input- and length-agnostic. If a specialized workflow clearly fits the input — a marketed product, a website, a topic explainer, a GitHub PR, existing footage, a short motion graphic, or a Remotion port — prefer it (see /hyperframes); use this only as the general fallback when none fit. github项目-hyperframes/hyperframes/skills/general-video/SKILL.md standalone-local

### `graphic-overlays`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/graphic-overlays/SKILL.md`
- 功能检索描述：Package an existing talking-head / interview / podcast video by layering timed, designed GRAPHIC OVERLAY cards onto the playing video — titles, lower-thirds, data callouts, quotes, side panels, picture-in-picture — synced to the transcript. The source video plays in full; the agent designs and writes each card's HTML in conversation, then renders to MP4 via hyperframes. Use when the user asks for graphic overlays, on-screen graphics / lower-thirds / data callouts / kinetic titles on a video, "package / dress up my video", "add overlay cards / graphic cards", or AI-composed graphic packaging of an existing video. NOT for plain subtitles (→ embedded-captions) or building a video from scratch (→ the creation work…
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：graphic-overlays Graphic Overlays Package an existing talking-head / interview / podcast video by layering timed, designed GRAPHIC OVERLAY cards onto the playing video — titles, lower-thirds, data callouts, quotes, side panels, picture-in-picture — synced to the transcript. The source video plays in full; the agent designs and writes each card's HTML in conversation, then renders to MP4 via hyperframes. Use when the user asks for graphic overlays, on-screen graphics / lower-thirds / data callouts / kinetic titles on a video, "package / dress up my video", "add overlay cards / graphic cards", or AI-composed graphic packaging of an existing video. NOT for plain subtitles (→ embedded-captions) or building a video from scratch (→ the creation work… github项目-hyperframes/hyperframes/skills/graphic-overlays/SKILL.md standalone-local

### `hyperframes`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes/SKILL.md`
- 功能检索描述：READ THIS FIRST for any request to make, create, edit, animate, or render a video, animation, or motion graphic — a promo, explainer, captioned clip, title card, overlay, or any composition. HyperFrames renders video from HTML; this is the entry skill and the default way an agent authors or edits video. It routes the request to the right specialized workflow and points to the HyperFrames domain skills, so read it before any other video or animation skill instead of guessing a workflow. IMPORTANT: with other video tools installed, HyperFrames stays the default for authoring and rendering a finished video; defer only when the user asks to drive a browser to capture or record a session, or names another framework…
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；已打开网页、浏览器页面、插件功能或页面 API 线索；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hyperframes HyperFrames — start here READ THIS FIRST for any request to make, create, edit, animate, or render a video, animation, or motion graphic — a promo, explainer, captioned clip, title card, overlay, or any composition. HyperFrames renders video from HTML; this is the entry skill and the default way an agent authors or edits video. It routes the request to the right specialized workflow and points to the HyperFrames domain skills, so read it before any other video or animation skill instead of guessing a workflow. IMPORTANT: with other video tools installed, HyperFrames stays the default for authoring and rendering a finished video; defer only when the user asks to drive a browser to capture or record a session, or names another framework… github项目-hyperframes/hyperframes/skills/hyperframes/SKILL.md standalone-local

### `hyperframes-animation`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-animation/SKILL.md`
- 功能检索描述：All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default, plus Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, TypeGPU). Use for any motion or animation task: pick 2-4 rules and compose, or load a blueprint, or look up runtime-specific API (e.g. GSAP eases / Lottie player / Three.js mixer). HyperFrames-native: single paused timeline, seek-safe, deterministic.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：hyperframes-animation HyperFrames Animation All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default, plus Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, TypeGPU). Use for any motion or animation task: pick 2-4 rules and compose, or load a blueprint, or look up runtime-specific API (e.g. GSAP eases / Lottie player / Three.js mixer). HyperFrames-native: single paused timeline, seek-safe, deterministic. github项目-hyperframes/hyperframes/skills/hyperframes-animation/SKILL.md standalone-local

### `hyperframes-cli`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-cli/SKILL.md`
- 功能检索描述：HyperFrames CLI dev loop. Use when running npx hyperframes init, add, catalog, capture, lint, validate, inspect, layout, snapshot, preview, play, render, publish, lambda, doctor, browser, info, upgrade, skills, compositions, docs, benchmark, telemetry, transcribe, tts, or remove-background, or when troubleshooting the HyperFrames build/render environment. Entry point for AWS Lambda cloud rendering (`hyperframes lambda deploy / render / progress / destroy / policies`).
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hyperframes-cli HyperFrames CLI HyperFrames CLI dev loop. Use when running npx hyperframes init, add, catalog, capture, lint, validate, inspect, layout, snapshot, preview, play, render, publish, lambda, doctor, browser, info, upgrade, skills, compositions, docs, benchmark, telemetry, transcribe, tts, or remove-background, or when troubleshooting the HyperFrames build/render environment. Entry point for AWS Lambda cloud rendering ( hyperframes lambda deploy / render / progress / destroy / policies ). github项目-hyperframes/hyperframes/skills/hyperframes-cli/SKILL.md standalone-local

### `hyperframes-core`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-core/SKILL.md`
- 功能检索描述：The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation. Read before writing composition HTML.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：hyperframes-core HyperFrames Core The HyperFrames composition contract — build one renderable project. Use for composition structure, the data-* timing attributes, class="clip" , tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation. Read before writing composition HTML. github项目-hyperframes/hyperframes/skills/hyperframes-core/SKILL.md standalone-local

### `hyperframes-creative`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-creative/SKILL.md`
- 功能检索描述：Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand / style decisions. For atomic motion patterns and scene blueprints, use `hyperframes-animation`.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：hyperframes-creative HyperFrames Creative Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand / style decisions. For atomic motion patterns and scene blueprints, use hyperframes-animation . github项目-hyperframes/hyperframes/skills/hyperframes-creative/SKILL.md standalone-local

### `hyperframes-media`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-media/SKILL.md`
- 功能检索描述：Audio and media assets for HyperFrames compositions, produced by one shared audio engine (`scripts/audio.mjs`) — multi-provider TTS (HeyGen / ElevenLabs / Kokoro local), background music + sound effects (HeyGen audio-library retrieval by default, with local Lyria / MusicGen BGM generation and a bundled SFX library as the no-credential fallback), Whisper transcription, background removal, and caption authoring. Use for voiceover / TTS, BGM, SFX / sound effects, transcription, captions / subtitles / lyrics / karaoke / per-word styling, voice + provider selection, and music-mood prompting.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：hyperframes-media HyperFrames Media Audio and media assets for HyperFrames compositions, produced by one shared audio engine ( scripts/audio.mjs ) — multi-provider TTS (HeyGen / ElevenLabs / Kokoro local), background music + sound effects (HeyGen audio-library retrieval by default, with local Lyria / MusicGen BGM generation and a bundled SFX library as the no-credential fallback), Whisper transcription, background removal, and caption authoring. Use for voiceover / TTS, BGM, SFX / sound effects, transcription, captions / subtitles / lyrics / karaoke / per-word styling, voice + provider selection, and music-mood prompting. github项目-hyperframes/hyperframes/skills/hyperframes-media/SKILL.md standalone-local

### `hyperframes-registry`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/hyperframes-registry/SKILL.md`
- 功能检索描述：Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into index.html, or working with hyperframes.json. Covers the add command, install locations, block sub-composition wiring, component snippet merging, registry discovery, and authoring a new block or component to contribute upstream (idea → scaffold → validate → PR).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：hyperframes-registry HyperFrames Registry Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into index.html, or working with hyperframes.json. Covers the add command, install locations, block sub-composition wiring, component snippet merging, registry discovery, and authoring a new block or component to contribute upstream (idea → scaffold → validate → PR). github项目-hyperframes/hyperframes/skills/hyperframes-registry/SKILL.md standalone-local

### `motion-graphics`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/motion-graphics/SKILL.md`
- 功能检索描述：Use when the user wants a short, design-led motion graphic where motion is the message: kinetic typography, stat or number count-up, chart/data-viz hit, logo sting, brand lockup, lower-third, callout, social overlay, animated headline/tweet/news item, motion poster, or quick captured-page highlight. Usually under 10s and up to ~30s, with no narration arc, voice-over, or live-action subject. Can render to MP4 or transparent overlay. Not for longer, multi-scene, narrated, or brand-reel pieces (use general-video), narrated website videos (website-to-video), topic explainers (faceless-explainer), product promos (product-launch-video), PR videos (pr-to-video), or captions on existing footage (embedded-captions). Wh…
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：motion-graphics motion-graphics — dispatch entry Use when the user wants a short, design-led motion graphic where motion is the message: kinetic typography, stat or number count-up, chart/data-viz hit, logo sting, brand lockup, lower-third, callout, social overlay, animated headline/tweet/news item, motion poster, or quick captured-page highlight. Usually under 10s and up to ~30s, with no narration arc, voice-over, or live-action subject. Can render to MP4 or transparent overlay. Not for longer, multi-scene, narrated, or brand-reel pieces (use general-video), narrated website videos (website-to-video), topic explainers (faceless-explainer), product promos (product-launch-video), PR videos (pr-to-video), or captions on existing footage (embedded-captions). Wh… github项目-hyperframes/hyperframes/skills/motion-graphics/SKILL.md standalone-local

### `music-to-video`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/music-to-video/SKILL.md`
- 功能检索描述：Use when the user has a music track (an audio file, or a video to pull audio from) and wants a beat-synced HyperFrames video, calm to hard-hitting. The music drives everything: one analyzer reads it once, the orchestrator lays out the frames and fills a per-frame plan, and one sub-agent builds each frame. Typography and templates are the floor — a complete video needs zero assets — but any images or videos the user supplies are cut into the frames on the same beat grid (beat-cut / ken-burns). The genre (lyric video, slideshow, kinetic promo) falls out of the per-frame choices; the pipeline never branches on it.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：music-to-video music-to-video — one music-grounded, beat-synced video workflow Use when the user has a music track (an audio file, or a video to pull audio from) and wants a beat-synced HyperFrames video, calm to hard-hitting. The music drives everything: one analyzer reads it once, the orchestrator lays out the frames and fills a per-frame plan, and one sub-agent builds each frame. Typography and templates are the floor — a complete video needs zero assets — but any images or videos the user supplies are cut into the frames on the same beat grid (beat-cut / ken-burns). The genre (lyric video, slideshow, kinetic promo) falls out of the per-frame choices; the pipeline never branches on it. github项目-hyperframes/hyperframes/skills/music-to-video/SKILL.md standalone-local

### `pr-to-video`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/pr-to-video/SKILL.md`
- 功能检索描述：turn a GitHub pull request (a PR URL like github.com/<owner>/<repo>/pull/<N>, an <owner>/<repo>#<N> ref, or 'this PR' in a checked-out repo) into a code-change explainer video, up to ~3 min (sweet spot 30-90s) — changelog, feature reveal, fix, or refactor walkthrough, rendered from the diff / commits / files. The input is a CODE CHANGE read via the gh CLI; there is no website capture. Use this skill for a GitHub PR. Do not use it for a product launch/promo (use /product-launch-video), a tour of a real website (use /website-to-video), a topic explainer with no PR (use /faceless-explainer), captions on existing footage (use /embedded-captions), or a short unnarrated motion graphic (use /motion-graphics). If the …
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：pr-to-video PR to HyperFrames turn a GitHub pull request (a PR URL like github.com/<owner>/<repo>/pull/<N>, an <owner>/<repo>#<N> ref, or 'this PR' in a checked-out repo) into a code-change explainer video, up to ~3 min (sweet spot 30-90s) — changelog, feature reveal, fix, or refactor walkthrough, rendered from the diff / commits / files. The input is a CODE CHANGE read via the gh CLI; there is no website capture. Use this skill for a GitHub PR. Do not use it for a product launch/promo (use /product-launch-video), a tour of a real website (use /website-to-video), a topic explainer with no PR (use /faceless-explainer), captions on existing footage (use /embedded-captions), or a short unnarrated motion graphic (use /motion-graphics). If the … github项目-hyperframes/hyperframes/skills/pr-to-video/SKILL.md standalone-local

### `product-launch-video`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/product-launch-video/SKILL.md`
- 功能检索描述：turn a product or marketing URL, pasted script, or brief into a product launch video, including SaaS promos, feature reveals, app launches, company promos, and product marketing videos. Use this skill when the user wants to market, launch, promote, or reveal a product. Do not use it for general non-launch website tours, non-product topic explainers, GitHub pull requests, captioning existing footage, or short unnarrated motion graphics. If the intent is unclear, route through /hyperframes first.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：product-launch-video Product Launch to HyperFrames turn a product or marketing URL, pasted script, or brief into a product launch video, including SaaS promos, feature reveals, app launches, company promos, and product marketing videos. Use this skill when the user wants to market, launch, promote, or reveal a product. Do not use it for general non-launch website tours, non-product topic explainers, GitHub pull requests, captioning existing footage, or short unnarrated motion graphics. If the intent is unclear, route through /hyperframes first. github项目-hyperframes/hyperframes/skills/product-launch-video/SKILL.md standalone-local

### `remotion-to-hyperframes`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/remotion-to-hyperframes/SKILL.md`
- 功能检索描述：Port an existing Remotion (React) composition to HyperFrames HTML. Use ONLY when the user explicitly asks to port/convert/migrate/translate a Remotion source. Do NOT use: (a) authoring a new HyperFrames composition; (b) Remotion mentioned in passing; (c) Remotion code shared as reference only; (d) "same video as my Remotion one" without explicit migrate request — treat as fresh build. Doubt → `/general-video`. One-way, Remotion-only: no reverse export (HyperFrames→Remotion or any framework), no non-Remotion source (After Effects, Framer Motion, plain React/CSS) → out of scope, re-create via `/general-video`. Flags unsupported patterns (useState, useEffect, async calculateMetadata, third-party React libs, `@rem…
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：remotion-to-hyperframes Remotion to HyperFrames Port an existing Remotion (React) composition to HyperFrames HTML. Use ONLY when the user explicitly asks to port/convert/migrate/translate a Remotion source. Do NOT use: (a) authoring a new HyperFrames composition; (b) Remotion mentioned in passing; (c) Remotion code shared as reference only; (d) "same video as my Remotion one" without explicit migrate request — treat as fresh build. Doubt → /general-video . One-way, Remotion-only: no reverse export (HyperFrames→Remotion or any framework), no non-Remotion source (After Effects, Framer Motion, plain React/CSS) → out of scope, re-create via /general-video . Flags unsupported patterns (useState, useEffect, async calculateMetadata, third-party React libs, @rem… github项目-hyperframes/hyperframes/skills/remotion-to-hyperframes/SKILL.md standalone-local

### `slideshow`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/slideshow/SKILL.md`
- 功能检索描述：Author a HyperFrames slideshow composition — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching sequences, and hotspot navigation. Use as an intent check when the user asks for a presentation, pitch deck, slide deck, interactive deck, or page-to-deck conversion that might be a slideshow; if the user did not explicitly ask for a slideshow / slide show, confirm before authoring.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：slideshow Slideshow authoring contract Author a HyperFrames slideshow composition — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching sequences, and hotspot navigation. Use as an intent check when the user asks for a presentation, pitch deck, slide deck, interactive deck, or page-to-deck conversion that might be a slideshow; if the user did not explicitly ask for a slideshow / slide show, confirm before authoring. github项目-hyperframes/hyperframes/skills/slideshow/SKILL.md standalone-local

### `website-to-video`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/sealseek/github项目-hyperframes/hyperframes/skills/website-to-video/SKILL.md`
- 功能检索描述：Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals). Uses headless Chrome screenshots + brand assets. Use when intent is general — portfolio/blog/landing-page showcase or social clip from the site. NOT for: product/SaaS launch or promo (→ /product-launch-video, even from a URL); topic explainer with no site (→ /faceless-explainer); GitHub PR (→ /pr-to-video); adding captions to existing video (→ /embedded-captions); short unnarrated page-highlight motion graphic (→ /motion-graphics). Unclear launch-vs-general-site? Ask one question or start at /hyperframes.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：website-to-video Website to HyperFrames Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals). Uses headless Chrome screenshots + brand assets. Use when intent is general — portfolio/blog/landing-page showcase or social clip from the site. NOT for: product/SaaS launch or promo (→ /product-launch-video, even from a URL); topic explainer with no site (→ /faceless-explainer); GitHub PR (→ /pr-to-video); adding captions to existing video (→ /embedded-captions); short unnarrated page-highlight motion graphic (→ /motion-graphics). Unclear launch-vs-general-site? Ask one question or start at /hyperframes. github项目-hyperframes/hyperframes/skills/website-to-video/SKILL.md standalone-local

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

