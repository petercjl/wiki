---
title: 淘宝营销工具规划查询入口
type: query
created: 2026-06-03
updated: 2026-06-03
domain: 电商运营
tags: [ecommerce, taobao, marketing-tool]
sources:
  - raw/webpages/taobao/taobao-coupon-settings-merchant-ops-2026-06-02.md
  - raw/webpages/taobao/taobao-shop-promotion-stacking-rule-upgrade-2026-04-14.md
  - raw/webpages/taobao/taobao-super-discount-registration-whitepaper-2026-05-19.md
status: active
---

# 淘宝营销工具规划查询入口

## 用途

当用户提出“根据淘宝营销知识库，帮我规划最合理的营销工具”这类问题时，AI Agent 应先读取本页，再读取相关工具页和规则页，不要直接从原始网页开始推理。

## 回答前必须读取

- [[domains/电商运营/02-淘宝天猫/02-淘宝营销工具/04-淘宝营销工具选择Playbook|淘宝营销工具选择 Playbook]]
- [[domains/电商运营/02-淘宝天猫/02-淘宝营销工具/03-淘宝营销工具叠加与互斥规则|淘宝营销工具叠加与互斥规则]]
- [[domains/电商运营/02-淘宝天猫/02-淘宝营销工具/01-淘宝营销工具：优惠券|淘宝营销工具：优惠券]]
- [[domains/电商运营/02-淘宝天猫/02-淘宝营销工具/02-淘宝营销工具：超级立减|淘宝营销工具：超级立减]]

必要时再回到 raw source 核对官方原文：

- `raw/webpages/taobao/taobao-coupon-settings-merchant-ops-2026-06-02.md`
- `raw/webpages/taobao/taobao-shop-promotion-stacking-rule-upgrade-2026-04-14.md`
- `raw/webpages/taobao/taobao-super-discount-registration-whitepaper-2026-05-19.md`

## 需要向商家确认的信息

- 商品类目、价格带、毛利率、库存。
- 活动目标：拉新、转化、客单、清库存、大促承接、会员运营、客服追单。
- 活动时间：日销、预热、售卖、大促、预售、主题营销。
- 当前已有优惠：优惠券、多件优惠、单品立减、超级立减、平台优惠。
- 目标到手价、可承受让利、红线价。
- 是否需要人群、渠道、场景定向。
- 是否已在商品图、详情页、客服话术中展示优惠信息。

## 回答结构

```md
## 结论

推荐工具组合：
不建议使用：

## 推荐理由

- 经营目标：
- 规则匹配：
- 到手价逻辑：

## 工具设置建议

- 优惠类型：
- 时间：
- 商品/SKU 范围：
- 面额/折扣/立减：
- 发放量/限领：

## 风险检查

- 叠加/互斥：
- 最低价：
- 价保：
- 资损：
- 大促/主题活动冲突：
- 主图/详情页/客服话术：

## 需要商家确认

- ...
```

## 当前知识库已覆盖的关键规则

- 优惠券和多件优惠在同一子订单互斥择优，不再叠加。
- 单品立减可用于 SKU 级价格，再叠加一种店铺级工具。
- 超级立减适合日销直降，但大促、预售、主题营销存在不生效、异常或互斥关系。
- 店铺券等普惠优惠是否完整覆盖超级立减活动周期，会影响活动普惠券后价校验。
- 规划前必须核查最低价、价保、红线价、资损和商品素材展示一致性。
