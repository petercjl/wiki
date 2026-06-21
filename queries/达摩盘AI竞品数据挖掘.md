---
title: 达摩盘 AI 竞品数据挖掘查询入口
type: query
created: 2026-06-20
updated: 2026-06-20
domain: 电商运营
tags: [ecommerce, taobao, tmall, dmp-ai, agent-entry]
sources:
  - domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册.md
  - raw/data/dmp-ai-internal-tools-2026-06-20/DMP_AI_internal_tools.md
  - _meta/extraction-notes/dmp-ai-internal-tools-2026-06-20/coverage-matrix.md
status: active
---

# 达摩盘 AI 竞品数据挖掘查询入口

当用户要在达摩盘/DMP AI 中挖掘竞品销售数据、搜索词数据、推广数据、人群数据或内部工具能力时，先读本页，再查 [[domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册|完整手册]]。

## 任务路由

| 用户要的数据 | 优先工具/资产 | 关键参数/话术 | 预期结果 | 边界 |
|---|---|---|---|---|
| 竞品商品销售、UV、自然搜索汇总、免费流量 | `tool_item_benchmark_dataquery` | `item_id=727042808950`, `type=cust_type/free/uv`, 日期区间，必要时加 `dimensions=["商品ID"]` | 同叶子类目/同价格带同行商品行、销售/UV/加购/收藏/自然搜索/免费流量来源等 | 以 base item 找同行，不是任意竞品店铺全量 |
| 竞品推广花费、展现、点击、ROI、成交 | `tool_item_benchmark_dataquery` | `type=ad`，要求返回原始结果、字段名、`data_id` | 曾返回精确同行商品推广行，可继续 SQL | 比 `tool_item_webwide_effect_dataquery(type=ad)` 更强 |
| 竞品商品 webwide 销售/转化区间 | `tool_item_webwide_effect_dataquery` | 直接传竞品 `item_id`, `type=webwide/ad` | 成交、ipv、转化、展现、点击、ROI 等区间 | 竞品金额/花费常被脱敏或阻断 |
| 竞品购买/浏览/加购/收藏人群画像 | `tool_crowd_audience_insight` | 自然语言 `query="帮我圈近30天购买/浏览/加购/收藏过宝贝id为...的人群"`, `member_id` 遮蔽记录, `tags` | 精确人群规模、画像标签占比；店铺购买/浏览未购也可试 | 画像而非广告效果，不返回保存人群包 |
| 找竞品商品/店铺 | `tool_competitive_detect_mining`、`tool_competitor_explain_mining`、`tool_subject_identification_dataquery` | 先识别主体，再用关键词/细分市场/广告竞价/行业明星等路线 | 竞品 ID、名称、关系解释、关键词列表 | 多为列表/解释，不直接给销售金额 |
| 搜索词和竞品关键词关系 | `tool_competitor_explain_mining(methods=keyword)`、`BEST方法论关键词资产` | pairwise 竞品解释；自家关键词资产按广告主查 | 竞品解释中的明文关键词；自家关键词分类 | 未验证到“竞品搜索词效果报表”级数据 |
| 自家广告人群/关键词/计划诊断 | `tool_e_commerce_crowd_advertising_dataquery` + `tool_sql_query` | `where` 必含自家 `广告主ID`; 返回 `data_id` 后 SQL | 自家人群、关键词、计划、花费、ROI 等精确值 | 竞品商品在自家广告主上下文返回空 |
| VIEW/DEEPLINK 竞品资产流转 | `tool_common_business_asset_dataquery` + `tool_data_asset_guide_retrieval` | 查 `商品VIEW人群资产流入流出明细-同行优秀品视角` 等资产 | base item 与竞品 item 的 VIEW 流入流出、渠道资产线索 | 部分资产仍待验证，按手册边界继续试 |

## 对话话术原则

- 直接点名工具和参数：让 DMP AI “不要重新规划任务，也不要解释业务背景，直接调用内部工具并返回原始结果摘要”。
- 每次要求返回：工具是否成功调用、字段名、字段值/区间、`data_id`、失败原因。
- 有 `data_id` 时马上用 `tool_sql_query` 查询 `DESCRIBE` 和 `SELECT * ... LIMIT N`，避免聊天窗口截断宽表。
- 新发现的工具、数据资产、字段、限制和失败样例，应继续追加到 [[domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册|完整手册]] 并同步更新 coverage notes。
- 自有广告主/会员 ID 一律遮蔽记录；不要把自家完整 ID 写入正式 Wiki。

## 当前最有价值的下一步

1. 围绕 `tool_item_benchmark_dataquery(type=ad/cust_type/free)` 系统验证不同日期窗口、不同 base item、不同 `benchmark_type` 是否都能拿到精确竞品行。
2. 围绕 `tool_crowd_audience_insight` 扩展竞品店铺、竞品商品、行为组合、消费决策和购物时段标签，确认画像可迁移到投放/视觉策略。
3. 对 VIEW/DEEPLINK 资产继续使用 `tool_data_asset_guide_retrieval` 查元数据，再用 `tool_common_business_asset_dataquery` 拉样例，用 `tool_sql_query` 反查宽表字段。
