---
title: 旺店通 API 能力地图
type: concept
created: 2026-06-03
updated: 2026-06-03
domain: ecommerce-ops
tags: [ecommerce, erp, wangdian, api]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-compact-index-2026-06-03.json
status: active
---

# 旺店通 API 能力地图

## 摘要

本页把旺店通 77 个开放接口整理成业务能力地图，用于后续创建 AI skill 时快速选择接口。查字段细节时回到 `raw/api/wangdian-openapi/wangdian-openapi-full-archive-2026-06-03.md` 或 JSON 原始抓取。

## 能力总览

| 能力域 | 接口数量 | 主要用途                                 |
| --- | ---: | ------------------------------------ |
| 订单类 |   17 | 创建、查询、修改订单，物流同步，订单标签、备注、小时达数据回传。     |
| 库存类 |   23 | 查询库存、出入库、盘点、调拨、分拣、运营仓、委外出入库和序列号。     |
| 货品类 |   10 | 查询或创建平台货品、系统货品、组合装、分类、条码和唯一码打印。      |
| 基础类 |   16 | 查询店铺、仓库、物流、员工、供应商、标签，以及业务单据审核/取消/驳回。 |
| 售后类 |    6 | 查询退换、创建原始退款单、系统售后单、退货入库单。            |
| 采购类 |    5 | 查询和创建采购单、采购退货单、采购申请单。                |

## 常见 AI 自动化需求映射

| 用户需求              | 首选接口                                                         | 辅助接口                                                                   | 输出建议                                          |
| ----------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------- |
| 获取商品库存情况并输出 Excel | `stock_query_Y` 查询可用库存                                       | `warehouse_query_Y` 查询仓库；`goods_query_Y` 查询货品档案                        | Excel 字段建议含商家编码、货品名、规格名、仓库、库存量、可用库存、成本价、更新时间。 |
| 查询全量库存快照          | `stock_full_query_Y` 全量查询库存                                  | `warehouse_query_Y`、`goods_query_Y`                                    | 适合做周期性库存盘点或 BI 基础表。                           |
| 查询库存变化并同步平台       | `api_goods_stock_change_query_Y` 查询库存同步                      | `api_goods_stock_change_ack_Y` 库存同步回写                                  | 适合“拉取变化 -> 同步外部平台 -> 回写结果”的闭环。                |
| 查询 ERP 内系统订单      | `trade_query_Y` 系统订单查询                                       | `sales_trade_modify_Y` 修改系统订单                                          | 适合订单看板、异常订单筛选、订单标记。                           |
| 查询平台原始订单          | `vip_api_trade_query_Y` 查询原始订单                               | `trade_push_Y` 创建原始订单                                                  | 适合平台订单与 ERP 订单映射核对。                           |
| 创建或更新平台货品         | `api_goodsspec_push_Y` 创建平台货品                                | `vip_api_goods_query_Y` 平台货品查询                                         | 适合平台货品映射、同步库存前置准备。                            |
| 查询货品档案            | `goods_query_Y` 查询货品档案                                       | `goods_category_query_Y` 查询分类；`spec_barcode_push_Y` 条码                 | 适合商品基础资料导出、货品治理。                              |
| 查询退换货情况           | `refund_query_Y` 查询退换管理                                      | `vip_api_refund_query_Y` 查询原始退单；`stockin_order_query_refund_Y` 退货入库单查询 | 适合售后分析、退款退货跟踪。                                |
| 创建采购单或查询采购进度      | `purchase_order_push_Y` 创建采购单；`purchase_order_query_Y` 查询采购单 | `purchase_provider_query_Y` 查询供应商                                      | 适合采购计划、供应商对账。                                 |
| 创建调拨单并跟踪调拨        | `stock_transfer_create_Y` 创建调拨单                              | `stock_transfer_query_Y` 查询调拨单及明细                                      | 适合多仓调度自动化。                                    |

## 重点接口卡片

### `stock_query_Y`：查询可用库存

- PHP 文件：`stock_query.php`
- 场景：财务系统、SAP、数据分析等系统对接；按 ERP 库存记录最后修改时间增量获取。
- 关键请求字段：`start_time`、`end_time`、`spec_no`、`spec_no_list`、`warehouse_id`、`warehouse_no`、`defect`、`page_size`、`page_no`。
- 关键响应字段：`spec_id`、`warehouse_id`、`warehouse_no`、`goods_no`、`goods_name`、`spec_no`、`spec_name`、`barcode`、`stock_num`、`available_num`、`cost_price`、`avg_cost_price`、`defect`、`created`、`modified`。
- 限制：`start_time` 和 `end_time` 最大跨度 30 天；`spec_no_list` 上限 200 条；商家编码和时间范围查询时至少有一个不为空。

### `stock_full_query_Y`：全量查询库存

- 用途：全量获取系统库存管理数据。
- 适合：首次建表、周期性全量校验、与增量库存接口对账。

### `api_goods_stock_change_query_Y` + `api_goods_stock_change_ack_Y`：库存同步闭环

- 查询接口获取变化后的 ERP 可销库存，并同步至平台店铺。
- 回写接口将库存量同步至平台是否成功的状态批量回传给旺店通 ERP。
- 适合：外部平台库存同步，不适合只做内部库存报表。

## 选接口原则

- 先判断业务对象：订单、库存、货品、基础档案、售后、采购。
- 再判断动作：查询、创建、修改、回写、审核、取消。
- 查询类 skill 优先使用读接口，避免默认调用创建、修改、回写类接口。
- 涉及库存同步、物流同步、业务审核、取消、驳回的接口会改变 ERP 状态，创建 skill 前必须明确权限和操作确认机制。

## 相关页面

- [[domains/ecommerce-ops/api/wangdian/index|旺店通开放平台 API 知识库]]
- [[domains/ecommerce-ops/api/wangdian/skill-building-guide|旺店通 API Skill 创建指南]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
