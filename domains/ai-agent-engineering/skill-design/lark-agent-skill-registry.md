---
title: Lark Agent Skill 注册页
type: concept
created: 2026-06-12
updated: 2026-06-12
domain: ai-agent-engineering
tags: [ai-agent, lark-agent, skill, registry]
sources:
  - /Users/pechen/.agents/skills
status: active
---
# Lark Agent Skill 注册页

本页记录 Lark Agent 环境中的 skill，用于 AI Agent 检索“是否已有类似 skill”并定位原始 SKILL.md。

## 维护范围

来源目录：

- `/Users/pechen/.agents/skills`

- 说明：Feishu/Lark agent skills.
- 当前记录数量：25

归属分类统计：

- 系统/内置: 25

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/ai-agent-engineering/skill-design/personal-ai-agent-skill-registry|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 知识库 / 知识管理 / LLM Wiki

- `lark-drive` (系统/内置 / local)：飞书云空间：管理云空间中的文件和文件夹。上传和下载文件、创建文件夹、复制/移动/删除文件、查看文件元数据、管理文档评论、管理文档权限、订阅用户评论变更事件、修改文件标题（docx、sheet、bitable、file、folder、wiki…
- `lark-wiki` (系统/内置 / local)：飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。

### 视觉 / 内容 / 课件生产

- `lark-doc` (系统/内置 / local)：飞书云文档（v2）：创建和编辑飞书文档。使用本 skill 时，docs +create、docs +fetch、docs +update 必须携带 --api-version v2；默认使用 DocxXML 格式（也支持 Markdown…
- `lark-event` (系统/内置 / local)：Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <Ev…
- `lark-im` (系统/内置 / local)：飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、管理标记数据时使用。
- `lark-slides` (系统/内置 / local)：飞书幻灯片：创建和编辑幻灯片，接口通过 XML 协议通信。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。
- `lark-whiteboard` (系统/内置 / local)：飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用 DSL（转成 OpenAPI 格式）、PlantUML/Mermaid 格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板，或是需要可视…

### 电商 / 商品 / 品牌运营

- `lark-minutes` (系统/内置 / local)：飞书妙记：妙记相关基本功能。1.查询妙记列表（按关键词/所有者/参与者/时间范围）；2.获取妙记基础信息（标题、封面、时长 等）；3.下载妙记音视频文件；4.获取妙记相关 AI 产物（总结、待办、章节）；5.上传音视频生成妙记，也支持将本地…
- `lark-sheets` (系统/内置 / local)：飞书电子表格：创建和操作电子表格。支持创建表格、创建/复制/删除/更新工作表、读写单元格、追加行数据、查找内容、导出文件。当用户需要创建电子表格、管理工作表、批量读写数据、在已知表格中查找内容、导出或下载表格时使用。若用户是想按名称或关键词…
- `lark-vc` (系统/内置 / local)：飞书视频会议：查询会议记录、获取会议纪要产物（总结、待办、章节、逐字稿）。1. 查询已经结束的会议数量或详情时使用本技能(如历史日期｜ 昨天 | 上周 | 今天已经开过的会议等场景)，查询未开始的会议日程使用 lark-calendar 技…

### Agent 工程 / Skill / Plugin / MCP

- `lark-approval` (系统/内置 / local)：飞书审批 API：审批实例、审批任务管理。
- `lark-attendance` (系统/内置 / local)：飞书考勤打卡：查询自己的考勤打卡记录
- `lark-base` (系统/内置 / local)：当需要用 lark-cli 操作飞书多维表格（Base）时调用：搜索 Base、建表、字段管理、记录读写、记录分享链接、视图配置、历史查询，以及角色/表单/仪表盘管理/工作流；也适用于把旧的 +table / +field / +recor…
- `lark-calendar` (系统/内置 / local)：飞书日历（calendar）：提供日历与日程（会议）的全面管理能力。核心场景包括：查看/搜索日程、创建/更新日程、管理参会人、查询忙闲状态及推荐空闲时段、查询/搜索与预定会议室。注意：涉及【预约日程/会议】或【查询/预定会议室】时，必须先读…
- `lark-contact` (系统/内置 / local)：飞书 / Lark 通讯录,用于按姓名 / 邮箱把员工解析成 open_id,以及按 open_id 反查员工的姓名 / 部门 / 邮箱 / 联系方式。当用户说出某人姓名而下一步需要发消息 / 加群 / 排日程时,先用本 skill 把姓名…
- `lark-mail` (系统/内置 / local)：飞书邮箱 — draft, compose, send, reply, forward, read, and search emails; manage drafts, folders, labels, contacts, attachme…
- `lark-markdown` (系统/内置 / local)：飞书 Markdown：查看、创建、上传和编辑 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取或修改时使用。
- `lark-okr` (系统/内置 / local)：飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标（Objective）、关键结果（Key Result）、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。
- `lark-openapi-explorer` (系统/内置 / local)：飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时…
- `lark-shared` (系统/内置 / local)：飞书/Lark CLI 共享基础：应用配置初始化、认证登录（auth login）、身份切换（--as user/bot）、权限与 scope 管理、Permission denied 错误处理、安全规则。当用户需要第一次配置(`lark-…
- `lark-skill-maker` (系统/内置 / local)：创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。
- `lark-task` (系统/内置 / local)：飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务…
- `lark-whiteboard-cli` (系统/内置 / local)：当用户要求或使用飞书画板绘制架构图、流程图、思维导图、时序图或其他可视化图表时使用此 skill，作为使用 whiteboard-cli 设计图表布局的指南
- `lark-workflow-meeting-summary` (系统/内置 / local)：会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。
- `lark-workflow-standup-report` (系统/内置 / local)：日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。

## Skill 详情

### `lark-approval`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-approval/SKILL.md`
- 功能检索描述：飞书审批 API：审批实例、审批任务管理。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-approval approval (v4) 飞书审批 API：审批实例、审批任务管理。 lark-approval/SKILL.md local

### `lark-attendance`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-attendance/SKILL.md`
- 功能检索描述：飞书考勤打卡：查询自己的考勤打卡记录
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-attendance attendance (v1) 飞书考勤打卡：查询自己的考勤打卡记录 lark-attendance/SKILL.md local

### `lark-base`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-base/SKILL.md`
- 功能检索描述：当需要用 lark-cli 操作飞书多维表格（Base）时调用：搜索 Base、建表、字段管理、记录读写、记录分享链接、视图配置、历史查询，以及角色/表单/仪表盘管理/工作流；也适用于把旧的 +table / +field / +record 写法改成当前命令写法。涉及字段设计、公式字段、查找引用、跨表计算、行级派生指标、数据分析需求时也必须使用本 skill。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-base base 当需要用 lark-cli 操作飞书多维表格（Base）时调用：搜索 Base、建表、字段管理、记录读写、记录分享链接、视图配置、历史查询，以及角色/表单/仪表盘管理/工作流；也适用于把旧的 +table / +field / +record 写法改成当前命令写法。涉及字段设计、公式字段、查找引用、跨表计算、行级派生指标、数据分析需求时也必须使用本 skill。 lark-base/SKILL.md local

### `lark-calendar`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-calendar/SKILL.md`
- 功能检索描述：飞书日历（calendar）：提供日历与日程（会议）的全面管理能力。核心场景包括：查看/搜索日程、创建/更新日程、管理参会人、查询忙闲状态及推荐空闲时段、查询/搜索与预定会议室。注意：涉及【预约日程/会议】或【查询/预定会议室】时，必须先读取 references/lark-calendar-schedule-meeting.md 工作流！高频操作请优先使用 Shortcuts：+agenda（快速概览今日/近期行程）、+create（创建日程并按需邀请参会人及预定会议室）、+freebusy（查询用户主日历的忙闲信息和rsvp的状态）、+rsvp（回复日程邀请）
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-calendar calendar (v4) 飞书日历（calendar）：提供日历与日程（会议）的全面管理能力。核心场景包括：查看/搜索日程、创建/更新日程、管理参会人、查询忙闲状态及推荐空闲时段、查询/搜索与预定会议室。注意：涉及【预约日程/会议】或【查询/预定会议室】时，必须先读取 references/lark-calendar-schedule-meeting.md 工作流！高频操作请优先使用 Shortcuts：+agenda（快速概览今日/近期行程）、+create（创建日程并按需邀请参会人及预定会议室）、+freebusy（查询用户主日历的忙闲信息和rsvp的状态）、+rsvp（回复日程邀请） lark-calendar/SKILL.md local

### `lark-contact`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-contact/SKILL.md`
- 功能检索描述：飞书 / Lark 通讯录,用于按姓名 / 邮箱把员工解析成 open_id,以及按 open_id 反查员工的姓名 / 部门 / 邮箱 / 联系方式。当用户说出某人姓名而下一步需要发消息 / 加群 / 排日程时,先用本 skill 把姓名换成 ID;当输出里出现 open_id 需要展示成姓名给用户看,或用户直接询问某人的部门 / 邮箱 / 联系方式时,用本 skill 查。不负责部门树遍历、按部门列员工、组织架构图,这类需求走原生 OpenAPI。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-contact lark-contact 飞书 / Lark 通讯录,用于按姓名 / 邮箱把员工解析成 open_id,以及按 open_id 反查员工的姓名 / 部门 / 邮箱 / 联系方式。当用户说出某人姓名而下一步需要发消息 / 加群 / 排日程时,先用本 skill 把姓名换成 ID;当输出里出现 open_id 需要展示成姓名给用户看,或用户直接询问某人的部门 / 邮箱 / 联系方式时,用本 skill 查。不负责部门树遍历、按部门列员工、组织架构图,这类需求走原生 OpenAPI。 lark-contact/SKILL.md local

### `lark-doc`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-doc/SKILL.md`
- 功能检索描述：飞书云文档（v2）：创建和编辑飞书文档。使用本 skill 时，docs +create、docs +fetch、docs +update 必须携带 --api-version v2；默认使用 DocxXML 格式（也支持 Markdown）。创建文档、获取文档内容（支持 simple/with-ids/full 三种导出详细度，以及 full/outline/range/keyword/section 五种局部读取模式，可按目录、block id 区间、关键词或标题自动成节只拉部分内容以节省上下文）、更新文档（八种指令：str_replace/block_insert_after/block_copy_insert_after/block_replace/block_delete/block_move_after/overwrite/append）、上传和下载文档中的图片和文件、搜索云空间文档。当用户需要创建或编辑飞书文档、读取文档内容、在文档中插入图片、搜索云空间文档时使用；如果用户是想按名称或关键词先定位电子表格、报表等云空间对象，也优先使用本 skill 的 docs +search 做资源发现。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-doc docs (v2) 飞书云文档（v2）：创建和编辑飞书文档。使用本 skill 时，docs +create、docs +fetch、docs +update 必须携带 --api-version v2；默认使用 DocxXML 格式（也支持 Markdown）。创建文档、获取文档内容（支持 simple/with-ids/full 三种导出详细度，以及 full/outline/range/keyword/section 五种局部读取模式，可按目录、block id 区间、关键词或标题自动成节只拉部分内容以节省上下文）、更新文档（八种指令：str_replace/block_insert_after/block_copy_insert_after/block_replace/block_delete/block_move_after/overwrite/append）、上传和下载文档中的图片和文件、搜索云空间文档。当用户需要创建或编辑飞书文档、读取文档内容、在文档中插入图片、搜索云空间文档时使用；如果用户是想按名称或关键词先定位电子表格、报表等云空间对象，也优先使用本 skill 的 docs +search 做资源发现。 lark-doc/SKILL.md local

### `lark-drive`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-drive/SKILL.md`
- 功能检索描述：飞书云空间：管理云空间中的文件和文件夹。上传和下载文件、创建文件夹、复制/移动/删除文件、查看文件元数据、管理文档评论、管理文档权限、订阅用户评论变更事件、修改文件标题（docx、sheet、bitable、file、folder、wiki）；也负责把本地 Word/Markdown/Excel/CSV 以及 Base 快照（.base）导入为飞书在线云文档（docx、sheet、bitable）。当用户需要上传或下载文件、整理云空间目录、查看文件详情、管理评论、管理文档权限、修改文件标题、订阅用户评论变更事件，或要把本地文件导入成新版文档、电子表格、多维表格/Base 时使用。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-drive drive (v1) 飞书云空间：管理云空间中的文件和文件夹。上传和下载文件、创建文件夹、复制/移动/删除文件、查看文件元数据、管理文档评论、管理文档权限、订阅用户评论变更事件、修改文件标题（docx、sheet、bitable、file、folder、wiki）；也负责把本地 Word/Markdown/Excel/CSV 以及 Base 快照（.base）导入为飞书在线云文档（docx、sheet、bitable）。当用户需要上传或下载文件、整理云空间目录、查看文件详情、管理评论、管理文档权限、修改文件标题、订阅用户评论变更事件，或要把本地文件导入成新版文档、电子表格、多维表格/Base 时使用。 lark-drive/SKILL.md local

### `lark-event`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-event/SKILL.md`
- 功能检索描述：Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <EventKey>` (covers IM message receive, reactions, chat member changes, etc.). Use for Lark bots, real-time message processing, long-running subscribers, streaming webhook/push handlers. Supports `--max-events` / `--timeout` bounded runs and a stderr ready-marker contract — designed for AI agents running as subprocesses.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-event Lark Events Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via lark-cli event consume <EventKey> (covers IM message receive, reactions, chat member changes, etc.). Use for Lark bots, real-time message processing, long-running subscribers, streaming webhook/push handlers. Supports --max-events / --timeout bounded runs and a stderr ready-marker contract — designed for AI agents running as subprocesses. lark-event/SKILL.md local

### `lark-im`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-im/SKILL.md`
- 功能检索描述：飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、管理标记数据时使用。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-im im (v1) 飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、管理标记数据时使用。 lark-im/SKILL.md local

### `lark-mail`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-mail/SKILL.md`
- 功能检索描述：飞书邮箱 — draft, compose, send, reply, forward, read, and search emails; manage drafts, folders, labels, contacts, attachments, and mail rules. Use when user mentions 起草邮件, 写一封邮件, 拟邮件, 草稿, 发通知邮件, 发送邮件, 发邮件, 回复邮件, 转发邮件, 查看邮件, 看邮件, 读邮件, 搜索邮件, 查邮件, 收件箱, 邮件会话, 编辑草稿, 管理草稿, 下载附件, 邮件文件夹, 邮件标签, 邮件联系人, 监听新邮件, 收信规则, 邮件规则, draft, compose, send email, reply, forward, inbox, mail thread, mail rules.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-mail mail (v1) 飞书邮箱 — draft, compose, send, reply, forward, read, and search emails; manage drafts, folders, labels, contacts, attachments, and mail rules. Use when user mentions 起草邮件, 写一封邮件, 拟邮件, 草稿, 发通知邮件, 发送邮件, 发邮件, 回复邮件, 转发邮件, 查看邮件, 看邮件, 读邮件, 搜索邮件, 查邮件, 收件箱, 邮件会话, 编辑草稿, 管理草稿, 下载附件, 邮件文件夹, 邮件标签, 邮件联系人, 监听新邮件, 收信规则, 邮件规则, draft, compose, send email, reply, forward, inbox, mail thread, mail rules. lark-mail/SKILL.md local

### `lark-markdown`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-markdown/SKILL.md`
- 功能检索描述：飞书 Markdown：查看、创建、上传和编辑 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取或修改时使用。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-markdown markdown (v1) 飞书 Markdown：查看、创建、上传和编辑 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取或修改时使用。 lark-markdown/SKILL.md local

### `lark-minutes`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-minutes/SKILL.md`
- 功能检索描述：飞书妙记：妙记相关基本功能。1.查询妙记列表（按关键词/所有者/参与者/时间范围）；2.获取妙记基础信息（标题、封面、时长 等）；3.下载妙记音视频文件；4.获取妙记相关 AI 产物（总结、待办、章节）；5.上传音视频生成妙记，也支持将本地音视频文件转成纪要、逐字稿、文字稿、撰写文字等产物。遇到这类请求时，应优先使用本 skill，而不是尝试 `ffmpeg`、`whisper` 等本地转写命令。飞书妙记 URL 格式: http(s)://<host>/minutes/<minute-token>
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：lark-minutes minutes (v1) 飞书妙记：妙记相关基本功能。1.查询妙记列表（按关键词/所有者/参与者/时间范围）；2.获取妙记基础信息（标题、封面、时长 等）；3.下载妙记音视频文件；4.获取妙记相关 AI 产物（总结、待办、章节）；5.上传音视频生成妙记，也支持将本地音视频文件转成纪要、逐字稿、文字稿、撰写文字等产物。遇到这类请求时，应优先使用本 skill，而不是尝试 ffmpeg 、 whisper 等本地转写命令。飞书妙记 URL 格式: http(s)://<host>/minutes/<minute-token> lark-minutes/SKILL.md local

### `lark-okr`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-okr/SKILL.md`
- 功能检索描述：飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标（Objective）、关键结果（Key Result）、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-okr okr (v2) 飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标（Objective）、关键结果（Key Result）、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。 lark-okr/SKILL.md local

### `lark-openapi-explorer`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-openapi-explorer/SKILL.md`
- 功能检索描述：飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-openapi-explorer OpenAPI Explorer 飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时使用。 lark-openapi-explorer/SKILL.md local

### `lark-shared`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-shared/SKILL.md`
- 功能检索描述：飞书/Lark CLI 共享基础：应用配置初始化、认证登录（auth login）、身份切换（--as user/bot）、权限与 scope 管理、Permission denied 错误处理、安全规则。当用户需要第一次配置(`lark-cli config init`)、使用登录授权(`lark-cli auth login`)、遇到权限不足、切换 user/bot 身份、配置 scope、或首次使用 lark-cli 时触发。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-shared lark-cli 共享规则 飞书/Lark CLI 共享基础：应用配置初始化、认证登录（auth login）、身份切换（--as user/bot）、权限与 scope 管理、Permission denied 错误处理、安全规则。当用户需要第一次配置( lark-cli config init )、使用登录授权( lark-cli auth login )、遇到权限不足、切换 user/bot 身份、配置 scope、或首次使用 lark-cli 时触发。 lark-shared/SKILL.md local

### `lark-sheets`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-sheets/SKILL.md`
- 功能检索描述：飞书电子表格：创建和操作电子表格。支持创建表格、创建/复制/删除/更新工作表、读写单元格、追加行数据、查找内容、导出文件。当用户需要创建电子表格、管理工作表、批量读写数据、在已知表格中查找内容、导出或下载表格时使用。若用户是想按名称或关键词搜索云空间里的表格文件，请改用 lark-doc 的 docs +search 先定位资源。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：lark-sheets sheets (v3) 飞书电子表格：创建和操作电子表格。支持创建表格、创建/复制/删除/更新工作表、读写单元格、追加行数据、查找内容、导出文件。当用户需要创建电子表格、管理工作表、批量读写数据、在已知表格中查找内容、导出或下载表格时使用。若用户是想按名称或关键词搜索云空间里的表格文件，请改用 lark-doc 的 docs +search 先定位资源。 lark-sheets/SKILL.md local

### `lark-skill-maker`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-skill-maker/SKILL.md`
- 功能检索描述：创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-skill-maker Skill Maker 创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。 lark-skill-maker/SKILL.md local

### `lark-slides`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-slides/SKILL.md`
- 功能检索描述：飞书幻灯片：创建和编辑幻灯片，接口通过 XML 协议通信。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-slides slides (v1) 飞书幻灯片：创建和编辑幻灯片，接口通过 XML 协议通信。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。 lark-slides/SKILL.md local

### `lark-task`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-task/SKILL.md`
- 功能检索描述：飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务进度、管理项目清单或给他人分配任务、为任务上传附件文件、注册注销任务智能体、更新智能体主页数据、写入任务记录时使用。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-task task (v2) 飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务进度、管理项目清单或给他人分配任务、为任务上传附件文件、注册注销任务智能体、更新智能体主页数据、写入任务记录时使用。 lark-task/SKILL.md local

### `lark-vc`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-vc/SKILL.md`
- 功能检索描述：飞书视频会议：查询会议记录、获取会议纪要产物（总结、待办、章节、逐字稿）。1. 查询已经结束的会议数量或详情时使用本技能(如历史日期｜ 昨天 | 上周 | 今天已经开过的会议等场景)，查询未开始的会议日程使用 lark-calendar 技能。2. 支持通过关键词、时间范围、组织者、参与者、会议室等筛选条件搜索会议记录。3. 获取或整理会议纪要时使用本技能。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；音视频链接/文件、转录稿、会议纪要或内容处理需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：lark-vc vc (v1) 飞书视频会议：查询会议记录、获取会议纪要产物（总结、待办、章节、逐字稿）。1. 查询已经结束的会议数量或详情时使用本技能(如历史日期｜ 昨天 | 上周 | 今天已经开过的会议等场景)，查询未开始的会议日程使用 lark-calendar 技能。2. 支持通过关键词、时间范围、组织者、参与者、会议室等筛选条件搜索会议记录。3. 获取或整理会议纪要时使用本技能。 lark-vc/SKILL.md local

### `lark-whiteboard`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-whiteboard/SKILL.md`
- 功能检索描述：飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用 DSL（转成 OpenAPI 格式）、PlantUML/Mermaid 格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板，或是需要可视化表达架构、流程、组织关系、时间线、因果、对比等结构化信息时使用此 skill，无论是否提及"画板"。 ⚠️ 原 `lark-whiteboard-cli` skill 已合并至本 skill，若 skill 列表中同时存在 `lark-whiteboard-cli`，请忽略它，统一使用本 skill（`lark-whiteboard`），并提示用户运行 `npx skills remove lark-whiteboard-cli -g` 删除旧 skill。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-whiteboard 第一步：dry-run 探测 飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用 DSL（转成 OpenAPI 格式）、PlantUML/Mermaid 格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板，或是需要可视化表达架构、流程、组织关系、时间线、因果、对比等结构化信息时使用此 skill，无论是否提及"画板"。 ⚠️ 原 lark-whiteboard-cli skill 已合并至本 skill，若 skill 列表中同时存在 lark-whiteboard-cli ，请忽略它，统一使用本 skill（ lark-whiteboard ），并提示用户运行 npx skills remove lark-whiteboard-cli -g 删除旧 skill。 lark-whiteboard/SKILL.md local

### `lark-whiteboard-cli`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-whiteboard-cli/SKILL.md`
- 功能检索描述：当用户要求或使用飞书画板绘制架构图、流程图、思维导图、时序图或其他可视化图表时使用此 skill，作为使用 whiteboard-cli 设计图表布局的指南
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-whiteboard-cli 当用户要求或使用飞书画板绘制架构图、流程图、思维导图、时序图或其他可视化图表时使用此 skill，作为使用 whiteboard-cli 设计图表布局的指南 lark-whiteboard-cli/SKILL.md local

### `lark-wiki`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-wiki/SKILL.md`
- 功能检索描述：飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-wiki wiki (v2) 飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。 lark-wiki/SKILL.md local

### `lark-workflow-meeting-summary`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-workflow-meeting-summary/SKILL.md`
- 功能检索描述：会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-workflow-meeting-summary 会议纪要汇总工作流 会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。 lark-workflow-meeting-summary/SKILL.md local

### `lark-workflow-standup-report`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-workflow-standup-report/SKILL.md`
- 功能检索描述：日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：lark-workflow-standup-report 日程待办摘要工作流 日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。 lark-workflow-standup-report/SKILL.md local

