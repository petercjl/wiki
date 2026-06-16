---
title: 电商运营知识域平台优先改造计划
type: decision
created: 2026-06-14
updated: 2026-06-14
domain: 电商运营
tags: [ecommerce, reorganization, platform, memory-first]
status: approved
---

# 电商运营知识域平台优先改造计划

## 改造判断

本次目标是 `domains/电商运营/`。

机械扫描结果：

```text
Scanned: 55 markdown pages
SHELL: 0   THIN: 0   OK: 55
```

因此本域不是大面积 shell/thin 或反浓缩问题，而是知识分类和长期检索问题：

- 当前目录以 `learning-paths/`、`platform-entry/`、`marketing-tools/`、`api/` 等来源或功能英文目录为主。
- Peter 检索电商知识时，首先会区分平台：淘宝/天猫、京东、拼多多、抖音、小红书、跨境等。
- 也存在平台无关的通用电商知识，例如经营咨询、平台合作判断、平台结算、供应链、团队、用户经营等。
- 财税与经营财务已经拆为独立 `domains/财税与经营财务/`，电商运营中只保留常用入口和相关记忆链接。

## 目标结构

```text
domains/电商运营/
├── 01-通用电商方法/
│   ├── 01-电商企业咨询与交付/
│   ├── 02-平台渠道与入驻合作/
│   └── 03-平台结算与经营财务/
├── 02-淘宝天猫/
│   ├── 01-淘宝运营速成指南/
│   ├── 02-淘宝营销工具/
│   └── 03-天猫超市入驻合作/
├── 03-京东/
├── 04-拼多多/
├── 05-抖音/
├── 06-小红书/
├── 20-跨境电商/
├── 30-ERP与系统工具/
└── domains/视觉制作/05-小红书风格AI生图/index.md
```

空平台目录可以保留为未来承载位置，但不强行创建空正式页面。

## 迁移融合表

| 旧路径 | 当前角色 | 新路径 | 处理方式 |
| --- | --- | --- | --- |
| `domains/电商运营/` | 电商运营一级域 | `domains/电商运营/` | 顶层 domain 中文化 |
| `learning-paths/consulting-logic/` | 电商企业咨询与交付体系 | `01-通用电商方法/01-电商企业咨询与交付/` | 整目录迁移，保留阅读顺序 |
| `finance-accounting/ecommerce-platform-settlement-accounting.md` | 平台结算与经营财务桥接 | `01-通用电商方法/03-平台结算与经营财务/01-电商平台结算时间口径财务核算方法.md` | 移动并保留与财税域关联 |
| `platform-entry/domains/视觉制作/05-小红书风格AI生图/index.md` | 平台入驻来源包入口 | `01-通用电商方法/02-平台渠道与入驻合作/domains/视觉制作/05-小红书风格AI生图/index.md` | 迁移为跨平台入口 |
| `platform-entry/tmall-supermarket-vs-jd-self-operated-comparison.md` | 天猫超市与京东自营对比 | `01-通用电商方法/02-平台渠道与入驻合作/01-天猫超市与京东自营合作模式对比.md` | 迁移为跨平台比较页 |
| `platform-entry/platform-entry-domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/05-小红书风格AI生图/09-Agent使用模板：小红书风格生图.md` | 平台入驻诊断模板 | `01-通用电商方法/02-平台渠道与入驻合作/02-平台入驻与自营合作诊断模板.md` | 迁移为通用诊断入口 |
| `learning-paths/taobao-operation-quick-guide-81-rules/` | 淘宝运营图书编译路径 | `02-淘宝天猫/01-淘宝运营速成指南/` | 整目录迁移，保留来源和阅读顺序 |
| `marketing-tools/*.md` | 淘宝营销工具专题 | `02-淘宝天猫/02-淘宝营销工具/` | 迁移并序号化 |
| `domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbooks/taobao-marketing-tool-selection.md` | 淘宝营销工具选择 domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook | `02-淘宝天猫/02-淘宝营销工具/04-淘宝营销工具选择Playbook.md` | 合入淘宝营销工具目录 |
| `platform-entry/tmall-supermarket-cooperation-guide.md` | 天猫超市合作 | `02-淘宝天猫/03-天猫超市入驻合作/01-天猫超市合作与入驻说明.md` | 平台归类 |
| `platform-entry/jd-self-operated-entry-guide.md` | 京东自营合作 | `03-京东/01-京东自营入驻解析.md` | 平台归类 |
| `learning-paths/cross-border-ecommerce-sme-globalization/` | 跨境电商出海知识 | `20-跨境电商/01-中小企业跨境出海/` | 独立跨境板块 |
| `api/wangdian/` | 旺店通 ERP API | `30-ERP与系统工具/01-旺店通开放平台API/` | 工具系统归类 |
| `learning-paths/ecommerce-tax-equity-strategic-finance/domains/视觉制作/05-小红书风格AI生图/index.md` | 财税旧路径指针 | 删除旧 learning-path 位置或改为跨域指针 | 财税主知识已在 `domains/财税与经营财务/` |

## 关联式融合原则

- 淘宝书中有通用经营方法，但来源语境是淘宝，先归入 `02-淘宝天猫/01-淘宝运营速成指南/`；通用电商方法页以后可通过“相关记忆”引用。
- 平台结算页保留在电商域作为运营视角入口，同时与 `财税与经营财务` 相关页面互链。
- 财税课程旧路径不再作为电商 learning path 使用，电商域只保留指向财税域的入口。
- 旺店通属于跨平台 ERP/系统工具，不归入某个单一平台。

## Skill 需要补充的规则

本次暴露出一个需要固化的规则：

> 电商知识入库时，先判断是否平台专属；平台专属知识进入对应平台目录，平台无关知识进入通用电商方法；ERP/API/工具进入系统工具；课程、书籍、网页只是来源，不决定最终目录。

该规则应补入 `llm-wiki-ingest` 的 Memory-First domain classification 和 placement references。

## QA 要求

- `placeholder_scan.py` 仍为 `SHELL: 0`, `THIN: 0`。
- 正式库中无 `domains/电商运营/` 旧路径残留。
- 新路径下 wikilink 无缺失。
- 根 `domains/视觉制作/05-小红书风格AI生图/index.md`、`SCHEMA.md`、`AGENTS.md`、domain `domains/视觉制作/05-小红书风格AI生图/index.md` 和 `log.md` 已更新。
- 与 `财税与经营财务`、`domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/domains/视觉制作/05-小红书风格AI生图/index` 的相关记忆链接仍可用。
