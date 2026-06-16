---
title: 旺店通 采购类 API 使用手册
type: concept
created: 2026-06-03
updated: 2026-06-03
domain: 电商运营
tags: [ecommerce, erp, wangdian, api]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
status: active
---

# 旺店通 采购类 API 使用手册

## 用途

本页整理旺店通开放平台 采购类 的具体接口使用方法，面向后续写代码或创建 Codex/Hermes skill。每个接口包含服务名、PHP 文件、请求地址、业务请求参数、业务响应字段、示例和注意事项。

## 本类接口

| 服务名 | 接口名 | 描述 | 客户端路径 |
|---|---|---|---|
| purchase_order_query_Y | 查询采购单 | 获取旺店通ERP各种业务类型的采购单信息 | 采购→采购单 |
| purchase_return_query_Y | 查询采购退货单 | 获取旺店通ERP各种业务类型的采购单信息 | 采购→采购退货单 |
| purchase_order_push_Y | 创建采购单 | 新增创建采购单接口 | 采购→采购单 |
| purchase_return_order_push_Y | 创建采购退货单 | 新增创建采购退货单接口 | 采购→采购退货单 |
| purchase_apply_query_Y | 查询采购申请单 | 获取旺店通ERP的采购申请单及其明细信息 | 采购→采购申请单 |

## 接口详情

### purchase_order_query_Y：查询采购单

| 项目 | 内容 |
|---|---|
| 分类 | 采购类 |
| 服务名 | `purchase_order_query_Y` |
| PHP 文件 | `purchase_order_query.php` |
| 文档标题 | 查询采购单管理 |
| 描述 | 获取旺店通ERP各种业务类型的采购单信息 |
| 客户端路径 | 采购→采购单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_order_query_Y |

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

### JSON

```text
{
    "code": 2900,
    "message": "必传参数缺失:start_time和end_time不能为空"
}
```


### purchase_return_query_Y：查询采购退货单

| 项目 | 内容 |
|---|---|
| 分类 | 采购类 |
| 服务名 | `purchase_return_query_Y` |
| PHP 文件 | `purchase_return_query.php` |
| 文档标题 | 查询采购退货单 |
| 描述 | 获取旺店通ERP各种业务类型的采购单信息 |
| 客户端路径 | 采购→采购退货单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_return_query_Y |

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

### JSON

```text
{
    "code": 2160,
    "message": "start_time和end_time为空或不是有效的时间格式"
}
```


### purchase_order_push_Y：创建采购单

| 项目 | 内容 |
|---|---|
| 分类 | 采购类 |
| 服务名 | `purchase_order_push_Y` |
| PHP 文件 | `purchase_order_push.php` |
| 文档标题 | 创建采购单 |
| 描述 | 新增创建采购单接口 |
| 客户端路径 | 采购→采购单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_order_push_Y |

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

### JSON

```text
{
    "code": 0,
    "message": "CG2603260001"
}
```

### JSON

```text
{
    "code": 140000001,
    "message": "采购单信息异常：存在重复的商家编码17773395551"
}
```


### purchase_return_order_push_Y：创建采购退货单

| 项目 | 内容 |
|---|---|
| 分类 | 采购类 |
| 服务名 | `purchase_return_order_push_Y` |
| PHP 文件 | `purchase_return_order_push.php` |
| 文档标题 | 创建采购退货单 |
| 描述 | 新增创建采购退货单接口 |
| 客户端路径 | 采购→采购退货单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_return_order_push_Y |

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

### JSON

```text
{
    "code": 0,
    "message": "CT2604030002"
}
```

### JSON

```text
{
    "code": 140000002,
    "message": "采购退货单信息异常：2026040300002API单号，系统中已存在"
}
```


### purchase_apply_query_Y：查询采购申请单

| 项目 | 内容 |
|---|---|
| 分类 | 采购类 |
| 服务名 | `purchase_apply_query_Y` |
| PHP 文件 | `purchase_apply_query.php` |
| 文档标题 | 查询采购申请单 |
| 描述 | 获取旺店通ERP的采购申请单及其明细信息 |
| 客户端路径 | 采购→采购申请单 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=purchase_apply_query_Y |

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

### JSON

```text
{
	"code": 2180,
	"message": "start_time与end_time时间跨度不能超过最大范围30天"
}
```


## 相关页面

- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/domains/视觉制作/05-小红书风格AI生图/index|旺店通开放平台 API 知识库]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/01-旺店通API能力地图|旺店通 API 能力地图]]
- [[domains/电商运营/30-ERP与系统工具/01-旺店通开放平台API/02-旺店通API Skill创建指南|旺店通 API Skill 创建指南]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
