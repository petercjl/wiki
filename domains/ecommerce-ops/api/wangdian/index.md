---
title: 旺店通开放平台 API 知识库
type: concept
created: 2026-06-03
updated: 2026-06-03
domain: ecommerce-ops
tags: [ecommerce, erp, wangdian, api]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
  - raw/api/wangdian-openapi/wangdian-openapi-full-archive-2026-06-03.md
status: active
---

# 旺店通开放平台 API 知识库

## 摘要

本页是旺店通 ERP 开放平台 API 的正式知识入口。raw 层已经保存 77 个接口的全量文档，包括请求地址、公共参数、业务请求参数、响应字段、请求示例和响应示例。正式使用时，先读本页确定接口，再回到 raw 归档核对字段细节。

## Raw 证据

- 机器可读全量抓取：`raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json`
- Obsidian 可搜索全量归档：`raw/api/wangdian-openapi/wangdian-openapi-full-archive-2026-06-03.md`
- 紧凑接口索引：`raw/api/wangdian-openapi/wangdian-openapi-compact-index-2026-06-03.json`

## 全局调用约定

| 项目 | 规则 |
|---|---|
| 测试环境 | `https://openapi.ali.huice.cc/openapi/<接口文件>.php` |
| 正式环境 | `https://openapi.huice.com/openapi/<接口文件>.php` |
| 公共参数 | `sid`、`appkey`、`timestamp`、`sign` |
| 时间戳 | 北京时间 1970-01-01 08:00:00 起至当前总秒数，允许最大时间误差 5 分钟 |
| 签名 | 使用 API 输入参数签名，具体算法需要读取官方签名说明或已有对接代码 |
| 分页 | 多数查询接口使用 `page_no` 和 `page_size`，`page_no` 常从 0 开始 |

## 分类统计

- 订单类: 17 个接口
- 库存类: 23 个接口
- 货品类: 10 个接口
- 基础类: 16 个接口
- 售后类: 6 个接口
- 采购类: 5 个接口

## 分类使用手册

下面 6 个页面保存每个接口的具体使用方法，包括请求地址、公共参数、业务请求参数、响应字段、请求示例和响应示例。写代码或创建 skill 时，先从能力地图定位接口，再进入对应分类手册查看字段。

- [[domains/ecommerce-ops/api/wangdian/reference/order-apis|旺店通订单类 API 使用手册]]：订单创建、查询、修改、物流同步、订单标签和小时达相关接口。
- [[domains/ecommerce-ops/api/wangdian/reference/stock-apis|旺店通库存类 API 使用手册]]：库存查询、全量库存、库存同步、出入库、盘点、调拨、分拣、运营仓等接口。
- [[domains/ecommerce-ops/api/wangdian/reference/goods-apis|旺店通货品类 API 使用手册]]：平台货品、系统货品、组合装、分类、条码和唯一码打印接口。
- [[domains/ecommerce-ops/api/wangdian/reference/base-apis|旺店通基础类 API 使用手册]]：供应商、标签、物流、员工、店铺、仓库和业务单据操作接口。
- [[domains/ecommerce-ops/api/wangdian/reference/aftersales-apis|旺店通售后类 API 使用手册]]：退货入库、原始退款单、退换管理、系统售后单和退货入库确认接口。
- [[domains/ecommerce-ops/api/wangdian/reference/purchase-apis|旺店通采购类 API 使用手册]]：采购单、采购退货单、采购申请单的查询和创建接口。

## 接口目录

### 订单类

| 服务名                                   | 接口名                 | 描述                                                                                                              | 客户端路径        |
| ------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------- | ------------ |
| trade_push_Y                          | 创建原始订单              | ①推送销售订单给ERP ；②更新已推送成功的销售订单。                                                                                     | 订单→订单管理→平台订单 |
| sales_trade_batch_change_Y            | 批量订单换货              | 获取批量订单换货                                                                                                        | 订单→订单管理→待审核  |
| sales_trade_simple_change_Y           | 单笔订单换货              | 获取单笔订单换货                                                                                                        | 订单→订单管理→待审核  |
| logistics_sync_query_Y                | 查询物流同步              | 旺店通ERP销售订单的发货状态、物流单号等同步给其他系统，注：”查询物流同步”与“物流同步回写”两个接口配合使用，完成“销售订单发货同步”，​仅支持自有/其它平台店铺                             |              |
| logistics_sync_ack_Y                  | 物流同步回写              | 将物流同步（发货状态、物流单号等）是否成功的结果批量回传给旺店通ERP。                                                                            |              |
| sales_trade_tags_modify_Y             | 修改订单标签              | 修改订单标签                                                                                                          |              |
| trade_query_Y                         | 系统订单（系统订单查询）        | 查询ERP内订单                                                                                                        |              |
| vip_api_trade_query_Y                 | 查询原始订单              | 查询原始订单                                                                                                          | 订单→订单管理→平台订单 |
| stockout_order_query_trade_Y          | 销售出库单               | 查询平台销售出库单                                                                                                       |              |
| sales_trade_modify_Y                  | 修改系统订单              | 修改旺店通erp内订单的订单标记                                                                                                |              |
| sales_trade_replenish_Y               | 创建补发订单              | 创建补发订单                                                                                                          |              |
| stockout_order_query_trade_cancel_Y   | 撤销发货的销售出库单查询        | 销售出库单是基于订单的，订单可以撤销发货。当前接口是用于查询历史的撤销的已发货订单数据。举例：订单JY20250001在2025-01-01 12:00:00第一次发货， 在2025-01-01 12:30:00撤销发货。 |              |
| sales_trade_batch_remark_flag_Y       | 批量修改系统订单的标旗和备注      | 批量修改系统订单的标旗和备注                                                                                                  |              |
| xsd_self_delivery_location_callback_Y | 小时达自配送三方运力回传状态和位置接口 | 小时达自配送三方运力回传状态和位置接口                                                                                             |              |
| api_trade_live_extend_query_Y         | 查询直播主播信息            | 获取租户系统内平台订单的直播信息扩展                                                                                              |              |
| logistics_multi_query_Y               | 查询多物流单号             | 获取旺店通ERP多物流单号                                                                                                   |              |
| xsd_upload_media_Y                    | 小时达订单图片回传           | 小时达订单图片回传                                                                                                       |              |

### 库存类

| 服务名 | 接口名 | 描述 | 客户端路径 |
|---|---|---|---|
| api_goods_stock_change_query_Y | 查询库存同步 | 获取变化后的旺店通ERP可销库存，并同步至平台店铺, | 仓储→库存同步 |
| stockout_order_query_Y | 查询出库单管理 | 获取旺店通ERP的各种业务类型的出库单就其明细信息 | 仓储→出库管理 |
| stockin_order_query_Y | 查询入库单管理 | 获取旺店通ERP的各种业务类型的入库单就其明细信息 | 仓储→入库管理 |
| api_goods_stock_change_ack_Y | 库存同步回写 | 库存量同步至平台是否成功的状态批量回传给旺店通ERP 注：仅支持自有/其他平台店铺 |  |
| stockin_order_push_Y | 创建入库单 | 调用本接口在旺店通ERP创建对应类型的入库单，增加库存。 | 仓储→入库管理 |
| stock_sync_by_pd_Y | 创建盘点单 | 旺店通ERP库存需要调整时，推送盘点库存单据给旺店通ERP，覆盖旺店通ERP实物库存。 注：旺店通ERP盘点成功后，盘点单内的库存值直接覆盖前库存 | 仓储→仓库盘点 |
| stock_query_Y | 查询可用库存 | 查询库存成本 可用库存数据 | 仓储→库存查询 |
| stockout_order_push_Y | 创建出库单 | 推送出库单给旺店通ERP，并执行出库操作（扣减库存等） | 仓储→出库管理 |
| pick_status_ack_Y | 分拣单状态回写接口 | 修改租户系统内分拣单的状态 | 仓储→分拣单管理 |
| pick_order_query_Y | 查询分拣单接口 | 获取旺店通ERP分拣单信息 | 仓储→分拣单管理 |
| pick_trade_query_Y | 查询分拣单订单 | 获取租户系统内分拣单的订单信息 | 仓储→分拣单管理 |
| stock_detail_report_query_Y | 查询出入库明细表 | 查询出入库明细表数据 |  |
| stock_inout_sn_query_Y | 查询出入库序列号 | 获取旺店通ERP各种业务类型的SN出入库明细 | 仓储→出库管理/入库管理 |
| stock_transfer_query_Y | 查询调拨单及明细 | 获取旺店通ERP调拨单及明细信息 | 仓储→调拨管理 |
| vip_wms_stockinout_order_push_Y | 创建委外出入库单 | 将要推送至WMS等第三方系统的委外出入库单创建到ERP | 仓储→委外出入库单管理 |
| stock_goods_sn_query_Y | 序列号管理查询接口 | 获取旺店通ERP各种业务类型的SN出入库明细 | 仓储→序列号管理 |
| stock_production_order_query_Y | 查询生产加工单接口 | 获取旺店通ERP生产加工单数据 | 仓储→生产加工 |
| stock_full_query_Y | 全量查询库存 | 全量获取系统库存管理数据 | 仓储→库存查询 |
| stock_transfer_create_Y | 创建调拨单 | ERP内仓与仓之间的库存需要调度时，推送调拨单给ERP | 仓储→调拨管理 |
| stock_outsource_order_query_Y | 查询委外出入库单 | 查询erp委外出库单、入库单数据 | 仓储-委外出入库单界面 |
| operational_order_create_Y | 运营仓单据创建 | 通过接口推送创建运营仓管理-运营仓单据到旺店通erp系统 | 仓储->运营仓管理->运营仓单据 |
| operational_order_query_Y | 运营仓单据查询 | 查询旺店通erp系统运营仓单据数据信息 | 仓储->运营仓管理->运营仓单据管理 |
| operational_stock_detail_query_Y | 运营仓库存明细查询 | 查询旺店通erp系统运营仓库存明细数据 | 仓储->运营仓管理->运营仓库存明细 |

### 货品类

| 服务名 | 接口名 | 描述 | 客户端路径 |
|---|---|---|---|
| vip_api_goods_query_Y | 平台货品查询 | 获取ERP的平台货品信息 | 商品→平台商品 |
| goods_query_Y | 查询货品档案 | 获取旺店通ERP的货品档案资料，“货品档案”其他系统称为“物料档案”“商品档案”等 | 商品→系统货品 |
| api_goodsspec_push_Y | 创建平台货品 | 在推送销售订单给旺店通ERP之前，需要映射匹配ERP系统单品或者设置同步库存的策略时调用 注：仅支持自有/其他平台店铺 | 商品→创建平台货品 |
| goods_push_Y | 创建货品档案 | 在ERP内创建货品档案 | 商品→系统货品 |
| suites_push_Y | 创建组合装 | 创建/更新组合装信息 | 商品→系统货品 |
| suites_query_Y | 查询组合装 | 获取旺店通ERP中组合装界面的组合装资料 | 商品→系统货品 |
| goods_category_query_Y | 查询货品分类 | 获取租户系统内全部货品分类的id、分类名词和分类的层级关系 | 商品→系统货品 |
| goods_category_flat_query_Y | 查询货品分类平级 | 获取租户系统内全部货品分类的id、分类名词和分类的层级关系 | 商品→系统货品 |
| unique_code_print_Y | 打印唯一码 |  | 档口→拿货标签管理 |
| spec_barcode_push_Y | 创建系统货品多条码 | 在ERP内创建、更新系统规格多条码 | 商品→货品条码 |

### 基础类

| 服务名 | 接口名 | 描述 | 客户端路径 |
|---|---|---|---|
| purchase_provider_query_Y | 查询供应商 | 批量获取旺店通ERP内供应商信息。 | 采购→供应商 |
| cfg_tags_query_Y | 查询标签 | 查询标签 |  |
| unique_code_query_Y | 查询唯一码 | 获取旺店通ERP内唯一码数据 | 档口→拿货标签管理 |
| logistics_Y | 物流公司 | 批量获取旺店通ERP内物流档案信息 | 配置→快递管理 |
| employee_query_Y | 员工查询 | 获取ERP的员工页面信息 | 配置→权限设置 |
| vip_stockout_sales_weight_push_Y | 称重 | 将重量回传写入旺店通ERP销售订单 | 仓储→包裹称重 |
| shop_Y | 查询店铺 | 批量获取旺店通ERP内店铺档案信息 | 配置→绑定店铺 |
| warehouse_query_Y | 查询仓库 | 批量获取旺店通ERP内仓库档案信息 | 配置→仓库信息维护 |
| sys_logisitcs_code_Y | 物流公司枚举 |  |  |
| unique_code_status_change_Y | 修改唯一码状态为已到货 | 将旺店通唯一码状态变更为已到货 | 档口→拿货标签管理 |
| purchase_provider_create_Y | 创建供应商 | 给旺店通推送供应商信息 | 采购→供应商 |
| order_audit_Y | 业务单据审核接口 | 第三方系统触发erp中待审核（待确认）的业务单据审核 | 订单→订单管理→待审核 |
| order_cancel_Y | 业务单据取消 | 第三方系统触发erp中业务单据取消。 |  |
| order_stop_waiting_Y | 业务单停止等待 | 第三方系统对接处理业务单据进行停止等待 |  |
| order_reject_Y | 业务单据驳回审核接口 | 第三方系统触发erp中业务单据驳回审核 |  |
| warehouse_create_Y |  |  |  |

### 售后类

| 服务名 | 接口名 | 描述 | 客户端路径 |
|---|---|---|---|
| stockin_order_query_refund_Y | 退货入库单查询 | 获取旺店通ERP销售退货（换货）订单对应的入库单信息 | 仓储→入库管理 |
| sales_refund_push_Y | 创建原始退款单 | 销售订单（包括发货前和发货后）退款或退货单据推送至ERP。注：销售订单的售后换货订单此接口推送“退货类型”退款单，换出订单“trade_push.php”推送 | 售后→售后管理→平台售后单 |
| refund_query_Y | 查询退换管理 | 获取ERP销售退货（换货）订单信息 | 售后→售后管理→售后单 |
| aftersales_refund_create_Y | 创建系统售后单 | 创建系统售后单，---目前不支持换货 ，只支退货单，退货单类型只能是退款退货和退款不退货 基于系统单创建退款单 | 售后→售后管理→售后单 |
| vip_api_refund_query_Y | 查询原始退单 |  | 售后→售后管理→平台售后单 |
| aftersale_stockin_confirm_Y | 创建退货入库单 | 推送旺店通ERP销售退货（换货）订单对应的入库单据给旺店通ERP，推送前提旺店通ERP的退换单状态为“待收货” | 仓储--入库管理--退货入库单--新建 |

### 采购类

| 服务名 | 接口名 | 描述 | 客户端路径 |
|---|---|---|---|
| purchase_order_query_Y | 查询采购单 | 获取旺店通ERP各种业务类型的采购单信息 | 采购→采购单 |
| purchase_return_query_Y | 查询采购退货单 | 获取旺店通ERP各种业务类型的采购单信息 | 采购→采购退货单 |
| purchase_order_push_Y | 创建采购单 | 新增创建采购单接口 | 采购→采购单 |
| purchase_return_order_push_Y | 创建采购退货单 | 新增创建采购退货单接口 | 采购→采购退货单 |
| purchase_apply_query_Y | 查询采购申请单 | 获取旺店通ERP的采购申请单及其明细信息 | 采购→采购申请单 |

## 相关页面

- [[domains/ecommerce-ops/api/wangdian/capability-map|旺店通 API 能力地图]]
- [[domains/ecommerce-ops/api/wangdian/skill-building-guide|旺店通 API Skill 创建指南]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
