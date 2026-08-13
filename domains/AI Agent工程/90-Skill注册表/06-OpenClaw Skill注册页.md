---
title: OpenClaw Skill 注册页
type: concept
created: 2026-08-10
updated: 2026-08-10
domain: AI Agent工程
tags: [ai-agent, openclaw, skill, registry]
sources:
  - /Users/pechen/.openclaw/workspace/skills
status: active
---
# OpenClaw Skill 注册页

本页记录 OpenClaw 环境中的 skill，用于 AI Agent 检索“是否已有类似 skill”并定位原始 SKILL.md。

## 维护范围

来源目录：

- `/Users/pechen/.openclaw/workspace/skills`

- 说明：OpenClaw workspace skills.
- 当前记录数量：11

归属分类统计：

- 个人/项目自定义: 11

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 知识库 / 知识管理 / LLM Wiki

- `1688-distribution` (个人/项目自定义 / local)：1688 分销唯一主入口。选品铺货、订单管理、知识库查询、店铺绑定，涵盖分销全链路。当用户提到铺货、选品、分销、上架、查订单、催发、旺旺、发货流程、绑店时触发。不要在用户仅询问非1688业务（如闲聊、天气、翻译等无关话题）时触发。

### 视觉 / 内容 / 课件生产

- `1688-product-find` (个人/项目自定义 / local)：1688智能选品找货能力。通过文字、图片或链接搜商品、找同款、找相似款，支持批量采购比价、热销选品、跨境找货、场景化选品及多条件筛选（价格/销量/材质/属性排除等）。 触发词：找商品、找同款、搜商品、帮我找、想要XX、图片找货、链接找货、以…
- `sealseek-canvas` (个人/项目自定义 / local)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authen…

### 电商 / 商品 / 品牌运营

- `1688-marketing` (个人/项目自定义 / local)：1688营销 Skill —— 帮助商家进行招商活动报名、查看商机推荐等营销操作。 核心工具能力：招商活动查询、商品建议价查询、活动报名提交、商机推荐查询。 触发词：报名活动、招商活动、查询活动、提报、报名、活动报名、查看建议价、商机推荐、…
- `1688-shopkeeper` (个人/项目自定义 / local)：1688选品铺货 + 商机趋势专家。用于：(1) 在1688搜索商品/选品找货源 (2) 查询已绑定的下游店铺 (3) 将商品铺货到抖音/拼多多/小红书/淘宝等平台 (4) 配置1688 AK密钥 (5) 查看即时商机热榜 (6) 查看类目…
- `1688-source-suppliers` (个人/项目自定义 / local)：1688找供应商 —— 结合用户需求与关键字查询对应的供应商及工厂信息 核心工具能力：1688供应商查询能力。用于查询1688平台上的供应商及工厂信息。 触发词：找供应商、查供应商、1688供应商、供应商信息、工厂信息、产业带查询。 不触发…
- `1688-sourcing-inquiry` (个人/项目自定义 / local)：1688采购询盘寻源能力。当用户有模糊的采购需求但尚未选定具体商品时，通过描述商品名称、数量和需求，发起采购询盘任务，由平台匹配合适的供应商和报价方案。 核心定位：采购前的询盘寻源阶段，帮助用户将模糊的采购意向转化为结构化询盘，获取供应商报…
- `ecom-market-rank` (个人/项目自定义 / local)：电商市场排行榜数据分析。适用于用户上传商品排行榜 Excel/CSV 文件（如淘宝生意参谋市场排行导出）时触发。输入：商品排行榜表格文件（xlsx/csv）。输出：文本分析总结 + 离线 HTML 可视化报告。触发场景：用户发送表格并要求分…
- `taobao-native` (个人/项目自定义 / local)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, pla…
- `web-reader` (个人/项目自定义 / local)：用真实 Chrome 浏览器（保留登录态）读取网页并压缩 DOM，供 AI 高效分析。适用于需要访问需要登录的网站（淘宝、生意参谋、千牛、飞书等）时抓取页面数据、进行页面操作（点击、填表、滚动）。核心优势：真实 Chrome 不被反爬识别，…

### Agent 工程 / Skill / Plugin / MCP

- `mcporter` (个人/项目自定义 / local)：Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio).

## Skill 详情

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

