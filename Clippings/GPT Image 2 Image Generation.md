---
title: "GPT Image 2 Image Generation"
source: "https://docs.evolink.ai/en/api-manual/image-series/gpt-image-2/gpt-image-2-image-generation"
author:
published:
created: 2026-06-19
description: "- GPT Image 2 (gpt-image-2) model supports text-to-image, image-to-image, image editing and other generation modes - Asynchronous processing mode, use the returned task ID to query - Generated image links are valid for 24 hours, please save them promptly"
tags:
  - "clippings"
---
```
curl --request POST \
  --url https://api.evolink.ai/v1/images/generations \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "model": "gpt-image-2",
  "prompt": "A beautiful colorful sunset over the ocean"
}
'
```

```
{
  "created": 1757156493,
  "id": "task-unified-1757156493-imcg5zqt",
  "model": "gpt-image-2",
  "object": "image.generation.task",
  "progress": 0,
  "status": "pending",
  "task_info": {
    "can_cancel": true,
    "estimated_time": 100
  },
  "type": "image",
  "usage": {
    "billing_rule": "per_call",
    "credits_reserved": 2.5,
    "user_group": "default"
  }
}
```

POST

/

v1

/

images

/

generations

```
curl --request POST \
  --url https://api.evolink.ai/v1/images/generations \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "model": "gpt-image-2",
  "prompt": "A beautiful colorful sunset over the ocean"
}
'
```

```
{
  "created": 1757156493,
  "id": "task-unified-1757156493-imcg5zqt",
  "model": "gpt-image-2",
  "object": "image.generation.task",
  "progress": 0,
  "status": "pending",
  "task_info": {
    "can_cancel": true,
    "estimated_time": 100
  },
  "type": "image",
  "usage": {
    "billing_rule": "per_call",
    "credits_reserved": 2.5,
    "user_group": "default"
  }
}
```

#### AuthorizationsAuthorization

string

header

required

##All APIs require Bearer Token authentication##

Get API Key:

Visit [API Key Management Page](https://evolink.ai/dashboard/keys) to get your API Key

Add to request header:

```
Authorization: Bearer YOUR_API_KEY
```

#### Body

application/jsonmodel

enum\<string>

default:gpt-image-2

required

Image generation model name, official channel, better stability and controllability, suitable for commercial scenarios

Available options:

`gpt-image-2`

Example:

`"gpt-image-2"`prompt

string

required

Prompt describing the image to be generated, or describing how to edit the input image

Limits:

- Up to `32000` characters (counted by Unicode code points, works for CJK and other languages)

Maximum string length: `32000`

Example:

`"A beautiful colorful sunset over the ocean"`image\_urls

string\<uri>\[\]

Reference image URL list for image-to-image and image editing functions

Note:

- Number of input images per request: `1~16`
- Size of a single image: not exceeding `50MB`
- Supported file formats: `.jpeg`, `.jpg`, `.png`, `.webp`
- Image URLs must be directly accessible by the server, or the image URL should directly download when accessed (typically these URLs end with image file extensions, such as `.png`, `.jpg`)
- In image-to-image / image editing scenarios, the reference images themselves also incur additional image input token consumption

```
[
  "https://example.com/image1.png",
  "https://example.com/image2.png"
]
```mask\_url

string\<uri>

Inpainting mask URL — marks the region of the reference image to regenerate. Only valid in image edit mode (must be combined with `image_urls`); the mask is silently ignored in pure text-to-image requests.

Format requirements:

- Must be a PNG with an alpha channel: transparent pixels (`alpha < 255`) = regions to regenerate; opaque pixels = preserved
- Mask dimensions must exactly match the reference image dimensions (width × height in pixels)
- Single mask per request

Note:

- At least one reference image is required in `image_urls`; a mask sent alone has no effect
- Common errors:
	- `Invalid mask image format - mask image missing alpha channel`: the uploaded image has no alpha channel (JPEG, opaque PNG, etc.). Re-export the mask as a PNG with transparent regions.
		- `Invalid mask image format - mask size does not match image size`: the mask dimensions don't match the reference image. Resize the mask to the same pixel dimensions as your reference image.

Example:

`"https://example.com/mask.png"`size

string

default:auto

Size of the generated image. Supports both ratio format and explicit pixel format, defaults to `auto`

① Ratio format (recommended, 15 options)

- `1:1`: Square
- `1:2` / `2:1`: Extreme portrait / landscape
- `1:3` / `3:1`: Ultra portrait / landscape (3:1 limit)
- `2:3` / `3:2`: Standard portrait / landscape
- `3:4` / `4:3`: Classic portrait / landscape
- `4:5` / `5:4`: Common social media
- `9:16` / `16:9`: Mobile / desktop widescreen
- `9:21` / `21:9`: Ultra-wide

② Explicit pixel format: `WxH` (or `W×H`), e.g. `1024x1024`, `1536x1024`, `3840×2160`

- Both width and height must be multiples of `16`
- Each edge range: `[16, 3840]`
- Pixel budget: `655,360 ≤ width × height ≤ 8,294,400` (about 0.65 MP ~ 8.29 MP)
- Aspect ratio: `≤ 3:1`

③ `auto`: The model decides the size automatically (`resolution` does not apply in this mode)

Out-of-range handling:

- If a ratio + `resolution` combination exceeds the pixel budget, dimensions are automatically scaled down proportionally (e.g. 4K 2:1 → 3840×1920)

Example:

`"auto"`resolution

enum\<string>

default:1K

Resolution tier shortcut, only effective when `size` is a ratio; ignored in explicit pixel mode

Pixel budget rules (dimensions are derived from the target pixel count and the `size` ratio, aligned to multiples of 16):

- `1K`: ~1 MP (1024² = 1,048,576 pixels)
- `2K`: ~4 MP (2048² = 4,194,304 pixels)
- `4K`: ~8.29 MP (3840×2160 = 8,294,400 pixels, the maximum)

Landscape / square output dimensions (portrait dimensions are the landscape width/height swapped, e.g. `2:3` = `3:2` reversed):

| Ratio | 1K | 2K | 4K |
| --- | --- | --- | --- |
| `1:1` | 1024×1024 | 2048×2048 | 2880×2880 |
| `2:1` | 1456×720 | 2896×1456 | 3840×1920 \* |
| `3:1` | 1776×592 | 3552×1184 | 3840×1280 \* |
| `3:2` | 1248×832 | 2512×1680 | 3520×2352 |
| `4:3` | 1184×880 | 2368×1776 | 3312×2480 \* |
| `5:4` | 1152×912 | 2288×1824 | 3216×2576 |
| `16:9` | 1360×768 | 2736×1536 | 3840×2160 (UHD) |
| `21:9` | 1568×672 | 3136×1344 | 3840×1632 \* |

\* Marks combinations that are auto-downscaled to fit the pixel budget. Values are case-insensitive.

Available options:

`1K`,

`2K`,

`4K`

Example:

`"1K"`quality

enum\<string>

default:medium

Rendering quality that controls the model's "reasoning depth", directly affecting output token count and cost. Defaults to `medium`

| Value | Tile base | Relative cost (1024²) |
| --- | --- | --- |
| `low` | 16 | ~0.11× |
| `medium` | 48 | 1.0× |
| `high` | 96 | ~4.0× |

Available options:

`low`,

`medium`,

`high`

Example:

`"medium"`n

integer

default:1

Number of images to generate, each billed independently

Note:

- Text input tokens scale linearly with `n`

Required range: `1 <= x <= 10`

Example:

`1`callback\_url

string\<uri>

HTTPS callback address after task completion

Callback Timing:

- Triggered when task is completed, failed, or cancelled
- Sent after billing confirmation is completed

Security Restrictions:

- Only HTTPS protocol is supported
- Callback to internal IP addresses is prohibited (127.0.0.1, 10.x.x.x, 172.16-31.x.x, 192.168.x.x, etc.)
- URL length must not exceed `2048` characters

Callback Mechanism:

- Timeout: `10` seconds
- Maximum `3` retries on failure (retries after `1` second/ `2` seconds/ `4` seconds)
- Callback response body format is consistent with the task query API response format
- Callback address returning 2xx status code is considered successful, other status codes will trigger retry

Example:

`"https://your-domain.com/webhooks/image-task-completed"`

#### Response

Image generation task created successfullycreated

integer

Task creation timestamp

Example:

`1757156493`id

string

Task ID

Example:

`"task-unified-1757156493-imcg5zqt"`model

string

Actual model name used

Example:

`"gpt-image-2"`object

enum\<string>

Specific task type

Available options:

`image.generation.task`progress

integer

Task progress percentage (0-100)

Required range: `0 <= x <= 100`

Example:

`0`status

enum\<string>

Task status

Available options:

`pending`,

`processing`,

`completed`,

`failed`

Example:

`"pending"`task\_info

object

Asynchronous task information

Show child attributestype

enum\<string>

Task output type

Available options:

`text`,

`image`,

`audio`,

`video`

Example:

`"image"`usage

object

Usage and billing information

Show child attributes