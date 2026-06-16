---
title: 旺店通 API Skill 创建指南
type: domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook
created: 2026-06-03
updated: 2026-06-03
domain: 电商运营
tags: [ecommerce, erp, wangdian, api, skill]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
  - raw/api/wangdian-openapi/wangdian-openapi-full-archive-2026-06-03.md
status: active
---

# 旺店通 API Skill 创建指南

## 用途

当用户要求“根据旺店通 API 知识库创建一个 skill”时，先读本页。本页把 API 文档转化为可执行的 skill 设计流程，避免直接从 77 个接口里盲选。

## 创建 Skill 的基本流程

1. 明确用户要操作的业务对象：库存、订单、货品、售后、采购或基础档案。
2. 判断动作类型：查询、导出、创建、修改、同步回写、审核、取消。
3. 优先选择只读接口；涉及创建/修改/回写/审核/取消时，必须设计用户确认步骤。
4. 从 [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/01-旺店通API能力地图|旺店通 API 能力地图]] 选择候选接口。
5. 到对应分类使用手册核对字段、请求示例和响应示例；必要时再回到 raw 全量归档。
6. 设计输入参数、分页策略、时间窗口、错误处理和输出格式。
7. 如果输出 Excel，使用字段映射表固定列名和顺序。

## 全局认证与请求

所有接口通常需要公共参数：

| 参数 | 含义 | 注意 |
|---|---|---|
| `sid` | 卖家账号 | 由旺店通分配给 ERP 购买方。 |
| `appkey` | 接口账号 | 需要从账号配置获取。 |
| `timestamp` | 时间戳 | 北京时间 1970-01-01 08:00:00 起至当前总秒数；最大时间误差 5 分钟。 |
| `sign` | 签名 | 由 API 输入参数计算。创建真实 skill 时必须补齐签名算法。 |

请求地址：

```text
测试环境：https://openapi.ali.huice.cc/openapi/<接口文件>.php
正式环境：https://openapi.huice.com/openapi/<接口文件>.php
```

## Skill 设计安全规则

- 查询和导出类 skill 可以直接执行，但要避免泄露敏感数据。
- 创建、修改、回写、审核、取消类 skill 必须在执行前向用户展示即将提交的数据并请求确认。
- 不要把 `sid`、`appkey`、`appsecret` 写入 skill 文件；应从环境变量或本地密钥配置读取。
- 所有分页查询都要设置最大页数或最大记录数，避免无限拉取。
- 时间范围查询要控制跨度；例如 `stock_query_Y` 的 `start_time` 和 `end_time` 最大跨度为 30 天。

## 示例：创建“获取商品库存并输出 Excel”的 Skill

### 目标

用户输入商品编码、仓库或时间范围，skill 调用旺店通库存接口获取库存，并导出 Excel。

### 推荐接口

首选：

- `stock_query_Y`：查询库存成本和可用库存数据。

辅助：

- `warehouse_query_Y`：查询仓库档案，用于把仓库编号/名称补齐。
- `goods_query_Y`：查询货品档案，用于补齐货品分类、货品名称或规格信息。

### 输入参数

| 参数 | 对应 API 字段 | 说明 |
|---|---|---|
| 开始时间 | `start_time` | 格式 `yyyy-MM-dd HH:mm:ss`，与结束时间最大跨度 30 天。 |
| 结束时间 | `end_time` | 格式 `yyyy-MM-dd HH:mm:ss`。 |
| 商家编码 | `spec_no` | 单个商家编码。 |
| 商家编码列表 | `spec_no_list` | JSON 字符串数组，上限 200 条。 |
| 仓库 ID | `warehouse_id` | 可选。 |
| 仓库编号 | `warehouse_no` | 可选。 |
| 是否残次品 | `defect` | 0 否，1 是。 |
| 分页大小 | `page_size` | 1-1000，默认 100。 |
| 页号 | `page_no` | 默认从 0 开始。 |

### Excel 字段建议

| Excel 列 | API 字段 |
|---|---|
| 商家编码 | `spec_no` |
| 货品编号 | `goods_no` |
| 货品名称 | `goods_name` |
| 规格名称 | `spec_name` |
| 条形码 | `barcode` |
| 仓库编号 | `warehouse_no` |
| 仓库名称 | `warehouse_name` |
| 库存量 | `stock_num` |
| 可用库存 | `available_num` |
| 虚拟库存 | `virtual_num` |
| 锁定量 | `stock_lock_num` |
| 成本价 | `cost_price` |
| 平均成本价 | `avg_cost_price` |
| 是否残次品 | `defect` |
| ERP 更新时间 | `modified` |

### 查询逻辑

1. 校验输入：时间范围和商家编码至少有一个不为空。
2. 如果传入多个商家编码，每批最多 200 个。
3. 按 `page_no` 从 0 开始分页拉取。
4. 当返回记录少于 `page_size` 或达到用户指定最大记录数时停止。
5. 将响应中的 `stocks` 数组转换为 Excel 行。
6. 保留 API 原始响应摘要和错误码，方便排错。

## 相关页面

- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/domains/视觉制作/05-小红书风格AI生图/index|旺店通开放平台 API 知识库]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/01-旺店通API能力地图|旺店通 API 能力地图]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/04-旺店通库存类API使用手册|旺店通库存类 API 使用手册]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
