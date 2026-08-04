---
title: 万相台无界关键词推广第二批十文档语义校验
type: source-summary
created: 2026-08-04
updated: 2026-08-04
domain: meta
tags: [llm-wiki, semantic-validation]
sources:
  - raw/webpages/taobao/audience-intelligent-bidding-2026-08-04/content.md
status: active
---

# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: 钉钉结构化正文、表格和 42 张截图；没有以 OCR 替代结构化正文
- Evidence sources: content.md、tables.json、原始截图、官方目录树和既有正式页
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 智能出价/功能介绍 | bidding | 价值系数 1.1～3.0 | 人群价值系数范围，非固定溢价 | 正文 + IMG-01 | high | accepted-as-is | 标记为版本快照 |
| A02 | 智能出价/适用目标 | eligibility | 支持四目标，不支持稳投产比等 | 仅列来源明确支持/不支持范围 | 正文两处 | high | accepted-as-is | 执行前核对后台 |
| A03 | 趋势榜单/温度 | threshold | 25、10–25、10度以下；降温5/7度 | 来源当期温度分段 | 表格 + IMG-02 | high | accepted-as-is | 作为历史榜单样例，不固化为长期标签 |
| A04 | 覆盖率/定义 | formula | 实展量 ÷ 买词×人群规模展现量 | 买词×人群覆盖率公式 | 正文 + IMG-01/05 | high | accepted-as-is | 区分实时分子与昨日预估分母 |
| A05 | 智能拉新/洞察 | threshold | 截至昨天7天累计点击量大于1000 | 洞察入口历史门槛 | 正文 + IMG-04/07 | high | accepted-as-is | 标记为 2026-08-04 快照 |
| A06 | AI点睛升级 | limit | 计划去重后高于500，超出不生效 | 计划级屏蔽词历史上限 | 正文 | high | accepted-as-is | 与原单元级规则分开并标记升级日期 |
| A07 | SKU裂变 | limit | 单创意 4→20 个素材 | 素材上限升级快照 | 正文 + IMG-01 | high | accepted-as-is | 不外推至其他场景 |
| A08 | SKU裂变 | timing | 生成约1分钟 | 官方体验说明 | 正文 + IMG-03 | high | accepted-as-is | 不作为服务 SLA |
| A09 | 分时折扣 | UI label | 优势时段推荐 | 优质时段推荐 | 标题、正文与 IMG-04 存在文案差异 | medium | corrected | 正式页使用文档章节名“优质时段推荐”，说明界面可能变化 |
| A10 | 人群定义 | duration | 新客180/365天、流失7天、高价值近180天前30% | 各人群口径 | 正文 | high | accepted-as-is | 作为历史口径，执行前复核 |
