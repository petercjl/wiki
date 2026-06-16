---
title: 品牌策略与视觉制作知识域边界改造计划
type: decision
created: 2026-06-14
updated: 2026-06-14
domain: meta
tags: [llm-wiki, reorganization, brand-strategy, domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/domains/视觉制作/05-小红书风格AI生图/index]
status: approved
---

# 品牌策略与视觉制作知识域边界改造计划

## 背景

`domains/品牌策略/` 和 `domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/` 都包含“品牌视觉”相关知识，但二者不应合并。品牌策略中的品牌视觉服务于定位、心智、差异化感知、记忆资产和品牌长期一致性；视觉制作中的品牌视觉服务于图片、视频、风格、拍摄、AI 生图、版式和生产工作流。

## 审计结果

- `brand-strategy`：88 个 Markdown 页面，`SHELL: 0`、`THIN: 0`。
- `domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/domains/视觉制作/05-小红书风格AI生图/index`：42 个 Markdown 页面，其中 `AI 在商业视觉设计中的应用方法与实践` 7 个章节页为 P0 空壳，需要先从 raw transcript 补实。

## 目标结构

```text
domains/品牌策略/
├── 01-品牌基础与增长方法/
├── 02-品类心智与差异化/
├── 03-产品战略与大单品/
├── 04-品牌视觉资产/
├── 90-样本/
└── domains/视觉制作/05-小红书风格AI生图/index.md

domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/
├── 01-电商视觉基础/
├── 02-品牌视觉标准化/
├── 03-AI商业视觉/
├── 04-AI生图风格库/
├── 05-小红书风格AI生图/
├── 06-AI视频/
└── domains/视觉制作/05-小红书风格AI生图/index.md
```

## 边界规则

| 问题 | 主知识域 | 处理方式 |
| --- | --- | --- |
| 品牌定位、心智、品类、人群、产品线、大单品 | 品牌策略 | 作为品牌方法论沉淀 |
| 品牌视觉资产、记忆符号、ABC 分层、视觉世界观的战略意义 | 品牌策略 | 放入 `04-品牌视觉资产/`，互链视觉制作 |
| 主图、详情页、场景图、证据图、拍摄、版式、AI 生图和视频 | 视觉制作 | 作为视觉生产方法沉淀 |
| 品牌视觉标准化、视觉系统、记忆符号的制作规范 | 视觉制作 | 放入 `02-品牌视觉标准化/`，互链品牌策略 |
| 同一知识点既涉及战略又涉及制作 | 双向桥接 | 不合并；各自保留问题意识，并在“相关记忆”中解释关系 |

## 执行步骤

1. 从 raw transcript 补实 `AI 商业视觉` 7 个空壳页。
2. 重命名顶层域：`brand-strategy/` -> `品牌策略/`，`domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/domains/视觉制作/05-小红书风格AI生图/index/` -> `视觉制作/`。
3. 迁移并中文序号化目录与页面。
4. 补充品牌视觉跨域桥接页。
5. 更新 root domains/视觉制作/05-小红书风格AI生图/index、domain domains/视觉制作/05-小红书风格AI生图/index、SCHEMA、AGENTS、query pages、extraction notes 和内部 wikilinks。
6. 更新 LLM Wiki skill 的跨域边界规则。
7. 运行 placeholder scan、链接检查和旧路径残留检查。
