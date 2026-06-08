---
title: 极简北欧风 AI 生图 Playbook
type: playbook
created: 2026-06-08
updated: 2026-06-08
domain: visual-production
tags: [visual-production, prompt-engineering, workflow, product-design]
sources:
  - raw/webpages/visual-style/minimal-scandinavian-style-image-generation-2026-06-08.md
  - raw/webpages/visual-style/minimal-scandinavian-web-research-2026-06-08.md
  - raw/assets/visual-style/minimal-scandinavian/user-product-references/
  - _meta/extraction-notes/minimal-scandinavian-style-image-generation-2026-06-08/knowledge-unit-inventory.md
status: active
---

# 极简北欧风 AI 生图 Playbook

本页用于指导生图工具稳定生成极简北欧风产品图。使用时先读 [[domains/visual-production/visual-styles/minimal-scandinavian|极简北欧风视觉风格]]，再按本页选择场景、构图和 prompt 模板。

## 输入诊断

生成前先判断产品属于哪一种图位：

| 图位 | 目标 | 适合构图 |
| --- | --- | --- |
| 白底替代场景图 | 保持产品清晰，同时提高质感 | 产品 45%-60%，干净台面，少道具 |
| 生活方式主图 | 让用户想象使用场景 | 产品 35%-50%，窗光、搁板、收纳内容物 |
| 详情页氛围图 | 建立品牌风格 | 产品 25%-40%，大留白，空间更完整 |
| 功能收纳图 | 解释容量和用途 | 产品内放毛巾、瓶罐、零食、儿童用品等真实物件 |
| 系列图 | 展示多规格/多颜色 | 三角构图或阶梯构图，产品间距稳定 |

## Prompt 骨架

```text
为【产品】生成一张【图位】。
场景是【极简北欧居家空间/浴室台面/窗边搁板/玄关收纳柜/开放式厨房台面】。
核心风格：哑光白墙、浅木或藤编自然材质、米白和暖灰主色、窗边自然柔光、大面积留白、低道具密度、清爽温暖的日常生活感。
产品摆放：【单品偏左/三件套三角构图/放在白色搁板上/放在轻纹理石材台面上】。
辅助道具：【陶瓷花瓶/尤加利枝/棉麻毛巾/玻璃罐/浅木画框/白色杯子】，道具不抢产品。
镜头：【50mm product photography/eye-level/three-quarter view/soft depth of field】。
画面要求：产品纹理清晰、自然阴影、不过曝、无杂乱、无强广告感、无文字水印。
```

## 英文基础 prompt

```text
Create a realistic product lifestyle image in a minimal Scandinavian home interior. Use matte off-white walls, pale oak or natural woven seagrass textures, warm grey shadows, soft window light, large negative space, low prop density, and a quiet lived-in feeling. Place the product as the clear hero on a subtle white stone counter or simple white shelf. Add only functional props such as a matte ceramic vase, folded linen towel, glass jar, eucalyptus branch, or pale wood frame. Keep the palette off-white, warm grey, natural straw, pale wood, with small muted sage green or mist blue accents. Realistic product photography, soft shadows, tactile texture, clean composition, no clutter, no luxury marble hotel mood, no harsh studio lighting.
```

## 中文基础 prompt

```text
生成一张真实摄影质感的极简北欧风产品场景图。空间使用哑光白墙、浅木或天然藤编材质、暖灰阴影、窗边自然柔光和大面积留白。产品是画面主角，放在轻纹理白色石材台面或简洁白色搁板上。只加入有生活功能的少量道具，例如哑光陶瓷花瓶、棉麻毛巾、玻璃罐、尤加利枝、浅木画框。色彩以米白、暖灰、藤草本色、浅木色为主，少量鼠尾草绿或雾蓝点缀。画面清爽、温暖、安静、可居住，产品纹理清晰，自然阴影，不要杂乱，不要奢华酒店感，不要硬光棚拍。
```

## 针对藤编收纳篮的推荐 prompt

```text
生成一张方形电商产品生活方式图，主角是一组三个双色藤编/海草编织收纳篮，篮身下半部为天然麦秆色，上沿为米白色粗编织纹理。场景为极简北欧风浴室或家居收纳角落：哑光白墙、白色轻纹理石材台面、右侧柔和窗光，背景有浅木画框或白色壁龛。最大篮筐放在后方，中号和小号在前方形成稳定三角构图，产品占画面约 50%。可在一个篮子中放入低饱和雾蓝、青绿、暖灰毛巾卷，另一个篮子放少量玻璃罐和白色护理瓶，第三个篮子保持空置以展示容量。添加一支尤加利或小型绿植作为自然点缀。真实产品摄影，纹理锐利但光线柔和，米白、暖灰、浅木、藤草本色，清爽温暖，大面积留白，无杂乱包装，无高饱和颜色，无黑金奢华，无文字水印。
```

## 场景配方

| 场景 | 适合产品 | 必备元素 | 风险控制 |
| --- | --- | --- | --- |
| 白色石材台面 | 收纳篮、浴室用品、陶瓷、香薰 | 轻纹理白石、窗光、少量绿植 | 大理石纹理必须低对比，避免豪宅感 |
| 开放白搁板 | 收纳用品、瓶罐、布艺 | 白色架子、浅木画框、陶瓷罐 | 不要摆满整架，留出空层 |
| 浴室壁龛 | 毛巾、洗护、香薰 | 哑光白墙、壁龛、柔光 | 避免酒店 SPA 奢华化 |
| 玄关收纳柜 | 鞋包收纳、篮筐、家居整理 | 悬空柜、隐藏灯带、浅木把手 | 灯带只做暖层次，不要霓虹 |
| 窗边桌面 | 小家居、餐厨、香薰 | 白纱窗、植物、陶瓷杯 | 窗光不过曝，产品边缘要清楚 |

## 负向约束

必须显式写入的 negative constraints：

- no clutter, no crowded props
- no glossy luxury marble, no black and gold luxury style
- no harsh studio flash, no overexposed pure white background
- no saturated bright colors
- no plastic look, no cheap synthetic texture
- no Japanese wabi-sabi dark rustic mood unless requested
- no cream-only beige monochrome look
- no text, no logo hallucination, no watermark

## 参考图权重

当同时使用站酷空间图和用户产品图作为参考时，权重应这样分配：

1. 产品造型、比例、纹理、双色编织方式：优先用户 7 张参考图。
2. 空间背景、柜体、灯带、白木关系：参考 ZCOOL core case 01-15。
3. 风格理论、禁忌和提示词结构：参考本页与 [[domains/visual-production/visual-styles/minimal-scandinavian|极简北欧风视觉风格]]。

如果生成结果像室内装修效果图而产品不突出，下一轮 prompt 增加：`product is the hero, ecommerce product lifestyle image, product occupies 50% of the frame, keep the basket texture crisp`。

如果生成结果像棚拍白底图而缺少北欧生活感，下一轮 prompt 增加：`soft Scandinavian home interior, subtle shelf or counter context, window light, functional living props`。

## QA 清单

输出图合格时应满足：

- 产品第一眼清楚，纹理和结构没有变形。
- 白色区域有暖灰层次，不是纯白死片。
- 藤编/木/棉麻/陶瓷至少出现两种自然材质。
- 道具数量少，但有使用逻辑。
- 光线来自窗边或柔和室内光，自然阴影存在。
- 色彩低饱和，只有小面积绿植或雾蓝/灰绿点缀。
- 没有黑金、豪宅、大理石强纹、霓虹、广告字、随机 logo。

