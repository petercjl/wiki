# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: ASR + OCR + visual keyframe inspection
- Evidence sources: raw SRT/TXT/JSON, Bilibili titles and metadata, 221 sampled keyframes, OCR, repeated context across 14 videos
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | C13 00:00-02:53 | feature | 铺祸、祸祸 | 铺货 | Bilibili title + repeated UI OCR + full-video context | high | corrected | use 铺货 |
| A02 | C13 00:54-02:49 | UI path | 连接铺祸 | 链接铺货 | UI context shows pasted 1688 product URL | high | corrected | use 链接铺货 |
| A03 | C06/C10/C12 throughout | role | 组电、主电 | 主店 | mode diagram + repeated UI labels + paired term 分店 | high | corrected | use 主店 |
| A04 | C06/C10/C12 throughout | role | 分电 | 分店 | mode diagram + repeated UI labels | high | corrected | use 分店 |
| A05 | C04/C09-C14 throughout | data object | SQ、STU、SKO | SKU | visible product/SKU mapping grids + ecommerce terminology | high | corrected | use SKU |
| A06 | C11 03:17 | data field | 库车 | 库存 | rule UI + repeated context | high | corrected | use 库存 |
| A07 | C11 03:30-04:20 | state | 伤出、进用、金用 | 删除、禁用 | visible batch buttons and switches + causal explanation | high | corrected | use 删除/禁用 |
| A08 | C02 02:25-02:31 | UI action | 一切恢复 | 一键恢复 | button context + operation meaning | high | corrected | use 一键恢复; current UI verification required |
| A09 | C07 00:00-00:29 | relationship | 下岸油、上岸 | 下游、上游 | video title + distributor relationship diagram | high | corrected | use 下游/上游分销商 |
| A10 | C05-C12 | mode | 分销商模式、店群模式 | 分销商模式、店群模式 | Bilibili titles + mode diagram + repeated UI labels | high | accepted-as-is | preserve exact mode names |
| A11 | C09/C10 00:58-01:32 | binding rule | 商家编码唯一 | 商家编码在店内唯一 | repeated speech + rule form UI | high | accepted-as-is | state as binding prerequisite, mark time-sensitive |
| A12 | C11 04:21-04:31 | risk boundary | 分销商实时同步只能上级到下级 | 单向：上级分销商 → 下级分销商 | explicit negation + relationship diagram | high | accepted-as-is | preserve as hard boundary; current-version verification required |
| A13 | C12 07:07-07:34 | direction | 可改成双向、一般以主店为基准 | 店群实时同步可配置单向或双向 | explicit narration + directional UI control | high | accepted-as-is | distinguish from distributor-mode boundary |
| A14 | C13 01:19-01:30 | numeric limit | 整页全选 50 个产品 | 当时界面每页 50 个 | transcript + product-list UI | medium | accepted-as-is | mark as 2026-06 UI snapshot, verify current limit |
| A15 | C01/C02 | capability count | 三种修改方法 vs 两种修改方法 | version-dependent entry differences | two separately dated videos show different navigation | high | unresolved | mark the fixed count 待确认 and exclude it from operational instructions; describe dated versions and require current UI check |
| A16 | C09/C10 | image field | 铸图、组图 | 主图/其他主图/属性图片 | visible rule field list + surrounding explanation | medium | corrected | use field names only when legible; otherwise say 商品图片类字段 |
| A17 | C01 example | case term | 大醋 | 大促 | timed title-keyword example context | high | corrected | treat as example only, not a product feature |
| A18 | all videos | product identity | logo text not consistently legible | 批量修改工具（描述性名称） | user description + video titles; no reliable official product name | medium | unresolved | mark the official product name 待确认 and exclude any invented brand from operational instructions; use only the descriptive tool name |

## Systematic Variant Search

- Searched all raw TXT/SRT files for `铺祸|组电|主电|分电|SQ|STU|SKO|库车|进用|金用|一切恢复|大醋`.
- Normalized variants are allowed only in interpreted notes and future formal pages; raw ASR is unchanged.
- Numeric examples such as 50 products per page and 2000+ queried products are preserved with dates and are not generalized into permanent limits.

## Safe Interpretation Boundary

- Exact current menu labels and available synchronization fields require checking the live tool because videos span 2023-2026.
- Demo shop names, product IDs, authorization codes, and account identifiers are evidence-only and must not enter formal instructions.
- The official product/brand name remains unresolved; formal pages should use the descriptive name “淘宝批量修改与店群同步工具”.
