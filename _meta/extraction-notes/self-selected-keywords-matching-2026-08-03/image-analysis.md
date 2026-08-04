---
title: 自选词广泛与精准匹配图片知识分析
type: source-summary
created: 2026-08-03
updated: 2026-08-03
domain: meta
tags: [llm-wiki, image-analysis, taobao, keyword-matching]
sources:
  - raw/assets/self-selected-keywords-matching-2026-08-03/
status: active
---

# 自选词广泛与精准匹配图片知识分析

| image_id | visual_claim | visible_text_or_relation | source_relation | confidence | ambiguity_or_boundary |
| --- | --- | --- | --- | --- | --- |
| IMG-01 | 关键词推荐是“添加更多关键词”后的一个标签页 | 流量智选、关键词组合、关键词推荐；五种推荐标签；相关性、预估展现、点击率、点击转化率、市场平均出价；右侧添加列表 | 证明入口和页面结构 | high | 截图显示 0/180，只是 2026-04-16 UI 快照 |
| IMG-02 | 方括号是精准匹配的可见标识 | `[婴儿服新生]` | 验证正文匹配定义 | high | 术语在官方资料中也写作“精确匹配” |
| IMG-03 | 无方括号是广泛匹配的可见标识 | `高腰裙` | 验证正文匹配定义 | high | 单张截图不能证明全部后台视图都采用同一展示方式 |
| IMG-04 | 关键词推荐按五类标签筛词 | 综合推荐、精准引流、类目优选、行业机会、助攻词；同一指标列 | 支撑五类定义和操作入口 | high | 指标算法和更新时间未说明 |
| IMG-05 | 自定义买词来自系统、市场搜索和商品属性 | 系统推荐词；淘宝搜索栏热搜关键词；宝贝属性词；可结合搜索习惯与属性组合 | 支撑三类买词来源 | high | 热搜和属性相关不等于适合当前计划，仍需筛选 |

## 正式化原则

- 5 张图均有独特操作或知识价值，全部嵌入既有正式页。
- UI 参数只作为日期快照；平台效果形容不转换为承诺。
- 方括号标识与结构化正文相互验证，不依赖 OCR 猜测。
