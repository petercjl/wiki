---
title: 旺店通 库存类 API 使用手册
type: concept
created: 2026-06-03
updated: 2026-06-03
domain: 电商运营
tags: [ecommerce, erp, wangdian, api]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
status: active
---

# 旺店通 库存类 API 使用手册

## 用途

本页整理旺店通开放平台 库存类 的具体接口使用方法，面向后续写代码或创建 Codex/Hermes skill。每个接口包含服务名、PHP 文件、请求地址、业务请求参数、业务响应字段、示例和注意事项。

## 本类接口

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

## 接口详情

### api_goods_stock_change_query_Y：查询库存同步

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `api_goods_stock_change_query_Y` |
| PHP 文件 | `api_goods_stock_change_query.php` |
| 文档标题 | 查询库存同步 |
| 描述 | 获取变化后的旺店通ERP可销库存，并同步至平台店铺, |
| 客户端路径 | 仓储→库存同步 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=api_goods_stock_change_query_Y |

#### 请求地址

| 1.1 接口描述：获取变化后的旺店通ERP可销库存，并同步至平台店铺,注：”查询同步库存”与“库存同步回写”两个接口配合使用，完成“库存同步”，仅支持自有/其他平台店铺 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 调用建议：建议间隔时间3~5分钟查询一次，集中获取待同步数据，注意上一次回写完成以后，再从数据池获取待同步的数据。 |
| 1.4 注意事项：“查询同步库存与“库存同步回写””配合使用，要在平台的库存同步成功后再回写同步成功状态给OMS，如果平台没有成功却回传成功，会导致后续无法再次获取到库存信息。 |
| 1.5 旺店通ERP配置：（接口调试前需要提前配置好）①店铺授权，如果店铺授权状态是非授权，设置→基本设置→店铺界面，点击授权按钮（测试环境默认授权）②创建平台货品和货品档案，并且保证平台货品和货品档案已经匹配。③需设置库存同步策略，路径：【仓储】—>【库存管理】—>【库存同步】。点击右侧的“查看同步策略”设置库存同步策略，并且在“店铺同步管理”里面添加对应的店铺。注：需要在设置库存同步策略后商品有库存变化，接口才能查到数据。 |

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/api_goods_stock_change_query.php |
| 正式环境 | https://openapi.huice.com/openapi/api_goods_stock_change_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/api_goods_stock_change_query.php';<br><br>    $c->putApiParam('shop_id','585');<br>    $c->putApiParam('limit',1);<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺id | shop_id | varchar | 20 | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar | 40 |  | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 获取数据条数 | limit | int | 11 | 是 | 取值范围：limit大于等于100，小于等于2000，获取的数据通过“库存同步回写”接口响应同步结果后，才可再次获取数据。注：库存数据获取同步给商城系统后，一定要通过api_goods_stock_change_ack.php回写结果，否则会出现待同步库存数量不能同步到商城的情况。 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 库存信息列表 | stock_change_list | data[ ] |  | 是 | 响应参数的1级数据节点，包含需要同步库存信息的数据节点，节点下数据字段详见下述“stock_change_list” |
| 获得当前同步记录的条数 | current_count | int |  | 是 | 记录当前获得的记录条数 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| Erp内平台货品表主键id | rec_id | string | 11 | 是 | Erp内平台货品表主键id，用于状态回传接口使用 |
| 店铺id | shop_id | string | 6 | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar | 40 | 是 | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 货品ID | goods_id | varchar | 40 | 是 | 外部系统货品主键，外部系统推送订单时使用的，erp只是保存了下外部系统的值 |
| 规格ID | spec_id | varchar | 40 | 是 | 外部系统货品规格id |
| Erp内库存 | sync_stock | int | 11 | 是 | 该库存是通过配置计算出来的，使用该接口注意配置库存同步策略。 |
| 库存变化时自增 | stock_change_count | int | 11 | 是 | 库存变化时自增用于状态回传接口使用，状态回传时把该值一并回传即可，不用深究其含义 |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "stock_change_list": [
        {
            "rec_id": "2754327482516635662",
            "shop_id": "585",
            "goods_id": "E1222666614528A",
            "spec_id": "34442266254221",
            "sync_stock": 6,
            "stock_change_count": 4
        }
    ],
    "current_count": 1
}
```

### JSON

```text
{
    "code": 2310,
    "message": "店铺编号在系统中不存在或已停用，请检查shop_id是否正确"
}
```


### stockout_order_query_Y：查询出库单管理

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stockout_order_query_Y` |
| PHP 文件 | `stockout_order_query.php` |
| 文档标题 | 查询出库单管理 |
| 描述 | 获取旺店通ERP的各种业务类型的出库单就其明细信息 |
| 客户端路径 | 仓储→出库管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stockout_order_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP的各种业务类型的出库单就其明细信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取：如果状态（status）未传值或者值大于等于95时按照出库时间增量获取数据，如果状态（status）小于95时按照最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |
| 1.3注意事项：⑴获取的各业务类型的出库单信息，不包含上层单据内容。（举例：调拨出库单的上层单据是调拨单，本接口能获取调拨出库单信息，不能查调拨单信息）⑵本接口销售出库单类型单据不进行返回，获取销售出库单类型的数据需调用查询销售出库单接口。 |


#### 调用场景

| 2.1 举例说明：SAP、线下ERP、SRM、SCM等系统对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stockout_order_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stockout_order_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单主键id | id | int | 11 | 是 | 出库单主键id |
| 出库单号 | stockout_no | varchar | 40 | 是 | 出库单号 |
| 源单号 | src_order_no | varchar | 40 | 是 | 源单号，上层单据的业务单号 |
| 仓库id | warehouse_id | varchar | 40 | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 状态 | consign_status | int | 4 | 是 | 出库单状态20, 待审核25,  已审核30, 已出库40,  已取消 |
| 出库时间 | consign_time | date |  | 是 | 出库时间，格式：yyyy-MM-dd HH:mm:ss |
| 出库单类型 | src_order_type | int | 4 | 是 | 出库单类型：  [2]: '调拨出库',  [3]: '采购退货出库',  [4]: '盘亏出库',  [5]: '生产出库',  [7]: '其他出库',  [9]: '委外出库',  [15]: '纠错出库' |
| 出库单类型名称 | src_order_type_name | varchar | 40 | 是 | 出库单类型名称 |
| 出库单子类型 | src_order_sub_type | varchar | 256 | 是 | 出库单子类型 |
| 出库原因 | stockout_reason | varchar | 32 | 是 | 出库原因 |
| 数量 | goods_count | decimal | (19,4) | 是 | 货品数量 |
| 货品总销售金额 | goods_total_amount | decimal | (19,4) | 是 | 货品总销售金额 |
| 物流单号 | logistics_no | varchar | 40 | 是 | 物流单号（该出库单的运单号） |
| 收件人 | receiver_name | varchar | 40 | 是 | 该字段已废弃 |
| 国家 | receiver_country | smallint | 6 | 是 | 国家 |
| 省份 | receiver_province | varchar | 40 | 是 | 省份 |
| 城市 | receiver_city | varchar | 40 | 是 | 城市 |
| 地区 | receiver_district | varchar | 60 | 是 | 地区 |
| 详细地址 | receiver_address | varchar | 256 | 是 | 该字段已废弃 |
| 收件人移动电话 | receiver_mobile | varchar | 40 | 是 | 该字段已废弃 |
| 收件人固定电话 | receiver_telno | varchar | 40 | 是 | 该字段已废弃 |
| 邮编 | receiver_zip | varchar | 20 | 是 | 邮编 |
| 重量 | weight | decimal | (19,4) | 是 | 重量 |
| 备注 | remark | varchar | 255 | 是 | 备注 |
| 外部单号 | outer_no | varchar | 40 | 是 | 外部单号 |
| 操作员姓名 | create_by | varchar | 40 | 是 | 操作员姓名 |
| 物流方式 | logistics_type | smallint | 6 | 是 | 响应值为代表物流方式的数字，数字对应的物流方式名称单击这里 |
| 物流编号 | logistics_code | varchar | 20 | 是 | 代表物流所有属性的唯一编码，用于物流区分，ERP内支持自定义（ERP物流界面设置） |
| 物流公司名称 | logistics_name | varchar | 40 | 是 | erp对应的物流公司名称 |
| 最后修改时间 | modify_date | datetime |  | 是 | 单据最后修改时间，格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | create_date | datetime |  | 是 | 单据创建时间，格式：yyyy-MM-dd HH:mm:ss |
| Sku详情节点 | order_detail_list | data[] |  | 是 | 响应参数的2级数据节点，包含当出库单货品属性信息的数据节点,节点下数据字段详见下述" details_list" |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stockout_order_query.php';<br><br>    $c->putApiParam('start_time', '2026-01-24 15:01:27');<br>    $c->putApiParam('end_time', '2026-01-28 15:10:27');<br>    $c->putApiParam('page_no', 0);<br>    $c->putApiParam('page_size', 1);<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 3,<br>    "stockout_list": [<br>        {<br>            "order_detail_list": [<br>                {<br>                    "prop1": null,<br>                    "prop2": null,<br>                    "prop3": null,<br>                    "prop4": null,<br>                    "prop5": null,<br>                    "prop6": null,<br>                    "prop7": null,<br>                    "prop8": null,<br>                    "prop9": null,<br>                    "prop10": null,<br>                    "sku_id": "2786271737598181394",<br>                    "warehouse_id": null,<br>                    "sku_sort_name": null,<br>                    "sku_no": "125001",<br>                    "sku_name": "\u9177\u5f00-TV-50C60",<br>                    "sku_short_name": "",<br>                    "barcode": "260119303",<br>                    "spu_id": "2786271737501712402",<br>                    "spu_name": "\u9177\u5f00-TV-50C60",<br>                    "spu_short_name": "\u9177\u5f00-TV-50C60",<br>                    "spu_no": "125001",<br>                    "spu_modify_date": "2026-01-21T15:18:06",<br>                    "plat_spu_no": "",<br>                    "plat_sku_no": "",<br>                    "image_url": "",<br>                    "spu_img_url": "",<br>                    "outer_sku_no": "",<br>                    "ref_cost_price": "0",<br>                    "price": "0",<br>                    "retail_price": "0",<br>                    "wholesale_price": "0",<br>                    "validity_days": null,<br>                    "unit_id": "0",<br>                    "unit_name": null,<br>                    "weight": "0",<br>                    "box_sku_num": 0,<br>                    "sku_remark": null,<br>                    "sku_delete_flag": false,<br>                    "brand_id": "2786271559587726354",<br>                    "brand_name": "\u5176\u4ed6",<br>                    "goods_category_id": "0",<br>                    "approval_number": "",<br>                    "stock_num": null,<br>                    "quality_num": null,<br>                    "defect_num": null,<br>                    "default_position_name": null,<br>                    "location_name": null,<br>                    "location_id": null,<br>                    "stock_type": 1,<br>                    "stock_type_text": null,<br>                    "batch_id": "0",<br>                    "batch_no": "",<br>                    "production_date": null,<br>                    "expire_date": null,<br>                    "sku_position_vo_list": null,<br>                    "id": "2789505483059232787",<br>                    "stockout_id": "2789505483055038483",<br>                    "src_order_detail_id": "2789504267856117779",<br>                    "base_unit_id": "0",<br>                    "base_unit_name": null,<br>                    "unit_ratio": "0",<br>                    "num": "30",<br>                    "plan_num": "30",<br>                    "actual_num": null,<br>                    "auxiliary_num": "0",<br>                    "stockout_amount": "0",<br>                    "stockout_price": "0",<br>                    "total_amount": "0",<br>                    "cost_price": "0",<br>                    "sku_code": "",<br>                    "img_url": "",<br>                    "owner_id": "",<br>                    "remark": "",<br>                    "sn_num": null,<br>                    "goods_labels": null<br>                }<br>            ],<br>            "detail_list": null,<br>            "id": "2789505483055038483",<br>            "stockout_no": "CKQ2601280002",<br>            "outer_no": "",<br>            "src_order_type": 3,<br>            "src_order_no": "CT2601280101",<br>            "src_order_id": "2789504267487019027",<br>            "src_order_type_name": "\u91c7\u8d2d\u9000\u8d27\u51fa\u5e93",<br>            "src_order_sub_type": "0",<br>            "src_order_sub_type_name": null,<br>            "warehouse_type": 0,<br>            "warehouse_id": "4",<br>            "warehouse_name": null,<br>            "stockout_reason": "0",<br>            "stockout_reason_name": null,<br>            "consign_status": 30,<br>            "consign_status_name": "\u5df2\u51fa\u5e93",<br>            "logistics_id": "0",<br>            "logistics_name": "",<br>            "logistics_code": "",<br>            "logistics_type": "",<br>            "logistics_no": "",<br>            "post_amount": null,<br>            "goods_count": "30",<br>            "quality_goods_count": "30",<br>            "actual_goods_count": null,<br>            "goods_type_count": 1,<br>            "goods_total_amount": null,<br>            "total_stockout_amount": "0",<br>            "receiver_name": "",<br>            "receiver_country": null,<br>            "receiver_province": 0,<br>            "receiver_city": 0,<br>            "receiver_district": 0,<br>            "receiver_address": "",<br>            "receiver_mobile": "",<br>            "receiver_telno": null,<br>            "receiver_zip": null,<br>            "receiver_area": null,<br>            "remark": "",<br>            "create_by": "4307",<br>            "creator_name": null,<br>            "create_date": "2026-01-28T13:38:54",<br>            "modify_date": "2026-01-28T13:38:54",<br>            "consign_time": "2026-01-28T13:38:54"<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量获取数据,start_time作为开始时间,格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量获取数据,end_time作为结束时间,格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int | 10 | 否 | 每页返回条数，输入值范围1~100，不传默认40，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 出库单类型 | order_type | tinyint | 1 | 否 | 2调拨出库,3采购退货出库,4盘亏出库,5生产出库,7其他出库,8多发出库,9纠错出库,10保修配件出库,11初始化出库，12jit拣货出库，13委外出库 |
| 出库单状态 | status | tinyint | 1 | 否 | 出库单状态20,待审核25, 已审核30, 已出库40,已取消 |
| 仓库编号 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 源单号 | src_order_no | varchar | 40 | 否 | 源单号，传该字段可以不传时间 |
| 出库单号 | stockout_no | varchar | 40 | 否 | 出库单号，传该字段可以不传时间 |
| 外部API单号 | outer_no | varcher | 40 | 否 | 外部系统出库单的唯一单据编号，传该字段可以不传开始时间和结束时间（创建出库单时所传outer_no字段） |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 出库单详情 | stockout_list | data[] |  | 否 | 响应参数的1级数据节点，包含当前页的出库单及其明细的数据节点,节点下数据字段详见下述“stockout_list”和" details_list" |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库单主键id | stockout_id | int | 11 | 是 | 出库单主键id |
| 出库单明细id | id | int | 11 | 是 | 出库单明细id |
| 上层单据明细主键 | src_order_detail_id | int | 11 | 是 | 上层单据明细主键 |
| 商家编码 | sku_no | varchar | 40 | 是 | 代表所单品（sku）所有属性的唯一编码，用于获取系统单品的数据，SKU概念介绍，单击这里 |
| 货品数量 | num | decimal | (19,4) | 是 | 货品数量 |
| 销售价 | stockout_price | decimal | (19,4) | 是 | 销售价 |
| 货品名称 | spu_name | varchar | 255 | 是 | 货品名称 |
| 货品编号 | spu_no | varchar | 40 | 是 | 代表SPU所有属性的唯一编号，用于获取系统货品的数据，SPU概念介绍，单击这里 |
| 规格名称 | sku_name | varchar | 100 | 是 | 规格名称 |
| 成本价 | cost_price | decimal | (19,4) | 是 | 成本价 |
| 总销售金额 | stockout_amount | decimal | (19,4) | 是 | 总销售金额 |
| 重量 | weight | decimal | (19,4) | 是 | 重量 |
| 备注 | remark | varchar | 64 | 是 | 备注 |
| 批次号 | batch_no | varchar | 20 | 是 | 批次号 |
| 有效期 | expire_date | datetime |  | 是 | 有效期，格式：yyyy-MM-dd HH:mm:ss |
| 生产日期 | production_date | datetime |  | 是 | 生产日期，格式：yyyy-MM-dd HH:mm:ss |
| 商品类型 | stock_type | tinyint | 4 | 是 | 1: 正品 \| 2: 次品 |
| 供应商id | provider_id | int | 11 | 否 | 供应商id      仅当order_type=3时，返回该字段 |
| 供应商编码 | provider_no | varchar | 64 | 否 | 供应商编码    仅当order_type=3时，返回该字段 |
| 供应商名称 | provider_name | varchar | 64 | 否 | 供应商名称    仅当order_type=3时，返回该字段 |
| SPU图片地址 | spu_img_url | varchar |  |  |  |
| sku参考成本价 | ref_cost_price | decimal | (19,4) |  |  |
| sku占用货位明细 | sku_position_vo_list | data[] |  |  |  |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| id | id | long |  |  |  |
| 库存Id | stock_id | long |  |  | 库存Id |
| 货位id | location_id | long |  |  | 货位id |
| 货位名称 | location_name | varchar |  |  | 货位名称 |
| 占用数量 | num | decimal |  |  | 占用数量 |


#### 响应示例

### JSON

```text
{
    "code": 11000000,
    "message": "时间查询范围不能超过30天，请缩小搜索范围！"
}
```


### stockin_order_query_Y：查询入库单管理

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stockin_order_query_Y` |
| PHP 文件 | `stockin_order_query.php` |
| 文档标题 | 查询入库单管理 |
| 描述 | 获取旺店通ERP的各种业务类型的入库单就其明细信息 |
| 客户端路径 | 仓储→入库管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stockin_order_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP的各种业务类型的入库单就其明细信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3注意事项：①获取的各业务类型的入库单信息，不包含上层单据内容。                     （举例：采购入库单的上层单据是采购单，本接口能查采购入库单，不能查采购单信息）                       ②本接口退货入库类型单据不进行返回，获取退货入库类型的数据需调用查询退货入库单接口 |


#### 调用场景

| 2.1 举例说明：自有商城接入ERP、金蝶接入、用友接入、SAP接入等 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stockin_order_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stockin_order_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stockin_order_query.php';<br><br>	$c->putApiParam('start_time', '2026-03-22 16:00:40');<br>	$c->putApiParam('end_time', '2026-03-31 16:00:40');<br>	$c->putApiParam('order_type', 1);<br>	$c->putApiParam('page_no', 0);<br>	$c->putApiParam('page_size', 1);<br><br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 是 | 制单开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 制单结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int | 10 | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为40，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 单据类别 | order_type | int | 4 | 否 | 单据类别 1采购入库  2调拨入库  4盘盈入库  5生产入库 6其他入库  9委外入库  11直发入库  15纠错入库  16预入库 |
| 入库单状态 | status | int | 4 | 否 | 入库单状态(10, "待审核"),(85, "已入库"),(101, "已取消"), |
| 仓库编号 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置），用于获取指定仓库单据信息(不支持一次推送多个仓库编号) |
| 上层单据编号 | src_order_no | varchar | 40 | 否 | 上层单据编号，传该字段可以不传开始时间和结束时间 |
| 入库单号 | stockin_no | varchar | 40 | 否 | 入库单号，传该字段可以不传开始时间和结束时间 |
| 外部API单号 | outer_no | varchar | 40 | 否 | 外部系统入库单的唯一单据编号，传该字段可以不传开始时间和结束时间（创建入库单时所传outer_no字段） |
| 最后修改时间 | modify_time_start | datetime |  | 是 | 最后修改开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 最后修改时间 | modify_time_end | datetime |  | 是 | 最后修改结束时间，格式：yyyy-MM-dd HH:mm:ss |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 入库单列表节点 | stockin_list | data |  | 否 | 响应参数的1级数据节点，包含当前页的入库单属性信息的数据节点，节点下数据字段详见下述“stockin_list”列表 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 15,<br>    "stockin_list": [<br>        {<br>            "stock_in_order_detail_list": [<br>                {<br>                    "prop7": "",<br>                    "prop8": "",<br>                    "prop9": "",<br>                    "prop10": "",<br>                    "sku_id": "2774335886379188249",<br>                    "warehouse_id": 0,<br>                    "sku_sort_name": "",<br>                    "sku_no": "6920585703278",<br>                    "sku_name": "XXX",<br>                    "sku_short_name": "",<br>                    "barcode": "6920585703278",<br>                    "spu_id": "2774335886035255321",<br>                    "spu_name": "XXX",<br>                    "spu_short_name": "",<br>                    "spu_no": "1017050003",<br>                    "spu_modify_date": "2025-12-17 17:00:19",<br>                    "plat_spu_no": "",<br>                    "plat_sku_no": "",<br>                    "image_url": "",<br>                    "spu_img_url": "",<br>                    "outer_sku_no": "",<br>                    "ref_cost_price": "0",<br>                    "price": "0",<br>                    "retail_price": "0",<br>                    "wholesale_price": "0",<br>                    "validity_days": 0,<br>                    "unit_id": "0",<br>                    "unit_name": "",<br>                    "weight": "0",<br>                    "box_sku_num": 0,<br>                    "sku_remark": "",<br>                    "sku_delete_flag": false,<br>                    "brand_id": "0",<br>                    "brand_name": "",<br>                    "goods_category_id": "0",<br>                    "approval_number": "",<br>                    "prop1": "",<br>                    "prop2": "",<br>                    "prop3": "",<br>                    "prop4": "",<br>                    "prop5": "",<br>                    "prop6": "",<br>                    "stock_num": 0,<br>                    "quality_num": "2500",<br>                    "defect_num": "0",<br>                    "default_position_name": "",<br>                    "location_name": "",<br>                    "location_id": 0,<br>                    "stock_type": 1,<br>                    "stock_type_text": "正品",<br>                    "batch_id": 0,<br>                    "batch_no": "wzz0331001",<br>                    "production_date": "2026-01-07 00:00:00",<br>                    "expire_date": "2028-01-07 00:00:00",<br>                    "id": "2811999816073084949",<br>                    "stockin_id": "2811999816068890645",<br>                    "src_order_type": 0,<br>                    "src_order_id": 0,<br>                    "src_order_no": "",<br>                    "src_order_detail_id": "2811999564943327253",<br>                    "operate_type": 0,<br>                    "provider_id": "2001217658216296450",<br>                    "provider_name": "0100001-XXX公司",<br>                    "provider_no": "0100001",<br>                    "warehouse_no": "",<br>                    "spu_type": "",<br>                    "stockin_position_id": 0,<br>                    "zone_id": 0,<br>                    "zone_name": "",<br>                    "real_num": "2500",<br>                    "num": "2500",<br>                    "purchase_price": "0",<br>                    "stockin_price": "25",<br>                    "tariff": "0",<br>                    "is_vat": 0,<br>                    "remark": "",<br>                    "share_post_amount": "0",<br>                    "stockin_amount": "62500",<br>                    "sn_num": 0,<br>                    "goods_labels": null,<br>                    "sn_list": null,<br>                    "print_flag": 0,<br>                    "create_date": "",<br>                    "batch_prop7": 0<br>                }<br>            ],<br>            "id": "2811999816068890645",<br>            "stockin_no": "RK2603310004",<br>            "src_order_type": 1,<br>            "src_order_sub_type": "0",<br>            "src_order_sub_type_name": "",<br>            "src_order_id": "2811999563940888597",<br>            "src_order_no": "CG2603310501",<br>            "src_order_type_name": "采购入库",<br>            "outer_no": "",<br>            "status": 85,<br>            "status_name": "已入库",<br>            "sku_count": "2500",<br>            "quality_sku_count": "2500",<br>            "sku_type_count": 1,<br>            "goods_amount_tax": "0",<br>            "goods_amount": "62500",<br>            "warehouse_id": "227",<br>            "warehouse_name": "100501002-XXX仓库",<br>            "remark": "",<br>            "stockin_date": "2026-03-31 15:23:21",<br>            "stockin_reason": "0",<br>            "stockin_reason_name": "",<br>            "create_by": "4252",<br>            "create_date": "2026-03-31 15:23:21",<br>            "modify_by": "4252",<br>            "modify_date": "2026-03-31 15:23:28",<br>            "provider_name": "0100001-XXX公司",<br>            "prepare_status": 30,<br>            "logistics_no": "",<br>            "logistics_id": 0,<br>            "quality_num": 0,<br>            "defect_num": 0,<br>            "refund_no": "",<br>            "refund_type": 0,<br>            "refund_reason": 0,<br>            "refund_logistics_name": "",<br>            "refund_logistics_no": "",<br>            "post_amount": "0",<br>            "post_share_type": 0<br>        }<br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 1020,<br>    "message": "系统异常，请稍后再试！",<br>    "total_count": null,<br>    "stockin_list": null<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单主键id | id | int | 11 | 是 | 入库单主键id |
| 入库单号 | stockin_no | varchar | 40 | 是 | 系统入库单号，默认为RK开头 |
| 仓库ID | warehouse_id | smallint | 6 | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 入库类型 | src_order_type | tinyint | 4 | 是 | 1采购入库  2调拨入库  4盘盈入库  5生产入库 6其他入库  9委外入库  11直发入库  15纠错入库  16预入库 |
| 入库id | src_order_id | int | 11 | 是 | 入库id |
| 其他入库原因 | stockin_reason | int | 11 | 是 | 其他入库原因 |
| 物流公司 | logistics_id | int | 11 | 是 | 物流公司 |
| 邮费分摊类型 | post_share_type | int | 11 | 是 | 邮费分摊类型0,不分摊 1,按数量分摊2,按照金额分摊 |
| 经办人ID | create_by | int | 11 | 是 | 经办人id |
| 最后修改时间 | modify_date | datetime |  |  | 最后修改时间 |
| 仓库名称 | warehouse_name | varchar | 40 | 是 | ERP内系统仓库名称 |
| 状态 | status | tinyint | 4 | 是 | 入库单状态(10, "待审核"),(85, "已入库"),(101, "已取消"), |
| 入库时间 | stockin_date | datetime | datetime | 是 | 入库时间，格式：YYYY-MM-DD HH:MM:SS   同modified含义相同，如需入库时间可取check_time字段值 |
| 创建时间 | create_date | datetime | datetime | 是 | 创建时间，格式：yyyy-MM-dd HH:mm:ss |
| 备注 | remark | varchar | 255 | 是 | 备注 |
| 货品数量 | sku_count | decimal | (19,4) | 是 | 货品数量 |
| 货款总额 | goods_amount | decimal | (19,4) | 是 | 货款总额 |
| 邮费 | post_amount | decimal | (19,4) | 是 | 邮费 |
| 源单号 | src_order_no | varchar | 40 | 是 | 上层单据编号，如果是采购入库就是采购单号，调拨入库就是调拨号，以此类推 |
| 外部单号 | outer_no | varchar | 40 | 是 | 外部单号 |
| 物流单号 | logistics_no | varchar | 40 | 否 | 物流单号, |
| 货品列表节点 | stock_in_order_detail_list | data[ ] |  | 是 | 响应参数的2级数据节点，包含单个入库单所有货品属性信息的数据节点，节点下数据字段详见下述“stockin_list”列表 |
| 最后修改人 | modify_by | String |  |  | 修改人 |
| 入库原因名称 | stockin_reason_name | String |  |  | stockin_reason对应的名称 |
| 入库正品总数量 | quality_sku_count | decimal |  |  | 入库正品总数量 |
| 状态名称 | status_name | varchar |  |  | status名称 |
| 入库类型名称 | src_order_type_name | varchar |  |  | src_order_type对应的名称 |
| 供应商名称 | provider_name | varchar |  |  | 供应商名称 |
| 采购单状态 | prepare_status | int |  |  | 5, "待审核"7, "待财审"10, "已审核"11, "待推送"12, "推送失败"13, "已推送"20, "部分入库"30, "已入库"99, "已取消" |
| 正品数量 | quality_num | BigDeciml |  |  | 正品数量 |
| 次品数量 | defect_num | BigDeciml |  |  | 次品数量 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库单主键id | stockin_id | int | 11 | 是 | 入库单主键id |
| 主键 | id | int | 11 | 是 | 主键（与业务无关） |
| 上层单据明细主键 | src_order_detail_id | int | 11 | 是 | 上层单据明细主键 |
| 入库类型 | src_order_type | tinyint | 4 | 是 | 1采购入库, 2调拨入库, 4盘盈入库, 5生产入库, 6其他入库, 7保修入库, 8纠错入库, 9初始化入库，10 预入库 11 JIT退货入库 12 委外入库 |
| 来源单id | src_order_id | int | 11 | 是 | 来源单id |
| 来源单号 | src_order_no | varchar | 40 | 是 | 上层单据编号，如果是采购入库就是采购单号，调拨入库就是调拨号，以此类推 |
| 条形码 | barcode | varchar |  |  | 条形码 |
| 规格ID | sku_id | int | 11 | 是 | 规格ID |
| 货位ID | location_id |  |  |  | 该字段值和stockin_position_id值一致 |
| 货位ID | stockin_position_id | int | 11 | 是 | 货位ID，入库时默认ID，后来做货位调拨不再修改 |
| 货区ID | zone_id | Long |  |  | 货区ID |
| 货区名称 | zone_name | varchar |  |  | 货区名称 |
| 实际入库数量 | real_num | decimal | (19,4) | 是 | 入库数量 |
| 辅助单位 | unit_id | smallint | 6 | 是 | 辅助单位 |
| 预期入库数量 | num | decimal | (19,4) | 是 | 预期入库数量（基本单位数量，显示可自动转换成辅助单位） |
| 分摊邮费 | share_post_amount | decimal | (19,4) |  | 分摊邮费 |
| 创建时间 | create_date | datetime |  | 是 | 创建时间 |
| 商家编码 | sku_no | varchar | 40 | 是 | 代表单品(sku)所有属性的编码，SKU概念介绍,单击这里 |
| 参考成本价 | ref_cost_price | decimal | (19,4) | 是 | 参考成本价 |
| 生产日期 | production_date | datetime |  | 是 | 生产日期，格式：yyyy-MM-dd HH:mm:ss |
| 有效期天数 | validity_days | int | 11 | 是 | 有效期天数 |
| 有效期 | expire_date | datetime |  | 是 | 有效期，格式：yyyy-MM-dd HH:mm:ss |
| 入库单价 | stockin_price | decimal | (19,4) | 是 | 入库单价 |
| 入库金额 | stockin_amount | decimal | (19,4) | 是 | 入库金额 |
| 备注 | remark | varchar | 255 | 是 | 入库单明细备注 |
| 货品名称 | spu_name | varchar | 255 | 是 | 货品名称 |
| 货品简称 | spu_short_name | varchar |  |  | 货品简称 |
| 货品编号 | spu_no | varchar | 40 | 是 | 代表货品(spu)所有属性的编号，SPU概念介绍,单击这里 |
| 货品id | spu_id | int | 11 |  | 货品id |
| 规格简称 | sku_short_name | varchar |  |  | 规格简称 |
| 规格名称 | sku_name | varchar | 100 | 是 | 规格名称 |
| 批次号 | batch_no | varchar | 20 | 是 | 批次号 |
| 货位编号 | location_name | varchar | 40 | 是 | 货位编号 |
| 供应商名称 | provider_name | varchar |  | 否 | 供应商名称，默认不返回该字段，当order_type传为1返回 |
| 供应商编码 | provider_no | varchar |  | 否 | 供应商编码，默认不返回该字段，当order_type传为1返回 |
| 供应商主键ID | provider_id | varchar |  | 否 | 供应商主键ID，默认不返回该字段，当order_type传为1返回 |
| 自定义属性1 | prop1 | varchar |  | 是 | 自定义属性1 |
| 自定义属性2 | prop2 | varchar |  | 是 | 自定义属性2 |
| 自定义属性3 | prop3 | varchar |  | 是 | 自定义属性3 |
| 自定义属性4 | prop4 | varchar |  | 是 | 自定义属性4 |
| 自定义属性5 | prop5 | varchar |  | 是 | 自定义属性5 |
| 自定义属性6 | prop6 | varchar |  | 是 | 自定义属性6 |
| 库存属性 | stock_type | int |  |  | 库存属性 |
| 库存属性名称 | stock_type_text | varchar |  |  | 库存属性名称 |
| 箱规 | box_sku_num | decimal | (19,4) |  | 箱规 |
| 重量 | weight | decimal | (19,4) |  | 重量 |
| 单位名称 | unit_name | varchar |  |  | 单位名称 |
| sku零售价 | price | decimal | (19,4) |  | sku零售价 |
| sku批发价 | wholesale_price | decimal | (19,4) |  | sku批发价 |
| sku图片 | image_url | varchar |  |  | sku图片 |
| spu图片 | spu_img_url | varchar |  |  | spu图片 |


### api_goods_stock_change_ack_Y：库存同步回写

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `api_goods_stock_change_ack_Y` |
| PHP 文件 | `api_goods_stock_change_ack.php` |
| 文档标题 | 库存同步回写 |
| 描述 | 库存量同步至平台是否成功的状态批量回传给旺店通ERP 注：仅支持自有/其他平台店铺 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=api_goods_stock_change_ack_Y |

#### 接口说明

| 1.1 接口描述：库存量同步至平台是否成功的状态批量回传给旺店通ERP   注：仅支持自有/其他平台店铺 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 注意事项：先执行完“查询库存同步接口”（api_goods_stock_change_query.php），再执行本接口 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/api_goods_stock_change_ack.php |
| 正式环境 | https://openapi.huice.com/openapi/api_goods_stock_change_ack.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = ' ';<br>    $c->appkey = ' ';<br>    $c->appsecret = " ";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/api_goods_stock_change_ack.php';<br><br>    $stock_sync_list = array(<br>        array(<br>            'rec_id' => '2754327482516635662',<br>            'sync_stock' => '6',<br>            'stock_change_count' => '4',<br>	    'syn_status'=> '0'<br>        ),<br>	array(<br>            'rec_id' => '2769302115481288729',<br>            'sync_stock' => '0',<br>            'stock_change_count' => '1',<br>	    'syn_status'=> '1'<br>        )<br>    );<br><br>    $c->putApiParam('stock_sync_list',json_encode($stock_sync_list,JSON_UNESCAPED_UNICODE));<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

| JSON | {<br>    "code": 2090,<br>    "message": "appkey已停用"<br>} |
| --- | --- |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 库存同步状态回传列表 | stock_sync_list | data[] |  | 是 | 请求参数的1级数据节点，包含库存同步状态的数据节点,节点下数据字段详见下述“stock_sync_list” |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 处理失败的错误列表 | errors | data | data[] | 否 | 处理失败的错误列表,当code为0且有错误信息时才非空.只列出同一批内有错误的记录.如果code=0,errors为空说明全部成功 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| ERP内平台货品表主键id | rec_id | bigint | 20 | 是 | 回写的记录id，见api_goods_stock_change_query中rec_id |
| 货品库存 | sync_stock | int | 11 | 是 | 货品库存，该值为api_goods_stock_change_query 中的值回传即可 |
| 库存变化时自增 | stock_change_count | int | 11 | 是 | 该值为api_goods_stock_change_query 中的值回传即可 |
| 成功标识 | syn_status | int |  | 是 | 0 失败 1 成功 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误的数据rec_id | rec_id | bigint | 20 | 是 | ERP内平台货品表主键id |
| 错误信息的描述 | error | varchar | 255 | 否 | 错误信息的描述 |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "errors": [

    ]
}
```


### stockin_order_push_Y：创建入库单

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stockin_order_push_Y` |
| PHP 文件 | `stockin_order_push.php` |
| 文档标题 | 创建入库单 |
| 描述 | 调用本接口在旺店通ERP创建对应类型的入库单，增加库存。 |
| 客户端路径 | 仓储→入库管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stockin_order_push_Y |

#### 接口说明

| 1.1 接口描述：旺店通ERP需要增加库存且入库单据没有对应的业务类型，调用本接口在旺店通ERP创建其他入库单，增加库存。 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 注意事项：该接口不支持创建委外类型仓库的其他入库单，涉及序列号sn推送，建议每单sn数量不超过2000 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stockin_order_push.php |
| 正式环境 | https://openapi.huice.com/openapi/stockin_order_push.php |

| PHP | <?php<br>	require_once('../WdtClient.php');<br>    $c = new WdtClient;<br>    $c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>    //测试环境地址<br>    //上线时需要换成线上的<br>	$c->gatewayUrl = 'https://openapitest.huice.com/openapi/stockin_order_push.php'; // 测试的<br>	//$c->gatewayUrl = 'https://openapi.huice.com/openapi/stockin_order_push.php'; //正式的<br>    $spec_item = new stdClass();<br>    $spec_item->sku_no = "test1";<br>    $spec_item->real_num = "1";<br>    $spec_item->stockin_price = "1";<br>    $stock_in_order_detail_list = [$spec_item];<br><br>    $c->putApiParam('outer_no', 'test1');<br>    $c->putApiParam('warehouse_id', '130');<br>    $c->putApiParam('src_order_type', 6);<br>    $c->putApiParam("stock_in_order_detail_list", json_encode($stock_in_order_detail_list, JSON_UNESCAPED_UNICODE));<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 外部单号 | outer_no | varchar | 40 | 是 | 外部系统的唯一单据编号，避免重复推送数据 |
| 仓库id | warehouse_id | varchar | 40 |  | 代表仓库所有属性的唯一ID，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 物流编号 | logistics_code | varchar | 20 | 否 | 代表物流所有属性的唯一编码，用于物流区分，ERP内支持自定义（ERP物流界面设置） |
| 物流单号 | logistics_no | varchar | 40 | 否 | 物流公司的运单号，用于追踪物流、快递流转信息（路由）的数字编码 |
| 是否仅保存 | is_save | bool | 1 | 否 | 传false自动审核    传true为不审核    默认为false |
| 邮资 | post_amount | decimal | (19,4) | 否 | 物流或者快递运输货物产生的费用 |
| 备注 | remark | varchar | 255 | 否 | 其他入库单备注 |
| 入库原因 | reason | varchar | 255 | 否 | 入库原因（需要在客户端维护好该原因，如客户端无该原因或者原因停用，则推送失败） |
| 货品明细节点 | stock_in_order_detail_list | data[] |  | 是 | 入库单货品列表节点 |
| 源单类型 | src_order_type | int | 11 | 是 | 源单类型-目前仅允许其他入库(type=6)、采购入库(type=1)和调拨入库(type=2) |
| 源单号 | src_order_no | varchar | 40 | 是 | 上层单据编号，如果是采购入库就是采购单号，调拨入库就是调拨号，以此类推 |
| 是否更新覆盖生产批号 | is_coverage_production_batch_no | int |  | 否 | 是否更新覆盖生产批号。1：覆盖  0和其他都不覆盖 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 入库单号 | stockin_no | varchar | 40 | 是 | ERP系统生成入库单据分配的单号 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | sku_no | varchar | 40 | 是 | ERP内单品唯一编码（SKU），代表单品(SKU)所有属性，<br>并且为库存量出入计算最小单元。注：推送的sku_no值在ERP货品档案必须存在，否则单据会创建失败。 |
| 源单明细id | src_order_detail_id | int | 11 | 否 | 源单明细id（采购入库必传） |
| 入库数量 | real_num | decimal | (19,4) | 是 | 入库数量 |
| 货位编号 | position_no | varchar | 20 | 否 | 商品在仓库内的位置编号 |
| 批次 | batch_no | varchar | 20 | 否 | 货品批次编号 |
| 生产日期 | production_date | datetime |  | 否 | 货品生产日期，格式：yyyy-MM-dd HH:mm:ss |
| 有效期天数 | validity_days | int | 11 | 否 | 商品有效期，单位：天 |
| 有效期 | expire_date | datetime |  | 否 | 有效期日期，格式：yyyy-MM-dd HH:mm:ss |
| 序列号信息 | sn_info | varchar |  | 否 | 序列号信息，多个以逗号分隔。开启序列号入库强管控配置时，序列号必填 |
| 入库价 | stockin_price | decimal | (19,4) | 是 | 入库价格，如不传该字段入库价默认取0 |
| 入库金额 | stockin_amount | decimal | (19,4) | 否 | 入库金额，默认：数量*单价 |
| 明细备注 | remark | varchar | 255 | 否 | 明细备注 |
| 生产批号 | production_batch_no | varchar | 64 | 否 | 生产批号 |


#### 响应示例

### JSON

```text
{
    "code":0,
    "message":"",
    "stockin_no":"RK2512300005",
    "fail_item_list":null
}
```

### JSON

```text
{
    "code":21000003,
    "message":"必要参数缺失：src_order_type"
}
```


### stock_sync_by_pd_Y：创建盘点单

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_sync_by_pd_Y` |
| PHP 文件 | `stock_sync_by_pd.php` |
| 文档标题 | 创建盘点单 |
| 描述 | 旺店通ERP库存需要调整时，推送盘点库存单据给旺店通ERP，覆盖旺店通ERP实物库存。 注：旺店通ERP盘点成功后，盘点单内的库存值直接覆盖前库存 |
| 客户端路径 | 仓储→仓库盘点 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_sync_by_pd_Y |

#### 接口说明

| 1.1 接口描述：旺店通ERP库存需要调整时，推送盘点库存单据给旺店通ERP，覆盖旺店通ERP实物库存。                        注：旺店通ERP盘点成功后，盘点单内的库存值直接覆盖前库存 |
| --- |
| 1.2 创建盘点分支场景说明：①单品盘点：将mode传为1，type传为1，按照仓库+商品+数量维度进行盘点；②货位盘点：按照仓库+商品+货位+数量维度进行盘点，将mode固定传为2，type传为1时，只变更该商品盘点货位的库存，其他货位库存不变；type传为2时，对该商品盘点货位库存进行传入数量盘点，其他货位库存盘点为0，具体场景说明如下：假设仓库1 A商品库存情况为 A1货位库存10；A2货位库存20；A3货位库存30，此时传输盘点信息为仓库1 A商品 货位A1 盘点数量20当mode传为2，type传为1后库存情况：仓库1 A商品库存情况为 A1货位库存20；A2货位库存20；A3货位库存30当mode传为2，type传为2后库存情况：仓库1 A商品库存情况为 A1货位库存20；A2货位库存0；A3货位库存0③明细盘点：将mode传为3，type传为1，按照仓库+商品+货位+批次+效期+数量维度进行盘点；特别说明：当mode传为3时，position字段为必传字段；Y极速版不支持货位盘点与明细盘点方案，如有需要请联系旺店通商务人员沟通 |
| 1.3 注意事项：①：本接口调用时占用服务器资源较多，会影响客户端功能执行效率，因此不要频繁调用，                        且推送时盘点单货品明细控制在500条及以下,如盘点明细过多，分多次推送。                        ②：在客户端不做发货操作时调用本接口，一般在前一天20:00以后至下一天凌晨6:00之前。                        如一个请求包含明细过多，分多次请求。                        ③：该接口调用日上限2000次。 |


#### 调用场景

| 2.1举例说明：线下ERP、SAP等系统对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_sync_by_pd.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_sync_by_pd.php |

| PHP | <?php<br>    require_once('../WdtClient.php');<br>    $c = new WdtClient;<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    //测试环境地址<br>    //上线时需要换成线上的<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stock_sync_by_pd.php'; // 测试的<br>    //$c->gatewayUrl = 'https://openapi.huice.com/openapi/stock_sync_by_pd.php'; //正式的<br>    $spec_item = new stdClass();<br>    $spec_item->spec_no = "test1";<br>    $spec_item->stock_num = "555";<br>    $goods_list = [$spec_item];<br><br>    $c->putApiParam('api_outer_no', 'pdnoxxxx');<br>    $c->putApiParam('warehouse_id', '130');<br>    $c->putApiParam("goods_list", json_encode($goods_list, JSON_UNESCAPED_UNICODE));<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 |  |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通网页API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库id | warehouse_id | int | 11 |  | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| API单号 | api_outer_no |  | 40 | 是 | 外部单号唯一标识 |
| 货品明细列表节点 | goods_list | data[ ] |  | 是 | 货品明细列表节点 |
| 盘点方案 | mode | int | 11 | 否 | 盘点方案：1.单品盘点（默认） 2.货位盘点 3.明细盘点 |
| 盘点类型 | type | int | 11 | 否 | 盘点类型：1.货品盘点（默认） 2.货位盘点  注：货位盘点（mode=2）时盘点类型才可以为货位盘点 |
| 严格模式 | is_post_error | int | 11 | 否 | 默认为非严格模式is_post_error=0。is_post_error=1,为严格模式盘点单中货品明细不允许部分盘点成功，全部盘点成功才成功，存在盘点失败的，则整单失败。is_post_error=0 非严格模式表示盘点单货品明细允许部分推送成功(盘点单内spec_no在ERP货品档案存在的部分创建成功，不存在的部分创建失败); |
| 是否添加库存记录 | is_create_stock | int | 11 | 否 | 默认为is_create_stock=1。is_create_stock=0表示不自动添加库存记录。is_create_stock=1表示自动添加库存记录 。注意:明细盘点不自动添加库存 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | varchar | 255 | 是 | 错误信息 |
| 明细校验失败列表 | warning | data[ ] | 255 | 否 | 返回创建失败的商品信息。创建成功，返回一个空的数组。 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec_no | varchar | 40 | 是 | 代表单品(sku)所有属性的编码，SKU概念介绍,单击这里 |
| 盘点数量 | stock_num | decimal | (19,4) | 是 | 盘点数量（盘点推送的库存数量指覆盖数量，不是调整数量） |
| 货位 | position_no | varchar | 40 | 否 | 货位；注：货位盘点（mode=2）或明细盘点（mode=3）时必传 |
| 批次 | batch_no | varchar |  | 否 | 批次编号 不传默认为空;注:明细盘点（mode=3）使用; |
| 有效期 | expire_date | varchar |  | 否 | 有效期 注:明细盘点使用;日期格式：[yyyy-MM-dd]不要时间time |
| 生产日期 | production_date | varchar |  | 否 | 生产日期 注:明细盘点使用;日期格式：[yyyy-MM-dd]不要时间time |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec_no | varchar | 40 | 否 | 代表单品(sku)所有属性的编码，SKU概念介绍,单击这里 |
| 错误信息 | error_msg | varchar |  | 否 | 错误信息 |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "pd_no": null,
    "warning": []
}
```

### JSON

```text
{
    "code": 21000006,
    "message": "外部单号重复，请保证外部单号[api_outer_no]的唯一性"
}
```


### stock_query_Y：查询可用库存

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_query_Y` |
| PHP 文件 | `stock_query.php` |
| 文档标题 | 查询库存成本 可用库存数据 |
| 描述 | 查询库存成本 可用库存数据 |
| 客户端路径 | 仓储→库存查询 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP查询库存成本 可用库存数据 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取：按照ERP库存记录的最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |


#### 调用场景

| 2.1举例说明：财务系统、SAP、数据分析等系统的对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_query.php |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    //测试环境地址<br>    //上线时需要换成线上的<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    //测试环境地址<br>    //上线时需要换成线上的<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stock_query.php';<br><br>    $c->putApiParam("page_no", "0");<br>    $c->putApiParam("page_size", "100");<br>    $c->putApiParam("spec_no_list", '["xxx","xxx2"]');<br>    //$c->putApiParam("start_time", "2025-01-09 15:00:00");<br>    //$c->putApiParam("end_time", "2025-01-11 15:00:00");<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 |  |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通网页API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 是 | 按时间增量获取数据,start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按时间增量获取数据,end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 商家编码 | spec_no | string |  | 否 | 商家编码（新），商家编码和开始结束时间必传一项 |
| 商家编码列表 | spec_no_list | string[] |  | 否 | 商家编码（新）批量查询，示例："spec_no_list":"[\"spec1\", \"spec2\"]"，上限为200条商家编码，时间范围和商家编码在查询时必须要有一个不为空 |
| 仓库id | warehouse_id | tinyint |  | 否 | 仓库主键，代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar |  | 否 | 仓库编号，代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 是否残次品 | defect | tinyint |  | 否 | 0否 1是 |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~1000，不传本参数，输入值默认为100，使用举例单击这里 |
| 页号 | page_no | int |  | 否 | 页号默认从0开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 入库单详情 | stocks | data[] |  | 否 | 库存节点数据 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "stocks": [<br>        {<br>            "spec_id": "2646773608436727836",<br>            "warehouse_id": "233",<br>            "rec_id": "2777490266540474390",<br>            "goods_no": "test1",<br>            "brand_no": "2744980845566624770",<br>            "brand_name": "测试品牌",<br>            "goods_name": "test1",<br>            "spec_no": "test1_1",<br>            "spec_name": "默认规格",<br>            "spec_code": "",<br>            "barcode": "",<br>            "stock_num": "50.0000",<br>            "available_num": "50.0000",<br>            "unit": "",<br>            "remark": "",<br>            "cost_price": "0.0000",<br>            "avg_cost_price": "0.0000",<br>            "defect": 0,<br>            "created": "2025-12-26 09:54:42",<br>            "modified": "2025-12-26 09:54:53",<br>            "virtual_num": "0.0000"<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务响应参数

| 字段名称 | 字段 | 类型 | 长度 | 是否必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单品主键id | spec_id | bigint(20) |  | 是 | 单品主键 |
| 仓库主键id | warehouse_id | int(11) |  | 是 | 仓库主键，代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar |  | 是 | 仓库编号，代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| ERP库存id | rec_id | bigint(20) |  | 是 | 库存明细主键 |
| 货品编号 | goods_no | string |  | 是 | 货品编号 |
| 品牌编号 | brand_no | string |  | 是 | 品牌编号 |
| 品牌名称 | brand_name | string |  | 是 | 品牌名称 |
| 货品名称 | goods_name | string |  | 是 | 品牌名称 |
| 商家编码 | spec_no | string |  | 是 | 商家编码 |
| 规格名称 | spec_name | string |  | 是 | 规格名称 |
| 规格码 | spec_code | string |  | 是 | 规格码 |
| 条形码 | barcode | string |  | 是 | 条形码 |
| 库存量 | stock_num | decimal(21, 6) |  | 是 | 库存量 |
| 可用库存 | available_num | decimal(21, 6) |  | 是 | 可用库存 |
| 辅助单位 | unit | string |  | 是 | 辅助单位名称 |
| 备注 | remark | string |  | 是 | 备注 |
| 成本价 | cost_price | decimal(21, 6) |  | 是 | 商品档案的固定成本价 |
| 虚拟库存 | virtual_num | decimal(21, 6) |  | 是 | 虚拟库存 |
| 仓库名称 | warehouse_name | string |  | 是 | 仓库名称 |
| 退货在途量 | refund_onway_num | decimal(21, 6) |  | 是 | 退货在途量 |
| 委外库存 | outer_stock_num | decimal(21, 6) |  | 是 | 委外库存 |
| 已审核量 | audited_num | decimal(21, 6) |  | 是 | 已审核量 |
| 待审核量 | unaudited_num | decimal(21, 6) |  | 是 | 待审核量 |
| 预约单量 | pre_sale_num | decimal(21, 6) |  | 是 | 预约单量 |
| 特殊单量 | special_sale_num | decimal(21, 6) |  | 是 | 特殊单量 |
| 采购在途量 | purchase_in_transit_num | decimal(21, 6) |  | 是 | 采购在途量 |
| 调拨在途量 | transfer_num | decimal(21, 6) |  | 是 | 调拨在途量 |
| 待调拨量 | to_transfer_num | decimal(21, 6) |  | 是 | 待调拨量 |
| 未付款量 | no_pay_sale_num | decimal(21, 6) |  | 是 | 未付款量 |
| 销退暂存位 | refund_position_num | decimal(21, 6) |  | 是 | 销退暂存位 |
| 异常库存 | abnormal_stock_nu | decimal(21, 6) |  | 是 | 异常库存 |
| 锁定量 | stock_lock_num | decimal(21, 6) |  | 是 | 锁定量 |
| 平均成本价 | avg_cost_price | decimal(21, 6) |  | 是 | 库存查询-成本价字段，支持不同成本价模式取值。加权平均和先进先出模式下，为平均成本价 |
| 是否残次品 | defect | tinyint(4) |  | 是 | 0否 1是 |
| ERP创建时间 | created | datetime |  | 是 | ERP创建时间 |
| ERP更新时间 | modified | datetime |  | 是 | ERP更新时间 |


#### 响应示例

### JSON

```text
{
    "code": 21000024,
    "message": "未查询到任何货品，请检查商家编码（新）是否正确！"
}
```


### stockout_order_push_Y：创建出库单

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stockout_order_push_Y` |
| PHP 文件 | `stockout_order_push.php` |
| 文档标题 | 创建出库单 |
| 描述 | 推送出库单给旺店通ERP，并执行出库操作（扣减库存等） |
| 客户端路径 | 仓储→出库管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stockout_order_push_Y |

#### 接口说明

| 1.1 接口描述：旺店通ERP需要减少库存且出库单据没有对应的业务类型，推送其他出库单给旺店通ERP，并执行出库操作（扣减库存等），在旺店通ERP中属于其他出库，order_type类型记录在单据的remark备注信息中。 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 注意事项：该接口不支持创建委外类型仓库的其他出库单，涉及序列号sn推送，建议每单sn数量不超过2000 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stockout_order_push.php |
| 正式环境 | https://openapi.huice.com/openapi/stockout_order_push.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stockout_order_push.php';<br><br>    $c->putApiParam("outer_no", "5558895550044");<br>    $c->putApiParam("warehouse_id", 38);<br>    $c->putApiParam("remark", "测试出库单");<br>    $c->putApiParam("src_order_type", 7);<br>    $c->putApiParam("src_order_no","7777789856666800");<br>    $order_detail_list = array (<br>            array (<br>                "sku_no" => "644400818",<br>                "num" => "1",<br>                "stockout_price" => "12",<br>                "batch_no" =>"0090"<br>            )<br>     );<br><br>    $c->putApiParam('order_detail_list', json_encode($order_detail_list, JSON_UNESCAPED_UNICODE));<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 外部单号 | outer_no | varchar | 40 | 是 | 外部系统的唯一单据编号，避免重复推送数据 |
| 是否审核 | stockout_flag | tinyint | 1 | 否 | 1：自动审核 0：不自动审核(默认1) |
| 仓库id | warehouse_id | varchar | 40 |  | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 物流编号 | logistics_code | varchar | 20 | 否 | 代表物流所有属性的唯一编码，用于物流区分，ERP内支持自定义（ERP物流界面设置） |
| 物流单号 | logistics_no | varchar | 40 | 否 | 物流公司的运单号 |
| 备注 | remark | varchar | 255 | 否 | 其他出库单备注 |
| 出库原因 | reason | varchar | 255 | 否 | 其他出库原因（需要在客户端维护好该原因，如客户端无该原因或者原因停用，则推送失败） |
| 货品列表节点 | order_detail_list | data[] |  | 是 | 请求参数的2级数据节点，包含其他出库单所有货品属性信息的数据节点 |
| 源单类型 | src_order_type | int | 11 | 是 | 源单类型-目前仅允许其他出库(type=7)、和调拨出库(type=2)和采购退货出库(type=3) |
| 源单号 | src_order_no | varchar | 40 | 是 | 上层单据编号 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 出库单号 | stockout_no | varchar | 40 | 是 | 出库单号 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | sku_no | varchar | 40 | 是 | 代表单品(sku)所有属性的编码 |
| 源单明细id | src_order_detail_id | int | 11 | 否 | 源单明细id |
| 出库数量 | num | decimal | (19,4) | 是 | 出库数量 |
| 价格 | stockout_price | decimal | (19,4) | 是 | 价格，默认为0 |
| 出库金额 | stockout_amount | decimal | (19,4) | 否 | 出库金额，默认：数量*单价 |
| 货位编号 | position_no | varchar | 20 | 否 | 货位编号 |
| 序列号信息 | sn_info | varchar |  | 否 | 序列号信息，多个以逗号分隔。开启序列号入库强管控配置时，序列号必填 |
| 批次号 | batch_no | varchar | 20 | 否 | 指定批次号 |
| 生产日期 | production_date | datetime |  | 否 | 时间格式：yyyy-MM-dd HH:mm:ss |
| 有效期 | expire_date | datetime |  | 否 | 时间格式：yyyy-MM-dd HH:mm:ss |
| 备注 | remark | varchar | 255 | 否 | 货品明细备注 |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "stockout_no": "CKQ2602130001",
    "fail_item_list": null
}
```

### JSON

```text
{
    "code": 21000011,
    "message": "当前仓库中不存在货位: 0090"
}
```


### pick_status_ack_Y：分拣单状态回写接口

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `pick_status_ack_Y` |
| PHP 文件 | `pick_status_ack.php` |
| 文档标题 | 分拣单状态回传 |
| 描述 | 修改租户系统内分拣单的状态 |
| 客户端路径 | 仓储→分拣单管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=pick_status_ack_Y |

#### 接口说明

| 1.1 接口描述：分拣设备回传分拣单状态处理 |
| --- |
| 1.2 适应版本：网页版 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/pick_status_ack.php |
| 正式环境 | https://openapi.huice.com/openapi/pick_status_ack.php |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient;<br>    //sid appkey appsecret 需要换成自己的<br>    $c->sid ='haijun';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    //测试环境地址<br>    //上线时需要换成线上的<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/pick_status_ack.php';<br><br>	$c->putApiParam('pick_finished_send', "1");<br>		$c->putApiParam('status', "40");<br>			$c->putApiParam('pick_no', "PB260204000003");<br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果 |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分拣单号 | pick_no |  |  | 是 | 分拣单号 |
| 分拣单状态 | status |  |  | 是 | 35.分货中 40.分拣完成 |
| 分拣完成是否直接发货 | pick_finished_send |  |  | 否 | 0：否 ，1：是。默认是0（当该参数回传1，且分拣单状态回传40分拣完成时，同时触发系统订单发货） |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 失败的错误列表 | errors_list | data | data[] | 否 | 处理失败的错误列表 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误的系统单号 | trade_no | int | 40 | 是 | 错误的系统单号 |
| 错误原因 | error | varchar | 255 | 是 | 错误原因 |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "send_fail_list": null
}
```

### JSON

```text
{
    "code": 0,
    "message": "",
    "send_fail_list": [
        {
            "trade_no": "JY2601080728",
            "error": "发货异常:订单已其他系统发货"
        }
    ]
}
```


### pick_order_query_Y：查询分拣单接口

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `pick_order_query_Y` |
| PHP 文件 | `pick_order_query.php` |
| 文档标题 | 查询分拣单接口 |
| 描述 | 获取旺店通ERP分拣单信息 |
| 客户端路径 | 仓储→分拣单管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=pick_order_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP分拣单信息 |
| --- |
| 1.2 适用版本：网页版 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/pick_order_query.php |
| 正式环境 | https://openapi.huice.com/openapi/pick_order_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret ="";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/pick_order_query.php';<br><br>    $c->putApiParam('start_time','2026-03-10 11:08:57');<br>    $c->putApiParam('end_time','2026-03-19 10:08:57');<br>    $c->putApiParam('pick_no','PB260312000004');<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分拣单号 | pick_no | varchar |  | 是 | 分拣单号 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 分拣单信息 | pick_list | data[] |  | 否 | 响应参数的1级数据节点，包含当前页的分拣单及其明细的数据节点,节点下数据字段详见下述" pick_list"和“trade_item_list” |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "pick_list": [<br>        {<br>            "pick_no": "PB260312000004",<br>            "status": 10,<br>            "pick_type": 2,<br>            "order_num": 1,<br>            "goods_count": "113",<br>            "create_date": "2026-03-12 14:37:39",<br>            "pick_goods_list": [<br>                {<br>                    "trade_no": "JY2603040011",<br>                    "trade_status": 50,<br>                    "spec_no": "02012004502",<br>                    "barcode": "260303005",<br>                    "picklist_seq": 1,<br>                    "num": "103",<br>                    "share_amount": "10300",<br>                    "batch_list": [<br><br>                    ]<br>                },<br>                {<br>                    "trade_no": "JY2603040011",<br>                    "trade_status": 50,<br>                    "spec_no": "55555551166114",<br>                    "barcode": "260211006",<br>                    "picklist_seq": 1,<br>                    "num": "10",<br>                    "share_amount": "990",<br>                    "batch_list": [<br><br>                    ]<br>                }<br>            ]<br>        }<br>    ] |
| --- | --- |

| JSON | {<br>    "code": 11000000,<br>    "message": "分拣单不存在",<br>    "total_count": null,<br>    "pick_list": null<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分拣单号 | pick_no | varchar |  |  |  |
| 分拣单状态 | status | int |  |  | 5 已取消 10 待拣货 20 拣货中 30 拣货完成 35 分货中 40 分拣完成 50 完成 |
| 分拣单类型 | pick_type | int |  |  | 1 一单一货 2 一单多货 3 爆款 |
| 订单数量 | order_num | int |  |  | 分拣单下，系统订单数量 |
| 商品件数 | goods_count | decimal(19, 4) |  |  | 分拣单下，商品总件数 |
| 分拣单下订单详情 | pick_goods_list | data[] |  |  | 响应参数的2级数据节点，包含分拣单下订单明细所有属性信息，节点下数据字段详见下述“pick_goods_list” |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 系统订单号 | trade_no | varchar |  |  | 系统订单编号，JY单号 |
| 订单状态 | trade_status | int |  |  | 系统订单状态 |
| 商家编码（新） | spec_no | varchar |  |  | 商家编码 |
| 主条码 | barcode | varchar |  |  | 主条码 |
| 订单序号 | picklist_seq | int |  |  | 订单在分拣单中序号 |
| 数量 | num | decimal(19, 4) |  |  | 数量 |


### pick_trade_query_Y：查询分拣单订单

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `pick_trade_query_Y` |
| PHP 文件 | `pick_trade_query.php` |
| 文档标题 | 查询分拣单订单 |
| 描述 | 获取租户系统内分拣单的订单信息 |
| 客户端路径 | 仓储→分拣单管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=pick_trade_query_Y |

#### 接口说明

| 1.1 接口描述：获取租户系统内分拣单的订单信息 |
| --- |
| 1.2 适用版本：网页版 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/pick_trade_query.php |
| 正式环境 | https://openapi.huice.com/openapi/pick_trade_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/pick_trade_query.php';<br><br>	$c->putApiParam('start_time', '2026-03-01 16:00:40');<br>	$c->putApiParam('end_time', '2026-03-19 16:00:40');<br>	$c->putApiParam('warehouse_no', '38');<br>	$c->putApiParam('page_no', '0');<br>	$c->putApiParam('page_size', '1');<br><br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | date |  | 是 | 按创建时间增量获取数据,start_time作为开始时间，格式： yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | date |  | 是 | 按创建时间增量获取数据,end_time作为结束时间，格式： yyyy-MM-dd HH:mm:ss |
| 仓库编号 | warehouse_no | varchar |  | 是 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 页号 | page_no | int |  | 否 | 需要查询第page_no页的数据，不传值默认从第0页开始 |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数输入值默认为40 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 4.2 业务响应参数 |  |  |  |  |  |
| 数据条数 | total_count | int | 11 | 否 | 符合条件的数据条数 |
| 订单列表节点 | pick_list | data[] |  | 否 | 响应参数的1级数据节点，包含获取分拣单和货品信息的数据节点,节点下数据字段详见下述“pick_list”和" trade_info_list" |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "pick_list": [<br>        {<br>            "pick_no": "PB260313000005",<br>            "status": 5,<br>            "pick_type": 2,<br>            "warehouse_no": "38",<br>            "warehouse_name": "滑雪场器材仓库1",<br>            "trade_info_list": [<br><br>            ]<br>        }<br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 11000000,<br>    "message": "建单时间不正确",<br>    "total_count": null,<br>    "pick_list": null<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分拣单号 | pick_no | varchar |  |  | 分拣单号 |
| 仓库id | warehouse_no | varchar |  |  | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库名称 | warehouse_name | varchar |  |  | 仓库名称 |
| 分拣单状态 | status | int |  |  | 5 已取消 10 待拣货 20 拣货中 30 拣货完成 35 分货中 40 分拣完成 50 完成 |
| 分拣单类型 | pick_type | int |  |  | 1 一单一货 2 一单多货 3 爆款 |
| 订单列表 | trade_info_list | data[] |  |  | 分拣单的订单列表 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单编号 | trade_no | varchar |  |  | 系统订单编号，JY单号 |
| 订单状态 | trade_status | int |  |  | 系统订单状态 |
| 物流名称 | logistics_name | varchar |  |  | 物流名称 |


### stock_detail_report_query_Y：查询出入库明细表

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_detail_report_query_Y` |
| PHP 文件 | `stock_detail_report_query.php` |
| 文档标题 | 查询出入库明细表 |
| 描述 | 查询出入库明细表数据 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_detail_report_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP各种业务类型的出入库明细报表 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：自有商城接入ERP、金蝶接入、用友接入、SAP接入等 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_detail_report_query.php.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_detail_report_query.php.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once("../WdtClient.php");<br>	$client = new WdtClient;<br>	$client->sid = '';<br>	$client->appkey = '';<br>	$client->appsecret = "";<br>	$client->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stock_detail_report_query.php';<br><br>	$client->putApiParam('start_time', '2026-03-22 10:00:00');<br>	$client->putApiParam('end_time', '2026-03-26 10:59:59');<br>	$client->putApiParam('page_no', 0);<br>	$client->putApiParam('page_size', 1);<br>	$client->putApiParam('inout_type_list', '[3]');<br><br>	$response = $client->wdtOpenApi();<br>	var_dump($response);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | data |  | 是 | 按最后出入库时间增量获取数据,start_time作为开始时间，格式： YYYY-MM-DD HH:MM:SS |
| 结束时间 | end_time | data |  | 是 | 按最后出入库时间增量获取数据,end_time作为结束时间，格式： YYYY-MM-DD HH:MM:SS |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数 |
| 页号 | page_no | int |  | 否 | 不传值默认从0页开始 |
| 出入库类型列表 | inout_type_list | int[] |  | 否 | 示例: [1,2,3] 类型参照 -- 1: 采购入库\|2: 调拨入库\|3: 退货入库\|4: 盘盈入库\|5: 生产入库\|6: 其他入库\|8: 委外仓入库\|9: 委外入库\|10: 委外盘盈入库\|11: 直发入库\|15: 纠错入库\|16: 预入库\|20: 移位上架\|-1: 销售订单\|-2: 调拨出库\|-3: 采购退货出库\|-4: 盘亏出库\|-5: 生产出库\|-6: 现款销售出库\|-7: 其他出库\|-8: 委外仓出库\|-9: 委外出库\|-10: 委外盘亏出库\|-15: 纠错出库\|-20: 移位下架\| |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 否 | 错误描述 |
| 数据条数 | total_count | int | 11 | 否 | 只有page_no = 0 时才返回的符合条件的数据总条数，用来分页 |
| 数据 | data | List<StockReportVO> |  | 否 | 响应参数的1级数据节点，包含当前页的StockReportVO的数据节点,节点下数据字段详见下文 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": -1,<br>    "data": [<br>        {<br>            "prop1": "",<br>            "prop2": "",<br>            "prop3": "",<br>            "prop4": "",<br>            "prop5": "",<br>            "prop6": "",<br>            "prop7": "",<br>            "prop8": "",<br>            "prop9": "",<br>            "prop10": "",<br>            "sku_id": "2809736617546219530",<br>            "warehouse_id": "107",<br>            "sku_sort_name": "",<br>            "sku_no": "202603250930110001",<br>            "sku_name": "api-洋葱规格值",<br>            "sku_short_name": "",<br>            "barcode": "260325003",<br>            "spu_id": "2802198152277393421",<br>            "spu_name": "api-洋葱商品-勿动-复制",<br>            "spu_short_name": "",<br>            "spu_no": "2029034896470814722",<br>            "spu_modify_date": "2026-03-26 17:00:12",<br>            "plat_spu_no": "2029034896470814722",<br>            "plat_sku_no": "",<br>            "image_url": "",<br>            "spu_img_url": "",<br>            "outer_sku_no": "",<br>            "ref_cost_price": "1450",<br>            "price": "0.01",<br>            "retail_price": "0.01",<br>            "wholesale_price": "0",<br>            "validity_days": 0,<br>            "unit_id": "0",<br>            "unit_name": "",<br>            "weight": "0",<br>            "box_sku_num": 0,<br>            "sku_remark": "",<br>            "sku_delete_flag": false,<br>            "brand_id": "0",<br>            "brand_name": "",<br>            "goods_category_id": "0",<br>            "approval_number": "",<br>            "warehouse_name": "01",<br>            "log_type": 1,<br>            "stock_type": 1,<br>            "src_order_type": 3,<br>            "in_out_type": "退货入库",<br>            "src_id": "2810112388194369541",<br>            "src_detail_id": "2810112388194370565",<br>            "src_order_no": "RK2603260001",<br>            "stockin_no": "RK2603260001",<br>            "stockout_no": null,<br>            "num": "2",<br>            "in_num": "2",<br>            "out_num": null,<br>            "create_date": "2026-03-26 10:23:22",<br>            "create_by": "3689",<br>            "create_name": "renmaolin-test",<br>            "expire_date": "9999-12-01T00:00:00",<br>            "production_date": "9999-12-01T00:00:00",<br>            "batch_no": "",<br>            "position_id": null,<br>            "position_no": "",<br>            "cost_price": "1450"<br>        }<br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 1020,<br>    "message": "单独筛选出入库时间，时间跨度不可超过一个月",<br>    "total_count": 0,<br>    "data": null<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库id | warehouse_id | Long |  | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库名称 | warehouse_name | Long |  | 是 |  |
| 货品名称 | spu_name | Long |  | 是 |  |
| 货品简称 | spu_short_name | Long |  | 是 |  |
| 货品编码 | spu_no | varchar |  | 是 |  |
| 规格名称 | sku_name | varchar |  | 是 |  |
| 规格简称 | sku_short_name | varchar |  | 是 |  |
| 商家编码（新） | sku_no | varchar |  | 是 |  |
| 出入库类型 | in_out_type | varchar |  | 是 |  |
| 源单ID | src_id | Long |  | 是 | 出入库主单ID |
| 源单明细ID | src_detail_id | Long |  | 是 | 出入库明细ID |
| 入库单号 | stockin_no | varchar |  | 是 | stockin_no和stockout_no只会有一个 |
| 出库单号 | stockout_no | varchar |  | 是 | stockin_no和stockout_no只会有一个 |
| 单号 | src_order_no | varchar |  | 是 | 统一的单号 |
| 入库数量 | in_num | decimal | (19,4) | 是 | in_num和out_num只会有一个 |
| 出库数量 | out_num | decimal | (19,4) | 是 | in_num和out_num只会有一个 |
| 数量 | num | decimal | (19,4) | 是 | 统一的数量 |
| 出入库时间 | create_date | datetime |  | 是 |  |
| 操作人 | create_by | varchar |  | 是 |  |
| 成本价 | cost_price | decimal |  | 是 |  |
| 批次 | batch_no | varchar |  | 是 |  |
| 生产日期 | production_date | datetime |  | 是 |  |
| 有效期 | expire_date | datetime |  | 是 |  |
| 货位ID | position_id | Long |  | 是 |  |
| 货位编号 | position_no | varchar |  | 是 |  |
| SKUID | sku_id | Long |  | 是 |  |
| SPUID | spu_id | Long |  | 是 |  |
| 库存属性 | stock_type | int |  | 是 |  |
| 业务单类型 | src_order_type | int | 11 | 是 | 源单号类型类型参照 -- 入库单：1: 采购入库\|2: 调拨入库\|3: 退货入库\|4: 盘盈入库\|5: 生产入库\|6: 其他入库\|8: 委外仓入库\|9: 委外入库\|10: 委外盘盈入库\|11: 直发入库\|15: 纠错入库\|16: 预入库\|20: 移位上架出库单：1,98,99: 销售订单\|2: 调拨出库\|3: 采购退货出库\|4: 盘亏出库\|5: 生产出库\|6: 现款销售出库\|7: 其他出库\|8: 委外仓出库\|9: 委外出库\|10: 委外盘亏出库\|15: 纠错出库\|20: 移位下架\| |


### stock_inout_sn_query_Y：查询出入库序列号

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_inout_sn_query_Y` |
| PHP 文件 | `stock_inout_sn_query.php` |
| 文档标题 | 查询出入库序列号 |
| 描述 | 获取旺店通ERP各种业务类型的SN出入库明细 |
| 客户端路径 | 仓储→出库管理/入库管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_inout_sn_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP各种业务类型的SN出入库明细 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：SAP、线下ERP、SRM、SCM等系统对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_inout_sn_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_inout_sn_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stock_inout_sn_query.php';<br><br>	$c->putApiParam('order_no', 'RK2603180008');<br>	$c->putApiParam('order_type', 1); //0 出库单 1 入库单，默认0<br>	$c->putApiParam('page_no', 0);<br>	$c->putApiParam('page_size', 1);<br><br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出入库单号 | order_no | varchar |  | 否 | 出入库单号 |
| 出入库类型 | order_type | int |  | 否 | 0 出库单 1 入库单，默认0 |
| 出入库单号批量查询 | order_no_list | String[] |  | 否 | 根据出入库单号批量查询，批量查询单号时，必须指定出入库类型 |
| 分页大小 | page_size | int |  | 否 | 每页返回条数 |
| 页号 | page_no | int |  | 否 | 不传值默认从0页开始 |
| 业务单类型 | src_order_type | int |  | 否 | 类型参照 -- 1: 采购入库\|2: 调拨入库\|3: 退货入库\|4: 盘盈入库\|5: 生产入库\|6: 其他入库\|8: 委外仓入库\|9: 委外入库\|10: 委外盘盈入库\|11: 直发入库\|15: 纠错入库\|16: 预入库\|20: 移位上架\|-1: 销售订单\|-2: 调拨出库\|-3: 采购退货出库\|-4: 盘亏出库\|-5: 生产出库\|-6: 现款销售出库\|-7: 其他出库\|-8: 委外仓出库\|-9: 委外出库\|-10: 委外盘亏出库\|-15: 纠错出库\|-20: 移位下架\| |
| 序列号 | sn | varchar |  | 否 | 序列号 |
| 规格编码 | spec_no | varchar |  | 否 | 商家编码 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int |  | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar |  | 否 | 错误描述 |
| 查询总数 | total_count | int |  | 否 | 分页查询总数 |
| 数据 | data | List<StockSnSrcDetailVO> |  | 否 | 分页查询结果 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "data": [<br>        {<br>            "id": "2807210582220996610",<br>            "sn": "SN2603180012",<br>            "sku_id": "2769302345274621977",<br>            "spec_no": "c9901244441229c1",<br>            "create_date": "2026-03-18T10:12:38",<br>            "order_id": "2807210481729667074",<br>            "order_no": "RK2603180008",<br>            "src_order_no": "00002603090002",<br>            "src_order_type": 6,<br>            "stock_inout_detail_id": "2807210481729668098"<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出入库单号 | order_no | varchar | 40 | 是 | 出入库单号 |
| 出入库明细id | stock_inout_detail_id | long |  | 是 | 出入库明细主键id |
| 业务单类型 | src_order_type | int | 11 | 是 | 源单号类型类型参照 -- 入库单：1: 采购入库\|2: 调拨入库\|3: 退货入库\|4: 盘盈入库\|5: 生产入库\|6: 其他入库\|8: 委外仓入库\|9: 委外入库\|10: 委外盘盈入库\|11: 直发入库\|15: 纠错入库\|16: 预入库\|20: 移位上架出库单：1,98,99: 销售订单\|2: 调拨出库\|3: 采购退货出库\|4: 盘亏出库\|5: 生产出库\|6: 现款销售出库\|7: 其他出库\|8: 委外仓出库\|9: 委外出库\|10: 委外盘亏出库\|15: 纠错出库\|20: 移位下架\| |
| 业务单号 | src_order_no | varchar | 40 | 是 | 源单号 |
| 序列号 | sn | varchar | 40 | 是 | 序列号 |
| 商家编码 | spec_no | varchar | 40 | 是 | 商家编码 |
| 创建时间 | created | datetime |  | 是 | 创建时间，格式：yyyy-MM-dd HH:mm:ss |


#### 响应示例

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### stock_transfer_query_Y：查询调拨单及明细

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_transfer_query_Y` |
| PHP 文件 | `stock_transfer_query.php` |
| 文档标题 | 查询调拨单及明细 |
| 描述 | 获取旺店通ERP调拨单及明细信息 |
| 客户端路径 | 仓储→调拨管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_transfer_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP调拨单及明细信息 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：获取旺店通ERP调拨单及明细信息 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_transfer_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_transfer_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once ('../WdtClient.php');<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stock_transfer_query.php';<br><br>    $c->putApiParam('start_time', '2026-03-17 00:42:22');<br>    $c->putApiParam('end_time', '2026-03-17 23:42:22');<br>    $c->putApiParam('type', '1');<br>    $c->putApiParam('status', '90');<br>    $c->putApiParam('page_no', '0');<br>    $c->putApiParam('page_size', '1');<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量获取数据,start_time作为开始时间,格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量获取数据,end_time作为结束时间,格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int | 10 | 否 | 每页返回条数，输入值范围1~100，不传默认40，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 调出仓库 | from_warehouse_no | varchar | 40 | 否 | 源仓库编号，代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置） |
| 调入仓库 | to_warehouse_no | varchar | 40 | 否 | 目标仓库编号，代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置） |
| 调拨单号 | transfer_no | varchar | 20 | 否 | 系统调拨单的编号，默认DB开头 |
| 调拨单状态 | status | tinyint | 4 | 否 | 调拨单状态10已取消 30待审核 40已审核 42出库单待推送 44出库单推送失败 46待出库 50部分出库 60全部出库 62入库单待推送 64入库单推送失败 66待入库 70部分入库 90调拨完成 (不传该字段默认返回全部状态的单据) |
| 调拨类型 | type | tinyint | 4 | 是 | 调拨类型（0：分步调拨，1：快速调拨） |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 调拨单数据 | transfer_list | data[] |  | 否 | 调拨单数据节点 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": "2",<br>    "transfer_list": [<br>        {<br>            "transfer_id": "2806836923887255575",<br>            "transfer_no": "DB2603170004",<br>            "type": 1,<br>            "from_warehouse_no": "38",<br>            "to_warehouse_no": "95",<br>            "from_wms_order_no": "",<br>            "to_wms_order_no": "",<br>            "status": 90,<br>            "creator_name": "system",<br>            "goods_count": "10",<br>            "goods_type_count": "1",<br>            "goods_in_count": "10",<br>            "goods_out_count": "10",<br>            "modified": "2026-03-17 09:27:52",<br>            "created": "2026-03-17 09:27:51",<br>            "remark": null,<br>            "details_list": [<br>                {<br>                    "transfer_id": "2806836923887255575",<br>                    "rec_id": "2806836923891449879",<br>                    "goods_no": "200221005589#26021028375510",<br>                    "spec_no": "c971152331c1",<br>                    "spec_code": "",<br>                    "spec_name": "260210的谷歌名称",<br>                    "unit": "0",<br>                    "barcode": "260210511",<br>                    "out_cost_total": "0.0000",<br>                    "batch_no": "",<br>                    "from_position": null,<br>                    "to_position": null,<br>                    "expire_date": null,<br>                    "stock_num": "0",<br>                    "num": "10",<br>                    "remark": "调拨"<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 调拨主键id | transfer_id | int | 11 | 是 | 调拨主键id |
| 调拨单号 | transfer_no | varchar | 20 | 是 | 系统调拨单的编号，默认DB开头 |
| 调拨类型 | type | tinyint | 4 | 是 | 调拨类型（0：分步调拨，1：快速调拨） |
| 外部单号 | outer_no | varchar | 40 | 是 | 外部单号，同创建调拨单接口入参outer_no |
| 调出仓库 | from_warehouse_no | varchar | 40 | 是 | 调出仓库编号，代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 调入仓库 | to_warehouse_no | varchar | 40 | 是 | 调入仓库编号，代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 推送出库单号 | from_wms_order_no | varchar | 40 | 是 | 推送出库单号 |
| 推送入库单号 | to_wms_order_no | varchar | 40 | 是 | 推送入库单号 |
| 调出仓储单号 | wms_out_no | varchar | 40 | 是 | 调出仓储单号 |
| 调入仓储单号 | wms_in_no | varchar | 40 | 是 | 调入仓储单号 |
| 调拨单状态 | status | tinyint | 4 | 否 | 调拨单状态10已取消 30待审核 40已审核 42出库单待推送 44出库单推送失败 46待出库 50部分出库 60全部出库 62入库单待推送 64入库单推送失败 66待入库 70部分入库 90调拨完成 |
| 制单人姓名 | creator_name | varchar | 40 | 是 | 调拨单管理的“创建者”字段 |
| 货品数量 | goods_count | decimal | (19,4) | 是 | 货品数量 |
| 货品种类数量 | goods_type_count | decimal | (19,4) | 是 | 调拨单管理界面的“货品种类”字段 |
| 入库数量 | goods_in_count | decimal | (19,4) | 是 | 入库数量 |
| 出库数量 | goods_out_count | decimal | (19,4) | 是 | 出库数量 |
| 最后修改时间 | modified | date | datetime | 是 | 最后修改时间，格式：YYYY-MM-DD HH:MM:SS |
| 创建时间 | created | date | datetime | 是 | 创建时间，格式：YYYY-MM-DD HH:MM:SS |
| 备注 | remark | varchar | 255 | 是 | 备注 |
| sku详情节点 | details_list | Data[] |  | 是 | sku详情节点 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 调拨主键id | transfer_id | int | 11 | 是 | 调拨主键id |
| 调拨明细主键id | rec_id | int | 11 | 是 | 调拨明细主键id |
| 货品编号 | goods_no | varchar | 40 | 是 | 代表SPU所有属性的唯一编号，用于系统货品的区分，SPU概念介绍，单击这里 |
| 商家编码（新） | spec_no | varchar | 40 | 是 | 代表所单品（sku）所有属性的唯一编码，用于获取系统单品的数据，SKU概念介绍，单击这里 |
| 规格码 | spec_code | varchar | 40 | 是 | 规格码 |
| 规格名称 | spec_name | varchar | 100 | 是 | 规格名称 |
| 单位 | unit | smallint | 6 | 是 | 单位 |
| 条码 | barcode | varchar | 40 | 是 | 条码 |
| 调出总成本 | out_cost_total | decimal | (19,4) | 是 | 调出总成本 |
| 批次号 | batch_no | varchar | 40 | 是 | 货品批次 |
| 调出货位 | from_position | varchar | 20 | 是 | 源货位 |
| 调入货位 | to_position | varchar | 20 | 是 | 目标货位 |
| 有效期 | expire_date | date | datetime | 是 | 有效期 |
| 库存 | stock_num | decimal | (19,4) | 是 | 调拨时的库存(显示用,不做依据) |
| 调拨数量 | num | decimal | (19,4) | 是 | 调拨数量 |
| 入库数量 | goods_in_count | decimal | (19,4) | 是 | 入库数量 |
| 出库数量 | goods_out_count | decimal | (19,4) | 是 | 出库数量 |
| 备注 | remark | varchar | 255 | 是 | 备注 |


#### 响应示例

### JSON

```text
{
    "code": 2830,
    "message": "参数值无效status"
}
```


### vip_wms_stockinout_order_push_Y：创建委外出入库单

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `vip_wms_stockinout_order_push_Y` |
| PHP 文件 | `vip_wms_stockinout_order_push.php` |
| 文档标题 | 创建委外出入库单 |
| 描述 | 将要推送至WMS等第三方系统的委外出入库单创建到ERP |
| 客户端路径 | 仓储→委外出入库单管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_wms_stockinout_order_push_Y |

#### 接口说明

| 1.1 接口描述：向旺店通推送委外出入库单据 |
| --- |
| 1.2 适用版本： |
| 1.3注意事项： |


#### 调用场景

| 2.1 举例说明：自有商城接入ERP、金蝶接入、用友接入、SAP接入等 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/vip_wms_stockinout_order_push.php |
| 正式环境 | https://openapi.huice.com/openapi/vip_wms_stockinout_order_push.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/vip_wms_stockinout_order_push.php';<br><br>	$c->putApiParam('api_outer_no', 'wms_20260413002');<br>	$c->putApiParam('warehouse_id', '38');<br>	$c->putApiParam('stock_order_type', 1);<br>	$c->putApiParam('logistics_no', 'ZT20260413002');<br>	$c->putApiParam('logistics_name', '中通快递1');<br><br>	$goods_list = array(<br>		array(<br>			'sku_no' => '20251010-0085',<br>			'num' => 14,<br>			'remark' => '测试货品',<br>			'price' => 111<br>		)<br>	);<br><br>	$c->putApiParam('goods_list', json_encode($goods_list, JSON_UNESCAPED_UNICODE));<br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 客户端汉字字段名，无对应字段缩略写，详细在描述写 | 请求的参数字段 | 字段类型 | 建议长度，查询接口可适当放大，创建接口务必准确 | 填写是或否 | 请求参数说明示例值或者格式、具体含义、使用方法及注意事项 |
| 接口外部单号 | api_outer_no | varchar | 40 | 是 | 调用本接口时推送的唯一单据编号，避免重复推送数据 |
| 仓库id | warehouse_id | varchar | 40 | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 出入库类型 | stock_order_type | tinyint | 1 | 是 | 可选值：1(入库)；2（出库） |
| 物流单号 | logistics_no | varchar | 20 | 否 | 代表物流所有属性的唯一编码，用于物流区分，ERP内支持自定义（ERP物流界面设置） |
| 收件人姓名 | receiver_name | varchar | 40 | 否 | 收件人姓名 |
| 省 | province | varchar | 50 | 否 | 省份名称，直辖市注意输入值为“北京”不是“北京市”，“北京市”在city参数内输入 |
| 市 | city | varchar | 50 | 否 | 市名称 |
| 县(区) | district | varchar | 50 | 否 | 区县名称 |
| 详细地址 | address | varchar | 255 | 否 | 地址详情描述 ，例如 xx街道XX小区xx号楼xx单元401 |
| 手机号 | receiver_mobile | varchar | 40 | 否 | 手机号码 |
| 备注 | remark | varchar | 40 | 否 | 委外其他出入库单据备注 |
| 货品明细节点 | goods_list | data[ ] |  | 是 | 委外出入库单货品列表节点 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 委外出入库单号 | outsource_no | varchar | 40 | 是 | 委外出入库单号 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | sku_no | varchar | 40 | 是 | ERP内单品唯一编码（SKU），代表单品(SKU)所有属性，并且为库存量出入计算最小单元。SKU概念介绍,单击这里注：推送的spec_no值在ERP货品档案必须存在，否则单据会创建失败。 |
| 出入库数量 | num | decimal | (19,4) | 是 | 出入库数量 |
| 价格 | price | decimal | (19,4) | 是 | 价格，默认为0 |
| 批次号 | batch_no | varchar | 20 | 否 | 指定批次号 |
| 备注 | remark | varchar | 255 | 否 | 货品明细备注 |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "outsource_no": "WK2604130002"
}
```

### JSON

```text
{
    "code": 21000006,
    "message": "外部单号重复，请保证外部单号[api_outer_no]的唯一性"
}
```


### stock_goods_sn_query_Y：序列号管理查询接口

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_goods_sn_query_Y` |
| PHP 文件 | `stock_goods_sn_query.php` |
| 文档标题 | 序列号管理查询接口 |
| 描述 | 获取旺店通ERP各种业务类型的SN出入库明细 |
| 客户端路径 | 仓储→序列号管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_goods_sn_query_Y |

#### 接口说明

| 1.1 接口描述：获取序列号管理界面上的序列号信息 |
| --- |
| 1.2 适用版本： |
| 1.3增量获取：按照序列号的最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |
| 1.5注意事项：如传序列号和商家编码时可以不传时间参数 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_goods_sn_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_goods_sn_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 入库类型 | inout_type_text | varchar | 40 | 是 | 入库类型 |
| 入库单编号 | stock_inout_no | varchar | 40 | 是 | 入库单编 |
| 源单号 | src_order_no | varchar | 40 | 是 | 入库单源单号 |
| 入库单状态 | consign_status | int | 10 | 是 | 入库单状态 |
| 操作人 | operator_name | varchar | 40 | 是 | 操作人 |
| 出入库时间 | create_date | datetime |  | 是 | 出入库时间 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 出库类型 | inout_type_text | varchar | 40 | 是 | 出库类型 |
| 出库单编号 | stock_inout_no | varchar | 40 | 是 | 出库单编 |
| 源单号 | src_order_no | varchar | 40 | 是 | 出库单源单号 |
| 出库单状态 | consign_status | int | 10 | 是 | 出库单状态 |
| 操作人 | operator_name | varchar | 40 | 是 | 操作人 |
| 出入库时间 | create_date | datetime |  | 是 | 出入库时间 |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"total_count": 1,<br>	"goods_list": [{<br>		"id": "2767076881390895129",<br>		"sn": "2767076881390895129",<br>		"secondSn": "",<br>		"skuNo": null,<br>		"skuCode": null,<br>		"spuNo": null,<br>		"spuName": null,<br>		"skuName": null,<br>		"warehouseId": "127",<br>		"warehouseName": "小哈电池售卖仓",<br>		"status": 30,<br>		"statusText": "已出库",<br>		"snNumber": "",<br>		"skuId": "99999",<br>		"modifyDate": "2025-11-27T16:15:43",<br>		"createDate": "2025-11-27T16:15:38",<br>		"stockInList": [],<br>		"stockOutList": [{<br>			"stockInoutOrderId": "2767076538858864665",<br>			"stockInoutNo": "JY2511274071",<br>			"inoutType": -1,<br>			"inoutTypeText": "销售订单",<br>			"srcOrderNo": null,<br>			"operatorId": 3947,<br>			"operatorName": "xh001-test",<br>			"createDate": "2025-11-27T16:15:38",<br>			"consignStatus": 95,<br>			"snId": "2767076881390895129"<br>		}]<br>	}]<br>} |
| --- | --- |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 序列号 | sn | String | 20 | 否 | 序列号 |
| 商家编码 | spec_no | String | 40 | 否 | 商家编码 |
| 序列号状态 | status | int | 11 | 否 | 序列号状态：5未启用,10待入库,15已入库,20已占用,30已出库 |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量获取数据，start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量获取数据，end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为40，使用举例单击这里 |
| 页号 | page_no | int |  | 否 | 页号默认从0开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int |  | 是 | 错误码，0成功 |
| 错误描述 | message | varchar |  | 是 | 错误描述 |
| 数据总条数 | total_count | int |  | 是 | 符合条件的数据总条数，当page_no=0时返回，用来分页 |
| 序列号节点 | goods_list | data[] |  | 是 | 响应参数的1级数据节点，包含序列号数据节点,节点下数据字段详见下述“stockout_list”," stockin_list" |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 序列号唯一码 | id | int | 11 | 是 | 序列号唯一码 |
| 序列号 | sn | varchar | 40 | 是 | 序列号 |
| 辅助序列号 | second_sn | varchar | 40 | 是 | 辅助序列号 |
| 创建编号 | sn_number | varchar | 40 |  |  |
| 仓库id | warehouse_id | int | 10 | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库名称 | warehouse_name | varchar | 40 | 是 | 仓库名称 |
| 序列号状态 | status | int | 11 | 是 | 序列号状态：5未启用,10待入库,15已入库,20已占用,30已出库 |
| 货品编码 | spu_no | varchar | 40 | 是 | 货品编码 |
| 货品名称 | spu_name | varchar | 40 | 是 | 货品名称 |
| 商家编码 | sku_no | varchar | 40 | 是 | 商家编码 |
| 规格码 | sku_code | varchar | 40 | 是 | 规格码 |
| 规格名称 | sku_name | varchar | 40 | 是 | 规格名称 |
| 序列号创建时间 | create_date | datetime |  | 是 | 序列号创建时间，格式：yyyy-MM-dd HH:mm:ss |
| 序列号最后更新时间 | modify_date | datetime |  | 是 | 序列号最后更新时间，格式：yyyy-MM-dd HH:mm:ss |
| 入库单据明细节点 | stockin_list | data[] |  | 是 | 入库单据明细节点，字段详细见stockin_list表 |
| 出库单据明细节点 | stockout_list | data[] |  | 是 | 出库单据明细节点，字段详细见stockout_list表 |


#### 响应示例

### JSON

```text
{
	"code": 2180,
	"message": "start_time与end_time时间跨度不能超过最大范围30天"
}
```


### stock_production_order_query_Y：查询生产加工单接口

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_production_order_query_Y` |
| PHP 文件 | `stock_production_order_query.php` |
| 文档标题 | 查询生产加工单接口 |
| 描述 | 获取旺店通ERP生产加工单数据 |
| 客户端路径 | 仓储→生产加工 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_production_order_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP生产加工单数据 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3增量获取：按照单据最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_production_order_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_production_order_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 生产加工单号 | production_no | String | 40 | 否 | 生产加工单号，传该字段可以不传时间范围 |
| 状态 | status | int | 11 | 否 | 状态5：已作废10：已取消20：待审核32：出库待推送34：出库推送失败38：委外待领料"40：待领料"45：领料中"50：生产中"52：入库单待推送"54：入库单推送失败"57：委外待入库"60：部分入库"100：已生产" |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量获取数据，start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量获取数据，end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为40，使用举例单击这里 |
| 页号 | page_no | int |  | 否 | 页号默认从0开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int |  | 是 | 错误码，0成功 |
| 错误描述 | message | varchar |  | 是 | 错误描述 |
| 数据总条数 | total_count | int |  | 是 | 符合条件的数据总条数，当page_no=0时返回，用来分页 |
| 生产加工单列表 | data | data[] |  | 是 | 响应参数的1级数据节点，包含生产加工单列表 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 13,<br>    "data": [<br>        {<br>            "id": "2772145811436339220",<br>            "production_no": "SC2512110004",<br>            "stockout_warehouse_id": "5",<br>            "stockout_warehouse_name": "hazs01",<br>            "stockin_warehouse_id": "19",<br>            "stockin_warehouse_name": "xx的仓库",<br>            "production_type": 2,<br>            "production_mode": 1,<br>            "status": 50,<br>            "status_text": "生产中",<br>            "production_amount": "10.0000",<br>            "parent_num": "9.0000",<br>            "parent_already_num": "0.0000",<br>            "parent_not_num": "9.0000",<br>            "children_num": "9.0000",<br>            "children_already_num": "9.0000",<br>            "children_not_num": "0.0000",<br>            "produceman_id": 3621,<br>            "produceman_name": "guijun",<br>            "material_by": "",<br>            "material_by_name": "",<br>            "remark": "大备注",<br>            "print_status": 1,<br>            "print_status_text": "未打印",<br>            "outer_out_no": "",<br>            "outer_in_no": "",<br>            "error_info": "",<br>            "create_date": "2025-12-11T15:57:45",<br>            "production_times": 3,<br>            "modify_date": "2025-12-11T15:58:00",<br>            "target_sku_list": [<br>                {<br>                    "prop1": null,<br>                    "prop2": null,<br>                    "prop3": null,<br>                    "prop4": null,<br>                    "prop5": null,<br>                    "prop6": null,<br>                    "prop7": null,<br>                    "prop8": null,<br>                    "prop9": null,<br>                    "prop10": null,<br>                    "sku_id": "2768547700164001813",<br>                    "warehouse_id": null,<br>                    "sku_sort_name": null,<br>                    "sku_no": "9011",<br>                    "sku_name": "Large",<br>                    "sku_short_name": "",<br>                    "barcode": "251201203",<br>                    "spu_id": "2768547700138835989",<br>                    "spu_name": "家用杂物收纳盒大容量带盖透明桌面整理盒家居维修工具五金工具储物箱",<br>                    "spu_short_name": "",<br>                    "spu_no": "9011",<br>                    "spu_modify_date": "2025-12-11T10:22:24",<br>                    "plat_spu_no": "9011",<br>                    "plat_sku_no": "9011",<br>                    "image_url": "https://img.kwcdn.com/product/fancy/bc7c2a66-dad9-4532-809a-ade3ce8f9616.jpg",<br>                    "spu_img_url": "https://img.kwcdn.com/product/fancy/bc7c2a66-dad9-4532-809a-ade3ce8f9616.jpg",<br>                    "outer_sku_no": null,<br>                    "ref_cost_price": "0.0000",<br>                    "price": "0.0000",<br>                    "retail_price": "0.0000",<br>                    "wholesale_price": "0.0000",<br>                    "validity_days": null,<br>                    "unit_id": "0",<br>                    "unit_name": "",<br>                    "weight": "0.7240",<br>                    "box_sku_num": 0,<br>                    "sku_remark": null,<br>                    "sku_delete_flag": false,<br>                    "brand_id": "2713730725894423568",<br>                    "brand_name": "娃哈哈",<br>                    "goods_category_id": "0",<br>                    "approval_number": null,<br>                    "stock_num": null,<br>                    "quality_num": null,<br>                    "defect_num": null,<br>                    "default_position_name": null,<br>                    "location_name": null,<br>                    "location_id": null,<br>                    "stock_type": 0,<br>                    "stock_type_text": null,<br>                    "batch_id": null,<br>                    "batch_no": "",<br>                    "production_date": null,<br>                    "expire_date": null,<br>                    "id": "2772145811444729876",<br>                    "stock_production_id": "2772145811436339220",<br>                    "source_type": 2,<br>                    "num": "2.0000",<br>                    "total_num": "6.0000",<br>                    "real_num": "0.0000",<br>                    "match_num": "0.0000",<br>                    "cost_rate": "30.0000",<br>                    "remark": ""<br>                },<br>                {<br>                    "prop1": null,<br>                    "prop2": null,<br>                    "prop3": null,<br>                    "prop4": null,<br>                    "prop5": null,<br>                    "prop6": null,<br>                    "prop7": null,<br>                    "prop8": null,<br>                    "prop9": null,<br>                    "prop10": null,<br>                    "sku_id": "2769594574882996228",<br>                    "warehouse_id": null,<br>                    "sku_sort_name": null,<br>                    "sku_no": "源单号",<br>                    "sku_name": "",<br>                    "sku_short_name": "",<br>                    "barcode": "251204101",<br>                    "spu_id": "2769594574576812036",<br>                    "spu_name": "源单号",<br>                    "spu_short_name": "源单号",<br>                    "spu_no": "源单号",<br>                    "spu_modify_date": "2025-12-11T10:21:32",<br>                    "plat_spu_no": "",<br>                    "plat_sku_no": "",<br>                    "image_url": "https://img0.baidu.com/it/u=1119010193,3065907151&fm=253&fmt=auto&app=138&f=JPEG?w=171&h=190",<br>                    "spu_img_url": "https://img0.baidu.com/it/u=1119010193,3065907151&fm=253&fmt=auto&app=138&f=JPEG?w=171&h=190",<br>                    "outer_sku_no": null,<br>                    "ref_cost_price": "23.0000",<br>                    "price": "0.0000",<br>                    "retail_price": "0.0000",<br>                    "wholesale_price": "0.0000",<br>                    "validity_days": null,<br>                    "unit_id": "0",<br>                    "unit_name": "",<br>                    "weight": "0.0000",<br>                    "box_sku_num": 0,<br>                    "sku_remark": null,<br>                    "sku_delete_flag": false,<br>                    "brand_id": "2771698899490964486",<br>                    "brand_name": "42311234",<br>                    "goods_category_id": "0",<br>                    "approval_number": null,<br>                    "stock_num": null,<br>                    "quality_num": null,<br>                    "defect_num": null,<br>                    "default_position_name": null,<br>                    "location_name": null,<br>                    "location_id": null,<br>                    "stock_type": 0,<br>                    "stock_type_text": null,<br>                    "batch_id": null,<br>                    "batch_no": "",<br>                    "production_date": null,<br>                    "expire_date": null,<br>                    "id": "2772145811444730900",<br>                    "stock_production_id": "2772145811436339220",<br>                    "source_type": 2,<br>                    "num": "1.0000",<br>                    "total_num": "3.0000",<br>                    "real_num": "0.0000",<br>                    "match_num": "0.0000",<br>                    "cost_rate": "70.0000",<br>                    "remark": ""<br>                }<br>            ],<br>            "source_sku_list": [<br>                {<br>                    "prop1": null,<br>                    "prop2": null,<br>                    "prop3": null,<br>                    "prop4": null,<br>                    "prop5": null,<br>                    "prop6": null,<br>                    "prop7": null,<br>                    "prop8": null,<br>                    "prop9": null,<br>                    "prop10": null,<br>                    "sku_id": "2705127425343225892",<br>                    "warehouse_id": null,<br>                    "sku_sort_name": null,<br>                    "sku_no": "看看移位",<br>                    "sku_name": "看看移位",<br>                    "sku_short_name": "看看移位",<br>                    "barcode": "kk1",<br>                    "spu_id": "2705127425078984740",<br>                    "spu_name": "看看移位",<br>                    "spu_short_name": "看看移位",<br>                    "spu_no": "看看移位",<br>                    "spu_modify_date": "2025-10-23T16:58:23",<br>                    "plat_spu_no": "",<br>                    "plat_sku_no": "",<br>                    "image_url": "https://erpx-prod.oss-cn-zhangjiakou.aliyuncs.com/goods/2e03034d-2f73-4823-b219-5f6cfc506cb2/chen_176bebec5dea42feb81d2a7d457870da.jpeg",<br>                    "spu_img_url": "https://erpx-prod.oss-cn-zhangjiakou.aliyuncs.com/goods/2e03034d-2f73-4823-b219-5f6cfc506cb2/chen_176bebec5dea42feb81d2a7d457870da.jpeg",<br>                    "outer_sku_no": null,<br>                    "ref_cost_price": "30.0000",<br>                    "price": "0.0000",<br>                    "retail_price": "0.0000",<br>                    "wholesale_price": "0.0000",<br>                    "validity_days": null,<br>                    "unit_id": "2503594148196515843",<br>                    "unit_name": "个",<br>                    "weight": "10.0000",<br>                    "box_sku_num": 3,<br>                    "sku_remark": null,<br>                    "sku_delete_flag": false,<br>                    "brand_id": "0",<br>                    "brand_name": "",<br>                    "goods_category_id": "0",<br>                    "approval_number": null,<br>                    "stock_num": null,<br>                    "quality_num": null,<br>                    "defect_num": null,<br>                    "default_position_name": null,<br>                    "location_name": null,<br>                    "location_id": null,<br>                    "stock_type": 0,<br>                    "stock_type_text": null,<br>                    "batch_id": null,<br>                    "batch_no": "",<br>                    "production_date": null,<br>                    "expire_date": null,<br>                    "id": "2772145811444727828",<br>                    "stock_production_id": "2772145811436339220",<br>                    "source_type": 1,<br>                    "num": "2.0000",<br>                    "total_num": "6.0000",<br>                    "real_num": "6.0000",<br>                    "match_num": "0.0000",<br>                    "cost_rate": "0.0000",<br>                    "remark": ""<br>                },<br>                {<br>                    "prop1": null,<br>                    "prop2": null,<br>                    "prop3": null,<br>                    "prop4": null,<br>                    "prop5": null,<br>                    "prop6": null,<br>                    "prop7": null,<br>                    "prop8": null,<br>                    "prop9": null,<br>                    "prop10": null,<br>                    "sku_id": "2698966609925505031",<br>                    "warehouse_id": null,<br>                    "sku_sort_name": null,<br>                    "sku_no": "看看占用",<br>                    "sku_name": "看看占用",<br>                    "sku_short_name": "看看占用",<br>                    "barcode": "kk2",<br>                    "spu_id": "2698966609833230343",<br>                    "spu_name": "看看占用",<br>                    "spu_short_name": "看看占用",<br>                    "spu_no": "看看占用",<br>                    "spu_modify_date": "2025-08-13T15:29:10",<br>                    "plat_spu_no": "",<br>                    "plat_sku_no": "",<br>                    "image_url": "https://erpx-prod.oss-cn-zhangjiakou.aliyuncs.com/goods/8aacc900-04c6-4ee9-b013-0788eac782cd/chen_ff488239ea8a43119e8f0ed6eb3e427f.jpeg",<br>                    "spu_img_url": "https://erpx-prod.oss-cn-zhangjiakou.aliyuncs.com/goods/8aacc900-04c6-4ee9-b013-0788eac782cd/chen_ff488239ea8a43119e8f0ed6eb3e427f.jpeg",<br>                    "outer_sku_no": null,<br>                    "ref_cost_price": "20.0000",<br>                    "price": "0.0000",<br>                    "retail_price": "0.0000",<br>                    "wholesale_price": "0.0000",<br>                    "validity_days": null,<br>                    "unit_id": "2503594148225875971",<br>                    "unit_name": "瓶",<br>                    "weight": "1.6999",<br>                    "box_sku_num": 5,<br>                    "sku_remark": null,<br>                    "sku_delete_flag": false,<br>                    "brand_id": "0",<br>                    "brand_name": "",<br>                    "goods_category_id": "0",<br>                    "approval_number": null,<br>                    "stock_num": null,<br>                    "quality_num": null,<br>                    "defect_num": null,<br>                    "default_position_name": null,<br>                    "location_name": null,<br>                    "location_id": null,<br>                    "stock_type": 0,<br>                    "stock_type_text": null,<br>                    "batch_id": null,<br>                    "batch_no": "",<br>                    "production_date": null,<br>                    "expire_date": null,<br>                    "id": "2772145811444728852",<br>                    "stock_production_id": "2772145811436339220",<br>                    "source_type": 1,<br>                    "num": "1.0000",<br>                    "total_num": "3.0000",<br>                    "real_num": "3.0000",<br>                    "match_num": "0.0000",<br>                    "cost_rate": "0.0000",<br>                    "remark": ""<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 生产加工单号 | production_no | string |  | 是 | 生产加工单号 |
| 生产入库仓id | stockin_warehouse_id | bigint | 20 | 是 | 生产入库仓id |
| 入库仓库名称 | stockin_warehouse_name | string |  | 是 | 入库仓库名称 |
| 生产出库仓id | stockout_warehouse_id | bigint | 20 |  | 生产出库仓id |
| 出库仓库名称 | stockout_warehouse_name | string |  | 是 | 出库仓库名称 |
| 生产入库仓编号 | stockin_warehouse_no | varchar | 40 | 是 | 生产入库仓编号 |
| 生产出库仓编号 | stockout_warehouse_no | varchar | 40 | 是 | 生产出库仓编号 |
| 生产方式 | production_type | int |  | 是 | 生产方式 |
| 生产类型 | production_mode | bigint | 20 | 是 | 生产类型 |
| 状态 | status | int |  | 是 | 状态 |
| 加工费用 | processing_fee | decimal |  | 是 | 加工费用 |
| 状态文案 | status_text | string | 40 | 是 | 状态文案 |
| 消耗品数 | children_num | decimal |  | 是 | 消耗品数 |
| 消耗品已出库数量 | children_already_num | decimal |  | 是 | 消耗品已出库数量 |
| 消耗品未出库数量 | children_not_num | decimal |  |  | 消耗品未出库数量 |
| 生产品已入库数量 | parent_already_num | decimal |  | 是 | 生产品已入库数量 |
| 生产品未入库数量 | parent_not_num | decimal |  | 是 | 生产品未入库数量 |
| 生产员 | produceman_name | string |  | 是 | 生产员 |
| 领料人 | material_by_name | string |  | 是 | 领料人 |
| 备注 | remark | string |  | 是 | 备注 |
| 打印状态 | print_status_text | string |  | 是 | 打印状态 |
| 推送出库单号 | outer_out_no | string |  | 是 | 推送出库单号 |
| 推送入库单号 | outer_in_no | string |  | 是 | 推送入库单号 |
| 推送失败信息 | error_info | string |  | 是 | 推送失败信息 |
| 制单时间 | create_date | datetime |  | 是 | 制单时间 |
| 生产次数 | production_times | int |  | 是 | 生产次数 |
| 最后修改时间 | modify_date | datetime |  | 是 | 最后修改时间 |
| 生产品数量 | parent_num | decimal |  | 是 | 生产品数量 |
| 生产品列表 | target_sku_list | data[] |  | 是 | 生产品明细节点，字段详细见target_sku_list表 |
| 消耗品列表 | source_sku_list | data[] |  | 是 | 消耗品明细节点，字段详细见source_sku_list表 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码（新） | sku_no | varchar |  | 是 | 商家编码（新） |
| 规格名称 | sku_name | varchar |  | 是 | 规格名称 |
| 货品名称 | spu_name | varchar |  | 是 | 货品名称 |
| 批次 | batch_no | varchar |  | 是 | 批次 |
| 生产日期 | production_date | datetime |  | 是 | 生产日期 |
| 保质期 | validity_days | int | 11 | 是 | 保质期 |
| 有效期 | expire_date | datetime |  | 是 | 有效期 |
| 数量 | num | decimal |  | 是 | 数量 |
| 总数量 | total_num | decimal |  | 是 | 总数量 |
| 已入库数量 | real_num | decimal |  | 是 | 出入库时间 |
| 匹配数量 | match_num | decimal |  | 是 | 匹配数量 |
| 成本比例 | cost_rate | decimal |  | 是 | 成本比例 |
| 备注 | remark | varchar |  | 是 | 备注 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码（新） | sku_no | varchar |  | 是 | 商家编码（新） |
| 规格名称 | sku_name | varchar |  | 是 | 规格名称 |
| 货品名称 | spu_name | varchar |  | 是 | 货品名称 |
| 批次 | batch_no | varchar |  | 是 | 批次 |
| 生产日期 | production_date | datetime |  | 是 | 生产日期 |
| 保质期 | validity_days | int | 11 | 是 | 保质期 |
| 有效期 | expire_date | datetime |  | 是 | 有效期 |
| 数量 | num | decimal |  | 是 | 数量 |
| 总数量 | total_num | decimal |  | 是 | 总数量 |
| 已出库数量 | real_num | decimal |  | 是 | 已出库数量 |
| 备注 | remark | varchar |  | 是 | 备注 |


#### 响应示例

### JSON

```text
{
	"code": 2180,
	"message": "start_time与end_time时间跨度不能超过最大范围30天"
}
```


### stock_full_query_Y：全量查询库存

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_full_query_Y` |
| PHP 文件 | `stock_full_query.php` |
| 文档标题 | 全量库存查询 |
| 描述 | 全量获取系统库存管理数据 |
| 客户端路径 | 仓储→库存查询 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_full_query_Y |

#### 调用场景

| 2.1 举例说明： SAP、线下ERP、SRM、SCM等系统对接 |
| --- |


#### 请求地址

| 1.1 接口描述：全量获取旺店通ERP实际库存、库存占用等数据。 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取：按照最库存管理数据最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。如不传时间按照全量查询 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |
| 1.5 注意事项：①测试环境不限制调用时间，仓库编号必传；正式环境只允许凌晨00:00-02:00调用，其余时间调用会报错。③接口返回的“库存量”字段值是仓库中的实物库存量，“可发库存量”可理解为可销售库存量或未被占用库存量，可发库存计算方式，需要对照系统设置中的可发库存计算公式。 |

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_full_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_full_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once ('../WdtClient.php');<br>    $c = new WdtClient();<br>     $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    $c->gatewayUrl =  'https://openapi.ali.huice.cc/openapi/stock_full_query.php';<br><br>  //  $c->putApiParam('start_time', '2026-01-01 00:00:00');<br>    //$c->putApiParam('end_time', '2026-01-30 23:59:59');<br>    $c->putApiParam('page_no', '0');<br>    $c->putApiParam('page_size', '100');<br>    $c->putApiParam('warehouse_id', '3');<br>   // $c->putApiParam('spec_no', '');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 否 | 按最后修改时间增量获取数据,start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss  如不传时间按照全量查询 |
| 结束时间 | end_time | datetime |  | 否 | 按最后修改时间增量获取数据,start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss  如不传时间按照全量查 |
| 分页大小 | page_size | int |  | 否 | 每页返回条数，不传默认40 |
| 页号 | page_no | int |  | 否 | 不传值默认从0页开始 |
| 仓库id | warehouse_id | varchar |  | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar |  | 否 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 商家编码 | spec_no | varchar |  | 否 | 代表单品(sku)所有属性的编码 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 库存数据列表 | stocks | data[] |  | 是 | 响应参数的1级数据节点，包含库存详细数据列表，节点下数据字段详见下述" stocks" |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"total_count": 1,<br>	"stocks": [{<br>		"barcode": "",<br>		"remark": "",<br>		"unit": "箱",<br>		"spec_id": "2605414821121753106",<br>		"warehouse_id": "3",<br>		"rec_id": "2702899664289529881",<br>		"goods_no": "0313",<br>		"brand_name": null,<br>		"brand_no": "0",<br>		"goods_name": "【黄桃界爱马仕】丹东黄金蜜桃5斤脆甜多汁新鲜黄油桃水果产地直发",<br>		"spec_no": "4.05.003",<br>		"spec_name": "5斤\/箱",<br>		"spec_code": "",<br>		"stock_num": "0",<br>		"available_num": "0",<br>		"cost_price": "0",<br>		"virtual_num": "0",<br>		"avg_cost_price": "0",<br>		"created": "2025-06-03 13:58:17",<br>		"modified": "2026-01-15 01:08:47",<br>		"defect": 0<br>	}]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单品主键id | spec_id | bigint(20) |  | 是 | 单品主键id |
| 仓库id | warehouse_id | int(11) |  | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar |  | 是 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 库存主键id | rec_id | bigint(20) |  | 是 | 库存明细主键id |
| 货品编号 | goods_no | varchar |  | 是 | 货品编号 |
| 品牌编号 | brand_no | varchar |  | 是 | 品牌编号 |
| 品牌名称 | brand_name | varchar |  | 是 | 品牌名称 |
| 货品名称 | goods_name | varchar |  | 是 | 货品名称 |
| 商家编码 | spec_no | varchar |  | 是 | 商家编码 |
| 规格名称 | spec_name | varchar |  | 是 | 规格名称 |
| 规格码 | spec_code | varchar |  | 是 | 规格码 |
| 条形码 | barcode | varchar |  | 是 | 条形码 |
| 库存量 | stock_num | decimal(21, 6) |  | 是 | 库存量 |
| 可用库存 | available_num | decimal(21, 6) |  | 是 | 可用库存 |
| 单位 | unit | varchar |  | 是 | 单位 |
| 备注 | remark | varchar |  | 是 | 备注 |
| 成本价 | cost_price | decimal(21, 6) |  | 是 | 商品档案的固定成本价 |
| 虚拟库存 | virtual_num | decimal(21, 6) |  | 是 | 虚拟库存 |
| 是否残次品 | defect | tinyint(4) |  | 是 | 0否 1是 |
| 创建时间 | created | datetime |  | 是 | 创建时间 |
| 最后修改时间 | modified | datetime |  | 是 | 最后修改时间 |
| 平均成本价 | avg_cost_price | decimal(21, 6) |  | 是 | 库存查询-成本价字段 |


#### 响应示例

### JSON

```text
{
	"code": 2180,
	"message": "xxxxxxxx"
}
```


### stock_transfer_create_Y：创建调拨单

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_transfer_create_Y` |
| PHP 文件 | `stock_transfer_create.php` |
| 文档标题 | 创建调拨单 |
| 描述 | ERP内仓与仓之间的库存需要调度时，推送调拨单给ERP |
| 客户端路径 | 仓储→调拨管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_transfer_create_Y |

#### 接口说明

| 1.1 接口描述：旺店通ERP内仓与仓之间的库存需要调度时，推送调拨单给旺店通ERP。 |
| --- |
| 1.2 适用版本：260303及之后的版本 |
| 1.3注意事项： |


#### 调用场景

| 2.1 举例说明：线下ERP、自研存货管理等系统对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_transfer_create.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_transfer_create.php |

| PHP | <?php<br>        require_once('../WdtClient.php');<br>    $c = new WdtClient;<br>        $c->sid ='haijun';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    //测试环境地址<br>    //上线时需要换成线上的<br>        $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stock_transfer_create.php'; // 测试的<br>        //$c->gatewayUrl = 'https://openapi.huice.com/openapi/stockin_order_push.php'; //正式的<br>    $spec_item = new stdClass();<br>    $spec_item->sku_no = "951027";<br>    $spec_item->num = "1";<br>    $skus = [$spec_item];<br><br>    $c->putApiParam('outer_no', 'zd2026030300201TF');<br>    $c->putApiParam('from_warehouse_no', '240');<br>    $c->putApiParam('to_warehouse_no', "130");<br>    $c->putApiParam('transfer_type', 1);<br>       $c->putApiParam('audit_flag', "true");<br>    $c->putApiParam("skus", json_encode($skus, JSON_UNESCAPED_UNICODE));<br><br>    $json = $c->wdtOpenApi();<br>    $array = json_decode($json, true); // 转成数组<br>    echo json_encode($array, JSON_UNESCAPED_UNICODE); // 输出中文正常显示<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 接口外部单号 | outer_no | varchar | 40 | 是 | 调用本接口时推送的唯一单据编号，避免重复推送数据 |
| 调出仓库ID | from_warehouse_no | varchar | 40 | 是 | 货品被调出的仓库编号 |
| 调入仓库ID | to_warehouse_no | varchar | 40 | 是 | 货品被调入的仓库编号 |
| 调拨类型 | transfer_type | tinyint | 4 | 否 | 1：快速调拨；2：分步调拨。默认是1 |
| 是否审核 | audit_flag | varchar | 40 | 否 | "true"：审核；"false"：不审核。默认为"false |
| 联系人姓名 | contact | varchar | 40 | 否 | 联系人姓名 |
| 联系电话 | telno | varchar | 40 | 否 | 联系电话 |
| 详细地址 | address | varchar | 255 | 否 | 详细地址 |
| 备注 | remark | varchar | 255 | 否 | 单据备注 |
| 货品明细节点 | skus | data[ ] |  | 是 | 调拨单货品列表节点 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | sku_no | varchar | 40 | 是 | ERP内单品唯一编码（SKU），代表单品(SKU)所有属性，并且为库存量出入计算最小单元。SKU概念介绍,单击这里注：推送的spec_no值在ERP货品档案必须存在，否则单据会创建失败。 |
| 调拨数量 | num | decimal | (19,4) | 是 | 调拨数量 |
| 调出货位 | from_position_no | decimal | (19,4) | 否 | 调出货位 （开启货位管理配置时启用，可进行货位调拨） |
| 调入货位 | to_position_no | varchar | 20 | 否 | 调出货位 （开启货位管理配置时启用，可进行货位调拨） |
| 备注 | remark | varchar | 255 | 否 | 货品明细备注 |


#### 响应示例

### JSON

```text
{
	"code": 0,
	"message": "",
	"transfer_no": "DB2603030002"
}
```

### JSON

```text
{
    "code":21000003,
    "message":"必要参数缺失：src_order_type"
}
```


### stock_outsource_order_query_Y：查询委外出入库单

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `stock_outsource_order_query_Y` |
| PHP 文件 | `stock_outsource_order_query.php` |
| 文档标题 | 查询委外出入库单 |
| 描述 | 查询erp委外出库单、入库单数据 |
| 客户端路径 | 仓储-委外出入库单界面 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_outsource_order_query_Y |

#### 接口说明

| 1.1 接口描述：获取委外出入库单及货品明细数据 |
| --- |
| 1.2 适用版本：网页版，20260312后迭代版本 |
| 1.3 增量获取：按照旺店通委外出入库单的最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stock_outsource_order_query.php |
| 正式环境 | https://openapi.huice.com/openapi/stock_outsource_order_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>  require_once ('../WdtClient.php');<br>  $c = new WdtClient();<br>   $c->sid = '';<br>        $c->appkey = '';<br>        $c->appsecret = '';<br>  $c->gatewayUrl = 'https://openapi.huice.com/openapi/stock_outsource_order_query.php';<br><br>  $c->putApiParam('start_time', '2026-02-01 15:38:55');<br>  $c->putApiParam('end_time', '2026-02-30 15:38:55');<br>  $c->putApiParam('warehouse_id', '1');<br>    $c->putApiParam('page_size', '1');<br>  $c->putApiParam('page_no', '0');<br>  //$c->putApiParam('outsource_no', 'WK2602092373');<br>  $c->putApiParam('order_type', 2);<br>  $json = $c->wdtOpenApi();<br>  var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库id | warehouse_id | varchar | 40 | 否 | 代表仓库所有属性的唯一ID，用于仓库区分 |
| 仓库编码 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编码，用于仓库区分 |
| 单据状态 | status | int | 4 | 否 | order_type=1 时   10 已取消 30待审核 40待推送 50推送失败 65待入库  75部分入库 80 已完成 （该字段需和order_type共同使用）order_type=2 时   10 已取消 30待审核 40待推送 50推送失败 65待出库  75部分出库 80 已完成 （该字段需和order_type共同使用） |
| 出入类别 | order_type | int | 4 | 否 | 可选值：1（入库），2（出库） 不传默认返回所有类型 |
| 推单单号 | push_no | varchar | 40 | 否 | 推单单号 |
| 出入库单号 | outsource_no | varchar | 40 | 否 | 创建委外出入库单成功后系统生产的单号，示例“WK201905280002”，通过“vip_wms_stockinout_order_push.php”创建委外出入库单成功后响应参数会返回此单号，单独查询不校验时间 |
| 委外单号 | order_no | varchar | 40 | 否 | 委外单号，单独查询不校验时间 |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量获取数据,start_time作为开始时间，  格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量获取数据,end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int | 10 | 否 | 每页返回数据条数，参数输入值范围1~100，不传此参数默认page_size=40，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 出库单列表节点 | order_list | data[ ] |  | 否 | 响应参数的1级数据节点，包含当前页的JIT出库单及其明细的数据节点,节点下数据字段详见下述“stockout_list”和" details_list" |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"total_count": "2",<br>	"order_list": [{<br>		"order_no": "WK2508200002",<br>		"push_no": "",<br>		"order_id": "2731203728232153102",<br>		"logistics_no": "",<br>		"warehouse_id": "50",<br>		"status": 50,<br>		"error_info": "存在系统商品未推送至云仓，请先推送云仓货品。商家编码：88471501",<br>		"operator_name": "renmaolin-test",<br>		"warehouse_type": 3,<br>		"logistics_name": "",<br>		"created": "2025-08-20 16:28:32",<br>		"remark": "",<br>		"order_type": 1,<br>		"goods_count": "9965",<br>		"goods_real_count": "0",<br>		"modified": "2025-08-20 16:28:32",<br>		"receiver_name": "",<br>		"shipper_name": "",<br>		"receiver_province": 0,<br>		"receiver_city": 0,<br>		"receiver_district": 0,<br>		"receiver_area": "",<br>		"receiver_address": "",<br>		"receiver_mobile": "",<br>		"detail_list": [{<br>			"order_id": "2731203728232153102",<br>			"rec_id": "2731203728265707534",<br>			"order_no": "WK2508200002",<br>			"goods_id": "2731198803569803278",<br>			"goods_name": "【圳兴乡村帮扶馆】古耕龙脊红糯米 1kg\/袋",<br>			"short_name": "",<br>			"spu_no": "16064",<br>			"spec_no": "88471501",<br>			"spec_name": "无",<br>			"spec_code": "",<br>			"barcode": "",<br>			"unit_id": "0",<br>			"goods_unit": "",<br>			"brand_id": "0",<br>			"brand_name": "",<br>			"batch_no": "",<br>			"expire_date": "",<br>			"validity_days": "",<br>			"num": "9965",<br>			"inout_num": "0",<br>			"price": "0",<br>			"remark": ""<br>		}]<br>	}]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据主键id | order_id | int | 11 | 是 | 单据主键id |
| 委外单号 | order_no | varchar | 40 | 是 | 委外单号，默认WK开头 |
| 外部单号 | api_outer_no | varchar | 40 | 是 | 外部单号，创建委外出入库单接口入参api_outer_no |
| 仓库id | warehouse_id | varchar | 40 | 是 | 代表仓库所有属性的唯一id，用于仓库区分 |
| 仓库编码 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编码，用于仓库区分 |
| 推单单号 | push_no | varchar | 40 | 是 | 推单单号 |
| 出入库单号 | outsource_no | varchar | 40 | 是 | 出入库单号 |
| 单据状态 | status | tinyint | 4 | 是 | 可选值：order_type=2 时   10 已取消 30待审核 40待推送 50推送失败 65待出库  75部分出库 80 已完成 （该字段需和order_type共同使用）order_type=1 时   10 已取消 30待审核 40待推送 50推送失败 65待入库  75部分入库 80 已完成 （该字段需和order_type共同使用） |
| 物流单号 | logistics_no | varchar | 40 | 是 | 物流单号 |
| 失败原因 | error_info | varchar | 255 | 是 | 失败原因 |
| 操作人姓名 | operator_name | varchar | 40 | 是 | 操作人姓名 |
| 仓库类型 | warehouse_type | tinyint | 4 | 是 | 仓库类型  0普通仓库 2分销仓 3委外仓库4自流转仓 |
| 物流公司 | logistics_name | varchar | 40 | 是 | 物流公司 |
| 制单时间 | created | datetime |  | 是 | 制单时间 |
| 备注 | remark | varchar | 255 | 是 | 备注 |
| 出入库类别 | order_type | tinyint | 4 | 是 | 出入库类别 |
| 开单总数量 | goods_count | decimal | (19,4) | 是 | 开单总数量 |
| 已出入库数量 | goods_real_count | decimal | (19,4) | 是 | 已出入库数量 |
| 最后修改时间 | modified | datetime |  | 是 | 最后修改时间 |
| 联系人 | receiver_name | varchar | 40 | 是 | 联系人 |
| 省份 | receiver_province | int | 11 | 是 | 省份 |
| 城市 | receiver_city | int | 11 | 是 | 城市 |
| 区县 | receiver_district | int | 11 | 是 | 区县 |
| 省市区 | receiver_area | varchar | 255 | 是 | 省市区 |
| 详细地址 | receiver_address | varchar | 255 | 是 | 详细地址 |
| 电话 | receiver_mobile | varchar | 40 | 是 | 电话 |
| 货品列表节点 | detail_list | data[ ] |  | 是 | 响应参数的2级数据节点，包含单个入库单所有货品属性信息的数据节点，节点下数据字段详见下述“detail_list”列表 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据主键id | order_id | int | 11 | 是 | 单据主键id |
| 主键 | rec_id | int | 11 | 是 | 主键（与业务无关） |
| 委外单号 | order_no | varchar | 40 | 是 | 委外单号，默认WK开头 |
| 货品id | goods_id | int | 11 | 是 | 货品id |
| 货品简称 | short_name | varchar | 255 | 是 | 货品简称 |
| 商家编码 | spec_no | varchar | 40 | 是 | 商家编码 |
| 主条码 | barcode | varchar | 40 | 是 | 主条码 |
| 单位id | unit_id | int | 11 | 是 | 单位id |
| 品牌id | brand_id | int | 11 | 是 | 品牌id |
| 批次 | batch_no | varchar | 40 | 是 | 批次 |
| 数量 | num | decimal | (19,4) | 是 | 数量 |
| 已出入库数量 | inout_num | decimal | (19,4) | 是 | 已出入库数量 |
| 入库价格 | price | decimal | (19,4) | 是 | 入库价格 |
| 明细备注 | remark | varchar | 255 | 是 | 明细备注 |
| 品牌名称 | brand_name | varchar | 64 | 是 | 品牌名称 |
| 货品名称 | goods_name | varchar | 64 | 是 | 货品名称 |
| 货品编码 | goods_no | varchar | 40 | 是 | 货品编码 |
| 规格名称 | spec_name | varchar | 100 | 是 | 规格名称 |
| 规格码 | spec_code | varchar | 40 | 是 | 规格码 |
| 货品单位 | goods_unit | varchar | 20 | 是 | 货品单位 |
| 有效期 | expire_date | datetime |  | 是 | 有效期 |
| 保质期 | validity_days | datetime |  | 是 | 保质期 |


#### 响应示例

### JSON

```text
{
	"code": 2160,
	"message": "start_time和end_time为空或不是有效的时间格式"
}
```


### operational_order_create_Y：运营仓单据创建

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `operational_order_create_Y` |
| PHP 文件 | `operational_order_create.php` |
| 文档标题 | 运营仓单据创建 |
| 描述 | 通过接口推送创建运营仓管理-运营仓单据到旺店通erp系统 |
| 客户端路径 | 仓储->运营仓管理->运营仓单据 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=operational_order_create_Y |

#### 接口说明

| 1.1 接口描述：通过接口推送创建erp系统运营仓管理-运营仓单据 数据 |
| --- |
| 1.2 适用版本：网页版 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/operational_order_create.php |
| 正式环境 | https://openapi.huice.com/openapi/operational_order_create.php |

| PHP | //其他入库单新建<br><?php<br>        require_once('../WdtClient.php');<br>    $c = new WdtClient;<br>        $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    //测试环境地址<br>    //上线时需要换成线上的<br>        $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/operational_order_create.php'; // 测试的<br>    $spec_item = new stdClass();<br>    $spec_item->sku_no = "951027";<br>    $spec_item->num = "1";<br>    $detail_list = [$spec_item];<br><br>    $c->putApiParam('order_type', '1');<br>    $c->putApiParam('in_warehouse_name', "测试运营仓1");<br>    //$c->putApiParam('out_warehouse_name', 1);<br>       $c->putApiParam('real_warehouse_id', "240");<br>    $c->putApiParam("detail_list", json_encode($detail_list, JSON_UNESCAPED_UNICODE));<br><br>    $json = $c->wdtOpenApi();<br>    $array = json_decode($json, true); // 转成数组<br>    echo json_encode($array, JSON_UNESCAPED_UNICODE); // 输出中文正常显示<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据类型 | order_type | int | 11 | 是 | 1.分配单 2.归还单 3.调拨单 |
| 入库运营仓 | in_warehouse_name | string | 40 | 否 | 入库运营仓仓库名称，当单据类型为1.分配单、3.调拨单时，该字段必填 |
| 出库运营仓 | out_warehouse_name | string | 40 | 否 | 出库运营仓仓库名称，当单据类型为2.归还单、3.调拨单时，该字段必填 |
| 仓库id | real_warehouse_id | string | 40 | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看  当单据类型为 1.分配单 2.归还单 仓库id或仓库编号字段其中一个必传 两个字段都传 仓库编号优先级最高 |
| 仓库编号 | real_warehouse_no | string | 40 | 否 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 当单据类型为 1.分配单 2.归还单 仓库id或仓库编号字段其中一个必传 两个字段都传 仓库编号优先级最高 |
| 备注 | remark | varchar | 255 | 否 | 备注 |
| 货品列表节点 | detail_list | data[ ] |  | 是 | 请求参数的2级数据节点，节点下数据字段详见下述“detail_list” |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | varchar | 255 | 是 | 错误信息 |
| 单据号 | order_no | varchar | 20 | 否 | 单据号 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | sku_no | varchar | 40 | 是 | 代表单品(sku)所有属性的唯一编码，ERP内单品唯一编码（sku）。推送的spec_no值在ERP货品档案必须存在，且上一层单据退换单也必须存在此编号，否则单据会创建失败。SKU概念介绍,单击这里 |
| 数量 | num | decimal | (19,4) | 是 | 数量 |
| 备注 | remark | varchar | 255 | 否 | 备注 |


#### 响应示例

### JSON

```text
{
	"code": 0,
	"message": "",
	"order_no": "OP2604090006"
}
```

### JSON

```text
{
	"code": 1020,
	"message": "商家编码(新):【951027】分配数量不可超过公共可用库存",
	"order_no": null
}
```


### operational_order_query_Y：运营仓单据查询

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `operational_order_query_Y` |
| PHP 文件 | `operational_order_query.php` |
| 文档标题 | 运营仓单据查询 |
| 描述 | 查询旺店通erp系统运营仓单据数据信息 |
| 客户端路径 | 仓储->运营仓管理->运营仓单据管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=operational_order_query_Y |

#### 接口说明

| 1.1 接口描述：查询erp系统，运营仓单据数据。即仓储->运营仓管理->运营仓单据管理的数据信息 |
| --- |
| 1.2 适用版本： |
| 1.3 增量获取：按照旺店通ERP运营仓单据的最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/operational_order_query.php |
| 正式环境 | https://openapi.huice.com/openapi/operational_order_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 运营仓名称 | warehouse_nam | string |  | 否 | 运营仓名 |
| 单据号 | order_no | string |  | 否 | 单据号 |
| 类型 | order_type | in |  | 否 | 类型，枚举："11": "分配", "12": "归还", "13": "调拨" |
| 实体仓库id | warehouse_id | long |  | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 单据状态 | status | int |  | 否 | 单据状态，枚举："10": "待审核", "50": "已完成" |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量获取数据，start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量获取数据，end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为40，使用举例单击这里 |
| 页号 | page_no | int |  | 否 | 页号默认从0开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int |  | 是 | 错误码，0成功 |
| 错误描述 | message | varchar |  | 是 | 错误描述 |
| 数据总条数 | total_count | int |  | 是 | 符合条件的数据总条数，当page_no=0时返回，用来分页 |
| 运营仓单据列表节点 | data | data[] |  | 是 | 响应参数的1级数据节点，包含当前页的运营仓及其明细的数据节点,节点下数据字段详见下述" data"和“detail_list” |

| JSON | {<br>	"code": "0",<br>	"message": "",<br>	"total_count": "7",<br>	"purchase_list": [{<br>		"apply_id": "118",<br>		"purchase_apply_no": "POA202005190001",<br>		"status": "30",<br>		"createtor_name": "wanxie2-test",<br>		"warehouse_no": "wanxie2-test",<br>		"name": "wanxie2-test",<br>		"real_num": "200.0000",<br>		"ref_num": "200.0000",<br>		"unref_num": "0.0000",<br>		"expected_time": "0000-00-00 00:00:00",<br>		"remark": "",<br>		"modified": "2020-05-19 11:57:04",<br>		"created": "2020-05-19 11:48:44",<br>		"details_list": [{<br>			"rec_id": "335",<br>			"apply_id": "118",<br>			"remark": "",<br>			"purchase_apply_no": "POA202005190001",<br>			"spec_name": "默认规格",<br>			"spec_no": "fapiao",<br>			"goods_name": "demlution test product",<br>			"brand_no": "BD201911060035",<br>			"brand_name": "无",<br>			"class_name": "无",<br>			"goods_no": "fapiao",<br>			"short_name": "dem product",<br>			"real_num": "100.0000",<br>			"ref_num": "100.0000",<br>			"provider_no": "",<br>			"provider_name": ""<br>		}, {<br>			"rec_id": "336",<br>			"apply_id": "118",<br>			"remark": "",<br>			"purchase_apply_no": "POA202005190001",<br>			"spec_name": "默认规格",<br>			"spec_no": "fapiao2",<br>			"goods_name": "demlution test product 2",<br>			"brand_no": "BD201911060035",<br>			"brand_name": "无",<br>			"class_name": "无",<br>			"goods_no": "fapiao2",<br>			"short_name": "dem test 2",<br>			"real_num": "100.0000",<br>			"ref_num": "100.0000",<br>			"provider_no": "",<br>			"provider_name": ""<br>		}]<br>	}]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单据号 | order_no | string |  | 是 | 单据号 |
| 运营仓名称 | op_warehouse_name | string |  | 是 | 运营仓名称 |
| 类型 | order_type | int |  | 是 | 类型，枚举："11": "分配", "12": "归还", "13": "调拨" |
| 单据状态 | status | int |  | 是 | 单据状态，枚举："10": "待审核", "50": "已完成" |
| 仓库id | real_warehouse_id | long |  | 是 | 实体仓库id，代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库名称 | real_warehouse_name | string |  | 是 | 实体仓库名称 |
| 货品种类数 | goods_type_count | int |  | 是 | 货品种类数 |
| 货品数量 | goods_count | decimal | (19,4) | 是 | 货品数量 |
| 制单人姓名 | create_by | string |  | 是 | 制单人姓名 |
| 制单时间 | create_date | datetime |  | 是 | 制单时间 |
| 审核时间 | check_time | datetime |  | 是 | 审核时间 |
| 备注 | remark | string |  | 是 | 备注 |
| 运营单明细节点 | detail_list | data[] |  |  | 响应参数的2级数据节点，,节点下数据字段详见下述“detail_list” |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商品id | sku_id | int | 11 | 是 | 商品id |
| 货品简称 | spu_short_name | int | 11 | 是 | 货品简称 |
| 商家编码 | sku_no | varchar | 20 | 是 | 商家编码 |
| 库存数量 | num | varchar | 40 | 是 | 库存数量 |
| 可用库存 | available_num | varchar | 255 | 是 | 可用库存 |
| 公共可用库存 | public_available_num | varchar | 64 | 是 | 公共可用库 |
| 备注 | remark | varchar | 32 | 是 | 备注 |


#### 响应示例

### JSON

```text
{
	"code": 2180,
	"message": "start_time与end_time时间跨度不能超过最大范围30天"
}
```


### operational_stock_detail_query_Y：运营仓库存明细查询

| 项目 | 内容 |
|---|---|
| 分类 | 库存类 |
| 服务名 | `operational_stock_detail_query_Y` |
| PHP 文件 | `operational_stock_detail_query.php` |
| 文档标题 | 运营仓库存明细查询 |
| 描述 | 查询旺店通erp系统运营仓库存明细数据 |
| 客户端路径 | 仓储->运营仓管理->运营仓库存明细 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=operational_stock_detail_query_Y |

#### 接口说明

| 1.1 接口描述：查询erp系统，运营仓库存明细数据。即仓储->运营仓管理->运营仓库存明细数据。 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取：按照运营仓库存明细数据最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |


#### 调用场景

| 2.1 举例说明： SAP、线下ERP、SRM、SCM等系统对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/operational_stock_detail_query.php |
| 正式环境 | https://openapi.huice.com/openapi/operational_stock_detail_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once ('../WdtClient.php');<br>    $c = new WdtClient();<br>     $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    $c->gatewayUrl =  'https://openapi.ali.huice.cc/openapi/stock_full_query.php';<br><br>  //  $c->putApiParam('start_time', '2026-01-01 00:00:00');<br>    //$c->putApiParam('end_time', '2026-01-30 23:59:59');<br>    $c->putApiParam('page_no', '0');<br>    $c->putApiParam('page_size', '100');<br>    $c->putApiParam('warehouse_id', '3');<br>   // $c->putApiParam('spec_no', '');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 否 | 按最后修改时间增量获取数据,start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 否 | 按最后修改时间增量获取数据,start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int |  | 否 | 每页返回条数，不传默认40 |
| 页号 | page_no | int |  | 否 | 不传值默认从0页开始 |
| 仓库id | warehouse_id | varchar |  | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 商家编码 | spec_no | varchar |  | 否 | 代表单品(sku)所有属性的编码 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 库存明细详情列表 | data | data[] |  | 是 | 响应参数的1级数据节点，包含库存详细数据列表，节点下数据字段详见下述"data" |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"total_count": 1,<br>	"data": [{<br>		"sku_id": "2710470137982484501",<br>		"sku_no": "jszc2-test3-12",<br>		"spu_short_name": "包材-初茶花月茶包绑绳款盖纸包装纸-21g-茉莉绿茶套\/-25C",<br>		"op_warehouse_name": "测试运营仓1",<br>		"original_lock_num": "1",<br>		"wait_send_num": "0",<br>		"checkable_lock_num": "1",<br>		"available_stock_num": "311",<br>		"purchase_in_transit_num": "0"<br>	}]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 运营仓名称 | op_warehouse_name | string |  | 是 | 运营仓名称 |
| 商品id | sku_id | long |  | 是 | 商品id ，代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 货品简称 | spu_short_name | string |  | 是 | 货品简称 |
| 商家编码 | sku_no | string |  | 是 | 商家编码 |
| 库存量 | original_lock_num | decimal | (19, 4) | 是 | 库存量 |
| 待发货量 | wait_send_num | decimal | (19, 4) | 是 | 待发货量 |
| 可用库存 | checkable_lock_num | decimal | (19, 4) | 是 | 可用库存 |
| 公共可用库存 | available_stock_num | decimal | (19, 4) | 是 | 公共可用库存 |
| 采购在途 | purchase_in_transit_num | decimal | (19, 4) | 是 | 采购在途 |


#### 响应示例

### JSON

```text
{
	"code": 2180,
	"message": "xxxxxxxx"
}
```


## 相关页面

- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/domains/视觉制作/05-小红书风格AI生图/index|旺店通开放平台 API 知识库]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/01-旺店通API能力地图|旺店通 API 能力地图]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/02-旺店通API Skill创建指南|旺店通 API Skill 创建指南]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
