# Knowledge Unit Inventory

| unit_id | source | knowledge unit | role |
| --- | --- | --- | --- |
| K01 | C05 | 分销商模式适合店铺各自管理、各自登录，但需要跨主体复制或同步数据 | decision rule |
| K02 | C05 | 店群模式适合一个操作者管理主店和多个分店，后续主要由主店账号操作 | decision rule |
| K03 | C06 | 建店群必须先由主店创建并邀请分店，分店账号确认加入后主店才能操作其数据 | prerequisite workflow |
| K04 | C03 | 普通多店管理通过其他店铺授权码添加，支持分组和备注 | setup workflow |
| K05 | C01/C02 | 批量修改支持按查询结果或已选商品执行，另有文件模板上传路径 | capability map |
| K06 | C01/C02 | 批量修改可立即执行或定时执行；高精度定时应优先走选择商品路径（2025-05说法） | operation rule |
| K07 | C01 | 定时任务可成对设置添加/删除关键词，任务按执行时间排列 | case + scheduling pattern |
| K08 | C02 | 文件修改需下载模板、按格式填写后上传，并在记录中查看详情 | workflow |
| K09 | C02 | 新版视频展示一键恢复修改前内容，但该功能需按当前版本复核 | recovery boundary |
| K10 | C04 | 普通跨店复制先建复制模板，再筛选源店商品、核对数量、选择目标店与模板 | workflow |
| K11 | C04 | 目标列表会包含源店，源店不需要复制时不要勾选 | failure prevention |
| K12 | C04/C08 | 复制标记或“是否已复制”筛选可避免重复复制 | deduplication rule |
| K13 | C07/C08 | 分销商复制从上级授权商品中选品；店群复制由主店选择任一源店和目标分店 | mode comparison |
| K14 | C07/C08 | 复制任务是后台离线任务，关闭浏览器不影响执行 | operational fact |
| K15 | C07/C08 | 复制完成后可按任务 ID 查看记录；失败记录可筛选并重新复制 | troubleshooting |
| K16 | C09/C10 | 手动同步用于把图片、SKU、价格、描述等已变化字段同步到对应商品 | definition |
| K17 | C09/C10 | 手动同步规则可按唯一商家编码绑定，或复用实时同步中已建立的关联 | binding decision |
| K18 | C09/C10 | 同步规则可选择字段，且可选择在手动同步后建立持续实时同步关系 | configuration rule |
| K19 | C09/C10 | 手动同步支持立即或定时任务，未开始任务可撤销，失败记录可重新同步 | lifecycle + recovery |
| K20 | C11/C12 | 实时同步前需要建立源商品与目标商品的一对一关联 | prerequisite |
| K21 | C11/C12 | 自动关联依赖商品编码或标题；不一致时必须手动关联 | matching decision |
| K22 | C11/C12/C14 | SKU 对应可自动匹配，也可拖拽或输入序号手工建立 | mapping workflow |
| K23 | C11/C12 | 关联规则可启用/禁用、批量删除、批量修改同步字段 | maintenance workflow |
| K24 | C11 | 分销商模式实时同步为上级到下级的单向同步 | hard boundary |
| K25 | C12 | 店群模式可按主店→分店单向同步，也可切换双向同步 | hard boundary |
| K26 | C11/C12 | 同步记录可按状态、商品 ID、备注等查询，用于排错 | troubleshooting |
| K27 | C13 | 1688 铺货先建模板，可按统一倍率或价格区间设置倍率 | pricing workflow |
| K28 | C13 | 铺货有关键词选品、图搜同款、1688 商品链接三条路径 | capability map |
| K29 | C13 | 提交铺货任务后在铺货记录中查看任务 | workflow |
| K30 | C14 | 软件铺货商品通常自动关联货源；非自动关联时可手动添加货源 | source-linking rule |
| K31 | C14 | 一个商品可关联多个货源，SKU 未自动对应时需手动拖拽 | sourcing workflow |
| K32 | C14 | 可输入专属货源链接再进行关联 | branch |
| K33 | all | 视频跨越 2023-2026，菜单、功能数量和字段集合存在版本差异 | time-sensitivity |
| K34 | all | 任何复制、同步、批量修改前都应先确认源/目标方向、商品范围、规则和可恢复性 | synthesized safety checklist |

