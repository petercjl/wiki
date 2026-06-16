---
title: 旺店通 基础类 API 使用手册
type: concept
created: 2026-06-03
updated: 2026-06-03
domain: 电商运营
tags: [ecommerce, erp, wangdian, api]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
status: active
---

# 旺店通 基础类 API 使用手册

## 用途

本页整理旺店通开放平台 基础类 的具体接口使用方法，面向后续写代码或创建 Codex/Hermes skill。每个接口包含服务名、PHP 文件、请求地址、业务请求参数、业务响应字段、示例和注意事项。

## 本类接口

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

## 接口详情

### purchase_provider_query_Y：查询供应商

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `purchase_provider_query_Y` |
| PHP 文件 | `purchase_provider_query.php` |
| 文档标题 | 查询供应商 |
| 描述 | 批量获取旺店通ERP内供应商信息。 |
| 客户端路径 | 采购→供应商 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_provider_query_Y |

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

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### cfg_tags_query_Y：查询标签

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `cfg_tags_query_Y` |
| PHP 文件 | `cfg_tags_query.php` |
| 文档标题 | 查询标签 |
| 描述 | 查询标签 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=cfg_tags_query_Y |

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

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### unique_code_query_Y：查询唯一码

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `unique_code_query_Y` |
| PHP 文件 | `unique_code_query.php` |
| 文档标题 | 查询唯一码 |
| 描述 | 获取旺店通ERP内唯一码数据 |
| 客户端路径 | 档口→拿货标签管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=unique_code_query_Y |

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

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### logistics_Y：物流公司

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `logistics_Y` |
| PHP 文件 | `` |
| 文档标题 |  |
| 描述 | 批量获取旺店通ERP内物流档案信息 |
| 客户端路径 | 配置→快递管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=logistics_Y |

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

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### employee_query_Y：员工查询

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `employee_query_Y` |
| PHP 文件 | `employee_query.php` |
| 文档标题 | 员工查询 |
| 描述 | 获取ERP的员工页面信息 |
| 客户端路径 | 配置→权限设置 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=employee_query_Y |

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

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### vip_stockout_sales_weight_push_Y：称重

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `vip_stockout_sales_weight_push_Y` |
| PHP 文件 | `vip_stockout_sales_weight_push.php` |
| 文档标题 | 重量回传 |
| 描述 | 将重量回传写入旺店通ERP销售订单 |
| 客户端路径 | 仓储→包裹称重 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_stockout_sales_weight_push_Y |

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

### JSON

```text
{
    "code": 0,
    "message": "",
    "channel_no": "",
    "logistics_name": "中通快递2",
    "logistics_type": "54"
}
```

### JSON

```text
{
    "code": 11000301,
    "message": "订单已发货，发货时间：2026-03-13 15:33:37 操作人：openapi",
    "channel_no": null,
    "logistics_name": null,
    "logistics_type": null
}
```


### shop_Y：查询店铺

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `shop_Y` |
| PHP 文件 | `shop.php` |
| 文档标题 | 查询店铺 |
| 描述 | 批量获取旺店通ERP内店铺档案信息 |
| 客户端路径 | 配置→绑定店铺 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=shop_Y |

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

### JSON

```text
{
    "code": 1020,
    "message": "系统异常"
}
```


### warehouse_query_Y：查询仓库

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `warehouse_query_Y` |
| PHP 文件 | `warehouse_query.php` |
| 文档标题 | 查询仓库 |
| 描述 | 批量获取旺店通ERP内仓库档案信息 |
| 客户端路径 | 配置→仓库信息维护 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=warehouse_query_Y |

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

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### sys_logisitcs_code_Y：物流公司枚举

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `sys_logisitcs_code_Y` |
| PHP 文件 | `` |
| 文档标题 |  |
| 描述 |  |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=sys_logisitcs_code_Y |

#### 接口说明

| 1.1 接口描述：物流公司枚举 |
| --- |
| 1.2 适用版本：网页版 |


#### 调用场景

| 2.1 举例说明：自有商城接入ERP、金蝶接入、用友接入、SAP接入等 |
| --- |


### unique_code_status_change_Y：修改唯一码状态为已到货

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `unique_code_status_change_Y` |
| PHP 文件 | `unique_code_status_change.php` |
| 文档标题 | 修改唯一码状态为已到货 |
| 描述 | 将旺店通唯一码状态变更为已到货 |
| 客户端路径 | 档口→拿货标签管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=unique_code_status_change_Y |

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

### JSON

```text
{
    "code": 0,
    "message": "",
    "success_count": 1,
    "fail_count": 0,
    "fail_list": [

    ]
}
```

### JSON

```text
{
    "code": 0,
    "message": "",
    "success_count": 1,
    "fail_count": 1,
    "fail_list": [{
        "unique_code": "0000006273626",
        "fail_msg": "仅支持修改“待拿货”状态的唯一码，唯一码状态是已到货，不允许修改！"
    }]
}
```


### purchase_provider_create_Y：创建供应商

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `purchase_provider_create_Y` |
| PHP 文件 | `purchase_provider_create.php` |
| 文档标题 | 创建供应商 |
| 描述 | 给旺店通推送供应商信息 |
| 客户端路径 | 采购→供应商 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_provider_create_Y |

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

### JSON

```text
{
    "code": 0,
    "message": ""
}
```


### order_audit_Y：业务单据审核接口

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `order_audit_Y` |
| PHP 文件 | `order_audit.php` |
| 文档标题 | 业务单据审核接口 |
| 描述 | 第三方系统触发erp中待审核（待确认）的业务单据审核 |
| 客户端路径 | 订单→订单管理→待审核 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=order_audit_Y |

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

### JSON

```text
{
	"code": 0,
	"message": "",
	"errors_list": []
}
```

### JSON

```text
{
	"code": 0,
	"message": "",
	"errors_list": [{
		"order_no": "CG2512160049",
		"error_info": "仅可审核 待审核 状态的采购单"
	}]
}
```


### order_cancel_Y：业务单据取消

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `order_cancel_Y` |
| PHP 文件 | `order_cancel.php` |
| 文档标题 | 业务单据取消 |
| 描述 | 第三方系统触发erp中业务单据取消。 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=order_cancel_Y |

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

### JSON

```text
{
	"code": 0,
	"message": "处理成功"
}
```

### JSON

```text
{
	"code": -1,
	"message": "采购单状态不正确"
}
```


### order_stop_waiting_Y：业务单停止等待

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `order_stop_waiting_Y` |
| PHP 文件 | `order_stop_waiting.php` |
| 文档标题 | 业务单停止等待 |
| 描述 | 第三方系统对接处理业务单据进行停止等待 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=order_stop_waiting_Y |

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

### JSON

```text
{
	"code": 0,
	"message": "处理成功"
}
```

### JSON

```text
{
    "code": -1,
    "message": "采购单状态不正确"
}
```


### order_reject_Y：业务单据驳回审核接口

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `order_reject_Y` |
| PHP 文件 | `order_reject.php` |
| 文档标题 | 业务单据驳回审核接口 |
| 描述 | 第三方系统触发erp中业务单据驳回审核 |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=order_reject_Y |

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

### JSON

```text
{
	"code": 0,
	"message": "",
	"errors_list": []
}
```

### JSON

```text
{
    "code": 0,
    "message": "",
    "errors_list": [
        {
            "order_no": "JY2503050349",
            "error_info": null
        }
    ]
```


### warehouse_create_Y：

| 项目 | 内容 |
|---|---|
| 分类 | 基础类 |
| 服务名 | `warehouse_create_Y` |
| PHP 文件 | `` |
| 文档标题 |  |
| 描述 |  |
| 客户端路径 |  |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=warehouse_create_Y |

## 相关页面

- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/domains/视觉制作/05-小红书风格AI生图/index|旺店通开放平台 API 知识库]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/01-旺店通API能力地图|旺店通 API 能力地图]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/02-旺店通API Skill创建指南|旺店通 API Skill 创建指南]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
