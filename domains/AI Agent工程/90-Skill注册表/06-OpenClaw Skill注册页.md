---
title: OpenClaw Skill 注册页
type: concept
created: 2026-06-14
updated: 2026-06-14
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
- 当前记录数量：4

归属分类统计：

- 个人/项目自定义: 4

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 电商 / 商品 / 品牌运营

- `ecom-market-rank` (个人/项目自定义 / local)：电商市场排行榜数据分析。适用于用户上传商品排行榜 Excel/CSV 文件（如淘宝生意参谋市场排行导出）时触发。输入：商品排行榜表格文件（xlsx/csv）。输出：文本分析总结 + 离线 HTML 可视化报告。触发场景：用户发送表格并要求分…
- `taobao-native` (个人/项目自定义 / local)：Shopping assistant via Taobao Desktop client. Use when the user needs to search products, view details, add to cart, pla…
- `web-reader` (个人/项目自定义 / local)：用真实 Chrome 浏览器（保留登录态）读取网页并压缩 DOM，供 AI 高效分析。适用于需要访问需要登录的网站（淘宝、生意参谋、千牛、飞书等）时抓取页面数据、进行页面操作（点击、填表、滚动）。核心优势：真实 Chrome 不被反爬识别，…

### Agent 工程 / Skill / Plugin / MCP

- `mcporter` (个人/项目自定义 / local)：Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio).

## Skill 详情

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

