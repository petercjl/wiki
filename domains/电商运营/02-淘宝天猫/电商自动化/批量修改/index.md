---
title: 淘宝批量修改、商品复制与店群同步
type: source-summary
created: 2026-08-11
updated: 2026-08-11
domain: 电商运营
tags: [ecommerce, taobao, automation, playbook]
sources:
  - raw/videos/taobao-batch-modification-help-videos/
  - raw/transcripts/taobao-batch-modification-help-videos/
  - _meta/extraction-notes/taobao-batch-modification-help-videos/coverage-matrix.md
  - raw/webpages/taobao/feidao-batch-edit-console-2026-08-11.md
  - _meta/extraction-notes/feidao-batch-edit-console-2026-08-11/coverage-matrix.md
status: active
---

# 淘宝批量修改、商品复制与店群同步

这套知识用于理解和安全使用“飞刀全批量修改（淘宝版）”。2026-08-11 当前新版确认多店管理、自动补库存、自动同步、批量修改和批量导出；视频中的模式、商品复制、手动同步和 1688 铺货保留为历史能力，不再默认视为新版现行入口。

## 推荐阅读顺序

1. [[domains/电商运营/02-淘宝天猫/电商自动化/批量修改/07-飞刀新版后台能力与只读CLI|飞刀新版后台能力与只读 CLI]]
2. [[domains/电商运营/02-淘宝天猫/电商自动化/批量修改/02-批量修改与定时任务|批量修改与定时任务]]
3. [[domains/电商运营/02-淘宝天猫/电商自动化/批量修改/04-手动同步与实时同步|手动同步与实时同步]]
4. [[domains/电商运营/02-淘宝天猫/电商自动化/批量修改/06-操作前检查与故障恢复|操作前检查与故障恢复]]
5. 历史能力：[[domains/电商运营/02-淘宝天猫/电商自动化/批量修改/01-模式选择与多店铺配置|模式选择与多店铺配置]]、[[domains/电商运营/02-淘宝天猫/电商自动化/批量修改/03-商品复制与防重复操作|商品复制与防重复操作]]、[[domains/电商运营/02-淘宝天猫/电商自动化/批量修改/05-1688铺货与货源关联|1688 铺货与货源关联]]。

## 快速路由

| 任务 | 先读 |
| --- | --- |
| 先确认新版当前能做什么、CLI 能查什么 | 07 |
| 自动补库存、撤单/退款补回 | 07 + 06 |
| 不知道选分销商还是店群模式 | 01 |
| 大批量改标题、价格、库存或定时改回 | 02 + 06 |
| 从一个店复制到另一个店 | 03 + 06 |
| 商品已经对应，需要同步字段变化 | 04 + 06 |
| 从 1688 选品、铺货或关联供货链接 | 05 + 06 |
| 任务失败、重复复制、同步方向不对 | 06，再回到对应任务页 |

## 时间边界

来源视频发布于 2023-09 至 2026-06；新版页面快照采集于 2026-08-11。精确菜单、套餐、分页、字段和认证策略仍会变化，应优先读 07，再以当前后台复核。
