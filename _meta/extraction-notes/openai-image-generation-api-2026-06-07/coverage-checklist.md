---
title: OpenAI image generation API coverage checklist
type: source-summary
created: 2026-06-07
updated: 2026-06-07
domain: ai-agent-engineering
tags: [openai, api, image-generation, coverage]
sources:
  - raw/webpages/openai/openai-image-generation-api-2026-06-07.md
  - https://developers.openai.com/api/docs/guides/image-generation
status: active
---

# OpenAI image generation API coverage checklist

## Scope

This checklist audits the raw Obsidian clipping and the current official OpenAI image generation guide against:

- `domains/ai-agent-engineering/toolchain/openai-image-generation-api.md`

Goal: no source knowledge unit should be lost. Source units are either formalized, preserved as raw-only, or called out as current-doc supplementation because the clipping missed language-switcher examples.

## Coverage Matrix

| Source unit | Status | Formal location / note |
| --- | --- | --- |
| Top gallery images | raw-only | Preserved in raw; formal page notes they are style examples, not API rules. |
| Overview: GPT Image models and `gpt-image-2` | formalized | 模型与访问前提; API 选择 |
| Image API: generations and edits | formalized | API 选择; 关键能力 |
| Image API variations endpoint for DALL-E 2 | formalized | 模型与访问前提 |
| Responses API as image generation built-in tool | formalized | API 选择; Responses API template |
| Responses API adds multi-turn editing and File ID inputs | formalized | API 选择; 参考图生成; 多轮改图 |
| API choice rules | formalized | API 选择; Agent 集成决策规则 |
| Organization verification requirement | formalized | 模型与访问前提 |
| Mug image | raw-only | Preserved in raw; decorative/example image without additional API rule. |
| Image API single generation Python | formalized | Image API：单次文生图 |
| Image API single generation JavaScript/curl/CLI | current-doc supplement | Added from official docs because raw clipping captured only Python. |
| `n` parameter for multiple images | formalized | Image API：单次文生图 notes |
| Responses API image generation Python | formalized | Responses API：图像生成 tool |
| Responses API action `auto/generate/edit` | formalized | action table |
| Force `edit` without image context causes error | formalized | API 选择; action table |
| Multi-turn via `previous_response_id` | formalized | Responses API：多轮改图 |
| Multi-turn via `image_generation_call.id` | formalized | Responses API：多轮改图 |
| Multi-turn result case: cat/otter -> realistic | formalized | 原文案例索引 |
| Streaming via Responses API | formalized | 流式生成 |
| Streaming via Image API | current-doc supplement | Added direct Image API stream template. |
| `partial_images` 0-3 and may return fewer | formalized | 流式生成; 输出参数 |
| Partial image cost +100 image output tokens each | formalized | 输出参数; 成本判断 |
| Revised prompt | formalized | Revised prompt |
| Edit Images capability list | formalized | 关键能力; 参考图生成; Mask 局部编辑 |
| Gift basket reference-image case | formalized | 原文案例索引; 参考图生成 |
| Input image as URL/base64/File ID | formalized | 参考图生成 |
| File upload with `purpose="vision"` | formalized | 参考图生成 |
| Base64 data URL helper | formalized | 参考图生成 |
| Multiple reference images in Responses API | formalized | 参考图生成 |
| Multiple reference images in Image API `images.edit` | current-doc supplement | Added Image API multi-reference template. |
| Mask edit with Responses API | formalized | Mask 局部编辑 |
| Mask edit with Image API/curl | current-doc supplement | Added direct Image API and curl templates. |
| Mask is prompt-guided, not exact shape guarantee | formalized | Mask 局部编辑 |
| Mask applied to first image when multiple inputs | formalized | Mask 文件要求 |
| Mask size/format/alpha requirements | formalized | Mask 文件要求 |
| Programmatic alpha channel conversion | formalized | Mask 局部编辑 |
| `input_fidelity` not configurable for `gpt-image-2` | formalized | 图片编辑规则 |
| `gpt-image-2` high-fidelity inputs can increase input tokens | formalized | 图片编辑规则; 成本判断 |
| Output options: size, quality, format, compression, background | formalized | 输出参数 |
| `size`, `quality`, `background` support `auto` | formalized | 输出参数 |
| `gpt-image-2` no transparent background | formalized | 输出参数 |
| Popular sizes | formalized | 输出参数; 尺寸约束 |
| Size constraints | formalized | 尺寸约束 |
| `quality: low` for drafts/thumbnails/iteration | formalized | 输出参数 |
| >2K experimental note | formalized | 尺寸约束 |
| Output format png/jpeg/webp and compression | formalized | 输出参数 |
| JPEG faster than PNG | formalized | 输出参数 |
| Limitations: latency up to 2 minutes | formalized | 模型限制; Agent 集成决策规则 |
| Limitations: text rendering | formalized | 模型限制; Agent 集成决策规则 |
| Limitations: consistency | formalized | 模型限制; Agent 集成决策规则 |
| Limitations: composition control | formalized | 模型限制; Agent 集成决策规则 |
| Moderation parameter `auto/low` | formalized | 输出参数; 错误处理 |
| `image_generation_user_error` | formalized | 错误处理 |
| `moderation_blocked` details | formalized | 错误处理; 内容安全错误处理模板 |
| `moderation_stage`: input/output/unknown | formalized | 错误处理 |
| `categories` examples | formalized | 内容安全错误处理模板 |
| JavaScript moderation template | formalized | 内容安全错误处理模板 |
| Python moderation handling | formalized | 内容安全错误处理模板 note |
| Supported models for Responses image tool | formalized | 模型与访问前提 |
| `gpt-image-2` output token calculator | formalized | 成本判断 |
| Prior-model image token table | formalized | 成本判断 |
| Final cost = text input + image input + image output | formalized | 成本判断 |
| Example price table | formalized | 成本判断 |

## Residual Notes

- The raw clipping captured only the Python tabs for several code switchers. Official docs MCP was used on 2026-06-07 to recover JavaScript/curl/CLI examples at the level of reusable templates.
- Image gallery and decorative image examples are intentionally raw-only because they are visual examples rather than API behavior. If a future task builds a GPT Image prompt-style gallery, revisit these images.
- Pricing is time-sensitive. The formal page keeps the source example table for reasoning but requires checking the official pricing page before production decisions.
