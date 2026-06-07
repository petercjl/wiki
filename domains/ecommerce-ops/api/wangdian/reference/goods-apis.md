---
title: 旺店通 货品类 API 使用手册
type: concept
created: 2026-06-03
updated: 2026-06-03
domain: ecommerce-ops
tags: [ecommerce, erp, wangdian, api]
sources:
  - raw/api/wangdian-openapi/wangdian-openapi-full-scrape-2026-06-03.json
status: active
---

# 旺店通 货品类 API 使用手册

## 用途

本页整理旺店通开放平台 货品类 的具体接口使用方法，面向后续写代码或创建 Codex/Hermes skill。每个接口包含服务名、PHP 文件、请求地址、业务请求参数、业务响应字段、示例和注意事项。

## 本类接口

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

## 接口详情

### vip_api_goods_query_Y：平台货品查询

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `vip_api_goods_query_Y` |
| PHP 文件 | `vip_api_goods_query.php` |
| 文档标题 | 查询平台货品 |
| 描述 | 获取ERP的平台货品信息 |
| 客户端路径 | 商品→平台商品 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=vip_api_goods_query_Y |

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

### JSON

```text
{
    "code": 2104,
    "message": "start_time与end_time时间跨度不能超过最大范围 30天"
}
```


### goods_query_Y：查询货品档案

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `goods_query_Y` |
| PHP 文件 | `goods_query.php` |
| 文档标题 | 查询货品档案 |
| 描述 | 获取旺店通ERP的货品档案资料，“货品档案”其他系统称为“物料档案”“商品档案”等 |
| 客户端路径 | 商品→系统货品 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=goods_query_Y |

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

### JSON

```text
{
    "code": "20",
    "message": "请求范围过宽，请增加请求参数条件过滤"
}
```


### api_goodsspec_push_Y：创建平台货品

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `api_goodsspec_push_Y` |
| PHP 文件 | `api_goodsspec_push.php` |
| 文档标题 | 创建平台货品 |
| 描述 | 在推送销售订单给旺店通ERP之前，需要映射匹配ERP系统单品或者设置同步库存的策略时调用 注：仅支持自有/其他平台店铺 |
| 客户端路径 | 商品→创建平台货品 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=api_goodsspec_push_Y |

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

### JSON

```text
{
    "code": 0,
    "message": "OK",
    "new_count": 1,
    "chg_count": 0
}
```

### JSON

```text
{
    "code": 4304,
    "message": "shop_no 对应的店铺所属的平台 与 传入platform_id 不一致 "
}
```


### goods_push_Y：创建货品档案

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `goods_push_Y` |
| PHP 文件 | `goods_push.php` |
| 文档标题 | 创建货品档案 |
| 描述 | 在ERP内创建货品档案 |
| 客户端路径 | 商品→系统货品 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=goods_push_Y |

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

### JSON

```text
{"code":0,"message":"","errors":[]}
```


### suites_push_Y：创建组合装

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `suites_push_Y` |
| PHP 文件 | `suites_push.php` |
| 文档标题 | 创建组合装 |
| 描述 | 创建/更新组合装信息 |
| 客户端路径 | 商品→系统货品 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=suites_push_Y |

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

### JSON

```text
{
    "code": 0,
    "message": "",
    "new_count": 1,
    "chg_count": 0,
    "error_count": 0,
    "errors": [

    ]
}
```

### JSON

```text
{
    "code": 0,
    "message": "",
    "new_count": null,
    "chg_count": null,
    "error_count": null,
    "errors": [
        {
            "error": "suite_details 下的spec_no 不存在",
            "suite_no": "202260410-001"
        }
    ]
}
```


### suites_query_Y：查询组合装

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `suites_query_Y` |
| PHP 文件 | `suites_query.php` |
| 文档标题 | 查询组合装 |
| 描述 | 获取旺店通ERP中组合装界面的组合装资料 |
| 客户端路径 | 商品→系统货品 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=suites_query_Y |

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

### JSON

```text
{
    "code": "20",
    "message": "请求范围过宽，请增加请求参数条件过滤"
}
```


### goods_category_query_Y：查询货品分类

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `goods_category_query_Y` |
| PHP 文件 | `goods_category_query.php` |
| 文档标题 | 查询货品分类 |
| 描述 | 获取租户系统内全部货品分类的id、分类名词和分类的层级关系 |
| 客户端路径 | 商品→系统货品 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=goods_category_query_Y |

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

### JSON

```text
{
    "code": 200,
    "message": null,
    "goods_category_list": [
        {
            "id": "2788804529557078030",
            "category_name": "测试分类第一级",
            "children_list": [
                {
                    "id": "2788804569222610958",
                    "category_name": "分类二级",
                    "children_list": [
                        {
                            "id": "2788804604446375950",
                            "category_name": "分类三级",
                            "children_list": null
                        }
                    ]
                }
            ]
        }
    ]
}
```

### JSON

```text

```


### goods_category_flat_query_Y：查询货品分类平级

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `goods_category_flat_query_Y` |
| PHP 文件 | `` |
| 文档标题 |  |
| 描述 | 获取租户系统内全部货品分类的id、分类名词和分类的层级关系 |
| 客户端路径 | 商品→系统货品 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=goods_category_flat_query_Y |

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

### JSON

```text
{
    "code": 2220,
    "message": "page_size为正整数，请检查page_size是否为有效值"
}
```


### unique_code_print_Y：打印唯一码

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `unique_code_print_Y` |
| PHP 文件 | `unique_code_print.php` |
| 文档标题 | 打印唯一码 |
| 描述 |  |
| 客户端路径 | 档口→拿货标签管理 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=unique_code_print_Y |

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

### JSON

```text

```

### JSON

```text

```


### spec_barcode_push_Y：创建系统货品多条码

| 项目 | 内容 |
|---|---|
| 分类 | 货品类 |
| 服务名 | `spec_barcode_push_Y` |
| PHP 文件 | `spec_barcode_push.php` |
| 文档标题 | 创建、更新系统规格多条码 |
| 描述 | 在ERP内创建、更新系统规格多条码 |
| 客户端路径 | 商品→货品条码 |
| 文档 URL | https://open.wangdian.cn/Y/open/apidoc/doc?path=spec_barcode_push_Y |

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

### JSON

```text
{"code":0,"message":""}
```

### JSON

```text
{"code":2541,"message":"请检查参数是否正确：：条码不能为空、数量需要大于1"}
```


## 相关页面

- [[domains/ecommerce-ops/api/wangdian/index|旺店通开放平台 API 知识库]]
- [[domains/ecommerce-ops/api/wangdian/capability-map|旺店通 API 能力地图]]
- [[domains/ecommerce-ops/api/wangdian/skill-building-guide|旺店通 API Skill 创建指南]]
- [[queries/wangdian-api-skill-creation|旺店通 API Skill 创建查询入口]]
