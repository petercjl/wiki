# QA Audit Report｜财税股权 28 期课程知识系统

- audit date: 2026-06-13
- skill: llm-wiki-audit-and-optimization
- target: `domains/ecommerce-ops/learning-paths/ecommerce-tax-equity-strategic-finance/`
- mode: Post-Ingest QA + Compile/Route Audit

## 1. Target Map

- formal path: `domains/ecommerce-ops/learning-paths/ecommerce-tax-equity-strategic-finance/`
- formal pages: 12 Markdown files, including index and Agent usage template.
- raw archive: `raw/transcripts/ecommerce-tax-equity-course-28-2026-04/`
- extraction notes: `_meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/`
- domain index route: `domains/ecommerce-ops/index.md`
- root index route: `index.md`

## 2. Placeholder / Shell Scan

Mechanical placeholder scan result:

- SHELL: 0
- THIN: 0
- OK: 12

Verdict: no compile-placeholder P0 found. The pages are not duplicate boilerplate shells.

## 3. Compile Audit

### Strengths

- The 4 transcript files were correctly treated as one source bundle, not as D1/D2 classroom notes.
- The formal learning path has a coherent dependency order: risk genes → four accounts → tax compliance → tax burden model → entity/fund separation → finance-accounting integration → equity/control → incentive governance → equity as resource integration → strategic finance → Agent template.
- Raw sources, source profile, source inventory, coverage matrix, omission audit, and audit handoff exist.
- Tax/legal risk boundaries are present and prevent unsafe direct execution advice.

### Issues Found Before Patch

| priority | label | issue | affected area |
| --- | --- | --- | --- |
| P1 | compile-omission | Several important case anchors existed in extraction notes but were not integrated into formal page bodies. | 03/06/07/09/10 |
| P1 | compile-shallow | Some pages had correct frameworks but lacked enough numeric/case evidence for future Agent answers. | 04/06/10 |
| P1 | route-template-gap | Agent template existed but did not yet point strongly enough to case/evidence-based reasoning. | 11 indirectly |
| P2 | route-boundary-conflict | Some finance/accounting content overlaps with existing platform-settlement accounting page; no contradiction found, but future cross-linking can be improved. | ecommerce-ops finance-accounting |

### Patches Applied

Added case, number, and risk anchors into formal pages:

- `03-tax-compliance-path-and-red-lines.md`: 山东暖宝宝补税、小规模天猫 1100 万/350 万申报偏离、抖音服务费收入错配、风险触发源、不可操作化提醒。
- `04-tax-burden-model-vat-income-tax-personal-tax.md`: 500 万、300 万、25%、20%、13%、6% 等数字锚点和服务费/代销模型风险边界。
- `06-business-finance-integration-profit-accounting.md`: 四平台边际贡献、2.5 亿/4 万单/13% 退货率、仓库黑洞、箱包/北京女装案例、现金流指标和获客成本边界。
- `07-equity-structure-shareholder-control.md`: 李子柒/微念、罗振宇/申音、雷士照明控制权案例、代持与人格混同、股权设计顺序。
- `08-incentive-dividend-budget-system.md`: 出资股、人力股、管理股、期权、虚拟股、分红股、有限合伙平台、阿米巴局部最优风险。
- `09-equity-as-resource-integration-tool.md`: 良品铺子、石家庄 200 万绑定供应商、大疆/格力/欧莱雅代理风险、股权换资源转化规则。
- `10-strategic-finance-competition-indicators.md`: 地毯涨价、男士石墨烯内裤提价、代理型业务财务风险、战略财务判断顺序。

## 4. Route Audit

### Strengths

- Root index includes the learning path and all 11 formal chapter links.
- Domain index includes a concise module-level route to the path and key pages.
- Learning path index is ordered and readable.
- Chapter titles are Chinese, human-readable, and problem-oriented.
- Agent usage template exists.

### Remaining Route Notes

- P2: could later add a query entry such as `queries/ecommerce-tax-equity-diagnosis.md` if Peter often asks direct diagnostic questions. Not required for current usability because the root/domain/path indexes already route correctly.
- P2: could cross-link `finance-accounting/ecommerce-platform-settlement-accounting` with page 06 if platform settlement and tax-equity diagnosis are often used together.

## 5. Reasoning Readiness Audit

The learning path can now support:

- ecommerce tax risk diagnosis;
- 30/90/365-day compliance transition planning;
- tax burden variable identification;
- multi-company / multi-store / fund-separation review;
- finance-accounting profit model review;
- equity/control/incentive review;
- strategic finance diagnosis.

The patches improve future answers because Agent responses can cite cases and numbers rather than only generic frameworks.

## 6. Scores

| dimension | score | rationale |
| --- | ---: | --- |
| No placeholder shells | PASS | scan found SHELL 0, THIN 0 |
| Source-to-knowledge transformation | 4 | strong thematic recompile, not classroom summary |
| Depth of reasoning | 4 | frameworks and decision order are present; some policy details intentionally bounded |
| Evidence preservation | 4 | improved after patch; most key cases/numbers now in formal pages |
| Case transferability | 4 | patches convert cases into transfer rules |
| Module boundaries | 4 | clear learning path; slight overlap with platform settlement accounting |
| Decision process | 4 | Agent template and chapter order support decisions |
| Template readiness | 4 | template exists; could add query entry later |
| Traceability | 5 | raw, notes, coverage, audit handoff present |
| Noise removal | 5 | classroom/marketing noise omitted or raw-only |
| Actionability | 4 | supports diagnosis and planning; execution still requires tax/legal review |

## 7. Final Verdict

Current state after patch: **usable and reasonably well compiled**.

No P0 blockers remain. The main pre-patch weakness was `compile-omission` of vivid course anchors from formal pages; this has been patched. Remaining improvements are P2 routing conveniences, not blockers.
