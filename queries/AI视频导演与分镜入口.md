---
title: AI视频导演与分镜入口
type: query
created: 2026-07-02
updated: 2026-07-29
domain: 视觉制作
tags: [visual-production, prompt-engineering, workflow]
sources:
  - domains/视觉制作/06-AI视频/index.md
  - raw/videos/douyin-prompt-layered-control-2026-07-23/original.mp4
  - _meta/extraction-notes/douyin-prompt-layered-control-2026-07-23/coverage-matrix.md
  - raw/articles/ai-short-video-prompt-research-2026-07-27/video-generation-prompt-research-log.raw.md
  - _meta/extraction-notes/ai-short-video-prompt-research-2026-07-27/coverage-matrix.md
  - raw/videos/ai-tvc-million-course-2026-07-29/original.mp4
  - _meta/extraction-notes/ai-tvc-million-course-2026-07-29/coverage-matrix.md
status: active
---

# AI视频导演与分镜入口

当用户要求写 AI 视频脚本、商业短视频创意、导演表、分镜、首尾帧方案、图生视频 prompt、长视频衔接或案例借鉴时，先读：

1. [[domains/视觉制作/06-AI视频/index|AI 视频知识入口]]
2. [[domains/视觉制作/06-AI视频/25-AI短视频分镜通用能力/index|AI短视频分镜通用能力]]
3. [[domains/视觉制作/06-AI视频/25-AI短视频分镜通用能力/08-Agent使用模板：故事大纲转分镜提示词|Agent使用模板：故事大纲转分镜提示词]]
4. [[domains/视觉制作/06-AI视频/25-AI短视频分镜通用能力/09-AI短视频完整视听分镜Prompt结构|AI短视频完整视听分镜 Prompt 结构]]
5. [[domains/视觉制作/06-AI视频/08-Agent使用模板：AI视频导演分镜|Agent 使用模板：AI视频导演分镜]]
6. [[domains/视觉制作/06-AI视频/02-AI商业短视频规划方法|AI 商业短视频规划方法]]
7. [[domains/视觉制作/06-AI视频/03-导演式镜头设计方法|导演式镜头设计方法]]
8. [[domains/视觉制作/06-AI视频/04-商业短视频摄影与运镜语法|商业短视频摄影与运镜语法]]
9. [[domains/视觉制作/06-AI视频/05-AI视频导演Prompt模板|AI 视频导演 Prompt 模板]]
10. [[domains/视觉制作/06-AI视频/13-AI短视频生成提示词方法论：TVC与剧情短片|AI短视频生成提示词方法论：TVC与剧情短片]]
11. [[domains/视觉制作/06-AI视频/14-AI品牌TVC的气质、视觉符号与产品登场|AI品牌TVC的气质、视觉符号与产品登场]]

## 分支读取

- 需要长视频连续性或多段续写时，读 [[domains/视觉制作/06-AI视频/09-AI长视频连续性组接方法|AI 长视频连续性组接方法]]。
- 需要更系统的导演、场面调度、剪辑、轴线、POV 或移动摄影知识时，读 [[queries/AI视频导演知识系统入口|AI 视频导演知识系统入口]]。
- 需要参考商业短视频案例时，读 [[domains/视觉制作/06-AI视频/90-案例库/index|AI 商业短视频案例库]]。
- 需要确定品牌 TVC 的广告气质、把自由/治愈/安全/品质等抽象价值变成可见证据，或判断产品应早露出、渐进露出还是延后英雄亮相时，读 [[domains/视觉制作/06-AI视频/14-AI品牌TVC的气质、视觉符号与产品登场|AI品牌TVC的气质、视觉符号与产品登场]]；需要对照气氛连续与产品因果时，读 [[domains/视觉制作/06-AI视频/90-案例库/09-香水与汽车TVC：从品牌世界到产品亮相|香水与汽车TVC案例]]。
- 需要把普通故事大纲转换成 2 分钟 AI 短视频分镜 prompt 时，优先读 [[domains/视觉制作/06-AI视频/25-AI短视频分镜通用能力/01-故事大纲到AI视频分镜的拆解方法|故事大纲到AI视频分镜的拆解方法]]、[[domains/视觉制作/06-AI视频/25-AI短视频分镜通用能力/02-AI视频镜头字段标准|AI视频镜头字段标准]]、[[domains/视觉制作/06-AI视频/25-AI短视频分镜通用能力/04-运镜选择方法|运镜选择方法]]、[[domains/视觉制作/06-AI视频/25-AI短视频分镜通用能力/07-镜头连续性与剪辑衔接|镜头连续性与剪辑衔接]] 和 [[domains/视觉制作/06-AI视频/25-AI短视频分镜通用能力/09-AI短视频完整视听分镜Prompt结构|AI短视频完整视听分镜 Prompt 结构]]。
- 需要为 AI 仿真人短剧建立角色、场景、道具资产包时，先读 [[domains/视觉制作/06-AI视频/11-AI短剧角色场景道具资产构建方法|AI短剧角色场景道具资产构建方法]]，把平台工具步骤还原为资产协议、模型/API 节点、四视图、多视角场景和 QA 工作流。
- 需要商业可控、对白、旁白、内心独白、画外音、环境声或禁止模型自由发挥时，必须先锁定台词总表、声音策略和空间锚点，再输出分段 prompt。
- 需要先解决“故事是否成立”、产品广告命题、情感短片结构、人物动机、传播钩子或故事模式时，先读 [[queries/AI短视频故事策划|AI短视频故事策划]]，不要直接进入分镜 prompt。
- 需要学习“如何做特定风格 AI 短视频”、影像美学大师风格、岩井俊二、王家卫、韦斯·安德森、是枝裕和、小津安二郎、侯孝贤、贾樟柯、大卫·芬奇、斯皮尔伯格、克里斯托弗·诺兰或秒级镜头 prompt 时，读 [[domains/视觉制作/06-AI视频/30-影像美学大师风格AI短视频/index|影像美学大师风格AI短视频]] 和对应导演风格页。
- 需要 Seedance 2.0 模型参数、价格或能力边界时，读 [[domains/视觉制作/06-AI视频/01-Doubao-Seedance-2.0视频生成模型卡|Doubao-Seedance-2.0 视频生成模型卡]]，并按当前官方文档复核。
- 当 Prompt 越写越长、细节越多却越不听话，或主体、构图、运镜、光线、情绪和风格互相抢控制力时，读 [[domains/视觉制作/06-AI视频/12-AI视频Prompt分层强控方法|AI视频 Prompt 分层强控方法]]，先排硬约束、关键细节和风格优先级，再判断是否应拆镜头、拆阶段或使用参考图、首尾帧、遮罩和后期。
- 当用户已经有角色、场景、产品/道具或风格参考图，只需要优化 5 秒 TVC 或 10—15 秒剧情生成 Prompt 时，优先读 [[domains/视觉制作/06-AI视频/13-AI短视频生成提示词方法论：TVC与剧情短片|AI短视频生成提示词方法论：TVC与剧情短片]]：先按自然镜头判断时长与约束负载，再决定参考图、人物关系、背景行为、声音和最小补丁；不要把上游资产规划问题混入 Prompt。

## 工作边界

- 不要直接输出 prompt；先判断传播问题、故事命题、镜头任务和前后衔接。
- 不要把每个镜头都写成复杂运镜；单镜头优先一个主动作或主运动。
- 不要承诺当前视频模型的实时价格、时长、画幅、参考图数量或审核规则，除非已复核当前官方资料。

## 标准输出

```text
1. 项目命题和传播问题
2. 参考案例或结构来源
3. 人物、场景、产品入场方式
4. 台词与旁白总表
5. 镜头表、空间锚点与前后衔接
6. 首帧/分镜图 prompt
7. 视频生成 prompt
8. AI 生成风险、声音策略和剪辑取舍
```
