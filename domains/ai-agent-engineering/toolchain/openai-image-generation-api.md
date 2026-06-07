---
title: OpenAI 图像生成 API 集成指南
type: tool
created: 2026-06-07
updated: 2026-06-07
domain: ai-agent-engineering
tags: [openai, api, image-generation, gpt-image, responses-api, toolchain]
sources:
  - raw/webpages/openai/openai-image-generation-api-2026-06-07.md
  - https://developers.openai.com/api/docs/guides/image-generation
status: active
---

# OpenAI 图像生成 API 集成指南

## 用途

这页用于未来 Agent 判断如何接入 OpenAI 图像生成能力：什么时候用 Image API，什么时候用 Responses API，怎样处理参考图、局部编辑、流式预览、输出规格、安全拦截和成本估算。

## API 选择

| 场景 | 优先 API | 原因 | 注意点 |
| --- | --- | --- | --- |
| 单次文生图 | Image API | 直接指定 `gpt-image-2` 等 GPT Image 模型，调用链短 | 默认返回 base64 图像数据 |
| 单次图片编辑 | Image API | `images.edit` 支持上传图片、参考图和 mask | 多参考图时注意输入图像 token 成本 |
| 对话式图像体验 | Responses API | 图像生成作为内置 tool，可与多轮上下文结合 | 选择主线模型，由 tool 处理 GPT Image 模型选择 |
| 多轮迭代编辑 | Responses API | 可用 `previous_response_id` 或把 `image_generation_call` 放回上下文 | 强制 `action: "edit"` 时必须有图像上下文 |
| 需要 File ID 作为图片输入 | Responses API | 支持 File API 产生的 `file_id` | 文件通常使用 `purpose: "vision"` |
| 快速脚本批量生成 | Image API | `n` 可一次返回多张图 | 仍要按业务控制重试、限流和成本 |

## 关键能力

| 能力 | Image API | Responses API |
| --- | --- | --- |
| 文生图 | `images.generate(model="gpt-image-2", prompt=...)` | `responses.create(..., tools=[{"type": "image_generation"}])` |
| 图片编辑 | `images.edit(model="gpt-image-2", image=..., prompt=...)` | 输入里放 `input_image`，tool 使用 `image_generation` |
| 参考图生成 | `images.edit` 可传单张或多张 image | 可用 URL、base64 data URL 或 File ID |
| 局部编辑 | `mask` 参数 | `input_image_mask.file_id` |
| 多轮上下文 | 不适合 | 使用 `previous_response_id` 或复用 `image_generation_call.id` |
| 流式预览 | 支持 `stream` 和 `partial_images` | 支持 `stream` 和 tool 内 `partial_images` |
| revised prompt | 不作为主工作流能力 | `image_generation_call.revised_prompt` 可读取 |

## 输出参数

| 参数 | 作用 | 实操建议 |
| --- | --- | --- |
| `size` | 输出尺寸；`gpt-image-2` 支持满足约束的多种分辨率 | 常用 `1024x1024`、`1536x1024`、`1024x1536`、`2048x2048`、`3840x2160`，也可用 `auto` |
| `quality` | 渲染质量：`low`、`medium`、`high`、`auto` | 草稿/缩略图用 `low`，定稿资产再升到 `medium` 或 `high` |
| `background` | 背景类型或 `auto` | `gpt-image-2` 当前不支持 `background: "transparent"` |
| `output_format` | Image API 输出格式 | 默认 `png`，可选 `jpeg`、`webp` |
| `output_compression` | JPEG/WebP 压缩比例 | 延迟敏感时优先考虑 `jpeg` 和合理压缩 |
| `partial_images` | 流式生成时返回 0-3 张中间图 | 每张 partial image 额外计 100 image output tokens |
| `moderation` | 图像生成安全过滤严格度 | 默认 `auto`；`low` 更宽松但仍受内容政策约束 |

## 尺寸约束

`gpt-image-2` 的 `size` 不是只能用固定枚举，但必须满足这些约束：

- 最大边长不超过 `3840px`。
- 两条边都必须是 `16px` 的倍数。
- 长边与短边比例不超过 `3:1`。
- 总像素数至少 `655,360`，最多 `8,294,400`。
- 超过 `2560x1440` 的 2K 以上输出在官方文档中标为实验性能力。

## 图片编辑规则

参考图和编辑请求要重点控制三件事：

- `gpt-image-2` 对图片输入自动高保真处理，`input_fidelity` 不可调，也不需要传；这会提高含参考图编辑的 input image token 成本。
- mask 编辑要求原图与 mask 格式和尺寸一致，且小于 50MB。
- mask 文件必须有 alpha channel；黑白 mask 需要先转成 RGBA，并把 mask 写入 alpha 通道。

## 错误处理

图像生成失败不要只做盲目重试：

| 错误类型 | 处理方式 |
| --- | --- |
| `429`、`5xx` | 可按普通 API transient failure 重试 |
| `image_generation_user_error` | 通常需要修改 prompt、输入图或参数，不应原样重试 |
| `moderation_blocked` | 先按 `error.code` 分支，再读取可选 `moderation_details` |
| `moderation_stage = input` | 引导用户改 prompt 或输入图 |
| `moderation_stage = output` | 记录为生成结果安全拦截，调整 prompt 后再生成 |

记录日志时保留 `request_id`、`error.code` 和可选 `moderation_details`，但不要向终端用户暴露内部判断细节。

## 成本判断

一次图像生成/编辑的成本由三部分组成：

- 输入文本 tokens。
- 编辑或参考图场景中的输入图片 tokens。
- 图像输出 tokens。

对 `gpt-image-2`，应以官方 pricing/calculator 当前价格为准。文档中的示例显示，同一质量下，非正方形大图不一定比正方形小图更贵；成本由输出 token 估算决定，不能只按像素直觉判断。

## Agent 集成决策规则

- 如果用户只要“一张图/一组图”，优先 Image API，除非需要对话式多轮上下文。
- 如果用户会持续追问“再改成某风格/保持这个角色继续生成/基于上一张继续改”，优先 Responses API。
- 如果需要严格版式、文字位置或品牌元素一致性，应在产品层预留人工或二次排版校验，因为官方限制里明确提到文字、视觉一致性和精确构图仍可能不稳定。
- 如果要做电商主图、海报或中文文案图，优先把图像生成与后处理排版拆开：让模型生成主体视觉，再用确定性排版工具处理中文文本。
- 如果要暴露给最终用户，必须实现安全拦截提示、请求 ID 记录、成本/质量档位控制和失败重试策略。

## 相关页面

- [[domains/ai-agent-engineering/skill-design/personal-ai-agent-skill-registry|个人/项目 Skill 注册库]]
- [[domains/ai-agent-engineering/skill-design/ai-agent-skill-registry|跨 Agent Skill 注册库]]
- [[domains/visual-production/index|视觉制作知识域]]

## Source

- Raw clipping: `raw/webpages/openai/openai-image-generation-api-2026-06-07.md`
- Official current doc checked: `https://developers.openai.com/api/docs/guides/image-generation`
