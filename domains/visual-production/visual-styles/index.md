---
title: AI 生图风格库
type: concept
created: 2026-06-08
updated: 2026-06-08
domain: visual-production
tags: [visual-production, prompt-engineering, knowledge-base]
sources: []
status: active
---

# AI 生图风格库

本目录用于沉淀可被 AI 生图工具稳定调用的视觉风格。每个风格必须独立成目录，避免所有风格文件平铺在 `visual-styles/` 下。

## 目录协议

每个风格目录采用固定结构：

```text
visual-styles/<style-slug>/
├── index.md              # 风格定义：边界、色彩、材质、光线、构图、相邻风格区分
├── playbook.md           # 生图执行：prompt 骨架、场景配方、负向约束、QA
└── reference-gallery.md  # 参考图索引：素材路径、可复用点、风险点、推荐组合
```

如果某个风格后续积累很多内容，再按需增加：

- `palette.md`：色板和配色比例。
- `materials.md`：材质、表面、纹理和道具库。
- `shot-recipes.md`：按主图、详情页、海报、短视频首帧拆分的图位配方。
- `negative-boundaries.md`：与相邻风格的排除规则。

## 已入库风格

- [[domains/visual-production/visual-styles/minimal-scandinavian|极简北欧风]]：明亮哑光白、浅木/藤编、自然窗光、大面积留白和功能性居家陈列，适合家居收纳、浴室用品、棉麻织物、陶瓷和轻生活方式产品。

## 已入库品牌变体

- [[domains/visual-production/visual-styles/minimal-scandinavian/variants/shanju-light-kitchen-living|杉居轻厨房生活风]]：基于极简北欧风衍生的厨房工具品牌风格，覆盖明亮室内厨房、露台、庭院、野餐和户外轻料理，以浅蓝衬衫女性、橘猫、烧烤盘、调味罐和短句文案建立品牌记忆。

## 新增风格时的判定标准

一个风格进入本库前，必须能回答：

1. 这个风格的核心视觉变量是什么。
2. 它和相邻风格的边界是什么。
3. 哪些产品/类目适合，哪些不适合。
4. 生图时应该使用哪些参考图，权重如何分配。
5. prompt 中必须写入哪些正向变量和负向约束。
6. 输出图如何 QA，哪些结果算风格漂移。
