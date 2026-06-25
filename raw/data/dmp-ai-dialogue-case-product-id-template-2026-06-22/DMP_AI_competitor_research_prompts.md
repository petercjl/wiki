# DMP AI Competitor Research Prompts

本文件用于在达摩盘 / DMP AI 对话窗口中测试竞品研究流程。目标是围绕一个自己的商品 ID，分两步完成：

1. 找出可研究的竞品候选，并拿到竞品基本信息。
2. 对选定竞品尽可能抽取销售、搜索词、推广、人群、VIEW/DEEPLINK 等数据。

使用时先替换变量。提示词里的 `{...}` 是占位符，不是要原样发送给 DMP AI 的内容；复制到 DMP AI 前，要把整段占位符替换成真实值，并删除花括号。正式知识库只保留模板变量，不记录真实本品商品 ID 或完整会员 ID。

| Variable | Meaning | Replacement note |
|---|---|---|
| `{BASE_ITEM_ID}` | 自己的商品 ID | 替换成要研究的本品商品 ID，例如把 `query={BASE_ITEM_ID}` 改成 `query=你的本品商品ID`。 |
| `{COMP_ITEM_ID}` | 选中的竞品商品 ID | 替换成已选中的竞品商品 ID。 |
| `{COMP_SHOP_NAME}` | 竞品店铺名 | 替换成竞品店铺名。 |
| `{START_DATE}` | 起始日期，格式 `YYYYMMDD` | 替换成查询开始日期。 |
| `{END_DATE}` | 结束日期，格式 `YYYYMMDD` | 替换成查询结束日期。 |
| `{LOOKBACK_DAYS}` | 回溯天数 | 替换成数字，例如 `30`。 |
| `{MEMBER_ID_MASKED}` | 当前广告主/会员 ID，记录时遮蔽 | 只写遮蔽值，不记录完整会员 ID。 |
| `{DATA_ID}` | DMP AI 返回的数据集编号 | 替换成上一步工具返回的真实 `data_id`。 |

## 总体对话规则

每次复制提示词时，都尽量保留下面这段约束，避免 DMP AI 重新规划或只给解释：

```text
请不要重新规划任务，也不要解释业务背景。请按我给出的工具名和参数直接调用内部工具。

输出必须包含：
1. 实际调用的工具名。
2. 实际传入的参数。
3. 工具是否成功调用。
4. 返回字段名。
5. 返回字段值、区间或样例行。
6. 如果有 data_id，请原样返回 data_id。
7. 如果失败、为空或被安全策略限制，请输出失败原因和限制原因。

不要只输出分析结论，不要省略原始字段。
```

## Phase 1: 找竞品与基本信息

### 1.1 识别自己的商品主体

目的：确认 `{BASE_ITEM_ID}` 在 DMP AI 内部能被识别，并返回商品/店铺/类目等基础实体信息。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_subject_identification_dataquery
参数：
query={BASE_ITEM_ID}
entityList=["item","shop","member","category"]

只输出：
1. 工具是否成功调用。
2. 返回的商品ID、商品名称、店铺ID、店铺名称、广告主/会员ID、叶子类目ID、叶子类目名称。
3. 如果有多个匹配，请用表格列出。
4. 失败原因。
```

### 1.2 从四个角度挖竞品候选

目的：用 `tool_competitive_detect_mining` 获取候选竞品池。四个角度分别是细分市场、关键词、广告竞价、行业明星。

分别复制以下 4 次，把 `mining_type` 替换为：

- `细分市场`
- `关键词`
- `广告竞价`
- `行业明星`

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_competitive_detect_mining
参数：
subject_dimension=商品
subject_id={BASE_ITEM_ID}
mining_type={MINING_TYPE}

只输出：
1. 工具是否成功调用。
2. mining_type。
3. 返回字段名。
4. 前 20 个竞品候选，字段至少包括：item_id、item_name、shop_name、score、type、命中原因。
5. 如果返回 data_id，请返回 data_id。
6. 失败原因或限制原因。
```

### 1.3 从生意流入/流出角度挖竞品

目的：补充业务流向型竞品。这个工具的复杂 nested config 曾经序列化失败，所以先用默认配置。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_competitor_mining_busi_flow
参数：
biz=item
entity_type=item
entity_id={BASE_ITEM_ID}

请不要传 nested object 参数，使用默认配置。

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 前 20 个竞品候选，字段至少包括：id、name、item_id、item_name、shop_name。
4. 是否返回流入/流出数量或金额。
5. 如果没有流量数值，请明确说明。
6. 失败原因。
```

### 1.4 用 benchmark peer 反查同行商品候选

目的：`tool_item_benchmark_dataquery` 经常能返回同叶子类目/同价格带同行商品 ID，是选竞品的强路线。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_item_benchmark_dataquery
参数：
item_id={BASE_ITEM_ID}
start_date={START_DATE}
end_date={END_DATE}
type=ad
benchmark_type=同叶子类目同价格带top5均值
dimensions=["商品ID","商品名称"]

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 所有同行商品行，字段至少包括：商品ID、商品名称、展现量、点击量、花费、ROI、引导成交金额、引导成交笔数。
4. 如果返回 data_id，请返回 data_id。
5. 失败原因或限制原因。
```

### 1.5 对候选竞品做关系验证

目的：从候选池中挑 3-5 个候选，用 `tool_competitor_explain_mining` 验证竞争关系、关键词重合、流入流出、细分市场、明星/竞价等命中路径。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_competitor_explain_mining
参数：
entity_type=item
entity_id={BASE_ITEM_ID}
competitor_id={COMP_ITEM_ID}
methods=keyword,busi_outflow,busi_inflow,niche,star,bidding
lookback_days={LOOKBACK_DAYS}
llm_polish=false

只输出：
1. 工具是否成功调用。
2. is_competitor。
3. confidence。
4. hit_methods。
5. 每个 method 的原始解释、命中关键词、流量/GMV区间、竞价/行业明星证据。
6. 返回字段名。
7. 如果返回 data_id，请返回 data_id。
8. 失败原因或限制原因。
```

### 1.6 Phase 1 汇总输出要求

当多个候选工具都跑完后，让 DMP AI 汇总一个竞品候选表：

```text
请基于本轮对话中已经调用过的工具结果，不要重新编造数据，不要补充未调用来源。

请输出竞品候选表，字段包括：
1. rank
2. item_id
3. item_name
4. shop_name
5. 来源工具：competitive_detect / busi_flow / benchmark_peer / explain
6. 命中路径：细分市场 / 关键词 / 广告竞价 / 行业明星 / 生意流入 / 生意流出 / 同叶子类目同价格带
7. score 或 confidence
8. 已知销售/推广/人群线索
9. 是否建议进入 Phase 2 深挖
10. 建议原因

最后给出你建议优先深挖的 3 个竞品商品 ID。
```

## Phase 2: 选中竞品后的全量数据挖掘

### 2.1 竞品商品基础销售与转化区间

目的：用直接竞品 item 查询拿 webwide 销售/转化区间。此路线常有脱敏，但适合做底层规模判断。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_item_webwide_effect_dataquery
参数：
item_id={COMP_ITEM_ID}
start_date={START_DATE}
end_date={END_DATE}
type=webwide

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 字段值或区间，至少包括：成交金额、成交笔数、成交件数、ipv、支付转化率、加购数、收藏数、加购率、笔单价、件单价。
4. 是否脱敏。
5. 失败原因或限制原因。
```

### 2.2 竞品推广区间：直接 item ad 查询

目的：直接查竞品广告曝光、点击、ROI 区间。花费/成交可能被安全策略阻断。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_item_webwide_effect_dataquery
参数：
item_id={COMP_ITEM_ID}
start_date={START_DATE}
end_date={END_DATE}
type=ad

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 展现量、点击量、点击率、ROI、引导成交金额、引导成交笔数、花费。
4. 哪些字段被安全策略限制。
5. 失败原因。
```

### 2.3 竞品精确推广/销售：benchmark ad

目的：目前知识库中最强路线。不要直接传竞品商品作为 base，而是用自己的 `{BASE_ITEM_ID}` 触发同行 TOP 商品表，再在返回行中找 `{COMP_ITEM_ID}`。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_item_benchmark_dataquery
参数：
item_id={BASE_ITEM_ID}
start_date={START_DATE}
end_date={END_DATE}
type=ad
benchmark_type=同叶子类目同价格带top5均值
dimensions=["商品ID","商品名称"]

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 所有包含商品ID的同行商品行。
4. 请特别标出商品ID={COMP_ITEM_ID} 的行。
5. 字段至少包括：商品ID、商品名称、展现量、点击量、点击率、花费、ROI、引导成交金额、引导成交笔数、CPC、CPM、成交成本、收藏加购成本。
6. 如果返回 data_id，请返回 data_id。
7. 失败原因。
```

如果返回了 `data_id`，立刻追问：

```text
请不要重新规划任务。请直接调用内部工具：

工具：tool_sql_query
参数：
sql=
SELECT *
FROM {DATA_ID}
WHERE 商品ID = '{COMP_ITEM_ID}'
LIMIT 20
description=从 benchmark ad 返回表中筛选指定竞品商品的完整推广行

只输出：
1. SQL 是否执行成功。
2. 返回字段名。
3. 返回的完整行。
4. 如果没有命中，请说明原因，并执行 SELECT * FROM {DATA_ID} LIMIT 20 返回样例行。
```

### 2.4 竞品精确销售/UV/自然搜索：benchmark cust_type 或 uv

目的：拉同行商品销售、UV、加购、收藏、自然搜索汇总等。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_item_benchmark_dataquery
参数：
item_id={BASE_ITEM_ID}
start_date={START_DATE}
end_date={END_DATE}
type=cust_type
benchmark_type=同叶子类目同价格带top5均值
dimensions=["商品ID","商品名称"]

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 所有包含商品ID的同行商品行。
4. 请特别标出商品ID={COMP_ITEM_ID} 的行。
5. 字段至少包括：销售金额、UV、加购、收藏、自然搜索相关指标、成交笔数、成交件数、转化率。
6. 如果返回 data_id，请返回 data_id。
7. 失败原因。
```

### 2.5 竞品免费流量来源/场景：benchmark free

目的：看竞品自然/免费流量结构，比如淘宝搜索、淘宝推荐、淘宝私域等。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_item_benchmark_dataquery
参数：
item_id={BASE_ITEM_ID}
start_date={START_DATE}
end_date={END_DATE}
type=free
benchmark_type=同叶子类目同价格带top5均值
dimensions=["商品ID","商品名称","流量来源"]

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 商品ID={COMP_ITEM_ID} 的所有免费流量来源/场景行。
4. 字段至少包括：流量来源、销售金额、访客数、成交笔数、加购、收藏、支付转化率。
5. 如果返回 data_id，请返回 data_id。
6. 失败原因。
```

### 2.6 竞品增长路径与投放打法

目的：拿竞品阶段性策略，不一定有数值，但能看到关键词/人群比例、目标、出价、辅助活动。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_item_success_path_mining
参数：
item_id={COMP_ITEM_ID}

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 每个阶段的 period、growth_stage、strategy summary。
4. 是否出现关键词/人群预算比例、推广目标、出价模式、控成本方式、活动工具、评价/买家秀/直播/关联宝贝等打法。
5. 失败原因。
```

### 2.7 竞品购买人群画像：完整标签

目的：用 `tool_crowd_audience_insight` 拉竞品购买人群画像。这个路线曾返回精确人数和比例。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_crowd_audience_insight
参数：
query=帮我圈近30天宝贝id为{COMP_ITEM_ID}的购买人群
member_id={MEMBER_ID_MASKED}
tags=["用户性别","用户年龄","城市等级","消费能力等级","月均消费金额","月均消费频次","消费决策导向","历史大促高活人群","最常购物时段","人生阶段","家享策略人群"]

只输出：
1. 工具是否成功调用。
2. crowd_desc。
3. total。
4. 每个 tag 的属性分布，保留百分比和绝对人数（如果返回）。
5. 哪些 tag 为空或不支持。
6. 是否有脱敏或限制。
7. 失败原因。
```

### 2.8 竞品行为人群画像：浏览/加购/收藏/购买

目的：对同一个竞品商品分别圈浏览、加购、收藏、购买人群，比较行为漏斗画像差异。

分别复制以下 4 次，把 `{ACTION}` 换成：

- `浏览过`
- `加购过`
- `收藏过`
- `购买过`

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_crowd_audience_insight
参数：
query=帮我圈近30天{ACTION}宝贝id为{COMP_ITEM_ID}的人群
member_id={MEMBER_ID_MASKED}
tags=["用户性别","用户年龄","城市等级","消费能力等级","消费决策导向","历史大促高活人群","最常购物时段"]

只输出：
1. 工具是否成功调用。
2. ACTION。
3. crowd_desc。
4. total。
5. 用户性别、用户年龄、城市等级、消费能力等级、消费决策导向、历史大促高活人群、最常购物时段的分布。
6. 是否有脱敏或限制。
7. 失败原因。
```

### 2.9 竞品店铺人群画像：购买与浏览未购买

目的：如果已知竞品店铺名，拉竞品店铺购买人群和浏览未购买人群。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_crowd_audience_insight
参数：
query=帮我圈近30天购买过{COMP_SHOP_NAME}商品的人群
member_id={MEMBER_ID_MASKED}
tags=["用户性别","用户年龄","城市等级","消费能力等级","月均消费金额","月均消费频次","消费决策导向","历史大促高活人群","最常购物时段","人生阶段"]

只输出：
1. 工具是否成功调用。
2. crowd_desc。
3. total。
4. 每个 tag 的属性分布，保留百分比和绝对人数（如果返回）。
5. 是否有脱敏或限制。
6. 失败原因。
```

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_crowd_audience_insight
参数：
query=帮我圈近30天浏览过{COMP_SHOP_NAME}商品但未购买的人群
member_id={MEMBER_ID_MASKED}
tags=["用户性别","用户年龄","城市等级","消费能力等级","月均消费金额","月均消费频次","消费决策导向","历史大促高活人群","最常购物时段","人生阶段"]

只输出：
1. 工具是否成功调用。
2. crowd_desc。
3. total。
4. 每个 tag 的属性分布，保留百分比和绝对人数（如果返回）。
5. 是否有脱敏或限制。
6. 失败原因。
```

### 2.10 竞品关键词/搜索词线索

目的：当前没有确认能直接拉“竞品搜索词效果报表”，但可以从竞品解释和关键词挖掘拿明文关键词线索。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_competitor_explain_mining
参数：
entity_type=item
entity_id={BASE_ITEM_ID}
competitor_id={COMP_ITEM_ID}
methods=keyword
lookback_days={LOOKBACK_DAYS}
llm_polish=false

只输出：
1. 工具是否成功调用。
2. is_competitor。
3. confidence。
4. keyword route 的所有明文关键词。
5. 每个关键词对应的竞争解释、流量/GMV/搜索相关区间（如果返回）。
6. 返回字段名。
7. 如果返回 data_id，请返回 data_id。
8. 失败原因。
```

再用关键词视角找更多竞品：

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_competitive_detect_mining
参数：
subject_dimension=商品
subject_id={BASE_ITEM_ID}
mining_type=关键词

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 前 30 个关键词竞争候选，字段包括：item_id、item_name、shop_name、score、关键词、命中原因。
4. 如果返回 data_id，请返回 data_id。
5. 失败原因。
```

### 2.11 竞品推广场景/策略明细数据资产

目的：尝试用业务资产查询竞品商品在不同推广场景/策略下的表现。历史记录显示竞品可能是区间脱敏。

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_common_business_asset_dataquery
参数：
data_name=商品推广场景策略明细数据
query_key=商品ID
filters=[
  ["商品ID","=", "{COMP_ITEM_ID}"],
  ["日期",">=", "{START_DATE}"],
  ["日期","<=", "{END_DATE}"]
]
order_by=[["消耗","DESC"]]
limit=50

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 前 50 行，字段至少包括：日期、一级场景、投放策略、消耗、展现量、点击量、加购量、直接成交金额。
4. 是否脱敏为区间。
5. 如果返回 data_id，请返回 data_id。
6. 失败原因或限制原因。
```

### 2.12 VIEW/DEEPLINK 竞品资产流动

目的：尝试从“同行优秀品视角”拿自己商品与竞品商品之间的 VIEW 人群资产流入流出。

先查元数据：

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_data_asset_guide_retrieval
参数：
title_list=["商品VIEW人群资产流入流出明细-同行优秀品视角"]

只输出：
1. 工具是否成功调用。
2. schema_id。
3. 字段列表。
4. 必填过滤条件。
5. 最新可用分区日期。
6. 失败原因。
```

再查询资产：

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要：

工具：tool_common_business_asset_dataquery
参数：
data_name=商品VIEW人群资产流入流出明细-同行优秀品视角
query_key=商品ID
filters=[
  ["商品ID","=", "{BASE_ITEM_ID}"],
  ["竞对商品ID","=", "{COMP_ITEM_ID}"],
  ["日期",">=", "{START_DATE}"],
  ["日期","<=", "{END_DATE}"]
]
order_by=[["活跃资产数","DESC"]]
limit=50

只输出：
1. 工具是否成功调用。
2. 返回字段名。
3. 前 50 行。
4. 字段中如果有 V1/V2/I/E、流转类型、流入/流出/加深、渠道、资产状态，请完整保留。
5. 是否返回精确值、区间或为空。
6. 如果返回 data_id，请返回 data_id。
7. 失败原因或限制原因。
```

### 2.13 对所有 data_id 做 SQL 深挖

目的：任何工具返回 `data_id` 后，都用 SQL 反查字段、筛选竞品、聚合指标。

字段检查：

```text
请不要重新规划任务。请直接调用内部工具：

工具：tool_sql_query
参数：
sql=DESCRIBE {DATA_ID}
description=查看返回表字段结构

只输出 SQL 是否成功、字段名、字段类型。
```

样例行：

```text
请不要重新规划任务。请直接调用内部工具：

工具：tool_sql_query
参数：
sql=SELECT * FROM {DATA_ID} LIMIT 20
description=查看返回表前20行

只输出 SQL 是否成功、字段名、前20行。
```

按竞品筛选：

```text
请不要重新规划任务。请直接调用内部工具：

工具：tool_sql_query
参数：
sql=SELECT * FROM {DATA_ID} WHERE 商品ID = '{COMP_ITEM_ID}' LIMIT 50
description=筛选指定竞品商品ID

只输出 SQL 是否成功、字段名、返回行；如果没有命中，说明可能的商品ID字段名，并返回前20行样例。
```

聚合推广效果：

```text
请不要重新规划任务。请直接调用内部工具：

工具：tool_sql_query
参数：
sql=
SELECT 商品ID, 商品名称,
       SUM(展现量) AS 展现量,
       SUM(点击量) AS 点击量,
       SUM(花费) AS 花费,
       SUM(总成交金额) AS 总成交金额,
       CASE WHEN SUM(花费)=0 THEN NULL ELSE SUM(总成交金额)/SUM(花费) END AS ROI
FROM {DATA_ID}
GROUP BY 商品ID, 商品名称
ORDER BY 花费 DESC
LIMIT 20
description=按商品聚合推广效果

只输出 SQL 是否成功、字段名、结果表；如果字段名不存在，请先 DESCRIBE 并建议替代字段。
```

## Phase 2 汇总输出要求

当上述数据跑完后，让 DMP AI 输出最终竞品数据报告：

```text
请基于本轮对话中已经成功调用的工具结果，不要编造，不要使用未调用数据。

请为商品 {BASE_ITEM_ID} 的竞品 {COMP_ITEM_ID} 输出一份竞品研究表，包含：

1. 竞品基本信息
   - 竞品商品ID
   - 商品名称
   - 店铺名称
   - 类目
   - 是否确认竞品
   - 命中路径和 confidence/score

2. 销售数据
   - webwide 成交金额/笔数/件数/IPV/转化率区间或精确值
   - benchmark cust_type/uv/free 中拿到的精确同行销售/UV/自然搜索/免费流量数据
   - 每个字段注明来源工具和是否脱敏

3. 推广数据
   - 展现、点击、点击率、花费、ROI、引导成交金额、引导成交笔数、CPC、CPM、成交成本
   - 推广场景、投放策略、消耗、直接成交金额
   - 每个字段注明来源工具和是否脱敏

4. 搜索词/关键词数据
   - keyword route 命中的关键词
   - 关键词竞争解释
   - 是否有搜索/流量/GMV区间
   - 明确哪些数据还没有直接拿到

5. 人群数据
   - 购买人群 total 与画像
   - 浏览、加购、收藏、购买人群漏斗画像
   - 店铺购买、浏览未购买人群画像
   - 高价值标签：消费决策导向、历史大促高活、最常购物时段、人生阶段、家享策略人群

6. VIEW/DEEPLINK 资产流动
   - 流入/流出/加深状态
   - V1/V2/I/E 或资产状态
   - 渠道、流转类型、活跃资产数
   - 是否精确、区间或为空

7. 竞品打法判断
   - 投放目标
   - 关键词/人群预算倾向
   - 出价方式
   - 活动工具
   - 评价/买家秀/直播/关联宝贝等动作

8. 数据缺口
   - 哪些工具返回空
   - 哪些字段被安全策略限制
   - 哪些 data_id 还可以继续 SQL 深挖

请用表格输出，不要只给总结。
```

## 测试记录模板

每次测试后，把结果补到下面：

| Date | Base item | Competitor item | Prompt section | Tool called | Success | data_id | Key finding | Boundary / next test |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
