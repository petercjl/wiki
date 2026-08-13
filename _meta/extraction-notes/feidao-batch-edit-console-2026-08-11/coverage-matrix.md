# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| U001 | 页面标题 | 产品身份 | identity | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前页面确认 |
| U002 | 当前菜单 | 一级能力 | capability-map | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/index.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前页面确认 |
| U003 | 多店管理页 | 多店管理 | workflow | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/01-模式选择与多店铺配置.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前页面确认 |
| U004 | 自动补库存页 | 自动补库存规则 | capability | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 视频知识缺口 |
| U005 | 自动同步页 | 自动同步 | workflow | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/04-手动同步与实时同步.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前页面确认 |
| U006 | 批量菜单 | 批量字段 | capability-map | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/02-批量修改与定时任务.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前页面确认 |
| U007 | 商品筛选器 | 筛选字段 | parameter-set | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/02-批量修改与定时任务.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前页面确认 |
| U008 | 批量修改页 | 输入与任务方式 | workflow | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/02-批量修改与定时任务.md | formalized | 当前页面确认 |
| U009 | 商家编码警告 | 编码不可清空 | limitation | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/02-批量修改与定时任务.md | formalized | 平台限制 |
| U010 | 批量导出页 | 批量导出 | workflow | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前页面确认 |
| U011 | 视频与当前菜单对照 | 历史能力当前不可见 | version-boundary | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/01-模式选择与多店铺配置.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/03-商品复制与防重复操作.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/04-手动同步与实时同步.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/05-1688铺货与货源关联.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/index.md | formalized | 保留历史，不静默覆盖 |
| U012 | 账号区和接口内容 | 私密和时效账号数据 | sensitive-ephemeral | — | omitted-with-reason | Cookie、token、pass、IP、店铺 ID、积分、期限和商品明细不归档 |
| U013 | 前端请求核心 | 加解密 | implementation-boundary | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前前端 |
| U014 | 前端 Cookie 设置 | 一天短会话 | auth-lifetime | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前前端 expires:1 |
| U015 | 旧版回调只读验证 | 续期凭证 | auth-refresh | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前有效，服务端期限未知 |
| U016 | 302 Location 结构 | 会话签发 | auth-session | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | merged | 并入认证流程 |
| U017 | 无 Cookie 探针 | 900005 | error-code | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 独立探针 |
| U018 | 页面和接口 URL | HTTP 风险 | security-risk | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 传输风险 |
| U019 | fdcli 测试 | fdcli 只读边界 | cli-safety | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/06-操作前检查与故障恢复.md; domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 用户明确只允许查看 |
| U020 | fdcli api list | 59 条路径 | api-inventory | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 当前前端快照 |
| E001 | 前端模块静态字符串 | `/a/b` | API endpoint (unknown) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | unresolved | 端点语义未确认，保持 unresolved |
| E002 | 前端模块静态字符串 | `/admin/changeid` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E003 | 前端模块静态字符串 | `/admin/listactiveshop` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E004 | 前端模块静态字符串 | `/admin/listrechargelog` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E005 | 前端模块静态字符串 | `/admin/login` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E006 | 前端模块静态字符串 | `/admin/recharge` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E007 | 前端模块静态字符串 | `/admin/sms` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E008 | 前端模块静态字符串 | `/admin9527/` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E009 | 前端模块静态字符串 | `/admin9527/changeid` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E010 | 前端模块静态字符串 | `/api/batch/log/export` | API endpoint (unknown) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | unresolved | 端点语义未确认，保持 unresolved |
| E011 | 前端模块静态字符串 | `/batch/log/list` | API endpoint (unknown) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | unresolved | 端点语义未确认，保持 unresolved |
| E012 | 前端模块静态字符串 | `/dict/listversion` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E013 | 前端模块静态字符串 | `/map/add` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E014 | 前端模块静态字符串 | `/map/automap` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E015 | 前端模块静态字符串 | `/map/batchremove` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E016 | 前端模块静态字符串 | `/map/batchupdate` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E017 | 前端模块静态字符串 | `/map/get` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E018 | 前端模块静态字符串 | `/map/getitem` | API endpoint (unknown) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | unresolved | 端点语义未确认，保持 unresolved |
| E019 | 前端模块静态字符串 | `/map/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E020 | 前端模块静态字符串 | `/map/product/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E021 | 前端模块静态字符串 | `/map/status/update` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E022 | 前端模块静态字符串 | `/map/update` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E023 | 前端模块静态字符串 | `/publish/log/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E024 | 前端模块静态字符串 | `/publish/template/add` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E025 | 前端模块静态字符串 | `/publish/template/get` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E026 | 前端模块静态字符串 | `/publish/template/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E027 | 前端模块静态字符串 | `/publish/template/listallsimple` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E028 | 前端模块静态字符串 | `/publish/template/remove` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E029 | 前端模块静态字符串 | `/publish/template/update` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E030 | 前端模块静态字符串 | `/shop` | API endpoint (unknown) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | unresolved | 端点语义未确认，保持 unresolved |
| E031 | 前端模块静态字符串 | `/shop/add` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E032 | 前端模块静态字符串 | `/shop/changemark` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 修改店铺标记，属于写入接口，不开放 CLI 调用 |
| E033 | 前端模块静态字符串 | `/shop/changeremark` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 修改店铺备注，属于写入接口，不开放 CLI 调用 |
| E034 | 前端模块静态字符串 | `/shop/getauthcode` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E035 | 前端模块静态字符串 | `/shop/getprofile` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E036 | 前端模块静态字符串 | `/shop/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E037 | 前端模块静态字符串 | `/shop/listall` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E038 | 前端模块静态字符串 | `/shop/listallsimple` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E039 | 前端模块静态字符串 | `/shop/logout` | API endpoint (restricted) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E040 | 前端模块静态字符串 | `/shop/remove` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E041 | 前端模块静态字符串 | `/sync/auto/log/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E042 | 前端模块静态字符串 | `/sync/direction/get` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E043 | 前端模块静态字符串 | `/sync/direction/update` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E044 | 前端模块静态字符串 | `/task/addbyfile` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E045 | 前端模块静态字符串 | `/task/addbypublishlog` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E046 | 前端模块静态字符串 | `/task/addbyselect` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E047 | 前端模块静态字符串 | `/task/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E048 | 前端模块静态字符串 | `/task/pause` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E049 | 前端模块静态字符串 | `/task/remove` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E050 | 前端模块静态字符串 | `/task/resume` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E051 | 前端模块静态字符串 | `/tool/brand/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E052 | 前端模块静态字符串 | `/tool/freight/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E053 | 前端模块静态字符串 | `/tool/picture/upload` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E054 | 前端模块静态字符串 | `/tool/product/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E055 | 前端模块静态字符串 | `/tool/product/refresh` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E056 | 前端模块静态字符串 | `/tool/product/refresh/count` | API endpoint (write) | raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md | raw-only | 写入、管理或敏感接口仅保留证据，不开放 CLI 调用 |
| E057 | 前端模块静态字符串 | `/tool/productstatus/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E058 | 前端模块静态字符串 | `/tool/rootcat/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
| E059 | 前端模块静态字符串 | `/tool/shopcat/list` | API endpoint (read) | domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI.md | formalized | 列入 07 的只读接口清单 |
