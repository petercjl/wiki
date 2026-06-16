---
title: 旺店通 售后类 API 使用手册
type: concept
created: 2026-06-03
updated: 2026-06-03
domain: 电商运营
tags: [ecommerce, erp, wangdian, api]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
status: active
---

# 旺店通 售后类 API 使用手册

## 用途

本页整理旺店通开放平台 售后类 的具体接口使用方法，面向后续写代码或创建 Codex/Hermes skill。每个接口包含服务名、PHP 文件、请求地址、业务请求参数、业务响应字段、示例和注意事项。

## 本类接口

| 服务名 | 接口名 | 描述 | 客户端路径 |
|---|---|---|---|
| stockin_order_query_refund_Y | 退货入库单查询 | 获取旺店通ERP销售退货（换货）订单对应的入库单信息 | 仓储→入库管理 |
| sales_refund_push_Y | 创建原始退款单 | 销售订单（包括发货前和发货后）退款或退货单据推送至ERP。注：销售订单的售后换货订单此接口推送“退货类型”退款单，换出订单“trade_push.php”推送 | 售后→售后管理→平台售后单 |
| refund_query_Y | 查询退换管理 | 获取ERP销售退货（换货）订单信息 | 售后→售后管理→售后单 |
| aftersales_refund_create_Y | 创建系统售后单 | 创建系统售后单，---目前不支持换货 ，只支退货单，退货单类型只能是退款退货和退款不退货 基于系统单创建退款单 | 售后→售后管理→售后单 |
| vip_api_refund_query_Y | 查询原始退单 |  | 售后→售后管理→平台售后单 |
| aftersale_stockin_confirm_Y | 创建退货入库单 | 推送旺店通ERP销售退货（换货）订单对应的入库单据给旺店通ERP，推送前提旺店通ERP的退换单状态为“待收货” | 仓储--入库管理--退货入库单--新建 |

## 接口详情

### stockin_order_query_refund_Y：退货入库单查询

| 项目 | 内容 |
|---|---|
| 分类 | 售后类 |
| 服务名 | `stockin_order_query_refund_Y` |
| PHP 文件 | `stockin_order_query_refund.php` |
| 文档标题 | 查询退货入库单 |
| 描述 | 获取旺店通ERP销售退货（换货）订单对应的入库单信息 |
| 客户端路径 | 仓储→入库管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stockin_order_query_refund_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP销售退货（换货）订单对应的入库单信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取：按照ERP退货入库单的最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |
| 1.5 注意事项：本接口不返回淘系及系统供销平台订单数据，相关平台规则单击这里。淘系及系统供销订单数据获取办法单击这里。其他平台的敏感信息会根据平台规则同步调整。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stockin_order_query_refund.php |
| 正式环境 | https://openapi.huice.com/openapi/stockin_order_query_refund.php |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    //测试环境地址<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stockin_order_query_refund.php';<br>    //上线时需要换成线上的<br>    //$c->gatewayUrl = 'https://openapi.huice.com/openapi/stockin_order_query_refund.php';<br><br>    $c->putApiParam("page_no", "0");<br>    $c->putApiParam("page_size", "100");<br>    // 修改时间<br>    $c->putApiParam("start_time", "2025-01-09 15:00:00");<br>    $c->putApiParam("end_time", "2025-01-11 15:00:00");<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
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
| 状态 | status | tinyint | 4 | 否 | 入库单状态 10已取消20编辑中30待审核80已完成 |
| 开始时间 | start_time | datetime |  | 是 | 按时间增量获取数据,start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按时间增量获取数据,end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 入库单号 | stockin_no | varchar | 40 | 否 | 入库单号，传该字段可以不传时间范围 |
| 是否仅获取库存数据 | fetch_stock_only |  |  |  | 1-是，0-否，默认为否 |
| 退换单号 | src_order_no | varchar | 40 | 否 | 系统退换单号，默认RT开头，传该字段可以不传时间范围 |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为40，使用举例单击这里 |
| 页号 | page_no | int |  | 否 | 页号默认从0开始 |
| 仓库id | warehouse_id | varchar | 40 | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 入库单详情 | stockin_list | data[] |  | 否 | 入库单详情数据节点 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "stockin_list": [{<br>        "stockin_id": "2759193026822668294",<br>        "status": 80,<br>        "refund_id": "2759192915048661008",<br>        "order_no": "RK2511050024",<br>         "creator_name": "测试",<br>        "src_order_no": "RT2511050025",<br>        "trade_no": "JY25110517874",<br>        "check_time": "2025-11-05 22:08:01",<br>        "stockin_time": "2025-11-05 22:08:01",<br>        "logistics_id": null,<br>        "logistics_no": "772048916873485",<br>        "warehouse_id": "116",<br>        "remark": "",<br>        "modified": "2025-11-05 22:08:01",<br>        "shop_id": "568",<br>        "trans_from_wt": 0,<br>        "details_list": [{<br>            "rec_id": "2759193026864611334",<br>            "stockin_id": "2759193026822668294",<br>            "src_order_detail_id": "2759192915098992656",<br>            "spec_id": "2758410743714938891",<br>            "num": "1.0000",<br>            "cost_price": "0.0000",<br>            "batch_no": "",<br>            "oid": "20005739317",<br>            "tid": "20005739317",<br>            "spec_no": "19861927100000077",<br>            "goods_name": "测试ERP 单品+赠品+套餐",<br>            "goods_no": "25110312301",<br>            "production_date": "9999-12-01 00:00:00",<br>            "spec_name": "色3小",<br>            "platform_id": "127",<br>            "defect": 0,<br>            "goods_unit": "",<br>            "actual_refund_amount": "0.02000000",<br>            "src_price": "0.02000000",<br>            "expire_date": "9999-12-01 00:00:00",<br>            "modified": "2025-11-05 22:08:01"<br>        }]<br>    }]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | Y 字段 | Y父级字段 | Y类型 | Y枚举 | 是否必须 | 默认值 | 是否可变更 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 销售入库单id | stockin_id |  | bigint(20) |  | 是 |  | 否 |
| 入库状态 | status |  | tinyint(4) | 入库单状态 10已取消20编辑中30待审核80已完成 | 是 |  | 是 |
| 系统退单id | refund_id |  | bigint(20) |  | 是 |  | 否 |
| 销售入库单号 | order_no |  | string |  | 是 |  | 否 |
| 仓库编号 | warehouse_name |  | string |  | 是 |  | 否 |
| 系统退单号 | src_order_no |  | string |  | 是 |  | 否 |
| 系统单号 | trade_no |  | string |  |  |  |  |
| 审核时间 | check_time |  | datetime |  |  |  |  |
| 创建时间 | stockin_time |  | datetime |  | 是 |  | 否 |
| 物流单号 | logistics_no |  | string |  | 是 |  | 是 |
| 仓库id | warehouse_id |  | int(11) | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 | 是 |  | 是 |
| 仓库编码 | warehouse_no |  | varchar(40) | 代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 | 是 |  | 是 |
| 备注 | remark |  | string |  | 是 |  | 是 |
| 最后修改时间 | modified |  | datetime |  | 是 |  | 是 |
| 制单人 | creator_name |  | string | 制单人 | 是 |  |  |
| 平台id | platform_id |  | int(11) |  | 是 |  |  |
| 供应商编码 | provider_nick_no |  | string | 供应商编码 | 是 |  |  |
| 供应商名称 | provider_name |  | string | 供应商名称 | 是 |  |  |
| 店铺id | shop_id |  | int(11) | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 | 是 |  | 否 |
| 店铺编码 | shop_no |  | varchar(50) | 代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 | 是 |  | 是 |
| 店铺名称 | shop_name |  | varchar(40) | 店铺名称 | 是 |  |  |
| 客户网名 | buyer_nick |  | string |  | 是 |  |  |
| 是否从无头件转成退货入库 | trans_from_wt |  | int | 0 否 1 是 | 否 |  | 是 |
| 货品列表 | details_list |  | array[] | 货品列表 | 是 |  |  |
| 销退入库明细id | rec_id | details_list | bigint(20) |  | 是 |  | 否 |
| 入库单id | stockin_id | details_list | bigint(20) |  | 否 |  | 否 |
| 系统退单明细id | src_order_detail_id | details_list | bigint(20) |  | 是 |  | 否 |
| 货品明细id | spec_id | details_list | bigint(20) |  | 是 |  | 否 |
| 入库数量 | num | details_list | decimal(21, 6) |  | 是 |  | 是 |
| 批次号 | batch_no | details_list | string |  | 否 | null | 是 |
| 最后修改时间 | modified | details_list | datetime |  | 是 |  | 是 |
| sku主条码 | barcode | details_list | varchar(40) |  | 是 |  | 是 |
| 明细备注 | remark | details_list | varchar(64) |  | 是 |  | 是 |
| 原订单原始子单号 | oid | details_list | varchar(64) |  | 是 |  |  |
| 原订单原始单号 | tid | details_list | varchar(64) |  | 是 |  |  |
| 商家编码 | spec_no | details_list | varchar(40) |  | 是 |  |  |
| 商品名称 | goods_name | details_list | varchar(100) |  | 是 |  |  |
| 货品编号 | goods_no | details_list | varchar(40) |  | 是 |  |  |
| 规格名称 | spec_name | details_list | varchar(100) |  | 是 |  |  |
| 批次有效期 | expire_date | details_list | datetime |  | 是 |  | 是 |
| 货位 | position_no | details_list | string |  | 是 |  |  |
| 生产日期 | production_date | details_list | datetime | 生产日期 | 是 |  |  |
| 成本价 | cost_price | details_list | decimal(21, 6) | 该成本价为批次成本价，当数据无批次时，该价格返回为0 | 是 |  | 否 |
| 入库价格 | stockin_price | details_list | decimal(21, 6) | 入库价格 | 是 |  |  |
| 平台id | platform_id | details_list | int(11) |  | 是 |  |  |
| 主播id | anchor_id | details_list | int(11) |  | 是 |  |  |
| 主播名称 | anchor_name | details_list | varchar(40) |  | 是 |  |  |
| 正品残次品 | stock_type | details_list | int(11) | 1：正品； 2：残品 | 是 | 0 |  |
| 实退金额 | actual_refund_amount | details_list | decimal(21, 6) |  | 否 |  | 是 |
| 单位 | goods_unit | details_list | varchar(40) |  | 否 |  | 是 |
| 原订单明细上的实付金额 | src_price | details_list |  |  |  |  |  |


#### 响应示例

### JSON

```text
{
    "code":2900,
    "message":"时间范围与入库单号不能全部为空"
}
```


### sales_refund_push_Y：创建原始退款单

| 项目 | 内容 |
|---|---|
| 分类 | 售后类 |
| 服务名 | `sales_refund_push_Y` |
| PHP 文件 | `sales_refund_push.php` |
| 文档标题 | 创建原始退款单 |
| 描述 | 销售订单（包括发货前和发货后）退款或退货单据推送至ERP。注：销售订单的售后换货订单此接口推送“退货类型”退款单，换出订单“trade_push.php”推送 |
| 客户端路径 | 售后→售后管理→平台售后单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_refund_push_Y |

#### 接口说明

| 1.1 接口描述：销售订单（包括发货前和发货后）退款或退货单据推送至ERP。注：销售订单的售后换货订单此接口推送“退货类型”退款单，换出订单“trade_push.php”推送 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 调用建议：批量推送的退款单据，每次不超过10单 |
| 1.4 注意事项：推送的原始退款单对应的销售订单必须在旺店通ERP内已经存在，否则无法生成系统售后单并进行处理。 注：仅支持自有/其他平台店铺 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/sales_refund_push.php |
| 正式环境 | https://openapi.huice.com/openapi/sales_refund_push.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/sales_refund_push.php';<br><br>    $api_refund_list = array(<br>	   array(<br>				"tid" => "20095888033751005",<br>				"shop_id" => "332",<br>				"platform_id" => 127,<br>				"refund_no" => "202603240001",<br>				"type" =>2 ,//2:退货退款<br>				"status" =>2,// 2 申请退款<br>				"refund_fee" => "16",<br>				"logistics_name"  => "邮政国内小包",<br>				"logistics_no"=>"YZGNXB202603240001",<br>				"buyer_nick" => "33",<br>				"refund_time" => "2026-03-24 00:00:08",<br>				"reason" => "不想要了",<br>				"desc" => "北京",<br>				"order_list" => array(<br>					array(<br>						"oid" => "19987739173003077",<br>						"num" =>1<br>					),<br>					array(<br>						"oid" => "12090008317300b",<br>						"num" =>1<br>					)<br><br>				)<br>			)<br>    );<br><br>    $c->putApiParam('api_refund_list',json_encode($api_refund_list,JSON_UNESCAPED_UNICODE));<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退款单节点 | api_refund_list | data[ ] |  | 是 | 请求参数的1级数据节点，包含平台售后订单所有属性信息的数据节点，节点下数据字段详见下述“api_refund_list” |

| JSON | {<br>    "code": 5040,<br>    "message": "推送订单信息错误，错误内容：售后单关联的原始单不存在，要推送售后单，也就是 给到的tid 必须在旺店通系统中存在"<br>} |
| --- | --- |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int |  | 是 | 返回码，0成功，非0失败 |
| 错误信息 | message | varchar |  | 是 | 返回信息 |
| 新增条数 | new_count | int |  | 否 | 新增条数 |
| 更新条数 | chg_count | int |  | 否 | 更新条数 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 平台ID | platform_id | smallint | 6 | 是 | 输入固定值127 |
| 店铺id | shop_id | int |  | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar | 50 | 是 | 代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看，如果与shop_id同时传输，shop_no字段优先级更高 |
| 平台销售订单号 | tid | varchar |  | 是 | 平台订单单号（与推送trade_push的tid保持一致对应旺店通ERP内原始单号） |
| 平台退款/退货单号 | refund_no | varchar | 40 | 是 | 平台退款/退货单单号，保证唯一 |
| 平台售后类型 | type | int |  | 是 | type=1：退款(未发货退款)；type=2：退货退款 type=4 退款不退货 |
| 平台售后状态 | status | varchar |  | 是 | 可选值：1 已取消 2 申请退款，3 等待退货（卖家同意后）  4 等待收货（买家发货后）5 退款成功 7 拒绝买家退货待买家修改8 卖家发出换货商品待买家签收 |
| 退款金额 | refund_fee | decimal | 19,4 | 否 | 退款金额 |
| 买家昵称 | buyer_nick | varchar | 100 | 是 | 买家昵称（不传该字段，默认取原始订单上客户网名） |
| 单据创建时间 | refund_time | datetime |  | 是 | 单据创建时间,时间格式：yyyy-MM-dd HH:mm:ss |
| 退款原因 | reason | varchar | 255 | 否 | 退款原因 |
| 备注 | desc | varchar | 255 | 否 | 备注 |
| 物流单号 | logistics_no | varchar | 40 | 否 | 物流单号（如需维护退货物流单号，与logistics_name物流公司名称同时使用） |
| 物流公司名称 | logistics_name | varchar | 40 | 否 | 物流公司名称 |
| 售后子订单 | order_list | data[] |  | 是 | 售后子订单 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 平台订单子订单编号 | oid | varchar | 40 | 是 | 平台订单子订单编号（与推送trade_push的oid保持一致，对应旺店通ERP内原始子订单编号）可推送部分子订单 |
| 退货货品数量 | num | decimal | (19,4) | 是 | 退货货品数量（如果是type=1 退款   4 退款不退货类型，此处代表退款数量） |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "new_count": 1,
    "chg_count": 0
}
```


### refund_query_Y：查询退换管理

| 项目 | 内容 |
|---|---|
| 分类 | 售后类 |
| 服务名 | `refund_query_Y` |
| PHP 文件 | `refund_query.php` |
| 文档标题 | 查询退换管理 |
| 描述 | 获取ERP销售退货（换货）订单信息 |
| 客户端路径 | 售后→售后管理→售后单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=refund_query_Y |

#### 接口说明

| 1.1 接口描述：获取ERP销售退货（换货）订单信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3注意事项：权限校验：【店铺、仓库权限】为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，相关平台规则点击这里，淘系及系统供销平台数据获取办法点击这里，拼多多请自行对接平台获取。本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/refund_query.php |
| 正式环境 | https://openapi.huice.com/openapi/refund_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>require_once("../WdtClient.php");<br>$c = new WdtClient;<br><br>$c->sid ='';<br>$c->appkey ='';<br>$c->appsecret ="";<br>$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/refund_query.php';<br>$c->putApiParam("page_no", "0");<br>$c->putApiParam("page_size", "100");<br>$c->putApiParam("modified_from", "2025-12-01 00:00:00");<br>$c->putApiParam("modified_to", "2025-12-02 00:00:00");<br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | Y字段 | 描述 | 必须 |
| --- | --- | --- | --- | --- |
| 店铺id |  | shop_ids | 由英文逗号分隔的店铺ID，代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |
| 店铺编号 | shop_nos | shop_nos | 由英文逗号分隔的店铺编码，代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |
| 原始单号 | tid | tid | 原始单号 |  |
| 系统订单编号 | trade_no | trade_no | 系统订单编号 |  |
| 退换单号 | refund_no | refund_no | 退换单号 |  |
| 物流单号 | return_logistics_no | return_logistics_no | 物流单号（退换单上的退回物流单号） |  |
| 修改起始时间 | modified_from | modified_from | 修改起始时间 | 是 |
| 修改结束时间 | modified_to | modified_to | 修改结束时间 | 是 |
| 时间类型 | time_type | time_type | 时间类型，0:最后修改时间，1:申请退款时间，2:结算时间。默认为0 |  |
| 退换单状态 | status | status | 10 已取消;20 待确认;35 待推送;36 推送失败;60 待入库;70 部分入库;90 已完成 |  |
| 入库状态 | stockin_status | stockin_status | 0:无需入库;1:待入库;2:部分入库;3:全部入库;4:终止入库 |  |
| 退回仓库id |  | return_warehouse_ids | 退回仓库id，用英文逗号分隔 |  |
| 退回仓库编码 | return_warehouse_nos | return_warehouse_nos | 退回仓库编码，用英文逗号分隔 |  |
| 退换单类型 | type | type | 订单类型 1.退款（未发货退款） 2.退货  3.换货  4.退款不退货  7 补寄   9 其他退款 11 已发货仅退款 |  |
| 分页大小 | page_size | page_size | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100，使用举例单击这里 | 否 |
| 页号 | page_no | page_no | 页号，不传默认从0页开始 | 否 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误信息 |
| 条数 | total_count | varchar | 255 | 是 | 满足条件的总条数 当page_no = 0时返回 |
| 系统退单 | refunds | data[] |  | 是 | 业务数据的一级节点，数组形式的订单数据，需要循环读取 |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"total_count": 1,<br>	"refunds": [{<br>		"refund_id": "2768505661460316165",<br>		"refund_no": "RT2512010001",<br>		"process_status": 90,<br>		"platform_status": 5,<br>		"shop_id": "1",<br>		"tid": "327309666449",<br>		"platform_id": "3",<br>		"sales_tid": "JY2512013650",<br>		"src_no": "35159434144",<br>		"swap_trade_no": "",<br>		"from_type": 1,<br>		"type": 1,<br>		"return_goods_count": "2.0000",<br>		"goods_amount": "5.5100",<br>		"guarante_refund_amount": "5.5100",<br>		"direct_refund_amount": "0.0000",<br>		"actual_refund_amount": "5.5100",<br>		"refund_reason": "不想要了",<br>		"remark": "不想要了",<br>		"modified": "2025-12-01 14:53:06",<br>		"return_logistics_name": "",<br>		"return_logistics_no": "",<br>		"reason_id": "1",<br>		"finish_time": "2025-12-01 14:53:06",<br>		"buyer_nick": "jd_44e290409fcca",<br>		"actual_refund_num": "0.0000",<br>		"apply_time": "2025-12-01 14:47:34",<br>		"refund_time": "2025-12-01 14:47:34",<br>		"created": "2025-12-01 14:53:06",<br>		"is_settled": false,<br>		"refund_order_list": [{<br>			"order_id": "2768505661485483013",<br>			"oid": "327309666449:10158623625970",<br>			"sales_order_id": "2768499451151517701",<br>			"platform_id": "3",<br>			"tid": "327309666449",<br>			"src_no": "35159434144",<br>			"sales_tid": "JY2512013650",<br>			"spec_id": "2712978405392909317",<br>			"spec_no": "aa",<br>			"goods_no": "sjbm0513-2",<br>			"spec_code": "",<br>			"refund_num": "1.0000",<br>			"original_price": "5.5100",<br>			"price": "2.7550",<br>			"refund_order_amount": "2.7550",<br>			"total_amount": "2.7550",<br>			"remark": "",<br>			"modified": "2025-12-01 14:53:06",<br>			"stockin_num": "0.0000",<br>			"goods_name": "测试品牌测试宝贝发布T恤0513-2测试品牌（0506-2）测试宝贝发布 黑色 (105) S 哇哈哈哈",<br>			"spec_name": "测试品牌测试宝贝发布T恤0513-2测试品牌（0506-2）测试宝贝发布;黑色;(105);S;哇哈哈哈",<br>			"deleted": 0,<br>			"order_num": "1.0000",<br>			"suite_id": "0",<br>			"suite_no": "",<br>			"suite_num": "0.0000",<br>			"anchor_id": "",<br>			"anchor_name": "",<br>			"gift_type": 0,<br>			"created": "2025-12-01 14:53:06",<br>			"api_spu_name": "测试品牌测试宝贝发布T恤0513-2测试品牌（0506-2）测试宝贝发布 黑色 S (105) 哇哈哈哈",<br>			"api_spu_no": "sjbm0513-3",<br>			"api_sku_name": "黑色 S (105) 哇哈哈哈",<br>			"api_sku_no": "aa"<br>		}, {<br>			"order_id": "2768505661485481989",<br>			"oid": "327309666449:10158623625972",<br>			"sales_order_id": "2768499451151516677",<br>			"platform_id": "3",<br>			"tid": "327309666449",<br>			"src_no": "35159434144",<br>			"sales_tid": "JY2512013650",<br>			"spec_id": "2718525646815888399",<br>			"spec_no": "sjbm0513-2_桔红色_(105)S哇哈哈哈",<br>			"goods_no": "sjbm0513-2#250701015",<br>			"spec_code": "",<br>			"refund_num": "1.0000",<br>			"original_price": "0.0000",<br>			"price": "2.7550",<br>			"refund_order_amount": "2.7550",<br>			"total_amount": "2.7550",<br>			"remark": "",<br>			"modified": "2025-12-01 14:53:06",<br>			"stockin_num": "0.0000",<br>			"goods_name": "测试品牌测试宝贝发布T恤0513-2测试品牌（0506-2）测试宝贝发布 桔红色 (105) S 哇哈哈哈",<br>			"spec_name": "测试品牌测试宝贝发布T恤0513-2测试品牌（0506-2）测试宝贝发布;桔红色;(105);S;哇哈哈哈",<br>			"deleted": 0,<br>			"order_num": "1.0000",<br>			"suite_id": "0",<br>			"suite_no": "",<br>			"suite_num": "0.0000",<br>			"anchor_id": "",<br>			"anchor_name": "",<br>			"gift_type": 0,<br>			"created": "2025-12-01 14:53:06",<br>			"api_spu_name": "测试品牌测试宝贝发布T恤0513-2测试品牌（0506-2）测试宝贝发布 桔红色 S (105) 哇哈哈哈",<br>			"api_spu_no": "sjbm0513-3",<br>			"api_sku_name": "桔红色 S (105) 哇哈哈哈",<br>			"api_sku_no": "sjbm0513-2_桔红色_(105)S哇哈哈哈"<br>		}]<br>	}]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单主键 | refund_id | bigint(20) | 20 | 是 | 退换单主键 |
| erp退换单号 | refund_no | string | 64 | 是 | erp退换单号，默认RT开头 |
| 系统退单状态 | process_status | tinyint(4) | 4 | 是 | 10 已取消;20 待确认;35 待推送;36 推送失败;60 待入库;70 部分入库;90 已完成 |
| 平台状态 | platform_status | tinyint(4) | 4 | 是 | 平台状态：1取消退款,2已申请退款,3等待退货,4等待收货,5退款成功 |
| 店铺id | shop_id | int(11) | 11 | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | string | 50 | 是 | 代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 退入仓库编号 | return_warehouse_no | string | 40 | 是 | 代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 退入仓库id | return_warehouse_id | int(11) | 11 | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 退入仓库名称 | return_warehouse_name | string |  | 是 | 退入仓库名称 |
| 入库状态 | stockin_status | tinyint(4) | 4 | 是 |  |
| 平台订单号 | tid | string | 255 | 是 | 可能多个 |
| 平台id | platform_id | int(11) | 11 | 是 |  |
| 是否收到货品 | is_goods_received |  |  | 是 | 是否收到货品 |
| 系统订单号 | sales_tid | string | 64 | 是 |  |
| 平台退单号 | src_no | string | 64 | 是 |  |
| 换出原始订单号 | swap_trade_no | string | 64 | 否 |  |
| 建单方式 | from_type | tinyint(4) | 4 | 是 | 建立方式 1api抓单 2手式建单 |
| 类型 | type | tinyint(4) | 4 | 是 | 类型 1.退款（未发货退款） 2.退货  3.换货  4.退款不退货  7.补寄  8.维修退款 9.其他退款    10.订单补款   11.已发货仅退款  21.退货退款（全托） |
| 数量 | return_goods_count | decimal(19, 4) | 19 | 是 |  |
| 申请退货金额 | goods_amount | decimal(19, 4) | 19 | 是 |  |
| 非担保退款金额 | direct_refund_amount | decimal(19, 4) |  | 是 | 非担保退款金额 |
| 平台退款金额 | guarante_refund_amount | decimal(19, 5) | 19 | 否 |  |
| 线下退款金额 | offline_refund_amount | decimal(19, 6) | 19 | 否 |  |
| 实际退款金额 | actual_refund_amount | decimal(19, 4) |  | 否 |  |
| 实退数量 | actual_refund_num | decimal(19, 4) |  | 否 | 实际入库完的数量 |
| 平台售后单售后原因 | refund_reason | varchar | 255 | 否 | 平台售后单售后原因 |
| 售后原因 | remark | varchar | 255 | 否 | 售后原因 |
| 创建人id | creator_id | varchar | 255 | 否 | 创建人id |
| 创建人姓名 | creator_name | varchar | 255 | 否 | 创建人姓名 |
| 原单业务员id | trade_salesman_id | varchar | 255 | 否 | 原单业务员id |
| 原单业务员姓名 | trade_salesman_name | varchar | 255 | 否 | 原单业务员姓名 |
| 退货人手机号 | return_mobile | varchar |  | 是 | 退货人手机号 |
| 结算状态 | statement_status | varchar |  | 是 | 结算状态 0未结算 1已结算 |
| 换货收件人省市区 | swap_area | varchar |  | 是 | 换货收件人省市区 |
| 换货收件人省份 | swap_province | varchar |  | 是 | 换货收件人省份 |
| 换货收件人城市 | swap_city | varchar |  | 是 | 换货收件人城市 |
| 换货收件人区县 | swap_district | varchar |  | 是 | 换货收件人区县 |
| 换货收件人手机 | swap_mobile | varchar |  | 是 | 换货收件人手机 |
| 退货人姓名 | return_name | varchar |  | 是 | 退货人姓名 |
| 换货收件人姓名 | swap_receiver | varchar |  | 是 | 换货收件人姓名 |
| 外部仓库的单号 | wms_outer_no | varchar |  | 是 | 外部仓库的单号 |
| 最后修改时间 | modified | datetime |  | 是 | 最后修改时间 |
| 申请时间 | apply_time | datetime |  | 是 | 申请时间 |
| 退回物流公司名称 | return_logistics_name | varchar | 255 | 否 | 退回物流公司名称 |
| 退回物流公司单号 | return_logistics_no | varchar | 255 | 否 | 退回物流公司单号 |
| 退款原因ID | reason_id | int(11) |  | 否 |  |
| 结算时间 | finish_time | datetime |  | 否 |  |
| 客户昵称 | buyer_nick | varchar | 255 | 否 |  |
| 创建时间 | created | datetime |  | 是 |  |
| 申请时间 | refund_time | datetime |  | 否 |  |
| 退款子订单信息 | refund_order_list | data[] |  | 是 | 退款子订单信息, refund_order_list结构 |
| 换货明细列表 | refund_out_goods_list | data[] |  | 是 | 换货明细列表节点refund_out_goods_list |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 系统退单明细id | order_id | bigint(20) |  | 是 |  |
| 平台子订单号 | oid | varchar | 64 | 是 |  |
| 系统订单明细id | sales_order_id | bigint(20) | 20 | 是 |  |
| 平台id | platform_id | int(11) | 11 | 是 |  |
| 平台订单号 | tid | varchar | 64 | 是 |  |
| 平台退单号 | src_no | varchar | 64 | 是 |  |
| 系统订单号 | sales_tid | varchar | 64 | 是 |  |
| 单品id | spec_id | bigint(20) | 20 | 是 |  |
| 商家编码 | spec_no | varchar | 64 | 是 |  |
| 货品编码 | goods_no | varchar | 64 | 是 |  |
| 规格编码 | spec_code | varchar | 64 | 否 |  |
| 组合装名称 | suite_name | varchar | 64 | 否 |  |
| 数量 | refund_num | decimal(19, 4) | 19 | 是 |  |
| 原价 | original_price | decimal(19, 4) | 19 | 是 | 系统订单明细的标价 |
| 价格 | price | decimal(19, 4) | 19 | 是 | 系统订单明细的成交价 |
| 退款金额 | refund_order_amount | decimal(19, 4) | 19 | 是 |  |
| 退货金额 | total_amount | decimal(19, 4) | 19 | 是 | 系统订单明细的分摊总价 |
| 备注 | remark | varchar | 255 | 是 |  |
| 最后修改时间 | modified | datetime |  | 是 |  |
| 实际入库数量 | stockin_num | decimal(19, 4) | 19 | 是 |  |
| 商品名称 | goods_name | varchar | 255 | 是 |  |
| 规格名称 | spec_name | varchar | 255 | 是 |  |
| 主播ID | anchor_id | varchar(64) |  | 是 | 主播ID |
| 主播名称 | anchor_name | varchar(64) |  | 是 | 主播名称 |
| 系统货品对应平台SPU编码 | api_spu_no | varchar | 255 | 是 | 系统货品对应平台SPU编码 |
| 系统货品对应平台SKU编码 | api_sku_no | varchar | 255 | 是 | 系统货品对应平台SKU编码 |
| 平台SPU名称 | api_spu_name | varchar | 255 | 是 | 平台SPU名称 |
| 平台SKU规格名称 | api_sku_name | varchar | 255 | 是 | 平台SKU规格名称 |
| 实际数量 | order_num | decimal(19, 4) | 19 | 否 |  |
| 组合装id | suite_id | bigint(20) | 20 | 否 |  |
| 组合装编码 | suite_no | decimal(19, 4) | 19 | 否 |  |
| 组合装数量 | suite_num | decimal(19, 4) | 19 | 否 |  |
| 货品成本 | goods_cost | decimal | 19 | 是 | 正向订单出库成本 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 售后单id | refund_id | bigint | 20 | 否 | 售后单id |
| 商品类型 | target_type | int | 11 | 否 | 商品类型 |
| 商品id | target_id | bigint | 20 | 否 | 商品id |
| 货品名称 | goods_name | string |  | 否 | 货品名称 |
| 单品名称 | spec_name | string |  | 否 | 单品名称 |
| 商家编码 | merchant_no | string |  | 否 | 商家编码(如果是组合装，返回的是组合装编码) |
| 价格 | pric | decimal(19, 4) |  | 否 | 价格 |
| 数量 | num | decimal(19, 4) |  | 否 | 数量 |
| 备注 | remark | string |  | 否 | 备注 |
| 单品编码 | spec_code | string |  | 否 | 单品编码 |
| 子订单号 | oid | string |  | 否 | 子订单号 |
| 创建时间 | created | datetime |  | 否 | 创建时间 |
| 更新时间 | modified | datetime |  | 否 | 更新时间 |
| 品牌名称 | brand_name | string |  | 否 | 品牌名称 |
| 条码 | barcode | string |  | 否 | 条码 |
| 单品商家编码 | spec_no | string |  | 否 | 单品商家编码 |
| 组合装编码 | suite_no | string |  | 否 | 组合装编码 |


#### 响应示例

### JSON

```text
{
    "code": 2105,
    "message": "modified_from不能等于modified_to"
}
```


### aftersales_refund_create_Y：创建系统售后单

| 项目 | 内容 |
|---|---|
| 分类 | 售后类 |
| 服务名 | `aftersales_refund_create_Y` |
| PHP 文件 | `aftersales_refund_create.php` |
| 文档标题 | 创建系统售后单 |
| 描述 | 创建系统售后单，---目前不支持换货 ，只支退货单，退货单类型只能是退款退货和退款不退货 基于系统单创建退款单 |
| 客户端路径 | 售后→售后管理→售后单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=aftersales_refund_create_Y |

#### 接口说明

| 1.1 接口描述：创建系统售后单，-支持退货和换货类型，退货单类型是退款退货和退款不退货  基于系统单创建售后单 |
| --- |
| 1.2 适用版本：网页版 |
| 1. 3注意事项：推送的售后单对应的销售订单必须在旺店通ERP内已经存在，否则无法生成系统售后单并进行处理 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/aftersales_refund_create.php |
| 正式环境 | https://openapi.huice.com/openapi/aftersales_refund_create.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once("../WdtClient.php");<br>	$c = new WdtClient;<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = "";<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/aftersales_refund_create.php';<br><br>    $refund_info = array(<br>    "trade_no" => "JY2603191166",<br>	"type"=> 2,<br>	"warehouse_id"=>38,<br>    "logistics_no"=> "JD2026032400002",<br>	"logistics_code"=> 59,<br>    "warehouse_id"=> 38,<br>    "reason_id"=> 2,<br>    "shop_id"=> 332,<br>    "pay_type"=> 2,<br>    "refund_order_list"=>array(<br>	   array(<br>        "trade_item_id"=> '2807683938439398427',//trade_query_Y接口返回的rec_id<br>	      "tid"=> "200733112e1233897",<br>       "oid"=> "192uu077890033399",<br>       "spec_id"=> "2807660532977371156",<br>       "refund_num"=> 2,<br>       "refund_amount"=> 45.00<br>	   )<br>	)<br>   );<br><br>$c->putApiParam('refund_info', json_encode($refund_info, JSON_UNESCAPED_UNICODE));<br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | Y父级字段 | Y类型 | Y枚举 | 是否必须 |
| --- | --- | --- | --- | --- | --- |
| 退款单主信息 | refund_info |  |  |  |  |
| 订单编号 | trade_no | refund_info | varchar(64) |  | 是 |
| 退换类型 | type | refund_info | int | 2 退货退款 3 换货 4 退款不退货 | 是 |
| 退回仓库ID | warehouse_id | refund_info | int | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 | 是 |
| 退回仓库编号 | warehouse_no | refund_info | varchar(40) | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |  |
| 退回物流单号 | logistics_no | refund_info | varchar(64) |  | 否 |
| 退回物流公司ID | logistics_code | refund_info | int | 物流公司类型代码，详情见物流代码表 | 否 |
| 退回物流公司名称 | logisitcs_name | refund_info | varchar(64) | 物流公司名称 | 否 |
| 退回原因 | reason_id | refund_info | int | 1 尺码错误/不喜欢/效果差 2 商品质量问题 3 7 天无理由退货4 重复购买 5 大小尺寸与描述不符合 6 不想买了 7 买错了 8 其他 | 否，不传为8 其他 |
| 店铺id | shop_id | refund_info | int | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 | 是 |
| 店铺编号 | shop_no | refund_info | varchar(40) | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |
| 支付类型 | pay_type | refund_info | int | 1 线下支付 2 微信支付3 支付宝支付 | 否 默认 1 |
| 换出收件人姓名 | receiver_name | refund_info | varchar | 换出收件人姓名 | 否 |
| 换出收件人手机号 | receiver_mobile | refund_info | varchar | 换出收件人手机号 | 否 |
| 换出收件人详细地址 | receiver_address | refund_info | varchar | 换出收件人详细地址 | 否 |
| 换出收件人省份 | receiver_province | refund_info | varchar | 换出收件人省份 | 否 |
| 换出收件人城市 | receiver_city | refund_info | varchar | 换出收件人城市 | 否 |
| 换出收件人区 | receiver_district | refund_info | varchar | 换出收件人区 | 否 |
| 退货明细信息 | refund_order_list | refund_info |  |  |  |
| 系统订单明细id | trade_item_id | refund_order_list |  |  | 是 |
| 原始订单号 | tid | refund_order_list | varchar(64) |  | 否 |
| 原始子订单号 | oid | refund_order_list | varchar(64) |  | 否 |
| 规格id | spec_id | refund_order_list | bigint(20) |  | 否 |
| 退款金额 | refund_amount | refund_order_list | decimal(19,4) |  | 否，不填写使用商品单价*退款数量 |
| 退款数量 | refund_num | refund_order_list | decimal(19,4) |  | 是 |
| 换货明细信息 | exchange_order_list | refund_info |  | 换货类型推送 |  |
| 换出商家编码 | spec_no | exchange_order_list | bigint(20) | 换出商家编码 | 否 |
| 换出数量 | refund_num | exchange_order_list | decimal(19,4) | 换出数量 | 否 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |  |
| --- | --- | --- | --- | --- | --- | --- |
| 返回码 | code | int |  | 是 | 0成功 其他值失败 | 成功为0 异常有其他的编码 |
| 返回message | message | varchar(255) |  | 否 | 成功时为空 | 成功为空，错误返回错误消息 |
| 生成的退款单ID | refund_id | bigint(20) |  | 否 |  | 失败时无 |
| 售后单号 | refund_no | varchar |  |  |  | 失败时无 |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "refund_id": "2809436287763742727",
    "refund_no": "RT2603240022"
}
```

### JSON

```text
{
    "code": 30402,
    "message": "订单明细id错误，请确认传值是否正确"
}
```


### vip_api_refund_query_Y：查询原始退单

| 项目 | 内容 |
|---|---|
| 分类 | 售后类 |
| 服务名 | `vip_api_refund_query_Y` |
| PHP 文件 | `vip_api_refund_query.php` |
| 文档标题 | 原始平台退单查询 |
| 描述 |  |
| 客户端路径 | 售后→售后管理→平台售后单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_api_refund_query_Y |

#### 接口说明

| 1.1 接口描述：获取ERP销售退货（换货）订单信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3注意事项：为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，相关平台规则点击这里，淘系及系统供销平台数据获取办法点击这里，拼多多请自行对接平台获取。本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/vip_api_refund_query.php |
| 正式环境 | https://openapi.huice.com/openapi/vip_api_refund_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>   require_once('../WdtClient.php');<br>   $c = new WdtClient;<br>   $c->sid = '';<br>   $c->appkey = '';<br>   $c->appsecret = "";<br>   $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/vip_api_refund_query.php';<br><br>   $c->putApiParam('start_time','2026-03-01 02:33:30');<br>   $c->putApiParam('end_time','2026-03-05 02:34:30');<br>   $c->putApiParam('refund_no','20238851089900');<br><br>   $json = $c->wdtOpenApi();<br>   var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 描述 | 是否必填 |
| --- | --- | --- | --- |
| 开始时间 | start_time | 开始时间 |  |
| 结束时间 | end_time | 结束时间 |  |
| 时间条件类型 | time_type | 1：修改时间 2：申请退款时间 。不传按照修改时间获取数据 |  |
| 平台售后单号 | refund_no | 平台售后单号   单独查询可不传时间范围 |  |
| 物流单号 | logistics_no | 物流单号 |  |
| 平台id | platform_id | 平台id，映射表点击文档中心查看 |  |
| 店铺id | shop_id | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |
| 店铺编号 | shop_no | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |
| 平台订单号 | tid | 平台原始单号，支持批量查询 用英文逗号隔开 最多支持查询单号上限为200 |  |
| 平台子单号 | oid | 平台原始子单号 |  |
| 分页大小 | page_size | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100，使用举例单击这里 | 否 |
| 页号 | page_no | 页号，不传默认从0页开始 | 否 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | varchar | 255 | 是 | 错误信息 |
| 条数 | total_count | varchar | 255 | 是 | 符合查询条件的总数量，只有page_no = 0 时才有值 |
| 当前页的退换单数据 | trade_list | data[] |  | 是 | 业务数据的一级节点，数组形式的订单数据，需要循环读取 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "trade_list": [<br>        {<br>            "refund_no": "20238851089900",<br>            "platform_id": "127",<br>            "status": 2,<br>            "tid": "207131222343423",<br>            "shop_id": "332",<br>            "type": 1,<br>            "reason": "不想要了",<br>            "refund_amount": "16.0000",<br>            "refund_time": "2025-12-31 00:00:08",<br>            "actual_refund_amount": "16.0000",<br>            "num": "0.0000",<br>            "logistics_name": "1688官方直送货运单",<br>            "logistics_no": "Lx131112033920234",<br>            "remark": "北京",<br>            "modified": "2026-03-04 16:43:19",<br>            "current_phase_timeout": null,<br>            "refund_mask": 0,<br>            "is_aftersale": 0,<br>            "goods_list": [<br>                {<br>                    "oid": "2071134342345120a",<br>                    "tid": "207131222343423",<br>                    "platform_id": "127",<br>                    "refund_no": "20238851089900",<br>                    "status": 2,<br>                    "num": "10.0000",<br>                    "total_amount": "1000.0000",<br>                    "remark": "",<br>                    "goods_id": "49",<br>                    "goods_no": "0201004500",<br>                    "goods_name": "260210的货品名称",<br>                    "spec_id": "64",<br>                    "spec_no": "0201004502",<br>                    "spec_name": "260210的谷歌名称",<br>                    "modified": "2026-03-04 16:43:19"<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | Y字段 | Y 父级字段 | Y类型 | Y枚举 | 是否必须 | 默认值 | 是否可变更 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 原始退单号 | refund_no |  | string |  | 是 |  | 否 |
| 平台id | platform_id |  | int(11) | 点击查看平台ID详情 | 是 |  | 否 |
| 平台退单状态 | status |  | tinyint(4) | 平台状态：1取消退款,2已申请退款,3等待退货,4等待收货,5退款成功,7拒绝售后申请，待买家修改,8商家发出商品,待买家签收,9待商家发出补寄/换新商品 | 是 |  | 是 |
| 原始订单号 | tid |  | string |  | 是 |  | 否 |
| 店铺id | shop_id |  | int(11) | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 | 是 |  | 否 |
| 店铺编号 | shop_no |  | string | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 | 是 |  | 是 |
| 退款类型 | type |  | tinyint(4) | 退款类型：0.无 1.退款（未发货退款） 2.退货 3.换货 4.退款不退货 5 拒收退货 6 投诉退款 7 补寄 8 维修退款 9 其他退款 11 已发货仅退款 40 三无包裹 | 是 |  | 否 |
| 退款阶段 | 无 |  | tinyint(4) | 退款阶段 0售前和售中 1售后 | 是 |  | 否 |
| 退款原因 | reason |  | string |  | 是 |  | 是 |
| 申请退款金额 | refund_amount |  | decimal(19, 4) |  | 是 |  | 是 |
| 申请退款时间 | refund_time |  | datetime |  | 是 |  | 是 |
| 退款成功金额 | actual_refund_amount |  | decimal(19, 4) |  | 是 |  | 否 |
| 退款成功时间 | current_phase_timeout |  | datetime | 完成后部分平台有，没有的传null | 否 |  | 否 |
| 退款数量 | num |  | decimal(19, 4) |  | 是 |  | 是 |
| 快递公司 | logistics_name |  | string |  | 否 | null | 是 |
| 物流单号 | logistics_no |  | string |  | 否 | null | 是 |
| 备注 | remark |  | string |  | 是 |  | 是 |
| 最后修改时间 | modified |  | datetime |  | 是 |  | 是 |
| 是否售后退款单据 | is_aftersale |  | int | 是否是售后退款单据 0 否 1 是 |  |  |  |
| 标记掩码 | refund_mask |  | int |  | 是 | 0 | 否 |
| 明细货品列表 | goods_list |  | array[] |  | 是 |  |  |
| 原始子单号 | oid | goods_list | string |  | 是 |  | 否 |
| 平台id | platform_id | goods_list | int(11) |  | 是 |  | 否 |
| 原始单号 | tid | goods_list | string |  |  |  |  |
| 原始退单号 | refund_no | goods_list | string |  | 是 |  | 否 |
| 退单子单状态 | status | goods_list | tinyint(4) | 平台状态：1取消退款,2已申请退款,3等待退货,4等待收货,5退款成功,7拒绝售后申请，待买家修改,8商家发出商品,待买家签收,9待商家发出补寄/换新商品 | 是 |  | 是 |
| 退款数量 | num | goods_list | decimal(19, 4) |  | 是 |  | 否 |
| 分摊后总额 | total_amount | goods_list | decimal(19, 4) | 与主单一对一目前不分摊 | 是 |  | 否 |
| 备注 | remark | goods_list | string |  | 是 |  | 是 |
| 平台货品ID | goods_id | goods_list | string |  | 是 |  | 是 |
| 平台货品编码 | goods_no | goods_list | string |  | 是 |  | 是 |
| 平台货品名称 | goods_name | goods_list | string |  | 是 |  | 是 |
| 平台规格ID | spec_id | goods_list | string |  | 是 |  | 是 |
| 平台规格编码 | spec_no | goods_list | string |  | 是 |  | 是 |
| 平台规格名称 | spec_name | goods_list | string |  | 是 |  | 是 |
| 子单最后修改时间 | modified | goods_list | datetime |  | 是 |  | 是 |


#### 响应示例

### JSON

```text
{
    "code": 2180,
    "message": "start_time与end_time时间跨度不能超过最大范围"
}
```


### aftersale_stockin_confirm_Y：创建退货入库单

| 项目 | 内容 |
|---|---|
| 分类 | 售后类 |
| 服务名 | `aftersale_stockin_confirm_Y` |
| PHP 文件 | `aftersale_stockin_confirm.php` |
| 文档标题 | 创建退货入库单 |
| 描述 | 推送旺店通ERP销售退货（换货）订单对应的入库单据给旺店通ERP，推送前提旺店通ERP的退换单状态为“待收货” |
| 客户端路径 | 仓储--入库管理--退货入库单--新建 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=aftersale_stockin_confirm_Y |

#### 接口说明

| 1.1 接口描述：推送旺店通ERP销售退货（换货）订单对应的入库单据给旺店通ERP，推送前提旺店通ERP的退换单状态为“待收货” |
| --- |
| 1.2 适用版本：网页版 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/aftersale_stockin_confirm.php |
| 正式环境 | https://openapi.huice.com/openapi/aftersale_stockin_confirm.php |

| PHP | <?php<br>    require_once '../WdtClient.php';<br>    $c = new WdtClient();<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    //测试环境地址<br>    //上线时需要换成线上的<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/aftersale_stockin_confirm.php';<br><br>    $stockin_refund_info = array (<br>        "refund_no" => "RT2603170237",<br>        "outer_no" => "zd202603180001",<br>        "warehouse_id" => "240",<br>        "logistics_code" => "11111",<br>         "logistics_no" => "11111",<br>           "is_check" => "1",<br>        "detail_list"  => array( array(<br>                "spec_no" => "10022740",<br>                "stockin_num" => 2<br>            )<br>         )<br>    );<br>    $c->putApiParam('stockin_refund_info', json_encode($stockin_refund_info, JSON_UNESCAPED_UNICODE));<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
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
| 退货单列表节点 | stockin_refund_info | data |  | 是 | 请求参数的1级数据节点，包含销售退货单所有属性信息的数据节点，节点下数据字段详见下述“stockin_refund_info” |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误信息 | message | varchar | 255 | 是 | 错误信息 |
| 入库单id | stockin_id | varchar | 20 | 否 | 入库单id |
| 入库单号 | stockin_no | varchar | 20 | 否 | 入库单号 |
| 售后单id | refund_id | varchar | 20 | 否 | 售后单id |
| 系统售后单号 | refund_no | varchar | 20 | 否 | 系统售后单号 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 退换单号 | refund_no | varchar | 40 | 是 | 系统退换单的单号，默认RT开头 |
| 仓库id | warehouse_id | varchar | 40 | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看。不支持推送多个仓库编号 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看。不支持推送多个仓库编号 |
| 物流公司编号 | logistics_code | varchar | 20 | 是 | 代表物流所有属性的唯一编码，用于物流区分，ERP内支持自定义（ERP物流界面设置） |
| 物流单号 | logistics_no | varchar | 40 | 是 | 物流单号 |
| 邮费 | post_fee | decimal | (19,4) | 否 | 邮费 |
| 备注 | remark | varchar | 255 | 否 | 备注 |
| 货品列表节点 | detail_list | data[ ] |  | 是 | 请求参数的2级数据节点，包含销售退货入库单所有属性信息的数据节点，节点下数据字段详见下述“detail_list” |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec_no | varchar | 40 | 是 | 代表单品(sku)所有属性的唯一编码，ERP内单品唯一编码（sku）。推送的spec_no值在ERP货品档案必须存在，且上一层单据退换单也必须存在此编号，否则单据会创建失败。SKU概念介绍,单击这里 |
| 货位 | position_no | varchar | 20 | 否 | 商品在仓库内的位置编号，传值时货位编号为空，读ERP配置【入库开单货位优先级配置】，来决定取默认货位、上一次入库货位、ZANCUN货位其中一个货位。 |
| 批次号 | batch_no | varchar | 20 | 否 | 商品批次编号，ERP“批次管理”不存在推送的批次号，是否允许单据创建成功，并创建新的“批次号”0：否；1：是，默认是0。is_create_batch=0时，入库单推送的“批次号”ERP“批次管理不存在”，单据创建失败，并返回错误信息。is_create_batch=1时，入库单推送的“批次号”ERP“批次管理不存在，单据会创建成功，并在ERP“批次管理”创建一个新的批次，请谨慎使用此字段。 |
| 批次备注 | batch_remark | varchar | 255 | 否 | 批次备注 |
| 入库数量 | stockin_num | decimal | (19,4) | 是 | 入库数量 |
| 生产日期 | production_date | datetime |  | 否 | 生产日期，格式：yyyy-MM-dd HH:mm:ss |
| 有效期 | expire_date | datetime |  | 否 | 有效期，格式：yyyy-MM-dd HH:mm:ss |
| 备注 | remark | varchar | 255 | 否 | 备注 |


#### 响应示例

### JSON

```text
{
	"code": 0,
	"message": "",
	"stockin_id": "2807203546011795458",
	"stockin_no": "RK2603180004",
	"refund_id": "2806954438558744604",
	"refund_no": "RT2603170237"
}
```

### JSON

```text
{
	"code": 11000000,
	"message": "该售后单状态不允许入库"
}
```


## 相关页面

- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/domains/视觉制作/05-小红书风格AI生图/index|旺店通开放平台 API 知识库]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/01-旺店通API能力地图|旺店通 API 能力地图]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/02-旺店通API Skill创建指南|旺店通 API Skill 创建指南]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
