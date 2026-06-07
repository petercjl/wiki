---
title: 旺店通开放平台 API 全量抓取归档
type: source-summary
created: 2026-06-03
updated: 2026-06-03
domain: ecommerce-ops
tags: [ecommerce, erp, wangdian, api]
sources:
  - https://open.wangdian.cn/Y/open/apidoc
status: active
---

# 旺店通开放平台 API 全量抓取归档

> Raw source generated from Chrome DevTools MCP on 2026-06-03. This file preserves the public API documentation content in Markdown form for search and AI retrieval. The machine-readable raw JSON is `raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json`.

- Source URL: https://open.wangdian.cn/Y/open/apidoc
- Scraped at: 2026-06-03T05:12:10.440Z
- Endpoint count: 77
- Error count: 0

## 分类目录

- 订单类: 17 个接口
- 库存类: 23 个接口
- 货品类: 10 个接口
- 基础类: 16 个接口
- 售后类: 6 个接口
- 采购类: 5 个接口

## 订单类

| 服务名 | 接口名 | 描述 | 客户端路径 |
| --- | --- | --- | --- |
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

### trade_push_Y - 创建原始订单

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=trade_push_Y
- PHP file: trade_push.php
- Doc title: 创建原始订单
- Client path: 订单→订单管理→平台订单
- Description: ①推送销售订单给ERP ；②更新已推送成功的销售订单。

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

| JSON | {<br>    'code': 0,<br>    'message': "",<br>    'new_count': 1,<br>    'chg_count': 0<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、分销系统、全渠道等系统对接 |
| --- |


### sales_trade_batch_change_Y - 批量订单换货

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_batch_change_Y
- PHP file: 
- Doc title: 
- Client path: 订单→订单管理→待审核
- Description: 获取批量订单换货

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "trade_nos": [<br>        "JY2508290053"<br>    ],<br>    "trade_ids": [<br>        "2734447459538305026"<br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 1020,<br>    "message": "请勿重复操作",<br>    "trade_nos": null,<br>    "trade_ids": null<br>} |
| --- | --- |


### sales_trade_simple_change_Y - 单笔订单换货

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_simple_change_Y
- PHP file: sales_trade_simple_change.php
- Doc title: 单笔换货
- Client path: 订单→订单管理→待审核
- Description: 获取单笔订单换货

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "trade_nos": [<br>        "JY2509150164"<br>    ],<br>    "trade_ids": [<br>        "2740612153277939735"<br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 2830,<br>    "message": "参数值无效"<br>} |
| --- | --- |


### logistics_sync_query_Y - 查询物流同步

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=logistics_sync_query_Y
- PHP file: logistics_sync_query.php
- Doc title: 查询物流同步
- Client path: 
- Description: 旺店通ERP销售订单的发货状态、物流单号等同步给其他系统，注：”查询物流同步”与“物流同步回写”两个接口配合使用，完成“销售订单发货同步”，​仅支持自有/其它平台店铺

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

| JSON | {<br>    "code": 1007,<br>    "message": "店铺ID不存在"<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、分销系统、全渠道等系统对接 |
| --- |


### logistics_sync_ack_Y - 物流同步回写

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=logistics_sync_ack_Y
- PHP file: logistics_sync_ack.php
- Doc title: 物流同步回写
- Client path: 
- Description: 将物流同步（发货状态、物流单号等）是否成功的结果批量回传给旺店通ERP。

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

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"errors": [{<br>		"rec_id": "1",<br>		"error": "物流同步结果回传失败,同步表不存在,packId:1"<br>	}]<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、分销系统、全渠道等系统对接 |
| --- |


### sales_trade_tags_modify_Y - 修改订单标签

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_tags_modify_Y
- PHP file: sales_trade_tags_modify.php
- Doc title: 修改订单标签
- Client path: 
- Description: 修改订单标签

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "trade_nos": [<br>        "JY2511251482"<br>    ],<br>    "trade_ids": [<br>        "2766250315173855241"<br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 2830,<br>    "message": "系统订单Id无效:276625031517385524100"<br>} |
| --- | --- |


### trade_query_Y - 系统订单（系统订单查询）

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=trade_query_Y
- PHP file: trade_query.php
- Doc title: 查询系统订单
- Client path: 
- Description: 查询ERP内订单

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

| JSON | {<br>    "code": 2900,<br>    "message": "时间范围与订单编号不能全部为空"<br>} |
| --- | --- |


### vip_api_trade_query_Y - 查询原始订单

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_api_trade_query_Y
- PHP file: vip_api_trade_query.php
- Doc title: 查询原始订单
- Client path: 订单→订单管理→平台订单
- Description: 查询原始订单

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

| JSON | {<br>    "code": 1060,<br>    "message": "充值余额为0或应用已欠费，请联系商务充值 "<br>} |
| --- | --- |

#### 其他表格

| 2.1 查询平台原始订单 |
| --- |


### stockout_order_query_trade_Y - 销售出库单

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stockout_order_query_trade_Y
- PHP file: stockout_order_query_trade.php
- Doc title: 销售出库单
- Client path: 
- Description: 查询平台销售出库单

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

| JSON | {<br>    "code": 2900,<br>    "message": "时间范围与订单编号不能全部为空"<br>} |
| --- | --- |

#### 其他表格

| 2.1 查询平台原始订单 |
| --- |


### sales_trade_modify_Y - 修改系统订单

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_modify_Y
- PHP file: sales_trade_modify.php
- Doc title: 修改系统订单 仓库 物流
- Client path: 
- Description: 修改旺店通erp内订单的订单标记

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

| JSON | {<br>  "code": 0,<br>  "message":""<br>} |
| --- | --- |

| JSON | {<br>  "code": 2900,<br>  "message": "必传参数缺失入参：warehouse_id 和logistics_id不能同时为空"<br>} |
| --- | --- |

#### 其他表格

| 2.1 修改旺店通erp内订单的订单标记，用来修改系统订单的仓库和物流，支持对一个订单进行操作  可以仅仅修改 仓库 ，或者仅仅修改物流 ，或者都修改。（仅支持修改待审核状态的订单的仓库） |
| --- |


### sales_trade_replenish_Y - 创建补发订单

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_replenish_Y
- PHP file: sales_trade_replenish.php
- Doc title: 创建补发订单
- Client path: 
- Description: 创建补发订单

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "trade_nos": [<br>        "JY2601280003"<br>    ],<br>    "trade_ids": [<br>        "2789447850105241602"<br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 30401,<br>    "message": "传入的spec_no错误"<br>} |
| --- | --- |


### stockout_order_query_trade_cancel_Y - 撤销发货的销售出库单查询

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stockout_order_query_trade_cancel_Y
- PHP file: stockout_order_query_trade_cancel.php
- Doc title: 撤销发货的销售出库单查询
- Client path: 
- Description: 销售出库单是基于订单的，订单可以撤销发货。当前接口是用于查询历史的撤销的已发货订单数据。举例：订单JY20250001在2025-01-01 12:00:00第一次发货， 在2025-01-01 12:30:00撤销发货。

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

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |


### sales_trade_batch_remark_flag_Y - 批量修改系统订单的标旗和备注

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_trade_batch_remark_flag_Y
- PHP file: sales_trade_batch_remark_flag.php
- Doc title: 批量修改系统订单的标旗和备注
- Client path: 
- Description: 批量修改系统订单的标旗和备注

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "errors": [<br><br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 1020,<br>    "message": "系统异常，请稍后再试！",<br>    "errors": [<br><br>    ]<br>} |
| --- | --- |


### xsd_self_delivery_location_callback_Y - 小时达自配送三方运力回传状态和位置接口

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=xsd_self_delivery_location_callback_Y
- PHP file: xsd_self_delivery_location_callback.php
- Doc title: 小时达自配送三方运力回传状态和位置接口
- Client path: 
- Description: 小时达自配送三方运力回传状态和位置接口

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

| JSON | {<br>    "code": 30400,<br>    "message": "订单号在系统中不存在，请确认传值是否正确"<br>} |
| --- | --- |


### api_trade_live_extend_query_Y - 查询直播主播信息

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=api_trade_live_extend_query_Y
- PHP file: api_trade_live_extend_query.php
- Doc title: 查询直播主播信息
- Client path: 
- Description: 获取租户系统内平台订单的直播信息扩展

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


### logistics_multi_query_Y - 查询多物流单号

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=logistics_multi_query_Y
- PHP file: logistics_multi_query.php
- Doc title: 多物流单号
- Client path: 
- Description: 获取旺店通ERP多物流单号

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

| JSON | {<br>    "code": 2900,<br>    "message": "时间范围不能为空"<br>} |
| --- | --- |


### xsd_upload_media_Y - 小时达订单图片回传

- Category: 订单类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=xsd_upload_media_Y
- PHP file: xsd_upload_media.php
- Doc title: 小时达订单图片回传
- Client path: 
- Description: 小时达订单图片回传

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

| JSON |  |
| --- | --- |

| JSON | {<br>    "code": 2900,<br>    "message": "必传参数缺失 param参数错误，请参照接口文档！",<br>    "resultList": [<br><br>    ],<br>    "success": false<br>} |
| --- | --- |


## 库存类

| 服务名 | 接口名 | 描述 | 客户端路径 |
| --- | --- | --- | --- |
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

### api_goods_stock_change_query_Y - 查询库存同步

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=api_goods_stock_change_query_Y
- PHP file: api_goods_stock_change_query.php
- Doc title: 查询库存同步
- Client path: 仓储→库存同步
- Description: 获取变化后的旺店通ERP可销库存，并同步至平台店铺,

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "stock_change_list": [<br>        {<br>            "rec_id": "2754327482516635662",<br>            "shop_id": "585",<br>            "goods_id": "E1222666614528A",<br>            "spec_id": "34442266254221",<br>            "sync_stock": 6,<br>            "stock_change_count": 4<br>        }<br>    ],<br>    "current_count": 1<br>} |
| --- | --- |

| JSON | {<br>    "code": 2310,<br>    "message": "店铺编号在系统中不存在或已停用，请检查shop_id是否正确"<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、分销系统、全渠道等系统对接 |
| --- |


### stockout_order_query_Y - 查询出库单管理

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stockout_order_query_Y
- PHP file: stockout_order_query.php
- Doc title: 查询出库单管理
- Client path: 仓储→出库管理
- Description: 获取旺店通ERP的各种业务类型的出库单就其明细信息

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

| JSON | {<br>    "code": 11000000,<br>    "message": "时间查询范围不能超过30天，请缩小搜索范围！"<br>} |
| --- | --- |


### stockin_order_query_Y - 查询入库单管理

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stockin_order_query_Y
- PHP file: stockin_order_query.php
- Doc title: 查询入库单管理
- Client path: 仓储→入库管理
- Description: 获取旺店通ERP的各种业务类型的入库单就其明细信息

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


### api_goods_stock_change_ack_Y - 库存同步回写

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=api_goods_stock_change_ack_Y
- PHP file: api_goods_stock_change_ack.php
- Doc title: 库存同步回写
- Client path: 
- Description: 库存量同步至平台是否成功的状态批量回传给旺店通ERP 注：仅支持自有/其他平台店铺

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "errors": [<br><br>    ]<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、分销系统、全渠道等系统对接 |
| --- |


### stockin_order_push_Y - 创建入库单

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stockin_order_push_Y
- PHP file: stockin_order_push.php
- Doc title: 创建入库单
- Client path: 仓储→入库管理
- Description: 调用本接口在旺店通ERP创建对应类型的入库单，增加库存。

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

| JSON | {<br>    "code":0,<br>    "message":"",<br>    "stockin_no":"RK2512300005",<br>    "fail_item_list":null<br>} |
| --- | --- |

| JSON | {<br>    "code":21000003,<br>    "message":"必要参数缺失：src_order_type"<br>} |
| --- | --- |

#### 其他表格

| 2.1 线下ERP、SAP等系统对接 |
| --- |


### stock_sync_by_pd_Y - 创建盘点单

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_sync_by_pd_Y
- PHP file: stock_sync_by_pd.php
- Doc title: 创建盘点单
- Client path: 仓储→仓库盘点
- Description: 旺店通ERP库存需要调整时，推送盘点库存单据给旺店通ERP，覆盖旺店通ERP实物库存。 注：旺店通ERP盘点成功后，盘点单内的库存值直接覆盖前库存

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "pd_no": null,<br>    "warning": []<br>} |
| --- | --- |

| JSON | {<br>    "code": 21000006,<br>    "message": "外部单号重复，请保证外部单号[api_outer_no]的唯一性"<br>} |
| --- | --- |


### stock_query_Y - 查询可用库存

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_query_Y
- PHP file: stock_query.php
- Doc title: 查询库存成本 可用库存数据
- Client path: 仓储→库存查询
- Description: 查询库存成本 可用库存数据

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

| JSON | {<br>    "code": 21000024,<br>    "message": "未查询到任何货品，请检查商家编码（新）是否正确！"<br>} |
| --- | --- |


### stockout_order_push_Y - 创建出库单

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stockout_order_push_Y
- PHP file: stockout_order_push.php
- Doc title: 创建出库单
- Client path: 仓储→出库管理
- Description: 推送出库单给旺店通ERP，并执行出库操作（扣减库存等）

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "stockout_no": "CKQ2602130001",<br>    "fail_item_list": null<br>} |
| --- | --- |

| JSON | {<br>    "code": 21000011,<br>    "message": "当前仓库中不存在货位: 0090"<br>} |
| --- | --- |

#### 其他表格

| 2.1 线下ERP、SAP等系统对接 |
| --- |


### pick_status_ack_Y - 分拣单状态回写接口

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=pick_status_ack_Y
- PHP file: pick_status_ack.php
- Doc title: 分拣单状态回传
- Client path: 仓储→分拣单管理
- Description: 修改租户系统内分拣单的状态

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "send_fail_list": null<br>} |
| --- | --- |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "send_fail_list": [<br>        {<br>            "trade_no": "JY2601080728",<br>            "error": "发货异常:订单已其他系统发货"<br>        }<br>    ]<br>} |
| --- | --- |

#### 其他表格

| 2.1 分拣设备 |
| --- |


### pick_order_query_Y - 查询分拣单接口

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=pick_order_query_Y
- PHP file: pick_order_query.php
- Doc title: 查询分拣单接口
- Client path: 仓储→分拣单管理
- Description: 获取旺店通ERP分拣单信息

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

#### 其他表格

| 2.1 对接分拣机系统 |
| --- |


### pick_trade_query_Y - 查询分拣单订单

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=pick_trade_query_Y
- PHP file: pick_trade_query.php
- Doc title: 查询分拣单订单
- Client path: 仓储→分拣单管理
- Description: 获取租户系统内分拣单的订单信息

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

#### 其他表格

| 2.1 对接分拣机系统 |
| --- |


### stock_detail_report_query_Y - 查询出入库明细表

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_detail_report_query_Y
- PHP file: stock_detail_report_query.php
- Doc title: 查询出入库明细表
- Client path: 
- Description: 查询出入库明细表数据

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


### stock_inout_sn_query_Y - 查询出入库序列号

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_inout_sn_query_Y
- PHP file: stock_inout_sn_query.php
- Doc title: 查询出入库序列号
- Client path: 仓储→出库管理/入库管理
- Description: 获取旺店通ERP各种业务类型的SN出入库明细

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

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |


### stock_transfer_query_Y - 查询调拨单及明细

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_transfer_query_Y
- PHP file: stock_transfer_query.php
- Doc title: 查询调拨单及明细
- Client path: 仓储→调拨管理
- Description: 获取旺店通ERP调拨单及明细信息

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

| JSON | {<br>    "code": 2830,<br>    "message": "参数值无效status"<br>} |
| --- | --- |


### vip_wms_stockinout_order_push_Y - 创建委外出入库单

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_wms_stockinout_order_push_Y
- PHP file: vip_wms_stockinout_order_push.php
- Doc title: 创建委外出入库单
- Client path: 仓储→委外出入库单管理
- Description: 将要推送至WMS等第三方系统的委外出入库单创建到ERP

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "outsource_no": "WK2604130002"<br>} |
| --- | --- |

| JSON | {<br>    "code": 21000006,<br>    "message": "外部单号重复，请保证外部单号[api_outer_no]的唯一性"<br>} |
| --- | --- |


### stock_goods_sn_query_Y - 序列号管理查询接口

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_goods_sn_query_Y
- PHP file: stock_goods_sn_query.php
- Doc title: 序列号管理查询接口
- Client path: 仓储→序列号管理
- Description: 获取旺店通ERP各种业务类型的SN出入库明细

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

| JSON | {<br>	"code": 2180,<br>	"message": "start_time与end_time时间跨度不能超过最大范围30天"<br>} |
| --- | --- |

#### 其他表格

| 2.1 财务系统、SAP、数据分析等系统的对接 |
| --- |


### stock_production_order_query_Y - 查询生产加工单接口

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_production_order_query_Y
- PHP file: stock_production_order_query.php
- Doc title: 查询生产加工单接口
- Client path: 仓储→生产加工
- Description: 获取旺店通ERP生产加工单数据

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

| JSON | {<br>	"code": 2180,<br>	"message": "start_time与end_time时间跨度不能超过最大范围30天"<br>} |
| --- | --- |

#### 其他表格

| 2.1 财务系统、SAP、数据分析等系统的对接 |
| --- |


### stock_full_query_Y - 全量查询库存

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_full_query_Y
- PHP file: stock_full_query.php
- Doc title: 全量库存查询
- Client path: 仓储→库存查询
- Description: 全量获取系统库存管理数据

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

| JSON | {<br>	"code": 2180,<br>	"message": "xxxxxxxx"<br>} |
| --- | --- |


### stock_transfer_create_Y - 创建调拨单

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_transfer_create_Y
- PHP file: stock_transfer_create.php
- Doc title: 创建调拨单
- Client path: 仓储→调拨管理
- Description: ERP内仓与仓之间的库存需要调度时，推送调拨单给ERP

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

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"transfer_no": "DB2603030002"<br>} |
| --- | --- |

| JSON | {<br>    "code":21000003,<br>    "message":"必要参数缺失：src_order_type"<br>} |
| --- | --- |


### stock_outsource_order_query_Y - 查询委外出入库单

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stock_outsource_order_query_Y
- PHP file: stock_outsource_order_query.php
- Doc title: 查询委外出入库单
- Client path: 仓储-委外出入库单界面
- Description: 查询erp委外出库单、入库单数据

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

| JSON | {<br>	"code": 2160,<br>	"message": "start_time和end_time为空或不是有效的时间格式"<br>} |
| --- | --- |

#### 其他表格

| 2.1 数据分析、SAP、财务系统等系统对接 |
| --- |


### operational_order_create_Y - 运营仓单据创建

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=operational_order_create_Y
- PHP file: operational_order_create.php
- Doc title: 运营仓单据创建
- Client path: 仓储->运营仓管理->运营仓单据
- Description: 通过接口推送创建运营仓管理-运营仓单据到旺店通erp系统

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

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"order_no": "OP2604090006"<br>} |
| --- | --- |

| JSON | {<br>	"code": 1020,<br>	"message": "商家编码(新):【951027】分配数量不可超过公共可用库存",<br>	"order_no": null<br>} |
| --- | --- |

#### 其他表格

| 2.1 线下ERP等系统对接 |
| --- |


### operational_order_query_Y - 运营仓单据查询

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=operational_order_query_Y
- PHP file: operational_order_query.php
- Doc title: 运营仓单据查询
- Client path: 仓储->运营仓管理->运营仓单据管理
- Description: 查询旺店通erp系统运营仓单据数据信息

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

| JSON | {<br>	"code": 2180,<br>	"message": "start_time与end_time时间跨度不能超过最大范围30天"<br>} |
| --- | --- |

#### 其他表格

| 2.1 财务系统、SAP、数据分析等系统的对接 |
| --- |


### operational_stock_detail_query_Y - 运营仓库存明细查询

- Category: 库存类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=operational_stock_detail_query_Y
- PHP file: operational_stock_detail_query.php
- Doc title: 运营仓库存明细查询
- Client path: 仓储->运营仓管理->运营仓库存明细
- Description: 查询旺店通erp系统运营仓库存明细数据

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

| JSON | {<br>	"code": 2180,<br>	"message": "xxxxxxxx"<br>} |
| --- | --- |


## 货品类

| 服务名 | 接口名 | 描述 | 客户端路径 |
| --- | --- | --- | --- |
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

### vip_api_goods_query_Y - 平台货品查询

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_api_goods_query_Y
- PHP file: vip_api_goods_query.php
- Doc title: 查询平台货品
- Client path: 商品→平台商品
- Description: 获取ERP的平台货品信息

#### 接口说明

| 1.1 接口描述：获取ERP的平台货品信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取：按照平台货品的最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天。开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |
| 1.5注意事项：权限校验：【店铺、仓库权限】为了达到保护用户隐私数据安全的目的，本接口不返回淘系、拼多多及系统供销平台数据，相关平台规则点击这里，淘系及系统供销平台数据获取办法点击这里，拼多多请自行对接平台获取。本接口中涉及到用户隐私的字段数据仅有自有平台及线下平台订单返回。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/vip_api_goods_query.php |
| 正式环境 | https://openapi.huice.com/openapi/vip_api_goods_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版APi服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | APi输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/vip_api_goods_query.php';<br><br>    //添加查询参数<br>    $c->putApiParam('start_time','2019-01-01 00:00:00');<br>    $c->putApiParam('end_time','2019-01-30 00:00:00');<br>    $c->putApiParam('page_no', '0');<br>    $c->putApiParam('page_size','10');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAvA |  |
| C# |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量查询数据，start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量查询数据，end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~1000，不传本参数，输入值默认为100，使用举例单击这里 |
| 页号 | page_no | int |  | 否 | 页号，不传默认从0页开始 |
| 店铺id | shop_id | varchar |  | 否 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 数据总条数，用来分页 |
| 平台商品列表节点 | goods_list | data[ ] |  | 是 | 响应参数的级数据节点，包含当前页的库存管理信息的数据节点，节点下数据字段详见下述“goods_list”列表 |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"total_count": 192,<br>	"goods_list": [{<br>		"shop_id": "266",<br>		"api_goods_id": "2506100000016670",<br>		"api_spec_id": "2506100000016730",<br>		"rec_id": "2705524893792862225",<br>		"platform_id": 127,<br>		"is_deleted": 0,<br>		"status": 2,<br>		"outer_id": "2506100000016670",<br>		"api_goods_name": "菲力牛排-多规格",<br>		"api_spec_name": "【爆款推荐】M3眼肉牛排1.5KG_3kg",<br>		"spec_outer_id": "347",<br>		"spec_code": "347",<br>		"stock_num": null,<br>		"match_target_type": 0,<br>		"match_code": "",<br>		"merchant_name": null,<br>		"merchant_code": null,<br>		"merchant_no": null,<br>		"match_target_id": "0",<br>		"price": "0.0000",<br>		"cid": "",<br>		"pic_url": "https:\/\/ody-offline-product.obs.cn-east-2.myhuaweicloud.com\/dev\/ouser-web\/1749609750275_60.36053469495526_fdf0fc16-445f-452e-9c00-1555c3b09dd7.jpg",<br>		"barcode": "",<br>		"brand_id": null,<br>		"class_id_path": null,<br>		"modified": "2025-06-11 10:45:02"<br>	}]<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 必须 | 描述 |
| --- | --- | --- | --- | --- |
| 店铺id | shop_id | int(11) | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 平台货品id | api_goods_id | string | 是 |  |
| 平台规格id | api_spec_id | string | 是 |  |
| 平台货品表id | rec_id | bigint(20) | 是 |  |
| 平台id | platform_id | int(11) | 是 | 点击查看平台ID详情 |
| 活动状态 | is_deleted | tinyint(4) | 是 | 0正常货品，1 删除， |
| 平台货品状态 | status | tinyint(4) | 是 | 0删除1在架2下架 |
| 平台货品编码 | outer_id | string | 是 |  |
| 平台货品名称 | api_goods_name | string | 是 |  |
| 平台规格名称 | api_spec_name | string | 是 |  |
| 平台规格编码 | spec_outer_id | string | 是 |  |
| 平台规格码 | spec_code | string | 是 |  |
| 平台库存 | stock_num | decimal(19, 4) | 是 | 该字段目前不返回 |
| 匹配类型 | match_target_type | tinyint(4) | 是 | 0未匹配，1匹配单品商家编码，2匹配组合装商家编 |
| 匹配编码 | match_code | string | 是 |  |
| 系统货品名称 | merchant_name | string | 是 | match_target_type=1时返回的为单品货品名称、match_target_type=2时返回的为组合装货品名称 |
| 系统规格名称 | merchant_code | string | 是 | match_target_type=1时返回的为单品规格名称、match_target_type=2时返回为“空” |
| 系统商家编码 | merchant_no | string | 是 | match_target_type=1时返回的为单品商家编码、match_target_type=2时返回的为组合装商家编码 |
| 系统商家编码主键id | match_target_id | string | 是 | 1是单品id，2是组合装id |
| 价格 | price | decimal(19, 4) | 是 |  |
| 类目 | cid | string | 否 |  |
| 图片链接 | pic_url | string | 是 |  |
| 条码 | barcode | string | 否 |  |
| 品牌id | brand_id | int(11) | 否 |  |
| 最后修改时间 | modified | datetime | 是 |  |
| 平台成本价 | platform_cost_price | decimal(19, 4) | 是 | 平台成本价 |

#### 响应示例

| JSON | {<br>    "code": 2104,<br>    "message": "start_time与end_time时间跨度不能超过最大范围 30天"<br>} |
| --- | --- |

#### 其他表格

| 2.1 其他 |
| --- |


### goods_query_Y - 查询货品档案

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=goods_query_Y
- PHP file: goods_query.php
- Doc title: 查询货品档案
- Client path: 商品→系统货品
- Description: 获取旺店通ERP的货品档案资料，“货品档案”其他系统称为“物料档案”“商品档案”等

#### 接口说明

| 1.1 接口描述：获取旺店通ERP的货品档案资料，“货品档案”其他系统称为“物料档案”“商品档案”等 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取：按照旺店通ERP内货品档案最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件，返回的结果不包含在旺店通ERP货品档案已停用的货品数据。         全量获取：支持不传start_time和end_time 时间查询，不传时间入参分页获取全量货品数据。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |
| 1.4 注意事项：本接口如果不传start_time和end_time，则spec_no和goods_no必须传一个；当请求参数传了spec_no和goods_no其中一个或者两个都传了的时候，start_time和end_time参数不生效。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/goods_query.php |
| 正式环境 | https://openapi.huice.com/openapi/goods_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec_no | varchar | 255 | 否 | 代表单品（SKU）所有属性的唯一编码，用于获取指定的系统单品的数据，SKU概念介绍，单击这里，单独查询可不传时间范围 |
| 货品编号 | goods_no | varchar | 40 | 否 | 代表货品(SPU)所有属性的唯一编号，用于指定获取系统货品的数据，SPU概念介绍，单击这里，单独查询可不传时间范围 |
| 条码 | barcode | varchar | 50 | 否 | 条码 |
| 品牌 | brand_name | varchar | 64 | 否 | 品牌名称 |
| 货品分类名称 | category_name | varchar | 40 | 否 | 货品分类名称 |
| 开始时间 | start_time | timestamp |  | 是 | 按最后修改时间增量查询数据，start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | timestamp |  | 是 | 按最后修改时间增量查询数据，end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 是否隐藏删除数据 | hide_deleted | int |  | 否 | 默认为0, 0：返回未删除和已删除货品1：只返回未删除货品 |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为40，使用举例单击这里 |
| 页号 | page_no | int |  | 否 | 页号，不传默认从0页开始 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品ID | goods_id | int | 11 | 是 | 货品表主键 |
| 货品编号 | goods_no | varchar | 255 | 是 | 代表SPU所有属性的唯一编号，用于系统货品的区分，SPU概念介绍，单击这里 |
| 货品名称 | goods_name | varchar | 255 | 是 | 货品名称 |
| 货品简称 | short_name | varchar | 255 | 是 | 货品简称 |
| 规格数 | spec_count | int | 11 | 是 | 规格数 |
| 品牌名称 | brand_name | varchar | 256 | 是 | 品牌名称 |
| 品牌编码 | brand_code | varchar | 128 | 是 | 品牌编码 |
| 最后修改时间 | modified | timestamp |  | 是 | 最后修改时间  格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | timestamp |  | 是 | 创建时间  格式：yyyy-MM-dd HH:mm:ss |
| 分类名称 | class_name | varchar | 40 | 否 | 分类名称 |
| 是否已删除 | deleted | int |  | 是 | 是否已删除： 0：未删除  >0代表已删除 |
| 货品状态 | goods_status | int |  | 是 | 0:启用    4:禁用 |
| 货品分类id | goods_category_id | bigint |  | 否 | 货品分类id |
| 货品分类名称 | category_name | varchar | 40 | 否 | 货品分类名称 |
| 货品类型 | goods_type | tinyint |  |  | 1成品、2半成品、3原料、4包装材料、5辅料、6资产。默认值为：成品 |
| 品牌id | brand_id | int | 11 | 否 | 品牌id |
| 备注 | remark | varchar | 512 | 是 | 备注 |
| 商品标签 | goods_label_name | varchar | 512 | 否 | 商品标签名称按英文逗号拼接的字符 |
| 货品图片 | spu_pic_url | varchar | 1024 | 是 | 货品图片 |
| 自定义属性1 | prop1 | varchar | 255 | 否 | 自定义属性1 |
| 自定义属性2 | prop2 | varchar | 255 | 否 | 自定义属性2 |
| 自定义属性2 | prop3 | varchar | 255 | 否 | 自定义属性3 |
| 自定义属性4 | prop4 | varchar | 255 | 否 | 自定义属性4 |
| 自定义属性5 | prop5 | varchar | 255 | 否 | 自定义属性5 |
| 自定义属性6 | prop6 | varchar | 255 | 否 | 自定义属性6 |
| 自定义属性7 | prop7 | varchar | 255 | 是 | 自定义属性7 |
| 自定义属性8 | prop8 | varchar | 255 | 是 | 自定义属性8 |
| 自定义属性9 | prop9 | varchar | 255 | 是 | 自定义属性9 |
| 自定义属性10 | prop10 | varchar | 255 | 是 | 自定义属性10 |
| 单品节点 | spec_list | data[] |  | 是 | 响应参数的2级数据节点，包含sku所有属性信息的数据节点,节点下数据字段详见下述"spec_list" |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 规格ID | spec_id | bigint |  | 是 | 规格ID |
| 商家编码 | spec_no | varchar | 255 | 是 | 代表单品（SKU）所有属性的唯一编号，用于系统单品的区分，SKU概念介绍，单击这里 |
| 规格名称 | spec_name | varchar | 255 | 是 | 规格名称 |
| 规格简称 | short_name | varchar | 255 | 是 | 规格简称 |
| 条码 | barcode | varchar | 50 | 是 | 条码 |
| 货品ID | goods_id | int | 11 | 是 | 货品ID |
| 零售价 | retail_price | decimal | 19，4 | 是 | 零售价 |
| 批发价 | wholesale_price | decimal | 19，4 | 是 | 批发价 |
| 重量 | weight | decimal | 19，4 | 是 | 重量 |
| 长 | length | decimal | 19，4 | 是 | 长(CM) |
| 宽 | width | decimal | 19，4 | 是 | 宽(CM) |
| 高 | height | decimal | 19，4 | 是 | 高(CM) |
| 单位 | unit | bigint |  | 是 | 单位id |
| 基本单位 | unit_name | varchar | 256 | 是 | 基本单位名称 |
| 辅助单位 | aux_unit | bigint |  | 是 | 辅助单位 |
| 最后修改时间 | modified | timestamp |  | 是 | 最后修改时间    格式：yyyy-MM-dd HH:mm:ss |
| 货品状态 | goods_status | int |  | 是 | 0:启用    4:禁用 |
| 创建时间 | created | timestamp |  | 是 | 创建时间  格式：yyyy-MM-dd HH:mm:ss |
| 是否已删除 | deleted | int |  | 是 | 是否已删除：0：未删除    >0代表已删除 |
| 图片 | img_url | varchar | 1024 | 是 | 规格图片 |
| 供应商编码 | provider_no | varchar | 64 |  | 供应商编码 |
| 供应商名称 | provider_name | varchar | 64 |  | 供应商名称 |
| 供应商id | provider_id | bigint |  |  | 供应商id |
| 成本价 | ref_cost_price | decimal | 19,4 | 否 | 固定成本价 为0 |
| 规格的编号 | spec_code | varchar | 255 |  | 规格的编号，Y当前都为空 |
| 备注 | remark | varchar | 512 | 是 | 备注 |
| 规格自定义属性1 | prop1 | varchar | 255 | 否 | 规格自定义属性1 |
| 规格自定义属性2 | prop2 | varchar | 255 | 否 | 规格自定义属性2 |
| 规格自定义属性2 | prop3 | varchar | 255 | 否 | 规格自定义属性3 |
| 规格自定义属性4 | prop4 | varchar | 255 | 否 | 规格自定义属性4 |
| 规格自定义属性5 | prop5 | varchar | 255 | 否 | 规格自定义属性5 |
| 规格自定义属性6 | prop6 | varchar | 255 | 否 | 规格自定义属性6 |
| 税率 | tax_rate | decimal | 19,4 | 否 | 税率 |
| 默认采购价 | sku_default_purchase_price | decimal | 19,4 | 否 | 默认采购价 |
| 附件 | file_url_list | data[] |  |  | 附件，字符串格式返回 |
| 箱规 | box_sku_num | int | 11 | 否 | 箱规 |
| 商品标签 | goods_label_name | varchar | 512 | 否 | 商品标签名称按英文逗号拼接的字符 |

| PHP | <php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/goods_query.php';<br><br>    //添加查询参数<br>    $c->putApiParam('start_time','2018-08-01 00:00:00');<br>    $c->putApiParam('end_time','2018-08-11 00:00:00');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 11 | 是 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 货品节点 | goods_list | data[] |  | 是 | 响应参数的1级数据节点，包含SPU所有属性信息的数据节点,节点下数据字段详见下述“goods_list”和"spec_list" |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "goods_list": [<br>        {<br>            "goods_id": "2679745084445949979",<br>            "goods_no": "250331101",<br>            "goods_name": "牛大腿",<br>            "short_name": "牛大腿",<br>            "goods_type": 2,<br>            "brand_name": "牛大力",<br>            "brand_id": "2677200835238167570",<br>            "class_name": "",<br>            "spec_count": 1,<br>            "deleted": 0,<br>            "modified": "2026-04-23 10:01:31",<br>            "created": "2025-03-31 16:30:15",<br>            "goods_label_name": "",<br>            "goods_category_id": "2679744097362640923",<br>            "category_name": "牛大腿",<br>            "prop1": "规格类型",<br>            "prop2": "",<br>            "prop3": "",<br>            "prop4": "",<br>            "prop5": "",<br>            "prop6": "",<br>            "prop7": "",<br>            "prop8": "",<br>            "prop9": "",<br>            "prop10": "",<br>            "brand_code": "ndl",<br>            "remark": "货品备注",<br>            "goods_status": 0,<br>            "spec_list": [<br>                {<br>                    "spec_id": "2679745085251256347",<br>                    "goods_id": "2679745084445949979",<br>                    "spec_name": "牛大腿",<br>                    "spec_no": "1122019",<br>                    "spec_code": "",<br>                    "retail_price": "50.0000",<br>                    "wholesale_price": "45.0000",<br>                    "weight": "0.0000",<br>                    "length": "0.0000",<br>                    "width": "0.0000",<br>                    "height": "0.0000",<br>                    "unit": "2625293876239269893",<br>                    "unit_name": "件",<br>                    "aux_unit": 0,<br>                    "deleted": 0,<br>                    "img_url": "https:\/\/erpx-prod.oss-cn-zhangjiakou.aliyuncs.com\/goods\/68b724c4-be61-4668-832e-05ed02298183\/haijun_29aad7e341df417d9a5d352462cb1f4f.png",<br>                    "modified": "2026-04-23 10:01:32",<br>                    "created": "2025-03-31 16:30:15",<br>                    "goods_label_name": "",<br>                    "provider_id": "2819675054202159118",<br>                    "provider_no": "8508",<br>                    "provider_name": "386410152",<br>                    "ref_cost_price": "30.0000",<br>                    "prop1": "",<br>                    "prop2": "",<br>                    "prop3": "",<br>                    "prop4": "",<br>                    "prop5": "",<br>                    "prop6": "",<br>                    "file_url_list": [<br>                        "https:\/\/cdn.pixabay.com\/photo\/2017\/03\/12\/11\/30\/alishan-2136879_1280.jpg"<br>                    ],<br>                    "short_name": "",<br>                    "barcode": "69000",<br>                    "tax_rate": "0.0000",<br>                    "remark": "",<br>                    "box_sku_num": 0,<br>                    "goods_status": 0,<br>                    "sku_default_purchase_price": "0.0000"<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |

#### 响应示例

| JSON | {<br>    "code": "20",<br>    "message": "请求范围过宽，请增加请求参数条件过滤"<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、SCM、SRM、财务系统、SAP等系统的对接 |
| --- |


### api_goodsspec_push_Y - 创建平台货品

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=api_goodsspec_push_Y
- PHP file: api_goodsspec_push.php
- Doc title: 创建平台货品
- Client path: 商品→创建平台货品
- Description: 在推送销售订单给旺店通ERP之前，需要映射匹配ERP系统单品或者设置同步库存的策略时调用 注：仅支持自有/其他平台店铺

#### 接口说明

| 1.1 接口描述：在推送销售订单给旺店通ERP之前，需要映射匹配ERP系统单品或者设置同步库存的策略时调用    注：仅支持自有平台店铺 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 注意事项：①本接口仅支持ERP内店铺平台类型为“自有”的店铺创建平台货品，货品明细一次不能超过2000条；②平台货品SPU下多个SKU，规格ID不能为空，并且店铺名+货品ID+规格ID要唯一，SPU和SKU概念介绍，单击这里 |

#### 调用场景

| 2.1 调用场景：自研商城对接 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/api_goodsspec_push.php |
| 正式环境 | https://openapi.huice.com/openapi/api_goodsspec_push.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once '../WdtClient.php';<br>    $c = new WdtClient();<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/api_goodsspec_push.php';<br><br>    $api_goods_info = array(<br>            'platform_id'=>127,<br>            'shop_id' => 'shop_test',<br>            'goods_list'=>array(<br>                array (<br>                    "status" => "1",<br>                    "goods_id" => "20151009100903",<br>                    "goods_no" => "xjftest002",<br>                    "goods_name" => "test",<br>                    "price" => "1",<br>                    "stock_num" => "2",<br>                    "pic_url" => "",<br>                    "spec_id" => "20151009100903",<br>                    "spec_code" => "test002",<br>                    "spec_name" => "test",<br>                    "spec_no" => "xjftest004"<br>                   )<br>            )<br><br>    );<br><br>    $c->putApiParam('api_goods_info', json_encode($api_goods_info, JSON_UNESCAPED_UNICODE));<br>    $json = $c -> wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品节点 | api_goods_info | data |  | 是 | 请求参数的1级数据节点，包含平台（商城）商品所有属性信息的数据节点，节点下数据字段详见下述“api_goods_info” |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 新增货品个数 | new_count | int | 10 | 是 | 新增货品个数 |
| 更新货品个数 | chg_count | int | 10 | 是 | 更新货品个数 |
| 处理失败的错误列表 | errors | data | data[] | 否 | 处理失败的错误列表,当code为0且有错误信息时才非空.只列出同一批内有错误的记录.如果code=0,errors为空说明全部成功 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 平台ID | platform_id | smallint | 6 | 是 | 详情介绍，单击这里 |
| 店铺id | shop_id | varchar | 20 | 是 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar | 40 |  | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 平台货品节点 | goods_list | data[ ] |  | 是 | 请求参数的2级数据节点，包含平台商品属性信息的数据节点，节点下数据字段详见下述“goods_list” |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品ID | goods_id | varchar | 40 | 是 | 平台系统货品主键，和创建原始订单接口中含义相同，是十分重要的字段，SPU和SKU概念介绍，单击这里,(注意:店铺名+货品ID+规格ID要保证唯一) |
| 规格ID | spec_id | varchar | 40 | 是 | 平台系统货品规格id，SPU和SKU概念介绍，单击这里,(注意:店铺名+货品ID+规格ID要保证唯一) |
| 货品编码 | goods_no | varchar | 40 | 是 | 平台系统货品SPU码，尽量不要为空，SPU和SKU概念介绍，单击这里 |
| 规格编码 | spec_no | varchar | 40 | 是 | 平台系统SKU唯一码，SPU和SKU概念介绍，单击这里 |
| 状态 | status | tinyint | 4 | 是 | 0删除 1在架 2下架 |
| 货品名称 | goods_name | varchar | 255 | 否 | 平台系统货品名称 |
| 平台规格码 | spec_code | varchar | 40 | 否 | 平台系统规格编码 |
| 规格名称 | spec_name | varchar | 100 | 否 | 平台系统规格名称 |
| 图片url | pic_url | varchar | 255 | 否 | 平台系统图片url |
| 货品图片url | spu_pic_url | varchar | 255 | 否 | 平台货品图片url |
| 价格 | price | decimal | 19,4 | 否 | 商品价格 |
| 平台库存 | stock_num | decimal | 19，4 | 否 | 平台上商品的库存量 |
| 平台类目 | cid | varchar | 40 | 否 | 平台系统商品所属类目 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误的goods_id | goods_id | varchar | 40 |  | 错误的goods_id |
| 错误的spec_id | spec_id | varchar | 40 |  | 错误的spec_id |
| 错误信息的描述 | error | varchar | 255 | 否 | 错误信息的描述 |

#### 响应示例

| JSON | {<br>    "code": 0,<br>    "message": "OK",<br>    "new_count": 1,<br>    "chg_count": 0<br>} |
| --- | --- |

| JSON | {<br>    "code": 4304,<br>    "message": "shop_no 对应的店铺所属的平台 与 传入platform_id 不一致 "<br>} |
| --- | --- |


### goods_push_Y - 创建货品档案

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=goods_push_Y
- PHP file: goods_push.php
- Doc title: 创建货品档案
- Client path: 商品→系统货品
- Description: 在ERP内创建货品档案

#### 接口说明

| 1.1 接口描述：①批量推送货品资料给旺店通ERP②批量更新旺店通ERP货品档案资料（支持已经存在的货品（spu），新增单品（sku），good_list中good_no确定sku新增在哪个货品之下，将新增的spec_no以及对应信息放在spec_list，推送成功以后，sku将新增到对应的货品档案（spu）下。） |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 注意事项：更新货品档案时，good_no确认要更新的spu属性信息，good_no+spec_no确认要更新的sku属性信息。更新货品（spu)数据时，good_list中good_no对应的数据做变更，spec_list要包含至少一个已经存在的单品（sku）数据。更新单品（sku)数据时，good_list中good_no对应的数据不变，spec_list中spec_no对应的数据做变更，重新推送成功后，变更部分将会更新到ERP。支持批量推送数据，每个请求建议包含50条以下的“goods_list”数据；goods_list下的spec_list条数不要超过500条 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/goods_push.php |
| 正式环境 | https://openapi.huice.com/openapi/goods_push.php |

| PHP | <?php<br>    require_once('../WdtClient.php');<br>    $c = new WdtClient;<br>    //sid appkey appsecret 需要换成自己的<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    //测试环境地址<br>    //上线时需要换成线上的<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/goods_push.php'; // 测试的<br>    //$c->gatewayUrl = 'https://openapi.huice.com/openapi/goods_push.php'; //正式的<br><br>    $goods_list = new stdClass();<br>    $goods_list->goods_no = "test1";<br>    $goods_list->goods_name = "test1";<br>    $goods_list->short_name = "简称";<br>    $goods_list->brand_name = "测试品牌";<br>    $goods_list->remark = "备注";<br><br>    $spec_item = new stdClass();<br><br>    $spec_item->spec_no = "test1";                  // 商家编码<br>  //  $spec_item->barcode = "1234567890123";         // 主条码<br>  //  $spec_item->spec_name = "商品规格名称";          // 规格名称<br>    $spec_item->lowest_price = 10.50;              // 最低价<br>   // $spec_item->img_url = "http://example.com/img.jpg"; // 图片url地址<br>   // $spec_item->retail_price = 15.00;              // 零售价<br>  //  $spec_item->wholesale_price = 12.00;          // 批发价<br> //   $spec_item->ref_cost_price = 9.00;             // 成本价<br>  //  $spec_item->weight = 0.5;                      // 重量 (kg)<br>    //$spec_item->length = 10.0;                     // 长 (CM)<br>   // $spec_item->width = 5.0;                       // 宽 (CM)<br>  //  $spec_item->height = 2.0;                      // 高 (CM)<br> //   $spec_item->spec_remark = "这是备注信息";        // 备注<br>    $goods_list->spec_list = [$spec_item];<br>    $goods_lists = [$goods_list];<br>    $c->putApiParam("goods_list", json_encode($goods_lists, JSON_UNESCAPED_UNICODE));<br>   //$c->putApiParam("goods_list", '[{"goods_no":"T20240805001","goods_name":"T20240805001","spec_list":[{"spec_no":"SPE20240805001","spec_name":"商城测试sku1"}]}]');<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>    ?> |
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
| 货品节点 | goods_list | data[ ] |  | 是 | 请求参数的1级数据节点，包含SPU所有属性信息的数据节点，节点下数据字段详见下述“goods_list” |

| JSON | {"code":0,"message":"","errors":[{"goods_no":null,"error":"货品名称不能为空"}]} |
| --- | --- |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 处理失败的错误列表 | errors | data | data[] | 否 | 处理失败的错误列表,当code为0且有错误信息时才非空.只列出同一批内有错误的记录.如果code=0,errors为空说明全部成功 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 货品编号 | goods_no | varchar | 40 | 是 | 代表货品(spu)所有属性的唯一编号，用于系统货品区分，，SPU概念介绍,单击这里 |
| 货品名称 | goods_name | varchar | 255 | 是 | 货品名称 |
| 货品简称 | short_name | varchar | 255 | 否 | 货品简称 |
| 品牌 | brand_name | varchar | 64 | 否 | 品牌名称 |
| 备注 | remark | varchar | 512 | 否 | 备注 |
| 货品成本价 | spu_ref_cost_price | decimal | 19,4 | 否 | 货品成本价 |
| 货品图片链接 | spu_img_url | varchar | 1024 | 否 | 货品图片链接 |
| 自定义属性1 | spu_prop1 | varchar | 255 | 否 | 自定义属性1 |
| 自定义属性2 | spu_prop2 | varchar | 255 | 否 | 自定义属性2 |
| 自定义属性3 | spu_prop3 | varchar | 255 | 否 | 自定义属性3 |
| 自定义属性4 | spu_prop4 | varchar | 255 | 否 | 自定义属性4 |
| 自定义属性5 | spu_prop5 | varchar | 255 | 否 | 自定义属性5 |
| 自定义属性6 | spu_prop6 | varchar | 255 | 否 | 自定义属性6 |
| 单品节点 | spec_list | data[] |  | 是 | 请求参数的2级数据节点，包含sku所有属性信息的数据节点,节点下数据字段详见下述"spec_list" |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码 | spec_no | varchar | 40 | 是 | 代表单品(sku)所有属性的唯一编码，用于系统单品区分，SKU概念介绍单击这里 |
| 主条码 | barcode | varchar | 50 | 否 | 主条码 |
| 规格名称 | spec_name | varchar | 100 | 否 | 规格名称 |
| 规格简称 | sku_short_name | varchar | 30 | 否 | 规格简称 |
| 商品标签 | goods_label_name_list | varchar | 255 | 否 | 商品标签，多个商品标签用英文逗号隔开 |
| 税率 | tax_rate | decimal | 19,4 | 否 | 税率 |
| 保质期 | validity_days | int |  | 否 | 保质期不支持小数 |
| 保质期类型 | validity_days_type | varchar | 20 | 否 | 保质期类型(天  月  年) |
| 图片url地址 | img_url | varchar | 1024 | 否 | 图片url地址 |
| 箱规 | box_sku_num | int |  | 否 | 箱规 |
| 零售价 | retail_price | decimal | 19,4 | 否 | 商品标价，系统内手工建单时使用，传值时需谨慎 |
| 批发价 | wholesale_price | decimal | 19,4 | 否 | 批发价 |
| 成本价 | ref_cost_price | decimal | 19,4 | 否 | 成本价 |
| 基本单位 | spec_unit_name | varchar | 40 | 否 | 基本单位 |
| 重量 | weight | decimal | 19,4 | 否 | ERP默认重量单位：kg |
| 长 | length | decimal | 19,4 | 否 | 长(CM) |
| 宽 | width | decimal | 19,4 | 否 | 宽(CM) |
| 高 | height | decimal | 19,4 | 否 | 高(CM) |
| 备注 | spec_remark | varchar | 512 | 否 | 备注 |
| 批准文号 | approval_number | varchar | 64 | 否 | 批准文号 |
| 生产厂家 | producer | varchar | 64 | 否 | 生产厂家 |
| 默认采购价 | sku_default_purchase_price | decimal | 19,4 | 否 | 默认采购价 |
| 默认供应商名称 | default_provider_name | varchar | 255 | 否 | 默认供应商名称 |
| 规格自定义属性1 | prop1 | varchar | 255 | 否 | 规格自定义属性1 |
| 规格自定义属性2 | prop2 | varchar | 255 | 否 | 规格自定义属性2 |
| 规格自定义属性3 | prop3 | varchar | 255 | 否 | 规格自定义属性3 |
| 规格自定义属性4 | prop4 | varchar | 255 | 否 | 规格自定义属性4 |
| 规格自定义属性5 | prop5 | varchar | 255 | 否 | 规格自定义属性5 |
| 规格自定义属性6 | prop6 | varchar | 255 | 否 | 规格自定义属性6 |
| 规格自定义属性7 | prop7 | varchar | 255 | 否 | 规格自定义属性7 |
| 规格自定义属性8 | prop8 | varchar | 255 | 否 | 规格自定义属性8 |
| 规格自定义属性9 | prop9 | varchar | 255 | 否 | 规格自定义属性9 |
| 规格自定义属性10 | prop10 | varchar | 255 | 否 | 规格自定义属性10 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误的货品编号 | goods_no | varchar | 40 | 是 | 错误的goods_no |
| 错误信息的描述 | error | varchar | 255 | 否 | 错误信息的描述 |

#### 响应示例

| JSON | {"code":0,"message":"","errors":[]} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、 |
| --- |


### suites_push_Y - 创建组合装

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=suites_push_Y
- PHP file: suites_push.php
- Doc title: 创建组合装
- Client path: 商品→系统货品
- Description: 创建/更新组合装信息

#### 接口说明

| 1.1 接口描述：仅创建 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3注意事项：如果suite_info中的is_default_ratio=1，即默认按照零售价分摊金额占比，那么suite_detail中的ratio字段不传值，传值也视为无效。如参数suite_info中的is_default_ratio=0，那么ratio必须传值，且总和为1，否则会提示错误。     如果suite_detail中的is_fixed_price=1,则相应的ratio需传0（接口默认处理成0），其他is_fixed_price=0时根据suite_info、is_default_ratio值，进行默认分摊金额占比或者按照指定金额占比处理（如果是指定金额占比，会检验剩下非固定价格行的金额占比之和是否为1）如所有行都选择固定价格，那么最后一行ratio=1，其他行均为0。 |

#### 调用场景

| 2.1 举例说明：满足外部系统——>OMS创建组合装的场景 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/suites_push.php |
| 正式环境 | https://openapi.huice.com/openapi/suites_push.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 |  |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>require_once '../WdtClient.php';<br>$c = new WdtClient();<br>$c->sid = '';<br>$c->appkey = '';<br>$c->appsecret = '';<br>$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/suites_push.php';<br>$suite_info = [<br>    [<br>        'suite_name' => '组合装创建测试20260410',<br>        'suite_no' => '202260410-001',<br>        'is_default_ratio' => 0,<br>        'short_name' => '组合装简称',<br>        'retail_price' => 990,<br>        'wholesale_price' => 990,<br>        'remark' => '备注',<br>        'goods_category_name' => '牛大腿',<br>        'brand_name' => '滑雪场',<br>        'suite_details' => [<br>            [<br>                'spec_no' => '2026030250930110001',<br>                'num' => 10,<br>                'ratio' => 0.6,<br>                'is_fixed_price' => 0,<br>            ],<br>            [<br>                'spec_no' => '20260408001',<br>                'num' => 10,<br>                'ratio' => 0.4,<br>                'is_fixed_price' => 0,<br>            ],<br>        ],<br>    ],<br>];<br><br>$c->putApiParam('suite_info', json_encode($suite_info));<br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 组合装列表节点 | suite_info | data[] |  | 是 | 请求参数的1级数据节点，包含组合装所有属性信息的数据节点，节点下数据字段详见下述“suite_info” |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 新增数量 | new_count | int | 11 | 是 | 新增数量 |
| 更新数量 | chg_count | int | 11 | 是 | 更新数量 |
| 出错数量 | error_count | int | 11 | 是 | 出错数量 |
| 出错信息 | error_message | varchar（255） |  | 是 | 出错信息 |
| 处理失败的错误列表 | errors | data | data[] | 否 | 处理失败的错误列表,当code为0且有错误信息时才非空.只列出同一批内有错误的记录.如果code=0,errors为空说明全部成功 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 组合装名称 | suite_name | varchar(255) |  | 是 | 组合装名称 |
| 组合装编码 | suite_no | varchar(40) |  | 是 | 组合装编码 |
| 是否默认金额占比 | is_default_ratio | tinyint(4) |  | 否 | 是否默认金额占比分摊1.默认0不默认（默认为1） |
| 组合装简称 | short_name | varchar(255) |  | 否 | 组合装简称（默认空） |
| 零售价 | retail_price | decimal(19,4) |  | 否 | 零售价（默认0） |
| 批发价 | wholesale_price | decimal(19,4) |  | 否 | 批发价（默认0） |
| 备注 | remark | varchar(64) |  | 否 | 备注 |
| 货品分类 | goods_category_name | varchar(40) |  | 否 | 货品分类 |
| 货品品牌 | brand_name | varchar(30) |  | 否 | 货品品牌 |
| 自定义属性1 | prop1 | varchar | 255 | 否 | 自定义属性1 |
| 自定义属性2 | prop2 | varchar | 255 | 否 | 自定义属性2 |
| 自定义属性3 | prop3 | varchar | 255 | 否 | 自定义属性3 |
| 自定义属性4 | prop4 | varchar | 255 | 否 | 自定义属性4 |
| 自定义属性5 | prop5 | varchar | 255 | 否 | 自定义属性5 |
| 自定义属性6 | prop6 | varchar | 255 | 否 | 自定义属性6 |
| 组合装组合单品 | suite_details | data[] |  | 是 | 装组合单品 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 单品商家编码 | spec_no | varchar |  | 是 | 单品商家编码 |
| 单品数量 | num | decimal(19,4) |  | 是 | 单品数量 |
| 金额占比 | ratio | decimal(5,4) |  | 否 | 金额占比（非默认占比的时候必填） |
| 是否使用固定价格 | is_fixed_price | tinyint(1) |  | 否 | 是否使用固定价格（1固定 0不固定）默认0 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误的组合装编码 | suite_no | varchar(40) | 40 | 是 | 组合装编码 |
| 错误信息的描述 | error | varchar | 255 | 否 | 错误信息的描述 |

#### 响应示例

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "new_count": 1,<br>    "chg_count": 0,<br>    "error_count": 0,<br>    "errors": [<br><br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "new_count": null,<br>    "chg_count": null,<br>    "error_count": null,<br>    "errors": [<br>        {<br>            "error": "suite_details 下的spec_no 不存在",<br>            "suite_no": "202260410-001"<br>        }<br>    ]<br>} |
| --- | --- |


### suites_query_Y - 查询组合装

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=suites_query_Y
- PHP file: suites_query.php
- Doc title: 查询组合装
- Client path: 商品→系统货品
- Description: 获取旺店通ERP中组合装界面的组合装资料

#### 接口说明

| 1.1 接口描述：获取旺店通ERP中组合装界面的组合装资料 |
| --- |
| 1.2 增量获取：按照旺店通ERP内组合装货品最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件，返回的结果不包含在旺店通ERP内组合装已停用的货品数据。 |
| 1.3时间跨度： start_time和end_time，无最大跨度范围，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |
| 1.4 注意事项：本接口如果不传start_time、end_time，则suite_no必须要传，如果start_time、end_time和suite_no都传了，则按照时间和商家编码的查询同时生效。 |

#### 调用场景

| 2.1 举例说明： 数据分析系统等系统的对接 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/suites_query.php |
| 正式环境 | https://openapi.huice.com/openapi/suites_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = '';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/suites_query.php';<br><br>    //添加查询参数<br>    $c->putApiParam('start_time','2018-08-01 00:00:00');<br>    $c->putApiParam('end_time','2018-08-11 00:00:00');<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量获取数据,start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量获取数据,end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 组合装商家编码 | suite_no | varchar | 40 | 否 | 代表组合装商品所有属性的唯一编码，用于系统组合装商品数据的获取，如果按照组合装商家编码查询，可以不传送开始时间和结束时间 |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~1000，不传本参数，输入值默认为40，使用举例单击这里 |
| 页号 | page_no | int |  | 否 | 不传值默认从0页开始 |
| 组合装名称 | suite_name | varchar | 255 | 否 | 组合装名称 |
| 主条码 | barcode | varchar | 50 | 否 | 主条码 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 11 | 是 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 组合装节点 | suites | data[] |  | 是 | （suite）数据节点，响应参数的1级数据节点，包含组合装所有属性信息的数据节点,节点下数据字段详见下述“suites”和"spec_list" |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 1,<br>    "suites": [<br>        {<br>            "suite_id": "2625298302945460230",<br>            "suite_no": "商家编码 (新)",<br>            "barcode": "",<br>            "spec_name": "旺店通测试商品",<br>            "suite_name": "旺店通测试商品",<br>            "retail_price": "0.04000000",<br>            "wholesale_price": "0",<br>            "member_price": "0.0000",<br>            "market_price": "0.0000",<br>            "weight": "0",<br>            "unit": "0",<br>            "aux_unit": 0,<br>            "deleted": 0,<br>            "modified": "2025-05-26 11:03:34",<br>            "img_url": "",<br>            "ref_cost_price": "0",<br>            "goods_category_id": "0",<br>            "category_name": null,<br>            "brand_id": "2680073525653406725",<br>            "brand_name": "牛叨小市",<br>            "prop1": "",<br>            "prop2": "",<br>            "prop3": "",<br>            "prop4": "",<br>            "prop5": "",<br>            "prop6": "",<br>            "specs_list": [<br>                {<br>                    "rec_id": "2699956590978531342",<br>                    "spec_no": "32727931",<br>                    "barcode": "",<br>                    "spec_code": "",<br>                    "spec_name": "颜色白色",<br>                    "goods_name": "用于测试删除",<br>                    "goods_no": "241030001",<br>                    "num": "1.0000",<br>                    "is_fixed_price": 0,<br>                    "fixed_price": null,<br>                    "ratio": "0.5000",<br>                    "spec_id": "2624640147219547140",<br>                    "unit": 0,<br>                    "deleted": 0,<br>                    "modified": "2025-05-26 11:03:34",<br>                    "img_url": "",<br>                    "prop1": null,<br>                    "prop2": null,<br>                    "prop3": null,<br>                    "prop4": null,<br>                    "prop5": null,<br>                    "prop6": null<br>                },<br>                {<br>                    "rec_id": "2699956591142109198",<br>                    "spec_no": "123456",<br>                    "barcode": "",<br>                    "spec_code": "",<br>                    "spec_name": "颜色蓝白",<br>                    "goods_name": "旺店通测试商品",<br>                    "goods_no": "zzz00001",<br>                    "num": "1.0000",<br>                    "is_fixed_price": 0,<br>                    "fixed_price": null,<br>                    "ratio": "0.5000",<br>                    "spec_id": "2624642187178017796",<br>                    "unit": 0,<br>                    "deleted": 0,<br>                    "modified": "2025-05-26 11:03:34",<br>                    "img_url": "https://img.huice.com/123456.jpg",<br>                    "prop1": null,<br>                    "prop2": null,<br>                    "prop3": null,<br>                    "prop4": null,<br>                    "prop5": null,<br>                    "prop6": null<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |

#### 业务响应参数

| suites |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| 组合装主键 | suite_id | int | 11 | 是 | erp组合装表的主键 |
| 组合装商家编码 | suite_no | varchar | 40 | 是 | 代表组合装商品所有属性的唯一编码，用于系统组合装商品的区分 |
| 组合装名称 | suite_name | varchar | 255 | 是 | 组合装名称 |
| 简称 | short_name | varchar | 255 | 是 | 组合装简称 |
| 分类名称 | class_name | varchar | 255 | 是 | 分类名称 |
| 品牌名称 | brand_name | varchar | 255 | 是 | 品牌名称 |
| 零售价 | retail_price | decimal | 19,4 | 是 | 零售价 |
| 批发价 | wholesale_price | decimal | 19,4 | 是 | 批发价 |
| 组合装成本价 | ref_cost_price | decimal | 19,4 | 否 | 组合装成本价 为0 表示没有组合装成本价 |
| 重量 | weight | decimal | 19,4 | 是 | 重量 |
| 删除状态 | deleted | varchar | 11 | 是 | 删除状态  未删除=0   已删除＞0 |
| 创建时间 | created | datetime |  | 是 | 创建时间  时间格式：yyyy-MM-dd HH:mm:ss |
| 最后修改时间 | modified | datetime |  | 是 | 最后修改时间   时间格式：yyyy-MM-dd HH:mm:ss |
| 组合装图片 | img_url | varchar |  | 是 | 组合装图片 |
| 货品分类id | goods_category_id | int |  | 否 |  |
| 货品分类名称 | category_name | varchar |  | 否 | 为空时null |
| 品牌id | brand_id | varchare |  | 否 | 品牌id |
| 自定义属性1 | prop1 | varchar | 255 | 否 | 自定义属性1 |
| 自定义属性2 | prop2 | varchar | 255 | 否 | 自定义属性2 |
| 自定义属性2 | prop3 | varchar | 255 | 否 | 自定义属性3 |
| 自定义属性4 | prop4 | varchar | 255 | 否 | 自定义属性4 |
| 自定义属性5 | prop5 | varchar | 255 | 否 | 自定义属性5 |
| 自定义属性6 | prop6 | varchar | 255 | 否 | 自定义属性6 |
| 单品节点 | specs_list | data[] |  | 是 | 响应参数的2级数据节点，包含sku所有属性信息的数据节点,节点下数据字段详见下述"specs_list" |
| specs_list |  |  |  |  |  |
| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| 单品商家编码 | spec_no | varchar | 40 | 是 | 代表所单品（sku）所有属性的编码，SPU和SKU概念介绍，单击这里 |
| 单品名称 | spec_name | varchar | 100 | 是 | 单品名称 |
| 条码 | barcode | varchar | 50 | 是 | 单品条形码 |
| 规格码 | spec_code | varchar | 40 | 是 | 规格码 |
| 货品名称 | goods_name | varchar | 255 | 是 | 货品名称 |
| 货品编号 | goods_no | varchar | 40 | 是 | 代表SPU所有属性的编号，SPU和SKU概念介绍，单击这里 |
| 数量 | num | decimal | 19,4 | 是 | 单品数量 |
| 单品主键id | rec_id | varchar | 11 | 是 | 单品主键id |
| 规格id | spec_id | varchar | 11 | 是 | 规格id |
| 基本单位 | unit | varchar | 11 | 是 | 基本单位 |
| 删除状态 | deleted | tinyint | 4 | 是 | 删除状态,删除状态  未删除=0   已删除＞0 |
| 使用固定售价 | is_fixed_price | tinyint | 1 | 是 | 是否使用固定售价 0:否/1:是（固定售价是手动填写的金额，非固定售价按金额占比分摊） |
| 固定金额 | fixed_price | decimal | 19,4 | 是 | 组合装中单品的单价金额 |
| 金额占比 | ratio | decimal | 5,4 | 是 | 单品占组合装总价格的百分比 |
| 最后修改时间 | modified | datetime |  | 是 | 时间格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | datetime |  | 是 | 时间格式：yyyy-MM-dd HH:mm:ss |
| 组合装单品图片 | img_url | varchar |  | 是 |  |
| 规格自定义属性1 | prop1 | varchar | 255 | 否 | 规格自定义属性1 |
| 规格自定义属性2 | prop2 | varchar | 255 | 否 | 规格自定义属性2 |
| 规格自定义属性2 | prop3 | varchar | 255 | 否 | 规格自定义属性3 |
| 规格自定义属性4 | prop4 | varchar | 255 | 否 | 规格自定义属性4 |
| 规格自定义属性5 | prop5 | varchar | 255 | 否 | 规格自定义属性5 |
| 规格自定义属性6 | prop6 | varchar | 255 | 否 | 规格自定义属性6 |

#### 响应示例

| JSON | {<br>    "code": "20",<br>    "message": "请求范围过宽，请增加请求参数条件过滤"<br>} |
| --- | --- |


### goods_category_query_Y - 查询货品分类

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=goods_category_query_Y
- PHP file: goods_category_query.php
- Doc title: 查询货品分类
- Client path: 商品→系统货品
- Description: 获取租户系统内全部货品分类的id、分类名词和分类的层级关系

#### 接口说明

| 1.1 接口描述：获取租户系统内全部货品分类的id、分类名词和分类的层级关系 |
| --- |
| 1.2 适用版本：250520迭代及之后 |

#### 调用场景

| 2.1 举例说明： SAP、线下ERP、SRM、SCM等系统对接 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/goods_category_query.php |
| 正式环境 | https://openapi.huice.com/openapi/goods_category_query.php |

| PHP | <?php<br>    require_once '../WdtClient.php';<br>    $c = new WdtClient;<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    //测试环境地址<br>    //上线时需要换成线上的<br><br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/goods_category_query.php';<br>   // $c->gatewayUrl = 'https://openapi.huice.com/openapi/goods_category_query.php';<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
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

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:200表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 一级分类列表 | goods_category_list | data[] |  | 是 | 响应参数的1级数据节点，包含一级分类及其子分类，节点下数据字段详见下述" goods_category_list"和“children_list” |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分类id | id | bigint(20) |  | 是 | 货品分类id |
| 分类名称 | category_name | varchar | 40 | 是 | 货品分类名称 |
| 分类下面的子分类 | children_list | data[] | 40 | 是 | 子分类包含内容和goods_category_list一致 |

#### 响应示例

| JSON | {<br>    "code": 200,<br>    "message": null,<br>    "goods_category_list": [<br>        {<br>            "id": "2788804529557078030",<br>            "category_name": "测试分类第一级",<br>            "children_list": [<br>                {<br>                    "id": "2788804569222610958",<br>                    "category_name": "分类二级",<br>                    "children_list": [<br>                        {<br>                            "id": "2788804604446375950",<br>                            "category_name": "分类三级",<br>                            "children_list": null<br>                        }<br>                    ]<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |

| JSON |  |
| --- | --- |


### goods_category_flat_query_Y - 查询货品分类平级

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=goods_category_flat_query_Y
- PHP file: 
- Doc title: 
- Client path: 商品→系统货品
- Description: 获取租户系统内全部货品分类的id、分类名词和分类的层级关系

#### 接口说明

| 1.1 接口描述：获取租户系统内全部货品分类的id、分类名词和分类的层级关系 |
| --- |
| 1.2 适用版本：250520迭代及之后 |

#### 调用场景

| 2.1 举例说明：SAP、线下ERP、SRM、SCM等系统对接 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/goods_category_flat_query.php |
| 正式环境 | https://openapi.huice.com/openapi/goods_category_flat_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/goods_category_flat_query.php';<br><br>	$c->putApiParam('page_no', '0');<br>	$c->putApiParam('page_size', '1');<br><br>	$json = $c->wdtOpenApi();<br>	print_r($json);<br><br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page_size | int |  | 否 | 每页返回条数，不传默认40 |
| 页号 | page_no | int |  | 否 | 不传值默认从0页开始 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 总条数 | totalCount | int | 11 | 是 | 总条数 |
| 分类列表 | goods_category_list | data[] |  | 是 | 响应参数包含一级分类及其子分类，节点下数据字段详见下述" goods_category_list" |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "goods_category_list": [<br>        {<br>            "id": "2677200940989153298",<br>            "parent_id": "0",<br>            "category_name": "牛肉",<br>            "category_level": 1,<br>            "sort_code": 1,<br>            "path": "-1,2677200940989153298"<br>        }<br>    ],<br>    "total_count": 115<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分类id | id | bigint |  | 是 | 货品分类id |
| 父级id | parent_id | bigint |  | 是 | 父级分类id |
| 分类名称 | category_name | varchar | 40 | 是 | 货品分类名称 |
| 所属层级 | category_level | int |  | 是 | 分类所属层级(1~5) |
| 排序码 | sort_code | int |  | 是 | 当前层级下的排序码 |
| 路径 | path | varchar |  | 是 | 路径 |

#### 响应示例

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |


### unique_code_print_Y - 打印唯一码

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=unique_code_print_Y
- PHP file: unique_code_print.php
- Doc title: 打印唯一码
- Client path: 档口→拿货标签管理
- Description: 

#### 接口说明

| 1.1 接口描述：变更唯一码打印状态，并返回唯一码信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3注意事项：暂无 |

#### 调用场景

| 2.1 举例说明：自研商城、SCM、SRM、财务系统、SAP等系统的对接 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/unique_code_print.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 |  |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一码id | ids | varchar |  | 是 | 唯一码id列表 (传字符串, 英文逗号分割) |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 标签列表 | unique_code_print_list | data[] |  | 是 | 小标签信息列表 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一码 | unique_no | varchar | 255 |  | 唯一码 |
| 货品主条码 | barcode | varchar | 255 |  | 货品主条码 |
| 唯一码状态 | unique_code_status | int | 11 |  | 唯一码状态 |
| 唯一码类型 | unique_code_type | int | 11 |  | 唯一码类型 |
| 打印状态 | print_status | int | 11 |  | 打印状态 |
| 分拣框名称 | box_name | varchar | 255 |  | 分拣框名称 |
| 分拣框订单序号 | box_trade_index | int | 11 |  | 分拣框订单序号 |
| 序号 | seq_no | int | 11 |  | 序号 |
| 最后一次打印时间 | last_print_time | datetime | 255 |  | 最后一次打印时间 |
| 第一次打印时间 | first_print_time | datetime | 255 |  | 第一次打印时间 |
| 规格名称 | sku_name | varchar | 255 |  | 规格名称 |
| 规格简称 | sku_short_name | varchar | 255 |  | 规格简称 |
| 商品标签 | goods_labels_name | varchar | 255 |  | 商品标签 |
| 图片 | img_url | varchar | 255 |  | 图片 |
| 商家编码(新) | sku_no | varchar | 255 |  | 商家编码(新) |
| 产地 | origin | varchar | 255 |  | 产地 |
| 货品名称 | spu_name | varchar | 255 |  | 货品名称 |
| 货品简称 | spu_short_name | varchar | 255 |  | 货品简称 |
| 货品编号 | spu_no | varchar | 255 |  | 货品编号 |
| 品牌名称 | brand_name | varchar | 255 |  | 品牌名称 |
| 供应商名称 | provider_name | varchar | 255 |  | 供应商名称 |
| 供应商地址 | provider_address | varchar | 255 |  | 供应商地址 |
| 供应商编码 | provider_no | varchar | 255 |  | 供应商编码 |
| 供应商分组 | provider_group_name | varchar | 255 |  | 供应商分组 |
| 供应商在分组内排序 | group_index | int | 11 |  | 供应商在分组内排序 |
| 供应商备注 | provider_remark | varchar | 255 |  | 供应商备注 |
| 订单付款时间 | trade_pay_time | datetime | 255 |  | 订单付款时间 |
| 订单编号 | trade_no | varchar | 255 |  | 订单编号 |
| 平台单号 | tid | varchar | 255 |  | 平台单号 |
| 价格 | trade_price | decimal |  |  | 价格 |
| 零售价 | price | decimal |  |  | 零售价 |
| 订单 买家留言 | buyer_message | varchar | 255 |  | 订单 买家留言 |
| 订单 客服留言 | remark | varchar | 255 |  | 订单 客服留言 |
| 卖家昵称 | trade_buyer_nick | varchar | 255 |  | 卖家昵称 |
| 收件人姓名 | trade_receiver_name | varchar | 255 |  | 收件人姓名 |
| 收件地址 | trade_receiver_address | varchar | 255 |  | 收件地址 |
| 平台货品名称 | plat_spu_name | varchar | 255 |  | 平台货品名称 |
| 平台规格名称 | plat_sku_name | varchar | 255 |  | 平台规格名称 |
| 平台货品编号 | plat_spu_no | varchar | 255 |  | 平台货品编号 |
| 平台规格商家编码 | plat_sku_no | varchar | 255 |  | 平台规格商家编码 |
| 物流公司名称 | logistics_name | varchar | 255 |  | 物流公司名称 |
| 物流品牌名称 | logistics_code_name | varchar | 255 |  | 物流品牌名称 |
| 物流品牌编码 | logistics_code | varchar | 255 |  | 物流品牌编码 |
| 货品数量 | trade_goods_num | decimal | 255 |  | 货品数量 |
| 货品种类数 | goods_type_count | int | 11 |  | 货品种类数 |
| 店铺名称 | shop_name | varchar | 255 |  | 店铺名称 |
| 店铺简称 | shop_short_name | varchar | 255 |  | 店铺简称 |
| 仓库名称 | warehouse_name | varchar | 255 |  | 仓库名称 |
| 唯一码打印批次 | print_batch_no | varchar | 255 |  | 唯一码打印批次 |
| 当前批次第几个位置 | print_batch_index | int | 11 |  | 当前批次第几个位置 |
| 货位 | sku_position | varchar | 255 |  | 货位 |
| 分拣码 | pick_no | varchar | 255 |  | 分拣码 |

#### 响应示例

| JSON |  |
| --- | --- |

| JSON |  |
| --- | --- |


### spec_barcode_push_Y - 创建系统货品多条码

- Category: 货品类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=spec_barcode_push_Y
- PHP file: spec_barcode_push.php
- Doc title: 创建、更新系统规格多条码
- Client path: 商品→货品条码
- Description: 在ERP内创建、更新系统规格多条码

#### 接口说明

| 1.1 接口描述：创建、更新系统规格多条码 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 注意事项：①每次请求，已存在的条码，执行更新操作。不存在的条码，执行新增操作。已存在但是未传输的条码不做处理。②当一次请求中存在重复条码时，需要提示“条码不允许重复”。③当请求中标识某一条记录为主条码时，自动清除已有的主条码记录标识，并同步更新sku的主条码字段。当一次请求中多条被标识为主条码时，需给出提示“只允许设置一个条码记录为主条码” |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/spec_barcode_push.php |
| 正式环境 | https://openapi.huice.com/openapi/spec_barcode_push.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once('../WdtClient.php');<br><br>    $c = new WdtClient;<br>  $c->sid = 'haijun';<br>    $c->appkey = '3-test';<br>    $c->appsecret = 'GGTl;@KPI]0w';<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/spec_barcode_push.php';<br><br>$c->putApiParam('spec_no', '951027');<br>   $barcode_list = [<br>    [<br>        "barcode_no" => "202605130001",<br>        "num" => "2",<br><br>    ]<br>];<br><br>$jsonString = json_encode($barcode_list, JSON_UNESCAPED_UNICODE);<br>$c->putApiParam('barcode_list', $jsonString);<br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码（新） | spec_no | varchar | 255 | 是 | 商家编码（新） |
| 多条码列表 | barcode_list | data[ ] |  | 是 | 多条码列表 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 条码 | barcode_no | varchar |  | 是 | 条码，不允许重复 |
| 数量 | num | int |  | 是 | 数量，主条码数量为1 |
| 是否是主条码 | is_main_barcode | int |  | 否 | 1.是 0.否 默认为0 ；只允许设置一个条码记录为主条码 |
| 是否删除 | deleted | int |  | 否 | 1.是 0.否 默认为0 |

#### 响应示例

| JSON | {"code":0,"message":""} |
| --- | --- |

| JSON | {"code":2541,"message":"请检查参数是否正确：：条码不能为空、数量需要大于1"} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、 |
| --- |


## 基础类

| 服务名 | 接口名 | 描述 | 客户端路径 |
| --- | --- | --- | --- |
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

### purchase_provider_query_Y - 查询供应商

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_provider_query_Y
- PHP file: purchase_provider_query.php
- Doc title: 查询供应商
- Client path: 采购→供应商
- Description: 批量获取旺店通ERP内供应商信息。

#### 接口说明

| 1.1 接口描述：批量获取旺店通ERP内供应商信息。 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取： 按照旺店通ERP内供应商最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件，返回的结果不包含在旺店通ERP已经删除的供应商数据.       全量获取： 支持不传start_time和end_time 时间查询，不传时间入参分页获取全量供应商数据。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/purchase_provider_query.php |
| 正式环境 | https://openapi.huice.com/openapi/purchase_provider_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>require_once '../WdtClient.php';<br>$c = new WdtClient();<br>$c->sid = '';<br>$c->appkey = '';<br>$c->appsecret = '';<br>$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/purchase_provider_query.php';<br><br>$c->putApiParam('start_time', '2025-12-10 13:00:44');<br>$c->putApiParam('end_time', '2026-12-30 13:59:44');<br>$c->putApiParam('page_no', 0);<br>$c->putApiParam('page_size', 1);<br><br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 11 | 是 | 符合条件的数据条数，用来分页 |
| 供应商节点 | provider_list | data[] |  | 是 |  |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 494,<br>    "provider_list": [<br>        {<br>            "tenantId": "haijun",<br>            "provider_id": "2812715471357345805",<br>            "provider_no": "8477",<br>            "provider_name": "SPE20260805001"<br>        }<br>    ]<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商编码 | provider_no | varchar | 64 | 否 | 供应商编码 |
| 供应商id | provider_id | long |  | 否 | 供应商在erp数据库内的主键id |
| 供应商名称 | provider_name | varchar | 64 | 否 | 供应商名称 |
| 开始时间 | start_time | datetime |  | 否 | 按最后修改时间增量查询数据，start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 否 | 按最后修改时间增量查询数据，end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 是否隐藏已删除供应商 | hide_deleted | tinyint | 4 | 否 | 目前无实际作用，传0或者不传 |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100 |
| 页号 | page_no | int |  | 否 | 页号，从0页开始 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商id | provider_id | long | 11 | 是 | 供应商表主键 |
| 供应商编号 | provider_no | varchar | 64 | 是 | 供应商编号 |
| 供应商名称 | provider_name | varchar | 64 | 是 | 供应商名称 |
| 联系人 | contact | varchar | 64 | 是 | 供应商联系人 |
| 电话 | telno | varchar | 20 | 是 | 移动电话/联系电话 |
| 开户银行 | bank_name | varchar | 50 | 是 | 开户银行名称 |
| 收款人 | payee_name | varchar | 20 | 是 | 收款人名称 |
| 银行账号 | bank_account | varchar | 40 | 是 | 银行账号（国际最长34位） |
| 地址 | address | varchar | 128 | 是 | 供应商详细地址 |
| 备注 | remark | varchar | 256 | 是 | 供应商备注信息 |
| 启用状态 | is_disabled | int | 11 | 是 | 是否停用：false 表示启用，true表示停用 |
| 更新时间 | modify_date | datetime |  | 是 | 更新时间，格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | create_date | datetime |  | 是 | 创建时间，格式：yyyy-MM-dd HH:mm:ss |

#### 响应示例

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、SCM、SRM、财务系统、SAP等系统的对接 |
| --- |




### cfg_tags_query_Y - 查询标签

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=cfg_tags_query_Y
- PHP file: cfg_tags_query.php
- Doc title: 查询标签
- Client path: 
- Description: 查询标签

#### 接口说明

| 1.1 接口描述：全量查询标签/异常 |
| --- |
| 1.2 适用版本：网页版 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/cfg_tags_query.php |
| 正式环境 | https://openapi.huice.com/openapi/cfg_tags_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/cfg_tags_query.php';<br><br>    $c->putApiParam('tag_name',"备注换货,备注换地址");<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 标签名称 | tag_name | String |  | 否 | 标签名称，精确查询，多个标签名字用英文逗号分割 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 只有page_no = 0 时，才返回的符合条件的数据总条数，用来分页 |
| 仓库详情数据节点 | tags | data[ ] |  | 是 | 标签数据节点 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 2,<br>    "records": [<br>        {<br>            "tag_id": "99",<br>            "basic_type": "1",<br>            "tag_name": "备注换地址",<br>            "modified": null<br>        },<br>        {<br>            "tag_id": "97",<br>            "basic_type": "1",<br>            "tag_name": "备注换货",<br>            "modified": null<br>        }<br>    ]<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 标签ID | tag_id | bigint(20) |  | 是 | 标签ID |
| 标签类型 | basic_type | int |  | 是 | 标签类型:1系统标签 2自定义标签 3异常标签 |
| 标签名称 | tag_name | string |  | 是 | 标签名称 |
| 修改时间 | modified | datetime |  |  | 系统标签没有更新时间 |

#### 响应示例

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |

#### 其他表格

| 2.1 全量查询标签/异常 |
| --- |


### unique_code_query_Y - 查询唯一码

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=unique_code_query_Y
- PHP file: unique_code_query.php
- Doc title: 查询唯一码
- Client path: 档口→拿货标签管理
- Description: 获取旺店通ERP内唯一码数据

#### 接口说明

| 1.1 接口描述：获取旺店通ERP内唯一码数据 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 增量获取：按照旺店通ERP内供应商最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/unique_code_query.php |
| 正式环境 | https://openapi.huice.com/openapi/unique_code_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/unique_code_query.php';<br><br>	$c->putApiParam('start_time', '2026-01-30 00:00:00');<br>	$c->putApiParam('end_time', '2026-02-01 00:00:00');<br>	$c->putApiParam('page_size', '1');<br>	$c->putApiParam('page_no', '0');<br><br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单号列表 | trade_nos | varchar |  | 否 | 订单号列表 (传字符串, 英文逗号分割) |
| 唯一码状态枚举列表 | status | varchar |  | 否 | 唯一码状态枚举列表 (传字符串, 英文逗号分割) (唯一码枚举 10:已失效 15:已退款 20:未拿货 37:已拿货 45:已到货 50:已分拣 60:已发货) |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量查询数据，start_time作为开始时间格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量查询数据，end_time作为结束时间格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数输入值默认为100 |
| 页号 | page_no | int |  | 否 | 页号，从0页开始 |

#### 公共响应参数

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 451,<br>    "unique_list": [<br>        {<br>            "uniqueCodeId": "2729046462829690910",<br>            "boxId": "0",<br>            "providerId": null,<br>            "tradeId": "2729046462590615582",<br>            "logisticsId": "2778951368499527691",<br>            "status": 60,<br>            "unique_code": "0000021763",<br>            "box_no": null,<br>            "pick_seq": "0",<br>            "modify_date": "2026-01-30T17:42:12",<br>            "provider_no": null,<br>            "provider_name": null,<br>            "goods_no": "133233522992",<br>            "goods_name": "测试测试22",<br>            "spec_no": "17773392251",<br>            "spec_name": "测试测试22",<br>            "sku_img_url": "",<br>            "api_goods_name": "测试测试22",<br>            "api_spec_name": "测试测试22",<br>            "price": "2099.0000",<br>            "wholesale_price": "0.0000",<br>            "trade_no": "JY2508140343",<br>            "trade_time": "2025-07-31T00:00:00",<br>            "pay_time": "2025-08-11T00:00:00",<br>            "cs_remark": "",<br>            "goods_count": 150,<br>            "shop_id": 332,<br>            "shop_name": "renmaolin-test",<br>            "trade_status": 95,<br>            "logistics_name": "极兔快递111",<br>            "logistics_no": "333333333333",<br>            "warehouse_id": "51",<br>            "warehouse_name": "发货仓"<br>        }<br>    ]<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 订单号列表 | trade_nos | varchar |  | 否 | 订单号列表 (传字符串, 英文逗号分割) |
| 唯一码状态枚举列表 | status | varchar |  | 否 | 唯一码状态枚举列表 (传字符串, 英文逗号分割) (唯一码枚举 10:已失效 15:已退款 20:未拿货 37:已拿货 45:已到货 50:已分拣 60:已发货) |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量查询数据，start_time作为开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量查询数据，end_time作为结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为100 |
| 页号 | page_no | int |  | 否 | 页号，从0页开始 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一码状态值 | status | int | 11 | 是 | 唯一码状态值 |
| 唯一码 | unique_code | varchar | 40 | 是 | 唯一码 |
| 分拣框 分拣框号 A1-2-3 中的 A1 | box_no | varchar | 40 | 是 | 分拣框 分拣框号 A1-2-3 中的 A1 |
| 分拣序列 分拣框号 A1-2-3 中的 2 | pick_seq | varchar | 40 |  | 分拣序列 分拣框号 A1-2-3 中的 2 |
| 修改时间 | modify_date | datetime |  |  | 修改时间 |
| 供应商编码 | provider_no | varchar | 64 |  | 供应商编码 |
| 供应商名称 | provider_name | varchar | 64 |  | 供应商名称 |
| 货品编码-spu | goods_no | varchar | 255 |  | 货品编码-spu |
| 商品名称 | goods_name | varchar | 255 |  | 商品名称 |
| 商家编码 | spec_no | varchar | 255 |  | 商家编码 |
| 规格名称 | spec_name | varchar | 255 |  | 规格名称 |
| 规格图片链接 | sku_img_url | varchar | 1024 |  | 规格图片链接 |
| 平台货品名称 | api_goods_name | varchar | 255 |  | 平台货品名称 |
| 平台规格名称 | api_spec_name | varchar | 255 |  | 平台规格名称 |
| 零售价 | price | decimal | 19,4 |  | 零售价 |
| 采购价 | wholesale_price | decimal | 19,4 |  | 采购价 |
| 订单编号 | trade_no | varchar | 255 |  | 订单编号 |
| 订单中下单时间 | trade_time | datetime |  |  | 订单中下单时间 |
| 付款时间 | pay_time | datetime |  |  | 付款时间 |
| 订单状态 | trade_status | tinyint | 4 |  | 订单状态 5 已取消 25 特殊单 29 预订单 30 待审核（已支付） 35 待财审 50 待发货 51 待推送 52 推送中 53 推送失败 55 已推送 95 已发货 110 已完成 |
| 订单中客服备注 | cs_remark | varchar | 1024 |  | 订单中客服备注 |
| 订单中货品总数 | goods_count | int |  |  | 订单中货品总数 |
| 订单中店铺id | shop_id | int |  |  | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺名称 | shop_name | varchar | 128 |  | 店铺名称 |
| 快递公司名称 | logistics_name | varchar | 128 |  | 快递公司名称 |
| 物流单号 | logistics_no | varchar | 128 |  | 物流单号 |
| 仓库名称 | warehouse_name | varchar |  |  | 仓库名称 |
| 仓库id | warehouse_id | int |  |  | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |

#### 响应示例

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、SCM、SRM、财务系统、SAP等系统的对接 |
| --- |


### logistics_Y - 物流公司

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=logistics_Y
- PHP file: 
- Doc title: 
- Client path: 配置→快递管理
- Description: 批量获取旺店通ERP内物流档案信息

#### 接口说明

| 1.1 接口描述：批量获取旺店通ERP内物流档案信息 |
| --- |
| 1.2 适用版本：网页版 |

#### 调用场景

| 2.1 举例说明：自有商城接入ERP、金蝶接入、用友接入、SAP接入等 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/logistics.php |
| 正式环境 | https://openapi.huice.com/openapi/logistics.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/unique_code_query.php';<br><br>	$c->putApiParam('start_time', '2026-01-30 00:00:00');<br>	$c->putApiParam('end_time', '2026-02-01 00:00:00');<br>	$c->putApiParam('page_size', '1');<br>	$c->putApiParam('page_no', '0');<br><br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流编号 | logistics_id | varchar | 20 | 否 | 代表物流所有属性的唯一编码，用于物流区分，ERP内支持自定义（ERP物流界面设置），用于获取指定物流数据信息 |
| 页号 | page_no | int |  | 否 | 页号，不传默认从0页开始 |
| 分页大小 | page_size | int |  | 否 | 每页返回的数据条数 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int |  | 是 | 错误码，0成功 |
| 错误描述 | message | varchar |  | 是 | 错误描述 |
| 物流档案列表节点 | logistics_list | data[ ] |  | 是 | 物流档案列表节点 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "total_count": 451,<br>    "unique_list": [<br>        {<br>            "uniqueCodeId": "2729046462829690910",<br>            "boxId": "0",<br>            "providerId": null,<br>            "tradeId": "2729046462590615582",<br>            "logisticsId": "2778951368499527691",<br>            "status": 60,<br>            "unique_code": "0000021763",<br>            "box_no": null,<br>            "pick_seq": "0",<br>            "modify_date": "2026-01-30T17:42:12",<br>            "provider_no": null,<br>            "provider_name": null,<br>            "goods_no": "133233522992",<br>            "goods_name": "测试测试22",<br>            "spec_no": "17773392251",<br>            "spec_name": "测试测试22",<br>            "sku_img_url": "",<br>            "api_goods_name": "测试测试22",<br>            "api_spec_name": "测试测试22",<br>            "price": "2099.0000",<br>            "wholesale_price": "0.0000",<br>            "trade_no": "JY2508140343",<br>            "trade_time": "2025-07-31T00:00:00",<br>            "pay_time": "2025-08-11T00:00:00",<br>            "cs_remark": "",<br>            "goods_count": 150,<br>            "shop_id": 332,<br>            "shop_name": "renmaolin-test",<br>            "trade_status": 95,<br>            "logistics_name": "极兔快递111",<br>            "logistics_no": "333333333333",<br>            "warehouse_id": "51",<br>            "warehouse_name": "发货仓"<br>        }<br>    ]<br>} |
| --- | --- |

#### 业务响应参数

| 字段 | Y类型 | 长度 | 是否必须 | 描述 |
| --- | --- | --- | --- | --- |
| logistics_id | bigint(20) |  | 是 | 物流公司id |
| logistics_name | string |  | 是 | 物流公司名称 |
| logistics_type | smallint(6) |  | 是 | 参考枚举中的系统物流公司编码 |
| logisitcs_code |  |  | 是 | erp物流类型编码物流代码表 |
| modified | datetime |  | 是 | 最后修改时间 |
| created | datetime |  | 是 | 创建时间 |
| status | tinyint(4) |  | 是 | 0 停用 1 启用 |

#### 响应示例

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |


### employee_query_Y - 员工查询

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=employee_query_Y
- PHP file: employee_query.php
- Doc title: 员工查询
- Client path: 配置→权限设置
- Description: 获取ERP的员工页面信息

#### 接口说明

| 1.1 接口描述：获取ERP的员工页面信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 全量获取：该接口是全量获取数据无法按照时间段增量获取数据。 |

#### 调用场景

| 2.1 举例说明：自研商城、SCM、SRM、财务系统、SAP等系统的对接 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/employee_query.php |
| 正式环境 | https://openapi.huice.com/openapi/employee_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 卖家账号, 由旺店通分配 |
| 接口账号 | appkey | String |  | 是 | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通网页版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/employee_query.php';<br><br>	$c->putApiParam('employee_id', 1976);<br>	$c->putApiParam('shortname', 'admin');<br>	$c->putApiParam('page_no', 0);<br>	$c->putApiParam('page_size', 10);<br><br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 分页大小 | page_size | int | 10 | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数输入值默认为30，<br>使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 员工ID | employee_id |  |  | 否 |  |
| 员工简称 | shortname |  |  | 否 |  |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 分页大小 | page_size | int | 10 | 否 | 每页返回的数据条数，输入值范围1~1000，不传本参数输入值默认为1000，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 员工列表节点 | userlist | data[ ] |  | 是 | 员工详情数据节点 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "userlist": [<br>        {<br>            "employee_id": "1976",<br>            "shortname": "admin",<br>            "fullname": "admin",<br>            "mobile_no": "176****1947",<br>            "deleted": false,<br>            "modified": "2025-04-25 11:53:02",<br>            "created": "2024-03-07 11:45:27",<br>            "status": 0,<br>            "user_no": ""<br>        }<br>    ],<br>    "total_count": 1<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 | Y枚举 | 是否必须 | 默认值 | 是否可变更 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 员工id | employee_id | bigint(20) | 20 |  |  |  | 是 |  | 否 |
| 员工编号 | employee_no | string | 64 |  |  |  | 是 |  | 是 |
| 状态 | status | int |  |  | 0：使用中1：已停用2：已删除 |  | 是 | 0 | 是 |
| 是否删除 | deleted | int(1) | 1 |  | 是否删除，0：否；1：是 |  | 是 |  | 是 |
| 最后修改时间 | modified | datetime |  |  | YYYY-MM-dd HH:mm:ss 例如2024-01-01 12:00:00 |  | 是 |  | 是 |
| 创建时间 | created | datetime |  |  | YYYY-MM-dd HH:mm:ss 例如2024-01-01 12:00:00 |  | 是 |  | 是 |

#### 响应示例

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |


### vip_stockout_sales_weight_push_Y - 称重

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_stockout_sales_weight_push_Y
- PHP file: vip_stockout_sales_weight_push.php
- Doc title: 重量回传
- Client path: 仓储→包裹称重
- Description: 将重量回传写入旺店通ERP销售订单

#### 接口说明

| 1.1 接口描述：将重量回传写入旺店通ERP销售订单 |
| --- |
| 1.2 适用版本：网页版 |

#### 调用场景

| 2.1 举例说明：自动化称重机、自动化分拣系统、仓储设备控制系统等称重以后，将重量回传写入ERP销售订单出库单。 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/vip_stockout_sales_weight_push.php |
| 正式环境 | https://openapi.huice.com/openapi/vip_stockout_sales_weight_push.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 卖家账号, 由旺店通分配 |
| 接口账号 | appkey | String |  | 是 | 由旺店通分配appkey, 在发送的数据中对应 key 字段,获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 秒级时间戳, 当前时间戳减去 1970-01-01 08:00:00起, 时间与服务器时间差120s内即合法。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/vip_stockout_sales_weight_push.php';<br><br>    $c->putApiParam('logistics_no', '8888888888887');<br>    $c->putApiParam('weight', '1.15');<br>    $c->putApiParam('is_check_trade_status', 0);//是否判断退款状态。0：不判断，1判断；默认为0<br>    $c->putApiParam('is_setting', 1);//校验重量是否超限。0：不校验，1：校验，默认为0<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 物流单号 | logistics_no | varchar |  | 是 | 物流单号 |
| 重量 | weight | decimal | (19,4) | 是 | 重量重量必须转成kg |
| 校验重量是否超限 | is_setting | tinyint | 1 | 否 | 0：不校验，1：校验，默认为0不进行校验（重量超限校验根据客户端配置进行校验，路径：配置>基本设置>称重超限提示 |
| 是否判断退款状态 | is_check_trade_status | tinyint | 1 | 否 | 0：不判断，1判断；默认为0 |
| 打包员编号 | packager_no | varchar | 40 | 否 | 打包员编号 |
| 长 | length | decimal | (19,4) | 否 | 只需要写入数字，单位cm |
| 宽 | width | decimal | (19,4) | 否 | 只需要写入数字，单位cm |
| 高 | height | decimal | (19,4) | 否 | 只需要写入数字，单位cm |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 物流类型 | logistics_name | String | 40 | 否 | 物流名称 |
| 物流通道编码 | channel_no | String | 64 | 否 | 物流公司的通道编码 |
| 物流方式 | logistics_type | smallint | 6 | 否 | 响应值为代表物流方式的数字 sheet页 枚举 中系统物流公司编码 |

#### 响应示例

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "channel_no": "",<br>    "logistics_name": "中通快递2",<br>    "logistics_type": "54"<br>} |
| --- | --- |

| JSON | {<br>    "code": 11000301,<br>    "message": "订单已发货，发货时间：2026-03-13 15:33:37 操作人：openapi",<br>    "channel_no": null,<br>    "logistics_name": null,<br>    "logistics_type": null<br>} |
| --- | --- |


### shop_Y - 查询店铺

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=shop_Y
- PHP file: shop.php
- Doc title: 查询店铺
- Client path: 配置→绑定店铺
- Description: 批量获取旺店通ERP内店铺档案信息

#### 接口说明

| 1.1 接口描述：批量获取旺店通ERP内店铺档案信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 全量获取：该接口是全量获取数据或按照shop_id获取，无法按照时间段增量获取数据。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/shop.php |
| 正式环境 | https://openapi.huice.com/openapi/shop.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/shop.php';<br><br>	$c->putApiParam('shop_id', 332);<br>	$c->putApiParam('platform_id', 127);<br>	$c->putApiParam('is_disabled', 0); //0未停用 1停用。默认为0<br>	$c->putApiParam('page_no', 0);<br>	$c->putApiParam('page_size', 20);<br><br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 店铺id | shop_id | int | 10 | 否 | 代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar |  |  | 代表店铺所有属性的唯一编号，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 平台ID | platform_id | smallint | 6 | 否 | 平台ID详情介绍单击这里 |
| 平台ID（批量） | platform_ids | varchar |  | 否 | 批量指定平台ID获取（多个平台ID之间用英文逗号隔开） |
| 分页大小 | page_size | int | 10 | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数输入值默认为30，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 是否停用 | is_disabled | varchar |  | 否 | 0未停用 1停用  不传默认为0 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 店铺列表节点 | shoplist | data[ ] |  | 是 | 店铺详情数据节点 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "shoplist": [<br>        {<br>            "fenxiaoNickNo": "",<br>            "shop_id": "332",<br>            "shop_no": "2598ad47a5400000",<br>            "platform_id": 127,<br>            "sub_platform_id": 0,<br>            "shop_name": "renmaolin-test",<br>            "shop_short_name": "33",<br>            "pay_account_id": null,<br>            "auth_state": 1,<br>            "push_rds_id": null,<br>            "pay_auth_state": null,<br>            "account_id": "",<br>            "account_nick": "",<br>            "refresh_token": null,<br>            "auth_time": "2025-06-20 16:58:51",<br>            "expire_time": null,<br>            "re_expire_time": null,<br>            "contact": null,<br>            "country": null,<br>            "province": null,<br>            "city": null,<br>            "district": null,<br>            "address": null,<br>            "telno": null,<br>            "mobile": null,<br>            "zip": null,<br>            "email": null,<br>            "remark": null,<br>            "website": null,<br>            "prop1": "",<br>            "prop2": "",<br>            "group_id": null,<br>            "is_disabled": false,<br>            "delete_flag": false,<br>            "shop_priority": null,<br>            "modified": "2026-03-17 14:12:43",<br>            "created": "2025-06-20 16:58:51",<br>            "main_shop_id": null,<br>            "platform_store_id": null,<br>            "sort": 2,<br>            "platform_shop_name": "",<br>            "employee_name": null<br>        }<br>    ],<br>    "total_count": 1<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 平台ID | platform_id | smallint | 6 | 是 | 平台ID详情介绍单击这里 |
| 子平台ID | sub_platform_id | tinyint | 4 | 是 | 子平台ID |
| 店铺ID | shop_id | smallint | 6 | 是 | 店铺列表主键，代表店铺所有属性的唯一id，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺编号 | shop_no | varchar | 50 | 是 | 店铺的唯一编码，用于店铺区分，在旺店通ERP【绑定店铺】界面查看 |
| 店铺名称 | shop_name | varchar | 128 | 是 | ERP店铺界面的店铺名称 |
| 平台授权账号ID | account_id | varchar | 40 | 是 | 平台授权账号ID（所有平台返回为空值） |
| 平台账号 | account_nick | varchar | 128 | 是 | 平台授权账号昵称（所有平台返回为空值） |
| 授权状态 | auth_state | varchar | 40 | 是 | 授权状态，0未授权 1已授权 2授权失效  3授权停用 |
| 是否启用推送 | push_rds_id | varchar | 40 | 是 | 是否启用推送 0不推送 其它值对应RDS服务器 |
| 邮件 | email | varchar | 64 | 是 | 邮件 |
| 最后修改时间 | modified | datetime | 11 | 是 | 最后修改时间    格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | datetime | 11 | 是 | 创建时间    格式：yyyy-MM-dd HH:mm:ss |
| 店铺简称 | shop_short_name | varchar | 128 | 否 |  |
| 是否停用 | is_disabled | bool | 1 | 是 | false 否 true 是 true 标识已经停用了 |
| 主店铺ID | main_shop_id | int |  | 否 | 只有小时达门店会有主店铺ID ，如果是小时达平台例如抖音小时达，有主店铺ID代表是子店铺 |
| 平台门店ID | platform_store_id | varchar | 64 | 否 | 只有小时达店铺会有， 表示平台的门店id，例如抖音小时达后台的门店Id |
| 平台店铺名称 | platform_shop_name | varchar | 100 | 否 | 平台店铺名称 |
| 业务员 | employee_name | varchar |  | 否 | 业务员 |

#### 响应示例

| JSON | {<br>    "code": 1020,<br>    "message": "系统异常"<br>} |
| --- | --- |

#### 其他表格

| 2.1 暂无 |
| --- |


### warehouse_query_Y - 查询仓库

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=warehouse_query_Y
- PHP file: warehouse_query.php
- Doc title: 查询仓库
- Client path: 配置→仓库信息维护
- Description: 批量获取旺店通ERP内仓库档案信息

#### 接口说明

| 1.1 接口描述：批量获取旺店通ERP内仓库档案信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 全量获取：该接口是全量获取数据或按照warehouse_no获取，无法按照时间段增量获取数据。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/warehouse_query.php |
| 正式环境 | https://openapi.huice.com/openapi/warehouse_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once('../WdtClient.php');<br><br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/warehouse_query.php';<br><br>    $c->putApiParam('warehouse_id', 38);<br>    $c->putApiParam('page_no', 0);<br>    $c->putApiParam('page_size', 100);<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库id | warehouse_id | bigint |  | 否 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看(不支持一次推送多个仓库编码) |
| 仓库编号 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看(不支持一次推送多个仓库编码) |
| 仓库类型 | warehouse_type | int |  | 否 | 0普通仓库 2分销仓 3委外仓库4自流转仓 |
| 分页大小 | page_size | int | 10 | 否 | 每页返回的数据条数，输入值范围1~100，不传本参数，输入值默认为40，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 是否停用 | is_disabled | tinyint |  | 否 | 0未停用 1停用  默认为0  返回未停用仓库 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 只有page_no = 0 时，才返回的符合条件的数据总条数，用来分页 |
| 仓库详情数据节点 | warehouses | data[ ] |  | 是 | 仓库详情数据节点 |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "warehouses": [<br>        {<br>            "warehouse_id": "38",<br>            "warehouse_no": "38",<br>            "name": "滑雪场器材仓库1",<br>            "warehouse_type": 0,<br>            "address": "河北省秦皇岛市",<br>            "contact": "lily",<br>            "mobile": "17300000066",<br>            "telno": "000068",<br>            "remark": "五",<br>            "province": "河北省",<br>            "city": "秦皇岛市",<br>            "district": "北戴河区",<br>            "is_disabled": 0,<br>            "modified": "2026-03-16 17:13:10",<br>            "created": "2025-07-01 09:33:03"<br>        }<br>    ],<br>    "total_count": 1<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 仓库id | warehouse_id | bigint(20) | 20 | 是 | 代表仓库所有属性的唯一id，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库编号 | warehouse_no | varchar | 40 |  | 代表仓库所有属性的唯一编号，用于仓库区分，在旺店通ERP【仓库信息维护】界面查看 |
| 仓库名称 | name | varchar | 128 | 是 |  |
| 仓库类型 | warehouse_type | int |  | 是 | 0普通仓库 2分销仓 3委外仓库4自流转仓 |
| 仓库地址（省市区详细地址） | address | varchar | 256 |  |  |
| 联系人名称 | contact | varchar | 128 |  |  |
| 联系人手机号 | mobile | varchar | 56 |  |  |
| 联系人固定电话 | telno | varchar | 56 |  |  |
| 备注 | remark | varchar | 512 | 否 |  |
| 省名称 | province | varchar | 40 |  |  |
| 市名称 | city | varchar | 40 |  |  |
| 区名称 | district | varchar | 40 |  |  |
| 是否停用 | is_disabled | tinyint |  | 是 | 0否 1是 |
| 最后修改时间 | modified | timestemp |  | 是 | 最后修改时间    格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | timestemp |  | 是 | 创建时间    格式：yyyy-MM-dd HH:mm:ss |

#### 响应示例

| JSON | {<br>    "code": 2220,<br>    "message": "page_size为正整数，请检查page_size是否为有效值"<br>} |
| --- | --- |

#### 其他表格

| 2.1 暂无 |
| --- |


### sys_logisitcs_code_Y - 物流公司枚举

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=sys_logisitcs_code_Y
- PHP file: 
- Doc title: 
- Client path: 
- Description: 

#### 接口说明

| 1.1 接口描述：物流公司枚举 |
| --- |
| 1.2 适用版本：网页版 |

#### 调用场景

| 2.1 举例说明：自有商城接入ERP、金蝶接入、用友接入、SAP接入等 |
| --- |

#### 其他表格

| 系统物流公司编码（sys_logisitcs_code） | 系统物流公司名称 |
| --- | --- |
| 1 | 1688官方直送货运单 |
| 2 | 1688官方直送快递单 |
| 3 | EMS |
| 4 | EMS快递包裹 |
| 5 | 安能快运 |
| 6 | 安能物流 |
| 7 | 百世国际 |
| 8 | 百世快递 |
| 9 | 百世物流 |
| 10 | 百世云配 |
| 11 | 大食品商家自配 |
| 12 | 德邦快递 |
| 13 | 德邦物流 |
| 14 | 广东EMS跨境易 |
| 15 | 广东顺心快运有限公司 |
| 16 | 国通快递 |
| 17 | 裹裹同城特快 |
| 18 | 加运美 |
| 19 | 京广速递 |
| 20 | 卡行快运 |
| 21 | 跨越速运 |
| 22 | 快捷快递 |
| 23 | 联邦快递 |
| 24 | 平安达腾飞快递 |
| 25 | 全峰快递 |
| 26 | 日日顺 |
| 27 | 如风达 |
| 28 | 山东递速 |
| 29 | 闪货极速达 |
| 30 | 申通快递 |
| 31 | 申通快运 |
| 32 | 顺丰速运 |
| 33 | 苏宁物流 |
| 34 | 速尔快运 |
| 35 | 速腾快递 |
| 36 | 淘特生鲜 |
| 37 | 淘特物流 |
| 38 | 天地华宇 |
| 39 | 天天快递 |
| 40 | 菜鸟速递(丹鸟) |
| 41 | 信丰物流 |
| 42 | 壹米滴答快运 |
| 43 | 优速快递 |
| 44 | 邮政标准快递 |
| 45 | 邮政国内小包 |
| 46 | 圆通承诺达特快(B网) |
| 47 | 圆通速递 |
| 48 | 远成快运 |
| 49 | 韵达快递 |
| 50 | 韵达快运 |
| 51 | 韵达同城 |
| 52 | 宅急送 |
| 53 | 中铁快运 |
| 54 | 中通快递 |
| 55 | 中通快运 |
| 56 | 顺丰快运 |
| 57 | 丰网 |
| 58 | 极兔快递 |
| 59 | 京东快递 |
| 60 | 众邮快递 |
| 61 | D速物流 |
| 62 | 安得物流 |
| 63 | 安迅物流 |
| 64 | 承诺达特快 |
| 65 | 当当网 |
| 66 | 顺心捷达 |
| 67 | 亚风速递 |
| 68 | 韵达国际 |
| 69 | 中通国际 |
| 70 | 全一快递 |
| 71 | 百世快运 |
| 72 | 未知 |
| 73 | 自有物流 |
| 74 | 中远 |
| 75 | 龙邦速递 |
| 76 | 全日通快递 |
| 77 | 发网 |
| 78 | 联昊通 |
| 79 | 华强物流 |
| 80 | 星辰急便 |
| 81 | 长宇 |
| 82 | 大田 |
| 83 | 长发 |
| 84 | CCES |
| 85 | 东方汇 |
| 86 | 首业 |
| 87 | 远长 |
| 88 | 新邦物流 |
| 89 | 港中能达 |
| 90 | 黑猫宅急便 |
| 91 | 浙江ABC |
| 92 | 飞远(爱彼西)配送 |
| 93 | 四川快捷 |
| 94 | 贝业新兄弟 |
| 95 | 飞远配送 |
| 96 | 尚橙物流 |
| 97 | 城市100 |
| 98 | 汇强快递 |
| 99 | E速宝 |
| 100 | 同城快递 |
| 101 | 北京EMS |
| 102 | 佳吉快递 |
| 103 | 凡宇速递 |
| 104 | 居无忧 |
| 105 | 美国速递 |
| 106 | 派易国际物流77 |
| 107 | RUSTON |
| 108 | 燕文北京 |
| 109 | 燕文广州 |
| 110 | 燕文国际 |
| 111 | 燕文上海 |
| 112 | 燕文深圳 |
| 113 | 燕文义乌 |
| 114 | 合众阳晟 |
| 115 | ZTOGZ |
| 116 | ZTOSH |
| 117 | 保宏物流 |
| 118 | 增益速递 |
| 119 | 贝海国际速递 |
| 120 | 菜鸟智选物流 |
| 121 | 菜鸟配送 |
| 122 | 德邦快运 |
| 123 | 品骏(JITX) |
| 124 | 圆通(JITX) |
| 125 | 承诺达 |
| 126 | 品骏快递 |
| 127 | 诚信物流 |
| 128 | 京东纯配 |
| 129 | 九曳快递 |
| 130 | 顺丰同城配 |
| 131 | 菜鸟落地配-万象 |
| 132 | 青岛日日顺 |
| 133 | 京邦达 |
| 134 | 其他 |
| 135 | 天天国际 |
| 136 | 递四方 |
| 137 | 中远E环球 |
| 138 | 秀驿物流 |
| 139 | 优邦速运 |
| 140 | VoyageOne |
| 141 | UEQ |
| 142 | 斑马物联网 |
| 143 | 卓志速运 |
| 144 | 申通国际 |
| 145 | 威时沛运 |
| 146 | 香港邮政 |
| 147 | 广东EMS |
| 148 | 日本邮政 |
| 149 | 贝海国际 |
| 150 | 圆通国际 |
| 151 | 高捷跨境快运 |
| 152 | 易客满国际物流 |
| 153 | EWE GLOBAL |
| 154 | 抖店BIC送货 |
| 155 | 无需物流 |
| 156 | 邮政电商标快 |
| 157 | 京东大件物流 |
| 158 | 无需物流（新） |
| 159 | 京东快运 |
| 160 | 哪吒速运 |
| 161 | 京广换京东 |


### unique_code_status_change_Y - 修改唯一码状态为已到货

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=unique_code_status_change_Y
- PHP file: unique_code_status_change.php
- Doc title: 修改唯一码状态为已到货
- Client path: 档口→拿货标签管理
- Description: 将旺店通唯一码状态变更为已到货

#### 接口说明

| 1.1 接口描述：将旺店通唯一码状态变更为已到货 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3注意事项：需要判断请求唯一码的状态是否是“待拿货”, 不是待拿货的将返回错误结果 |

#### 调用场景

| 2.1 举例说明：自研商城、SCM、SRM、财务系统、SAP等系统的对接 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/unique_code_status_change.php |
| 正式环境 | https://openapi.huice.com/openapi/unique_code_status_change.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 |  |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>	require_once("../WdtClient.php");<br>	$client = new WdtClient;<br>	$client->sid = '';<br>	$client->appkey = '';<br>	$client->appsecret = "";<br>	$client->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/unique_code_status_change.php';<br><br>	$client->putApiParam('unique_codes', '0000006273626');<br><br>	$response = $client->wdtOpenApi();<br>	var_dump($response);<br>?> |
| --- | --- |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一码列表 | unique_codes | varchar |  | 否 | 订单号列表 (传字符串, 英文逗号分割) |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 成功条数 | success_count | int |  |  |  |
| 失败条数 | fail_count | int |  |  |  |
| 失败列表 | fail_list | data[] |  |  |  |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 唯一码 | unique_code | varchar | 40 | 是 | 唯一码 |
| 失败信息 | fail_msg | varchar |  | 是 | 仅支持修改“待拿货”状态的唯一码，唯一码状态是xxx，不允许修改！ |

#### 响应示例

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "success_count": 1,<br>    "fail_count": 0,<br>    "fail_list": [<br><br>    ]<br>} |
| --- | --- |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "success_count": 1,<br>    "fail_count": 1,<br>    "fail_list": [{<br>        "unique_code": "0000006273626",<br>        "fail_msg": "仅支持修改“待拿货”状态的唯一码，唯一码状态是已到货，不允许修改！"<br>    }]<br>} |
| --- | --- |


### purchase_provider_create_Y - 创建供应商

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_provider_create_Y
- PHP file: purchase_provider_create.php
- Doc title: 创建供应商
- Client path: 采购→供应商
- Description: 给旺店通推送供应商信息

#### 接口说明

| 1.1 接口描述：推送供应商给旺店通网页版ERP |
| --- |
| 1.2 适用版本： |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/purchase_provider_create.php |
| 正式环境 | https://openapi.huice.com/openapi/purchase_provider_create.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果 |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/purchase_provider_create.php';<br><br>	$c->putApiParam('provider_no', 'rmlS0410');<br>	$c->putApiParam('provider_name', '室内滑雪场供应商');<br>	$c->putApiParam('contact', '联系人');<br>	$c->putApiParam('mobile', '17000000000');<br>	$c->putApiParam('email', '2120012456@163.com');<br>	$c->putApiParam('address', '天津天津市滨海新区室内滑雪场');<br>	$c->putApiParam('last_purchase_time', '2026-04-10 08:00:00');<br>	$c->putApiParam('is_disabled', '0');<br>	$qualifica_list = [<br>		[<br>			'certificate_name' => '营业执照',<br>			'certificate_no' => '91000000MA0F0K0Y0P',<br>			'start_date' => '2023-04-10 00:00:00',<br>			'end_date' => '2033-04-09 23:59:59',<br>			'expire_remind_day' => '30',<br>			'certificate_img_list' => [<br>				[<br>					'img_name' => '附件图片文件的名称',<br>					'img_url' =>'https://www.keaitupian.cn/cjpic/frombd/0/253/3119496853/2980537814.jpg'<br>				]<br>			]<br>		]<br>	];<br><br>	$c->putApiParam('qualifica_list', json_encode($qualifica_list, JSON_UNESCAPED_UNICODE));<br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商编码 | provider_no | varchar | 20 | 是 | 代表供应商所有属性的唯一编码，用于供应商区分，ERP内支持自定义（ERP供应商界面设置），用于创建供应商数据信息 |
| 供应商名称 | provider_name | varchar | 64 | 是 | 供应商名称 |
| 供应商分组 | provider_group | varchar | 64 | 否 | 供应商分组 |
| 联系人 | contact | varchar | 64 | 否 | 联系人 |
| 电话 | mobile | varchar | 40 | 否 | 手机号 |
| 邮箱 | email | varchar | 64 | 否 | 电子邮箱 |
| 地址 | address | varchar | 128 | 否 | 省、市、区（县）、地址详情 |
| 最后采购日期 | last_purchase_time | datetime |  | 否 | 对供应商最后一次采购日期，不传默认接口创建供应商的年月日，格式：yyyy-MM-dd HH:mm:ss |
| 状态 | is_disabled | tinyint | 1 | 否 | 0 启用 1停用 |
| 资质信息列表 | qualifica_list | data[] |  | 否 | 资质信息列表 |

| JSON | {<br>    "code": 17000001,<br>    "message": "供应商名称或者编码重复"<br>} |
| --- | --- |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 证件名称 | certificate_name | varchar | 20 | 是 | 注意：当 qualifica_list 不为空时，该字段必传。 资质证件的名称，如“营业执照” |
| 证件编码 | certificate_no | varchar | 64 | 否 | 证件上的统一社会信用代码或编号 |
| 证件有效期开始时间 | start_date | varchar | 64 | 否 | 证件有效期开始时间，格式：yyyy-MM-dd HH:mm:ss |
| 证件有效期结束时间 | end_date | varchar | 64 | 否 | 证件有效期结束时间，格式：yyyy-MM-dd HH:mm:ss |
| 到期提醒(天) | expire_remind_day | varchar | 40 | 否 | 证件有效期结束前*天 |
| 附件证件图片列表节点 | certificate_img_list | varchar | 64 | 否 | 证件图片数组节点，包含具体的图片明细 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 附件图片名称 | img_name | varchar | 255 | 否 | 图片文件的名称 |
| 附件图片链接 | img_url | varchar | 1024 | 否 | 外部可访问的图片 URL 地址 |

#### 响应示例

| JSON | {<br>    "code": 0,<br>    "message": ""<br>} |
| --- | --- |

#### 其他表格

| 2.1 SCM、SRM系统对接 |
| --- |


### order_audit_Y - 业务单据审核接口

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=order_audit_Y
- PHP file: order_audit.php
- Doc title: 业务单据审核接口
- Client path: 订单→订单管理→待审核
- Description: 第三方系统触发erp中待审核（待确认）的业务单据审核

#### 接口说明

| 1.1 接口描述：第三方系统触发erp中待审核（待确认）的业务单据审核 |
| --- |
| 1.2 注意事项：接口不支持批量执行 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/order_audit.php |
| 正式环境 | https://openapi.huice.com/openapi/order_audit.php |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient;<br>    //sid appkey appsecret 需要换成自己的<br>    $c->sid ='';<br>    $c->appkey ='';<br>    $c->appsecret ="";<br>    //测试环境地址<br>    //上线时需要换成线上的<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/order_audit.php';<br><br>	$c->putApiParam('order_type', "7");<br>	$c->putApiParam('type', "2");<br>	$c->putApiParam('order_no', "CG2512160045");<br>	$json = $c->wdtOpenApi();<br>	var_dump($json);<br>?> |
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
| 业务单据类型 | order_type |  |  | 是 | 1.销售订单 2.售后单  4.委外入库单 5.委外出库单 6.调拨单7.采购单 |
| 操作业务类型 | type |  |  | 是 | 2.审核 3.财务审核。（仅采购单、销售订单时，3 财务审核 才生效，其他业务单据财审提示“该业务单据暂不支持财务审核”） |
| 业务单号 | order_no |  |  | 是 | 业务单号 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 处理失败的错误列表 | errors_list | data | data[] | 否 | 处理失败的错误列表,当code为0,errors_list 也为空，则表示全部成功。code为0，errors_list不为空，代表部分成功。 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误的业务单号 | order_no | int | 40 | 是 | 错误的业务单号order_no |
| 错误原因 | error_info | varchar | 255 | 是 | 错误原因 |

#### 响应示例

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"errors_list": []<br>} |
| --- | --- |

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"errors_list": [{<br>		"order_no": "CG2512160049",<br>		"error_info": "仅可审核 待审核 状态的采购单"<br>	}]<br>} |
| --- | --- |

#### 其他表格

| 2.1 第三方系统触发erp中待审核（待确认）的业务单据审核 |
| --- |


### order_cancel_Y - 业务单据取消

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=order_cancel_Y
- PHP file: order_cancel.php
- Doc title: 业务单据取消
- Client path: 
- Description: 第三方系统触发erp中业务单据取消。

#### 接口说明

| 1.1 接口描述：第三方系统触发erp中业务单据取消。 |
| --- |
| 1.2 注意事项：● 执行业务单的取消功能           普通仓业务单能取消的状态是：待审核，待财审，已审核，如果没有取消成功返回错误信息，其他状态都是不能取消的，调用会返回错误信息。           委外仓业务单能取消的状态是：待审核，待财审，已审核，待推送，推送失败，已推送。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/order_cancel.php |
| 正式环境 | https://openapi.huice.com/openapi/order_cancel.php |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	//sid appkey appsecret 需要换成自己的<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	//测试环境地址<br>	//上线时需要换成线上的<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/order_cancel.php';<br><br>	$c->putApiParam('order_no', 'CG2512110101');<br>	$c->putApiParam('type', '1'); //1.采购单  2.采购退货单<br>	$c->putApiParam('is_reject_review', '1'); //0已审核的单子无法进行取消。1已审核的单子，可以先进行驳回审核再进行取消<br>	$json = $c->wdtOpenApi();<br>	$array = json_decode($json, true); // 转成数组<br>	echo json_encode($array, JSON_UNESCAPED_UNICODE); // 输出中文正常显示<br>?> |
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
| 业务单据类型 | type | int |  | 是 | 1.采购单  2.采购退货单 |
| 是否允许已审核（待财审+已审核状态）的单子取消 | is_reject_review | int |  | 是 | 0已审核的单子无法进行取消。1已审核的单子，支持自动驳回审核再进行取消。（待财审状态先驳回审核，再取消；已审核、待推送、推送失败 状态先驳回财审再驳回审核再取消）默认为0（当is_reject_review=1时，针对委外单据已推送状态，自动向下游发起“撤销采购单”，再驳回财审、驳回审核、系统内部取消） |
| 业务单号 | order_no | String |  | 是 | 业务单号 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |

#### 响应示例

| JSON | {<br>	"code": 0,<br>	"message": "处理成功"<br>} |
| --- | --- |

| JSON | {<br>	"code": -1,<br>	"message": "采购单状态不正确"<br>} |
| --- | --- |

#### 其他表格

| 2.1 客户自研SCM系统，通过API接口对接，希望在SCM系统里面操作业务单据的取消操作。 |
| --- |


### order_stop_waiting_Y - 业务单停止等待

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=order_stop_waiting_Y
- PHP file: order_stop_waiting.php
- Doc title: 业务单停止等待
- Client path: 
- Description: 第三方系统对接处理业务单据进行停止等待

#### 接口说明

| 1.1 接口描述：第三方系统触发erp中业务单据停止等待。 |
| --- |
| 1.2 注意事项：当type=1时，执行业务单的停止等待功能，只能停止等待部分入库的业务单，如果没有停止等待成功返回错误信息，其他状态都是不能停止等待的，也会返回错误信息。当type=2时，执行业务单的明细停止等待功能，只能操作部分入库的业务单，如果没有停止等待成功返回错误信息，其他状态都是不能停止等待的，也会返回错误信息。（外部仓库，停止等待时，会自动向外仓发起停止等待申请） |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/order_stop_waiting.php |
| 正式环境 | https://openapi.huice.com/openapi/order_stop_waiting.php |

| PHP | <?php<br>	require_once '../WdtClient.php';<br>	$c = new WdtClient();<br>	//sid appkey appsecret 需要换成自己的<br>	$c->sid = '';<br>	$c->appkey = '';<br>	$c->appsecret = '';<br>	//测试环境地址<br>	//上线时需要换成线上的<br>	$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/order_stop_waiting.php';<br><br>	$c->putApiParam('order_no', 'JY2603180871');<br>	$c->putApiParam('type', '1'); //1停止等待（终止出库），2明细停止等待（仅 type=1时，支持明细停止等待）<br>	$c->putApiParam('operation_type', '1'); //1.采购单 2.采购退货单<br>	$json = $c->wdtOpenApi();<br>	$array = json_decode($json, true); // 转成数组<br>	echo json_encode($array, JSON_UNESCAPED_UNICODE); // 输出中文正常显示<br>?> |
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
| 业务单据类型 | type | int |  | 是 | 1.采购单 2.采购退货单 |
| 操作类型 | operation _type | int |  | 是 | 1停止等待（终止出库），2明细停止等待（仅 type=1时，支持明细停止等待） |
| 业务单批量列表节点 | order_no | data[] |  | 是 | 业务单号 |
| 商家编码列表节点 | spec_no | data[] |  | 否 | 商家编码列表节点,当operation _type=2时必传。 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |

#### 响应示例

| JSON | {<br>	"code": 0,<br>	"message": "处理成功"<br>} |
| --- | --- |

| JSON | {<br>    "code": -1,<br>    "message": "采购单状态不正确"<br>} |
| --- | --- |

#### 其他表格

| 2.1 客户自研SCM系统，通过API接口对接，希望在SCM系统里面操作业务单据的停止等待。 |
| --- |


### order_reject_Y - 业务单据驳回审核接口

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=order_reject_Y
- PHP file: order_reject.php
- Doc title: 业务单据驳回审核接口
- Client path: 
- Description: 第三方系统触发erp中业务单据驳回审核

#### 接口说明

| 1.1 接口描述：第三方系统触发erp中已审核、已财审的业务单据驳回审核 |
| --- |
| 1.2 注意事项：接口支持批量执行，单次批量操作单据数量最大为50条。批量操作情况下，接口支持部分成功，失败的单据将在错误信息中返回具体的失败原因。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/order_reject.php |
| 正式环境 | https://openapi.huice.com/openapi/order_reject.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/order_reject.php';<br><br>    $c->putApiParam('order_type',1);//1.销售订单 2.售后单 4.委外入库单 5.委外出库单 6.调拨单 7.采购单<br>    $c->putApiParam('type',2);<br>    $c->putApiParam('order_no',"JY2503050349");<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 业务单据类型 | order_type | int |  | 是 | 1.销售订单 2.售后单  4.委外入库单 5.委外出库单 6.调拨单7.采购单 |
| 驳回审核类型 | type | int |  | 是 | 2.驳回审核 3.驳回财务审核。（仅采购单、销售订单时，3 财务审核 才生效，其他业务单据财审提示“该业务单据暂不支持财务审核”） |
| 业务单号 | order_no | varchar |  | 是 | 业务单号（系统订单号） |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 40 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误原因 | message | varchar | 255 | 是 | 错误原因 |
| 处理失败的错误列表 | errors_list | data | data[] | 否 | 处理失败的错误列表,当code为0,errors_list 也为空，则表示全部成功。code为0，errors_list不为空，代表部分成功。 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误的业务单号 | order_no | int | 40 | 是 | 错误的业务单号order_no |
| 错误原因 | error_info | varchar | 255 | 是 | 错误原因 |

#### 响应示例

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"errors_list": []<br>} |
| --- | --- |

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "errors_list": [<br>        {<br>            "order_no": "JY2503050349",<br>            "error_info": null<br>        }<br>    ] |
| --- | --- |

#### 其他表格

| 2.1 第三方系统触发erp中已审核、已财审的业务单据驳回审核 |
| --- |


### warehouse_create_Y - 

- Category: 基础类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=warehouse_create_Y
- PHP file: 
- Doc title: 
- Client path: 
- Description: 


## 售后类

| 服务名 | 接口名 | 描述 | 客户端路径 |
| --- | --- | --- | --- |
| stockin_order_query_refund_Y | 退货入库单查询 | 获取旺店通ERP销售退货（换货）订单对应的入库单信息 | 仓储→入库管理 |
| sales_refund_push_Y | 创建原始退款单 | 销售订单（包括发货前和发货后）退款或退货单据推送至ERP。注：销售订单的售后换货订单此接口推送“退货类型”退款单，换出订单“trade_push.php”推送 | 售后→售后管理→平台售后单 |
| refund_query_Y | 查询退换管理 | 获取ERP销售退货（换货）订单信息 | 售后→售后管理→售后单 |
| aftersales_refund_create_Y | 创建系统售后单 | 创建系统售后单，---目前不支持换货 ，只支退货单，退货单类型只能是退款退货和退款不退货 基于系统单创建退款单 | 售后→售后管理→售后单 |
| vip_api_refund_query_Y | 查询原始退单 |  | 售后→售后管理→平台售后单 |
| aftersale_stockin_confirm_Y | 创建退货入库单 | 推送旺店通ERP销售退货（换货）订单对应的入库单据给旺店通ERP，推送前提旺店通ERP的退换单状态为“待收货” | 仓储--入库管理--退货入库单--新建 |

### stockin_order_query_refund_Y - 退货入库单查询

- Category: 售后类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=stockin_order_query_refund_Y
- PHP file: stockin_order_query_refund.php
- Doc title: 查询退货入库单
- Client path: 仓储→入库管理
- Description: 获取旺店通ERP销售退货（换货）订单对应的入库单信息

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

| JSON | {<br>    "code":2900,<br>    "message":"时间范围与入库单号不能全部为空"<br>} |
| --- | --- |

#### 其他表格

| 2.1 财务系统、SAP、数据分析等系统的对接 |
| --- |


### sales_refund_push_Y - 创建原始退款单

- Category: 售后类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=sales_refund_push_Y
- PHP file: sales_refund_push.php
- Doc title: 创建原始退款单
- Client path: 售后→售后管理→平台售后单
- Description: 销售订单（包括发货前和发货后）退款或退货单据推送至ERP。注：销售订单的售后换货订单此接口推送“退货类型”退款单，换出订单“trade_push.php”推送

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "new_count": 1,<br>    "chg_count": 0<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、分销系统、全渠道等系统对接 |
| --- |


### refund_query_Y - 查询退换管理

- Category: 售后类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=refund_query_Y
- PHP file: refund_query.php
- Doc title: 查询退换管理
- Client path: 售后→售后管理→售后单
- Description: 获取ERP销售退货（换货）订单信息

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

| JSON | {<br>    "code": 2105,<br>    "message": "modified_from不能等于modified_to"<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、财务系统、SAP、数据分析等系统的对接 |
| --- |


### aftersales_refund_create_Y - 创建系统售后单

- Category: 售后类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=aftersales_refund_create_Y
- PHP file: aftersales_refund_create.php
- Doc title: 创建系统售后单
- Client path: 售后→售后管理→售后单
- Description: 创建系统售后单，---目前不支持换货 ，只支退货单，退货单类型只能是退款退货和退款不退货 基于系统单创建退款单

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

| JSON | {<br>    "code": 0,<br>    "message": "",<br>    "refund_id": "2809436287763742727",<br>    "refund_no": "RT2603240022"<br>} |
| --- | --- |

| JSON | {<br>    "code": 30402,<br>    "message": "订单明细id错误，请确认传值是否正确"<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、分销系统、全渠道等系统对接 |
| --- |


### vip_api_refund_query_Y - 查询原始退单

- Category: 售后类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_api_refund_query_Y
- PHP file: vip_api_refund_query.php
- Doc title: 原始平台退单查询
- Client path: 售后→售后管理→平台售后单
- Description: 

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

| JSON | {<br>    "code": 2180,<br>    "message": "start_time与end_time时间跨度不能超过最大范围"<br>} |
| --- | --- |

#### 其他表格

| 2.1 自研商城、财务系统、SAP、数据分析等系统的对接 |
| --- |


### aftersale_stockin_confirm_Y - 创建退货入库单

- Category: 售后类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=aftersale_stockin_confirm_Y
- PHP file: aftersale_stockin_confirm.php
- Doc title: 创建退货入库单
- Client path: 仓储--入库管理--退货入库单--新建
- Description: 推送旺店通ERP销售退货（换货）订单对应的入库单据给旺店通ERP，推送前提旺店通ERP的退换单状态为“待收货”

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

| JSON | {<br>	"code": 0,<br>	"message": "",<br>	"stockin_id": "2807203546011795458",<br>	"stockin_no": "RK2603180004",<br>	"refund_id": "2806954438558744604",<br>	"refund_no": "RT2603170237"<br>} |
| --- | --- |

| JSON | {<br>	"code": 11000000,<br>	"message": "该售后单状态不允许入库"<br>} |
| --- | --- |

#### 其他表格

| 2.1 线下ERP等系统对接 |
| --- |


## 采购类

| 服务名 | 接口名 | 描述 | 客户端路径 |
| --- | --- | --- | --- |
| purchase_order_query_Y | 查询采购单 | 获取旺店通ERP各种业务类型的采购单信息 | 采购→采购单 |
| purchase_return_query_Y | 查询采购退货单 | 获取旺店通ERP各种业务类型的采购单信息 | 采购→采购退货单 |
| purchase_order_push_Y | 创建采购单 | 新增创建采购单接口 | 采购→采购单 |
| purchase_return_order_push_Y | 创建采购退货单 | 新增创建采购退货单接口 | 采购→采购退货单 |
| purchase_apply_query_Y | 查询采购申请单 | 获取旺店通ERP的采购申请单及其明细信息 | 采购→采购申请单 |

### purchase_order_query_Y - 查询采购单

- Category: 采购类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_order_query_Y
- PHP file: purchase_order_query.php
- Doc title: 查询采购单管理
- Client path: 采购→采购单
- Description: 获取旺店通ERP各种业务类型的采购单信息

#### 接口说明

| 1.1 接口描述：获取旺店通ERP各种业务类型的采购单信息 |
| --- |
| 1.2 适用版本：250304迭代及之后 |
| 1.3 时间跨度：开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/purchase_order_query.php |
| 正式环境 | https://openapi.huice.com/openapi/purchase_order_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/purchase_order_query.php';<br><br>    $c->putApiParam('start_time', '2026-03-09 09:00:00');<br>    $c->putApiParam('end_time', '2026-03-09 10:00:00');<br>    $c->putApiParam('page_no', 0 );<br>    $c->putApiParam('page_size', 1 );<br><br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 开始时间 | start_time | datetime |  | 是 | 按最后修改时间增量获取数据,start_time作为开始时间,格式：yyyy-MM-dd HH:mm:ss，注意时分秒无效 |
| 结束时间 | end_time | datetime |  | 是 | 按最后修改时间增量获取数据,end_time作为结束时间,格式：yyyy-MM-dd HH:mm:ss |
| 查询时间类型 | time_type | int |  | 时间查询时必传 | 1：创建时间， 2：修改时间 |
| 分页大小 | page_size | int | 10 | 否 | 每页返回条数，输入值范围1~100，不传默认40，使用举例单击这里 |
| 页号 | page_no | int | 10 | 否 | 不传值默认从0页开始 |
| 采购单状态 | status | tinyint | 1 | 否 | 采购单状态5：待审核， 7：待财审， 10：已审核，11：待推送，12：推送失败，13：已推送，20：部分推送，30：已入库，99：已取消 |
| 仓库编号 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置）(不支持一次推送多个仓库编号) |
| 采购单号 | purchase_no | varchar | 40 | 否 | 采购单号 |
| 外部单号 | outer_no | varchar | 40 | 否 | ERP推送采购单外部返回单号（对应外部仓储单号） |
| 平台单号 | platform_order_no | varchar | 40 | 否 | 传该字段可以不传开始时间和结束时间 (接口创建采购单推送的outer_no会作为客户端的平台单号) |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:200表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 采购单列表节点 | purchase_list | data[] |  | 否 | 响应参数的1级数据节点，包含当前页的采购单及其明细的数据节点,节点下数据字段详见下述" purchase_list"和“details_list” |

| JSON | {<br>    "code": 200,<br>    "message": null,<br>    "total_count": 2,<br>    "purchase_list": [<br>        {<br>            "purchase_id": "2803943306390667268",<br>            "purchase_no": "CG2603090101",<br>            "provider_id": "0",<br>            "provider_name": "",<br>            "provider_no": "",<br>            "purchaser_name": "admin",<br>            "creator_id": "1976",<br>            "creator_name": "admin",<br>            "warehouse_no": "30",<br>            "warehouse_name": "北京自有仓库（测试0603）",<br>            "goods_fee": "0",<br>            "goods_count": "1",<br>            "cancel_num": "0",<br>            "remark": "",<br>            "status": 99,<br>            "created": "2026-03-09T09:49:39",<br>            "modified": "2026-03-10T09:18:06",<br>            "purchase_outer_no": "",<br>            "purchase_platform_order_no": "",<br>            "post_fee": "0",<br>            "details_list": [<br>                {<br>                    "rec_id": "2803943307317608452",<br>                    "purchase_id": "2803943306390667268",<br>                    "provider_id": "0",<br>                    "provider_name": "",<br>                    "provider_no": "",<br>                    "price": "0",<br>                    "num": "1",<br>                    "cancel_num": "0",<br>                    "remark": "",<br>                    "spec_id": "2803928459665998850",<br>                    "spec_name": "默认规格",<br>                    "spec_no": "2030808254194241537",<br>                    "goods_name": "活力开阳蕨麻饮品",<br>                    "goods_no": "2030808254194241537",<br>                    "purchase_price": "0"<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购单id | purchase_id | bigint(20) |  | 是 | 采购单id，采购单表主键 |
| 采购单号 | purchase_no | varchar | 40 | 是 | ERP系统采购单编号 |
| 外部单号 | purchase_outer_no | varchar | 40 | 是 | ERP推送采购单外部返回单号（对应外部仓储单号）。ERP客户端需升级至V2.3.8.6及以上版本可获取此字段 |
| 仓库 | warehouse_name | varchar | 64 | 是 | 仓库名称 |
| 仓库编号 | warehouse_no | varchar | 64 | 是 | 代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置） |
| 采购单状态 | status | tinyint | 4 | 是 | 5：待审核， 7：待财审，10：已审核，11：待推送，12：推送失败，13：已推送，20：部分推送，30：已入库，99：已取消 |
| 供应商名称 | provider_name | varchar | 64 | 是 | 供应商名称 |
| 采购员 | purchaser_name | varchar | 20 | 是 | 采购员 |
| 邮资 | post_fee | decimal | (19,4) | 是 | 邮资 |
| 备注 | remark | varchar | 255 | 是 | 采购单备注 |
| 最后修改时间 | modified | datetime |  | 是 | 单据的最后修改时间 |
| 创建时间 | created | datetime |  | 是 | 创建时间 |
| 创建人id | creator_id | int | 11 | 是 | 创建人id |
| 创建人姓名 | creator_name | varchar | 40 | 是 | 创建人姓名 |
| 供应商 | provider_id | bigint(20) |  | 是 | 供应商 |
| 货品总价 | goods_fee | decimal | (19,4) | 是 | 货品总价 |
| 货品数量 | goods_count | decimal | (19,4) | 是 | 货品数量 |
| 取消数量 | cancel_num | int | 11 | 是 | 取消数量 |
| 供应商编码 | provider_no | varchar | 40 | 是 | 供应商编码 |
| 供应商id | provider_id | int | 11 | 是 | 供应商id |
| 平台单号 | purchase_platform_order_no | varchar | 40 | 是 | 平台单号 |
| 采购单明细节点 | details_list | data[] | 40 | 是 | 响应参数的2级数据节点，,节点下数据字段详见下述“details_list” |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键 | rec_id | bigint(20) |  | 是 | 采购明细表主键id |
| 采购单id | purchase_id | bigint(20) |  | 是 | 采购单id |
| 商家编码 | spec_no | varchar | 40 | 是 | 代表单品（sku）所有属性的编码 |
| 数量 | num | decimal | (19,4) | 是 | 数量 |
| 单价 | price | decimal | (19,4) | 是 | 单价 |
| 备注 | remark | varchar | 255 | 是 | 明细备注 |
| 货品编号 | goods_no | varchar | 40 | 是 | 货品编号 |
| 货品名称 | goods_name | varchar | 255 | 是 | 货品名称 |
| 规格名称 | spec_name | varchar | 255 | 是 | 规格名称 |
| 规格id | spec_id | bigint(20) |  | 是 | 规格id |
| 采购金额 | purchase_price | decimal | (19,4) | 是 | 采购价 |
| 取消数量 | cancel_num | decimal | (19,4) | 是 | 取消数量 |
| 供应商编码 | provider_no | varchar | 40 | 是 | 供应商编码 |
| 供应商id | provider_id | int | 11 | 是 | 供应商id |
| 供应商名称 | provider_name | varchar | 40 | 是 | 供应商名称 |

#### 响应示例

| JSON | {<br>    "code": 2900,<br>    "message": "必传参数缺失:start_time和end_time不能为空"<br>} |
| --- | --- |

#### 其他表格

| 2.1 SAP、线下ERP、SRM、SCM等系统对接 |
| --- |


### purchase_return_query_Y - 查询采购退货单

- Category: 采购类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_return_query_Y
- PHP file: purchase_return_query.php
- Doc title: 查询采购退货单
- Client path: 采购→采购退货单
- Description: 获取旺店通ERP各种业务类型的采购单信息

#### 接口说明

| 1.1 接口描述：获取旺店通ERP各种业务类型的采购单信息 |
| --- |
| 1.2 适用版本：网页版 |
| 1.3 时间跨度：开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/purchase_return_query.php |
| 正式环境 | https://openapi.huice.com/openapi/purchase_return_query.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，获取方式点击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>require_once '../WdtClient.php';<br>$c = new WdtClient();<br>$c->sid = '';<br>$c->appkey = '';<br>$c->appsecret = '';<br>$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/purchase_return_query.php';<br><br>$c->putApiParam('page_no', 0);<br>$c->putApiParam('page_size', 100);<br>$c->putApiParam('return_no', 'CT2604030002');<br><br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
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
| 查询时间类型 | time_type | int | 1 | 否 | 1：创建时间， 2：修改时间 |
| 状态 | status | tinyint | 1 | 否 | 采购单状态5：待审核，10：已审核，11：待推送，12：推送失败，13：已推送，20：部分推送，30：已出库，99：已取消 |
| 仓库编号 | warehouse_no | varchar | 40 | 否 | 代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置）(不支持一次推送多个仓库编号) |
| 退货单号 | return_no | varchar | 40 | 否 | 按照退货单号查询不校验时间参数 |
| 外部单号 | outer_no | varchar | 40 | 否 | 外部单号 |
| 平台单号 | platform_order_no | varchar | 40 | 否 | 按照平台单号查询不校验时间参数(接口创建采购退货单推送的outer_no会作为客户端的平台单号) |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:200表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |
| 数据条数 | total_count | int | 10 | 否 | 符合条件的数据条数，用来分页 当page_no = 0时返回 |
| 采购退货单数据节点 | purchase_list | data[] |  | 否 | 响应参数的1级数据节点，包含当前页的采购单及其明细的数据节点,节点下数据字段详见下述" purchase_list"和“details_list” |

| JSON | {<br>    "code": 200,<br>    "message": null,<br>    "total_count": 1,<br>    "purchase_list": [<br>        {<br>            "return_id": "2813006528200572931",<br>            "return_no": "CT2604030002",<br>            "provider_id": "1977902135890620418",<br>            "provider_name": "毛毛的店铺",<br>            "provider_no": "S0027",<br>            "purchaser_name": "",<br>            "creator_id": "-1",<br>            "creator_name": "openapi",<br>            "warehouse_no": "38",<br>            "warehouse_name": "滑雪场器材仓库1",<br>            "goods_fee": "0",<br>            "goods_count": "6",<br>            "cancel_num": "0",<br>            "remark": "备注",<br>            "status": 10,<br>            "created": "2026-04-03T10:03:39",<br>            "modified": "2026-04-03T10:03:39",<br>            "purchase_outer_no": "",<br>            "purchase_platform_order_no": "2026040300002",<br>            "details_list": [<br>                {<br>                    "rec_id": "2813006528246710275",<br>                    "return_id": "2813006528200572931",<br>                    "provider_id": "1977902135890620418",<br>                    "provider_name": "毛毛的店铺",<br>                    "provider_no": "S0027",<br>                    "price": "149.3097",<br>                    "num": "6",<br>                    "cancel_num": "0",<br>                    "remark": "采购货品明细备注",<br>                    "spec_id": "2750004503452319778",<br>                    "spec_name": "rm5555货品档案的规格铭恒",<br>                    "spec_no": "20251010-0085",<br>                    "goods_name": "这是货品档案的货品名称",<br>                    "goods_no": "20251010-007",<br>                    "purchase_price": "895.8582"<br>                }<br>            ]<br>        }<br>    ]<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购退货单id | return_id | int | 11 | 是 | 采购退货单主键id |
| 退货单号 | return_no | varchar | 40 | 是 | 退货单号 |
| 仓库 | warehouse_name | varchar | 64 | 是 | 仓库名称 |
| 仓库编号 | warehouse_no | varchar | 64 | 是 | 代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置） |
| 采购退货单状态 | status | tinyint | 4 | 是 | 5：待审核，10：已审核，11：待推送，12：推送失败，13：已推送，20：部分推送，30：已出库，99：已取消 |
| 供应商名称 | provider_name | varchar | 64 | 是 | 供应商名称 |
| 供应商编码 | provider_no | varchar | 40 | 是 | 供应商编码 |
| 采购员名称 | purchaser_name | varchar | 20 | 是 | 采购员名称 |
| 采购员 | purchaser_id | int | 10 | 是 | 采购员id |
| 备注 | remark | varchar | 255 | 是 | 采购单备注 |
| 最后修改时间 | modified | datetime |  | 是 | 单据的最后修改 |
| 创建时间 | created | datetime |  | 是 | 创建时间 |
| 制单员id | creator_id | int | 11 | 是 | 制单员id |
| 制单员姓名 | creator_name | varchar | 40 | 是 | 制单员姓名 |
| 供应商id | provider_id | int | 11 | 是 | 供应商id |
| 货品总价 | goods_fee | decimal | (19,4) | 是 | 货品总价 |
| 货品数量 | goods_count | decimal | (19,4) | 是 | 货品数量 |
| 取消数量 | cancel_num | int | 11 | 是 | 取消数量 |
| 平台单号 | purchase_platform_order_no | varchar | 40 | 是 | 平台单号 |
| 采购退货单货品列表节点 | details_list | data[] | 40 | 是 | 响应参数的2级数据节点，包含采购退货单货货品明细所有属性信息，节点下数据字段详见下述“detail_list” |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键 | rec_id | int | 11 | 是 | 采购明细表主键id |
| 采购退货单id | return_id | int | 11 | 是 | 采购退货单主键id |
| 商家编码 | spec_no | varchar | 40 | 是 | 代表单品（sku）所有属性的编码 |
| 退货数量 | num | decimal | (19,4) | 是 | 退货数量 |
| 单价 | price | decimal | (19,4) | 是 | 单价 |
| 备注 | remark | varchar | 255 | 是 | 明细备注 |
| 货品编号 | goods_no | varchar | 40 | 是 | 货品编号 |
| 货品名称 | goods_name | varchar | 255 | 是 | 货品名称 |
| 规格名称 | spec_name | varchar | 255 | 是 | 规格名称 |
| 规格id | spec_id | int | 11 | 是 | 规格id |
| 退货金额 | purchase_price | decimal | (19,4) | 是 | 退货金额 |
| 取消数量 | cancel_num | int | 11 | 是 | 取消数量 |
| 供应商id | provider_id | int | 11 | 是 | 供应商id |
| 供应商编码 | provider_no | varchar | 40 | 是 | 供应商编码 |
| 供应商名称 | provider_name | varchar | 40 | 是 | 供应商名称 |

#### 响应示例

| JSON | {<br>    "code": 2160,<br>    "message": "start_time和end_time为空或不是有效的时间格式"<br>} |
| --- | --- |

#### 其他表格

| 2.1 SAP、线下ERP、SRM、SCM等系统对接 |
| --- |


### purchase_order_push_Y - 创建采购单

- Category: 采购类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_order_push_Y
- PHP file: purchase_order_push.php
- Doc title: 创建采购单
- Client path: 采购→采购单
- Description: 新增创建采购单接口

#### 接口说明

| 1.1 接口描述：①新增创建采购单接口 |
| --- |
| 1.2 适用版本：网页版 |

#### 调用场景

| 2.1 举例说明：新增创建采购单接口 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/purchase_order_push.php |
| 正式环境 | https://openapi.huice.com/openapi/purchase_order_push.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>    require_once("../WdtClient.php");<br>    $c = new WdtClient;<br>    $c->sid = '';<br>    $c->appkey = '';<br>    $c->appsecret = "";<br>    $c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/purchase_order_push.php';<br>    $purchase_info= array(<br>		"provider_no"=>"S0014",<br>		"warehouse_no"=>"38",<br>		"outer_no"=> "2026032600001",<br>		"expect_arrive_time" => "2027-09-01",<br>		"is_check"=>1,<br>		"details_list"=>array(<br>			array(<br>				"spec_no"=>"17773395551",<br>				"num"=>"100",<br>				"price"=>"180"<br>				),<br>			array(<br>				"spec_no"=>"c97111011c1",<br>				"num"=>"100",<br>				"price"=>"180"<br>				)<br>		)<br><br>    );<br><br>    $c->putApiParam('purchase_info',json_encode($purchase_info));<br>    $json = $c->wdtOpenApi();<br>    var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购列表节点 | purchase_info | data |  | 是 | 请求参数的1级数据节点，包含采购单所有属性信息的数据节点，节点下数据字段详见下述“purchase_info” |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商编号 | provider_no | varchar | 20 | 是 | 供应商编号，ERP供应商档案必须存在此编号，否则推送失败 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置），用于创建指定仓库数据信息(不支持一次推送多个仓库编码) |
| API单号 | outer_no | varchar | 40 | 是 | API单号,该单号会记录到客户端 平台单号上 |
| 自动审核 | is_check | tinyint | 1 | 否 | 是否自动审核，0 不审核，1 审核，默认不自动审核 |
| 采购姓名 | purchase_name | varchar | 40 | 否 | 采购员:姓名 |
| 预计到货日期 | expect_arrive_time | date |  | 否 | 采购单对应货品预计到达仓库时间，时间格式：YYYY-MM-DD |
| 采购时间 | real_create_date | date |  | 否 | 采购时间，时间格式：YYYY-MM-DD |
| 运费 | post_fee | decimal | (19,4) | 否 | 邮资 |
| 备注 | remark | varchar | 255 | 否 | 采购单备注 |
| API单号作为采购单号 | is_use_outer_no | tinyint |  | 否 | 是否使用API单号作为采购单号  1.使用 0.不使用 默认不使用 |
| 采购明细节点 | details_list | data[] |  | 是 | 请求参数的2级数据节点，包含采购单所有货品明细信息的数据节点，节点下数据字段详见下述“details_list” |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码（新） | spec_no | varchar | 40 | 是 | 代表单品(sku)所有属性的唯一编码，用于系统单品区分，SKU概念介绍单击这里 |
| 采购量 | num | decimal | (19,4) | 否 | 采购量 |
| 采购价格 | price | decimal | (19,4) | 是 | 采购价格,按采购单位，税前单价 |
| 折扣 | discount | decimal | (19,4) | 否 | 折扣字段，默认值为1，1代表原价，无折扣；假设需要折扣为一折时，可将字段值传为0.1，同理，折扣为5折时，传值0.5；折扣为八折时，传值0.8，以此类推 |
| 行备注 | remark | varchar | 255 | 否 | 采购货品明细备注 |

#### 响应示例

| JSON | {<br>    "code": 0,<br>    "message": "CG2603260001"<br>} |
| --- | --- |

| JSON | {<br>    "code": 140000001,<br>    "message": "采购单信息异常：存在重复的商家编码17773395551"<br>} |
| --- | --- |


### purchase_return_order_push_Y - 创建采购退货单

- Category: 采购类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_return_order_push_Y
- PHP file: purchase_return_order_push.php
- Doc title: 创建采购退货单
- Client path: 采购→采购退货单
- Description: 新增创建采购退货单接口

#### 接口说明

| 1.1 接口描述：新增创建采购退货单接口 |
| --- |
| 1.2 适用版本：网页版 |

#### 调用场景

| 2.1 举例说明：新增创建采购退货单接口 |
| --- |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/purchase_return_order_push.php |
| 正式环境 | https://openapi.huice.com/openapi/purchase_return_order_push.php |

#### 公共请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 卖家账号 | sid | String |  | 是 | 购买ERP时由旺店通分配给ERP购买方，请从ERP购买方获取。 |
| 接口账号 | appkey | String |  | 是 | 本开放平台“自助对接”功能模块内自助申请，申请流程单击这里 |
| 时间戳 | timestamp | int |  | 是 | 北京时间1970-01-01 08:00:00起至现在的总秒数，10位int值,旺店通企业版API服务端允许请求最大时间误差为5min，date.timezone = Asia/Shanghai。 |
| 签名 | sign | String |  | 是 | API输入参数签名结果，签名算法介绍单击这里 |

| PHP | <?php<br>require_once '../WdtClient.php';<br>$c = new WdtClient();<br>$c->sid = '';<br>$c->appkey = '';<br>$c->appsecret = '';<br>$c->gatewayUrl = 'https://openapi.ali.huice.cc/openapi/purchase_return_order_push.php';<br><br>$return_info = [<br>    'provider_no' => 'S0027',<br>    'warehouse_no' => '38',<br>    'outer_no' => '2026040300002',<br>    'is_check' => 1,<br>    'contact' => '联系人信息',<br>    'telno' => '15124578965',<br>    'address' => '天津 天津市 滨海新区 一条街道200',<br>    'post_fee' => '10',<br>    'remark' => '备注',<br><br>    'details_list' => [<br>        [<br>            'spec_no' => '20251010-0085',<br>            'num' => '6',<br>            'price' => '149.3097',<br>            'detail_remark' => '采购货品明细备注',<br>        ]<br>    ],<br>];<br><br>$c->putApiParam('return_info', json_encode($return_info, JSON_UNESCAPED_UNICODE));<br>$json = $c->wdtOpenApi();<br>var_dump($json);<br>?> |
| --- | --- |
| JAVA |  |
| C# |  |
| python |  |

#### 业务请求参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购列表节点 | return_info | data[ ] |  | 是 | 请求参数的1级数据节点，包含采购退货单所有属性信息的数据节点，节点下数据字段详见下述“return_info”列表 |

#### 公共响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 错误码 | code | int | 11 | 是 | 状态码:0表示成功,其他表示失败 |
| 错误描述 | message | varchar | 255 | 是 | 错误描述 |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 供应商编号 | provider_no | varchar | 20 | 是 | 供应商编号，ERP供应商档案必须存在此编号，否则推送失败 |
| 出库仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置），用于创建指定仓库数据信息(不支持一次推送多个仓库编码) |
| API外部单号 | outer_no | varchar | 40 | 是 | API外部单号，该单号会记录到客户端 平台单号上 |
| 是否使用外部单号作为采购退货单号 | is_use_outer_no | tinyint | 1 | 是 | 是否使用外部单号作为采购退货单号，1 使用，0 不使用（默认为0 不使用） |
| 自动审核 | is_check | tinyint | 1 | 否 | 是否自动审核，0 不审核，1 审核，默认不自动审核 |
| 退货时间 | real_create_date | datetime |  | 否 | 退货时间  格式：yyyy-MM-dd HH:mm:ss |
| 采购姓名 | purchase_name | varchar | 40 | 否 | 采购员:姓名 |
| 收件人姓名 | contact | varchar | 40 | 否 | 联系人 |
| 收件人电话 | telno | varchar | 32 | 否 | 联系电话 |
| 详细地址 | address | varchar | 255 | 否 | 详细地址 |
| 运费 | post_fee | decimal | (19,4) | 否 | 联系人 |
| 备注 | remark | varchar | 255 | 否 | 采购单备注 |
| 采购明细节点 | details_list | data[] |  | 是 | 请求参数的2级数据节点，包含采购退货单所有货品明细属性信息的数据节点，节点下数据字段详见下述“detail_list”列表 |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 商家编码（新） | spec_no | varchar | 40 | 是 | 代表单品(sku)所有属性的唯一编码，用于系统单品区分，SKU概念介绍单击这里 |
| 退货数量 | num | decimal | (19,4) | 否 | 退货数量 |
| 退货价格 | price | decimal | (19,4) | 是 | 单价 |
| 行备注 | detail_remark | varchar | 255 | 否 | 采购货品明细备注 |

#### 响应示例

| JSON | {<br>    "code": 0,<br>    "message": "CT2604030002"<br>} |
| --- | --- |

| JSON | {<br>    "code": 140000002,<br>    "message": "采购退货单信息异常：2026040300002API单号，系统中已存在"<br>} |
| --- | --- |


### purchase_apply_query_Y - 查询采购申请单

- Category: 采购类
- Doc URL: https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_apply_query_Y
- PHP file: purchase_apply_query.php
- Doc title: 查询采购申请单
- Client path: 采购→采购申请单
- Description: 获取旺店通ERP的采购申请单及其明细信息

#### 接口说明

| 1.1 接口描述：获取旺店通ERP的采购申请单及其明细信息 |
| --- |
| 1.2 适用版本： |
| 1.3 增量获取：按照采购申请单的最后修改时间增量获取数据，请求时输入start_time和end_time作为时间跨度的筛选条件。 |
| 1.4 时间跨度：start_time和end_time最大跨度为30天，开始时间和结束时间取值范围为闭区间取值，例如2018-11-01 00:00:00至2018-11-30 23:59:59，建议根据获取数据量的多少适当减小时间跨度。 |

#### 请求地址

| 环境 | HTTP地址 |
| --- | --- |
| 测试环境 | https://openapi.ali.huice.cc/openapi/purchase_apply_query.php |
| 正式环境 | https://openapi.huice.com/openapi/purchase_apply_query.php |

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
| 采购申请单号 | purchase_apply_no | varchar | 40 | 否 | ERP系统采购申请单编号，传该字段不限制时间跨度 |
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
| 采购申请单列表节点 | purchase_list | data[] |  | 是 | 响应参数的1级数据节点，包含当前页的采购申请单及其明细的数据节点,节点下数据字段详见下述" purchase_list"和“details_list” |

| JSON | {<br>	"code": "0",<br>	"message": "",<br>	"total_count": "7",<br>	"purchase_list": [{<br>		"apply_id": "118",<br>		"purchase_apply_no": "POA202005190001",<br>		"status": "30",<br>		"createtor_name": "wanxie2-test",<br>		"warehouse_no": "wanxie2-test",<br>		"name": "wanxie2-test",<br>		"real_num": "200.0000",<br>		"ref_num": "200.0000",<br>		"unref_num": "0.0000",<br>		"expected_time": "0000-00-00 00:00:00",<br>		"remark": "",<br>		"modified": "2020-05-19 11:57:04",<br>		"created": "2020-05-19 11:48:44",<br>		"details_list": [{<br>			"rec_id": "335",<br>			"apply_id": "118",<br>			"remark": "",<br>			"purchase_apply_no": "POA202005190001",<br>			"spec_name": "默认规格",<br>			"spec_no": "fapiao",<br>			"goods_name": "demlution test product",<br>			"brand_no": "BD201911060035",<br>			"brand_name": "无",<br>			"class_name": "无",<br>			"goods_no": "fapiao",<br>			"short_name": "dem product",<br>			"real_num": "100.0000",<br>			"ref_num": "100.0000",<br>			"provider_no": "",<br>			"provider_name": ""<br>		}, {<br>			"rec_id": "336",<br>			"apply_id": "118",<br>			"remark": "",<br>			"purchase_apply_no": "POA202005190001",<br>			"spec_name": "默认规格",<br>			"spec_no": "fapiao2",<br>			"goods_name": "demlution test product 2",<br>			"brand_no": "BD201911060035",<br>			"brand_name": "无",<br>			"class_name": "无",<br>			"goods_no": "fapiao2",<br>			"short_name": "dem test 2",<br>			"real_num": "100.0000",<br>			"ref_num": "100.0000",<br>			"provider_no": "",<br>			"provider_name": ""<br>		}]<br>	}]<br>} |
| --- | --- |

#### 业务响应参数

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 采购申请单id | apply_id | int | 11 | 是 | 采购申请单id，采购申请单表主键 |
| 采购申请单号 | purchase_apply_no | varchar | 20 | 是 | ERP系统采购申请单编号 |
| 申请量 | real_num | decimal | (19,4) | 是 | 申请量 |
| 申请人 | createor_name | varchar | 40 | 是 | 申请人 |
| 仓库 | name | varchar | 64 | 是 | 仓库名称 |
| 仓库编号 | warehouse_no | varchar | 40 | 是 | 代表仓库所有属性的唯一编码，用于仓库区分，ERP内支持自定义（ERP仓库界面设置） |
| 采购申请单状态 | status | tinyint | 4 | 是 | 采购申请单状态：99 已取消 10 待确认  20 待引用  30 部分引用  40 已引用 |
| 引用量 | ref_num | decimal | (19,4) | 是 | 引用量 |
| 未引用量 | unref_num | decimal | (19,4) | 是 | 未引用量 |
| 期望到货时间 | expected_time | datetime |  | 是 | 期望到货时间  格式：yyyy-MM-dd HH:mm:ss |
| 备注 | remark | varchar | 255 | 是 | 采购申请单备注 |
| 最后修改时间 | modified | datetime |  | 是 | 单据的最后修改时间，格式：yyyy-MM-dd HH:mm:ss |
| 创建时间 | created | datetime |  | 是 | 单据创建时间，格式：yyyy-MM-dd HH:mm:ss |
| 采购申请单明细节点 | details_list | data[] |  |  | 响应参数的2级数据节点，,节点下数据字段详见下述“details_list” |

| 名称 | 字段 | 类型 | 长度 | 必须 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 主键 | rec_id | int | 11 | 是 | 采购明细表主键id |
| 采购单id | apply_id | int | 11 | 是 | 采购单id |
| 采购申请单号 | purchase_apply_no | varchar | 20 | 是 | 采购申请单号 |
| 商家编码 | spec_no | varchar | 40 | 是 | 代表单品（sku）所有属性的编码，SKU概念介绍，单击这里 |
| 规格名称 | spec_name | varchar | 255 | 是 | 规格名称 |
| 品牌 | brand_name | varchar | 64 | 是 | 品牌名称 |
| 品牌编号 | brand_no | varchar | 32 | 是 | 品牌编号 |
| 分类 | class_name | decimal | 64 | 是 | 分类 |
| 申请采购量 | real_num | decimal | (19,4) | 是 | 申请采购量 |
| 已引用量 | ref_num | decimal | (19,4) | 是 | 已引用量 |
| 供应商编号 | provider_no | varchar | 20 | 是 | 供应商编号 |
| 供应商名称 | provider_name | varchar | 64 | 是 | 供应商名称 |
| 备注 | remark | varchar | 255 | 是 | 明细备注 |
| 货品编号 | goods_no | varchar | 40 | 是 | 货品编号 |
| 货品名称 | goods_name | varchar | 255 | 是 | 货品名称 |
| 货品简称 | short_name | varchar | 255 | 是 | 货品简称 |

#### 响应示例

| JSON | {<br>	"code": 2180,<br>	"message": "start_time与end_time时间跨度不能超过最大范围30天"<br>} |
| --- | --- |

#### 其他表格

| 2.1 财务系统、SAP、数据分析等系统的对接 |
| --- |

