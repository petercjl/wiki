---
title: "GPT-Image-2 图像生成"
source: "https://docs.toapis.com/docs/cn/api-reference/images/gpt-image-2/generation"
author:
published:
created: 2026-06-19
description: "使用 gpt-image-2 模型生成图像，支持文生图和 reference_images 图生图"
tags:
  - "clippings"
---
```shellscript
curl --request POST \
  --url https://toapis.com/v1/images/generations \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gpt-image-2",
    "prompt": "生成一张未来城市夜景海报，霓虹灯，电影感构图",
    "n": 1,
    "size": "1:1",
    "resolution": "1K",
    "response_format": "url"
  }'
```

```json
{
  "id": "task_img_abc123def456",
  "object": "generation.task",
  "model": "gpt-image-2",
  "status": "queued",
  "progress": 0,
  "created_at": 1703884800,
  "metadata": {}
}
```

POST

/

v1

/

images

/

generations

```shellscript
curl --request POST \
  --url https://toapis.com/v1/images/generations \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gpt-image-2",
    "prompt": "生成一张未来城市夜景海报，霓虹灯，电影感构图",
    "n": 1,
    "size": "1:1",
    "resolution": "1K",
    "response_format": "url"
  }'
```

```json
{
  "id": "task_img_abc123def456",
  "object": "generation.task",
  "model": "gpt-image-2",
  "status": "queued",
  "progress": 0,
  "created_at": 1703884800,
  "metadata": {}
}
```

- 统一的图像生成 API 接口
- 通过 `model` 参数选择 `gpt-image-2`
- 支持文生图、单图参考和多图参考生成
- 异步任务管理，通过任务 ID 查询结果

**重要变更** ：为了更好的性能和成本控制，我们不再支持在 `image_urls` / `reference_images` 中直接传入 base64 图片数据。请先使用 [上传图片接口](https://docs.toapis.com/docs/cn/api-reference/uploads/images) 上传图片，获取 URL 后再调用本接口。

## AuthorizationsAuthorization

string

必填

所有接口均需要使用 Bearer Token 进行认证

获取 API Key：访问 [API Key 管理页面](https://toapis.com/console/token) 获取您的 API Key

使用时在请求头中添加：

```text
Authorization: Bearer YOUR_API_KEY
```

## Bodymodel

string

默认值:"gpt-image-2"

必填

图像生成模型名称

示例： `"gpt-image-2"`prompt

string

必填

图像生成的文本描述

最长 32,000 个字符（GPT image models 官方上限）size

string

默认值:"1:1"

输出图像比例

支持值取决于 `resolution` ：

- `1K` ： `1:1` 、 `3:2` 、 `2:3` 、 `4:3` 、 `3:4` 、 `5:4` 、 `4:5` 、 `16:9` 、 `9:16` 、 `2:1` 、 `1:2` 、 `21:9` 、 `9:21`
- `2K` ： `1:1` 、 `3:2` 、 `2:3` 、 `4:3` 、 `3:4` 、 `5:4` 、 `4:5` 、 `16:9` 、 `9:16` 、 `2:1` 、 `1:2` 、 `21:9` 、 `9:21`
- `4K` ： `16:9` 、 `9:16` 、 `2:1` 、 `1:2` 、 `21:9` 、 `9:21`resolution

string

默认值:"1K"

输出分辨率档位

支持值： `1K` 、 `2K` 、 `4K`

### 尺寸对照表

| size | 1K | 2K | 4K |
| --- | --- | --- | --- |
| `1:1` | `1024x1024` | `2048x2048` | 不支持 |
| `3:2` | `1536x1024` | `2048x1360` | 不支持 |
| `2:3` | `1024x1536` | `1360x2048` | 不支持 |
| `4:3` | `1024x768` | `2048x1536` | 不支持 |
| `3:4` | `768x1024` | `1536x2048` | 不支持 |
| `5:4` | `1280x1024` | `2560x2048` | 不支持 |
| `4:5` | `1024x1280` | `2048x2560` | 不支持 |
| `16:9` | `1536x864` | `2048x1152` | `3840x2160` |
| `9:16` | `864x1536` | `1152x2048` | `2160x3840` |
| `2:1` | `2048x1024` | `2688x1344` | `3840x1920` |
| `1:2` | `1024x2048` | `1344x2688` | `1920x3840` |
| `21:9` | `2016x864` | `2688x1152` | `3840x1648` |
| `9:21` | `864x2016` | `1152x2688` | `1648x3840` |n

integer

默认值:1

生成图像的数量

默认：1response\_format

string

默认值:"url"

返回格式

固定返回图片 URL，推荐使用 `url`reference\_images

string\[\]

参考图 URL 列表，用于图生图

**⚠️ 仅支持 URL 格式（不再支持 base64）**

- 公开可访问的图片 URL（http:// 或 https://）
- 可使用 [上传图片接口](https://docs.toapis.com/docs/cn/api-reference/uploads/images) 上传本地图片获取 URL
- 支持单图和多图参考image\_urls

string\[\]

向后兼容的参考图字段

在 ToAPIs 中会自动归一化为 `reference_images`

## Responseid

string

任务唯一标识符，用于查询任务状态object

string

对象类型，固定为 `generation.task`model

string

使用的模型名称status

string

任务状态progress

integer

任务进度百分比（0-100）created\_at

integer

任务创建时间戳（Unix 时间戳）