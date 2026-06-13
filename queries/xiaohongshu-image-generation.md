---
title: 小红书风格生图查询入口
type: query
created: 2026-06-13
updated: 2026-06-13
domain: visual-production
tags: [visual-production, xiaohongshu, ai-image-generation, query]
sources:
  - raw/articles/xiaohongshu-image-prompt-library-2026-06-13.md
  - _meta/extraction-notes/xiaohongshu-image-prompt-library-2026-06-13/coverage-matrix.md
status: active
---

# 小红书风格生图查询入口

当 Agent 需要生成、改写、审核小红书风格图片 prompt 时，先读本页，再按任务读取具体页面。

## 入口判断

| 用户任务 | 必读页面 |
| --- | --- |
| 生成单张小红书封面 | [[domains/visual-production/xiaohongshu-image-generation/cover-image-types|小红书封面类型库]]、[[domains/visual-production/xiaohongshu-image-generation/prompt-templates|小红书生图 Prompt 模板库]] |
| 生成小红书组图 | [[domains/visual-production/xiaohongshu-image-generation/image-set-structure|小红书组图结构]]、[[domains/visual-production/xiaohongshu-image-generation/prompt-templates|小红书生图 Prompt 模板库]] |
| 判断信息流/搜索图 | [[domains/visual-production/xiaohongshu-image-generation/feed-vs-search-image-strategy|信息流与搜索承接图片策略]] |
| 把产品卖点变成画面 | [[domains/visual-production/xiaohongshu-image-generation/selling-point-translation|小红书卖点转译]] |
| 检查生成结果是否合格 | [[domains/visual-production/xiaohongshu-image-generation/qa-checklist|小红书生图 QA 检查表]] |
| 给 Agent 自动化使用 | [[domains/visual-production/xiaohongshu-image-generation/agent-usage-template|Agent 使用模板：小红书生图]] |

## 核心页面

- [[domains/visual-production/xiaohongshu-image-generation/index|小红书风格 AI 生图知识库]]
- [[domains/visual-production/xiaohongshu-image-generation/xiaohongshu-image-generation-principles|小红书生图底层原则]]
- [[domains/visual-production/xiaohongshu-image-generation/feed-vs-search-image-strategy|信息流与搜索承接图片策略]]
- [[domains/visual-production/xiaohongshu-image-generation/cover-image-types|小红书封面类型库]]
- [[domains/visual-production/xiaohongshu-image-generation/image-set-structure|小红书组图结构]]
- [[domains/visual-production/xiaohongshu-image-generation/selling-point-translation|小红书卖点转译]]
- [[domains/visual-production/xiaohongshu-image-generation/prompt-formula-and-variable-library|Prompt 公式与变量库]]
- [[domains/visual-production/xiaohongshu-image-generation/prompt-templates|小红书生图 Prompt 模板库]]
- [[domains/visual-production/xiaohongshu-image-generation/qa-checklist|小红书生图 QA 检查表]]

## 最小输入

如果用户没有提供完整信息，Agent 至少需要补齐或合理假设：

```text
产品/品类：
目标人群：
使用场景：
核心痛点：
核心结果：
内容场景：信息流 / 搜索
图片目标：点击 / 收藏 / 搜索承接 / 种草转化
```

## 默认输出

优先输出：

1. 图片策略判断。
2. 推荐封面类型或组图结构。
3. 可直接用于生图的正向 prompt。
4. 负面 prompt。
5. QA 自检。
