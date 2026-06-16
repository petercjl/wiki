---
title: 旺店通 API Skill 创建查询入口
type: query
created: 2026-06-03
updated: 2026-06-03
domain: 电商运营
tags: [ecommerce, erp, wangdian, api, skill]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
status: active
---

# 旺店通 API Skill 创建查询入口

## 用途

当用户提出“根据旺店通 API 知识库创建一个 skill”或“帮我用 AI 操作旺店通 ERP”时，AI Agent 应先读取本页，再读取能力地图和接口详情。

## 回答前必须读取

- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/index|旺店通开放平台 API 知识库]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/01-旺店通API能力地图|旺店通 API 能力地图]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/02-旺店通API Skill创建指南|旺店通 API Skill 创建指南]]

字段细节必须回到 raw：

- `raw/api/wangdian-openapi/wangdian-openapi-full-archive-2026-06-03.md`
- `raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json`
- `raw/api/wangdian-openapi/wangdian-openapi-compact-domains/视觉制作/05-小红书风格AI生图/index-2026-06-03.json`

## 需要向用户确认的信息

- 要操作的业务对象：库存、订单、货品、售后、采购、基础档案。
- 要执行的动作：查询、导出、创建、修改、同步回写、审核、取消。
- 是否允许调用会改变 ERP 状态的接口。
- 使用测试环境还是真实环境。
- API 凭证从哪里读取：环境变量、本地配置、密钥管理工具。
- 输出格式：Excel、CSV、Markdown、JSON、飞书表格等。
- 最大拉取时间范围、最大页数、最大记录数。

## 输出结构

```md
## Skill 目标

## 选用接口

## 输入参数

## 调用流程

## 输出格式

## 安全与确认机制

## 需要用户提供的配置

## 需要回到 raw 文档核对的字段
```

## 示例问题映射

| 用户问题 | 应读取接口 | 初步结论 |
|---|---|---|
| 获取商品库存情况并输出 Excel | `stock_query_Y`，必要时 `warehouse_query_Y`、`goods_query_Y` | 创建查询 + 导出类 skill，默认只读。 |
| 自动同步库存到平台 | `api_goods_stock_change_query_Y` + `api_goods_stock_change_ack_Y` | 涉及回写状态，需要确认机制。 |
| 查询订单并标记异常订单 | `trade_query_Y` + `sales_trade_modify_Y` | 查询可直接做，修改标记前要确认。 |
| 创建采购单 | `purchase_order_push_Y` | 创建业务单据，必须在提交前让用户确认。 |
