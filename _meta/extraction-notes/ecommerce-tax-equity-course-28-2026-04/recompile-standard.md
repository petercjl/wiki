# Recompile Standard｜财税股权 28 期课程知识系统

- created: 2026-06-14
- reason: Peter reviewed the first compile and correctly pointed out that the formal pages were too outline-like and over-compressed.

## Core Correction

Transcript-to-wiki compilation must not compress course material into sparse outlines. The goal is not to produce fewer words. The goal is to transform oral classroom material into durable, searchable, explainable, and reusable knowledge.

## New Compilation Standard

Each formal page must include:

1. **完整解释链**：不仅写结论，还写为什么、怎么判断、先后顺序和适用条件。
2. **案例进入正文**：案例不能只放在 coverage matrix；必须进入对应正式页，并被转成可迁移规则。
3. **数字保留但标边界**：课程中的金额、比例、税率、指标、阈值要保留；政策性数字必须标注“需按最新法规复核”。
4. **经营语境补足**：对课堂口语、省略的前提和隐含逻辑进行理解性补充，但不能伪造原文没有的事实。
5. **Agent 可调用结构**：页面要支持未来回答，而不是只供人浏览；必须有诊断顺序、判断条件、风险边界和输出方式。
6. **少做浓缩，多做展开**：如果原文包含两天课程的推导，正式知识页应接近“系统讲义/方法文章”，而不是“知识点清单”。

## Failure Pattern in Previous Compile

Previous compile had correct high-level architecture but too many pages were outline-like. Example:

> 关键指标包括：毛利率、推广费率、边际贡献率、固定成本率、净利润率……

This is insufficient. A proper page should explain:

- each metric's business meaning;
- why ecommerce businesses misread it;
- how platform/channel/product structure changes it;
- what cases from the course demonstrate it;
- what diagnostic questions an Agent should ask;
- what decision the metric supports.

## Repair Mode

Current repair mode: **formal synthesis repair**.

- Raw transcripts are preserved unchanged.
- Existing learning-path structure can remain, but formal pages must be re-expanded.
- Extraction notes must be upgraded with fine-grained durable knowledge units from all 4 transcript files.
- After rewrite, run llm-wiki-audit-and-optimization again.
