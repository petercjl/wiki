---
title: 1688 牛顿Hub 电商 AI 技能库来源档案
type: source-summary
created: 2026-07-16
updated: 2026-07-16
domain: meta
tags: [llm-wiki, ecommerce, 1688, skill]
sources:
  - raw/webpages/1688-clawhub-skill-library-2026-07-16/
status: active
---

# 1688 牛顿Hub 电商 AI 技能库来源档案

## 来源范围

- 来源类型：Obsidian Web Clipper Markdown，7 个 ClawHub/牛顿Hub Skill 页面。
- 适配器：`llm-wiki-ingest/adapters/web-clipping.md`。
- 抓取日期：2026-07-16。
- 语言：中文，夹杂 CLI 命令、JSON、字段名和英文 Skill 标识。
- 原始网址：
  - `https://clawhub.1688.com/community/skill/66359`
  - `https://clawhub.1688.com/community/skill/66352`
  - `https://clawhub.1688.com/community/skill/66351`
  - `https://clawhub.1688.com/community/skill/66350`
  - `https://clawhub.1688.com/community/skill/10816`
  - `https://clawhub.1688.com/community/skill/42590`
  - `https://clawhub.1688.com/community/skill/41748`
- 原始本地目录：`/Users/pechen/大模型临时提示词/大模型临时提示词/Clippings/`；7 个输入文件名已与 `source-inventory.md` 中的 S01-S07 一一映射。

## 知识内容

本批资料不是一般电商教程，而是 1688 场景下的 Agent Skill 执行说明，覆盖供应商查询、招商活动与商机、分销选品铺货、采购询盘、文本/图片/链接找货与比价、88 生意通采购单、跨平台店管家。共同结构包括意图路由、CLI 能力、参考文档前置、AK 鉴权、读写风险等级、用户确认、禁止浏览器降级、输出契约和错误恢复。

## 已确认归类

- 用户否决了原推荐的 ERP 与系统工具位置，要求在电商运营中新增平台分类 `1688`，并在其下建立 `1688CLI`。
- 最终主位置：`domains/电商运营/07-1688/01-1688CLI/`。
- 融合方式：一个能力地图、一个采购/分销旅程路由页、一个执行与安全契约页；7 个 Skill 的命令、边界、示例与异常矩阵在三页中保留。
- 查询入口：`queries/1688找货采购与铺货Agent入口.md`。
- 相关记忆桥接：`domains/AI Agent工程/03-Skill设计/`，只链接其可复用的 Skill 设计模式，不把 1688 业务操作主体移入 AI Agent 工程域。
- 备选：在 `domains/电商运营/` 下新建独立平台目录 `07-1688/`。此方案平台识别更直观，但会把 API/CLI/Agent 工具与普通平台运营规则混在一起，当前不优先。

## 现有记忆检索

- 现有 `domains/电商运营/30-ERP与系统工具/` 已承载旺店通 API 和快递 100，语义上最接近“电商业务系统 + Agent 自动化接口”。
- `domains/电商运营/01-通用电商方法/05-产品开发与供应链管理系统/02-供应商开发与分级管理.md` 提供供应商管理方法，但不包含 1688 CLI/Skill 执行契约，宜建立相关记忆而非合并。
- `domains/AI Agent工程/03-Skill设计/` 已有 Skill 世界观、测试和可移植设计方法，可作为结构设计的相关记忆，但不是 1688 业务知识的主归属。
- 未发现现有 1688 牛顿Hub、`1688-product-find`、采购询盘或 88 生意通正式页面。

## 时效与敏感性

- 所有命令名、参数、授权流程、页面入口、版本号、默认值和业务限制均为 2026-07-16 抓取快照，实际执行前应读取已安装 Skill 的当前 `SKILL.md`、对应 reference 和 CLI `--help`。
- AK 是敏感凭证；正式知识只保留安全边界，不记录任何真实 AK。
- 来源之间存在契约差异，例如有的写操作必须明确确认/二次确认，有的采购询盘在字段齐全时允许直接发起；编译时必须按能力分别保留，不能强行统一。

## 状态

- 原文归档：完成。
- 来源盘点：完成。
- 归类确认：用户已于 2026-07-16 明确确认 `电商运营/1688/1688CLI` 结构。
- 正式知识页、查询入口、索引与日志：已写入，等待最终验证。
