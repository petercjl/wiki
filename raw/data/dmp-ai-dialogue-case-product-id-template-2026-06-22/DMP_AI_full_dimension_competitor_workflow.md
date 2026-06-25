# DMP AI Full-Dimension Competitor Research Workflow

目标：针对一个本品商品 ID，系统性利用 `DMP_AI_internal_tools.md` 和 wiki 中沉淀的所有已验证工具/数据资产，完成竞品发现、竞品筛选、销售/搜索/推广/人群/资产流转/策略路径/店铺层面的全维度竞品研究。

适用入口：

- 本地工具手册：`/Users/pechen/AI/Research/DMP_AI_internal_tools.md`
- Wiki 查询入口：`/Users/pechen/wiki/queries/达摩盘AI竞品数据挖掘.md`
- Wiki 完整手册：`/Users/pechen/wiki/domains/电商运营/02-淘宝天猫/04-达摩盘AI/01-达摩盘AI内部工具与竞品数据挖掘手册.md`

## 0. 本次 MVP 覆盖评估

刚才针对 `{BASE_ITEM_ID}` 的过程已经覆盖：

| 维度 | 已覆盖内容 | 是否充分 | 说明 |
|---|---|---|---|
| 主体识别 | `tool_subject_identification_dataquery` | 基本充分 | 拿到本品店铺、会员、类目 ID。 |
| 竞品发现 | `tool_competitive_detect_mining` 的关键词、行业明星、广告竞价、细分市场 | 部分充分 | 拿到了候选池，但没有继续对 Top N 全部做关系验证和矩阵化。 |
| 单竞品关系验证 | `tool_competitor_explain_mining` | 对单竞品充分 | 对 `688909526916` 命中 5/6 路径。 |
| 单竞品销售区间 | `tool_item_webwide_effect_dataquery(type=webwide)` | 对单竞品充分 | 拿到竞品销售、IPV、转化区间。 |
| 单竞品广告区间 | `tool_item_webwide_effect_dataquery(type=ad)` | 对单竞品部分充分 | 拿到展现、点击、CTR、CPC、ROI 区间，但部分成本/成交字段被安全策略拦截。 |
| 推广场景策略 | `商品推广场景策略明细数据` | 对单竞品充分 | 拿到 `货品全站推 / 控投产比` 及脱敏指标。 |
| VIEW 竞品流转 | `商品VIEW人群资产流入流出明细-同行优秀品视角` | 对单竞品充分 | 拿到精确流入/流出 UV 和净流入。 |
| 搜索词线索 | `tool_competitor_explain_mining(methods=keyword)` | 基本覆盖 | 有明文关键词和总引流量区间，但没有词级点击/转化/排名。 |
| Excel 交付 | 已生成 | MVP 充分 | 结构完整，但不是全量维度版。 |

刚才没有充分利用的内容：

| 未充分利用内容 | 应补动作 |
|---|---|
| `tool_item_benchmark_dataquery(type=ad)` 精确同行推广明细 | 必须跑，并用 SQL 按 ROI/花费/成交排序。之前手册显示它比直接查竞品 ad 更强。 |
| `tool_item_benchmark_dataquery(type=cust_type/uv/free)` 精确同行销售、自然搜索、免费流量 | 必须跑，用来选“数据更完整”的竞品，不只盯行业明星 TOP1。 |
| `tool_sql_query` | 必须作为二阶段，对所有 `data_id` 做排序、过滤、聚合。 |
| `tool_item_success_path_mining` | 必须分别跑本品和候选竞品，提炼关键词/人群预算、出价模式、活动打法。 |
| `tool_crowd_audience_insight` | 必须跑竞品购买/浏览/加购/收藏人群画像，尤其 11 个高价值标签。 |
| `tool_e_commerce_crowd_advertising_dataquery` | 可用于自家广告关键词/人群/计划诊断，与竞品搜索词/推广结构做映射。 |
| `tool_shop_compete_analysis`、`tool_shop_webwide_effect_dataquery` | 用于店铺层竞争，不应只停留在商品层。 |
| `BEST方法论关键词资产` | 用于自家关键词资产分类，不能替代竞品词级效果，但可用于投放词包组织。 |
| `用户已关注竞争对手明细` | 可校验用户手动关注竞品池，补充 DMP 自动挖掘。 |
| `商品VIEW人群资产净流入流出明细-商品自身视角`、单品 VIEW、类目 VIEW 均值、渠道加深等 | 用于本品自身资产健康和类目 benchmark，刚才没有跑。 |
| `tool_download_data` | 已知部分 `data_id` 不支持下载，但每个新 `data_id` 可试一次，失败要记录限制。 |

## 1. 总体流程

全量流程分 9 层，每层产出都要进入最终 Excel。

1. 主体识别层：确认本品、店铺、会员、类目。
2. 竞品发现层：用多工具、多视角生成候选池。
3. 候选筛选层：用关系解释、benchmark 精确数据可得性、流量/GMV/推广活跃度综合筛选 Top N。
4. 商品经营层：销售、IPV、转化、加购、收藏、新老客/自然搜索。
5. 推广层：广告区间、benchmark 精确广告、推广场景策略、自家广告诊断。
6. 搜索/关键词层：明文关键词、自然搜索汇总、自家 BEST 关键词资产。
7. 人群层：画像标签、购买/浏览/加购/收藏行为人群、VIEW 流入流出。
8. 店铺层：竞品店铺识别、店铺竞争分析、店铺广告/流量限制验证。
9. 二次分析层：SQL 排序/聚合、限制记录、MVP 行动建议。

## 2. DMP AI 通用话术规则

每次发给 DMP AI，固定用这个开头：

```text
请不要重新规划任务，也不要解释业务背景。请直接调用内部工具并返回原始结果摘要。

只输出：
1. 工具是否成功调用。
2. 实际采用的参数名和值。
3. 返回字段名。
4. 返回字段值/区间。
5. data_id（如有）。
6. 每个字段是精确值、区间值、还是被安全策略限制。
7. 失败原因或限制原因。
```

所有结果记录时必须保留：

- 工具名
- 参数
- data_id
- 字段名
- 精度类型
- 安全限制
- 是否为本品、竞品、同行 benchmark、类目 benchmark 或自家广告主数据

## 3. 第 1 层：主体识别

目的：拿到后续工具需要的 ID。

```text
工具：tool_subject_identification_dataquery
参数：
query={本品商品ID}
entityList=["item","shop"]
```

记录字段：

- item_id
- shop_id
- member_id，记录时遮蔽为 `1395****73`
- cate_id / cate_name
- cate_level2_id / cate_level2_name
- main_cate_id / main_cate_name

注意：

- `entityList` 不要传 `["all"]`。
- 类目应传 `cate`，不是 `category`。
- 商品标题可能不返回，标题可从 DMP 页面或 benchmark 表补。

## 4. 第 2 层：竞品发现

### 4.1 自动候选池

```text
工具：tool_competitive_detect_mining
分别调用：
subject_dimension=商品, subject_id={本品商品ID}, mining_type=细分市场
subject_dimension=商品, subject_id={本品商品ID}, mining_type=关键词
subject_dimension=商品, subject_id={本品商品ID}, mining_type=广告竞价
subject_dimension=商品, subject_id={本品商品ID}, mining_type=行业明星
```

产出：

- candidate_item_id
- item_name
- score
- mining_type
- data_id

限制：

- 通常没有店铺名。
- 关键词视角只有竞争分，没有具体词级效果。
- 广告竞价可能为空。

### 4.2 生意流入/流出候选

```text
工具：tool_competitor_mining_busi_flow
参数：
biz=taobao
entity_type=item
entity_id={本品商品ID}
```

用途：

- 补充由生意流动发现的竞品。
- 默认配置可能只有竞品列表，没有金额/重叠人群。
- 嵌套参数序列化容易失败，先用默认配置。

### 4.3 用户已关注竞品

```text
工具：tool_common_business_asset_dataquery
参数：
data_name=用户已关注竞争对手明细
query_key=["日期","实体ID","竞对实体ID","竞对名称","竞对类型","探测方式","广告主ID"]
filters=[["广告主ID","=","{member_id}"]]
order_by=[["日期","DESC"]]
limit=100
```

用途：

- 校验用户手动关注/历史关注竞品。
- 与 DMP 自动挖掘候选池合并去重。

## 5. 第 3 层：候选筛选与关系验证

对候选池 Top N，每个候选都跑：

```text
工具：tool_competitor_explain_mining
参数：
entity_type=item
entity_id={本品商品ID}
competitor_id={候选竞品商品ID}
methods=keyword,busi_outflow,busi_inflow,niche,star,bidding
lookback_days=30
llm_polish=false
```

记录：

- is_competitor
- confidence
- hit_methods
- keyword_list
- keyword_ipv
- inflow_trd_amt / outflow_trd_amt
- same_cate_id / same_price_level
- total_gmv / current_gmv / growth_rate
- bidding 是否命中

候选评分建议：

| 评分项 | 权重 |
|---|---:|
| hit_methods 数量 | 30% |
| 关键词命中强度 | 20% |
| star/niche GMV 和增长区间 | 20% |
| benchmark 精确数据是否命中 | 20% |
| VIEW 流转是否有显著流入/流出 | 10% |

最终不要只选一个竞品，至少保留：

- 1 个行业明星最高分竞品
- 1 个关键词最高分竞品
- 1 个 benchmark 精确广告/销售表现最强同行
- 1 个生意流入/流出明显竞品

## 6. 第 4 层：商品经营数据

### 6.1 直接查指定竞品区间

```text
工具：tool_item_webwide_effect_dataquery
参数：
item_id={竞品商品ID}
start_date={YYYYMMDD}
end_date={YYYYMMDD}
type=webwide
```

返回维度：

- 成交笔数
- 成交金额
- 成交件数
- 加购数
- 收藏数
- ipv
- 支付转化率
- 加购率
- 笔单价
- 件单价
- 当笔成交件数

限制：竞品数据通常是区间值。

### 6.2 benchmark 精确同行经营数据

```text
工具：tool_item_benchmark_dataquery
参数：
item_id={本品商品ID}
start_date={YYYYMMDD}
end_date={YYYYMMDD}
type=cust_type
benchmark_type=同叶子类目同价格带top5均值
dimensions=["商品ID","商品标题"]
metrics=["ipv","自然搜索点击次数","自然搜索点击量","成交人数","加购人数","收藏人数","笔单价","支付转化率","加购率","件单价","当笔成交件数","总收藏数","总加购数","总成交金额","总成交笔数","总成交件数"]
```

这是必须跑的核心工具。

原因：

- 它能返回真实同行商品 ID。
- 可拿精确销售、UV、自然搜索汇总、加购、收藏。
- 比直接查询某竞品 `webwide` 的区间数据更有分析价值。

### 6.3 webwide 标杆均值

```text
工具：tool_item_benchmark_dataquery
参数：
item_id={本品商品ID}
start_date={YYYYMMDD}
end_date={YYYYMMDD}
type=webwide
benchmark_type=同叶子类目同价格带top5均值
dimensions=["商品ID"]
metrics=["总成交金额","总成交笔数","ipv","支付转化率","加购率","笔单价"]
```

用途：

- 作为类目同价带校准线。
- 不返回具体竞品列表。

## 7. 第 5 层：推广数据

### 7.1 直接查指定竞品广告区间

```text
工具：tool_item_webwide_effect_dataquery
参数：
item_id={竞品商品ID}
start_date={YYYYMMDD}
end_date={YYYYMMDD}
type=ad
```

用途：

- 拿竞品展现、点击、点击率、CPC、点击转化率、ROI 等区间。

限制：

- 花费、千次展现花费、总成交金额、总成交笔数、总成交成本等可能被安全策略拦截。

### 7.2 benchmark 精确推广明细

```text
工具：tool_item_benchmark_dataquery
参数：
item_id={本品商品ID}
start_date={YYYYMMDD}
end_date={YYYYMMDD}
type=ad
benchmark_type=同叶子类目同价格带top5均值
dimensions=["商品ID","商品标题"]
metrics=[
  "展现量","点击量","花费","点击率","平均点击花费","千次展现花费",
  "总成交金额","总成交笔数","点击转化率","投入产出比","总成交成本",
  "总加购数","加购率","总收藏数","收藏店铺数","店铺收藏成本",
  "总收藏加购数","总收藏加购成本","宝贝收藏加购数",
  "宝贝收藏成本","宝贝收藏率","加购成本"
]
```

这是推广层最强路径。

必须做 SQL 二次分析：

```sql
SELECT
  "商品ID",
  "商品名称",
  "展现量",
  "点击量",
  "花费",
  "平均点击花费",
  "投入产出比",
  "总成交金额",
  "总成交笔数",
  "点击转化率",
  "加购率",
  "总成交成本"
FROM {data_id}
ORDER BY "投入产出比" DESC
```

### 7.3 推广场景策略明细

```text
工具：tool_common_business_asset_dataquery
参数：
data_name=商品推广场景策略明细数据
query_key=["日期","商品ID","一级场景","投放策略","消耗","展现量","点击量","加购量","直接成交金额"]
filters=[["商品ID","=","{竞品商品ID}"],["日期","=","{YYYYMMDD}"]]
order_by=[["消耗","DESC"]]
limit=20
```

记录：

- 一级场景，比如 `货品全站推`、`关键词推广`
- 投放策略，比如 `控投产比`
- 消耗、展现、点击、加购、直接成交金额
- 竞品指标一般为区间值

### 7.4 自家广告人群/关键词/计划诊断

```text
工具：tool_e_commerce_crowd_advertising_dataquery
参数按当前广告主维度查询，where 必含广告主ID。
```

用途：

- 不是查竞品。
- 用来自家关键词、人群、计划、出价模式、广告表现诊断。
- 与竞品关键词线索和推广场景做映射，生成“我该怎么投”的动作。

## 8. 第 6 层：搜索词与免费流量

### 8.1 明文搜索词

用 `tool_competitor_explain_mining(methods=keyword)` 获取：

- keyword_list
- keyword_ipv 区间
- 竞争解释

限制：

- 没有词级点击、成交、排名、份额。

### 8.2 自然搜索汇总

用 `tool_item_benchmark_dataquery(type=cust_type)` 获取：

- 自然搜索点击量
- 自然搜索点击次数

这是搜索层的精确汇总指标。

### 8.3 免费流量来源

```text
工具：tool_item_benchmark_dataquery
参数：
item_id={本品商品ID}
start_date={YYYYMMDD}
end_date={YYYYMMDD}
type=free
benchmark_type=同叶子类目同价格带top5均值
dimensions=["商品ID","流量来源","一级场景ID","二级场景ID"]
metrics=["点击率","加购率","直接成交金额","直接成交笔数","总成交金额","总成交笔数","直接宝贝加购量","总宝贝加购量","店铺收藏量","直接宝贝收藏量","点击量","展现量","花费","投入产出比","支付转化率"]
```

注意：

- 不要传 `总宝贝收藏数`。
- 不要传 `单次点击成本`。

必须做 SQL 聚合：

```sql
SELECT
  "商品ID",
  "商品标题",
  "流量来源",
  SUM("点击量") AS 点击量,
  SUM("总成交金额") AS 总成交金额,
  SUM("总成交笔数") AS 总成交笔数,
  SUM("直接成交金额") AS 直接成交金额,
  SUM("直接成交笔数") AS 直接成交笔数,
  SUM("直接宝贝加购量") AS 直接宝贝加购量,
  SUM("总宝贝加购量") AS 总宝贝加购量,
  SUM("店铺收藏量") AS 店铺收藏量,
  SUM("直接宝贝收藏量") AS 直接宝贝收藏量
FROM {data_id}
GROUP BY "商品ID", "商品标题", "流量来源"
ORDER BY "商品ID", "总成交金额" DESC
```

### 8.4 BEST 方法论关键词资产

```text
工具：tool_data_asset_guide_retrieval
参数：
title_list=["BEST方法论关键词资产"]

工具：tool_common_business_asset_dataquery
参数：
data_name=BEST方法论关键词资产
query_key=["关键词","词类型","二级类目ID"]
filters=[["广告主ID","=","{member_id}"],["日期","=","{YYYYMMDD}"]]
limit=200
```

用途：

- 自家关键词分类和词包组织。
- 不提供竞品词级效果。

## 9. 第 7 层：人群画像与资产流转

### 9.1 竞品购买人群画像

```text
工具：tool_crowd_audience_insight
参数：
query="帮我圈近30天宝贝id为{竞品商品ID}的购买人群"
member_id="{member_id}"
tags=["用户性别","用户年龄","城市等级","消费能力等级","月均消费金额","月均消费频次","消费决策导向","历史大促高活人群","最常购物时段","人生阶段","家享策略人群"]
```

必须扩展测试的行为：

- 购买人群
- 浏览人群
- 加购人群
- 收藏人群
- 浏览未购买人群
- 购买过竞品但未购买本品人群，若自然语言能圈出

重点标签：

- 消费决策导向
- 历史大促高活人群
- 最常购物时段
- 人生阶段
- 家享策略人群

这些标签比基础性别年龄更能指导投放和素材。

### 9.2 竞品 VIEW 流入流出

流入：

```text
工具：tool_common_business_asset_dataquery
参数：
data_name=商品VIEW人群资产流入流出明细-同行优秀品视角
query_key=["日期","商品ID","竞对商品ID","竞品店铺ID","流转前同行状态","流转本品资产V1","流转本品资产V2","流转本品资产I","流转本品资产E","时间周期","流转类型"]
filters=[["商品ID","=","{本品商品ID}"],["竞对商品ID","=","{竞品商品ID}"],["日期","=","{YYYYMMDD}"],["类型","=","1"],["时间周期","=","30"],["流转类型","=","0"]]
order_by=[["流转本品资产V1","DESC"]]
limit=20
```

流出：

- 同上，但 `流转类型=1`。

记录：

- V1/V2/I/E 分层流入
- V1/V2/I/E 分层流出
- 净流入
- 竞品店铺 ID

### 9.3 本品自身 VIEW 资产

```text
工具：tool_common_business_asset_dataquery
参数：
data_name=商品VIEW人群资产净流入流出明细-商品自身视角
```

用途：

- 看本品自己在 V1/V2/I/E/W 的流转健康。
- 与竞品流转形成“我能承接谁、我流失给谁”的解释。

### 9.4 单品 VIEW 人群资产明细

```text
工具：tool_common_business_asset_dataquery
参数：
data_name=达摩盘单品VIEW人群资产明细
query_key=["日期","商品ID","VIEW状态类型","单日用户数","成交金额","贡献叶子类目成交金额"]
filters=[["商品ID","=","{本品商品ID}"],["日期","=","{YYYYMMDD}"]]
```

用途：

- 本品各 VIEW 状态规模和成交贡献。
- 目前只适合本品，不适合任意竞品。

### 9.5 类目/渠道 VIEW 基准

按手册继续验证：

- `货品VIEW叶子类目均值流转明细`
- `货品VIEW资产叶子类目分渠道流入明细`
- `货品VIEW资产渠道加深明细`
- `货品VIEW资产渠道加深-同行均值`

这些部分目前有些是 metadata verified 或 direct query failed，不应当直接当成稳定能力。流程中要作为“可选验证层”，跑到失败也要记录失败参数和失败原因。

## 10. 第 8 层：策略路径

分别对本品和每个 Top 竞品调用：

```text
工具：tool_item_success_path_mining
参数：
item_id={商品ID}
```

记录：

- 成长阶段所在周期
- 成长阶段
- 关键词/人群预算比例
- 推广目标
- 出价模式
- 控成本方式
- 活动工具：百亿补贴、淘宝秒杀、评价有礼、买家秀、直播、关联宝贝等

用途：

- 还原竞品打法，而不是只看数值。
- 形成“竞品为什么增长”的解释。

## 11. 第 9 层：店铺层竞争

### 11.1 竞品店铺识别

用 `tool_subject_identification_dataquery` 对竞品商品 ID 查：

- competitor shop_id
- competitor member_id
- cate_id

### 11.2 店铺竞争分析

```text
工具：tool_shop_compete_analysis
参数：
memberId={本店member_id}
memberName={竞品店铺名或memberId}
startDate={YYYYMMDD}
endDate={YYYYMMDD}
compStartDate={YYYYMMDD}
compEndDate={YYYYMMDD}
```

用途：

- 共同点击人数
- 共同点击占比
- 买家控制比例

### 11.3 店铺 webwide/ad 查询

```text
工具：tool_shop_webwide_effect_dataquery
```

用途：

- 验证店铺 GMV / ad 是否可查。

限制：

- 竞品店铺 GMV 可能完全阻断。
- 店铺广告可能部分区间脱敏。

## 12. SQL 和下载层

每个返回 `data_id` 的工具，都执行：

1. `DESCRIBE` 或选择前 5 行，确认字段名。
2. 按核心业务指标排序。
3. 聚合到商品/流量来源/场景/策略粒度。
4. 试一次 `tool_download_data`。

下载测试：

```text
工具：tool_download_data
参数：
data_id={data_id}
```

如果失败，记录：

- 是否参数错误
- 是否业务策略不允许下载
- 是否只有当前 data_id 不允许

## 13. 最终 Excel 工作簿结构

全量版 Excel 应包含这些 sheet：

1. `MVP Summary`：最终结论、可执行动作、数据可信度。
2. `Entity Map`：本品、店铺、会员、类目、竞品店铺 ID。
3. `Candidate Pool`：所有候选竞品、来源视角、score、data_id。
4. `Selection Matrix`：候选评分、命中路径、数据可得性、是否进入 Top N。
5. `Relationship Evidence`：每个 Top 竞品的 6 路解释。
6. `Webwide Ranges`：指定竞品销售/转化区间。
7. `Benchmark Sales Exact`：`cust_type/uv` 精确同行经营数据。
8. `Benchmark Ad Exact`：`ad` 精确同行推广数据。
9. `Free Traffic Exact`：`free` 免费流量来源聚合。
10. `Promotion Scene`：商品推广场景策略明细。
11. `Search Keywords`：明文关键词、自然搜索汇总、BEST 词资产。
12. `Audience Profile`：购买/浏览/加购/收藏人群画像。
13. `VIEW Flow Pair`：本品与竞品 VIEW 流入流出。
14. `VIEW Own Item`：本品自身 VIEW 资产。
15. `Success Path`：本品和竞品成长路径与打法。
16. `Shop Competition`：店铺层竞争、共同点击、买家控制。
17. `SQL Outputs`：所有 SQL 二次分析结果。
18. `Limitations`：失败工具、被拦截字段、不可下载 data_id。
19. `Raw Transcript`：DMP AI 原始摘要和关键 prompt。

## 14. 全量研究最小执行顺序

如果时间有限，但又想最大化利用 MD 内容，按这个顺序跑：

1. `tool_subject_identification_dataquery`
2. `tool_competitive_detect_mining` 四视角
3. `tool_item_benchmark_dataquery(type=ad/cust_type/free)` 三件套
4. 对 benchmark 结果用 `tool_sql_query` 排序和聚合
5. 从候选池 + benchmark 强同行中选 Top 5
6. 对 Top 5 跑 `tool_competitor_explain_mining`
7. 对 Top 5 跑 `tool_item_webwide_effect_dataquery(type=webwide/ad)`
8. 对 Top 5 跑 `商品推广场景策略明细数据`
9. 对 Top 5 跑 `商品VIEW人群资产流入流出明细-同行优秀品视角`
10. 对 Top 3 跑 `tool_crowd_audience_insight`
11. 对本品 + Top 3 跑 `tool_item_success_path_mining`
12. 跑 `BEST方法论关键词资产` 和 `tool_e_commerce_crowd_advertising_dataquery` 做自家投放映射
13. 补店铺层 `tool_shop_compete_analysis`
14. 试 `tool_download_data`
15. 生成全量 Excel 和 MVP 行动建议

## 15. 对刚才结果的修正建议

刚才的 Excel 可以作为 V0 MVP，但下一版应补：

1. 把 `734065650463`、`806643871787`、`528309297271` 这几个 benchmark 精确同行拉进来。
2. 不只分析 `688909526916`，因为它是行业明星强竞品，但 benchmark 精确表未命中它。
3. 竞品选择要分两类：
   - 战略竞品：比如 `688909526916`，行业明星、关系强、适合看区间和人群攻防。
   - 数据竞品：比如 benchmark 表命中的同行，适合拿精确销售/推广/免费流量。
4. 购买人群画像还没跑，应补 `tool_crowd_audience_insight`。
5. 成功路径还没跑，应补 `tool_item_success_path_mining`。
6. 自家广告和 BEST 关键词资产还没跑，应补，用来把竞品线索转成投放动作。
7. VIEW 自身资产和类目/渠道 benchmark 没跑，应作为下一层资产健康分析补上。

