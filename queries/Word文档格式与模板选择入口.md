---
title: Word文档格式与模板选择入口
type: query
created: 2026-07-30
updated: 2026-07-30
domain: AI Agent工程
tags: [word, formatting, template, query]
sources:
  - raw/webpages/word-document-format-design-research-2026-07-30/
  - _meta/extraction-notes/word-document-format-design-research-2026-07-30/coverage-matrix.md
status: active
---

# Word 文档格式与模板选择入口

## 何时使用

- “帮我优化这个 Word 文档的格式。”
- “这类报告应该使用什么排版？”
- “有哪些 Word 格式，分别适合什么场合？”
- “帮我设计一个可复用的 Word 模板。”
- “检查这个 DOCX 是否美观、易读、专业。”
- “用 Node.js 生成 Word 时应该实现哪些样式和组件？”

## 必读顺序

1. [[domains/AI Agent工程/格式化文档/word文档/01-Word文档格式系统|Word 文档格式系统]]
2. [[domains/AI Agent工程/格式化文档/word文档/02-Word格式适用场景与误用|Word 格式适用场景与误用]]
3. 按任务选择：
   - 设计模板：[[domains/AI Agent工程/格式化文档/word文档/03-Word模板菜谱设计方法|Word 模板菜谱设计方法]]
   - 选择文档结构：[[domains/AI Agent工程/格式化文档/word文档/04-常用Word文档菜谱库|常用 Word 文档菜谱库]]
4. 完成前使用 [[domains/AI Agent工程/格式化文档/word文档/05-Word文档设计与验收清单|Word 文档设计与验收清单]]。

## Agent 标准流程

1. 读取原文内容、现有样式、页面设置、表格、图片、页眉页脚和分节。
2. 判断文档类型、读者任务、屏幕/打印场景、篇幅和品牌约束。
3. 先修正明显的结构与语义问题，再选择菜谱和页面原型。
4. 把重复的直接格式归并为命名样式。
5. 建立标题层级、导航、正文节奏、数据表达和行动信息。
6. 保留可编辑性；不要用截图、空格或文本框代替正文结构。
7. 生成或修改后渲染检查，并运行结构、可访问性和发布验收。
8. 向用户说明语义修订、格式变化、输出路径和剩余风险。

## 向用户补充索取

- Word 文件；
- 读者与用途；
- 是否有品牌字体、颜色、徽标或既有模板；
- 主要在屏幕阅读还是打印；
- 是否允许修订明显语义错误；
- 交付 DOCX、PDF，还是两者。

缺少品牌要求时可以使用克制、中性的专业系统继续工作；缺少读者和用途时，应从文档内容推断并明确说明假设。

## 技术实现原则

Node.js 包、Word CLI 或 Agent Skill 是执行层。它们应实现知识库定义的：

- 命名样式；
- 页面原型；
- 自动目录、编号、题注和交叉引用；
- 组件适用规则；
- 渲染与验收。

不要让库的 API 能力反过来决定文档结构。
