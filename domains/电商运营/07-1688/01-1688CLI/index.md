---
title: 1688 CLI
type: concept
created: 2026-07-16
updated: 2026-07-16
domain: 电商运营
tags: [ecommerce, 1688, cli, skill, ai-agent]
sources:
  - raw/webpages/1688-clawhub-skill-library-2026-07-16/
  - _meta/extraction-notes/1688-clawhub-skill-library-2026-07-16/coverage-matrix.md
status: active
---

# 1688 CLI

本专题将 7 个牛顿Hub/ClawHub Skill 编译成一套可供 Agent 路由和执行的 1688 CLI 知识。它不是已安装 CLI 的替代说明；命令、参数和 reference 文件必须以当前 Skill 包为准。

## 阅读顺序

1. [[domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图|1688 采购与分销 Agent 能力地图]]：确认能力、边界、命令和风险等级。
2. [[domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流|从找货到采购铺货的意图路由与工作流]]：根据搜索、寻源、询盘、铺货或交易阶段选择 Skill。
3. [[domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约|1688 电商 Skill 执行安全与输出契约]]：检查 reference、AK、安全确认、输出格式和失败处理。
4. [[queries/1688找货采购与铺货Agent入口|1688 找货采购与铺货 Agent 入口]]：自然语言任务的 Agent 路由入口。

## 七个来源 Skill

| Skill | 核心任务 | 典型入口 |
| --- | --- | --- |
| `1688-source-suppliers` | 查供应商、工厂、产业带 | 明确供应商查询关键词 |
| `1688-marketing-skill` | 招商活动、建议提报价、活动报名、商机推荐 | 活动或商机意图 |
| `1688 分销` | 选品、分销参谋、铺货、分销订单、催发、分销知识 | 分销全链路 |
| `1688 采购询盘寻源` | 发布模糊采购需求，等待平台匹配报价 | 商品名、数量、需求齐全 |
| `1688-product-find` | 文搜、图搜、链接找同款、比价 | 商品搜索或明确比价 |
| `88 生意通` | 线下交易采购单的创建、签署、收货、退款等 | 采购单状态与交易动作 |
| `1688-shopkeeper` | 搜品、绑定店铺、跨平台铺货、经营 FAQ | 店管家状态机 |

## 使用边界

- 不从本页猜测 CLI 参数；先读取当前 Skill 的 `SKILL.md`、对应 reference，必要时再查 `--help`。
- 不把浏览器或搜索引擎当成 API 失败后的业务数据兜底。
- 不记录或展示真实 AK。
- 写入操作的确认要求按具体能力判断，不能一概而论。
