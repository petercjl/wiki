---
title: 飞书文档「资产构建：角色定调与场景搭建」覆盖清单
type: source-summary
created: 2026-07-07
updated: 2026-07-07
domain: meta
tags: [llm-wiki, visual-production, ai-video]
sources:
  - raw/webpages/feishu-ai-short-drama-assets-2026-07-07/section-asset-construction.md
status: active
---

# 飞书文档「资产构建：角色定调与场景搭建」覆盖清单

## Source Profile

- source title: 飞书文档章节「二、资产构建：角色定调与场景搭建」
- original URL: https://tcndype5nozr.feishu.cn/docx/KTILdGRvhox7OJxodK5cotzenEd
- captured section: `doxcnINbZiE7MjDBCWFBSZeA9Ve`
- capture date: 2026-07-07
- adapter: `markdown-doc` over Feishu Docx fetch
- domain placement: `domains/视觉制作/06-AI视频/`
- fusion disposition: create a focused playbook and cross-link existing [[domains/视觉制作/06-AI视频/07-故事板铁三角AI视频控制法|AI视频控制资产系统]]
- tool handling: LibTV、即梦等平台步骤不作为固定工具依赖，只抽象为模型选择、参考图输入、多角度资产生成、质量门和审核门。

## Source Inventory

- 章节主线：从剧本/小说抽取角色、场景、道具资产，而不是先写外貌 prompt。
- 角色设计：人物小传、男频/女频受众差异、AI 辅助提取人物信息、提示词模板。
- 执行层工具：LibTV、即梦、Seedream、Nano Banana、Z-image、GPT Image 2 等模型/平台对比。
- 角色常见问题：服装造型不搭、比例问题、美观度问题、背景/手持物污染。
- 角色视图资产：正面全身图、脸部特写、三视图/四视图、真人审核/合规校验。
- 场景设计：先列场景库，再按景别、正反打、无人物、全景/四宫格、多角度和反打生成。
- 道具设计：纯白底、无人物、符合时代气质、避免现代元素和简体字污染。
- 作业/交付：剧本梗概、角色四视图、核心场景图、道具图。

## Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | 标题与小结 | 资产构建不是工具教程，而是把影视/动画资产方法迁移到 AI 短剧生产线 | core principle | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 作为页面总论 |
| S02 | 一）角色设计/先了解故事 | 先故事再人物，人物小传包含身份位置、性格反差、欲望困境、关系网络、视觉暗示 | method | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 转为角色资产协议 |
| S03 | 男频与女频 | 受众爽点决定角色视觉方向：男频偏力量/爽感/等级压制，女频偏情绪/氛围/关系 | decision rule | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 转为受众-视觉映射表 |
| S04 | AI辅助提取人物信息 | 从剧本抽取人物、场景、道具，再生成中英提示词 | workflow | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 改写为可由 API/Skill 实现的信息抽取节点 |
| S05 | 资产图生成工具 | LibTV/即梦等平台选择图片模型、比例和分辨率 | execution layer | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | merged | 抽象为模型路由、画幅协议和批量候选生成 |
| S06 | 不同模型生成效果 | 不同模型在审美、真实感、地域/风格理解和成本上不同，哪个效果好用哪个 | model selection | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 动态模型路由原则，不固化平台 |
| S07 | 角色设计常见问题 | 服化道、比例、审美、表情、背景、手持物、刻板印象需要人工审美与 QA | QA | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 转为失败模式与修正表 |
| S08 | 三视图及四视图 | 正面全身图之后生成脸部特写 + 正侧背三视图，纯白背景、统一风格 | asset spec | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 与身份板知识交叉链接 |
| S09 | 场景设计 | 场景是空间化叙事工具，先列剧本场景库，再决定全景、正反打、四宫格和无人物图 | asset spec | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 转为场景资产协议 |
| S10 | 多宫格/全景/反打 | 四宫格用于同一空间多视角，全景适合室外，反打靠视觉锚点、前中背景和视线关系 | spatial control | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 抽象为 API/Skill 节点 |
| S11 | 道具资产设计 | 道具纯白底、无人物、符合时代气质，避免现代元素和简体字 | asset spec | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 转为道具资产协议 |
| S12 | 作业 | 交付包含剧本梗概、角色四视图、核心场景、道具图 | output contract | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | formalized | 转为 Agent 输出包 |
| S13 | 图片与工具界面截图 | 平台按钮、界面高亮和示范截图 | evidence | raw/webpages/feishu-ai-short-drama-assets-2026-07-07/section-asset-construction.md | raw-only | 工具界面不作为当前执行依赖；图片说明已保留在 raw |
| S14 | 具体平台审核规则 | LibTV/即梦真人审核差异 | current-sensitive | [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]] | merged | 仅保留“审核/合规门”原则；具体规则需按当前平台复核 |

## Omission Audit

- `raw-only`: 平台按钮路径、界面截图、模型商品名映射和价格/审核描述，原因是这些属于工具 UI 与时效信息，且用户明确不使用这些工具。
- `omitted-with-reason`: 无。原章节的可复用方法均已进入正式页或覆盖表。
- `unresolved`: 具体模型最新能力、价格、审核政策需要实时复核，不能从该文档固化。

## Formal Page Plan

- create: [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法]]
- update: [[domains/视觉制作/06-AI视频/index]]
- update: [[queries/AI视频导演与分镜入口]]
- update: root `index.md`
- update: `log.md`

query-entry: updated existing `queries/AI视频导演与分镜入口` because该知识会被自然语言问题触发，如“帮我给短剧做角色/场景/道具资产”。
