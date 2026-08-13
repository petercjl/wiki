---
title: Lark Agent Skill 注册页
type: concept
created: 2026-08-10
updated: 2026-08-10
domain: AI Agent工程
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
- 当前记录数量：41

归属分类统计：

- 系统/内置: 41

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 知识库 / 知识管理 / LLM Wiki

- `dws` (系统/内置 / local)：管理钉钉产品能力(AI表格/AI搜问/日历/通讯录/群聊与机器人/待办/审批/考勤/日志/DING消息/开放平台文档/钉钉文档/钉钉云盘/AI听记/邮箱/在线电子表格/知识库等)。当用户需要操作表格数据、管理日程会议、模糊找人/查谁负责某事…
- `lark-doc` (系统/内置 / local)：飞书云文档（Docx / Wiki 文档）：读取和编辑飞书文档内容。当用户给出文档 URL 或 token，或需要查看、创建、编辑文档、插入或下载文档图片附件时使用。文档中嵌入的电子表格、多维表格、画板，先用本 skill 提取 token…
- `lark-drive` (系统/内置 / local)：飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、评论/权限/订阅、标题、版本和本地文件导入。用户需要整理云盘目录、处理云空间资源 URL/token，或导入 Word/M…
- `lark-wiki` (系统/内置 / local)：飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出…

### 视觉 / 内容 / 课件生产

- `lark-apps` (系统/内置 / local)：妙搭（Spark/Miaoda）应用开发与托管：应用创建、HTML静态站点发布、本地全栈开发、云端生成迭代、AI相关能力和飞书平台能力或者其他外部能力集成、日志/Trace/监控指标/PV/UV 查询、环境变量管理。当用户要开发/新建一个系…
- `lark-event` (系统/内置 / local)：Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <Ev…
- `lark-im` (系统/内置 / local)：飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive Card）、监听卡片按钮回调（ca…
- `lark-sheets` (系统/内置 / local)：飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表、条件格式、筛选器、迷你图、浮动图片等对…
- `lark-slides` (系统/内置 / local)：飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/ URL/token 时，…
- `lark-whiteboard` (系统/内置 / local)：飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此 skill。不负责：飞书云文档内容编辑（lark-doc）、文档内嵌电子表…
- `sealseek-canvas` (系统/内置 / local)：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authen…
- `seedaudiocli` (系统/内置 / local)：Use the local `seedaudiocli` system CLI to generate audio with EvoLink Doubao Seed-Audio 1.0. Use when an Agent needs ba…
- `wecomcli-msg` (系统/内置 / local)：企业微信消息技能。提供会话列表查询、消息记录拉取（支持文本/图片/文件/语音/视频）、多媒体文件获取和文本消息发送能力。当用户需要"查看消息"、"看聊天记录"、"发消息给某人"、"最近有什么消息"、"给群里发消息"、"看看发了什么图片/文件…
- `workctl-operator` (系统/内置 / local)：安装、升级、认证、发现并使用 Work Agent CLI (`workctl`)。适用于通过 `workctl schema` 发现并调用阿里巴巴国际站商家经营工具，处理店铺经营数据、广告、发品、商品优化、AI 图片/视频、旺铺、选品、物…

### 电商 / 商品 / 品牌运营

- `international-station-seller-assistant` (系统/内置 / local)：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data throug…
- `lark-minutes` (系统/内置 / local)：飞书妙记：搜索妙记、查看妙记基础信息、下载/上传音视频、读取或编辑妙记的产物内容、改标题、替换说话人/关键词。当给出minute_token、本地音视频文件，要查/改/转妙记产物时使用；本地音视频转纪要/逐字稿优先走本 skill，不要用 …

### Agent 工程 / Skill / Plugin / MCP

- `lark-approval` (系统/内置 / local)：飞书审批：查询和处理审批待办/已办/实例，搜索可发起审批定义、查看定义详情并发起原生审批实例。当用户要处理审批任务、查看审批实例、搜索或发起审批时使用。审批待办不是飞书任务；非审批类待办走 lark-task。不负责创建审批定义；三方审批定…
- `lark-attendance` (系统/内置 / local)：飞书考勤打卡：查询自己的考勤打卡记录
- `lark-base` (系统/内置 / local)：飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、workflow、角色权限；遇到 Base/多维表格/bitable 或 /base/ 链接时使用。文件导入转 lark-drive，认证/授权转…
- `lark-calendar` (系统/内置 / local)：飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走 lark-vc）、待办任务（走 …
- `lark-contact` (系统/内置 / local)：飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名。当用户提到某人姓名要下一步发消息 / 排日程,或拿到 open_id 想查具体信息…
- `lark-mail` (系统/内置 / local)：飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for mail/email inten…
- `lark-markdown` (系统/内置 / local)：飞书 Markdown：查看、创建、上传、编辑和比较 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取、修改、局部 patch 或比较差异时使用。不负责将 Markdown 导入为飞书在线文档，也不负责文件搜索、权…
- `lark-note` (系统/内置 / local)：飞书会议纪要（Note）直查：已知 note_id 时查询纪要详情、展示类型、关联文档 token，并读取 unified 原始逐字记录。当用户已持有 note_id，或从文档显式 vc-node-id 获得 note_id 时使用。不负责…
- `lark-okr` (系统/内置 / local)：飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标、关键结果、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。不负责：待办任务管理（lark-task）、日程/会议安排（la…
- `lark-openapi-explorer` (系统/内置 / local)：飞书/Lark 原生 OpenAPI 探索：从官方文档库中挖掘未经 CLI 封装的原生 OpenAPI 接口。当用户的需求无法被现有 lark-* skill 或 lark-cli 已注册命令满足，需要查找并调用原生飞书 OpenAPI 时…
- `lark-shared` (系统/内置 / local)：Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain permissions (--domain…
- `lark-skill-maker` (系统/内置 / local)：创建 lark-cli 的自定义 Skill。当用户需要把飞书 API 操作封装成可复用的 Skill（包装原子 API 或编排多步流程）时使用。
- `lark-task` (系统/内置 / local)：飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查看任务列表、跟踪任务…
- `lark-vc` (系统/内置 / local)：飞书视频会议：搜索历史会议记录、查询会议纪要（总结/待办/章节/逐字稿）、查询参会人快照。当用户查询已结束的会议、获取会议产物（纪要/妙记）、查看参会人时使用；查询未来日程走 lark-calendar。不负责：Agent 真实入会/离会、…
- `lark-vc-agent` (系统/内置 / local)：飞书视频会议会中能力：用于让应用机器人真实加入或离开正在进行的会议，并读取当前身份可见的会中事件、发送会中文本消息或会中表情。适用于用户询问正在开的会议发生了什么、谁在发言、是否共享内容，或需要发现当前可读的进行中会议 ID。不负责已结束会…
- `lark-whiteboard-cli` (系统/内置 / local)：当用户要求或使用飞书画板绘制架构图、流程图、思维导图、时序图或其他可视化图表时使用此 skill，作为使用 whiteboard-cli 设计图表布局的指南
- `lark-workflow-meeting-summary` (系统/内置 / local)：会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。
- `lark-workflow-standup-report` (系统/内置 / local)：日程待办摘要：编排 calendar +agenda 和 task +get-my-tasks，生成指定日期的日程与未完成任务摘要。适用于了解今天/明天/本周的安排。
- `wecomcli-contact` (系统/内置 / local)：通讯录成员查询技能，获取当前用户可见范围内的通讯录成员，支持按姓名/别名本地筛选匹配。返回 userid、姓名和别名。⚠️ 仅返回当前用户有权限查看的成员，非全量成员。
- `wecomcli-doc` (系统/内置 / local)：企业微信文档、表格（在线表格）、智能表格和智能文档（原名智能主页）管理技能。提供文档的创建、读取、编辑能力，表格和智能表格的内容读取，智能表格的创建，以及智能文档的创建和内容导出。适用场景：(1) 以 Markdown 格式获取文档/表格/…
- `wecomcli-meeting` (系统/内置 / local)：企业微信会议技能，支持创建预约会议、查询会议列表、获取会议详情、取消会议、更新会议成员。当用户需要"创建会议"、"预约会议"、"约会议"、"安排会议"、"查看会议"、"查询会议列表"、"会议详情"、"什么时候开会"、"有哪些会议"、"查找会…
- `wecomcli-schedule` (系统/内置 / local)：企业微信日程管理技能。适用于用户对企业微信日程的各类管理需求。当用户需要：(1) 查询指定时间范围内的日程列表或获取日程详细信息（标题、时间、地点、参与者等），(2) 创建新日程并设置提醒、参与人等，(3) 修改已有日程的标题、时间、地点等…
- `wecomcli-smartsheet` (系统/内置 / local)：企业微信智能表格管理技能。提供智能表格的结构管理（子表、字段）和数据管理（记录增删改查）。适用场景：(1) 管理智能表格子表和字段/列 (2) 查询、添加、更新、删除智能表格记录。支持通过 docid 或文档 URL 定位文档。
- `wecomcli-todo` (系统/内置 / local)：企业微信待办事项管理技能，支持查询待办列表、获取待办详情、创建待办、更新待办、删除待办及变更用户处理进度状态。在用户说"看看我的待办列表"、"我有哪些待办"、"帮我创建一个待办"、"把这个任务分派给张三"、"标记待办完成"、"删掉那个待办"…
- `workctl` (系统/内置 / local)：管理 Work Agent 平台能力。通过 `workctl schema` 发现动态产品和命令，再用结构化输出执行操作。

## Skill 详情

### `dws`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.agents/skills/dws/SKILL.md`
- 功能检索描述：管理钉钉产品能力(AI表格/AI搜问/日历/通讯录/群聊与机器人/待办/审批/考勤/日志/DING消息/开放平台文档/钉钉文档/钉钉云盘/AI听记/邮箱/在线电子表格/知识库等)。当用户需要操作表格数据、管理日程会议、模糊找人/查谁负责某事项、查询通讯录、管理群聊、机器人发消息、创建待办、提交审批、查看考勤、提交日报周报（钉钉日志模版）、读写钉钉文档、上传下载云盘文件、查询听记纪要、收发邮件、读写在线电子表格(axls)、管理钉钉知识库时使用。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：dws 钉钉全产品 Skill 管理钉钉产品能力(AI表格/AI搜问/日历/通讯录/群聊与机器人/待办/审批/考勤/日志/DING消息/开放平台文档/钉钉文档/钉钉云盘/AI听记/邮箱/在线电子表格/知识库等)。当用户需要操作表格数据、管理日程会议、模糊找人/查谁负责某事项、查询通讯录、管理群聊、机器人发消息、创建待办、提交审批、查看考勤、提交日报周报（钉钉日志模版）、读写钉钉文档、上传下载云盘文件、查询听记纪要、收发邮件、读写在线电子表格(axls)、管理钉钉知识库时使用。 dws/SKILL.md local

### `international-station-seller-assistant`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.agents/skills/international-station-seller-assistant/SKILL.md`
- 功能检索描述：Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl CLI, including 店铺经营数据, 询盘, TM/IM conversations, 客服诊断, 广告, 商品, 发品, 选品, RFQ, 物流, 交易, 旺铺, or 国际站生意助手 workflows.
- 输入 / 触发方式：电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：international-station-seller-assistant International Station Seller Assistant Use when Peter asks to query, analyze, diagnose, export, or operate Alibaba.com International Station seller data through the system workctl CLI, including 店铺经营数据, 询盘, TM/IM conversations, 客服诊断, 广告, 商品, 发品, 选品, RFQ, 物流, 交易, 旺铺, or 国际站生意助手 workflows. international-station-seller-assistant/SKILL.md local

### `lark-approval`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-approval/SKILL.md`
- 功能检索描述：飞书审批：查询和处理审批待办/已办/实例，搜索可发起审批定义、查看定义详情并发起原生审批实例。当用户要处理审批任务、查看审批实例、搜索或发起审批时使用。审批待办不是飞书任务；非审批类待办走 lark-task。不负责创建审批定义；三方审批定义不走原生提单。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-approval 飞书审批：查询和处理审批待办/已办/实例，搜索可发起审批定义、查看定义详情并发起原生审批实例。当用户要处理审批任务、查看审批实例、搜索或发起审批时使用。审批待办不是飞书任务；非审批类待办走 lark-task。不负责创建审批定义；三方审批定义不走原生提单。 lark-approval/SKILL.md local

### `lark-apps`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-apps/SKILL.md`
- 功能检索描述：妙搭（Spark/Miaoda）应用开发与托管：应用创建、HTML静态站点发布、本地全栈开发、云端生成迭代、AI相关能力和飞书平台能力或者其他外部能力集成、日志/Trace/监控指标/PV/UV 查询、环境变量管理。当用户要开发/新建一个系统·工具·平台·应用，或要本地开发 / 云端开发 / 修改 / 部署 / 发布 / 上线 / 拿可分享链接，或用 HTML 做页面·网站·部署到妙搭，或提到妙搭/Spark/Miaoda（应用运行时域名形如 *.aiforce.cloud）、应用数据库、应用文件存储、开放 API Key、可见范围、线上日志、接口请求量、错误量、延迟、访问量、环境变量时使用。不负责普通云盘文件上传（lark-drive）、飞书文档编辑（lark-doc）、原生幻灯片创建（lark-slides）。
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-apps apps (v1) 妙搭（Spark/Miaoda）应用开发与托管：应用创建、HTML静态站点发布、本地全栈开发、云端生成迭代、AI相关能力和飞书平台能力或者其他外部能力集成、日志/Trace/监控指标/PV/UV 查询、环境变量管理。当用户要开发/新建一个系统·工具·平台·应用，或要本地开发 / 云端开发 / 修改 / 部署 / 发布 / 上线 / 拿可分享链接，或用 HTML 做页面·网站·部署到妙搭，或提到妙搭/Spark/Miaoda（应用运行时域名形如 *.aiforce.cloud）、应用数据库、应用文件存储、开放 API Key、可见范围、线上日志、接口请求量、错误量、延迟、访问量、环境变量时使用。不负责普通云盘文件上传（lark-drive）、飞书文档编辑（lark-doc）、原生幻灯片创建（lark-slides）。 lark-apps/SKILL.md local

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
- 功能检索描述：飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、workflow、角色权限；遇到 Base/多维表格/bitable 或 /base/ 链接时使用。文件导入转 lark-drive，认证/授权转 lark-shared。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-base base 飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、workflow、角色权限；遇到 Base/多维表格/bitable 或 /base/ 链接时使用。文件导入转 lark-drive，认证/授权转 lark-shared。 lark-base/SKILL.md local

### `lark-calendar`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-calendar/SKILL.md`
- 功能检索描述：飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走 lark-vc）、待办任务（走 lark-task）。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：lark-calendar calendar (v4) 飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走 lark-vc）、待办任务（走 lark-task）。 lark-calendar/SKILL.md local

### `lark-contact`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-contact/SKILL.md`
- 功能检索描述：飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名。当用户提到某人姓名要下一步发消息 / 排日程,或拿到 open_id 想查具体信息时使用。不负责部门树遍历、按部门列员工、组织架构图,这类需求走原生 OpenAPI。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-contact 飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名。当用户提到某人姓名要下一步发消息 / 排日程,或拿到 open_id 想查具体信息时使用。不负责部门树遍历、按部门列员工、组织架构图,这类需求走原生 OpenAPI。 lark-contact/SKILL.md local

### `lark-doc`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-doc/SKILL.md`
- 功能检索描述：飞书云文档（Docx / Wiki 文档）：读取和编辑飞书文档内容。当用户给出文档 URL 或 token，或需要查看、创建、编辑文档、插入或下载文档图片附件时使用。文档中嵌入的电子表格、多维表格、画板，先用本 skill 提取 token 再切到对应 skill。当用户给出 doubao.com 的 /docx/ 或 /wiki/ URL/token 时，也应直接使用本 skill；路由依据是 URL 路径模式和 token，而不是域名。不负责文档评论管理，也不负责表格或 Base 的数据操作。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：lark-doc docs 飞书云文档（Docx / Wiki 文档）：读取和编辑飞书文档内容。当用户给出文档 URL 或 token，或需要查看、创建、编辑文档、插入或下载文档图片附件时使用。文档中嵌入的电子表格、多维表格、画板，先用本 skill 提取 token 再切到对应 skill。当用户给出 doubao.com 的 /docx/ 或 /wiki/ URL/token 时，也应直接使用本 skill；路由依据是 URL 路径模式和 token，而不是域名。不负责文档评论管理，也不负责表格或 Base 的数据操作。 lark-doc/SKILL.md local

### `lark-drive`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-drive/SKILL.md`
- 功能检索描述：飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、评论/权限/订阅、标题、版本和本地文件导入。用户需要整理云盘目录、处理云空间资源 URL/token，或导入 Word/Markdown/Excel/CSV/PPTX/.base 为 docx/sheet/bitable/slides 时使用；doubao.com 云空间 URL/token 也按资源路径和 token 路由，不回退 WebFetch。不负责：文档内容编辑（走 lark-doc）、表格/Base 表内数据操作（走 lark-sheets/lark-base）、知识空间节点/成员管理（走 lark-wiki）、原生 Markdown 文件读写/patch/diff（走 lark-markdown）。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：lark-drive drive (v1) 飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、评论/权限/订阅、标题、版本和本地文件导入。用户需要整理云盘目录、处理云空间资源 URL/token，或导入 Word/Markdown/Excel/CSV/PPTX/.base 为 docx/sheet/bitable/slides 时使用；doubao.com 云空间 URL/token 也按资源路径和 token 路由，不回退 WebFetch。不负责：文档内容编辑（走 lark-doc）、表格/Base 表内数据操作（走 lark-sheets/lark-base）、知识空间节点/成员管理（走 lark-wiki）、原生 Markdown 文件读写/patch/diff（走 lark-markdown）。 lark-drive/SKILL.md local

### `lark-event`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-event/SKILL.md`
- 功能检索描述：Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event consume <EventKey>` (covers IM messages/reactions/chat changes, Task updates, VC meeting started/joined/ended, Minutes generated, Whiteboard updated, etc.). Use for Lark bots, real-time message processing, long-running subscribers, streaming webhook/push handlers. Supports `--max-events` / `--timeout` bounded runs and a stderr ready-marker contract — designed for AI agents running as subprocesses.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：lark-event Lark Events Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via lark-cli event consume <EventKey> (covers IM messages/reactions/chat changes, Task updates, VC meeting started/joined/ended, Minutes generated, Whiteboard updated, etc.). Use for Lark bots, real-time message processing, long-running subscribers, streaming webhook/push handlers. Supports --max-events / --timeout bounded runs and a stderr ready-marker contract — designed for AI agents running as subprocesses. lark-event/SKILL.md local

### `lark-im`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-im/SKILL.md`
- 功能检索描述：飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive Card）、监听卡片按钮回调（card.action.trigger）。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、搜索群、创建群聊或话题群、管理标记数据、管理 Feed 置顶（添加/移除/查询置顶会话）、管理标签数据、处理卡片回调时使用。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-im im (v1) 飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件（支持大文件分片下载）、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive Card）、监听卡片按钮回调（card.action.trigger）。当用户需要发消息、查看或搜索聊天记录、下载聊天中的文件、查看群成员、搜索群、创建群聊或话题群、管理标记数据、管理 Feed 置顶（添加/移除/查询置顶会话）、管理标签数据、处理卡片回调时使用。 lark-im/SKILL.md local

### `lark-mail`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-mail/SKILL.md`
- 功能检索描述：飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for mail/email intent only. Do not use for docs/sheets/calendar/auth setup/pure contact lookup/IM chat tasks.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-mail mail (v1) 飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for mail/email intent only. Do not use for docs/sheets/calendar/auth setup/pure contact lookup/IM chat tasks. lark-mail/SKILL.md local

### `lark-markdown`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-markdown/SKILL.md`
- 功能检索描述：飞书 Markdown：查看、创建、上传、编辑和比较 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取、修改、局部 patch 或比较差异时使用。不负责将 Markdown 导入为飞书在线文档，也不负责文件搜索、权限、评论、移动、删除等云空间管理操作。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-markdown markdown (v1) 飞书 Markdown：查看、创建、上传、编辑和比较 Markdown 文件。当用户需要创建或编辑 Markdown 文件、读取、修改、局部 patch 或比较差异时使用。不负责将 Markdown 导入为飞书在线文档，也不负责文件搜索、权限、评论、移动、删除等云空间管理操作。 lark-markdown/SKILL.md local

### `lark-minutes`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-minutes/SKILL.md`
- 功能检索描述：飞书妙记：搜索妙记、查看妙记基础信息、下载/上传音视频、读取或编辑妙记的产物内容、改标题、替换说话人/关键词。当给出minute_token、本地音视频文件，要查/改/转妙记产物时使用；本地音视频转纪要/逐字稿优先走本 skill，不要用 ffmpeg/whisper 本地转写。不负责：获取会议关联妙记，或仅按自然语言标题定位纪要
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：lark-minutes minutes (v1) 飞书妙记：搜索妙记、查看妙记基础信息、下载/上传音视频、读取或编辑妙记的产物内容、改标题、替换说话人/关键词。当给出minute_token、本地音视频文件，要查/改/转妙记产物时使用；本地音视频转纪要/逐字稿优先走本 skill，不要用 ffmpeg/whisper 本地转写。不负责：获取会议关联妙记，或仅按自然语言标题定位纪要 lark-minutes/SKILL.md local

### `lark-note`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-note/SKILL.md`
- 功能检索描述：飞书会议纪要（Note）直查：已知 note_id 时查询纪要详情、展示类型、关联文档 token，并读取 unified 原始逐字记录。当用户已持有 note_id，或从文档显式 vc-node-id 获得 note_id 时使用。不负责会议/日程/妙记定位、文档标题搜索或 Docx 正文读取。
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-note note (v1) 飞书会议纪要（Note）直查：已知 note_id 时查询纪要详情、展示类型、关联文档 token，并读取 unified 原始逐字记录。当用户已持有 note_id，或从文档显式 vc-node-id 获得 note_id 时使用。不负责会议/日程/妙记定位、文档标题搜索或 Docx 正文读取。 lark-note/SKILL.md local

### `lark-okr`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-okr/SKILL.md`
- 功能检索描述：飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标、关键结果、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。不负责：待办任务管理（lark-task）、日程/会议安排（lark-calendar）、绩效评估
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-okr okr (v2) 飞书 OKR：管理目标与关键结果。查看和编辑 OKR 周期、目标、关键结果、对齐关系、量化指标和进展记录。当用户需要查看或创建 OKR、管理目标和关键结果、查看对齐关系时使用。不负责：待办任务管理（lark-task）、日程/会议安排（lark-calendar）、绩效评估 lark-okr/SKILL.md local

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
- 功能检索描述：Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain permissions (--domain, including all/docs/drive), missing scopes, revoking authorization, or handling _notice JSON.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-shared lark-cli 共享规则 Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain permissions (--domain, including all/docs/drive), missing scopes, revoking authorization, or handling _notice JSON. lark-shared/SKILL.md local

### `lark-sheets`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-sheets/SKILL.md`
- 功能检索描述：飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表、条件格式、筛选器、迷你图、浮动图片等对象的创建与维护。当用户需要创建电子表格、管理工作表、批量读写或编辑数据、统计汇总与可视化、表格美化、公式计算（含 Excel 公式迁移）、金融/财务建模（DCF、三张表、预算、Sensitivity 等）等任务时使用。若用户是想按名称或关键词搜索云空间（云盘/云存储）里的表格文件，请改用 lark-drive 的 drive +search 先定位资源。当用户给出 doubao.com 的 /sheets/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：lark-sheets sheets 飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表、条件格式、筛选器、迷你图、浮动图片等对象的创建与维护。当用户需要创建电子表格、管理工作表、批量读写或编辑数据、统计汇总与可视化、表格美化、公式计算（含 Excel 公式迁移）、金融/财务建模（DCF、三张表、预算、Sensitivity 等）等任务时使用。若用户是想按名称或关键词搜索云空间（云盘/云存储）里的表格文件，请改用 lark-drive 的 drive +search 先定位资源。当用户给出 doubao.com 的 /sheets/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。 lark-sheets/SKILL.md local

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
- 功能检索描述：飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。不负责：云文档内容编辑（走 lark-doc）、云文档里的独立画板对象（走 lark-whiteboard，注意 slide 内嵌的流程图/架构图仍属本 skill）、上传或下载普通文件（走 lark-drive）。
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；API 文档 URL、接口规格、鉴权/参数/示例需求；已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-slides slides (v1) 飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。不负责：云文档内容编辑（走 lark-doc）、云文档里的独立画板对象（走 lark-whiteboard，注意 slide 内嵌的流程图/架构图仍属本 skill）、上传或下载普通文件（走 lark-drive）。 lark-slides/SKILL.md local

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
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-vc/SKILL.md`
- 功能检索描述：飞书视频会议：搜索历史会议记录、查询会议纪要（总结/待办/章节/逐字稿）、查询参会人快照。当用户查询已结束的会议、获取会议产物（纪要/妙记）、查看参会人时使用；查询未来日程走 lark-calendar。不负责：Agent 真实入会/离会、会中实时事件（走 lark-vc-agent）。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：lark-vc vc (v1) 飞书视频会议：搜索历史会议记录、查询会议纪要（总结/待办/章节/逐字稿）、查询参会人快照。当用户查询已结束的会议、获取会议产物（纪要/妙记）、查看参会人时使用；查询未来日程走 lark-calendar。不负责：Agent 真实入会/离会、会中实时事件（走 lark-vc-agent）。 lark-vc/SKILL.md local

### `lark-vc-agent`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-vc-agent/SKILL.md`
- 功能检索描述：飞书视频会议会中能力：用于让应用机器人真实加入或离开正在进行的会议，并读取当前身份可见的会中事件、发送会中文本消息或会中表情。适用于用户询问正在开的会议发生了什么、谁在发言、是否共享内容，或需要发现当前可读的进行中会议 ID。不负责已结束会议搜索、参会人快照、纪要、逐字稿或录制查询，这些使用 lark-vc 技能。
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：lark-vc-agent vc-agent (v1) 飞书视频会议会中能力：用于让应用机器人真实加入或离开正在进行的会议，并读取当前身份可见的会中事件、发送会中文本消息或会中表情。适用于用户询问正在开的会议发生了什么、谁在发言、是否共享内容，或需要发现当前可读的进行中会议 ID。不负责已结束会议搜索、参会人快照、纪要、逐字稿或录制查询，这些使用 lark-vc 技能。 lark-vc-agent/SKILL.md local

### `lark-whiteboard`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/lark-whiteboard/SKILL.md`
- 功能检索描述：飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此 skill。不负责：飞书云文档内容编辑（lark-doc）、文档内嵌电子表格/Base（lark-sheets / lark-base）。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-whiteboard 飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此 skill。不负责：飞书云文档内容编辑（lark-doc）、文档内嵌电子表格/Base（lark-sheets / lark-base）。 lark-whiteboard/SKILL.md local

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
- 功能检索描述：飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出 doubao.com 的 /wiki/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。不负责：上传文件到知识库节点下（走 lark-drive）、编辑文档/表格/Base 内容（走 lark-doc / lark-sheets / lark-base）。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：lark-wiki wiki (v2) 飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出 doubao.com 的 /wiki/ URL/token 时，也应直接使用本 skill，不要因为域名不是飞书而回退到 WebFetch；路由依据是 URL 路径模式和 token，而不是域名。不负责：上传文件到知识库节点下（走 lark-drive）、编辑文档/表格/Base 内容（走 lark-doc / lark-sheets / lark-base）。 lark-wiki/SKILL.md local

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

### `sealseek-canvas`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/sealseek-canvas/SKILL.md`
- 功能检索描述：Operate SealSeek Infinite Canvas through the browserless-capable `sealseek-canvas` CLI. Use when the user asks to authenticate, create or manage an 无限画板, generate/retrieve/place/arrange `gpt-image-2` images, generate/retrieve/place `seedance2-0` videos, add explanatory text, inspect supported parameters, download assets, or lay out labeled media tightly in blank board space. Prefer this CLI over browser clicking, Agent-mode generation, or ad hoc HTTP calls.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：sealseek-canvas SealSeek Infinite Canvas CLI Operate SealSeek Infinite Canvas through the browserless-capable sealseek-canvas CLI. Use when the user asks to authenticate, create or manage an 无限画板, generate/retrieve/place/arrange gpt-image-2 images, generate/retrieve/place seedance2-0 videos, add explanatory text, inspect supported parameters, download assets, or lay out labeled media tightly in blank board space. Prefer this CLI over browser clicking, Agent-mode generation, or ad hoc HTTP calls. sealseek-canvas/SKILL.md local

### `seedaudiocli`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/seedaudiocli/SKILL.md`
- 功能检索描述：Use the local `seedaudiocli` system CLI to generate audio with EvoLink Doubao Seed-Audio 1.0. Use when an Agent needs background music, product-video BGM, speech, voice/preset audio, reference-audio voice cloning, reference-image-guided audio, task polling, or downloading generated Seed Audio files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：seedaudiocli Seed Audio CLI Use the local seedaudiocli system CLI to generate audio with EvoLink Doubao Seed-Audio 1.0. Use when an Agent needs background music, product-video BGM, speech, voice/preset audio, reference-audio voice cloning, reference-image-guided audio, task polling, or downloading generated Seed Audio files. seedaudiocli/SKILL.md local

### `wecomcli-contact`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/wecomcli-contact/SKILL.md`
- 功能检索描述：通讯录成员查询技能，获取当前用户可见范围内的通讯录成员，支持按姓名/别名本地筛选匹配。返回 userid、姓名和别名。⚠️ 仅返回当前用户有权限查看的成员，非全量成员。
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：wecomcli-contact 通讯录成员查询技能 通讯录成员查询技能，获取当前用户可见范围内的通讯录成员，支持按姓名/别名本地筛选匹配。返回 userid、姓名和别名。⚠️ 仅返回当前用户有权限查看的成员，非全量成员。 wecomcli-contact/SKILL.md local

### `wecomcli-doc`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/wecomcli-doc/SKILL.md`
- 功能检索描述：企业微信文档、表格（在线表格）、智能表格和智能文档（原名智能主页）管理技能。提供文档的创建、读取、编辑能力，表格和智能表格的内容读取，智能表格的创建，以及智能文档的创建和内容导出。适用场景：(1) 以 Markdown 格式获取文档/表格/智能表格完整内容 (2) 新建文档或智能表格 (3) 用 Markdown 格式覆写文档内容 (4) 创建智能文档，将本地 Markdown 文件发布为智能文档 (5) 导出智能文档内容为 Markdown。支持通过 docid 或文档 URL 定位文档。用户提及 `https://doc.weixin.qq.com/xxxx` 格式的URL链接时，触发该技能。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：wecomcli-doc 企业微信文档管理 企业微信文档、表格（在线表格）、智能表格和智能文档（原名智能主页）管理技能。提供文档的创建、读取、编辑能力，表格和智能表格的内容读取，智能表格的创建，以及智能文档的创建和内容导出。适用场景：(1) 以 Markdown 格式获取文档/表格/智能表格完整内容 (2) 新建文档或智能表格 (3) 用 Markdown 格式覆写文档内容 (4) 创建智能文档，将本地 Markdown 文件发布为智能文档 (5) 导出智能文档内容为 Markdown。支持通过 docid 或文档 URL 定位文档。用户提及 https://doc.weixin.qq.com/xxxx 格式的URL链接时，触发该技能。 wecomcli-doc/SKILL.md local

### `wecomcli-meeting`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/wecomcli-meeting/SKILL.md`
- 功能检索描述：企业微信会议技能，支持创建预约会议、查询会议列表、获取会议详情、取消会议、更新会议成员。当用户需要"创建会议"、"预约会议"、"约会议"、"安排会议"、"查看会议"、"查询会议列表"、"会议详情"、"什么时候开会"、"有哪些会议"、"查找会议"、"取消会议"、"删除会议"、"修改会议成员"、"添加会议参与人"、"移除会议成员"时触发。
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：wecomcli-meeting 企业微信会议技能 企业微信会议技能，支持创建预约会议、查询会议列表、获取会议详情、取消会议、更新会议成员。当用户需要"创建会议"、"预约会议"、"约会议"、"安排会议"、"查看会议"、"查询会议列表"、"会议详情"、"什么时候开会"、"有哪些会议"、"查找会议"、"取消会议"、"删除会议"、"修改会议成员"、"添加会议参与人"、"移除会议成员"时触发。 wecomcli-meeting/SKILL.md local

### `wecomcli-msg`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/wecomcli-msg/SKILL.md`
- 功能检索描述：企业微信消息技能。提供会话列表查询、消息记录拉取（支持文本/图片/文件/语音/视频）、多媒体文件获取和文本消息发送能力。当用户需要"查看消息"、"看聊天记录"、"发消息给某人"、"最近有什么消息"、"给群里发消息"、"看看发了什么图片/文件"时触发。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：wecomcli-msg 企业微信消息技能 企业微信消息技能。提供会话列表查询、消息记录拉取（支持文本/图片/文件/语音/视频）、多媒体文件获取和文本消息发送能力。当用户需要"查看消息"、"看聊天记录"、"发消息给某人"、"最近有什么消息"、"给群里发消息"、"看看发了什么图片/文件"时触发。 wecomcli-msg/SKILL.md local

### `wecomcli-schedule`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/wecomcli-schedule/SKILL.md`
- 功能检索描述：企业微信日程管理技能。适用于用户对企业微信日程的各类管理需求。当用户需要：(1) 查询指定时间范围内的日程列表或获取日程详细信息（标题、时间、地点、参与者等），(2) 创建新日程并设置提醒、参与人等，(3) 修改已有日程的标题、时间、地点等信息或取消日程，(4) 添加或移除日程参与人，(5) 查询多个成员的闲忙状态并分析共同空闲时段以安排会议时使用此技能。
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：wecomcli-schedule 企业微信日程管理技能 企业微信日程管理技能。适用于用户对企业微信日程的各类管理需求。当用户需要：(1) 查询指定时间范围内的日程列表或获取日程详细信息（标题、时间、地点、参与者等），(2) 创建新日程并设置提醒、参与人等，(3) 修改已有日程的标题、时间、地点等信息或取消日程，(4) 添加或移除日程参与人，(5) 查询多个成员的闲忙状态并分析共同空闲时段以安排会议时使用此技能。 wecomcli-schedule/SKILL.md local

### `wecomcli-smartsheet`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/wecomcli-smartsheet/SKILL.md`
- 功能检索描述：企业微信智能表格管理技能。提供智能表格的结构管理（子表、字段）和数据管理（记录增删改查）。适用场景：(1) 管理智能表格子表和字段/列 (2) 查询、添加、更新、删除智能表格记录。支持通过 docid 或文档 URL 定位文档。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：wecomcli-smartsheet 企业微信智能表格管理 企业微信智能表格管理技能。提供智能表格的结构管理（子表、字段）和数据管理（记录增删改查）。适用场景：(1) 管理智能表格子表和字段/列 (2) 查询、添加、更新、删除智能表格记录。支持通过 docid 或文档 URL 定位文档。 wecomcli-smartsheet/SKILL.md local

### `wecomcli-todo`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/wecomcli-todo/SKILL.md`
- 功能检索描述：企业微信待办事项管理技能，支持查询待办列表、获取待办详情、创建待办、更新待办、删除待办及变更用户处理进度状态。在用户说"看看我的待办列表"、"我有哪些待办"、"帮我创建一个待办"、"把这个任务分派给张三"、"标记待办完成"、"删掉那个待办"、"帮我建个提醒"、"更新一下待办内容"、"把提醒时间改到下周"、"接受这个待办"、"拒绝这个待办"、"这个待办的详情"、"待办分派给谁了"等需要对待办进行读写操作的场景时使用。
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：wecomcli-todo 企业微信待办事项管理技能 企业微信待办事项管理技能，支持查询待办列表、获取待办详情、创建待办、更新待办、删除待办及变更用户处理进度状态。在用户说"看看我的待办列表"、"我有哪些待办"、"帮我创建一个待办"、"把这个任务分派给张三"、"标记待办完成"、"删掉那个待办"、"帮我建个提醒"、"更新一下待办内容"、"把提醒时间改到下周"、"接受这个待办"、"拒绝这个待办"、"这个待办的详情"、"待办分派给谁了"等需要对待办进行读写操作的场景时使用。 wecomcli-todo/SKILL.md local

### `workctl`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.agents/skills/workctl/SKILL.md`
- 功能检索描述：管理 Work Agent 平台能力。通过 `workctl schema` 发现动态产品和命令，再用结构化输出执行操作。
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：workctl Work Agent CLI Skill 管理 Work Agent 平台能力。通过 workctl schema 发现动态产品和命令，再用结构化输出执行操作。 workctl/SKILL.md local

### `workctl-operator`

- Agent / 环境：Lark Agent
- 归属分类：系统/内置
- 归属依据：Lark/Feishu 通用工具 skill，视为底层工具能力。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.agents/skills/workctl/workctl-operator/SKILL.md`
- 功能检索描述：安装、升级、认证、发现并使用 Work Agent CLI (`workctl`)。适用于通过 `workctl schema` 发现并调用阿里巴巴国际站商家经营工具，处理店铺经营数据、广告、发品、商品优化、AI 图片/视频、旺铺、选品、物流、交易、IM、知识问答、深度研究等场景。 也适用于配置 workctl、登录认证、排查 token/cache/schema/runtime/async task/recovery 问题，编排多个 workctl 工具，或为新业务域接入 registry/discovery/detail/tools/call 协议。执行业务命令时必须以当前 `workctl schema` 和 `workctl <command> --help` 为准，不照搬旧 MCP/CLI 命令。
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：workctl-operator Workctl Operator 安装、升级、认证、发现并使用 Work Agent CLI ( workctl )。适用于通过 workctl schema 发现并调用阿里巴巴国际站商家经营工具，处理店铺经营数据、广告、发品、商品优化、AI 图片/视频、旺铺、选品、物流、交易、IM、知识问答、深度研究等场景。 也适用于配置 workctl、登录认证、排查 token/cache/schema/runtime/async task/recovery 问题，编排多个 workctl 工具，或为新业务域接入 registry/discovery/detail/tools/call 协议。执行业务命令时必须以当前 workctl schema 和 workctl <command> --help 为准，不照搬旧 MCP/CLI 命令。 workctl/workctl-operator/SKILL.md local

