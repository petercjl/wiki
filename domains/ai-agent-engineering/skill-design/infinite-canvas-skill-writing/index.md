---
title: 无限画板 Skill 写作知识库
type: playbook
created: 2026-06-11
updated: 2026-06-11
domain: ai-agent-engineering
tags: [ai-agent-engineering, skill, infinite-canvas, visual-production, prompt-engineering]
sources:
  - raw/my-temp-data/infinite-canvas-skill.md
  - /Users/pechen/.sealseek/workspaces/default/skills/skill-builder/SKILL.md
status: active
---

# 无限画板 Skill 写作知识库

本知识库用于支持 Peter 后续更快、更稳地创建无限画板中的 `skill.md`。它不是历史 skill 原文归档，而是从 15 个已使用的无限画板 skill 与「无限画板 Skill 生成器」规则中提炼出的写作规则、任务范式、工具约束、Prompt 模板和反坑清单。

## 适用场景

当 Agent 准备为无限画板创建或优化 skill 时，应先读取本入口，再按任务类型进入对应页面：

1. 明确无限画板 skill 与 SealSeek/OpenClaw skill 的边界。
2. 选择正确工具与参数，避免虚构工具能力。
3. 根据主图、详情页、批量优化、视频、成套视觉、产品设计等任务类型套用合适范式。
4. 在生成 `skill.md` 前完成规划、约束、失败场景和质量检查。
5. 把历史踩坑项转成创建前自检清单。

## 页面导航

- [[domains/ai-agent-engineering/skill-design/infinite-canvas-skill-writing/core-rules|核心规则]]：无限画板 skill 的结构边界、交互顺序、默认模型、确认机制和不可违反规则。
- [[domains/ai-agent-engineering/skill-design/infinite-canvas-skill-writing/tool-specs|工具规范]]：图片、视频、辅助、搜索与规划工具的适用条件、必填参数和禁用写法。
- [[domains/ai-agent-engineering/skill-design/infinite-canvas-skill-writing/task-patterns|任务范式]]：电商图片优化、主图、详情页、批量优化、视频、成套视觉、产品设计等常见 skill 模式。
- [[domains/ai-agent-engineering/skill-design/infinite-canvas-skill-writing/prompt-patterns|Prompt 模板]]：产品保真、风格迁移、营销转化、文案入图、视频镜头和批量处理的可复用写法。
- [[domains/ai-agent-engineering/skill-design/infinite-canvas-skill-writing/common-pitfalls|常见反坑库]]：已知高频错误与对应修正规则。
- [[domains/ai-agent-engineering/skill-design/infinite-canvas-skill-writing/quality-checklist|质量检查清单]]：新建或优化无限画板 skill 前后的检查项。
- [[domains/ai-agent-engineering/skill-design/infinite-canvas-skill-writing/agent-usage-template|Agent 使用模板]]：未来 Agent 写新 skill 前如何检索、规划和应用本知识库。

## 推荐读取顺序

### 新建普通图片/视频生成 skill

1. [[core-rules]]
2. [[tool-specs]]
3. [[task-patterns]] 中对应任务类型
4. [[prompt-patterns]] 中相关模板
5. [[quality-checklist]]

### 优化已有 skill 或修复出图问题

1. [[common-pitfalls]]
2. [[quality-checklist]]
3. [[prompt-patterns]]
4. 回到原 skill 做最小改动

### 创建复杂电商视觉工作流

1. [[core-rules]]
2. [[task-patterns]] 的“详情页/成套视觉/批量优化”
3. [[prompt-patterns]] 的“产品保真、营销转化、文案入图、批次规划”
4. [[agent-usage-template]]

## 来源范围

本知识库来自一个 9582 行的汇总源文件，包含 15 个无限画板 skill：白色松弛氛围杉居品牌营销转化图优化、白色松弛氛围杉居品牌详情图优化、电商图片营销优化、商品详情页视觉规划与分批生图、杉居品牌视觉图片批量优化、极简北欧风图片优化、主图生成、品牌策略详情页规划与分批生图、电商主图视频、静谧剧场、治愈系生图技能工作流、Single Image E-commerce Optimization、电商视觉全套生成、产品设计生图等。

详见 extraction notes：`_meta/extraction-notes/infinite-canvas-skill-writing-2026-06-11/`。
