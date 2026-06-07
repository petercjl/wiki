---
title: OpenAI 图像生成 API 集成指南
type: tool
created: 2026-06-07
updated: 2026-06-07
domain: ai-agent-engineering
tags: [openai, api, image-generation, gpt-image, responses-api, toolchain]
sources:
  - raw/webpages/openai/openai-image-generation-api-2026-06-07.md
  - _meta/extraction-notes/openai-image-generation-api-2026-06-07/coverage-checklist.md
  - https://developers.openai.com/api/docs/guides/image-generation
status: active
---

# OpenAI 图像生成 API 集成指南

## 用途

这页用于未来 Agent 判断如何接入 OpenAI 图像生成能力：什么时候用 Image API，什么时候用 Responses API，怎样处理参考图、局部编辑、流式预览、输出规格、安全拦截和成本估算。

本页不是原文摘要，而是集成手册。原文中的图片画廊、完整示例代码和案例截图已保存在 raw；正式页必须保留所有 API 形态、关键参数、案例意图和可改写代码模板。

## API 选择

| 场景 | 优先 API | 原因 | 注意点 |
| --- | --- | --- | --- |
| 单次文生图 | Image API | 直接指定 `gpt-image-2` 等 GPT Image 模型，调用链短 | 默认返回 base64 图像数据 |
| 单次图片编辑 | Image API | `images.edit` 支持上传图片、参考图和 mask | 多参考图时注意输入图像 token 成本 |
| 对话式图像体验 | Responses API | 图像生成作为内置 tool，可与多轮上下文结合 | 选择主线模型，由 tool 处理 GPT Image 模型选择 |
| 多轮迭代编辑 | Responses API | 可用 `previous_response_id` 或把 `image_generation_call` 放回上下文 | 强制 `action: "edit"` 时必须有图像上下文 |
| 需要 File ID 作为图片输入 | Responses API | 支持 File API 产生的 `file_id` | 文件通常使用 `purpose: "vision"` |
| 快速脚本批量生成 | Image API | `n` 可一次返回多张图 | 仍要按业务控制重试、限流和成本 |

## 模型与访问前提

- GPT Image 模型包括 `gpt-image-2`、`gpt-image-1.5`、`gpt-image-1`、`gpt-image-1-mini`。
- 使用 GPT Image 模型前，组织可能需要完成 API Organization Verification；这属于开发者控制台/组织权限问题，不是代码实现问题。
- Image API 从 `gpt-image-1` 及后续模型开始提供 Generations 和 Edits 两类核心能力。
- Image API 还包含 variations endpoint，但这是给支持 variations 的模型使用，例如 DALL-E 2；不要把它当成 `gpt-image-2` 的主工作流。
- Responses API 图像生成 tool 不直接选择 GPT Image 模型，而是选择支持该 tool 的主线模型；官方说明是 `gpt-5` 及更新模型通常应支持，接入前仍要查模型详情页确认。

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

## 原文案例索引

| 原文案例 | 演示能力 | 可复用价值 |
| --- | --- | --- |
| 页面顶部 16 张 gallery 图 | GPT Image 输出风格展示 | 作为 raw-only 视觉参考保留；不进入正式页逐图分析，除非未来做提示词风格库 |
| 木桌上的米色咖啡杯 | 文档中的普通示例图 | raw-only；不承载 API 规则 |
| 儿童书风格兽医听小水獭心跳 | Image API 单次文生图 | 最小可运行 `images.generate` 模板：prompt -> base64 -> 本地图片 |
| 灰色虎斑猫抱橙围巾小水獭 | Responses API 图像 tool | `responses.create` + `tools=[{"type": "image_generation"}]` 的基础模板 |
| “Now make it look realistic” | 多轮图像迭代 | 使用 `previous_response_id` 或复用 `image_generation_call.id` 继续改图 |
| 白色猫头鹰羽毛河流穿过冬季景观 | 流式生成和 partial images | 用 `partial_images` 提前拿 0-3 张中间图，改善交互体验 |
| 浴液、香皂、香薰、浴球生成礼篮 | 多参考图生成 | 同一请求混用 base64 图片和 File ID 作为参考图输入 |
| 室内泳池加火烈鸟 | mask 局部编辑 | 使用原图 + mask，只替换局部区域；mask 作为提示性指导而非像素级硬约束 |
| 冒犯同事海报被拦截 | 内容安全错误处理 | 识别 `moderation_blocked`，根据 `moderation_stage` 区分输入拦截和输出拦截 |

## 代码模板

### Image API：单次文生图

适合简单“一条 prompt 生成一张图”的任务。返回值在 `result.data[0].b64_json`，应用层负责 base64 解码和落盘。

```python
from openai import OpenAI
import base64

client = OpenAI()

result = client.images.generate(
    model="gpt-image-2",
    prompt="A children's book drawing of a veterinarian listening to a baby otter's heartbeat."
)

image_bytes = base64.b64decode(result.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
```

要点：

- 批量生成可加 `n`，默认返回 1 张。
- 适合脚本和后端任务，不适合连续对话式改图。
- 如果需要 `jpeg`/`webp`、压缩或特定尺寸，把输出参数放到同一请求里。

同一能力的其他调用形态：

```javascript
const result = await openai.images.generate({
  model: "gpt-image-2",
  prompt,
});

fs.writeFileSync(
  "output.png",
  Buffer.from(result.data[0].b64_json, "base64")
);
```

```bash
curl -X POST "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-image-2","prompt":"A children book drawing of a veterinarian listening to a baby otter heartbeat."}' \
  | jq -r '.data[0].b64_json' | base64 --decode > output.png
```

```bash
openai images generate \
  --model gpt-image-2 \
  --prompt "A children book drawing of a veterinarian listening to a baby otter heartbeat." \
  --raw-output \
  --transform 'data.0.b64_json' | base64 --decode > output.png
```

### Responses API：图像生成 tool

适合把图像生成放进对话或多步流程。模型选主线模型，例如原文示例使用 `gpt-5.5`；图像生成由 `image_generation` tool 完成。

```python
from openai import OpenAI
import base64

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Generate an image of a gray tabby cat hugging an otter with an orange scarf.",
    tools=[{"type": "image_generation", "action": "generate"}],
)

image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    with open("image.png", "wb") as f:
        f.write(base64.b64decode(image_data[0]))
```

`action` 的含义：

| `action` | 行为 |
| --- | --- |
| `auto` | 默认，让模型判断生成新图还是编辑上下文中的图 |
| `generate` | 强制生成新图 |
| `edit` | 强制编辑上下文中的图；如果上下文没有图会报错 |

### Responses API：多轮改图

原文给了两种路径：

- `previous_response_id`：让下一轮自动继承上一轮上下文。
- `image_generation_call.id`：把上一轮生成图的 call id 显式放进新请求输入。

```python
first = client.responses.create(
    model="gpt-5.5",
    input="Generate an image of a gray tabby cat hugging an otter with an orange scarf.",
    tools=[{"type": "image_generation"}],
)

second = client.responses.create(
    model="gpt-5.5",
    previous_response_id=first.id,
    input="Now make it look realistic.",
    tools=[{"type": "image_generation"}],
)
```

集成判断：

- 如果产品是聊天式改图，优先 `previous_response_id`。
- 如果服务端需要精确控制引用哪张图，保存 `image_generation_call.id`。

### 流式生成：partial images

Responses API 和 Image API 都支持流式生成。`partial_images` 可设为 0-3；请求的中间图数量不保证全部返回，生成太快时可能少于请求数。

```python
stream = client.responses.create(
    model="gpt-5.5",
    input="Draw a river made of white owl feathers through a winter landscape.",
    stream=True,
    tools=[{"type": "image_generation", "partial_images": 2}],
)

for event in stream:
    if event.type == "response.image_generation_call.partial_image":
        save_base64_image(f"partial-{event.partial_image_index}.png", event.partial_image_b64)
    elif event.type == "response.completed":
        final_images = [
            output.result
            for output in event.response.output
            if output.type == "image_generation_call"
        ]
```

Image API 的事件名不同：中间图事件是 `image_generation.partial_image`，图像 base64 在 `event.b64_json`。

Image API 直接流式模板：

```python
stream = client.images.generate(
    model="gpt-image-2",
    prompt="Draw a river made of white owl feathers through a winter landscape.",
    stream=True,
    partial_images=2,
)

for event in stream:
    if event.type == "image_generation.partial_image":
        with open(f"partial-{event.partial_image_index}.png", "wb") as f:
            f.write(base64.b64decode(event.b64_json))
```

### Revised prompt

Responses API 的图像生成 tool 可能会自动改写 prompt。可在 `image_generation_call.revised_prompt` 读取，适合做调试、日志和 prompt 质量分析。

```json
{
  "type": "image_generation_call",
  "status": "completed",
  "revised_prompt": "...",
  "result": "..."
}
```

### 参考图生成：URL、base64、File ID

Responses API 输入图片有三种方式：

| 输入方式 | 字段 | 适用情况 |
| --- | --- | --- |
| 远程 URL | `image_url` | 图片已经有可访问 URL |
| base64 data URL | `image_url: "data:image/png;base64,..."` | 本地图片少量临时传入 |
| File ID | `file_id` | 多轮复用、较复杂工作流或服务端先上传 |

上传 File ID 的模板：

```python
def create_file(file_path):
    with open(file_path, "rb") as file_content:
        result = client.files.create(file=file_content, purpose="vision")
    return result.id
```

base64 模板：

```python
import base64

def encode_image(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
```

多参考图案例的结构：

```python
response = client.responses.create(
    model="gpt-5.5",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "Generate a gift basket containing all reference products."},
            {"type": "input_image", "image_url": f"data:image/png;base64,{base64_image1}"},
            {"type": "input_image", "file_id": file_id1},
        ],
    }],
    tools=[{"type": "image_generation"}],
)
```

Image API 也能用 `images.edit` 做多参考图生成，适合不需要对话上下文的脚本：

```python
result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("body-lotion.png", "rb"),
        open("bath-bomb.png", "rb"),
        open("incense-kit.png", "rb"),
        open("soap.png", "rb"),
    ],
    prompt="Generate a photorealistic gift basket containing all reference products.",
)
```

对应 curl/CLI 形态使用 `/v1/images/edits`，多个参考图用重复的 `image[]=@file.png` 字段传入；CLI 则重复 `--image`。

### Mask 局部编辑

Responses API 使用 `input_image_mask.file_id`；Image API 使用 `mask` 参数。原文强调：mask 是提示性指导，模型可能不会完全按 mask 边界逐像素执行。

```python
image_file_id = create_file("source.png")
mask_file_id = create_file("mask.png")

response = client.responses.create(
    model="gpt-5.5",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "Keep the room, but add a flamingo in the pool."},
            {"type": "input_image", "file_id": image_file_id},
        ],
    }],
    tools=[{
        "type": "image_generation",
        "quality": "high",
        "input_image_mask": {"file_id": mask_file_id},
    }],
)
```

Image API 的 mask 编辑模板：

```python
result = client.images.edit(
    model="gpt-image-2",
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
```

curl/CLI 形态：

```bash
curl -X POST "https://api.openai.com/v1/images/edits" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "model=gpt-image-2" \
  -F "image[]=@sunlit_lounge.png" \
  -F "mask=@mask.png" \
  -F "prompt=A sunlit indoor lounge area with a pool containing a flamingo" \
  | jq -r '.data[0].b64_json' | base64 --decode > lounge.png
```

mask 文件要求：

- 原图和 mask 格式、尺寸一致。
- 原图和 mask 都小于 50MB。
- mask 必须带 alpha channel。
- 多输入图时，mask 应用于第一张输入图。

黑白 mask 转 alpha channel：

```python
from PIL import Image
from io import BytesIO

mask = Image.open("mask.png").convert("L")
mask_rgba = mask.convert("RGBA")
mask_rgba.putalpha(mask)

buf = BytesIO()
mask_rgba.save(buf, format="PNG")
with open("mask_alpha.png", "wb") as f:
    f.write(buf.getvalue())
```

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

## 模型限制

| 限制 | 原文含义 | 集成影响 |
| --- | --- | --- |
| Latency | 复杂 prompt 可能需要最多约 2 分钟处理 | 前端要做异步状态、超时提示和任务轮询/恢复，不要假设秒级返回 |
| Text rendering | 文字渲染已有提升，但仍可能在位置和清晰度上失败 | 中文海报、电商主图、品牌字样优先用后处理排版 |
| Consistency | 多次生成能保持一定一致性，但角色或品牌元素仍可能漂移 | 需要参考图、固定 prompt 规范和人工/自动 QA |
| Composition control | 结构化布局和精确元素位置仍可能不稳定 | 严格版式不要完全依赖模型一次生成 |

## 错误处理

图像生成失败不要只做盲目重试：

| 错误类型 | 处理方式 |
| --- | --- |
| `429`、`5xx` | 可按普通 API transient failure 重试 |
| `image_generation_user_error` | 通常需要修改 prompt、输入图或参数，不应原样重试 |
| `moderation_blocked` | 先按 `error.code` 分支，再读取可选 `moderation_details` |
| `moderation_stage = input` | 引导用户改 prompt 或输入图 |
| `moderation_stage = output` | 记录为生成结果安全拦截，调整 prompt 后再生成 |
| `moderation_stage = unknown` | 少见兜底状态，记录日志并让用户泛化修改输入 |

所有 prompts 和生成图都会受内容政策过滤。记录日志时保留 `request_id`、`error.code` 和可选 `moderation_details`，但不要向终端用户暴露内部判断细节。`moderation_details.categories` 是粗粒度公开标签，可能出现 `harassment`、`self-harm`、`sexual`、`violence` 等。

### 内容安全错误处理模板

```javascript
try {
  await openai.images.generate({
    model: "gpt-image-2",
    prompt,
  });
} catch (error) {
  if (error?.code !== "moderation_blocked") throw error;

  const details = error?.moderation_details;
  const stage = details?.moderation_stage;
  const categories = details?.categories ?? [];

  console.error("Image generation blocked", {
    request_id: error?.request_id,
    code: error?.code,
    moderation_details: details,
  });

  if (categories.includes("harassment")) {
    return "请去掉攻击、羞辱或针对个人的表达。";
  }
  if (stage === "input") {
    return "请调整提示词或输入图片后重试。";
  }
  if (stage === "output") {
    return "生成结果被安全检查拦截，请换一种表达重新生成。";
  }
  return "请求未通过安全检查，请修改后重试。";
}
```

Python 处理模式同理：捕获 `openai.BadRequestError`，先判断 `error.code == "moderation_blocked"`，再从 `error.body["moderation_details"]` 读取 `categories` 和 `moderation_stage`；不要把 `moderation_details` 当成必定存在的字段。

## 成本判断

一次图像生成/编辑的成本由三部分组成：

- 输入文本 tokens。
- 编辑或参考图场景中的输入图片 tokens。
- 图像输出 tokens。

对 `gpt-image-2`，应以官方 pricing/calculator 当前价格为准。文档中的示例显示，同一质量下，非正方形大图不一定比正方形小图更贵；成本由输出 token 估算决定，不能只按像素直觉判断。

`gpt-image-2` 的 output tokens 应使用官方 calculator 根据 `quality` 和 `size` 估算；剪藏中 calculator 动态组件只留下了 `196` 这个输出 token 示例值，不应把它当成通用固定值。

旧 GPT Image 模型在成本/延迟上先生成专用 image tokens，尺寸越大、质量越高 token 越多。原文保留的旧模型 token 表：

| Quality | Square 1024x1024 | Portrait 1024x1536 | Landscape 1536x1024 |
| --- | --- | --- | --- |
| Low | 272 tokens | 408 tokens | 400 tokens |
| Medium | 1056 tokens | 1584 tokens | 1568 tokens |
| High | 4160 tokens | 6240 tokens | 6208 tokens |

原文保留的示例价格表：

| 模型 | 质量 | 1024x1024 | 1024x1536 | 1536x1024 |
| --- | --- | --- | --- | --- |
| GPT Image 2 | Low | $0.006 | $0.005 | $0.005 |
| GPT Image 2 | Medium | $0.053 | $0.041 | $0.041 |
| GPT Image 2 | High | $0.211 | $0.165 | $0.165 |
| GPT Image 1.5 | Low | $0.009 | $0.013 | $0.013 |
| GPT Image 1.5 | Medium | $0.034 | $0.050 | $0.050 |
| GPT Image 1.5 | High | $0.133 | $0.200 | $0.200 |
| GPT Image 1 | Low | $0.011 | $0.016 | $0.016 |
| GPT Image 1 | Medium | $0.042 | $0.063 | $0.063 |
| GPT Image 1 | High | $0.167 | $0.250 | $0.250 |
| GPT Image 1 Mini | Low | $0.005 | $0.006 | $0.006 |
| GPT Image 1 Mini | Medium | $0.011 | $0.015 | $0.015 |
| GPT Image 1 Mini | High | $0.036 | $0.052 | $0.052 |

注意：价格属于时间敏感信息，实际接入前必须重新查官方 pricing 页面。上表用于理解不同模型、尺寸和质量之间的成本关系。

## Agent 集成决策规则

- 如果用户只要“一张图/一组图”，优先 Image API，除非需要对话式多轮上下文。
- 如果用户会持续追问“再改成某风格/保持这个角色继续生成/基于上一张继续改”，优先 Responses API。
- 如果需要严格版式、文字位置或品牌元素一致性，应在产品层预留人工或二次排版校验，因为官方限制里明确提到文字、视觉一致性和精确构图仍可能不稳定。
- 如果要做电商主图、海报或中文文案图，优先把图像生成与后处理排版拆开：让模型生成主体视觉，再用确定性排版工具处理中文文本。
- 如果要暴露给最终用户，必须实现安全拦截提示、请求 ID 记录、成本/质量档位控制和失败重试策略。

## Coverage Notes

- Full coverage checklist: `_meta/extraction-notes/openai-image-generation-api-2026-06-07/coverage-checklist.md`
- Coverage status: all source headings, API shapes, code/example categories, parameter tables, limitations, moderation behavior, supported-model note, and cost tables are represented in this page or marked raw-only.
- Raw-only: gallery images and decorative/example images that do not carry API rules remain in `raw/webpages/openai/openai-image-generation-api-2026-06-07.md`.

## 相关页面

- [[domains/ai-agent-engineering/skill-design/personal-ai-agent-skill-registry|个人/项目 Skill 注册库]]
- [[domains/ai-agent-engineering/skill-design/ai-agent-skill-registry|跨 Agent Skill 注册库]]
- [[domains/visual-production/index|视觉制作知识域]]

## Source

- Raw clipping: `raw/webpages/openai/openai-image-generation-api-2026-06-07.md`
- Official current doc checked: `https://developers.openai.com/api/docs/guides/image-generation`
