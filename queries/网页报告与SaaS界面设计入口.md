---
title: 网页报告与 SaaS 界面设计入口
type: query
created: 2026-08-06
updated: 2026-08-10
domain: AI Agent工程
tags: [product-design, dashboard, saas, html, query]
sources:
  - raw/articles/compact-commerce-ui-2026-08-06/source-evidence.md
  - _meta/extraction-notes/compact-commerce-ui-2026-08-06/coverage-matrix.md
status: active
---

# 网页报告与 SaaS 界面设计入口

## 触发问题

- 生成、美化或改版 HTML 数据报告。
- 设计经营工作台、SaaS 后台、管理面板或网页插件。
- 沿用“紧凑插件面板”“紧凑商务工作台”风格。
- 检查网页字体太小、模块太乱、导航不清或数据口径不足。

## 必读顺序

1. [[domains/AI Agent工程/11-网页设计规范/01-网页UI设计总则|网页 UI 设计总则]]
2. [[domains/AI Agent工程/11-网页设计规范/02-紧凑商务工作台布局规范|紧凑商务工作台布局规范]]
3. [[domains/AI Agent工程/11-网页设计规范/03-设计变量与字体可读性|设计变量与字体可读性]]
4. [[domains/AI Agent工程/11-网页设计规范/04-模块与组件规范|模块与组件规范]]
5. [[domains/AI Agent工程/11-网页设计规范/06-验收与反模式|验收与反模式]]
6. [[domains/AI Agent工程/11-网页设计规范/07-HTML生成CLI与伴生Skill组合规范|HTML 生成 CLI 与伴生 Skill 组合规范]]

## 条件读取

- 电商经营、广告投放和店铺数据：再读 [[domains/AI Agent工程/11-网页设计规范/05-电商数据报告内容规范|电商数据报告内容规范]]。
- 特定平台诊断：继续进入对应的电商运营查询页，本入口不替代平台知识。
- 品牌故事、活动页或作品集：只复用可读性和层级原则，不默认套用工作台骨架。

## 标准执行

1. 运行 `commerce-ui doctor`，确认 CLI、伴生 Skill 与所需 contract；缺少 Skill 时从 CLI 官方来源安装，不复制模板。
2. 判断任务是否需要多区域导航、全局搜索和时间范围。
3. 建立页面信息架构与决策链，再选择组件。
4. 应用设计变量与字号下限。
5. 使用豆腐块系统表达模块权重。
6. 接入真实数据，核对单位、周期、归因、样本和总计。
7. 通过 ViewModel 调用 CLI，完成交互、响应式、打印与依赖检查。
8. 按验收页逐项检查后再交付。

## 输出边界

- 不因模板存在而伪造功能或业务结论。
- 不把汇总指标当作原因证据。
- 不以小字号换取信息密度。
- 不在可分享网页或 Skill 中写入私有绝对路径、账号或凭证。
