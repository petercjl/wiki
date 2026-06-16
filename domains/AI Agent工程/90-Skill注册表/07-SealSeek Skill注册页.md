---
title: SealSeek Skill 注册页
type: concept
created: 2026-06-14
updated: 2026-06-14
domain: AI Agent工程
tags: [ai-agent, sealseek, skill, registry]
sources:
  - /Users/pechen/.sealseek/skill_pool
  - /Users/pechen/.sealseek/workspace/skills
  - /Users/pechen/.sealseek/workspaces/default/skills
  - /Users/pechen/.sealseek/workspaces/default/active_skills
  - /Users/pechen/.sealseek/workspaces/default/customized_skills
  - /Users/pechen/.sealseek/backups
  - /Users/pechen/sealseek
  - /Users/pechen/hermes/xc-sealseek-aicoding-skill
status: active
---
# SealSeek Skill 注册页

本页记录 SealSeek 环境中的 skill，用于 AI Agent 检索“是否已有类似 skill”并定位原始 SKILL.md。

## 维护范围

来源目录：

- `/Users/pechen/.sealseek/skill_pool`
- `/Users/pechen/.sealseek/workspace/skills`
- `/Users/pechen/.sealseek/workspaces/default/skills`
- `/Users/pechen/.sealseek/workspaces/default/active_skills`
- `/Users/pechen/.sealseek/workspaces/default/customized_skills`
- `/Users/pechen/.sealseek/backups`
- `/Users/pechen/sealseek`
- `/Users/pechen/hermes/xc-sealseek-aicoding-skill`

- 说明：SealSeek multi-source skills: global skill_pool, workspace skills, default workspace, active/customized skills, local standalone skills, backups, and migration bundles.
- 当前记录数量：134

归属分类统计：

- 个人/项目自定义: 90
- 系统/内置: 12
- 运行时副本: 26
- 归档/备份: 6

SealSeek 来源类型统计：

- active-skills: 26
- backup: 6
- customized-skills: 6
- default-workspace-skills: 32
- global-skill-pool: 12
- migration-bundle: 7
- standalone-local: 8
- workspace-skills: 37

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 知识库 / 知识管理 / LLM Wiki

- `ai-agent-skill-registry-sync` (归档/备份 / backup)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, the…
- `llm-wiki` (归档/备份 / backup)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compil…
- `llm-wiki-audit-and-optimization` (归档/备份 / backup)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or w…
- `llm-wiki-ingest` (归档/备份 / backup)：Unified LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wik…
- `llm-wiki-recompile-runner` (归档/备份 / backup)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit find…
- `lark-cli-doc-reader` (个人/项目自定义 / workspace-skills)：使用用户本机 /opt/homebrew/bin/lark-cli 读取飞书云文档。适用于按文档标题/文件名搜索并读取飞书 Docx/Doc/Wiki，或用户给出飞书文档 URL/token 时读取内容。重点规避 OpenClaw/Seal…
- `ai-agent-skill-registry-sync` (个人/项目自定义 / default-workspace-skills)：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, the…
- `llm-wiki` (个人/项目自定义 / default-workspace-skills)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compil…
- `llm-wiki-audit-and-optimization` (个人/项目自定义 / default-workspace-skills)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or w…
- `llm-wiki-ingest` (个人/项目自定义 / default-workspace-skills)：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled int…
- `llm-wiki-recompile-runner` (个人/项目自定义 / default-workspace-skills)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit find…
- `outline-paper-builder` (个人/项目自定义 / migration-bundle)：Reconstruct complete teaching-grade knowledge from mm/xmind outlines and output reviewable artifacts: lecture notes, opt…
- `llm-wiki` (个人/项目自定义 / standalone-local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compil…
- `llm-wiki-audit-and-optimization` (个人/项目自定义 / standalone-local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or w…
- `llm-wiki-ingest` (个人/项目自定义 / standalone-local)：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled int…
- `llm-wiki-recompile-runner` (个人/项目自定义 / standalone-local)：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit find…

### 视觉 / 内容 / 课件生产

- `gpt生图` (归档/备份 / backup)：使用 EvoLink GPT Image 2 / gpt-image-2 进行文生图、图生图、图片优化、中文电商海报/主图文案排版优化。用户说“用gpt生图skill”“gpt生图”“GPT生图”“优化这张图和文案排版”“用GPT优化图片/…
- `file_reader` (系统/内置 / global-skill-pool)：Read and summarize text-based file types only. Prefer read_file for text formats; use execute_shell_command for type det…
- `pdf` (系统/内置 / global-skill-pool)：PDF 文件处理技能。只要用户提到 PDF、.pdf、PDF文件、读取PDF、提取PDF文字、提取PDF表格、合并PDF、拆分PDF、旋转PDF、生成PDF、填写PDF表单、导出PDF、扫描件OCR 等需求，就应使用本 skill。 Sup…
- `pptx` (系统/内置 / global-skill-pool)：Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide d…
- `detail-page-batch-optimization` (个人/项目自定义 / workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared prod…
- `docx` (个人/项目自定义 / workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers inclu…
- `ecommerce-visual-plan` (个人/项目自定义 / workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design…
- `gpt生图` (个人/项目自定义 / workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、…
- `image-understanding` (个人/项目自定义 / workspace-skills)：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。
- `search-term-relevance-scorer` (个人/项目自定义 / workspace-skills)：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 …
- `shop-product-diagnosis` (个人/项目自定义 / workspace-skills)：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action ma…
- `single-image-optimization` (个人/项目自定义 / workspace-skills)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/st…
- `taobao-item` (个人/项目自定义 / workspace-skills)：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查…
- `web-image-extractor` (个人/项目自定义 / workspace-skills)：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. *…
- `xmind-cli` (个人/项目自定义 / workspace-skills)：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。
- `成套视觉生成` (个人/项目自定义 / workspace-skills)：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 …
- `无限画板 Skill 生成器` (个人/项目自定义 / workspace-skills)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生…
- `淘宝商品助手` (个人/项目自定义 / workspace-skills)：淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/…
- `电商视觉全套生成` (个人/项目自定义 / workspace-skills)：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3…
- `docx` (运行时副本 / active-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers inclu…
- `file_reader` (运行时副本 / active-skills)：Read and summarize text-based file types only. Prefer read_file for text formats; use execute_shell_command for type det…
- `pdf` (运行时副本 / active-skills)：PDF 文件处理技能。只要用户提到 PDF、.pdf、PDF文件、读取PDF、提取PDF文字、提取PDF表格、合并PDF、拆分PDF、旋转PDF、生成PDF、填写PDF表单、导出PDF、扫描件OCR 等需求，就应使用本 skill。 Sup…
- `pptx` (运行时副本 / active-skills)：Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide d…
- `image-understanding` (运行时副本 / active-skills)：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。
- `淘宝商品助手` (运行时副本 / active-skills)：淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/…
- `image-understanding` (个人/项目自定义 / customized-skills)：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。
- `detail-page-batch-optimization` (个人/项目自定义 / default-workspace-skills)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared prod…
- `docx` (个人/项目自定义 / default-workspace-skills)：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers inclu…
- `成套视觉生成` (个人/项目自定义 / default-workspace-skills)：基于 ecommerce-visual-plan 输出的规划 Excel，选择某一套方案，读取生图衔接表与图片展开表， 生成该方案下全部图位的逐图 prompt、参考图映射、一致性约束与执行清单，并在用户确认后调用 GPT Image 2 …
- `ecommerce-visual-plan` (个人/项目自定义 / default-workspace-skills)：Analyze product signals and imagery, then output structured multi-route e-commerce visual planning for downstream design…
- `电商视觉全套生成` (个人/项目自定义 / default-workspace-skills)：电商视觉全套生成 skill。输入产品参考图，按三个模块依次规划并生成完整电商视觉： 模块一：5张主图（3:4，含情绪文案）； 模块二：1张SKU场景图（1:1，含产品名称与尺寸规格标注）+ 1张白底图（1:1）； 模块三：10张详情页（3…
- `gpt生图` (个人/项目自定义 / default-workspace-skills)：使用 GPT Image 2 / gpt-image-2 进行文生图、图生图、图片编辑、图片优化、中文电商海报/主图文案排版。触发：gpt生图、GPT生图、用GPT生成图片、生成图片、画一张、做一张图、修改图片、P图、优化这张图和文案排版、…
- `search-term-relevance-scorer` (个人/项目自定义 / default-workspace-skills)：搜索词相关度评分器 — 输入一个搜索词排行 Excel 和一个产品图片目录，由系统 Agent 按既定流程完成搜索词预扫描、图片观察任务清单生成、产品画像抽取、逐词相关度评分、结构化依据生成与自然语言解释，再由脚本负责输入整理与结果导出。 …
- `shop-product-diagnosis` (个人/项目自定义 / default-workspace-skills)：Diagnose an ecommerce shop from a 商品列表 Excel workbook and produce a consulting-style HTML report plus an XMind action ma…
- `single-image-optimization` (个人/项目自定义 / default-workspace-skills)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/st…
- `无限画板 Skill 生成器` (个人/项目自定义 / default-workspace-skills)：根据用户的生图、生视频、图像编辑、分镜、视觉工作流等自然语言需求，先理解需求并输出规划，待用户确认后，生成无限画板中可直接使用的唯一 skill.md 文件内容，并同步维护 skill.md 文件与 README.md 迭代记录。 触发：生…
- `taobao-item` (个人/项目自定义 / default-workspace-skills)：淘宝商品助手 — 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查…
- `web-image-extractor` (个人/项目自定义 / default-workspace-skills)：网页图片批量采集 Skill。输入网页链接，自动识别并下载页面中的图片。 核心特性： 1. 复用 work-browser 浏览器实例，自动处理登录态 2. 支持已知网站的专用解析器（高效） 3. 支持未知网站的自动探索（自适应） 4. *…
- `xmind-cli` (个人/项目自定义 / default-workspace-skills)：XMind 脑图输出助手 — 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。
- `detail-page-batch-optimization` (个人/项目自定义 / migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared prod…
- `detail-page-batch-optimization` (个人/项目自定义 / migration-bundle)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared prod…
- `gemini-image` (个人/项目自定义 / migration-bundle)：Generate, edit, and iterate on images using Gemini image models via 12API. Use when the user asks to create, generate, d…
- `single-image-optimization` (个人/项目自定义 / migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/st…
- `single-image-optimization` (个人/项目自定义 / migration-bundle)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/st…
- `xmind-cli` (个人/项目自定义 / standalone-local)：XMind 脑图输出助手 —— 把结构化内容或分析框架生成 .xmind 文件。 适合“帮我做成脑图”“输出成 XMind”“把这个方案整理成导图”“生成脑图文件”这类需求。 默认风格：向右展开、商务简洁、结构清晰。
- `商品成套视觉规划skill` (个人/项目自定义 / standalone-local)：把一个商品的多源证据（搜索词、评价、问大家、商品图）整理成**可执行的成套视觉规划**，输出给后续设计、生图、详情页优化或投放团队直接使用的规划结果。

### 电商 / 商品 / 品牌运营

- `keyword-assistant` (个人/项目自定义 / workspace-skills)：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词…
- `keyword-data-export` (个人/项目自定义 / workspace-skills)：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。
- `keyword-traffic` (个人/项目自定义 / workspace-skills)：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总…
- `market-analysis` (个人/项目自定义 / workspace-skills)：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- `market-trend` (个人/项目自定义 / workspace-skills)：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、…
- `qa-merge-clean` (个人/项目自定义 / workspace-skills)：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输…
- `review-cleaning-assistant` (个人/项目自定义 / workspace-skills)：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“…
- `search-term-blue-ocean-report` (个人/项目自定义 / workspace-skills)：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数…
- `taobao-market-analysis` (个人/项目自定义 / workspace-skills)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- `taobao-native` (个人/项目自定义 / workspace-skills)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, pla…
- `taobao-search-parser` (个人/项目自定义 / workspace-skills)：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”…
- `work-browser` (个人/项目自定义 / workspace-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 …
- `work-browser2` (个人/项目自定义 / workspace-skills)：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各…
- `关键词助手` (个人/项目自定义 / workspace-skills)：生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 …
- `关键词流量解析` (个人/项目自定义 / workspace-skills)：万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势…
- `商品静态四象限分析` (个人/项目自定义 / workspace-skills)：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根…
- `市场排行趋势` (个人/项目自定义 / workspace-skills)：生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量…
- `快递超重补差对账` (个人/项目自定义 / workspace-skills)：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北…
- `推广管理助手` (个人/项目自定义 / workspace-skills)：万相台无界版推广计划的自动化管理 Skill。通过 API 直接调用万相台后端，支持 P0+P1 全场景： - 货品全站推广（onebpSite）：选品 + 投产比 + 预算，一键创建 - 关键词推广（onebpSearch）：搜索卡位 /…
- `生意参谋搜索词排行下载` (个人/项目自定义 / workspace-skills)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹…
- `电商凭证管理` (个人/项目自定义 / workspace-skills)：多平台电商登录凭证管理。支持淘系(生意参谋/淘宝/1688)、抖音(抖店/千川)、拼多多、京东等平台。 全平台统一通过CDP交互式登录提取Cookie(绕过App-Bound Encryption)。自动检测有效性，失效自动刷新，兜底引导手…
- `电商凭证管理` (运行时副本 / active-skills)：多平台电商登录凭证管理。支持淘系(生意参谋/淘宝/1688)、抖音(抖店/千川)、拼多多、京东等平台。 全平台统一通过CDP交互式登录提取Cookie(绕过App-Bound Encryption)。自动检测有效性，失效自动刷新，兜底引导手…
- `关键词助手` (运行时副本 / active-skills)：生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 …
- `关键词流量解析` (运行时副本 / active-skills)：万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势…
- `商品静态四象限分析` (运行时副本 / active-skills)：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根…
- `work-browser` (运行时副本 / active-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 …
- `market-analysis` (运行时副本 / active-skills)：市场分析 skill。适合“帮我看看手机的趋势”“分析耳机市场”“查下女装在浙江发货的情况”这类需求。 默认行为对齐当前插件项目里的市场分析功能：综合排序、关键词来自用户输入、发货地默认留空，并自动获取一批靠前商品做分析。
- `市场排行趋势` (运行时副本 / active-skills)：生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量…
- `快递超重补差对账` (运行时副本 / active-skills)：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北…
- `推广管理助手` (运行时副本 / active-skills)：万相台无界版推广计划的自动化管理 Skill。通过 API 直接调用万相台后端，支持 P0+P1 全场景： - 货品全站推广（onebpSite）：选品 + 投产比 + 预算，一键创建 - 关键词推广（onebpSearch）：搜索卡位 /…
- `taobao-market-analysis` (运行时副本 / active-skills)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- `taobao-market-analysis` (运行时副本 / active-skills)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- `商品静态四象限分析` (个人/项目自定义 / customized-skills)：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根…
- `market-analysis` (个人/项目自定义 / customized-skills)：市场分析 skill。适合“帮我看看手机的趋势”“分析耳机市场”“查下女装在浙江发货的情况”这类需求。 默认行为对齐当前插件项目里的市场分析功能：综合排序、关键词来自用户输入、发货地默认留空，并自动获取一批靠前商品做分析。
- `快递超重补差对账` (个人/项目自定义 / customized-skills)：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北…
- `work-browser` (个人/项目自定义 / customized-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 …
- `taobao-market-analysis` (个人/项目自定义 / customized-skills)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- `keyword-assistant` (个人/项目自定义 / default-workspace-skills)：关键词分析助手 — 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词…
- `keyword-data-export` (个人/项目自定义 / default-workspace-skills)：关键词数据导出 — 只查词、不分析、生成带格式的 Excel。 输入：种子关键词。 触发：用户要导出关键词词表、查关键词明细数据、只要 Excel 不要分析报告、提到"关键词数据导出/生成词表/只查词表"。
- `keyword-traffic` (个人/项目自定义 / default-workspace-skills)：关键词流量解析 — 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总…
- `market-analysis` (个人/项目自定义 / default-workspace-skills)：淘宝商品市场分析 — 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- `market-trend` (个人/项目自定义 / default-workspace-skills)：市场排行趋势 — 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、…
- `qa-merge-clean` (个人/项目自定义 / default-workspace-skills)：问大家合并清洗助手 — 处理一个或多个“问大家”Excel 表格。 适合“把问大家表合并”“删除昵称/时间列”“从文件名提取商品ID”“整理成统一分析表”这类需求。 核心能力： 1. 输入一个 Excel 文件，输出单文件清洗结果 2. 输…
- `review-cleaning-assistant` (个人/项目自定义 / default-workspace-skills)：评价清洗助手 — 处理电商评价 Excel 表格。适合“清洗评价表”“把追评并到初评下面”“只保留评价列”“删除无意义评价”“清理和商品无关的评价”这类需求。 核心能力： 1. 读取评价 Excel（如观数评价数据） 2. 将“追评”并入“…
- `search-term-blue-ocean-report` (个人/项目自定义 / default-workspace-skills)：搜索词蓝海分析报告 — 输入结构与“观数搜索分析”类似的 Excel 表格，自动识别蓝海搜索词，输出单文件可转发的 HTML 分析报告与明细 CSV。 适合“分析这个搜索词表”“找蓝海搜索词”“把搜索分析 Excel 做成报告”“从搜索词数…
- `生意参谋搜索词排行下载` (个人/项目自定义 / default-workspace-skills)：输入一个淘宝生意参谋“市场-搜索词排行榜”页面 URL，连接已打开且已登录的生意参谋 Chrome，自动完成： 1) 打开目标页面 2) 打开观数插件“搜索分析”弹窗 3) 自动加载 30 页数据 4) 导出 XLSX 5) 关闭观数插件弹…
- `taobao-native` (个人/项目自定义 / default-workspace-skills)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, pla…
- `taobao-profit-statement` (个人/项目自定义 / default-workspace-skills)：淘宝利润表自动生成 Skill。输入包含淘宝资金账单、映射表、聚合账户、保证金等 sheet 的 Excel 工作簿，自动生成“利润表”。适合“生成淘宝利润表”“财税表格处理”“用淘宝账单做利润表”“自动完成利润表”这类需求。生成时必须忽略…
- `taobao-search-parser` (个人/项目自定义 / default-workspace-skills)：淘宝搜索商品解析 skill。输入由工作浏览器输出并持久化保存的压缩 DOM JSON，解析淘宝搜索结果页中的商品卡片信息，输出结构化数据和 Excel 文件。 适合“解析这个淘宝搜索压缩dom”“把淘宝搜索结果压缩dom导出成excel”…
- `work-browser` (个人/项目自定义 / default-workspace-skills)：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 …
- `work-browser2` (个人/项目自定义 / default-workspace-skills)：工作浏览器 skill。用于“打开/复用我的淘宝、生意参谋、小红书、抖音或普通账号浏览器”“继续操作已登录页面”“读取网页压缩 DOM 并降低 token 消耗”等任务。 它提供按 profile 隔离的真实 Chrome 工作会话，复用各…
- `guanshu-review` (个人/项目自定义 / migration-bundle)：观数浏览器扩展前端代码评审工具。对分支代码进行规范检查，生成评审报告。检查项：P0-颜色硬编码、内联样式、if嵌套、重复造轮子、Content Script挂载方式；P1-BEM命名、魔法数字、第三方库引入；P2-文件职责单一、长文件拆分。…
- `taobao-market-analysis` (个人/项目自定义 / standalone-local)：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- `货号跨店铺表现差异分析` (个人/项目自定义 / standalone-local)：🎯 任务目标 基于指定货号或全量数据，分析并识别同一货号在不同店铺/链接间销售表现差异显著的商品，帮助商家发现潜在的分销优化机会。

### Agent 工程 / Skill / Plugin / MCP

- `browser_visible` (系统/内置 / global-skill-pool)：当用户希望打开真实可见的浏览器窗口（而非后台无头模式）时，使用 browser_use 的 headed 参数启动浏览器，随后可正常 open/snapshot/click 等。适用于用户想亲眼看到页面、演示或调试场景。
- `cron` (系统/内置 / global-skill-pool)：通过 sealclaw 命令管理定时任务 - 创建、查询、暂停、恢复、删除任务
- `dingtalk_channel_connect` (系统/内置 / global-skill-pool)：使用可视浏览器自动完成 SealClaw 的钉钉频道接入。适用于用户提到钉钉、DingTalk、开发者后台、Client ID、Client Secret、机器人、Stream 模式、绑定或配置 channel 的场景；支持遇到登录页时暂停…
- `guidance` (系统/内置 / global-skill-pool)：回答用户关于 SealClaw 安装与配置的问题：优先定位并阅读本地文档，再提炼答案；若本地信息不足，兜底访问官网文档。
- `himalaya` (系统/内置 / global-skill-pool)：CLI to manage emails via IMAP/SMTP. Use `himalaya` to list, read, write, reply, forward, search, and organize emails fro…
- `news` (系统/内置 / global-skill-pool)：Look up the latest news for the user from specified news sites. Provides authoritative URLs for politics, finance, socie…
- `全局脚本工具集` (系统/内置 / global-skill-pool)：Skill 基础设施脚本，提供环境初始化、依赖自动安装和跨平台启动能力。 包含：全局依赖安装（macOS/Linux/Windows）、Skill 运行时自动依赖引导（bootstrap）、Windows 嵌入式 Python 部署。 触发…
- `智能数据分析` (系统/内置 / global-skill-pool)：基于 DuckDB 引擎的高效数据分析工具；当用户需要对 CSV/JSON/Parquet/Excel 等数据文件进行 SQL 查询、数据分析、数据抽样或需要自动纠错的查询执行时使用
- `xlsx` (系统/内置 / global-skill-pool)：Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: …
- `browser_visible` (运行时副本 / active-skills)：当用户希望打开真实可见的浏览器窗口（而非后台无头模式）时，使用 browser_use 的 headed 参数启动浏览器，随后可正常 open/snapshot/click 等。适用于用户想亲眼看到页面、演示或调试场景。
- `cron` (运行时副本 / active-skills)：通过 sealclaw 命令管理定时任务 - 创建、查询、暂停、恢复、删除任务
- `dingtalk_channel_connect` (运行时副本 / active-skills)：使用可视浏览器自动完成 SealClaw 的钉钉频道接入。适用于用户提到钉钉、DingTalk、开发者后台、Client ID、Client Secret、机器人、Stream 模式、绑定或配置 channel 的场景；支持遇到登录页时暂停…
- `guidance` (运行时副本 / active-skills)：回答用户关于 SealClaw 安装与配置的问题：优先定位并阅读本地文档，再提炼答案；若本地信息不足，兜底访问官网文档。
- `himalaya` (运行时副本 / active-skills)：CLI to manage emails via IMAP/SMTP. Use `himalaya` to list, read, write, reply, forward, search, and organize emails fro…
- `news` (运行时副本 / active-skills)：Look up the latest news for the user from specified news sites. Provides authoritative URLs for politics, finance, socie…
- `全局脚本工具集` (运行时副本 / active-skills)：Skill 基础设施脚本，提供环境初始化、依赖自动安装和跨平台启动能力。 包含：全局依赖安装（macOS/Linux/Windows）、Skill 运行时自动依赖引导（bootstrap）、Windows 嵌入式 Python 部署。 触发…
- `智能数据分析` (运行时副本 / active-skills)：基于 DuckDB 引擎的高效数据分析工具；当用户需要对 CSV/JSON/Parquet/Excel 等数据文件进行 SQL 查询、数据分析、数据抽样或需要自动纠错的查询执行时使用
- `xlsx` (运行时副本 / active-skills)：Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: …

## Skill 详情

### `gpt生图`

- Agent / 环境：SealSeek
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：backup
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/backups/_backup_gpt-image-generation_before_gemini_migration_20260430/SKILL.md`
- 功能检索描述：使用 EvoLink GPT Image 2 / gpt-image-2 进行文生图、图生图、图片优化、中文电商海报/主图文案排版优化。用户说“用gpt生图skill”“gpt生图”“GPT生图”“优化这张图和文案排版”“用GPT优化图片/生成图片”时触发。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：gpt生图 gpt生图 使用 EvoLink GPT Image 2 / gpt-image-2 进行文生图、图生图、图片优化、中文电商海报/主图文案排版优化。用户说“用gpt生图skill”“gpt生图”“GPT生图”“优化这张图和文案排版”“用GPT优化图片/生成图片”时触发。 _backup_gpt-image-generation_before_gemini_migration_20260430/SKILL.md backup

### `ai-agent-skill-registry-sync`

- Agent / 环境：SealSeek
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：backup
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/backups/llmwiki-skill-update-20260612171939/workspace-ai-agent-skill-registry-sync/SKILL.md`
- 功能检索描述：Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under /Users/pechen/wiki. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：ai-agent-skill-registry-sync AI Agent Skill Registry Sync Scan Peter's local AI agent skill directories across Codex, Hermes, Lark Agent, OpenClaw, SealSeek, and Claude Code, then update the LLM Wiki skill registry pages under /Users/pechen/wiki. Use when the user asks to find newly created skills, refresh the cross-agent skill registry, add agent skills to the wiki, check whether skill inventory is up to date, or make skills discoverable for future AI agents. llmwiki-skill-update-20260612171939/workspace-ai-agent-skill-registry-sync/SKILL.md backup

### `llm-wiki`

- Agent / 环境：SealSeek
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：backup
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/backups/llmwiki-skill-update-20260612171939/workspace-llm-wiki/SKILL.md`
- 功能检索描述：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki Karpathy's LLM Wiki Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency. llmwiki-skill-update-20260612171939/workspace-llm-wiki/SKILL.md backup

### `llm-wiki-audit-and-optimization`

- Agent / 环境：SealSeek
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：backup
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/backups/llmwiki-skill-update-20260612171939/workspace-llm-wiki-audit-and-optimization/SKILL.md`
- 功能检索描述：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit and Optimization Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base. llmwiki-skill-update-20260612171939/workspace-llm-wiki-audit-and-optimization/SKILL.md backup

### `llm-wiki-ingest`

- Agent / 环境：SealSeek
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：backup
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/backups/llmwiki-skill-update-20260612171939/workspace-llm-wiki-ingest/SKILL.md`
- 功能检索描述：Unified LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal knowledge pages, domains/视觉制作/05-小红书风格AI生图/index/log updates, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal knowledge pages, domains/视觉制作/05-小红书风格AI生图/index/log updates, and audit handoff. llmwiki-skill-update-20260612171939/workspace-llm-wiki-ingest/SKILL.md backup

### `llm-wiki-recompile-runner`

- Agent / 环境：SealSeek
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：backup
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/backups/llmwiki-skill-update-20260612171939/workspace-llm-wiki-recompile-runner/SKILL.md`
- 功能检索描述：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale domains/视觉制作/05-小红书风格AI生图/index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and course-transcript-to-knowledge, then verifies post-ingest quality.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：llm-wiki-recompile-runner LLM Wiki Recompile Runner Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale domains/视觉制作/05-小红书风格AI生图/index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and course-transcript-to-knowledge, then verifies post-ingest quality. llmwiki-skill-update-20260612171939/workspace-llm-wiki-recompile-runner/SKILL.md backup

### `browser_visible`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/browser_visible/SKILL.md`
- 功能检索描述：当用户希望打开真实可见的浏览器窗口（而非后台无头模式）时，使用 browser_use 的 headed 参数启动浏览器，随后可正常 open/snapshot/click 等。适用于用户想亲眼看到页面、演示或调试场景。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：browser_visible 可见浏览器（真实窗口）参考 当用户希望打开真实可见的浏览器窗口（而非后台无头模式）时，使用 browser_use 的 headed 参数启动浏览器，随后可正常 open/snapshot/click 等。适用于用户想亲眼看到页面、演示或调试场景。 browser_visible/SKILL.md global-skill-pool

### `cron`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/cron/SKILL.md`
- 功能检索描述：通过 sealclaw 命令管理定时任务 - 创建、查询、暂停、恢复、删除任务
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：cron 定时任务管理 通过 sealclaw 命令管理定时任务 - 创建、查询、暂停、恢复、删除任务 cron/SKILL.md global-skill-pool

### `dingtalk_channel_connect`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/dingtalk_channel/SKILL.md`
- 功能检索描述：使用可视浏览器自动完成 SealClaw 的钉钉频道接入。适用于用户提到钉钉、DingTalk、开发者后台、Client ID、Client Secret、机器人、Stream 模式、绑定或配置 channel 的场景；支持遇到登录页时暂停，等待用户登录后继续。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：dingtalk_channel_connect 钉钉 Channel 自动连接（可视浏览器） 使用可视浏览器自动完成 SealClaw 的钉钉频道接入。适用于用户提到钉钉、DingTalk、开发者后台、Client ID、Client Secret、机器人、Stream 模式、绑定或配置 channel 的场景；支持遇到登录页时暂停，等待用户登录后继续。 dingtalk_channel/SKILL.md global-skill-pool

### `file_reader`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/file_reader/SKILL.md`
- 功能检索描述：Read and summarize text-based file types only. Prefer read_file for text formats; use execute_shell_command for type detection when needed. PDF/Office/images/archives are handled by other skills.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：file_reader File Reader Toolbox Read and summarize text-based file types only. Prefer read_file for text formats; use execute_shell_command for type detection when needed. PDF/Office/images/archives are handled by other skills. file_reader/SKILL.md global-skill-pool

### `guidance`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/guidance/SKILL.md`
- 功能检索描述：回答用户关于 SealClaw 安装与配置的问题：优先定位并阅读本地文档，再提炼答案；若本地信息不足，兜底访问官网文档。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：guidance SealClaw 安装与配置问答指南 回答用户关于 SealClaw 安装与配置的问题：优先定位并阅读本地文档，再提炼答案；若本地信息不足，兜底访问官网文档。 guidance/SKILL.md global-skill-pool

### `himalaya`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/himalaya/SKILL.md`
- 功能检索描述：CLI to manage emails via IMAP/SMTP. Use `himalaya` to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language).
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：himalaya Himalaya Email CLI CLI to manage emails via IMAP/SMTP. Use himalaya to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language). himalaya/SKILL.md global-skill-pool

### `news`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/news/SKILL.md`
- 功能检索描述：Look up the latest news for the user from specified news sites. Provides authoritative URLs for politics, finance, society, world, tech, sports, and entertainment. Use browser_use to open each URL and snapshot to get content, then summarize for the user.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：news News Reference Look up the latest news for the user from specified news sites. Provides authoritative URLs for politics, finance, society, world, tech, sports, and entertainment. Use browser_use to open each URL and snapshot to get content, then summarize for the user. news/SKILL.md global-skill-pool

### `pdf`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/pdf/SKILL.md`
- 功能检索描述：PDF 文件处理技能。只要用户提到 PDF、.pdf、PDF文件、读取PDF、提取PDF文字、提取PDF表格、合并PDF、拆分PDF、旋转PDF、生成PDF、填写PDF表单、导出PDF、扫描件OCR 等需求，就应使用本 skill。 Supports reading, writing, extracting, merging, splitting, rotating, annotating, form filling, image extraction, and OCR-oriented preparation for PDF files.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：pdf PDF Processing Guide PDF 文件处理技能。只要用户提到 PDF、.pdf、PDF文件、读取PDF、提取PDF文字、提取PDF表格、合并PDF、拆分PDF、旋转PDF、生成PDF、填写PDF表单、导出PDF、扫描件OCR 等需求，就应使用本 skill。 Supports reading, writing, extracting, merging, splitting, rotating, annotating, form filling, image extraction, and OCR-oriented preparation for PDF files. pdf/SKILL.md global-skill-pool

### `pptx`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/pptx/SKILL.md`
- 功能检索描述：Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：pptx PPTX Skill Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill. pptx/SKILL.md global-skill-pool

### `全局脚本工具集`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/scripts/SKILL.md`
- 功能检索描述：Skill 基础设施脚本，提供环境初始化、依赖自动安装和跨平台启动能力。 包含：全局依赖安装（macOS/Linux/Windows）、Skill 运行时自动依赖引导（bootstrap）、Windows 嵌入式 Python 部署。 触发：首次部署环境、依赖缺失、新 Skill 开发时需要集成 bootstrap 排除：具体业务 Skill 的运行 → 用对应 Skill
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：全局脚本工具集 脚本清单 Skill 基础设施脚本，提供环境初始化、依赖自动安装和跨平台启动能力。 包含：全局依赖安装（macOS/Linux/Windows）、Skill 运行时自动依赖引导（bootstrap）、Windows 嵌入式 Python 部署。 触发：首次部署环境、依赖缺失、新 Skill 开发时需要集成 bootstrap 排除：具体业务 Skill 的运行 → 用对应 Skill scripts/SKILL.md global-skill-pool

### `智能数据分析`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/smart-data-analyzer/SKILL.md`
- 功能检索描述：基于 DuckDB 引擎的高效数据分析工具；当用户需要对 CSV/JSON/Parquet/Excel 等数据文件进行 SQL 查询、数据分析、数据抽样或需要自动纠错的查询执行时使用
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求
- 检索关键词：智能数据分析 Chat2DuckDB 数据分析 基于 DuckDB 引擎的高效数据分析工具；当用户需要对 CSV/JSON/Parquet/Excel 等数据文件进行 SQL 查询、数据分析、数据抽样或需要自动纠错的查询执行时使用 smart-data-analyzer/SKILL.md global-skill-pool

### `xlsx`

- Agent / 环境：SealSeek
- 归属分类：系统/内置
- 归属依据：SealSeek 全局 skill_pool，视为系统/底层通用能力。
- 来源类型：global-skill-pool
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/skill_pool/xlsx/SKILL.md`
- 功能检索描述：Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliv…
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：xlsx Requirements for Outputs Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliv… xlsx/SKILL.md global-skill-pool

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

### `browser_visible`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/browser_visible/SKILL.md`
- 功能检索描述：当用户希望打开真实可见的浏览器窗口（而非后台无头模式）时，使用 browser_use 的 headed 参数启动浏览器，随后可正常 open/snapshot/click 等。适用于用户想亲眼看到页面、演示或调试场景。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：browser_visible 可见浏览器（真实窗口）参考 当用户希望打开真实可见的浏览器窗口（而非后台无头模式）时，使用 browser_use 的 headed 参数启动浏览器，随后可正常 open/snapshot/click 等。适用于用户想亲眼看到页面、演示或调试场景。 browser_visible/SKILL.md active-skills

### `cron`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/cron/SKILL.md`
- 功能检索描述：通过 sealclaw 命令管理定时任务 - 创建、查询、暂停、恢复、删除任务
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：cron 定时任务管理 通过 sealclaw 命令管理定时任务 - 创建、查询、暂停、恢复、删除任务 cron/SKILL.md active-skills

### `dingtalk_channel_connect`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/dingtalk_channel/SKILL.md`
- 功能检索描述：使用可视浏览器自动完成 SealClaw 的钉钉频道接入。适用于用户提到钉钉、DingTalk、开发者后台、Client ID、Client Secret、机器人、Stream 模式、绑定或配置 channel 的场景；支持遇到登录页时暂停，等待用户登录后继续。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：dingtalk_channel_connect 钉钉 Channel 自动连接（可视浏览器） 使用可视浏览器自动完成 SealClaw 的钉钉频道接入。适用于用户提到钉钉、DingTalk、开发者后台、Client ID、Client Secret、机器人、Stream 模式、绑定或配置 channel 的场景；支持遇到登录页时暂停，等待用户登录后继续。 dingtalk_channel/SKILL.md active-skills

### `docx`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/docx/SKILL.md`
- 功能检索描述：Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\", \"word document\", \".docx\", or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a \"report\", \"memo\", \"letter\", \"template\", or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spre…
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：docx DOCX creation, editing, and analysis Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of \"Word doc\", \"word document\", \".docx\", or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a \"report\", \"memo\", \"letter\", \"template\", or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spre… docx/SKILL.md active-skills

### `file_reader`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/file_reader/SKILL.md`
- 功能检索描述：Read and summarize text-based file types only. Prefer read_file for text formats; use execute_shell_command for type detection when needed. PDF/Office/images/archives are handled by other skills.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：file_reader File Reader Toolbox Read and summarize text-based file types only. Prefer read_file for text formats; use execute_shell_command for type detection when needed. PDF/Office/images/archives are handled by other skills. file_reader/SKILL.md active-skills

### `guidance`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/guidance/SKILL.md`
- 功能检索描述：回答用户关于 SealClaw 安装与配置的问题：优先定位并阅读本地文档，再提炼答案；若本地信息不足，兜底访问官网文档。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：guidance SealClaw 安装与配置问答指南 回答用户关于 SealClaw 安装与配置的问题：优先定位并阅读本地文档，再提炼答案；若本地信息不足，兜底访问官网文档。 guidance/SKILL.md active-skills

### `himalaya`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/himalaya/SKILL.md`
- 功能检索描述：CLI to manage emails via IMAP/SMTP. Use `himalaya` to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language).
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：himalaya Himalaya Email CLI CLI to manage emails via IMAP/SMTP. Use himalaya to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language). himalaya/SKILL.md active-skills

### `news`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/news/SKILL.md`
- 功能检索描述：Look up the latest news for the user from specified news sites. Provides authoritative URLs for politics, finance, society, world, tech, sports, and entertainment. Use browser_use to open each URL and snapshot to get content, then summarize for the user.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：news News Reference Look up the latest news for the user from specified news sites. Provides authoritative URLs for politics, finance, society, world, tech, sports, and entertainment. Use browser_use to open each URL and snapshot to get content, then summarize for the user. news/SKILL.md active-skills

### `pdf`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/pdf/SKILL.md`
- 功能检索描述：PDF 文件处理技能。只要用户提到 PDF、.pdf、PDF文件、读取PDF、提取PDF文字、提取PDF表格、合并PDF、拆分PDF、旋转PDF、生成PDF、填写PDF表单、导出PDF、扫描件OCR 等需求，就应使用本 skill。 Supports reading, writing, extracting, merging, splitting, rotating, annotating, form filling, image extraction, and OCR-oriented preparation for PDF files.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：pdf PDF Processing Guide PDF 文件处理技能。只要用户提到 PDF、.pdf、PDF文件、读取PDF、提取PDF文字、提取PDF表格、合并PDF、拆分PDF、旋转PDF、生成PDF、填写PDF表单、导出PDF、扫描件OCR 等需求，就应使用本 skill。 Supports reading, writing, extracting, merging, splitting, rotating, annotating, form filling, image extraction, and OCR-oriented preparation for PDF files. pdf/SKILL.md active-skills

### `pptx`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/pptx/SKILL.md`
- 功能检索描述：Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：pptx PPTX Skill Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill. pptx/SKILL.md active-skills

### `全局脚本工具集`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/scripts/SKILL.md`
- 功能检索描述：Skill 基础设施脚本，提供环境初始化、依赖自动安装和跨平台启动能力。 包含：全局依赖安装（macOS/Linux/Windows）、Skill 运行时自动依赖引导（bootstrap）、Windows 嵌入式 Python 部署。 触发：首次部署环境、依赖缺失、新 Skill 开发时需要集成 bootstrap 排除：具体业务 Skill 的运行 → 用对应 Skill
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：全局脚本工具集 脚本清单 Skill 基础设施脚本，提供环境初始化、依赖自动安装和跨平台启动能力。 包含：全局依赖安装（macOS/Linux/Windows）、Skill 运行时自动依赖引导（bootstrap）、Windows 嵌入式 Python 部署。 触发：首次部署环境、依赖缺失、新 Skill 开发时需要集成 bootstrap 排除：具体业务 Skill 的运行 → 用对应 Skill scripts/SKILL.md active-skills

### `电商凭证管理`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/sealclaw-auth/SKILL.md`
- 功能检索描述：多平台电商登录凭证管理。支持淘系(生意参谋/淘宝/1688)、抖音(抖店/千川)、拼多多、京东等平台。 全平台统一通过CDP交互式登录提取Cookie(绕过App-Bound Encryption)。自动检测有效性，失效自动刷新，兜底引导手动提供。 触发：用户首次使用任何电商Skill、提到"登录/Cookie/凭证/过期/重新登录"、业务Skill报Cookie无效 排除：具体业务数据查询 → 用对应业务Skill
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：电商凭证管理 支持平台 多平台电商登录凭证管理。支持淘系(生意参谋/淘宝/1688)、抖音(抖店/千川)、拼多多、京东等平台。 全平台统一通过CDP交互式登录提取Cookie(绕过App-Bound Encryption)。自动检测有效性，失效自动刷新，兜底引导手动提供。 触发：用户首次使用任何电商Skill、提到"登录/Cookie/凭证/过期/重新登录"、业务Skill报Cookie无效 排除：具体业务数据查询 → 用对应业务Skill sealclaw-auth/SKILL.md active-skills

### `智能数据分析`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/smart-data-analyzer/SKILL.md`
- 功能检索描述：基于 DuckDB 引擎的高效数据分析工具；当用户需要对 CSV/JSON/Parquet/Excel 等数据文件进行 SQL 查询、数据分析、数据抽样或需要自动纠错的查询执行时使用
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求
- 检索关键词：智能数据分析 Chat2DuckDB 数据分析 基于 DuckDB 引擎的高效数据分析工具；当用户需要对 CSV/JSON/Parquet/Excel 等数据文件进行 SQL 查询、数据分析、数据抽样或需要自动纠错的查询执行时使用 smart-data-analyzer/SKILL.md active-skills

### `xlsx`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/xlsx/SKILL.md`
- 功能检索描述：Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliv…
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：xlsx Requirements for Outputs Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliv… xlsx/SKILL.md active-skills

### `关键词助手`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/关键词分析助手/SKILL.md`
- 功能检索描述：生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标题优化、查看热搜排行、提到"关键词分析/挖掘/蓝海词/供需比/热搜榜/飙升词"
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：关键词助手 Step 0: 登录获取 Cookie（首次使用必做） 生意参谋关键词挖掘与分析工具。支持两种模式： 1. 关联词拓展（expand）：输入种子关键词，批量拓展关联长尾词，返回搜索人气、点击率、转化率、供需比、环比变化等指标 2. 搜索排行榜（rank）：获取热搜/飙升/新词排行榜，无需种子词 触发：用户要分析关键词数据、查蓝海词/长尾词/高转化词、做标题优化、查看热搜排行、提到"关键词分析/挖掘/蓝海词/供需比/热搜榜/飙升词" 关键词分析助手/SKILL.md active-skills

### `关键词流量解析`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/关键词流量解析/SKILL.md`
- 功能检索描述：万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流量趋势/13个月数据/月度趋势/展现指数/竞争指数/市场均价"，或在使用关键词分析助手后想深入分析某个词的长期走势。 排除：关键词拓展/排行榜（用关键词助手）、创建推广计划（用推广管理助手）。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：关键词流量解析 Step 0: 登录获取 Cookie（首次使用必做） 万相台无界版关键词流量趋势分析工具。查询指定关键词在付费搜索场景下的长期市场数据趋势（最多13个月），包括： - 展现指数、点击指数、点击率、点击转化率、竞争指数、市场均价 - 自动匹配关键词所属行业类目 - 市场数据总结（词特性、流量趋势、竞争情况、人群/时间特征） 触发：用户提到"关键词趋势/流量趋势/13个月数据/月度趋势/展现指数/竞争指数/市场均价"，或在使用关键词分析助手后想深入分析某个词的长期走势。 排除：关键词拓展/排行榜（用关键词助手）、创建推广计划（用推广管理助手）。 关键词流量解析/SKILL.md active-skills

### `商品静态四象限分析`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/商品静态四象限分析/SKILL.md`
- 功能检索描述：输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数和付费占比给商品分层并准备分析资料”这类需求。
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：商品静态四象限分析 输入店铺商品统计表（通常为近30天，也支持近7天/最近一周/最近一个月），基于“商品四象限费用迁移静态理论”完成商品四象限分层，并输出 Tailwind 风格的 HTML 报告骨架与结构化分析数据包。 适用于“帮我做商品静态四象限分析”“根据这个商品表输出HTML报告”“按访客数和付费占比给商品分层并准备分析资料”这类需求。 商品静态四象限分析/SKILL.md active-skills

### `image-understanding`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/图片理解/SKILL.md`
- 功能检索描述：图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：image-understanding 图片理解元 skill。输入一张或多张图片，以及一段可选提示词，调用豆包大模型 doubao-seed-2-0-pro-260215 输出图片理解结果。 适合作为其他 skill 的底层图片理解能力，也支持单独调用。 图片理解/SKILL.md active-skills

### `work-browser`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/工作浏览器/SKILL.md`
- 功能检索描述：工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出适合继续喂给模型的压缩 DOM。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：work-browser 查看所有 profile 工作浏览器 skill。适合“打开我的淘宝浏览器”“打开我的生意参谋浏览器”“打开我的小红书浏览器”“打开我的普通账号浏览器”“继续操作已登录页面”这类需求。 它为 SealSeek 提供带独立 profile 的真实浏览器环境，可按命名 profile 启动或连接对应浏览器，复用各自登录态，并输出适合继续喂给模型的压缩 DOM。 工作浏览器/SKILL.md active-skills

### `market-analysis`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/市场分析/SKILL.md`
- 功能检索描述：市场分析 skill。适合“帮我看看手机的趋势”“分析耳机市场”“查下女装在浙江发货的情况”这类需求。 默认行为对齐当前插件项目里的市场分析功能：综合排序、关键词来自用户输入、发货地默认留空，并自动获取一批靠前商品做分析。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：market-analysis 默认方式：综合排序 + 发货地不限 市场分析 skill。适合“帮我看看手机的趋势”“分析耳机市场”“查下女装在浙江发货的情况”这类需求。 默认行为对齐当前插件项目里的市场分析功能：综合排序、关键词来自用户输入、发货地默认留空，并自动获取一批靠前商品做分析。 市场分析/SKILL.md active-skills

### `市场排行趋势`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/市场排行趋势/SKILL.md`
- 功能检索描述：生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、持续上升商品、提到"市场排行/趋势分析/排名变化/新上榜/跌出榜" 排除：关键词分析 → 用关键词助手 Skill
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：市场排行趋势 重要：命令格式 生意参谋市场排行商品趋势分析工具。获取指定类目 4 个周期（周/月）的商品排行数据，聚合分析排名趋势（上升/下降/新上榜/跌出榜/持平），输出趋势数据 + Excel。 支持 5 种榜单类型：交易总量、交易增速、流量总量、加购收藏、新品流量。 触发：用户要查看市场排行趋势、商品排名变化、新上榜商品、持续上升商品、提到"市场排行/趋势分析/排名变化/新上榜/跌出榜" 排除：关键词分析 → 用关键词助手 Skill 市场排行趋势/SKILL.md active-skills

### `快递超重补差对账`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/快递超重补差对账/SKILL.md`
- 功能检索描述：读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 1 元安检费 - 新疆/西藏：0.5kg 以内 5 元；超过 0.5kg 后按“max(floor(重量), 1) × 15”计算 额外输出： - 省份城市统计（按对账明细聚合，支持省份折叠查看城市） - 店铺统计（按对账明细聚合） 适用于“快递超重补差对账”“核对快递公司超重收费”“根据报价单和账单自动对账”场景。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：快递超重补差对账 用途 读取快递报价单、企业内部账单、快递公司账单三类 Excel，按超重补差规则自动逐单对账，输出中文 Excel 结果。 当前内置规则： - 普通地区：3kg 以内不收超重费，超过 3kg 后按“floor(总重量) × 续重单价”计算 - 北京/上海：在普通地区规则基础上，每单加 1 元安检费 - 新疆/西藏：0.5kg 以内 5 元；超过 0.5kg 后按“max(floor(重量), 1) × 15”计算 额外输出： - 省份城市统计（按对账明细聚合，支持省份折叠查看城市） - 店铺统计（按对账明细聚合） 适用于“快递超重补差对账”“核对快递公司超重收费”“根据报价单和账单自动对账”场景。 快递超重补差对账/SKILL.md active-skills

### `推广管理助手`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/推广管理助手/SKILL.md`
- 功能检索描述：万相台无界版推广计划的自动化管理 Skill。通过 API 直接调用万相台后端，支持 P0+P1 全场景： - 货品全站推广（onebpSite）：选品 + 投产比 + 预算，一键创建 - 关键词推广（onebpSearch）：搜索卡位 / 趋势明星 / 流量金卡 / 自定义推广 - 人群推广（onebpDisplay）：高效拉新 / 常客转化 / 人群超市 / 自定义推广 - 计划/广告组查询与启停 - 关键词增删改查 + 质量分查询 - 报表数据查询 触发：用户提到"万相台/推广计划/创建计划/管理计划/广告组/关键词推广/人群推广/货品全站推广/出价/报表"。 排除：纯生意参谋数据分析（用关键词助手）、纯市场排行（用市场排行趋势）。 安全边界：创建/变更类操作必须显式传 `--confirm_submit YES`。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：推广管理助手 Step 0: 登录获取 Cookie（首次使用必做） 万相台无界版推广计划的自动化管理 Skill。通过 API 直接调用万相台后端，支持 P0+P1 全场景： - 货品全站推广（onebpSite）：选品 + 投产比 + 预算，一键创建 - 关键词推广（onebpSearch）：搜索卡位 / 趋势明星 / 流量金卡 / 自定义推广 - 人群推广（onebpDisplay）：高效拉新 / 常客转化 / 人群超市 / 自定义推广 - 计划/广告组查询与启停 - 关键词增删改查 + 质量分查询 - 报表数据查询 触发：用户提到"万相台/推广计划/创建计划/管理计划/广告组/关键词推广/人群推广/货品全站推广/出价/报表"。 排除：纯生意参谋数据分析（用关键词助手）、纯市场排行（用市场排行趋势）。 安全边界：创建/变更类操作必须显式传 --confirm_submit YES 。 推广管理助手/SKILL.md active-skills

### `淘宝商品助手`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/淘宝商品助手/SKILL.md`
- 功能检索描述：淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析"
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：淘宝商品助手 能力说明 淘宝/天猫单品详情查询工具。输入商品ID或链接，获取商品完整信息： 标题、价格（原价/券后价）、销量、SKU列表（属性/价格/库存）、店铺信息、店铺评分、物流、评价数、主图等。 触发：用户要查某个商品的详情、查竞品信息、查商品价格/SKU/销量、提到"查商品/看商品/商品详情/竞品分析" 淘宝商品助手/SKILL.md active-skills

### `taobao-market-analysis`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/淘宝商品市场分析/SKILL.md`
- 功能检索描述：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-market-analysis 默认方式：综合排序 + 发货地不限 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 淘宝商品市场分析/SKILL.md active-skills

### `taobao-market-analysis`

- Agent / 环境：SealSeek
- 归属分类：运行时副本
- 归属依据：SealSeek default workspace active_skills 运行时副本；全量保留，个人库优先使用源目录条目。
- 来源类型：active-skills
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/active_skills/淘宝商品市场分析_原始备份/SKILL.md`
- 功能检索描述：淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-market-analysis 默认方式：综合排序 + 发货地不限 淘宝商品市场分析 skill。通过淘宝搜索页获取指定关键词下的商品市场数据，分析价格分布、标题统计以及商品多维度信息。 适合”帮我看看手机的趋势””分析耳机市场””查下女装在浙江发货的情况”这类需求。 淘宝商品市场分析_原始备份/SKILL.md active-skills

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
- 功能检索描述：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal pages, domains/视觉制作/05-小红书风格AI生图/index/log updates, Obsidian route audit, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal pages, domains/视觉制作/05-小红书风格AI生图/index/log updates, Obsidian route audit, and audit handoff. llm-wiki-ingest/SKILL.md default-workspace-skills

### `llm-wiki-recompile-runner`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：default-workspace-skills
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.sealseek/workspaces/default/skills/llm-wiki-recompile-runner/SKILL.md`
- 功能检索描述：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale domains/视觉制作/05-小红书风格AI生图/index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：llm-wiki-recompile-runner LLM Wiki Recompile Runner Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale domains/视觉制作/05-小红书风格AI生图/index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality. llm-wiki-recompile-runner/SKILL.md default-workspace-skills

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
- 功能检索描述：Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal pages, domains/视觉制作/05-小红书风格AI生图/index/log updates, Obsidian route audit, and audit handoff.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：llm-wiki-ingest LLM Wiki Ingest Unified and only LLM Wiki ingestion skill for Peter's /Users/pechen/wiki. Use for any source that should be compiled into the wiki, including Obsidian Clippings, webpages, books, EPUB/PDF, course transcripts, meeting transcripts, API docs, XMind files, spreadsheets, markdown docs, product/tool docs, PPT/courseware, and unknown source types. Enforces lossless knowledge-unit coverage, raw preservation, extraction notes, formal pages, domains/视觉制作/05-小红书风格AI生图/index/log updates, Obsidian route audit, and audit handoff. LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-ingest/SKILL.md standalone-local

### `llm-wiki-recompile-runner`

- Agent / 环境：SealSeek
- 归属分类：个人/项目自定义
- 归属依据：SealSeek workspace/customized/standalone/migration skill，按个人/项目自定义处理。
- 来源类型：standalone-local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/sealseek/LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-recompile-runner/SKILL.md`
- 功能检索描述：Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale domains/视觉制作/05-小红书风格AI生图/index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：llm-wiki-recompile-runner LLM Wiki Recompile Runner Orchestrate repair of existing LLM Wiki domains or learning paths that contain shell/thin pages. Use after an audit finds placeholder pages, incomplete extraction notes, stale domains/视觉制作/05-小红书风格AI生图/index status, or raw transcripts that need to be recompiled into usable formal knowledge pages. Coordinates llm-wiki-audit-and-optimization and llm-wiki-ingest transcript adapter, then verifies post-ingest quality. LLM-Wiki核心Skill交付包/package_contents/skills/llm-wiki-recompile-runner/SKILL.md standalone-local

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

