---
title: 小红书风格 AI 生图知识库
type: playbook
created: 2026-06-13
updated: 2026-06-13
domain: 视觉制作
tags: [visual-production, xiaohongshu, ai-image-generation, prompt-engineering]
sources:
  - raw/articles/xiaohongshu-image-prompt-library-2026-06-13.md
  - _meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/coverage-matrix.md
status: active
---

# 小红书风格 AI 生图知识库

本目录用于把小红书内容逻辑转化为可复用的 AI 生图方法。它不是单纯的提示词堆叠，而是围绕“笔记目标 → 图片任务 → 画面结构 → prompt → 质量检查”组织的视觉生产知识库。

## 核心判断

小红书图片的首要任务不是“好看”，而是帮助笔记完成：

- **点击**：封面一眼说清这篇笔记解决什么问题。
- **搜索承接**：画面和标题自然覆盖品类词、人群词、场景词、功效词。
- **品类识别**：用户在手机端能快速判断这是哪个品类/产品。
- **场景代入**：让目标人群看到自己会遇到的使用场景。
- **痛点呈现**：把“不会选、踩坑、不实用、显廉价”等问题视觉化。
- **证据展示**：通过细节、对比、步骤、清单建立可信度。
- **收藏价值**：让图片像真实博主整理的有用卡片，而不是品牌硬广。

## 推荐读取顺序

1. [[domains/视觉制作/05-小红书风格AI生图/01-小红书风格生图原则|小红书生图底层原则]]
2. [[domains/视觉制作/05-小红书风格AI生图/05-信息流与搜索承接图片策略|信息流与搜索承接图片策略]]
3. [[domains/视觉制作/05-小红书风格AI生图/02-封面图类型|小红书封面类型库]]
4. [[domains/视觉制作/05-小红书风格AI生图/03-组图结构|小红书组图结构]]
5. [[domains/视觉制作/05-小红书风格AI生图/04-卖点转译|小红书卖点转译]]
6. [[domains/视觉制作/05-小红书风格AI生图/06-Prompt公式与变量库|Prompt 公式与变量库]]
7. [[domains/视觉制作/05-小红书风格AI生图/07-Prompt模板|小红书生图 Prompt 模板库]]
8. [[domains/视觉制作/05-小红书风格AI生图/08-QA检查清单|小红书生图 QA 检查表]]
9. [[domains/视觉制作/05-小红书风格AI生图/09-Agent使用模板：小红书风格生图|Agent 使用模板：小红书生图]]

## 与现有视觉知识的关系

- 本目录聚焦小红书内容种草场景。
- [[domains/视觉制作/01-电商视觉基础/02-电商图片营销策划与AI生图Playbook|电商图片营销策划与 AI 生图 Playbook]] 负责更通用的电商图片策划。
- [[domains/视觉制作/01-电商视觉基础/01-营销学理论在电商图片中的应用|营销学理论在电商图片中的应用]] 负责底层营销理论与图片任务关系。
- [[queries/xiaohongshu-image-generation|小红书风格生图查询入口]] 是未来 Agent 生成、改写或审核小红书图片 prompt 前的读取入口。
