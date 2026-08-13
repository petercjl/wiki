---
title: Agent 网页设计规范
type: concept
created: 2026-08-06
updated: 2026-08-10
domain: AI Agent工程
tags: [ai-agent-engineering, product-design, visual-production, index]
sources:
  - raw/articles/compact-commerce-ui-2026-08-06/source-evidence.md
  - _meta/extraction-notes/compact-commerce-ui-2026-08-06/coverage-matrix.md
status: active
---

# Agent 网页设计规范

本目录规定 Agent 生成 HTML 报告、经营工作台、SaaS 后台和网页插件时的布局、视觉、组件、内容与验收标准。第一套正式方向命名为“紧凑商务工作台”（Compact Commerce UI）。

## 推荐读取顺序

1. [[domains/AI Agent工程/11-网页设计规范/01-网页UI设计总则|网页 UI 设计总则]]
2. [[domains/AI Agent工程/11-网页设计规范/02-紧凑商务工作台布局规范|紧凑商务工作台布局规范]]
3. [[domains/AI Agent工程/11-网页设计规范/03-设计变量与字体可读性|设计变量与字体可读性]]
4. [[domains/AI Agent工程/11-网页设计规范/04-模块与组件规范|模块与组件规范]]
5. [[domains/AI Agent工程/11-网页设计规范/05-电商数据报告内容规范|电商数据报告内容规范]]
6. [[domains/AI Agent工程/11-网页设计规范/06-验收与反模式|验收与反模式]]
7. [[domains/AI Agent工程/11-网页设计规范/07-HTML生成CLI与伴生Skill组合规范|HTML 生成 CLI 与伴生 Skill 组合规范]]

## 任务路由

- 生成或改版网页：从总则开始，按布局、变量、组件、内容、验收的顺序执行。
- 只调整可读性：优先读取设计变量与验收页。
- 只设计信息架构：优先读取布局与组件页。
- 电商数据报告：必须额外读取内容规范。
- 需要实际生成 HTML，或业务 Skill 需要复用网页能力：先读取 CLI 与伴生 Skill 组合规范，确认唯一源码、安装状态、contract 和调用边界。
- 自然语言入口：[[queries/网页报告与SaaS界面设计入口|网页报告与 SaaS 界面设计入口]]。

## 当前版本

- 规范版本：Compact Commerce UI v0.2
- 证据：AI 点睛七日数据报告两种视觉方向对照，以及两轮字号与布局反馈。
- 执行面：`commerce-ui 1.1.0` + `compact-workbench@1.0` + CLI 内唯一来源的 `compact-commerce-ui` 伴生 Skill。
- 适用：经营报告、营销投放报告、运营监控、内部 SaaS、插件面板。
- 待扩展验证：物流异常报告、利润报表、纯操作型插件与移动端。
