# Audit Handoff

| field | value |
| --- | --- |
| source_slug | china-express-pricing-basics-2026-07-01 |
| adapter | llm-wiki-ingest unknown-source/web research notes |
| raw_source | raw/webpages/china-express-pricing-2026-07-01/source-notes.md |
| source_profile | _meta/extraction-notes/china-express-pricing-basics-2026-07-01/source-profile.md |
| coverage_matrix | _meta/extraction-notes/china-express-pricing-basics-2026-07-01/coverage-matrix.md |
| formal_pages | domains/电商运营/01-通用电商方法/06-物流履约与快递成本/index.md; domains/电商运营/01-通用电商方法/06-物流履约与快递成本/01-中国快递收费方式基础.md; queries/中国快递收费与物流成本诊断.md |
| unresolved | 具体快递公司价格、抛比系数、面单费、隐私面单费和月结折扣需要按实际日期、地区、合同和平台后台二次核验。 |
| expected_agent_use | 回答国内快递怎么收费、商家如何核算物流成本、泡货如何判断、面单费如何入账、快递与快运如何选择。 |

## Validation Notes

- 所有知识单元已在 coverage matrix 中映射到正式页面。
- 正式页前部明确动态规则声明，避免把公司示例当成长期标准。
- 后续如接入某家快递实时价格或平台电子面单账单，应另建 API/平台来源并按日期归档。

