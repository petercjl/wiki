---
title: SKU裂变：爆款风格复制与素材限制
type: playbook
created: 2026-08-04
updated: 2026-08-04
domain: 电商运营
tags: [ecommerce, taobao, tmall, wanxiangtai, keyword-promotion, creative, sku]
sources:
  - raw/webpages/taobao/wanxiangtai-wujie-woyaotuiguang-2026-08-03/document-tree.json
  - _meta/extraction-notes/wanxiangtai-woyaotuiguang-completion-2026-08-04/coverage-matrix.md
  - raw/webpages/taobao/sku-splitting-tool-2026-08-04/content.md
  - raw/assets/sku-splitting-tool-2026-08-04/
  - _meta/extraction-notes/wanxiangtai-keyword-promotion-batch-2-2026-08-04/coverage-matrix.md
status: active
---

# SKU裂变：爆款风格复制与素材限制

## 一句话定位

SKU 裂变把同一商品中表现较好的创意风格复制到其他 SKU：AI 学习构图、光线、色调和版式，再为不同规格生成新素材。它提升的是素材生产效率，不保证生成图一定合格或投放效果一定更好。

官方当期说明将单创意素材上限从 4 张提升到 20 张，并在关键词推广创意设置中提供 AI 裂变入口。

![[raw/assets/sku-splitting-tool-2026-08-04/01.png]]

> 图：界面显示 `0/20` 与 AI 百变制图入口，属于 2026-08-04 产品快照。

图片语义锚点：单创意素材计数 0/20 和 SKU 裂变入口。

## 操作主线

1. 在关键词推广的创意设置中进入 AI 裂变。
2. 选择表现较好的原始创意，作为风格参考。
3. 选择需要生成素材的目标 SKU。
4. 等待系统生成候选图并逐张检查。
5. 只把商品结构、文字、颜色和规格都准确的素材加入投放，并做后续效果验证。

入口出现有两个前提：商品存在多个 SKU 图，且当前素材不是视频；否则素材下不会出现 SKU 裂变入口。生成结果后还可以进入“对话修图”做替换、去除、添加元素、换背景或调整光影，但每次修改后仍要重新核验商品真实性。

## 输入素材限制

| 限制类型 | 检查重点 |
| --- | --- |
| 原图 | 含赠品，不支持 |
| 原图 | 分格展示多个商品，不支持 |
| 原图 | 含代言人或明星，不支持 |
| SKU 图 | 分格展示多个商品，不支持 |
| SKU 图 | 没有商品主体，不支持 |
| SKU 图 | 商品主体不完整，不支持 |

![[raw/assets/sku-splitting-tool-2026-08-04/04.png]]

> 图：不支持裂变的 SKU 或不合格素材会被系统拒绝；具体原因以界面提示为准。

图片语义锚点：原图或 SKU 图不清晰、不完整时拒绝生成。

如果希望保留含赠品等不合格主图，可另上传一张符合限制的创意图作为裂变原图，不必修改商品主图。来源示例称生成通常约需 1 分钟，这不是服务时限承诺。生成后必须核验商品结构、规格、颜色、文字、Logo 和连接关系；任何变形或错配素材都不应进入投放。

## Agent 使用边界

- 把爆款图当“视觉风格参考”，不能据此改变目标 SKU 的真实商品结构。
- 不因素材数量上限提高就一次性启用全部图片；先小批测试点击和转化。
- 保留原始图、生成图、审核结果和投放版本，方便追溯哪类风格有效。
- 上限、入口和生成时间均是 2026-08-04 快照，执行时复核当前后台。

## 相关记忆

- [[domains/电商运营/02-淘宝天猫/万相台无界白皮书/01-关键词推广/index|万相台无界关键词推广]]
