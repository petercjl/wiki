# Source Inventory

| source_unit_id | source_location | source_unit | knowledge_role | disposition | reason_or_target |
| --- | --- | --- | --- | --- | --- |
| U001 | 页面标题 | 产品名为“飞刀全批量修改（淘宝版）” | identity | formalized | 07 |
| U002 | 当前菜单 | 多店管理、自动补库存、自动同步、批量修改、批量导出 | capability-map | formalized | index、07 |
| U003 | 多店管理页 | 查询、添加、改备注、删除店铺 | workflow | formalized | 01、07 |
| U004 | 自动补库存页 | 全店/商品/记录及完整规则 | capability | formalized | 07 |
| U005 | 自动同步页 | 源/目标、商品关联、属性和日志 | workflow | formalized | 04、07 |
| U006 | 批量菜单 | 当前批量修改字段清单 | capability-map | formalized | 02、07 |
| U007 | 商品筛选器 | 当前批量筛选字段清单 | parameter-set | formalized | 02、07 |
| U008 | 批量修改页 | 选择商品、上传文件、记录、立即/定时 | workflow | formalized | 02 |
| U009 | 商家编码警告 | 商家编码不能清空 | limitation | formalized | 02 |
| U010 | 批量导出页 | 筛选、导出和记录 | workflow | formalized | 07 |
| U011 | 视频与当前菜单对照 | 模式、复制、手动同步、1688 当前不可见 | version-boundary | formalized | 01、03、04、05、index |
| U012 | 账号区和接口内容 | 账号、积分、期限、店铺 ID、商品明细 | sensitive-ephemeral | omitted-with-reason | 私密且时效，不归档 |
| U013 | 前端请求核心 | API 使用 AES-CBC | implementation-boundary | formalized | 07 |
| U014 | 前端 Cookie 设置 | token Cookie 约 1 天 | auth-lifetime | formalized | 07 |
| U015 | 旧版回调只读验证 | 续期凭证刷新后稳定，可签发短会话 | auth-refresh | formalized | 07 |
| U016 | 302 Location 结构 | 32 位短会话 Token | auth-session | merged | 并入 07 认证流程 |
| U017 | 无 Cookie 探针 | 900005 会话失效 | error-code | formalized | 07 |
| U018 | 页面和接口 URL | 服务使用 HTTP | security-risk | formalized | 07 |
| U019 | fdcli 测试 | 查询白名单并阻止 refresh=true | cli-safety | formalized | 06、07 |
| U020 | fdcli api list | 当前静态发现 59 条路径 | api-inventory | formalized | 07 + 本清单 |
| E001 | 前端模块静态字符串 | `/a/b` | API endpoint (unknown) | unresolved | 端点语义未确认，不调用 |
| E002 | 前端模块静态字符串 | `/admin/changeid` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E003 | 前端模块静态字符串 | `/admin/listactiveshop` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E004 | 前端模块静态字符串 | `/admin/listrechargelog` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E005 | 前端模块静态字符串 | `/admin/login` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E006 | 前端模块静态字符串 | `/admin/recharge` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E007 | 前端模块静态字符串 | `/admin/sms` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E008 | 前端模块静态字符串 | `/admin9527/` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E009 | 前端模块静态字符串 | `/admin9527/changeid` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E010 | 前端模块静态字符串 | `/api/batch/log/export` | API endpoint (unknown) | unresolved | 端点语义未确认，不调用 |
| E011 | 前端模块静态字符串 | `/batch/log/list` | API endpoint (unknown) | unresolved | 端点语义未确认，不调用 |
| E012 | 前端模块静态字符串 | `/dict/listversion` | API endpoint (read) | formalized | 进入只读目录 |
| E013 | 前端模块静态字符串 | `/map/add` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E014 | 前端模块静态字符串 | `/map/automap` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E015 | 前端模块静态字符串 | `/map/batchremove` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E016 | 前端模块静态字符串 | `/map/batchupdate` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E017 | 前端模块静态字符串 | `/map/get` | API endpoint (read) | formalized | 进入只读目录 |
| E018 | 前端模块静态字符串 | `/map/getitem` | API endpoint (unknown) | unresolved | 端点语义未确认，不调用 |
| E019 | 前端模块静态字符串 | `/map/list` | API endpoint (read) | formalized | 进入只读目录 |
| E020 | 前端模块静态字符串 | `/map/product/list` | API endpoint (read) | formalized | 进入只读目录 |
| E021 | 前端模块静态字符串 | `/map/status/update` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E022 | 前端模块静态字符串 | `/map/update` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E023 | 前端模块静态字符串 | `/publish/log/list` | API endpoint (read) | formalized | 进入只读目录 |
| E024 | 前端模块静态字符串 | `/publish/template/add` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E025 | 前端模块静态字符串 | `/publish/template/get` | API endpoint (read) | formalized | 进入只读目录 |
| E026 | 前端模块静态字符串 | `/publish/template/list` | API endpoint (read) | formalized | 进入只读目录 |
| E027 | 前端模块静态字符串 | `/publish/template/listallsimple` | API endpoint (read) | formalized | 进入只读目录 |
| E028 | 前端模块静态字符串 | `/publish/template/remove` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E029 | 前端模块静态字符串 | `/publish/template/update` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E030 | 前端模块静态字符串 | `/shop` | API endpoint (unknown) | unresolved | 端点语义未确认，不调用 |
| E031 | 前端模块静态字符串 | `/shop/add` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E032 | 前端模块静态字符串 | `/shop/changemark` | API endpoint (write) | raw-only | 修改店铺标记，不调用 |
| E033 | 前端模块静态字符串 | `/shop/changeremark` | API endpoint (write) | raw-only | 修改店铺备注，不调用 |
| E034 | 前端模块静态字符串 | `/shop/getauthcode` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E035 | 前端模块静态字符串 | `/shop/getprofile` | API endpoint (read) | formalized | 进入只读目录 |
| E036 | 前端模块静态字符串 | `/shop/list` | API endpoint (read) | formalized | 进入只读目录 |
| E037 | 前端模块静态字符串 | `/shop/listall` | API endpoint (read) | formalized | 进入只读目录 |
| E038 | 前端模块静态字符串 | `/shop/listallsimple` | API endpoint (read) | formalized | 进入只读目录 |
| E039 | 前端模块静态字符串 | `/shop/logout` | API endpoint (restricted) | raw-only | 不开放 CLI 调用 |
| E040 | 前端模块静态字符串 | `/shop/remove` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E041 | 前端模块静态字符串 | `/sync/auto/log/list` | API endpoint (read) | formalized | 进入只读目录 |
| E042 | 前端模块静态字符串 | `/sync/direction/get` | API endpoint (read) | formalized | 进入只读目录 |
| E043 | 前端模块静态字符串 | `/sync/direction/update` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E044 | 前端模块静态字符串 | `/task/addbyfile` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E045 | 前端模块静态字符串 | `/task/addbypublishlog` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E046 | 前端模块静态字符串 | `/task/addbyselect` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E047 | 前端模块静态字符串 | `/task/list` | API endpoint (read) | formalized | 进入只读目录 |
| E048 | 前端模块静态字符串 | `/task/pause` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E049 | 前端模块静态字符串 | `/task/remove` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E050 | 前端模块静态字符串 | `/task/resume` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E051 | 前端模块静态字符串 | `/tool/brand/list` | API endpoint (read) | formalized | 进入只读目录 |
| E052 | 前端模块静态字符串 | `/tool/freight/list` | API endpoint (read) | formalized | 进入只读目录 |
| E053 | 前端模块静态字符串 | `/tool/picture/upload` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E054 | 前端模块静态字符串 | `/tool/product/list` | API endpoint (read) | formalized | 进入只读目录 |
| E055 | 前端模块静态字符串 | `/tool/product/refresh` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E056 | 前端模块静态字符串 | `/tool/product/refresh/count` | API endpoint (write) | raw-only | 不开放 CLI 调用 |
| E057 | 前端模块静态字符串 | `/tool/productstatus/list` | API endpoint (read) | formalized | 进入只读目录 |
| E058 | 前端模块静态字符串 | `/tool/rootcat/list` | API endpoint (read) | formalized | 进入只读目录 |
| E059 | 前端模块静态字符串 | `/tool/shopcat/list` | API endpoint (read) | formalized | 进入只读目录 |
