---
title: Word 文档格式与模板设计来源档案
type: source-summary
created: 2026-07-30
updated: 2026-07-30
domain: meta
tags: [llm-wiki, word, document-design, template]
sources:
  - raw/webpages/word-document-format-design-research-2026-07-30/
status: active
---

# Word 文档格式与模板设计来源档案

## 研究问题

本研究不讨论“用什么代码生成 DOCX”，而回答三个更基础的问题：

1. Word 文档有哪些可复用的格式、结构和组件？
2. 每种格式分别解决什么阅读问题，适合什么场合，又有哪些误用风险？
3. 如何把这些格式组合成针对报告、提案、复盘、SOP 等文档类型的“模板菜谱”？

## 来源范围

- 5 个机构级 Word 模板或排版规范：Microsoft、英国 DWP、英国 DfT、Utrecht University、Kansas State University。
- 2 个 GitHub 相关样本：GitHub Docs 内容类型模板、Wordinator 的 DOTX 样式模板机制。
- 适配器：Web clipping。
- 抓取日期：2026-07-30。
- 原始归档：`raw/webpages/word-document-format-design-research-2026-07-30/`。

## 来源角色

- Microsoft 模板站：文档类型与商务场景。
- DWP/DfT：长报告结构、表格、图表、可访问性和发布检查。
- Utrecht/K-State：模板复杂度分层、长文档自动化与样式维护。
- GitHub Docs：内容类型决定模板骨架。
- Wordinator：命名样式和 DOTX 如何成为稳定设计资产。

## 初步判断

Word 文档设计可以拆成四层：

1. **语义层**：标题、正文、引语、列表、题注、注释、数据、行动项各自扮演什么角色。
2. **导航层**：层级、目录、页码、页眉页脚、交叉引用如何帮助定位。
3. **视觉层**：字体、字号、行距、段距、色彩、留白、对齐、边框、底纹如何建立秩序和节奏。
4. **页面层**：纸张、页边距、分栏、分页、分节、横竖版和跨页规则如何承载内容。

模板则是在明确文档任务后，把四层中的选项组合成一套可重复使用、可维护、可验证的配方。

## 研究边界

- 本批建立第一版知识模型，不宣称穷尽 Word 所有功能。
- 机构规范中的具体字体和字号是场景化基线，不会被编译成普遍真理。
- GitHub 中大量项目聚焦 DOCX 生成、填充和转换；本研究仅保留与样式资产、内容模型和模板管理相关的知识。
- 用户已确认正式位置为 `domains/AI Agent工程/格式化文档/`；Word 第一版正式知识页已创建。
