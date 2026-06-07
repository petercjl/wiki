---
title: 旺店通 订单类 API 使用手册
type: concept
created: 2026-06-03
updated: 2026-06-03
domain: ecommerce-ops
tags: [ecommerce, erp, wangdian, api]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
status: active
---

# 旺店通 订单类 API 使用手册

## 用途

本页整理旺店通开放平台 订单类 的具体接口使用方法，面向后续写代码或创建 Codex/Hermes skill。每个接口包含服务名、PHP 文件、请求地址、业务请求参数、业务响应字段、示例和注意事项。

## 本类接口

| 服务名 | 接口名 | 描述 | 客户端路径 |
|---|---|---|---|
| trade_push_Y | 创建原始订单 | ①推送销售订单给ERP ；②更新已推送成功的销售订单。 | 订单→订单管理→平台订单 |
| sales_trade_batch_change_Y | 批量订单换货 | 获取批量订单换货 | 订单→订单管理→待审核 |
| sales_trade_simple_change_Y | 单笔订单换货 | 获取单笔订单换货 | 订单→订单管理→待审核 |
| logistics_sync_query_Y | 查询物流同步 | 旺店通ERP销售订单的发货状态、物流单号等同步给其他系统，注：”查询物流同步”与“物流同步回写”两个接口配合使用，完成“销售订单发货同步”，​仅支持自有/其它平台店铺 |  |
| logistics_sync_ack_Y | 物流同步回写 | 将物流同步（发货状态、物流单号等）是否成功的结果批量回传给旺店通ERP。 |  |
| sales_trade_tags_modify_Y | 修改订单标签 | 修改订单标签 |  |
| trade_query_Y | 系统订单（系统订单查询） | 查询ERP内订单 |  |
| vip_api_trade_query_Y | 查询原始订单 | 查询原始订单 | 订单→订单管理→平台订单 |
| stockout_order_query_trade_Y | 销售出库单 | 查询平台销售出库单 |  |
| sales_trade_modify_Y | 修改系统订单 | 修改旺店通erp内订单的订单标记 |  |
| sales_trade_replenish_Y | 创建补发订单 | 创建补发订单 |  |
| stockout_order_query_trade_cancel_Y | 撤销发货的销售出库单查询 | 销售出库单是基于订单的，订单可以撤销发货。当前接口是用于查询历史的撤销的已发货订单数据。举例：订单JY20250001在2025-01-01 12:00:00第一次发货， 在2025-01-01 12:30:00撤销发货。 |  |
| sales_trade_batch_remark_flag_Y | 批量修改系统订单的标旗和备注 | 批量修改系统订单的标旗和备注 |  |
| xsd_self_delivery_location_callback_Y | 小时达自配送三方运力回传状态和位置接口 | 小时达自配送三方运力回传状态和位置接口 |  |
| api_trade_live_extend_query_Y | 查询直播主播信息 | 获取租户系统内平台订单的直播信息扩展 |  |
| logistics_multi_query_Y | 查询多物流单号 | 获取旺店通ERP多物流单号 |  |
| xsd_upload_media_Y | 小时达订单图片回传 | 小时达订单图片回传 |  |

## 接口详情

### trade_push_Y：创建原始订单

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `trade_push_Y` |
| PHP 文件 | `trade_push.php` |
| 文档标题 | 创建原始订单 |
| 描述 | ①推送销售订单给ERP ；②更新已推送成功的销售订单。 |
| 客户端路径 | 订单→订单管理→平台订单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=trade_push_Y |

#### 接口说明

| 1.1 接口描述：①推送销售订单给ERP ；②更新已推送成功的销售订单。 |
| --- |
| 1.2 注意事项：仅支持推送自有/其它平台店铺 |
| 1.3 订单更新：已推送成功的销售订单的订单状态、退款状态、订单信息变更到ERP情况比较复杂，订单变更处理办法详解， 单击这里【必看】 |
| 1.4 调用建议：建议每间隔（5~10）分钟，将商城积累的订单集中推送，每次请求包含订单条数建议不超过50条(1条订单由“trade_list+order_list”构成)，如果累积量超过了50条，分多次请求。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/trade_push.php |
| 正式环境 | https://openapi.huice.com/openapi/trade_push.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once('../WdtClient.php');<br><br>    $c = new WdtClient;<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    $c->gatewayUrl = 'https://openapi.huice.com/openapi/trade_push.php';<br><br>    $trade_list[] = array<br>    (<br>        'tid'              => 'LxTestTid'.time(),<br>        'trade_status'     => 30,<br>        'delivery_term'    => 1,<br>        'pay_status'       => 2,<br>        'trade_time'       => '0000-00-00 00:00:00',<br>        'pay_time'         => '0000-00-00 00:00:00', // 未付款情况下为0000-00-00 00:00:00<br>        'buyer_nick'       => '',<br>        'buyer_email'      => '123456234533@mail.com',<br>        'receiver_mobile'  => '13233456110',<br>        'receiver_telno'   => '1234563567',<br>        'receiver_zip'     => '0000000',<br>        'receiver_province'=>'北京',<br>        'receiver_name'    =>'亚历山大',<br>        'receiver_city'    =>'北京市',<br>        'receiver_district'=>'海淀区',<br>        'receiver_address' =>'海淀',<br>        'logistics_type'   => 4, // ems<br>        'invoice_kind'     => 0,<br>        'invoice_title'    => '',<br>        'invoice_content'  => '发票内容+',<br>        'buyer_message'    => '发最好&&&的+',<br>        'remark'           => '测试专用',<br>        'remark_flag'      => 1,<br>        'post_amount'      => 10, //邮费<br>        'paid'             => 409, //已支付金额<br>        'cod_amount'       => '0',<br>        'ext_cod_fee'      => '0',<br>        'order_list'       => array(<br>            array<br>            (<br>                'oid'            => 'LxTestOid'.time(),<br>                'status'         => 30,<br>                'refund_status'  => 0,<br>                'goods_id'       => 'E166D18BAAEA420CB132E105B3B6128A',<br>                'spec_id'        => '',<br>                'goods_no'       => '',<br>                'spec_no'        => '9787533951092',<br>                'goods_name'     => '情商是什么？——关于生活智慧的44个故事',<br>                'spec_name'      => '',<br>                'num'            => 1,<br>                'price'          => 399,<br>                'adjust_amount'  => '0', //手工调整,特别注意:正的表示加价,负的表示减价<br>                'discount'       => 0, //子订单折扣<br>                'share_discount' => '0', //分摊优惠<br>                'cid'            => '13',<br>            )<br>        )<br>    );<br><br>    $c->putApiParam('shop_id','api_test');<br>    $c->putApiParam('trade_list',json_encode($trade_list, JSON_UNESCAPED_UNICODE));<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺id | shop_id | int | 10 | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar | 50 | 否 | 代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看（shop_no与shop_id传一个即可，店铺编码优先级更高） |
| 订单列表节点 | trade_list | data[] |  | 是 | 请求参数的1级数据节点，包含销售订单所有属性信息的数据节点，节点下数据字段详见下述“trade_list” |

| JSON | {<br>    "code": 99,<br>    "message": "buyer_nick 名字不能只用一个，不同客户必须用不同的名字"<br>} |
| --- | --- |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 返回的新增订单个数 | new_count | int | 10 | 否 | 有单据新增时不为0(新建的原始单据) |
| 返回的更新订单个数 | chg_count | int | 10 | 否 | 有单据更新时不为0(在已有的原始单据上进行修改) |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 原始单号 | tid | varchar | 40 | 是 | 指商城、官网等平台的订单编号，ERP称之为原始单号，同一个sid下通过本接口新增订单的tid保证唯一。 |
| 平台状态 | trade_status | tinyint | 4 | 是 | 平台订单状态较多且涉及变更，平台订单状态：10待支付 20待尾款 30已支付 40 部分发货 50已发货 70已完成 80已退款 90已关闭(付款前取消) |
| 支付状态 | pay_status | tinyint | 4 | 否 | 平台订单付款状态:0:未付款,1:部分付款,2:已付款 |
| 发货条件 | delivery_term | tinyint | 4 | 是 | 1:款到发货,2:货到付款(包含部分货到付款),3:分期付款 |
| 下单时间 | trade_time | datetime |  | 否 | 平台订单创建时间,时间格式：yyyy-MM-dd HH:mm:ss |
| 支付时间 | pay_time | datetime |  | 是 | 平台订单付款时间,时间格式：yyyy-MM-dd HH:mm:ss，未付款订单为:0000-00-00 00:00:00 |
| 客户网名 | buyer_nick | varchar | 100 | 是 | 平台买家昵称，注意：一次推送网名相同的订单不能超过30 |
| 买家email | buyer_email | varchar | 60 | 否 | 买家email |
| 收件人 | receiver_name | varchar | 40 | 是 | 收件人姓名 |
| 省份 | receiver_province | varchar | 40 | 是 | 收件人省份，传为中文名称需与旺店通地址库匹配，点击查看 |
| 城市 | receiver_city | varchar | 40 | 是 | 收件人城市，传为中文名称需与旺店通地址库匹配，点击查看 |
| 区县 | receiver_district | varchar | 40 | 是 | 收件人区县，传为中文名称需与旺店通地址库匹配，点击查看 |
| 地址详情 | receiver_address | varchar | 256 | 是 | 收件人地址详情，传为中文名称，需与旺店通地址库匹配，点击查看，如果不传省市区，则会尝试从详细地址解析省市区，必须是空格分隔的才能解析成功，需要注意直辖市的地址格式，举例“北京 北京市 海淀区 花园路xxxx” |
| 手机 | receiver_mobile | varchar | 40 | 是 | 手机号码 |
| 电话 | receiver_telno | varchar | 40 | 否 | 电话号码 |
| 邮编 | receiver_zip | varchar | 20 | 否 | 收件人邮编 |
| 发票类别 | invoice_kind | tinyint | 4 | 否 | 0:不需要,1:普通发票,2:增值税普通发票电子,3:增值税普通发票纸质,4:增值税专用发票 |
| 发票抬头 | invoice_title | varchar | 255 | 否 | 发票抬头 |
| 发票内容 | invoice_content | varchar | 255 | 否 | 常见内容：纳税人识别号、地址、联系电话、开户银行、银行账号，按照以下格式推送，系统开发票时可解析。推送格式：纳税人识别号:xxxxxxxxxxx;地址:xxxxxxxx;联系电话:13888888888;开户银行:银行名称;银行账号:账号信息; |
| 客户备注标旗 | seller_flag | tinyint | 4 | 否 | 客户备注标旗，取值0至5对应的标旗颜色依次为灰（无标旗）、红、黄、绿、蓝、紫，不传默认0 |
| 买家备注 | buyer_message | varchar | 1024 | 否 | 买家下单时填写的订单备注 |
| 客服备注 | seller_memo | varchar | 1024 | 否 | 商家客服对订单进行的备注内容 |
| 邮费 | post_amount | decimal | (19,4) | 是 | 商家收取买家的物流或者快递费用 |
| 货到付款金额 | cod_amount | decimal | (19,4) | 是 | 货到付款金额   即cod金额 |
| 货到付款买家费用 | ext_cod_fee | decimal | (19,4) | 是 | 货到付款买家费用，扣除货到付款订单金额后，卖家仍需支付的货到付款其他金额。这个钱卖家收不回来，是快递公司直接收走，但在快递单里是要打印出来，否则快递收款就错了 |
| 其它收费 | other_amount | decimal | (19,4) | 是 | 其它应从买家收取的服务费，其他费用 |
| 最晚发货时间 | to_deliver_time | datetime |  | 否 | 最晚发货时间 |
| 已付 | paid | decimal | (19,4) | 是 | 订单已付金额，即消费者实际付款金额。传参后，系统会自动分摊到子单上。 |
| 自动流转模式 | is_auto_wms | tinyint | 1 | 否 | 是否为自动流转模式（1：是 0：不是 不传默认0），非自动流转模式一定不要传值。自动流转模式处理办法，”自动流转模式处理办法详解”)单击这里 |
| 国补标识 | biz_mask | varchar | 20 | 否 | 国补标识，固定256 |
| 仓库类型 | wms_type | tinyint |  | 否 | 非自动流转模式一定不要传值 |
| 退款状态 | refund_status | tinyint |  | 否 | 退款状态 0-无退款, 1-申请退款, 2-部分退款, 3-全部退款 |
| 保价金额 | insured_amount | decimal | (19,4) | 否 | 保价金额  不传默认为0 |
| 订单货品明细节点 | order_list | data[] |  | 是 | 货品明细列表（子订单列表）节点 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 子订单编号 | oid | varchar | 40 | 是 | 平台订单货品表主键,子订单唯一标识,同一个sid下通过本接口新增订单的oid（子订单编号）要保证唯一；如果oid重复,ERP生成系统单（递交）时会提示“订单货品数量不一致xxxxxx”.一条订单下的子订单数量建议不超过200条。 |
| 数量 | num | decimal | (19,4) | 是 | 货品数量，订单推送成功以后本字段值不能更改 |
| 单价 | price | decimal | (19,4) | 是 | 标价,折扣前的价格,可以推送价格为0的商品。订单推送成功以后本字段值不能更改 |
| 状态 | status | tinyint | 4 | 是 | 平台子订单状态，子订单状态可以和主订单不一样，比如其中一个子订单退款完成，其状态是80，但主订单仍然是待发货，可选值同trade_status |
| 退款状态 | refund_status | tinyint | 4 | 是 | 0:无退款,1:取消退款,2:已申请退款,3:等待退货,4:等待收货,5:退款成功。本字段在售前退款的时候，根据不同的场景填写不同的值，eg：申请退款值为2，取消退款值为1…… |
| 平台货品ID | goods_id | varchar | 40 | 是 | 平台系统货品（SPU）的唯一标识。goods_id不能为空，goods_id和goods_no区别与SPU、SKU概念介绍，单击这里 |
| 平台规格ID | spec_id | varchar | 40 | 否 | 平台系统单品（SKU）的的唯一标识，尽量不为空，spec_id和spec_no区别与SPU、SKU概念介绍，单击这里 |
| 货品编码 | goods_no | varchar | 40 | 否 | 平台货品SPU编码，对应ERP货品编号，尽量不为空 |
| 规格编码 | spec_no | varchar | 40 | 是 | 平台货品SKU唯一码，对应ERP商家编码，goods_no和spec_no不能同时为空 |
| 最晚发货时间 | to_deliver_time | datetime |  | 否 | 最晚发货时间 |
| 货品名称 | goods_name | varchar | 255 | 是 | 平台货品名称 |
| 规格名称 | spec_name | varchar | 100 | 否 | 平台货品规格名称 |
| 调整 | adjust_amount | decimal | (19,4) | 是 | 客服调整总金额(大于0加价，小于0减价，是折扣来源的一部分,没有传0) |
| 优惠 | discount | decimal | (19,4) | 是 | 下单总折扣，客户下单时折扣(比如促销打折，不包含客服调整、分摊折扣，没有传0) |
| 分摊优惠 | share_discount | decimal | (19,4) | 是 | 分摊总折扣，由总订单分摊而来，一般是付款时产生，如使用优惠券，没有传0。分摊优惠传值注意：例如三个商品，优惠10，分摊优惠可以是：3/3/4，或者3.33/3.33/3.34.即最后一个商品的分摊优惠使用减法计算 |
| 备注 | remark | varchar | 1024 | 否 | 货品明细备注 |
| 主播id | anchor_id | varchar | 40 | 否 |  |
| 主播名称 | anchor_name | varchar | 40 | 否 |  |


#### 响应示例

### JSON

```text
{
    'code': 0,
    'message': "",
    'new_count': 1,
    'chg_count': 0
}
```


### sales_trade_batch_change_Y：批量订单换货

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `sales_trade_batch_change_Y` |
| PHP 文件 | `` |
| 文档标题 |  |
| 描述 | 获取批量订单换货 |
| 客户端路径 | 订单→订单管理→待审核 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_batch_change_Y |

#### 接口说明

| 1.1 接口描述：订单批量换货 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：自有商城接入ERP、金蝶接入、用友接入、SAP接入等 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/sales_trade_batch_change.php |
| 正式环境 | https://openapi.huice.com/openapi/sales_trade_batch_change.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>require_once("../WdtClient.php");<br><br>$c = new WdtClient;<br>$c->sid = '';<br>$c->appkey = '';<br>$c->appsecret = "";<br>$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/sales_trade_batch_change.php';<br><br>$trade_info_list = [<br>  [<br>    "trade_id"=> "2734447459538305026",<br>    "change_info_list"=> [<br>      [<br>        "rec_id"=> "2734447459538307074",<br>        "num"=> "1",<br>        "spec_list"=> [<br>          [<br>            "spec_id"=> "2788722012439183360",<br>            "num"=>"1"<br>          ]<br>        ]<br><br>      ],<br>       [<br>        "rec_id"=> "2734447459538308098",<br>        "num"=> "1",<br>        "spec_list"=> [<br>          [<br>            "spec_id"=> "2787359232045875215",<br>            "num"=> "1"<br>          ]<br>        ]<br><br>      ]<br>    ]<br>  ]<br>];<br><br>$c->putApiParam('trade_info_list', json_encode($trade_info_list, JSON_UNESCAPED_UNICODE));<br>$json = $c->wdtOpenApi();<br>var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | Y字段 | 描述 | Y类型 | Y枚举 | 是否必须 |
| --- | --- | --- | --- | --- | --- | --- |
| 订单换货信息 | trade_info_list |  | 换货主要信息 | [ ] |  | 是 |
| 订单trade_id | trade_id | trade_info_list |  | bigint(20) |  | 是 |
| 换货参数 | change_info_list | trade_info_list |  | [ ] |  | 是 |
| 订单明细id | rec_id | change_info_list |  |  |  | 是 |
| 原订单被换商品数量 | num | change_info_list |  | decimal(19, 4) |  | 是 |
| 换出新商品信息 | spec_list | change_info_list |  | [ ] |  | 是 |
| 换出商品id | spec_id | spec_list | 货品档案的spec_id | bigint(20) |  | 是 |
| 换出数量 | num | spec_list |  | decimal(19, 4) |  | 是 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述，多个订单失败原因用 英文 分号 “;” 标识 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单编号 | trade_nos | data[varchar] | 64 | 否 |  |
| 订单id | trade_ids | data[bigint] | 20 | 否 |  |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "trade_nos": [
        "JY2508290053"
    ],
    "trade_ids": [
        "2734447459538305026"
    ]
}
```

### JSON

```text
{
    "code": 1020,
    "message": "请勿重复操作",
    "trade_nos": null,
    "trade_ids": null
}
```


### sales_trade_simple_change_Y：单笔订单换货

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `sales_trade_simple_change_Y` |
| PHP 文件 | `sales_trade_simple_change.php` |
| 文档标题 | 单笔换货 |
| 描述 | 获取单笔订单换货 |
| 客户端路径 | 订单→订单管理→待审核 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_simple_change_Y |

#### 接口说明

| 1.1 接口描述：获取单笔订单换货 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：自有商城接入ERP、金蝶接入、用友接入、SAP接入等 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/sales_trade_simple_change.php |
| 正式环境 | https://openapi.huice.com/openapi/sales_trade_simple_change.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>require_once("../WdtClient.php");<br><br>$c = new WdtClient;<br>$c->sid = '';<br>$c->appkey = '';<br>$c->appsecret = "";<br>$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/sales_trade_simple_change.php';<br><br>$trade_info = [<br><br>        'trade_id' => "2740612153277939735",<br>        'rec_id' => "2740612153282134039",<br>        'is_suite' =>0,<br>        'num'=> 1,<br>        'spec_list' => [<br>                [<br>                     'spec_id' => '2788722012439183360',<br>                     'num' => 10,<br>                     'is_suite' => 0<br>                ]<br>        ]<br>];<br><br>$c->putApiParam('trade_info', json_encode($trade_info, JSON_UNESCAPED_UNICODE));<br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 公共响应参数

| 3.3 业务请求参数 |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 名称 | 字段 | 父级字段 | 描述 | Y类型 | Y枚举 | 是否必须 | 默认值 |
| 订单主信息部分 | trade_info |  | 换货主要信息 参数trade_info举例：{"tradeId":"","src_oid":"","spec_list":[{"":""}]} | Object |  | 是 |  |
| 订单trade_id | trade_id | trade_info |  | bigint(20) |  | 是 |  |
| 订单明细id | rec_id | trade_info | is_suite =0 时，必传：换出商品为普通单品必传 | bigint(20) |  |  |  |
| 平台子单号 | src_oid | trade_info | is_suite=1 时，必传：换出商品为组合装时必传 | string |  |  |  |
| 组合装id | suite_id | trade_info | is_suite=1 时，必传：换出商品为组合装时必传 | bigint(20) |  |  |  |
| 是否为组合装 | is_suite | trade_info |  | int | 0 否 1 是 | 是 |  |
| 原订单被换商品数量 | num | trade_info |  | decimal(19, 4) |  |  |  |
| 换出新商品信息 | spec_list | trade_info |  | Array |  |  |  |
| 换出商品id | spec_id | spec_list | is_suite =0 时，为普通商品ID：spec_id ；is_suite =1 时， 为组合装商品id：suite_id | bigint(20) |  |  |  |
| 换出数量 | num | spec_list |  | decimal(19, 4) |  |  |  |
| 换出商品是否为组合装 | is_suite | spec_list |  | int | 0 否 1 是 | 是 |  |
| 出参 |  |  |  |  |  |  |  |
| 公共响应参数 |  |  |  |  |  |  |  |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |  |  |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |  |  |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |  |  |
| 业务响应参数 |  |  |  |  |  |  |  |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |  |  |
| 订单编号 | trade_nos | 数组 data[varchar(64)] |  | 否 |  |  |  |
| 订单id | trade_ids | 数组 data[bigint(20)] |  | 否 |  |  |  |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "trade_nos": [
        "JY2509150164"
    ],
    "trade_ids": [
        "2740612153277939735"
    ]
}
```

### JSON

```text
{
    "code": 2830,
    "message": "参数值无效"
}
```


### logistics_sync_query_Y：查询物流同步

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `logistics_sync_query_Y` |
| PHP 文件 | `logistics_sync_query.php` |
| 文档标题 | 查询物流同步 |
| 描述 | 旺店通ERP销售订单的发货状态、物流单号等同步给其他系统，注：”查询物流同步”与“物流同步回写”两个接口配合使用，完成“销售订单发货同步”，​仅支持自有/其它平台店铺 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=logistics_sync_query_Y |

#### 请求地址

| 1.1 接口描述：旺店通ERP销售订单的发货状态、物流单号等同步给其他系统，注：”查询物流同步”与“物流同步回写”两个接口配合使用，完成“销售订单发货同步”，仅支持自有/其它平台店铺 |
| --- |
| 1.2 调用建议：物流同步业务分两部分，一部分是数据抓取，另一部分是状态回写，建议每五分钟从待同步物流数据池中，抓取一次物流数据，每次100条，处理完成一百条之后，把成功或者失败状态回写到OMS中，如此循环，直到数据池中取不出数据为止。 |
| 1.3 注意事项：①本接口logistics_sync_query是与logistics_sync_ack（物流同步状态回写）配合调用的，调用一次logistics_sync_query获得的待同步物流信息处理完成后，需要调用logistics_sync_ack响应同步结果；<br>②测试环境如何测试物流同步请看本文档最下边的附录说明；③子母单只返回母单号，不返回子单号； |

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/logistics_sync_query.php |
| 正式环境 | https://openapi.huice.com/openapi/logistics_sync_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 |  |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键 | rec_id | bigint | 20 | 是 | 主键,用于logistics_sync_ack回写状态 |
| 原始订单 | tid | varchar | 40 | 是 | 原始订单编号，商城或平台订单号 |
| 物流单号 | logistics_no | varchar | 100 | 是 | 物流或者快递面单对应的编号 |
| 物流方式 | logistics_type | smallint | 6 | 是 | 响应值为代表物流方式的数字，数字对应的物流方式名称单击这里 |
| 发货时间 | consign_time | datetime |  | 是 | 发货时间    时间格式：yyyy-MM-dd HH:mm:ss |
| 是否拆分发货 | is_part_sync | varchar | 1 | 是 | 是否拆分发货,1:拆单发货,0:不进行拆单发货 |
| 原始子订单 | oids | varchar | 208 | 是 | 子订单编号串，以逗号(,) 分隔。如果是拆分订单，会分多条trades返回 |
| 平台ID | platform_id | smallint | 6 | 是 | 平台ID，固定值127 |
| 订单ID | trade_id | int | 11 | 是 | 订单ID |
| 物流方式名称 | logistics_name | varchar | 40 | 是 | 物流方式类型名称，（ERP设置-基本设置-物流界面的物流类型中文名称） |
| erp物流id | logistics_code_erp | varchar | 40 | 是 | 数字对应的erp物流id单击这里 |
| erp物流名称 | logistics_name_erp | varchar | 40 | 是 |  |
| 是否同步 | is_need_sync | int | 1 | 是 | 1:需要同步,0:不需要同步 |
| 同步状态 | sync_status | int | 1 | 是 | 0：等待同步（实际需要自研商城处理的数据，其他状态都可以忽略），1：提交运单信息失败，2：同步失败，3：同步成功（回收单号后也会变成这个状态），4：手动设置为同步成功，5：手动取消同步 |
| 店铺id | shop_id | int | 11 | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar | 40 | 是 | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面自定义维护查看 |
| 物流id | logistics_id | int | 11 | 是 | 默认为0 |
| 同步时间 | sync_time | datetime |  | 是 | 成功同步时间 |
| 错误码 | error_code | varchar | 200 | 是 | 默认为 ''，平台返回的错误码 |
| 错误描述 | error_msg | varchar | 200 | 是 | 默认为 ''，平台返回的错误描述 |
| 重试次数 | try_times | tinyint | 4 | 是 | 默认为1，重试计数(有些同步失败可重试) |
| 最后修改时间 | modified | datetime |  | 是 | 最后修改时间， 时间格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | datetime |  | 是 | 创建时间，时间格式：yyyy-MM-dd HH:mm:ss |
| 序列号 | sn_list | data[] |  | 是 |  |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/logistics_sync_query.php';<br><br>    $c->putApiParam('shop_no','api_test');<br>    $c->putApiParam('is_part_sync_able',0);<br>    $c->putApiParam('limit',100);<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"total_count": 1,<br>	"trades": [{<br>		"rec_id": "2778958909363191820",<br>		"shop_id": "332",<br>		"tid": "201111670112119",<br>		"logistics_no": "1111111111221",<br>		"logistics_type": 5,<br>		"delivery_term": 1,<br>		"consign_time": "2025-12-30 11:10:34",<br>		"is_part_sync": 1,<br>		"oids": "5553112233122501",<br>		"platform_id": 127,<br>		"trade_id": "2778958322735251459",<br>		"logistics_code_erp": "54",<br>		"logistics_name_erp": "中通快递",<br>		"logistics_name": "中通快递",<br>		"is_need_sync": 1,<br>		"sync_status": 0,<br>		"logistics_id": null,<br>		"description": "",<br>		"sync_time": null,<br>		"error_code": "",<br>		"error_msg": "",<br>		"try_times": 1,<br>		"modified": "2025-12-30 11:10:34",<br>		"created": "2025-12-30 11:10:34",<br>		"sn_list": []<br>	}]<br>} |
| --- | --- |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 获取条数 | limit | tinyint | 4 | 是 | 每次请求需返回发货记录条数控制，取值范围大于等于，1小于等于100，<br>limit输入值大于100时接口默认limit=100.注：数据获取同步给商城系统后，<br>一定要通过logistics_sync_ack.php回写结果，<br>否则会出现ERP发货状态不能同步到商城的情况。 |
| 店铺id | shop_id | int | 11 | 否 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 数据条数 | total_count | int | 11 | 是 | 待物流同步数据总条数 |
| 待同步物流订单信息列表 | trades | data[] |  | 否 | 响应参数的1级数据节点，包含当前页的订单待同步物流订单信<br>                息的数据节点,节点下数据字段详见下述“trades” |


#### 响应示例

### JSON

```text
{
    "code": 1007,
    "message": "店铺ID不存在"
}
```


### logistics_sync_ack_Y：物流同步回写

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `logistics_sync_ack_Y` |
| PHP 文件 | `logistics_sync_ack.php` |
| 文档标题 | 物流同步回写 |
| 描述 | 将物流同步（发货状态、物流单号等）是否成功的结果批量回传给旺店通ERP。 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=logistics_sync_ack_Y |

#### 接口说明

| 1.1 接口描述：将物流同步（发货状态、物流单号等）是否成功的结果批量回传给旺店通ERP。 |
| --- |
| 1.2 适用版本：未限制 |
| 1.3 注意事项：仅支持自有/其他平台店铺 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/logistics_sync_ack.php |
| 正式环境 | https://openapi.huice.com/openapi/logistics_sync_ack.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once('../WdtClient.php');<br><br>    $c = new WdtClient;<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/logistics_sync_ack.php';<br><br>    $order_list[] = array(<br>        'rec_id'=>1,<br>        'status'=>0,<br>        'message'=>"同步成功"<br>    );<br>    $order_list[] = array(<br>        'rec_id'=>2,<br>        'status'=>1,<br>        'message'=>"同步失败"<br>    );<br><br>    $c->putApiParam('logistics_list',json_encode($order_list, JSON_UNESCAPED_UNICODE));<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

| JSON | {<br>    "code": 1007,<br>    "message": "接口appkey已停用【解决办法：联系商务人员，重新开启接口appkey】 "<br>} |
| --- | --- |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流同步状态回传列表 | logistics_list | data[] |  | 是 | 请求参数的1级数据节点，包含订单同步状态的数据节点,节点下数据字段详见下述“logistics_list”注意 数据不要超过50条。否则容易出现超时 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 处理失败的错误列表 | errors | data | data[] | 否 | 处理失败的错误列表,当code为0且有错误信息时才非空.只列出同一批内有错误的记录.如果code=0,errors为空说明全部成功 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 回写的记录id | rec_id | int | 11 | 是 | 回写的记录id，见logistics_sync_query中rec_id |
| 回写状态 | status | tinyint | 4 | 是 | 回写状态: 0成功 1失败 |
| 相关描述信息 | message | varchar | 255 | 否 | 相关描述信息,可在erp的物流同步界面看到 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 回写的记录id | rec_id | int | 11 | 是 | 回写的记录id |
| 错误信息的描述 | error | varchar | 255 | 否 | 错误信息的描述 |


#### 响应示例

### JSON

```text
{
	"code": 0,
	"message": "",
	"errors": [{
		"rec_id": "1",
		"error": "物流同步结果回传失败,同步表不存在,packId:1"
	}]
}
```


### sales_trade_tags_modify_Y：修改订单标签

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `sales_trade_tags_modify_Y` |
| PHP 文件 | `sales_trade_tags_modify.php` |
| 文档标题 | 修改订单标签 |
| 描述 | 修改订单标签 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_tags_modify_Y |

#### 接口说明

| 1.1 接口描述：修改订单标签 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：财务系统、SAP、线下ERP、数据分析等系统的对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/sales_trade_tags_modify.php |
| 正式环境 | https://openapi.huice.com/openapi/sales_trade_tags_modify.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 必须 | 描述 |
| --- | --- | --- | --- | --- |
| 卖家账号 | sid | String | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String | 是 |  |
| 时间戳 | timestamp | int | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String | 是 | API输入参数签名结果，签名算法介绍文档中心 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/sales_trade_tags_modify.php';<br><br>    $c->putApiParam('trade_ids', '2766250315173855241');<br>    $c->putApiParam('tag_ids', '97');<br>    $c->putApiParam('type', '1');<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 描述 | Y类型 | 是否必须 |
| --- | --- | --- | --- | --- |
| 订单trade_id | trade_ids | 订单系统id, 多个订单系统id 用英文逗号分割 | String | 是 |
| 标签id | tag_ids | 标签id,多个标签id 用英文逗号分割 | String | 可选必传tag_ids和abnormal_ids必传其一 |
| 类型 | type | type =1 :添加，type =2 ,删除 | string | 是 |
| 异常 id | abnormal_ids | 异常 id 多个用英文逗号分割 | string | 可选必传tag_ids和abnormal_ids必传其一 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | Int | 11 | 是 | 状态码,0表示调用成功，其他表示失败 |
| 错误信息 | message | varchar | 255 | 是 | 错误描述 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单编号 | trade_nos | 数组 data[varchar(64)] |  | 否 |  |
| 订单id | trade_ids | 数组 data[bigint(20)] |  | 否 |  |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "trade_nos": [
        "JY2511251482"
    ],
    "trade_ids": [
        "2766250315173855241"
    ]
}
```

### JSON

```text
{
    "code": 2830,
    "message": "系统订单Id无效:276625031517385524100"
}
```


### trade_query_Y：系统订单（系统订单查询）

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `trade_query_Y` |
| PHP 文件 | `trade_query.php` |
| 文档标题 | 查询系统订单 |
| 描述 | 查询ERP内订单 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=trade_query_Y |

#### 接口说明

| 1.1 接口描述：查询ERP内订单 |
| --- |
| 1.2 时间跨度：start_time和end_time最大跨度为3天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-03 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |
| 1.5注意事项：权限校验：【店铺、仓库权限】为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，相关平台规则点击这里，淘系及系统供销平台数据获取办法点击这里，拼多多请自行对接平台获取。本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/trade_query.php |
| 正式环境 | https://openapi.huice.com/openapi/trade_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取2。 |
| 接口账号 | appkey | String |  | 是 |  |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通网页版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍文档中心 |

|  | trades |  | array[] |  |
| --- | --- | --- | --- | --- |
| 名称 | Y字段 | 父级字段 | 类型 | 枚举及 描述 |
| 系统订单id | trade_id |  | bigint(20) |  |
| 系统订单编号 | trade_no |  | varchar（64） | 默认JY开头 |
| 系统订单状态 | trade_status |  | tinyint | 4 已取消（可恢复） 5 已取消  10 未付款  25 特殊单 29 预订单 30 待审核（已支付） 35 待财审 50 待发货 51 待推送 52 推送中 53 推送失败 55 已推送 95 已发货 |
| 店铺id | shop_id |  | bigint(20) | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no |  | varchar(50) | 代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺名称 | shop_name |  | varchar(64) | 店铺名称（不返回平台店铺名称） |
| 订单类型 | trade_type |  | varchar(64) | 分销、供销、分销+供销、自定义类型 |
| 平台id | platform_id |  | bigint(20) | 点击查看平台ID详情 |
| 仓库id | warehouse_id |  | bigint(20) | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编码 | warehouse_no |  | varchar(40) | 代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库类型 | warehouse_type |  | tinyint | 0普通仓库 2分销仓 3委外仓库4自流转仓 |
| 最晚发货时间 | estimate_consign_time |  | datetime | 最晚发货时间 |
| 平台订单号 | src_tids |  | varchar(1024) | 合单后是多个平台单号 用,分隔，受限于字段长度可能截取 |
| 出库单号 | stockout_no |  | varchar(64) |  |
| 订单来源 | trade_from |  | tinyint | 1、API抓单2、手工建单3、导入4、复制订单5、接口推送6、补发订单7、展架下单8、换货订单 |
| 支付时间 | pay_time |  | datetime |  |
| 数量 | goods_count |  | decimal(19, 4) |  |
| 邮费收入 | post_amount |  | decimal(19, 4) |  |
| 预估邮资成本 | post_cost |  | decimal(19, 4) |  |
| 退款状态 | refund_status |  | tinyint | 0、无退款1、申请退款2、部分退款3、全部退款 |
| 买家备注 | buyer_message |  | varchar(1024) |  |
| 客服备注 | cs_remark |  | varchar(1024) |  |
| 线下备注 | sys_remark |  | varchar(1024) |  |
| 标旗 | remark_flag |  | tinyint |  |
| 最后修改时间 | modified |  | timestemp |  |
| 物流单号 | logistics_no |  | varchar（40） | 返回其中一个 |
| 物流公司ID | logistics_id |  | bigint(20) |  |
| 物流公司名称 | logistics_name |  | varchar（128） |  |
| 物流公司编号 | sys_logistics_code |  | varchar（64） | 响应值为代表物流方式的数字，数字对应的物流方式名称 点击这里 |
| 物流公司类型 | logistics_type |  | tinyint | 响应值为代表物流方式的数字，数字对应的物流方式名称 点击这里 |
| 物流公司类型名称 | logistics_type_name |  | varchar（128） | 物流品牌的名称 |
| 分销昵称 | fenxiao_nick |  | varchar（255） |  |
| 分销原始店铺 | fenxiao_shop_name |  | varchar（255） | 分销原始店铺 |
| 分销原始单号 | fenxiao_tid |  | varchar(255) |  |
| 分销平台ID | fenxiao_platform_id |  | bigint(20) |  |
| 分销子平台ID | fenxiao_sub_platform_id |  | bigint(20) |  |
| 收件人电话 | receiver_telno |  | varchar（255） |  |
| 建单人姓名 | creator_name |  | string(128) |  |
| 推单时间 | push_date |  | datetime |  |
| 推单单号 | push_no |  | string(40) |  |
| 客户网名 | buyer_nick |  | string(40) | 客户网名，注意：线上淘系、京东、拼多多等平台不返回 |
| 客户编码 | customer_no |  | string(40) | 客户编码 |
| 订单标签 | tags |  | 255 | 1,2,3 |
| 下单时间 | trade_time |  |  |  |
| 折扣 | discount |  | decimal(19, 4) |  |
| 应收金额 | receivable |  | decimal(19, 4) |  |
| 商家实收 | real_amount |  | decimal(19, 4) |  |
| 退款金额 | refund_amount |  | decimal(19, 4) |  |
| 买家实付 | paid |  | decimal(19, 4) |  |
| 是否打印 | is_print |  | tinyint | 0 未打印 1 已打印 |
| 发货时间 | consign_time |  | datetime |  |
| 创建时间 | created |  | datetime | 举例：2025-01-01 00:00:00 |
| 收件人省 | receiver_province |  | bigint(20) | 目前不返回，实际省市区信息查看receiver_area字段 |
| 收件人市 | receiver_city |  | bigint(20) | 目前不返回，实际省市区信息查看receiver_area字段 |
| 收件人区 | receiver_district |  | bigint(20) | 目前不返回，实际省市区信息查看receiver_area字段 |
| 收件人省市区拼接 名称 | receiver_area |  | string(128) |  |
| 收件人手机号 | receiver_mobile |  | string(128) |  |
| 收件人地址 | receiver_address |  | string(128) |  |
| 收件人姓名 | receiver_name |  | string(128) |  |
| 业务员id | salesman_id |  | int(11) | 业务员id |
| 代发邮费 | oms_post_amount |  | decimal | 代发邮费 |
| 采购成本 | oms_purchase_amount |  | decimal | 采购成本 |
| 佣金 | oms_employ_amount |  | decimal | 佣金 |
| 物流单打印时间 | print_time |  | datetime | 物流单打印时间 |
| 收件人省名称 | receiver_province_name |  | string | 收件人省名称 |
| 收件人市名称 | receiver_city_name |  | string | 收件人市名称 |
| 收件人区名 | receiver_district_name |  | string | 收件人区名称 |
| 货品列表 | goods_list |  | array[] |  |
| 订单明细id | rec_id | goods_list | bigint |  |
| 平台子单号 | src_oid | goods_list | varchar(64) |  |
| 平台id | platform_id | goods_list | bigint |  |
| 平台单号 | src_tid | goods_list | varchar(64) |  |
| 货品明细id | spec_id | goods_list | bigint |  |
| 商家编码 | spec_no | goods_list | varchar(255) |  |
| 货品编码 | goods_no | goods_list | varchar(255) |  |
| 规格码 | spec_code | goods_list | varchar(255) |  |
| 系统规格图片链接 | spec_img_url | goods_list | varchar(1024) | 系统规格图片链接 |
| 下单数量 | num | goods_list | decimal(19, 4) |  |
| 分摊邮费 | share_post | goods_list | decimal(19, 4) |  |
| 分摊单价 | share_price | goods_list | decimal(19, 4) | 分摊价格，扣减优惠之后，不加邮费收入的单价 |
| 分摊后总价 | share_amount | goods_list | decimal(19, 4) |  |
| 分摊优惠 | share_discount | goods_list | decimal(19, 4) |  |
| 调整金额，手工改价金额 | adjust | goods_list | decimal(19, 4) | 手工改价金额 手工调整价,正数为加价,负数为减价 |
| 折扣金额 | discount | goods_list | decimal(19, 4) | 折扣金额 |
| 货品重量 | weight | goods_list | decimal(19, 4) | 单个货品重量 |
| 退款状态 | refund_status | goods_list | tinyint | 0-无退款,1-取消退款,2-已申请退款,3-等待退货,4-等待收货,5-退款成功 |
| 组合装编码 | suite_no | goods_list | varchar(255) |  |
| 组合装数量 | suite_num | goods_list | decimal(19, 4) |  |
| 赠品方式 | gift_type | goods_list | tinyint | 0、非赠品1、自动赠送 2、手工赠送  5 平台赠品 |
| 备注 | remark | goods_list | varchar(255) |  |
| 最后修改时间 | modified | goods_list | timestemp |  |
| 平台货品名称 | api_goods_name | goods_list | varchar(255) |  |
| 平台规格名称 | api_spec_name | goods_list | varchar(255) |  |
| 货品id | goods_id | goods_list | bigint |  |
| 货品自定义属性1 | goods_prop1 | goods_list | varchar(255) | 货品自定义属性1 |
| 货品自定义属性2 | goods_prop2 | goods_list | varchar(255) | 货品自定义属性2 |
| 货品自定义属性3 | goods_prop3 | goods_list | varchar(255) | 货品自定义属性3 |
| 货品自定义属性4 | goods_prop4 | goods_list | varchar(255) | 货品自定义属性4 |
| 货品自定义属性5 | goods_prop5 | goods_list | varchar(255) | 货品自定义属性5 |
| 货品自定义属性6 | goods_prop6 | goods_list | varchar(255) | 货品自定义属性6 |
| 单品自定义属性1 | prop1 | goods_list | varchar(255) | 单品自定义属性1 |
| 单品自定义属性2 | prop2 | goods_list | varchar(255) | 单品自定义属性2 |
| 单品自定义属性3 | prop3 | goods_list | varchar(255) | 单品自定义属性3 |
| 单品自定义属性4 | prop4 | goods_list | varchar(255) | 单品自定义属性4 |
| 单品自定义属性5 | prop5 | goods_list | varchar(255) | 单品自定义属性5 |
| 单品自定义属性6 | prop6 | goods_list | varchar(255) | 单品自定义属性6 |
| 单品自定义属性7 | prop7 | goods_list | varchar(255) | 单品自定义属性7 |
| 单品自定义属性8 | prop8 | goods_list | varchar(255) | 单品自定义属性8 |
| 单品自定义属性9 | prop9 | goods_list | varchar(255) | 单品自定义属性9 |
| 单品自定义属性10 | prop10 | goods_list | varchar(255) | 单品自定义属性10 |
| 商品名称 | goods_name | goods_list | varchar(255) |  |
| 规格名称 | spec_name | goods_list | varchar(255) |  |
| 组合装名称 | suite_name | goods_list | varchar(255) |  |
| 组合装ID | suite_id | goods_list | bigint(20) |  |
| 平台货品ID | platform_goods_id | goods_list | varchar(128) |  |
| 平台货品编码 | api_goods_no | goods_list | varchar(255) |  |
| 平台规格ID | platform_spec_id | goods_list | varchar(128) |  |
| 平台规格编码 | api_spec_no | goods_list | varchar(255) |  |
| 买家实付 | paid | goods_list | decimal(19, 4) |  |
| 商品单价 | price | goods_list | decimal(19, 4) |  |
| 组合装价格 | suite_amount | goods_list | decimal(19, 4) |  |
| 主播Id | anchor_id | goods_list | varchar(64) |  |
| 主播名称 | anchor_name | goods_list | varchar(64) |  |
| 组合装拆合标识 | suit_flag | goods_list | tinyint | 0标识无拆合，其他标识有拆分合并换货 |
| 订单明细发货状态 | trade_status | goods_list | tinyint | 0 未发货 1 已发货 |
| 订单明细发货类型 | trade_status_type | goods_list | tinyint | 0：无 1 平台发货 2 erp系统发货 |
| 是否包装 | is_package | goods_list | tinyint | 0 否 1 是 包装 |
| 货品成本 | goods_cost | goods_list | decimal | 是 |
| 货位批次明细数据 | position_list | details_list |  |  |
| 出库单明细或者订单明细Id | stockout_order_detail_id | position_list | string | 出库单明细或者订单明细Id |
| 入库单明细id | stock_spec_detail_id | position_list | string | 入库单明细id |
| 货位主键 | rec_id | position_list | string | 货位主键 |
| 货位ID | position_id | position_list | string | 货位ID |
| 货位编号 | position_no | position_list | string | 货位编号 |
| 批次 | batch_no | position_list | string | 批次 |
| 有效期 | expire_date | position_list | datetime | 有效期 |
| 生产日期 | production_date | position_list | datetime | 生产日期 |
| 出库数量 | num | position_list | decimal | 出库数量 |
| 最后修改时间 | modified | position_list | datetime | 最后修改时间 |
| 异常列表 | abnormal_list | position_list | array[] |  |
| 异常Code值 | abnormal_code | abnormal_list | int | 异常的Code值 |
| 异常名称 | abnormal_name | abnormal_list | string(64) | 异常名称 |
| 异常类型 | abnormal_type | abnormal_list | tinyint | 异常类型 1 系统异常 2 客户自定义异常 |
| 代发邮费 | oms_post_amount |  | decimal | 代发邮费 |
| 采购成本 | oms_purchase_amount |  | decimal | 采购成本 |
| 物流列表 | logistics_list |  | array[] | 物流列表 |
| 物流单号 | logistics_no | logistics_list | string | 物流单号 |
| 关联物流单 | related_logistics_no | logistics_list | string | 若parent_child_flag=1，则该字段为母单号 |
| 物流公司名称 | logistics_name | logistics_list | string | 物流公司名称 |
| 重量 | weight | logistics_list | decimal(19, 4) | 重量 |
| 邮资 | post_cost | logistics_list | decimal(19, 4) | 邮资 |
| 打印状态 | print_status | logistics_list | int | 0-未打印 1-已打印 |
| 创建时间 | created | logistics_list | datetime | 创建时间 |
| 子母单标识 | parent_child_flag | logistics_list | int | 0-普通单 1-子母单 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/trade_query.php';<br><br>    //添加查询参数<br>    $c->putApiParam('start_time','2018-08-01 00:00:00');<br>    $c->putApiParam('end_time','2018-08-11 00:00:00');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "trades": [<br>        {<br>            "trade_id": "2812636489043673101",<br>            "trade_no": "JY2604020001",<br>            "trade_status": 95,<br>            "shop_id": "332",<br>            "shop_name": "renmaolin-test",<br>            "platform_id": "127",<br>            "warehouse_id": "38",<br>            "warehouse_type": 0,<br>            "src_tids": "20073154135362858",<br>            "stockout_no": "",<br>            "trade_from": 1,<br>            "pay_time": "2026-04-02 20:25:14",<br>            "goods_count": "102.0000",<br>            "post_amount": "100.0000",<br>            "post_cost": "20.0000",<br>            "refund_status": 0,<br>            "buyer_message": "https:\/\/picx.zhimg.com\/v2-ab23d513fab6abd0a27cda9ba9676383_720w.jpg?source=172ae18b",<br>            "cs_remark": " 已建售后单",<br>            "sys_remark": "",<br>            "remark_flag": 6,<br>            "modified": "2026-04-07 11:25:11",<br>            "logistics_no": "1e708-c28c-44de-8e59-5cc85a65b7ee",<br>            "logistics_id": "2688069327617261580",<br>            "logistics_name": "中通快递1",<br>            "logistics_type": "5",<br>            "logistics_type_name": "中通快递",<br>            "sys_logistics_code": "54",<br>            "tags": "",<br>            "fenxiao_platform_id": "0",<br>            "fenxiao_sub_platform_id": 0,<br>            "fenxiao_nick": "",<br>            "fenxiao_tid": "",<br>            "fenxiao_shop_name": "",<br>            "trade_time": "2026-04-02 20:25:14",<br>            "order_type": 0,<br>            "receiver_name": "亚历山大",<br>            "receiver_address": "天津 天津市 null",<br>            "receiver_mobile": "13233456110",<br>            "receiver_telno": "",<br>            "receiver_area": "北京 北京市 海淀区",<br>            "receiver_province": 110000,<br>            "receiver_city": 110100,<br>            "receiver_district": 110108,<br>            "receiver_province_name": "北京",<br>            "receiver_city_name": "北京市",<br>            "receiver_district_name": "海淀区",<br>            "receiver_street_name": "",<br>            "paid": "590.0000",<br>            "print_time": "0000-00-00 00:00:00",<br>            "is_print": 0,<br>            "consign_time": "2026-04-02 09:34:29",<br>            "estimate_consign_time": "0000-00-00 00:00:00",<br>            "push_date": "0000-00-00 00:00:00",<br>            "push_no": "",<br>            "trade_type": "",<br>            "discount": "70.0000",<br>            "receivable": "226583258.4000",<br>            "real_amount": "226583258.4000",<br>            "refund_amount": "0.0000",<br>            "salesman_id": 0,<br>            "created": "2026-04-02 09:33:15",<br>            "oms_post_amount": "0.0000",<br>            "oms_purchase_amount": "0.0000",<br>            "oms_employ_amount": "0.0000",<br>            "plan_deliver_time": "2026-04-04 20:25:14",<br>            "customer_no": "",<br>            "creator_id": "system",<br>            "creator_name": "system",<br>            "buyer_nick": "33",<br>            "serial_no": "",<br>            "goods_list": [<br>                {<br>                    "prop1": "",<br>                    "prop2": "",<br>                    "prop3": "",<br>                    "prop4": "",<br>                    "prop5": "",<br>                    "prop6": "",<br>                    "prop7": "",<br>                    "prop8": "",<br>                    "prop9": "",<br>                    "prop10": "",<br>                    "rec_id": "2812636489047868429",<br>                    "src_oid": "20157963331820",<br>                    "platform_id": "127",<br>                    "src_tid": "20073154135362858",<br>                    "spec_id": "2806920974736294919",<br>                    "suite_no": "",<br>                    "goods_no": "y23y24111100",<br>                    "spec_code": "",<br>                    "num": "102.0000",<br>                    "share_post": "100.0000",<br>                    "share_amount": "226583158.4000",<br>                    "share_price": "2221403.5137",<br>                    "share_discount": "40.0000",<br>                    "weight": "0.0000",<br>                    "refund_status": 0,<br>                    "spec_no": "y23y24111100",<br>                    "suite_num": "0.0000",<br>                    "gift_type": 0,<br>                    "remark": "这是提行备注",<br>                    "modified": "2026-04-02 09:34:34",<br>                    "api_goods_name": "260311的zhhz货品名称",<br>                    "api_spec_name": "260311的zhz规格名称",<br>                    "goods_id": "2806920974732099591",<br>                    "goods_name": "260311的zhhz货品名称",<br>                    "spec_name": "260311的zhz规格名称",<br>                    "suite_name": "",<br>                    "suite_id": "0",<br>                    "platform_goods_id": "y23y24111100",<br>                    "api_goods_no": "y23y24111100",<br>                    "platform_spec_id": "y23y2411100",<br>                    "api_spec_no": "y23y24111100",<br>                    "commission": "0",<br>                    "paid": "590.0000",<br>                    "adjust": "0.0000",<br>                    "discount": "70.0000",<br>                    "price": "2221404.2000",<br>                    "suite_amount": "0.0000",<br>                    "anchor_id": "",<br>                    "anchor_name": "",<br>                    "suit_flag": 0,<br>                    "spec_img_url": "",<br>                    "trade_status": 1,<br>                    "trade_status_type": 2,<br>                    "is_package": 0,<br>                    "oms_post_amount": "0.0000",<br>                    "oms_purchase_amount": "0.0000",<br>                    "goods_cost": "56876.0160",<br>                    "goods_prop1": "",<br>                    "goods_prop2": "",<br>                    "goods_prop3": "",<br>                    "goods_prop4": "",<br>                    "goods_prop5": "",<br>                    "goods_prop6": "",<br>                    "position_list": [<br><br>                    ]<br>                }<br>            ],<br>            "abnormal_list": [<br>                {<br>                    "abnormal_code": 0,<br>                    "abnormal_name": "地址异常",<br>                    "abnormal_type": 2<br>                }<br>            ],<br>            "logistics_list": [<br>                {<br>                    "logistics_no": "1e708-c28c-44de-8e59-5cc85a65b7ee",<br>                    "related_logistics_no": "",<br>                    "logistics_name": "中通快递1",<br>                    "weight": "0.0000",<br>                    "post_cost": "0.0000",<br>                    "print_status": 0,<br>                    "created": "2026-04-02 09:34:29",<br>                    "parent_child_flag": 0<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务请求参数

| 名称 | 字段 | 类型 | 必须 | 描述 |
| --- | --- | --- | --- | --- |
| 开始时间 | start_time | String | 可选必传 | 修改起始时间，若无订单号/物流单号，则为必填。示例：“ 2021-11-11 00:00:00” |
| 结束时间 | end_time | String | 可选必传 | 修改结束时间，上同开始时间。示例：“ 2021-11-11 01:00:00”  开始时间和结束时间最大间隔为3天 |
| 仓库id | warehouse_id | int | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 订单状态 | status | int | 否 | 若多个状态则以“，”隔开。订单状态: 4 已取消（可恢复） 5 已取消  10 未付款  25 特殊单 29 预订单  30 已支付  35 待财审 50 待发货 51 待推送  52 推送中  53 推送失败 55  已推送 95 已发货 |
| 订单编号 | trade_no | String | 可选必传 | 订单编号，默认JY开头。多个订单编号之间使用英文逗号分隔,长度限制200，单独查询可不传时间范围 |
| 店铺id | shop_id | int | 否 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar(50) | 否 | 代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 仓库编码 | warehouse_no | varchar(40) | 否 | 代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 物流单号 | logistics_no | String | 否 | 物流单号 |
| 原始单号 | src_tid | String | 可选必传 | 原始单号, 多个原始单号之间使用英文逗号分隔（字符长度不超过200）单独查询可不传时间范围 |
| 订单来源 | trade_from | int | 否 | 1-平台抓单 2-手工建单 3-EXCEL导入 6-补发订单 7-展架下单 8-换货订单 9-现款销售 10-补寄订单 11-维修订单 |
| 时间类型入参 | time_type | int | 否 | 1、最后修改时间   2、下单时间    默认为1 |
| 是否返回货位批次信息 | is_position | int | 否 | 是否返回货位批次信息。1：返回position_list节点数据   0：不返回position_list节点数据，默认为0 |
| 系统订单id | trade_ids | String | 可选必传 | 系统订单id, 多个系统订单id之间使用英文逗号分隔 |
| 标旗列表 | remark_flags | String | 否 | 查询对应标旗的数据，标旗取值为0到5,多个之间用逗号,分隔。传入 0 表示无标旗， 1 红色 2 黄色 3 绿色 4 蓝色 5 紫色 |
| 分页大小 | page_size | int | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100，使用举例 |
| 页号 | page_no | int | 否 | 页号，不传默认从0页开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 条数 | total_count | varchar | 255 | 是 | 符合查询条件的总数量，只有page_no = 0 时才有值。 |
| 原始单节点 | trades | data[] |  | 是 | 业务数据的一级节点，数组形式的订单数据，需要循环读取。 |


#### 响应示例

### JSON

```text
{
    "code": 2900,
    "message": "时间范围与订单编号不能全部为空"
}
```


### vip_api_trade_query_Y：查询原始订单

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `vip_api_trade_query_Y` |
| PHP 文件 | `vip_api_trade_query.php` |
| 文档标题 | 查询原始订单 |
| 描述 | 查询原始订单 |
| 客户端路径 | 订单→订单管理→平台订单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_api_trade_query_Y |

#### 接口说明

| 1.1 接口描述：查询平台原始订单 |
| --- |
| 1.2注意事项：权限校验：【店铺、仓库权限】为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，相关平台规则点击这里，淘系及系统供销平台数据获取办法点击这里，拼多多请自行对接平台获取。本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/vip_api_trade_query.php |
| 正式环境 | https://openapi.huice.com/openapi/vip_api_trade_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/vip_api_trade_query.php';<br><br>    $c->putApiParam('start_time','2018-01-01 00:00:00');<br>    $c->putApiParam('end_time','2018-01-01 01:00:00');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 字段 | 名称 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- |
| tid | 原始单号 |  |  | 原始单号，支持批量查询 用英文逗号隔开 最多支持查询单号上限为200 支持单独查询，不校验时间范围 |
| start_time | 开始时间 |  |  | 修改起始时间 |
| end_time | 结束时间 |  |  | 修改结束时间  最大间隔为 30 天 |
| shop_id | 店铺id |  |  | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| shop_no | 店铺编号 |  |  | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| page_size | 分页大小 |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100，使用举例单击这里 |
| page_no | 页号 |  | 否 | 页号，不传默认从0页开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 条数 | total_count | varchar | 255 | 是 | 符合查询条件的总数量，只有page_no = 0 时才有值。 |
| 原始单节点 | trade_list | data[] |  | 是 | 业务数据的一级节点，数组形式的订单数据，需要循环读取。 |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"total_count": 1,<br>	"trade_list": [{<br>		"tid": "624995754000-001",<br>		"platform_id": "127",<br>		"trade_status": 70,<br>		"shop_id": "353",<br>		"delivery_term": 1,<br>		"guarantee_mode": 1,<br>		"pay_status": 2,<br>		"pay_method": 1,<br>		"pay_time": "2025-10-30 12:56:30",<br>		"trade_time": "2025-10-30 12:56:25",<br>		"end_time": null,<br>		"goods_count": "1.0000",<br>		"goods_amount": "110.0000",<br>		"post_amount": "0.0000",<br>		"discount": "0.0000",<br>		"paid": "0.0000",<br>		"receivable": "110.0000",<br>		"received": "110.0000",<br>		"currency": "",<br>		"refund_status": 0,<br>		"buyer_message": "",<br>		"remark": "",<br>		"remark_flag": 0,<br>		"modified": "2025-11-01 22:38:32",<br>		"receiver_province": "440000",<br>		"receiver_city": "440300",<br>		"receiver_district": "440303",<br>		"receiver_name": "测试",<br>		"receiver_address": "地址测试",<br>		"receiver_mobile": "13855559999",<br>		"receiver_area": "广东省 深圳市 罗湖区",<br>		"created": "2025-11-01 22:38:32",<br>		"goods_list": [{<br>			"oid": "624995754000-001-14600-55730",<br>			"platform_id": "127",<br>			"tid": "624995754000-001",<br>			"status": 30,<br>			"end_time": null,<br>			"goods_id": "14600",<br>			"goods_no": "RM633589993472",<br>			"goods_name": "八百秀才 英德红茶 花果香型250g",<br>			"spec_id": "14600",<br>			"spec_no": "RM633589993472",<br>			"sku_code": "",<br>			"spec_name": "",<br>			"num": "1.0000",<br>			"price": "110.0000",<br>			"share_amount": "0.0000",<br>			"refund_status": 0,<br>			"remark": "",<br>			"shipment_box": "",<br>			"modified": "2025-11-01 22:38:32"<br>		}],<br>		"discount_list": null<br>	}]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 必须 | 描述 |
| --- | --- | --- | --- | --- |
| 平台订单号 | tid | string | 是 |  |
| 平台id | platform_id | int(11) | 是 | 点击查看平台ID详情 |
| 平台订单状态 | trade_status | int(11) | 是 | 平台订单状态：10 未确认  20待尾款 30已支付 40 部分发货 50已发货 60 已签收 70已完成 80已退款 90已关闭(付款前取消) |
| 系统状态 | process_status | int | 是 | 10-待递交  19-预递交 20-已递交  70-已取消 （19是递交的中间态，可忽略） |
| 店铺id | shop_id | int(11) | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | string | 是 | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 发货条件 | delivery_term | tinyint(4) | 是 | 发货条件 1款到发货 2货到付款(包含部分货到付款) 3分期付款 4挂帐单 |
| 担保交易类别 | guarantee_mode | tinyint(4) | 是 | 担保交易类别：1担保交易2非担保交易3非担保在线交易 |
| 支付状态 | pay_status | tinyint(4) | 是 | 支付状态：0未付款 1部分付款 2已付款 |
| 支付方式 | pay_method | tinyint(4) | 是 | 支付方式: 1在线转帐 2现金，3银行转账，4邮局汇款 5预付款 6刷卡 7支付宝 8微信支付 0 未知 |
| 支付时间 | pay_time | datetime | 是 | 时间格式：yyyy-MM-dd HH:mm:ss |
| 下单时间 | trade_time | datetime | 是 | 时间格式：yyyy-MM-dd HH:mm:ss |
| 完成时间 | end_time | datetime | 否 | 部分平台有，没有的可以传null |
| 发票类型 | invoice_type | string | 是 | 0不需要   1普通发票  2普通增值税发票   3专用增值税发票  4需要开票 |
| 发票抬头 | invoice_title | string | 是 | 发票抬头 |
| 发票内容 | invoice_content | string | 是 | 发票内容 |
| 货品数量 | goods_count | decimal(19, 4) | 是 |  |
| 货款 | goods_amount | decimal(19, 4) | 是 | 未除优惠 |
| 邮费 | post_amount | decimal(19, 4) | 是 |  |
| 优惠 | discount | decimal(19, 4) | 是 |  |
| 实付 | paid | decimal(19, 4) | 是 |  |
| 应收 | receivable | decimal(19, 4) | 是 |  |
| 已收 | received | decimal(19, 4) | 是 |  |
| 币种 | currency | string | 否 |  |
| 退款状态 | refund_status | decimal(19, 4) | 是 | 退款状态： 0.无退款 1.申请退款 2.部分退款 3.全部退款 |
| 买家备注 | buyer_message | string | 是 |  |
| 客服备注 | remark | string | 是 |  |
| 标旗 | remark_flag | int(11) | 是 | 标旗（0灰、1 红、2 黄、3 绿、4 蓝、5 紫 ） |
| 最后修改时间 | modified | datetime | 是 | 时间格式：yyyy-MM-dd HH:mm:ss |
| 收件人省 | receiver_province | int(11) | 是 |  |
| 收件人市 | receiver_city | int(11) | 是 |  |
| 收件人区 | receiver_district | int(11) | 是 |  |
| 收件人省市区拼接 名称 | receiver_area | string | 是 |  |
| 收件人手机号 | receiver_mobile | string | 是 |  |
| 收件人地址 | receiver_address | string | 是 |  |
| 收件人姓名 | receiver_name | string | 是 |  |
| 创建时间 | created | datetime | 是 |  |
| 明细货品列表 | goods_list | array[] | 是 |  |

| 名称 | 字段 | 类型 | 必须 | 描述 |
| --- | --- | --- | --- | --- |
| 平台子订单号 | oid | string | 是 |  |
| 平台id | platform_id | int(11) | 是 |  |
| 平台订单号 | tid | string | 是 |  |
| 平台子单状态 | status | int(11) | 是 | 平台子单状态：10未确认 20待尾款 30待发货 40部分发货 50已发货 60已签收 70已完成 80已退款 90已关闭 |
| 子单完成时间 | end_time | datetime | 否 | 部分平台有，没有的可以传null |
| 平台货品表主键 | platform_goods_id | int(11) | 是 | 平台货品表主键 |
| 平台货品ID | goods_id | string | 是 |  |
| 平台货品编码 | goods_no | string | 是 |  |
| 平台货品名称 | goods_name | string | 是 |  |
| 平台规格ID | spec_id | string | 是 |  |
| 平台规格编码 | spec_no | string | 是 |  |
| 平台规格码 | sku_code | string | 是 |  |
| 平台规格名称 | spec_name | string | 是 |  |
| 货品数量 | num | decimal(19, 4) | 是 |  |
| 平台单价 | price | decimal(19, 4) | 是 |  |
| 分摊应收 | share_amount | decimal(19, 4) | 是 |  |
| 退款状态 | refund_status | tinyint(4) | 是 | 退款状态： 0.无退款 1.取消退款 2.已申请退款 3.等待退货 4.等待收货 5.退款成功 |
| 子单备注 | remark | string | 是 |  |
| 子单最后修改时间 | modified | datetime | 是 | 时间格式：yyyy-MM-dd HH:mm:ss |
| 优惠信息列表 | discount_list | array[] | 否 | 优惠明细数据列表 |

| 名称 | 字段 | 类型 | 必须 | 描述 |
| --- | --- | --- | --- | --- |
| 优惠明细id | rec_id | bigint | 否 |  |
| 平台id | platform_id | int(11) | 否 |  |
| 平台订单单号 | tid | string | 否 |  |
| 平台订单子单号 | oid | string | 否 |  |
| 优惠类型 | type | int | 否 | 优惠类型 来源于平台 |
| 是否是优惠卷 | is_bonus | int | 否 | 0 否 1 是 |
| 优惠名称 | name | string | 否 |  |
| 优惠明细描述 | detail | string | 否 |  |
| 金额 | amount | decimal(19, 4) | 否 |  |
| 平台优惠的唯一标识 | sn | string |  |  |
| 创建时间 | created | datetime | 否 | 时间格式：yyyy-MM-dd HH:mm:ss |


#### 响应示例

### JSON

```text
{
    "code": 1060,
    "message": "充值余额为0或应用已欠费，请联系商务充值 "
}
```


### stockout_order_query_trade_Y：销售出库单

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `stockout_order_query_trade_Y` |
| PHP 文件 | `stockout_order_query_trade.php` |
| 文档标题 | 销售出库单 |
| 描述 | 查询平台销售出库单 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stockout_order_query_trade_Y |

#### 接口说明

| 1.1 接口描述：查询销售出库单// Y目前没有走销售出库流程 目前没有，直接使用已发货的订单作为替代 |
| --- |
| 1.2 时间跨度：时间跨度：start_time和end_time最大跨度为30天。建议根据获取数据量的多少适当减小时间跨度。 |
| 1.5注意事项：权限校验：【店铺、仓库权限】为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台订单数据，相关平台规则点击这里，淘系及系统供销平台数据获取办法点击这里，拼多多请自行对接平台获取。本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stockout_order_query_trade.php |
| 正式环境 | https://openapi.huice.com/openapi/stockout_order_query_trade.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| 名称 | Y字段 | Y父级字段 | 是否必须 | 默认值 | 是否可变更 |
| --- | --- | --- | --- | --- | --- |
| 销售出库单id | stockout_id |  | 是 |  | 否 |
| 销售出库单号 | order_no |  | 是 |  | 否 |
| 订单状态 | status |  | 是 | 4 已取消（可恢复） 5 已取消  50 待发货 51 待推送 52 推送中 53 推送失败 55 已推送 95 已发货 | 是 |
| 订单退款状态 | refund_status |  | 是 | 订单退款状态 0-无退款 1-申请退款 2-部分退款 3-全部退款 |  |
| 系统订单号 | src_order_no |  | 是 |  | 否 |
| 仓库id | warehouse_id |  | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 | 是 |
| 仓库编码 | warehouse_no |  | 是 | 代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |  |
| 仓库类型 | warehouse_type |  | 是 | 仓库类型 |  |
| 仓库名称 | warehouse_name |  |  |  |  |
| 出库时间 | consign_time |  | 是 |  | 是 |
| 邮资成本 | post_fee |  | 是 |  | 是 |
| 物流公司id | logistics_id |  | 是 |  | 是 |
| 客户网名 | buyer_nick |  |  | 客户网名 |  |
| 物流单号 | logistics_no |  | 是 | 物流单号 | 是 |
| 平台Id | platform_id |  |  | 点击查看平台ID详情 |  |
| 供应商编码 | provider_nick_no |  | 是 | 供应商编码 | 是 |
| 店铺名称 | shop_name |  |  | 店铺名称 |  |
| 店铺编码 | shop_no |  | 是 | 代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |
| 审核时间 | check_time |  |  | 审核时间 |  |
| 货品总数 | goods_count |  |  | 货品总数 |  |
| 仓库名称 | warehouse_name |  |  | 仓库名称 |  |
| 物流公司 | logistics_name |  |  | 物流公司 |  |
| 订单来源 | trade_from |  | 是 | 订单来源1、API抓单2、手工建单3、导入4、复制订单5、接口推送6、补发订单7、PDA选货开单8、分销补发订单 |  |
| 供应商名称 | provider_name |  | 是 | 供应商名称 | 是 |
| 分销商编码 | fenxiao_nick_no |  | 是 | 分销商编码 | 是 |
| 分销商名称 | fenxiao_nick_name |  | 是 | 分销商名称 | 是 |
| 分销原始店铺名称 | fenxiao_shop_name |  | 是 | 分销原始店铺名称 |  |
| 收件人姓名 | receiver_name |  | 是 | 收件人姓名 |  |
| 收件人国家 | receiver_country |  | 是 | 收件人国家 |  |
| 收件人省份 | receiver_province |  | 是 | 收件人省份 |  |
| 物流类型 | logistics_type |  | 是 | 物流类型，点击这里 | 是 |
| 物流类型名称 | logistics_type_name |  | 是 | 物流类型名称 | 是 |
| 收件人城市 | receiver_city |  | 是 | 收件人城市 |  |
| 收件人区 | receiver_district |  | 是 | 收件人区 |  |
| 货品数量 | goods_count |  | 是 | 货品数量 |  |
| 代发邮费 | oms_post_amount |  | 是 | 代发邮费，供销给分销代发的邮费 ， 只有这类订单需要 |  |
| 采购成本 | oms_purchase_amount |  | 是 | 采购成本 |  |
| 佣金 | oms_employ_amount |  | 是 | 佣金 |  |
| 分拣单号 | pick_no |  | 是 | 分拣单号 |  |
| 平台单号 | src_tids |  | 是 |  |  |
| 店铺id | shop_id |  | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |
| 店铺名称 | shop_name |  | 是 | 店铺名称 |  |
| 备注 | remark |  | 是 |  | 是 |
| 最后修改时间 | modified |  | 是 |  | 是 |
| 称重重量 | weight |  | 是 |  | 是 |
| 快递重量 | post_weight |  | 是 |  | 是 |
| 是否本系统发货 | trade_status_type |  |  | 1 平台发货 2 erp发货 |  |
| 打单员姓名 | printman_name |  | 是 |  |  |
| 审单员姓名 | auditman_name |  | 是 |  |  |
| 货品总额 | goods_amount |  | 是 |  |  |
| 货品列表 | details_list |  | 是 |  |  |
| 销售出库明细id | rec_id | details_list | 是 |  | 否 |
| 货品明细id | spec_id | details_list | 是 |  | 否 |
| 原始子订单号 | src_oid | details_list |  |  |  |
| 子单原始单号 | src_tid | details_list |  |  |  |
| 子单退款状态 | refund_status | details_list | 是 | 子单退款状态  0-无退款,1-取消退款,2-已申请退款,3-等待退货,4-等待收货,5-退款成功 |  |
| 出库单主键Id | stockout_id | details_list |  |  |  |
| 出库单明细id 关联系统订单id | src_order_detail_id | details_list |  |  |  |
| 系统订单明细id | stockin_detail_id | details_list | 是 |  | 否 |
| 数量 | num | details_list | 是 |  | 是 |
| 分摊邮费 | share_post | details_list | 否 | null | 是 |
| 分摊后总价 | share_amount | details_list | 是 |  | 是 |
| 零售价 | retail_price | details_list | 是 | 零售价 | 是 |
| 商家编码 | spec_no | details_list | 是 |  | 是 |
| sku主条码 | barcode | details_list | 是 | sku主条码 |  |
| 货品编号 | goods_no | details_list | 是 |  | 是 |
| 规格编号 | spec_code | details_list | 是 |  | 是 |
| 预估重量 | weight | details_list | 是 |  | 是 |
| 成本价 | cost_price | details_list | 是 |  | 是 |
| 销售价 | sell_price | details_list | 是 | 平台的销售价 | 是 |
| 商品名称 | goods_name | details_list | 是 |  | 是 |
| 规格名称 | spec_name | details_list | 是 |  | 是 |
| 最后修改时间 | modified | details_list | 是 |  | 是 |
| 单位id | base_unit_id | details_list | 是 |  | 是 |
| 赠品方式 | gift_type | details_list | 是 | 0、非赠品1、自动赠送 2、手工赠送  5 平台赠品 | 是 |
| 单位名称 | base_unit_name | details_list | 是 |  | 是 |
| 出库批次号 | batch_no | details_list | 否 |  | 否 |
| 平台售卖单价 | price | details_list | 是 | 平台售卖单价 | 是 |
| 单品自定义属性1 | prop1 | details_list | 是 | 单品自定义属性1 | 是 |
| 单品自定义属性2 | prop2 | details_list | 是 | 单品自定义属性2 | 是 |
| 单品自定义属性3 | prop3 | details_list | 是 | 单品自定义属性3 | 是 |
| 单品自定义属性4 | prop4 | details_list | 是 | 单品自定义属性4 | 是 |
| 单品自定义属性5 | prop5 | details_list | 是 | 单品自定义属性5 | 是 |
| 单品自定义属性6 | prop6 | details_list | 是 | 单品自定义属性6 | 是 |
| 单品自定义属性7 | prop7 | details_list | 是 | 单品自定义属性7 | 是 |
| 单品自定义属性8 | prop8 | details_list | 是 | 单品自定义属性8 | 是 |
| 单品自定义属性9 | prop9 | details_list | 是 | 单品自定义属性9 | 是 |
| 单品自定义属性10 | prop10 | details_list | 是 | 单品自定义属性10 | 是 |
| 货品自定义属性1 | goods_prop1 | details_list | 是 | 货品自定义属性1 | 是 |
| 货品自定义属性2 | goods_prop2 | details_list | 是 | 货品自定义属性2 | 是 |
| 货品自定义属性3 | goods_prop3 | details_list | 是 | 货品自定义属性3 | 是 |
| 货品自定义属性4 | goods_prop4 | details_list | 是 | 货品自定义属性4 | 是 |
| 货品自定义属性5 | goods_prop5 | details_list | 是 | 货品自定义属性5 | 是 |
| 货品自定义属性6 | goods_prop6 | details_list | 是 | 货品自定义属性6 | 是 |
| 组合装id | suite_id | details_list | 是 | 组合装id |  |
| 组合装编码 | suite_no | details_list | 是 | 组合装编码 |  |
| 组合装数量 | suite_num | details_list | 是 | 组合装数量 |  |
| 是否是完整组合装 | is_complete_suite | details_list | 是 | 1-是，0-否 |  |
| 主播id | anchor_id | details_list | 否 |  | 否 |
| 主播名称 | anchor_name | details_list | 否 |  | 否 |
| 分摊单价 | share_price | details_list | 是 | 分摊价格，扣减优惠之后，不加邮费收入的单价 | 是 |
| 组合装拆分合并标识 | suit_flag | details_list | 否 |  | 是 |
| 供应商编号 | provider_nick_no | details_list | 是 |  |  |
| 供应商昵称 | provider_name | details_list | 是 |  |  |
| 是否包装 | is_package | details_list | 是 |  |  |
| 货品成本 | goods_cost | details_list | 是 |  |  |
| 代发邮费 | oms_post_amount | details_list | 是 | 代发邮费 |  |
| 采购成本 | oms_purchase_amount | details_list | 是 | 采购成本 |  |
| 组合装ID | suite_id | details_list | 否 | 0 | 是 |
| 序列号列表 | sn_list | details_list | 是 |  |  |
| 序列号 | sn | sn_list | 否 | 序列号 |  |
| 辅助序列号 | second_sn | sn_list | 否 | 辅助序列号 |  |
| 货位批次明细数据 | position_list | details_list | 否 |  | 是 |
| 出库单明细或者订单明细Id | stockout_order_detail_id | position_list | 否 |  | 是 |
| 入库单号明细id | stock_spec_detail_id | position_list | 否 |  | 是 |
| 货位主键id | rec_id | position_list | 否 |  | 是 |
| 货位ID | position_id | position_list | 否 |  | 是 |
| 货位编号 | position_no | position_list | 是 | 货位编号 |  |
| 批次号 | batch_no | position_list | 否 |  | 是 |
| 有效期 | expire_date | position_list | 否 |  | 是 |
| 生产日期 | production_date | position_list | 否 |  | 是 |
| 出库数量 | num | position_list | 否 |  | 是 |
| 成本价 | cost_price | position_list | 否 |  | 是 |
| 最后修改时间 | modified | position_list | 否 |  | 是 |
| 物流列表 | logistics_list | array[] |  |  |  |
| 物流单号 | logistics_no | logistics_list | string | 物流单号 |  |
| 关联物流单 | related_logistics_no | logistics_list | string | 若parent_child_flag=1，则该字段为母单号 |  |
| 物流公司名称 | logistics_name | logistics_list | string | 物流公司名称 |  |
| 重量 | weight | logistics_list | decimal(19, 4) | 重量 |  |
| 邮资 | post_cost | logistics_list | decimal(19, 4) | 邮资 |  |
| 打印状态 | print_status | logistics_list | int | 0-未打印 1-已打印 |  |
| 创建时间 | created | logistics_list | datetime | 创建时间 |  |
| 子母单标识 | parent_child_flag | logistics_list | int | 0-普通单 1-子母单 |  |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stockout_order_query_trade.php';<br><br>    //添加查询参数<br>    $c->putApiParam('start_time','2018-08-01 00:00:00');<br>    $c->putApiParam('end_time','2018-08-11 00:00:00');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "stockout_list": [<br>        {<br>            "trade_from": 1,<br>            "stockout_id": "2756286207594856469",<br>            "order_no": "JY2510282687",<br>            "status": 95,<br>            "src_order_no": "JY2510282687",<br>            "warehouse_id": "1",<br>            "warehouse_type": 2,<br>            "consign_time": "2025-10-28 22:01:21",<br>            "platform_id": "1",<br>            "shop_id": "12",<br>            "post_fee": "0.0000",<br>            "logistics_id": "0",<br>            "logistics_no": "78858955625465",<br>            "remark": "1",<br>            "modified": "2025-11-03 09:59:21",<br>            "weight": "0.0000",<br>            "post_weight": "0.0000",<br>            "src_tids": "4842818029414320724",<br>            "goods_count": "1.0000",<br>            "trade_status_type": 1,<br>            "goods_total_amount": null,<br>            "receiver_name": null,<br>            "receiver_country": null,<br>            "receiver_province": 110000,<br>            "receiver_city": 110100,<br>            "receiver_district": 110115,<br>            "logistics_type": "5",<br>            "logistics_type_name": "中通快递",<br>            "oms_post_amount": "0.0000",<br>            "oms_purchase_amount": "0.0000",<br>            "oms_employ_amount": "0.0000",<br>            "refund_status": 3,<br>            "pick_no": "",<br>            "fenxiao_nick_name": "",<br>            "fenxiao_nick_no": "",<br>            "provider_nick_no": "74caf04",<br>            "provider_name": "y_qiyeban2",<br>            "details_list": [<br>                {<br>                    "rec_id": "2756286207594858517",<br>                    "stockout_id": "2756286207594856469",<br>                    "spec_id": "2720289868889456644",<br>                    "stockin_detail_id": "2756286207594858517",<br>                    "src_order_detail_id": "2756286207594858517",<br>                    "num": "1.0000",<br>                    "share_amount": "0.0100",<br>                    "share_post": "0.0000",<br>                    "spec_no": "pc_xq1",<br>                    "goods_no": "pc_xq_ceshi",<br>                    "spec_code": "",<br>                    "weight": "3.0000",<br>                    "cost_price": "0.5000",<br>                    "sell_price": "0.0100",<br>                    "retail_price": "0.1200",<br>                    "goods_name": "试下批量修改",<br>                    "spec_name": "粉红",<br>                    "modified": "2025-10-28 23:16:02",<br>                    "src_oid": "4842818029414320724",<br>                    "src_tid": "4842818029414320724",<br>                    "base_unit_id": "0",<br>                    "base_unit_name": "",<br>                    "batch_no": "",<br>                    "anchor_id": null,<br>                    "anchor_name": null,<br>                    "share_price": "0.0100",<br>                    "suit_flag": 0,<br>                    "suite_id": "0",<br>                    "is_package": 0,<br>                    "goods_cost": "0.5000",<br>                    "oms_post_amount": "0.0000",<br>                    "oms_purchase_amount": "0.0000",<br>                    "position_list": [],<br>                    "sn_list": [],<br>                    "refund_status": 5,<br>                    "provider_nick_no": "74caf04",<br>                    "provider_name": "y_qiyeban2"<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务请求参数

| 名称 | Y字段 | 描述 | 必须 |
| --- | --- | --- | --- |
| 开始时间 | start_time | 修改起始时间，若无订单号/物流单号，则为必填。示例：“ 2021-11-11 00:00:00” | 时间开始和结束 和系统单号不能同时为空 |
| 结束时间 | end_time | 修改结束时间，上同开始时间。示例：“ 2021-11-11 01:00:00” |  |
| 店铺编码 | shop_no | 代表店铺所有属性的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |
| 仓库编码 | warehouse_no | 代表仓库所有属性的唯一编码，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |  |
| 时间类型 | time_type | 时间类型 默认不填为 修改时间 1 修改时间 2 发货时间 | 否 |
| 系统订单号 | src_order_no | 系统订单号，多个用,分隔 | 传入系统订单号可以不传时间 |
| 状态类型 | status_type | 1-已发货及以后 2-已审核及以后  默认已发货及以后 |  |
| 是否仅获取库存数据 | fetch_stock_only | 1-是, 0-否, 默认为否 |  |
| 分页大小 | page_size | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100，使用举例单击这里 | 否 |
| 页号 | page_no | 页号，不传默认从0页开始 | 否 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 条数 | total_count | varchar | 255 | 是 | 符合查询条件的总数量，只有page_no = 0 时才有值。 |
| 原始单节点 | stockout_list | data[] |  | 是 | 业务数据的一级节点，数组形式的订单数据，需要循环读取。 |


#### 响应示例

### JSON

```text
{
    "code": 2900,
    "message": "时间范围与订单编号不能全部为空"
}
```


### sales_trade_modify_Y：修改系统订单

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `sales_trade_modify_Y` |
| PHP 文件 | `sales_trade_modify.php` |
| 文档标题 | 修改系统订单 仓库 物流 |
| 描述 | 修改旺店通erp内订单的订单标记 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_modify_Y |

#### 接口说明

| 1.1 接口描述：修改旺店通erp内订单的订单标记 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/sales_trade_modify.php |
| 正式环境 | https://openapi.huice.com/openapi/sales_trade_modify.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| php | //<br><?php<br>   require_once('../WdtClient.php');<br><br>   $c = new WdtClient;<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>   $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/sales_trade_modify.php';<br>   //系统订单号<br>   $c->putApiParam('trade_no','JY2505130492');<br>   //仓库id<br>   $c->putApiParam('warehouse_id','6');<br>   //物流公司id<br>   $c->putApiParam('logistics_id','2675780066033532930');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>    ?> |
| --- | --- |
| JAVA | package com.erpx.api.trade;<br><br>import com.erpx.api.CommonConstants;<br>import com.erpx.api.WdtClient;<br><br>import java.io.IOException;<br>import java.util.HashMap;<br>import java.util.Map;<br><br>public class ChangeWarehouseService {<br>    public static void changeWarehouse() throws Exception {<br><br>        WdtClient client = new WdtClient(CommonConstants.sid, CommonConstants.appkey, CommonConstants.appSecret,<br>            CommonConstants.baseUrl);<br>        Map<String, String> params = new HashMap<String, String>();<br><br>        params.put("trade_no", "JY2505130492");<br>        params.put("warehouse_id", "6");<br>        params.put("logistics_id", "2675780066033532930");<br><br>        try {<br>            String response = client.execute("sales_trade_modify.php", params);<br>            System.out.println(response);<br>        } catch (IOException e) {<br>            e.printStackTrace();<br>        }<br>    }<br><br>    public static void main(String[] args) throws Exception {<br>        changeWarehouse();<br>    }<br>} |
| python | #  修改系统订单的仓库店铺<br>import WdtClient<br>import json<br>from wdt_constants import *<br>t =  WdtClient.WdtClient(APPKEY, APPSECRET, SID, BASEURL)<br>params = {}<br># 订单号 页面展示的系统订单号<br>params.update({"trade_no":'JY2505130492'})<br># 仓库id<br>params.update({"warehouse_id": "6"})<br># 物流id<br>params.update({"logistics_id": "2675780066033532930"})<br>response = t.execute("sales_trade_modify.php", params)<br>print(response) |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单编号 | trade_no | varchar | 40 | 是 | 系统订单编号，默认为JY开头 |
| 物流公司id | logistics_id | bigint(20) | 20 | 否 | 物流公司id，使用 物流公司 接口返回的logistics_id |
| 仓库id | warehouse_id | int | 11 | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 包裹数 | package_num | int | 1 | 否 | 注意包裹数不能多于50个 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |


#### 响应示例

### JSON

```text
{
  "code": 0,
  "message":""
}
```

### JSON

```text
{
  "code": 2900,
  "message": "必传参数缺失入参：warehouse_id 和logistics_id不能同时为空"
}
```


### sales_trade_replenish_Y：创建补发订单

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `sales_trade_replenish_Y` |
| PHP 文件 | `sales_trade_replenish.php` |
| 文档标题 | 创建补发订单 |
| 描述 | 创建补发订单 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_replenish_Y |

#### 接口说明

| 1.1 接口描述：通过接口推送补发订单给ERP |
| --- |
| 1.2 适用版本：网页版 |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/sales_trade_replenish.php |
| 正式环境 | https://openapi.huice.com/openapi/sales_trade_replenish.php |

| PHP | //根据系统订单补发<br><?php<br>require_once('../WdtClient.php');<br>$c = new WdtClient;<br>$c->sid ='';<br>$c->appkey ='';<br>$c->appsecret ="";<br>//测试环境地址上线时需要换成线上的<br>$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/sales_trade_replenish.php'; // 测试的<br>//$c->gatewayUrl = 'https://openapi.huice.com/openapi/sales_trade_replenish.php'; //正式的<br><br>$trade_info = new stdClass();<br>$trade_info->trade_no = "JY26032413816";<br>$trade_info->receiver_name = "张三";              // 收件人姓名<br>$trade_info->receiver_mobile = "13800138000";    // 收件人手机号<br>$trade_info->receiver_address = "北京北京市朝阳区XX路XX号"; // 收件人详细地址<br>$trade_info->receiver_province = 120000;         // 收件人省编码<br>$trade_info->receiver_city = 120100;             // 收件人市编码<br>$trade_info->receiver_district = 120116;         // 收件人区编码<br>$trade_info->sys_remark = "这是线下备注";          // 线下备注<br>$trade_info->is_check = 1;<br>$spec_item = new stdClass();<br>$spec_item->spec_no = "26032428375582";<br>$spec_item->is_suite = 0;   //0 否 1 是 默认 0<br>$spec_item->amount = 1;   //金额<br>$spec_item->num = "1";<br>$trade_info->spec_list = [$spec_item];<br>$c->putApiParam("trade_info", json_encode($trade_info, JSON_UNESCAPED_UNICODE));<br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 卖家账号, 由旺店通分配 |
| 接口账号 | key | String |  | 是 | 由旺店通分配appkey, 在发送的数据中对应 key 字段 |
| 秒级时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | 签名 |


#### 业务请求参数

| 字段名称 | Y 字段 | Y父级字段 | Y类型 | Y枚举 | 是否必填 | 默认值 |
| --- | --- | --- | --- | --- | --- | --- |
| 订单主信息部分 | trade_info |  | 单个订单 ，不是数组 | JSON 格式的字符串放在form 参数 trade_info 中 |  |  |
| 订单trade_no(补发的订单trade_no) | trade_no | trade_info | varchar(64) |  | 是 |  |
| 收件人姓名 | receiver_name | trade_info | varchar(128) |  | 否 |  |
| 收件人手机号 | receiver_mobile | trade_info | varchar(128) |  | 否 |  |
| 收件人详细地址 | receiver_address | trade_info | varchar(255) |  | 否 |  |
| 收件人省名称 | receiver_province_name | trade_info | varchar |  | 否 |  |
| 收件人市名称 | receiver_city_name | trade_info | varchar |  | 否 |  |
| 收件人区名称 | receiver_district_name | trade_info | varchar |  | 否 |  |
| 客服备注 | cs_remark | trade_info | varchar(1024) |  | 否 |  |
| 线下备注 | sys_remark | trade_info | varchar(1024) |  | 否 |  |
| 仓库编号 | warehouse_no | trade_info | varchar(40) | 仓库编号，代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 | 否 |  |
| 物流主键ID | logistics_id | trade_info | varchar(40) | 快递管理界面系统主键id | 否 |  |
| 物流名称 | logistics_name | trade_info | varchar(40) | 物流名称，快递管理界面自定义维护物流公司说名称 | 否 |  |
| 是否审核 | is_check | trade_info | int | 1 审核 （自动执行审核）0 不审核 默认为0 | 否 |  |
| 补发的货品信息 | spec_list | trade_info |  |  | 是 |  |
| 商品规格编码 | spec_no | spec_list | varchar(64) |  | 是 |  |
| 数量 | num | spec_list | decimal(19,4) |  | 是 |  |
| 是否组合装 | is_suite | spec_list | int | 0 否 1 是 默认 0 | 否 | 0 |
| 金额 | amount | spec_list | decimal(19,4) |  | 否 |  |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 返回码 | code | int |  | 是 | 0成功 其他值失败 |
| 返回message | message | varchar(255) |  | 是 | 成功时为空 |
| 订单编号 | trade_nos | 数组 data[varchar(64)] |  | 否 |  |
| 订单id | trade_ids | 数组 data[bigint(20)] |  | 否 |  |


#### 响应示例

### JSON

```text
{
    "code": 0,
    "message": "",
    "trade_nos": [
        "JY2601280003"
    ],
    "trade_ids": [
        "2789447850105241602"
    ]
}
```

### JSON

```text
{
    "code": 30401,
    "message": "传入的spec_no错误"
}
```


### stockout_order_query_trade_cancel_Y：撤销发货的销售出库单查询

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `stockout_order_query_trade_cancel_Y` |
| PHP 文件 | `stockout_order_query_trade_cancel.php` |
| 文档标题 | 撤销发货的销售出库单查询 |
| 描述 | 销售出库单是基于订单的，订单可以撤销发货。当前接口是用于查询历史的撤销的已发货订单数据。举例：订单JY20250001在2025-01-01 12:00:00第一次发货， 在2025-01-01 12:30:00撤销发货。 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=stockout_order_query_trade_cancel_Y |

#### 接口说明

| 1.1 接口描述：销售出库单是基于订单的，订单可以撤销发货。当前接口是用于查询历史的撤销的已发货订单数据。举例：订单JY20250001在2025-01-01 12:00:00第一次发货， 在2025-01-01 12:30:00撤销发货。 |
| --- |
| 1.2 适用版本：网页端 |
| 1.3 注意事项：Y目前没有走销售出库流程 目前没有   直接使用已发货的订单作为替代 ，已发货订单支持撤销，也就是同一个订单可以撤销发货 |


#### 调用场景

| 2.1 举例说明：撤销发货的销售出库单查询 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/stockout_order_query_trade_cancel.php |
| 正式环境 | https://openapi.huice.com/openapi/stockout_order_query_trade_cancel.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 |  |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| 名称 | Y字段 | Y父级字段 | 慧经营类型 | 慧经营枚举 | 是否必须 | 默认值 | 是否可变更 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 销售出库单id | stockout_id |  | bigint(20) |  | 是 |  | 否 |
| 销售出库单号 | order_no |  | string |  | 是 |  | 否 |
| 发货状态 | status |  | tinyint(4) | 已发货95 已完成110 已取消5 | 是 |  | 是 |
| 系统订单号 | src_order_no |  | string |  | 是 |  | 否 |
| 仓库id | warehouse_id |  | int(11) | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 | 是 |  | 是 |
| 出库时间 | consign_time |  | datetime | 已取消可以传null | 是 |  | 是 |
| 邮资成本 | post_fee |  | decimal(19, 4) |  | 是 |  | 是 |
| 物流公司id | logistics_id |  | bigint(20) |  | 是 |  | 是 |
| 物流编号 | logistics_no |  | string |  | 是 |  | 是 |
| 平台Id | platform_id |  | int(11) |  |  |  |  |
| 平台单号 | src_tids |  | string |  | 是 |  |  |
| 店铺id | shop_id |  | int(11) | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |  |  |  |
| 备注 | remark |  | string |  | 是 |  | 是 |
| 最后修改时间 | modified |  | datetime |  | 是 |  | 是 |
| 称重重量 | weight |  | decimal(19, 4) |  | 是 |  | 是 |
| 快递重量 | post_weight |  | decimal(19, 4) |  | 是 |  | 是 |
| 是否本系统发货 | trade_status_type |  | int | 1 平台发货 2 erp发货 |  |  |  |
| 业务员 |  |  | string |  | 否 | null | 是 |
| 物流状态 | 无 |  | tinyint(4) | 99推送失败0待查询1待取件2已取件3在途中4待派件5签收6拒收8未订阅9退件中10已退签发货后是待取件状态，后边就是根据物流追踪信息去变更 | 否 | null | 是 |
| 货品列表 | details_list |  | array[] |  | 是 |  |  |
| 销售出库明细id | rec_id | details_list | bigint(20) |  | 是 |  | 否 |
| 货品明细id | spec_id | details_list | int(11) |  | 是 |  | 否 |
| 原始子订单号 | src_oid | details_list | string |  |  |  |  |
| 子单原始单号 | src_tid | details_list | string |  |  |  |  |
| 出库单主键Id | stockout_id | details_list | bigint(20) |  |  |  |  |
| 出库单明细id 关联系统订单id | src_order_detail_id | details_list | bigint(20) |  |  |  |  |
| 系统订单明细id | stockin_detail_id | details_list | bigint(20) |  | 是 |  | 否 |
| 数量 | num | details_list | decimal(19, 4) |  | 是 |  | 是 |
| 分摊邮费 | share_post | details_list | decimal(19, 4) |  | 否 | null | 是 |
| 分摊后总价 | share_amount | details_list | decimal(19, 4) |  | 是 |  | 是 |
| 商家编码 | spec_no | details_list | string |  | 是 |  | 是 |
| 货品编号 | goods_no | details_list | string |  | 是 |  | 是 |
| 规格编号 | spec_code | details_list | string |  | 是 |  | 是 |
| 预估重量 | weight | details_list | decimal(19, 4) |  | 是 |  | 是 |
| 成本价 | cost_price | details_list | decimal(19, 4) |  | 是 |  | 是 |
| 销售价 | sell_price | details_list | decimal(19, 4) |  | 是 |  | 是 |
| 商品名称 | goods_name | details_list | string |  | 是 |  | 是 |
| 规格名称 | spec_name | details_list | string |  | 是 |  | 是 |
| 批次号 | 无 | details_list | string |  | 否 | null | 是 |
| 最后修改时间 | modified | details_list | datetime |  | 是 |  | 是 |
| 删除标记 |  | details_list | tinyint(4) | 0未删除 >0已删除 | 否 | 0 | 是 |
| 出库批次号 | batch_no | details_list | string |  | 否 |  | 否 |
| 主播id | anchor_id | details_list | string |  | 否 |  | 否 |
| 主播名称 | anchor_name | details_list | string |  | 否 |  | 否 |
| 货位批次明细数据 | position_list | details_list | array[] |  | 否 |  | 是 |
| 出库单明细或者订单明细Id | stockout_order_detail_id | position_list | bigint(20) |  | 否 |  | 是 |
| 入库单号明细id | stock_spec_detail_id | position_list | bigint(20) |  | 否 |  | 是 |
| 货位主键id | rec_id | position_list | bigint(20) |  | 否 |  | 是 |
| 货位ID | position_id | position_list | bigint(20) |  | 否 |  | 是 |
| 批次号 | batch_no | position_list | string |  | 否 |  | 是 |
| 有效期 | expire_date | position_list | datetime | 举例 2025-01-01 00:00:00 | 否 |  | 是 |
| 生产日期 | production_date | position_list | datetime |  | 否 |  | 是 |
| 出库数量 | num | position_list | decimal(19, 4) |  | 否 |  | 是 |
| 成本价 | cost_price | position_list | decimal(19, 4) |  | 否 |  | 是 |
| 最后修改时间 | modified | position_list | datetime |  | 否 |  | 是 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/stockout_order_query_trade_cancel.php';<br><br>	$c->putApiParam('start_time', '2026-02-09 10:00:00');<br>	$c->putApiParam('end_time', '2026-02-09 23:59:59');<br>	$c->putApiParam('src_order_no', 'JY2512100886');<br>	$c->putApiParam('page_no', 0);<br>	$c->putApiParam('page_size', 1);<br><br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 3,<br>    "stockout_list": [<br>        {<br>            "trade_from": null,<br>            "stockout_id": "2793799624756822049",<br>            "order_no": "JY2602090107",<br>            "status": 5,<br>            "src_order_no": "JY2602090107",<br>            "warehouse_id": "95",<br>            "warehouse_name": null,<br>            "warehouse_type": null,<br>            "check_time": null,<br>            "consign_time": "2026-02-09 10:15:43",<br>            "platform_id": "127",<br>            "shop_id": "332",<br>            "shop_name": null,<br>            "post_fee": "2E+1",<br>            "logistics_id": null,<br>            "logistics_name": null,<br>            "logistics_no": "",<br>            "remark": null,<br>            "modified": null,<br>            "weight": null,<br>            "post_weight": null,<br>            "src_tids": "2071111001",<br>            "goods_count": "1E+1",<br>            "trade_status_type": 2,<br>            "goods_total_amount": "1E+3",<br>            "receiver_name": "******",<br>            "receiver_country": 0,<br>            "receiver_province": 110000,<br>            "receiver_city": 110100,<br>            "receiver_district": 110108,<br>            "buyer_nick": null,<br>            "logistics_type": null,<br>            "logistics_type_name": null,<br>            "oms_post_amount": null,<br>            "oms_purchase_amount": null,<br>            "oms_employ_amount": null,<br>            "pick_no": null,<br>            "refund_status": null,<br>            "fenxiao_nick_name": null,<br>            "fenxiao_nick_no": null,<br>            "fenxiao_shop_name": null,<br>            "provider_nick_no": null,<br>            "provider_name": null,<br>            "printman_name": null,<br>            "auditman_name": null,<br>            "goods_amount": null,<br>            "details_list": [<br>                {<br>                    "price": null,<br>                    "barcode": null,<br>                    "prop1": null,<br>                    "prop2": null,<br>                    "prop3": null,<br>                    "prop4": null,<br>                    "prop5": null,<br>                    "prop6": null,<br>                    "prop7": null,<br>                    "prop8": null,<br>                    "prop9": null,<br>                    "prop10": null,<br>                    "rec_id": "2793799624756824097",<br>                    "platform_id": null,<br>                    "stockout_id": "2793799624756822049",<br>                    "spec_id": "2787359232045875215",<br>                    "stockin_detail_id": "2793799624756824097",<br>                    "src_order_detail_id": "2793799624756824097",<br>                    "num": "1E+1",<br>                    "share_amount": "981",<br>                    "share_post": "12",<br>                    "spec_no": "c9711555111c1",<br>                    "goods_no": "2002205578005589",<br>                    "spec_code": "",<br>                    "weight": "0",<br>                    "cost_price": "0.0000",<br>                    "sell_price": "98.1",<br>                    "retail_price": null,<br>                    "goods_name": "货位000022",<br>                    "spec_name": "",<br>                    "modified": null,<br>                    "src_oid": "2071112227001a",<br>                    "src_tid": "2071111001",<br>                    "base_unit_id": "0",<br>                    "base_unit_name": "",<br>                    "batch_no": null,<br>                    "anchor_id": null,<br>                    "anchor_name": null,<br>                    "share_price": null,<br>                    "suit_flag": null,<br>                    "suite_id": null,<br>                    "is_package": 0,<br>                    "goods_cost": null,<br>                    "oms_post_amount": null,<br>                    "oms_purchase_amount": null,<br>                    "position_list": null,<br>                    "sn_list": null,<br>                    "refund_status": null,<br>                    "provider_nick_no": null,<br>                    "provider_name": null,<br>                    "goods_prop1": null,<br>                    "goods_prop2": null,<br>                    "goods_prop3": null,<br>                    "goods_prop4": null,<br>                    "goods_prop5": null,<br>                    "goods_prop6": null,<br>                    "gift_type": null,<br>                    "actual_num": null<br>                }<br>            ],<br>            "logistics_list": null<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务请求参数

| 名称 | 字段 | Y字段 | 必须 | 描述 |
| --- | --- | --- | --- | --- |
| 开始时间 | start_time | start_time |  | 修改起始时间，若无订单号/物流单号，则为必填。示例：“ 2021-11-11 00:00:00”。时间开始和结束和系统单号不能同时为空 |
| 结束时间 | end_time | end_time |  | 修改结束时间，上同开始时间。示例：“ 2021-11-11 01:00:00” |
| 系统订单号 | src_order_no | src_order_no |  | 系统订单号，多个用,分隔 |
| 分页大小 | page_size | page_size | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100，使用举例单击这里 |
| 页号 | page_no | page_no | 否 | 页号，不传默认从0页开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 条数 | total_count | varchar | 255 | 是 | 符合查询条件的总数量，只有page_no = 0 时才有值。 |
| 原始单节点 | stockout_list | data[] |  | 是 | 业务数据的一级节点，数组形式的订单数据，需要循环读取。 |


#### 响应示例

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### sales_trade_batch_remark_flag_Y：批量修改系统订单的标旗和备注

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `sales_trade_batch_remark_flag_Y` |
| PHP 文件 | `sales_trade_batch_remark_flag.php` |
| 文档标题 | 批量修改系统订单的标旗和备注 |
| 描述 | 批量修改系统订单的标旗和备注 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_batch_remark_flag_Y |

#### 接口说明

| 1.1 接口描述：批量修改系统订单的标旗和备注 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3注意事项：①批量修改系统订单的标旗和备注  ，只能修改为相同的标旗和备注 |


#### 调用场景

| 2.1 举例说明：批量修改系统订单的标旗和备注 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/sales_trade_batch_remark_flag.php |
| 正式环境 | https://openapi.huice.com/openapi/sales_trade_batch_remark_flag.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret = '';<br><br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/sales_trade_batch_remark_flag.php';<br>    $c->putApiParam('trade_ids',"2769892786424512518,2766250315173855241");<br>    $c->putApiParam('remark',"客服备注");<br>    $c->putApiParam('remark_flag',1);<br>    $c->putApiParam('type',1);<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单id | trade_ids | varchar |  | 是 | 订单id，多个订单id用,拼接 ,最多100个 |
| 标旗 | remark_flag | int |  | 是 | 订单标旗在取值枚举为1：红色  2：黄色  3：绿色 4：蓝色 5：紫色  6：灰色 |
| 客服备注 | remark | vachar | 512 | 否 | 客服备注 |
| 备注类型 | type | int |  | 否 | 1追加 2 覆盖    不传默认追加 |
| 线下备注 | system_remark | vachar | 512 | 可选必传 | remark_flag和system_remark 必传其一 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 错误明细 | errors | data |  | 否 | 响应参数的1级数据节点，节点下数据字段详见下述“errors”列表 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单id | trade_id | long | 11 | 是 | 入库单主键id |
| 错误描述信息 | error | varchar | 255 | 是 | 错误明细描述 |


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

### JSON

```text
{
    "code": 1020,
    "message": "系统异常，请稍后再试！",
    "errors": [

    ]
}
```


### xsd_self_delivery_location_callback_Y：小时达自配送三方运力回传状态和位置接口

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `xsd_self_delivery_location_callback_Y` |
| PHP 文件 | `xsd_self_delivery_location_callback.php` |
| 文档标题 | 小时达自配送三方运力回传状态和位置接口 |
| 描述 | 小时达自配送三方运力回传状态和位置接口 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=xsd_self_delivery_location_callback_Y |

#### 接口说明

| 1.1 接口描述：小时达自配送三方运力回传状态和位置接口 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：小时达自配送三方运力回传状态和位置接口 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/xsd_self_delivery_location_callback.php |
| 正式环境 | https://openapi.huice.com/openapi/xsd_self_delivery_location_callback.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once '../WdtClient.php';<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/xsd_self_delivery_location_callback.php';<br><br>    $locations = array( array(<br>        "tid"=> "0902372222222689",<br>        "shop_id"=> "332",<br>        "platform_id"=> 127,<br>        "logistic_tag"=> "ONESELF",<br>	    "logistic_no"=>"Lx1311110122310809045",<br>        "status"=>"102",<br>	    "rider_name"=>"骑手名称",<br>	    "rider_phone"=>"11111110000",<br>	    "distance"=>"33",<br>	    "longitude"=>"116.397128",<br>	    "latitude"=>"39.909736"<br>        )<br>    );<br>    $c->putApiParam('locations',json_encode($locations,JSON_UNESCAPED_UNICODE));<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 字段 | 名称 | 父级字段 | 是否必须 | 描述 | 枚举值 |
| --- | --- | --- | --- | --- | --- |
| locations | List |  | 是 | 定位数据 |  |
| tid | String | locations | 是 | 平台方订单唯一ID |  |
| platform_id | int | locations | 是 | 平台ID |  |
| shop_id | int | locations | 是 | 归属门店ID | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| logistic_tag | String | locations | 是 | 配送三方标识 | 枚举名 枚举值美团骑手 MEITUAN顺丰 SHUNFENG达达 DADA蜂鸟跑腿 FENGNIAO饿了么众包 ELEZB饿百众包 EBAIZB闪送 BINGEXUU跑腿 UUPT帮拉 BANGLA邻趣 LINQU曹操送 CAOSONG指动跑腿 ZHIDONG曹操跑腿 CAOCAO喊跑跑 PAOPAO大侠跑腿 DAXIA点我达 DIANWO爱跑腿 IPAOTUI小帮 XIAOBANG蚂蚁派 RIDER拼必达 PINBIDA久久跑腿 JIUJIU赛曹操 SAICAOCAO直通车 ZHITONG小哥快运 XIAOGE云递配 YUNDA零点壹 HUICONG时路网 SHILU聚合配送 SONGSHUWU宅帮手 ZBS靠谱送 KAOPU0851跑腿 KUAIMA祥子 XIANGZI快到 KUAIDAOE派速达 EPAI一城飞客 FEIKE哪都达 NADUDA服务之家 FUWUJIA便利专送 BIANLI鸿速同城急送 HONGSU裹小递 GUOXIAODI快服务 FUWU快跑者 KELOOP好急跑腿 HAOJI京东配送 JDPS鹏九跑腿 PENGJIU货拉拉 HUOLALA代帮跑腿 DAIBANG来啦跑腿 LAILA懒猪跑腿 LANZHU快跑者急送 KUAIPAO飞兔跑腿 FEITU送道 SONGDAO安克弗跑腿 ANKEFO送个东西跑腿 SONGDONGXI安讯即配 ANXUN自提 PICKER其他 OTHER自配送 ONESELF |
| logistic_no | String | locations | 是 | 配送运单号 |  |
| status | String | locations | 是 | 配送状态 | 枚举名   枚举值未分配骑手 101已分配骑手 102已到店 103配送中 104  已完单  200配送取消  300 配送退回 301配送转单 302订单创建失败  400 |
| rider_name | String | locations | 是 | 骑手名称 |  |
| rider_phone | String | locations | 是 | 骑手电话 |  |
| distance | String | locations | 否 | 骑手距离 |  |
| longitude | String | locations | 否 | 骑手经度(国测局02标准，如高德) |  |
| latitude | String | locations | 否 | 骑手纬度(国测局02标准，如高德) |  |
| is_transship | Boolean | locations | 否 | 是否接驳配送 | true 是，false 否 |
| province | String | locations | 否 | 省名称 | 天猫非小时达自配送必传，其他业务不必传 |
| city | String | locations | 否 | 市名称 | 天猫非小时达自配送必传，其他业务不必传 |
| district | String | locations | 否 | 区名称 | 天猫非小时达自配送必传，其他业务不必传 |
| twon | String | locations | 否 | 街道名称 | 天猫非小时达自配送必传，其他业务不必传 |
| trade_no | String | locations | 否 | 系统单号 | 非必传字段，如果涉及拆分后，需要控制到系统单级别传该字段 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 条数 | total_count | varchar | 255 | 是 | 条数 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": null,<br>    "errors": [<br><br>    ]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误的数据 | tid | bigint | 20 | 是 | 平台订单ID |
| 错误信息的描述 | error | varchar | 255 | 否 | 错误信息的描述 |


#### 响应示例

### JSON

```text
{
    "code": 30400,
    "message": "订单号在系统中不存在，请确认传值是否正确"
}
```


### api_trade_live_extend_query_Y：查询直播主播信息

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `api_trade_live_extend_query_Y` |
| PHP 文件 | `api_trade_live_extend_query.php` |
| 文档标题 | 查询直播主播信息 |
| 描述 | 获取租户系统内平台订单的直播信息扩展 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=api_trade_live_extend_query_Y |

#### 接口说明

| 1.1 接口描述：获取租户系统内平台订单的直播信息扩展 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 时间跨度：开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |


#### 调用场景

| 2.1 举例说明：SAP、线下ERP、SRM、SCM等系统对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/api_trade_live_extend_query.php |
| 正式环境 | https://openapi.huice.com/openapi/api_trade_live_extend_query.php |


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
| tid | 原始单号 | tid |  |  | 原始单号 有原始单号可以不传时间 |
| start_time | 开始时间 | start_time |  |  | 修改起始时间 |
| end_time | 结束时间 | end_time |  |  | 修改结束时间 |
| shop_id | 店铺id | shop_id |  |  | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| shop_no | 店铺编号 | shop_no |  |  | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 分页大小 | page_size | page_size |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100，使用举例单击这里 |
| 页号 | page_no | page_no |  | 否 | 页号，不传默认从0页开始 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 总条数 | total_count | in | 11 |  |  |
| 直播数据列表 | list | data[] |  | 是 | 响应参数的数据节点 |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| id | rec_id | bigint |  |  |  |
| 平台id | platform_id | int |  |  |  |
| 原始单号 | tid | varchar |  |  |  |
| 原始子单号 | oid | varchar |  |  |  |
| 店铺ID | shop_id | int |  |  | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_id | varchar |  |  | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 状态 | status | int |  |  | 0 已处理 1 待处理 2 获取失败 |
| 平台主播id | role_id | varchar |  |  |  |
| 预估达人佣金率 | commission_rate | decimal(19,4) |  |  |  |
| 预估达人佣金 | commission | decimal(19,4) |  |  |  |
| 类型 | other_flags | int |  |  | 1 自营 2 平台分销 4 直播 8 短视频 16 店铺自卖 |
| 达人昵称 | role_name | varchar |  |  |  |
| 直播间ID | room_id | varchar |  |  |  |
| 直播间名称 | room_name | varchar |  |  |  |
| 短视频ID | video_id | varchar |  |  |  |
| 团长ID | activity_user_id | varchar |  |  |  |
| 团长昵称 | activity_user_name | varchar |  |  |  |
| 团长服务费率 | investment_promotion_rate | decimal(19,4) |  |  |  |
| 团长服务费金额 | investment_promotion_amount | decimal(19,4) |  |  |  |
| 流量渠道 | flow_tools | varchar |  |  |  |
| 流量类型 | flow_type | varchar |  |  |  |
| 商家预估支出 | shop_estimated_commission | decimal(19,4) |  |  |  |
| 备注 | remark | varchar |  |  |  |
| 备用字段1 | reserve_field1 | decimal(19,4) |  |  |  |
| 备用字段2 | reserve_field2 | varchar |  |  |  |
| 备用字段3 | reserve_field3 | varchar |  |  |  |
| 修改时间 | modified | datetime |  |  |  |
| 数据创建时间 | created | datetime |  |  |  |
| 下单时间 | order_time | datetime |  |  |  |
| 支付时间 | pay_time | datetime |  |  |  |
| 完成时间 | end_time | datetime |  |  |  |
| 商品ID | goods_id | varchar |  |  |  |
| 规格ID | spec_id | varchar |  |  |  |


### logistics_multi_query_Y：查询多物流单号

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `logistics_multi_query_Y` |
| PHP 文件 | `logistics_multi_query.php` |
| 文档标题 | 多物流单号 |
| 描述 | 获取旺店通ERP多物流单号 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=logistics_multi_query_Y |

#### 接口说明

| 1.1 接口描述：获取旺店通ERP多物流单号 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：获取旺店通ERP多物流单号 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/logistics_multi_query.php |
| 正式环境 | https://openapi.huice.com/openapi/logistics_multi_query.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once '../WdtClient.php';<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/logistics_multi_query.php';<br><br>    $c->putApiParam('page_no', 0);<br>    $c->putApiParam('page_size', 10);<br>    $c->putApiParam('trade_no', "JY2511264104");<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 是 | 按创建时间增量获取数据,start_time作为开始时间,格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按创建时间增量获取数据,end_time作为结束时间,格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int | 10 | 否 | 每页返回条数，输入值范围1~100，不传默认40，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 物流单号 | logistics_no | varchar | 40 | 否 | 按照物流单号单独查询，不校验时间范围 |
| 系统订单编号 | trade_no | varchar | 40 | 否 | 按照系统订单编号单独查询，不校验时间范围 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 调拨单数据 | logistics_multi_list | data[] |  | 否 | 调拨单数据节点 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": "2",<br>    "logistics_multi_list": [<br>        {<br>            "weight": "0.0000",<br>            "rec_id": "2789146342570590210",<br>            "operator_name": "",<br>            "trade_id": "2766720490100757520",<br>            "trade_no": "JY2511264104",<br>            "logistics_no": "YT3761167080941",<br>            "logistics_id": "2703626668085346307",<br>            "logistics_name": "圆通速递-测试",<br>            "post_cost": "0.0000",<br>            "print_status": 0,<br>            "create": "2026-01-27 13:51:49"<br>        },<br>        {<br>            "weight": "0.0000",<br>            "rec_id": "2789146342570591234",<br>            "operator_name": "",<br>            "trade_id": "2766720490100757520",<br>            "trade_no": "JY2511264104",<br>            "logistics_no": "YT3761166815249",<br>            "logistics_id": "2703626668085346307",<br>            "logistics_name": "圆通速递-测试",<br>            "post_cost": "0.0000",<br>            "print_status": 0,<br>            "create": "2026-01-27 13:51:49"<br>        }<br>    ]<br>} |
| --- | --- |


#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键 | rec_id | bigint | 20 | 是 | 多物流单号主键 |
| 操作人 | operator_name | int | 11 | 是 | 操作人姓名 |
| 订单编号 | trade_no | varchar | 40 | 是 |  |
| 物流单号 | logistics_no | varchar |  | 是 |  |
| 物流公司名称 | logistics_name | varchar |  | 是 |  |
| 重量 | weight | decimal |  | 是 |  |
| 邮资 | post_cost | decimal |  | 是 |  |
| 多物流打印状态 | print_status | tinyint |  | 是 | 0未打印，1已打印 |
| 创建时间 | created | datetime |  | 是 | 创建时间,时间格式：yyyy-MM-dd HH:mm:ss |


#### 响应示例

### JSON

```text
{
    "code": 2900,
    "message": "时间范围不能为空"
}
```


### xsd_upload_media_Y：小时达订单图片回传

| 项目 | 内容 |
|---|---|
| 分类 | 订单类 |
| 服务名 | `xsd_upload_media_Y` |
| PHP 文件 | `xsd_upload_media.php` |
| 文档标题 | 小时达订单图片回传 |
| 描述 | 小时达订单图片回传 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=xsd_upload_media_Y |

#### 接口说明

| 1.1 接口描述：用于小时达订单回传平台图片，例如美团鲜花类目配送前需要先上传图片。 |
| --- |
| 1.2 注意事项：图片大小受限于对应平台。例如美团限制图片大小限制为10M，长宽比例需要限制为4:3。 |


#### 调用场景

| 2.1 举例说明：SAP、线下ERP、SRM、SCM等系统对接 |
| --- |


#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/xsd_upload_media.php |
| 正式环境 | https://openapi.huice.com/openapi/xsd_upload_media.php |


#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/xsd_upload_media.php';<br><br>	$uploadJson = '{<br>			"tid":"4033340323853971099",<br>			"shop_id":486,<br>			"media_list":[<br>				{<br>				"url":"http://p0.meituan.net/xianfu/63d5cb4cf120c89da74c1dd3e7c8bae651375.jpg",<br>				"type":0<br>				}<br>			]<br>		}';<br><br>	$c->putApiParam('upload', $uploadJson);<br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA | package com.erpx.api.trade;<br><br>import com.erpx.api.CommonConstants;<br>import com.erpx.api.WdtClient;<br>import java.io.IOException;<br>import java.util.HashMap;<br>import java.util.Map;<br><br>public class XsdUploadMediaService {<br><br>    public static void main(String[] args) {<br>        WdtClient client = new WdtClient(<br>            "test",<br>            CommonConstants.appkey,<br>            CommonConstants.appSecret,<br>            CommonConstants.baseUrlProd<br>        );<br>        try {<br>            Map<String, String> params = new HashMap<>();<br>            params.put(<br>                "upload",<br>                "{\"tid\":\"T202604280001\",\"shop_id\":1001,\"media_list\":[{\"url\":\"https://example.com/media/image1.jpg\",\"type\":0},{\"url\":\"https://example.com/media/image2.jpg\",\"type\":0}]}"<br>            );<br>            String result = client.execute("xsd_upload_media.php", params);<br>        } catch (IOException e) {<br>            throw new RuntimeException(e);<br>        }<br>    }<br>} |
| C# |  |
| python |  |


#### 业务请求参数

| 名称 | 字段 | 类型 | 父级字段 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- | --- |
| 上传数据 | upload | varchar |  |  | 是 | 字符的 json对象格式例如：{  "tid": "T202604280001",  "shop_id": 1001,  "media_list": [    {      "url": "https://example.com/media/image1.jpg",      "type": 0    },    {      "url": "https://example.com/media/image2.jpg",      "type": 0    }  ]} |
| 平台订单号 | tid | varchar | upload |  | 是 |  |
| 店铺ID | shop_id | int | upload |  | 是 |  |
| 文件列表 | media_list | 数组 | upload |  | 是 | [    {      "url": "https://example.com/media/image1.jpg",      "type": 0    },    {      "url": "https://example.com/media/image2.jpg",      "type": 0    }  ]} |
| 文件url | url | varchar | media_list |  | 是 | 文件url |
| 类型 | type | varchar | media_list |  | 是 | 类型 0 图片 |


#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |


#### 响应示例

### JSON

```text

```

### JSON

```text
{
    "code": 2900,
    "message": "必传参数缺失 param参数错误，请参照接口文档！",
    "resultList": [

    ],
    "success": false
}
```


## 相关页面

- [[domains/ecommerce-ops/api/wangdian/index|旺店通开放平台 API 知识库]]
- [[domains/ecommerce-ops/api/wangdian/capability-map|旺店通 API 能力地图]]
- [[domains/ecommerce-ops/api/wangdian/skill-building-guide|旺店通 API Skill 创建指南]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
