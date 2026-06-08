---
title: 极简北欧风生图查询入口
type: query
created: 2026-06-08
updated: 2026-06-08
domain: visual-production
tags: [visual-production, prompt-engineering, workflow]
sources:
  - domains/visual-production/visual-styles/minimal-scandinavian/index.md
  - domains/visual-production/visual-styles/minimal-scandinavian/playbook.md
  - domains/visual-production/visual-styles/minimal-scandinavian/reference-gallery.md
status: active
---

# 极简北欧风生图查询入口

当 Agent 需要生成、改写或审核“极简北欧风”图片时，先读取：

1. [[domains/visual-production/visual-styles/minimal-scandinavian|极简北欧风视觉风格]]
2. [[domains/visual-production/visual-styles/minimal-scandinavian/playbook|极简北欧风 AI 生图 Playbook]]
3. [[domains/visual-production/visual-styles/minimal-scandinavian/reference-gallery|极简北欧风参考图索引]]

## Agent 输出结构

回答用户时按以下结构输出：

1. 判断产品是否适合极简北欧风。
2. 选择图位：主图、场景图、详情页氛围图、收纳功能图或系列图。
3. 给出风格变量：色彩、材质、光线、空间、构图、道具、负向约束。
4. 给出一版中文 prompt 和一版英文 prompt。
5. 如有参考图，说明使用哪几张作为产品锚点、哪几张作为空间锚点。
6. 给出 QA 检查清单，避免风格漂移。

## 快速模板

```text
请为【产品】生成极简北欧风【图位】。
先使用 [[domains/visual-production/visual-styles/minimal-scandinavian]] 判断风格边界，
再使用 [[domains/visual-production/visual-styles/minimal-scandinavian/playbook]] 输出 prompt。
如果产品是藤编收纳篮，优先参考 U03/U04/U06/U07 的产品陈列逻辑。
```
