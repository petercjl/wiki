---
title: 飞刀全批量修改（淘宝版）当前后台快照
type: source-summary
captured: 2026-08-11
url: http://39.101.142.186/shop
source_kind: dynamic-console
acquisition: user-authorized-CDP-and-static-frontend-inspection
---

# 飞刀全批量修改（淘宝版）当前后台快照

> 本快照来自 2026-08-11 的实际管理页面、只读网络观察与前端静态模块。已移除店铺名、店铺 ID、积分、到期日、授权码、回调凭证、短会话 Token、Cookie、IP 和商品明细。

## 当前可见一级能力

- 多店管理
- 自动补库存
- 自动同步
- 批量修改
- 批量导出

## 多店管理

当前页面提供店铺账号查询、添加店铺、修改备注和删除店铺；列表字段包含店铺账号、出售商品数、仓库商品数、剩余积分、剩余天数和备注。账号、数量、积分、期限属于私密和时效数据，未归档。

## 自动补库存

页面有“全店设置、选择商品设置、查看补库存记录”三部分。全店规则包括：

- SKU 库存低于阈值时增加指定数量；
- 始终固定每个 SKU 的库存；
- SKU 售罄时按规则补库存并上架；
- 延迟若干分钟后补库存；
- 低于指定阈值不再补库存；
- 全店、指定参与商品、指定不参与商品；
- 未付款订单取消后补回库存；
- 退款后补回库存并可在仓库时上架；
- 已发货订单不补回库存；
- 支持“恢复原样”。

页面将该能力描述为饥饿营销场景，但实际使用仍需同时考虑超卖、真实库存和履约风险。

## 自动同步

页面包含“同步商品属性、配置商品关联、自动同步记录”。当前确认：

- 明确选择源店铺与目标店铺；
- 可用商家编码、商品 ID 或标题关键词筛选；
- 支持添加关联、批量修改、批量删除；
- 关联表展示源/目标商品、库存、编码、同步属性和状态；
- 前端存在自动关联、方向查询/更新和自动同步日志接口。

当前页面没有显示“分销商模式/店群模式”切换，也没有把同步命名为“手动同步”；旧教程的模式与手动同步流程只能作为历史功能参考。

## 批量修改

当前可见字段：

- 商品：标题、库存、价格、商家编码、品牌；
- SKU：添加、删除、翻新、SKU 名称、搜索标题、搜索主图；
- 素材：1:1 视频、1:1 主图、3:4 主图；
- 其他：发货时效、运费模板、上架商品、下架商品、删除商品、店铺分类。

标题、库存、价格、商家编码、品牌页面都确认有“选择商品修改、上传文件修改、查看修改记录”；选择商品路径支持立即修改和定时修改。

通用筛选包括上架/更新日期范围、商品状态、一级类目、运费模板、店铺分类、价格、库存、销量、商家编码、商品 ID 和标题关键词。商家编码页面明确提示平台不支持清空编码，只能改成不再使用的其他字符。

## 批量导出

当前“导出商品”支持选择商品、使用与批量修改相近的筛选条件、立即导出和查看导出记录。

## 与视频教程的差异

2023-09 至 2026-06 视频中出现的分销商模式、店群模式、商品复制、手动同步、1688 选品铺货和货源关联，在 2026-08-11 当前新版可见菜单中均未出现。不能据此断言服务端永久删除；准确表述是“当前账号和当前新版页面未确认可用”，执行前应回旧版或咨询服务方。

## 认证与加密

- 业务请求统一发到 `/api`，请求体和响应均为 AES-CBC 加密。
- 前端使用名为 `token` 的 Cookie 维持会话，代码设置约 1 天有效期。
- 无 Cookie 的外部 `getprofile` 请求返回 `900005 会话失效`。
- 旧版页面的新版回调包含一段稳定的续期凭证；它在页面刷新后不变，并能在无浏览器 Cookie 的情况下签发 32 位短会话 Token。
- 续期凭证当前有效，但服务没有公开永久期限；可能受订购到期、解绑或服务端策略影响。
- 服务当前使用 HTTP 而非 HTTPS，续期凭证和短会话没有 HTTPS 传输保护。

## 前端接口清单

| unit_id | path | mode | evidence | disposition | notes |
| --- | --- | --- | --- | --- | --- |
| E001 | `/a/b` | unknown | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E002 | `/admin/changeid` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E003 | `/admin/listactiveshop` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E004 | `/admin/listrechargelog` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E005 | `/admin/login` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E006 | `/admin/recharge` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E007 | `/admin/sms` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E008 | `/admin9527/` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E009 | `/admin9527/changeid` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E010 | `/api/batch/log/export` | unknown | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E011 | `/batch/log/list` | unknown | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E012 | `/dict/listversion` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E013 | `/map/add` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E014 | `/map/automap` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E015 | `/map/batchremove` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E016 | `/map/batchupdate` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E017 | `/map/get` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E018 | `/map/getitem` | unknown | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E019 | `/map/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E020 | `/map/product/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E021 | `/map/status/update` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E022 | `/map/update` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E023 | `/publish/log/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E024 | `/publish/template/add` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E025 | `/publish/template/get` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E026 | `/publish/template/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E027 | `/publish/template/listallsimple` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E028 | `/publish/template/remove` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E029 | `/publish/template/update` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E030 | `/shop` | unknown | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E031 | `/shop/add` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E032 | `/shop/changemark` | write | 前端静态模块 | raw-only | 修改店铺标记；不进入通用调用 |
| E033 | `/shop/changeremark` | write | 前端静态模块 | raw-only | 修改店铺备注；不进入通用调用 |
| E034 | `/shop/getauthcode` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E035 | `/shop/getprofile` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E036 | `/shop/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E037 | `/shop/listall` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E038 | `/shop/listallsimple` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E039 | `/shop/logout` | restricted | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E040 | `/shop/remove` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E041 | `/sync/auto/log/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E042 | `/sync/direction/get` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E043 | `/sync/direction/update` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E044 | `/task/addbyfile` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E045 | `/task/addbypublishlog` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E046 | `/task/addbyselect` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E047 | `/task/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E048 | `/task/pause` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E049 | `/task/remove` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E050 | `/task/resume` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E051 | `/tool/brand/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E052 | `/tool/freight/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E053 | `/tool/picture/upload` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E054 | `/tool/product/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E055 | `/tool/product/refresh` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E056 | `/tool/product/refresh/count` | write | 前端静态模块 | raw-only | 不进入通用调用；仅作为能力/风险证据 |
| E057 | `/tool/productstatus/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E058 | `/tool/rootcat/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
| E059 | `/tool/shopcat/list` | read | 前端静态模块 | formalized | 列入当前只读接口清单 |
