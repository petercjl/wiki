---
title: 财税股权 28 期知识库迁移融合计划
type: decision
created: 2026-06-14
updated: 2026-06-14
domain: meta
tags: [llm-wiki, knowledge-base, reorganization, ecommerce, finance-accounting]
sources:
  - domains/财税与经营财务/90-课程包/01-财税股权28期/domains/视觉制作/05-小红书风格AI生图/index.md
  - _meta/extraction-notes/ecommerce-tax-equity-course-28-2026-04/coverage-matrix.md
status: approved
---

# 财税股权 28 期知识库迁移融合计划

本计划先做信息架构和迁移融合判断。Peter 已确认关键决策：新增 `domains/财税与经营财务/`，正式知识页使用中文文件名，Agent 模板迁移到 `queries/`，08/20 激励页合并，24 归入电商财税合规。

## 1. 本次试点要验证的原则

LLM Wiki 不是课程归档，而是 Peter 的个人记忆系统。课程是来源，正式知识应进入长期内容域，并和旧知识融合。

对“财税股权 28 期”来说，当前路径 `domains/财税与经营财务/90-课程包/01-财税股权28期/` 是来源形状，不是最佳记忆形状。

## 2. 需要 Peter 确认的架构决策

### 2.1 是否新增一级知识域：财税与经营财务

推荐新增：

```text
domains/财税与经营财务/
├── domains/视觉制作/05-小红书风格AI生图/index.md
├── 电商财税合规/
├── 经营财务与业财一体/
├── 股权与激励/
├── 战略财务/
├── 内控与组织能力/
└── 课程包/
```

理由：

- Peter 的知识库未来会有独立财税知识，不应全部埋在 `ecommerce-ops`。
- 本课程虽然以电商企业为场景，但增值税、所得税、分红、股权、预算、ROE、BP 等知识可以迁移到非电商企业。
- `ecommerce-ops` 可以保留“电商财税与经营财务入口”，但正式知识主体放在 `财税与经营财务` 更利于长期生长。

备选方案：

```text
domains/电商运营/财税与经营财务/
```

适用条件：Peter 暂时不希望扩展一级 domain，先把财税作为电商运营的子能力。

Peter 确认：采用新增一级知识域方案。

### 2.2 learning-paths 的新定位

推荐将当前 learning path 降级为来源包：

```text
domains/财税与经营财务/90-课程包/01-财税股权28期/
```

只保留：

- 课程包 domains/视觉制作/05-小红书风格AI生图/index
- raw 转写链接
- coverage matrix 链接
- 课程案例锚点
- 指向正式知识页的导航

不再把它作为唯一正式知识目录。

### 2.3 文件名和标题

推荐正式知识页使用中文文件名：

```text
01-电商税务合规路径与红线.md
02-增值税进销项与发票管理.md
```

英文 slug 保留在 frontmatter：

```yaml
slug: vat-input-output-and-invoice-management
aliases:
  - 增值税进销项
  - 发票管理
```

Peter 确认：正式知识页默认使用中文文件名。

### 2.4 关联式融合原则

Peter 确认：旧知识有自己的来源和体系，不能因为发现相关性就直接移动或吞并到新知识中。更合理的方式是“关联式融合”：

- 旧知识保留在原知识体系中，继续承担原来的意义。
- 新知识页增加“相关记忆”或“关联旧知识”小节，说明过去哪些知识可作为印证、旁证、补充场景或反例。
- 只有新旧页面本身已经重复、同属一个长期概念且没有独立来源体系时，才考虑真正合并。
- 对课程、书籍、平台规则这类有独立语境的旧知识，默认保留原路径，只做双向链接或索引关联。

这更接近人的记忆：新知识会激活旧知识、重新解释旧知识，但不会抹掉旧知识原来的结构。

## 3. 拟议目标结构

如果采用推荐方案：

```text
domains/财税与经营财务/
├── domains/视觉制作/05-小红书风格AI生图/index.md
├── 电商财税合规/
│   ├── 电商企业财税风险的经营基因.md
│   ├── 电商税务合规路径与红线.md
│   ├── 增值税、所得税与个税的电商税负模型.md
│   ├── 增值税进销项与发票管理.md
│   ├── 企业所得税、税务利润与成本扣除.md
│   ├── 主体拆分、代销与收入性质转换.md
│   └── 合规转型路线图.md
├── 经营财务与业财一体/
│   ├── 电商企业四本账.md
│   ├── 收入确认、退货、补偿与平台补贴口径.md
│   ├── 平台利润表与边际贡献率.md
│   ├── 业财一体与利润核算体系.md
│   ├── 预算、经营计划与月度经营分析.md
│   └── 存货周转、现金流与 ROE.md
├── 股权与激励/
│   ├── 股权结构、持股主体与控制权设计.md
│   ├── 股东投钱、取钱与分红税负.md
│   ├── 控股公司、项目公司与有限合伙平台.md
│   ├── 电商团队激励、分红与预算联动.md
│   ├── 激励机制、奖金包与股权条件.md
│   └── 股权作为资源整合工具.md
├── 战略财务/
│   ├── 战略财务：用财务指标支撑竞争战略.md
│   └── 商业模式选择与税负承载能力.md
├── 内控与组织能力/
│   ├── 多公司、多店铺与资金隔离的合规架构.md
│   ├── 资金、库存与权限内控.md
│   ├── 电商财务团队、BP 与组织能力.md
│   └── 工贸、拿货、代理、品牌四类业务的税务规划.md
└── 课程包/
    └── 财税股权28期/
        ├── domains/视觉制作/05-小红书风格AI生图/index.md
        └── 课程案例锚点库.md
```

## 4. 迁移融合表

| 旧页面 | 当前角色 | 拟议内容域 | 旧知识融合判断 | 拟议中文新路径 | 是否需 Peter 确认 |
| --- | --- | --- | --- | --- | --- |
| `domains/视觉制作/05-小红书风格AI生图/index.md` | 来源包目录 + 总论入口 | 课程包 | source-package-only；保留为课程来源导航，不作为正式知识主目录 | `domains/财税与经营财务/90-课程包/01-财税股权28期/domains/视觉制作/05-小红书风格AI生图/index.md` | 是 |
| `01-ecommerce-tax-risk-business-genes.md` | 概念页 | 电商财税合规 | create-new；与 `ecommerce-ops/domains/视觉制作/05-小红书风格AI生图/index` 交叉链接 | `domains/财税与经营财务/01-电商财税合规/01-电商企业财税风险的经营基因.md` | 是 |
| `02-four-account-system.md` | 框架页 | 经营财务与业财一体 | create-new；未来可和企业经营分析类知识融合 | `domains/财税与经营财务/02-经营财务与业财一体/01-电商企业四本账.md` | 是 |
| `03-tax-compliance-path-and-red-lines.md` | 概念/规则页 | 电商财税合规 | create-new；未来和通用税务合规页面互链 | `domains/财税与经营财务/01-电商财税合规/02-电商税务合规路径与红线.md` | 是 |
| `04-tax-burden-model-vat-income-tax-personal-tax.md` | 模型页 | 电商财税合规 | create-new；可拆出通用税负模型，但本轮先保留电商版本 | `domains/财税与经营财务/01-电商财税合规/03-增值税、所得税与个税的电商税负模型.md` | 是 |
| `05-multi-company-store-fund-separation.md` | 架构页 | 内控与组织能力 | create-new；和股权架构、主体拆分互链 | `domains/财税与经营财务/05-内控与组织能力/01-多公司、多店铺与资金隔离的合规架构.md` | 是 |
| `06-business-finance-integration-profit-accounting.md` | 方法页 | 经营财务与业财一体 | extend-existing-with-section；应融合 `domains/电商运营/01-通用电商方法/03-平台结算与经营财务/01-电商平台结算时间口径财务核算方法.md` 的平台结算口径 | `domains/财税与经营财务/02-经营财务与业财一体/04-业财一体与利润核算体系.md` | 是 |
| `07-equity-structure-shareholder-control.md` | 概念页 | 股权与激励 | create-new；未来可抽象为通用股权控制权页 | `domains/财税与经营财务/03-股权与激励/01-股权结构、持股主体与控制权设计.md` | 是 |
| `08-incentive-dividend-budget-system.md` | 方法页 | 股权与激励 | merge/extend；和 20 页存在重叠，应合并为“激励总论 + 条件设计”双层 | `domains/财税与经营财务/03-股权与激励/04-电商团队激励、分红与预算联动.md` | 是 |
| `09-equity-as-resource-integration-tool.md` | 方法页 | 股权与激励 | create-new；保留资源整合视角，与品牌/供应链知识互链 | `domains/财税与经营财务/03-股权与激励/05-股权作为资源整合工具.md` | 是 |
| `10-strategic-finance-competition-indicators.md` | 战略财务页 | 战略财务 | create-new；可与品牌战略、商业模式页互链 | `domains/财税与经营财务/04-战略财务/01-战略财务：用财务指标支撑竞争战略.md` | 是 |
| `domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略/11-Agent使用模板：心智产品力与大单品诊断.md` | Agent 模板 | query | move-to-query；Peter 已确认放到 `queries/`，作为财税股权诊断入口 | `queries/电商企业财税股权诊断.md` | 已确认 |
| `12-revenue-recognition-refunds-and-subsidies.md` | 专题页 | 经营财务与业财一体 | merge/extend；和平台结算财务核算页强相关，需合并口径或互为主从 | `domains/财税与经营财务/02-经营财务与业财一体/02-收入确认、退货、补偿与平台补贴口径.md` | 是 |
| `13-platform-profit-and-marginal-contribution.md` | 专题页 | 经营财务与业财一体 | create-new；未来和投流、平台经营分析知识融合 | `domains/财税与经营财务/02-经营财务与业财一体/03-平台利润表与边际贡献率.md` | 是 |
| `14-internal-control-funds-inventory-authority.md` | 专题页 | 内控与组织能力 | create-new；同时链接供应链仓储和财务核算 | `domains/财税与经营财务/05-内控与组织能力/02-资金、库存与权限内控.md` | 是 |
| `15-vat-input-output-and-invoice-management.md` | 专题页 | 电商财税合规 | create-new；未来可拆通用增值税页和电商应用页 | `domains/财税与经营财务/01-电商财税合规/04-增值税进销项与发票管理.md` | 是 |
| `16-income-tax-profit-adjustment-and-cost-deduction.md` | 专题页 | 电商财税合规 | create-new；与 04 页建立模型/专题关系 | `domains/财税与经营财务/01-电商财税合规/05-企业所得税、税务利润与成本扣除.md` | 是 |
| `17-subject-splitting-consignment-and-income-nature.md` | 专题页 | 电商财税合规 | create-new；必须保留风险边界，不写成方案 | `domains/财税与经营财务/01-电商财税合规/06-主体拆分、代销与收入性质转换.md` | 是 |
| `18-shareholder-money-in-out-and-dividend-tax.md` | 专题页 | 股权与激励 | create-new；与 04、07 页互链 | `domains/财税与经营财务/03-股权与激励/02-股东投钱、取钱与分红税负.md` | 是 |
| `19-holding-company-project-company-and-partnership-platform.md` | 专题页 | 股权与激励 | create-new；涉及税务、股权、组织三域，主归股权 | `domains/财税与经营财务/03-股权与激励/03-控股公司、项目公司与有限合伙平台.md` | 是 |
| `20-incentive-mechanism-bonus-pool-and-equity-conditions.md` | 专题页 | 股权与激励 | merge-into-08；Peter 已确认与 08 合并，避免激励知识双入口 | `domains/财税与经营财务/03-股权与激励/04-电商团队激励、分红与预算联动.md` | 已确认 |
| `21-business-model-selection-and-tax-bearing-capacity.md` | 专题页 | 战略财务 | create-new；和品牌/商业模式知识互链 | `domains/财税与经营财务/04-战略财务/02-商业模式选择与税负承载能力.md` | 是 |
| `22-budget-operating-plan-and-monthly-review.md` | 专题页 | 经营财务与业财一体 | create-new；未来和经营分析模板融合 | `domains/财税与经营财务/02-经营财务与业财一体/05-预算、经营计划与月度经营分析.md` | 是 |
| `23-finance-team-bp-and-organization-capability.md` | 专题页 | 内控与组织能力 | create-new；也可放 AI/组织能力，但本轮主归财务组织 | `domains/财税与经营财务/05-内控与组织能力/03-电商财务团队、BP 与组织能力.md` | 是 |
| `24-business-type-tax-planning-scenarios.md` | 专题页 | 电商财税合规 | create-new；Peter 已确认归入电商财税合规 | `domains/财税与经营财务/01-电商财税合规/07-工贸、拿货、代理、品牌四类业务的税务规划.md` | 已确认 |
| `25-inventory-turnover-cashflow-and-roe.md` | 专题页 | 经营财务与业财一体 | create-new；与战略财务互链 | `domains/财税与经营财务/02-经营财务与业财一体/06-存货周转、现金流与 ROE.md` | 是 |
| `26-case-anchor-library.md` | 案例库 | 课程包 | source-package + case-library；不作为正式理论页，保留课程案例索引并从各正式页反链 | `domains/财税与经营财务/90-课程包/01-财税股权28期/01-课程案例锚点库.md` | 是 |
| `27-compliance-transition-roadmap.md` | 路线图 | 电商财税合规 | create-new；与 03 页形成“原则 + 路线图”关系 | `domains/财税与经营财务/01-电商财税合规/08-合规转型路线图.md` | 是 |

## 5. 需要关联式融合的旧知识

当前检索发现，最明确的旧知识关联对象是。注意：这些旧知识不移动、不吞并，只在新知识中建立“相关记忆”链接，并在必要时从旧知识页反链。

| 旧知识页 | 融合关系 |
| --- | --- |
| `domains/电商运营/01-通用电商方法/03-平台结算与经营财务/01-电商平台结算时间口径财务核算方法.md` | 与收入确认、平台结算、快麦成本匹配、五平台账单核对高度相关。作为“收入确认、退货、补偿与平台补贴口径”和“业财一体与利润核算体系”的相关记忆。 |
| `domains/电商运营/02-淘宝天猫/01-淘宝运营速成指南/09-供应链、仓储与财务控制.md` | 与供应链、仓储、财务控制、库存、包裹触点相关。作为“资金、库存与权限内控”“存货周转、现金流与 ROE”的相关记忆。 |
| `domains/电商运营/02-淘宝天猫/01-淘宝运营速成指南/10-团队组织、招聘与绩效管理.md` | 与团队组织、绩效、股权激励相关。作为“电商团队激励、分红与预算联动”的相关记忆。 |
| `domains/电商运营/03-京东/01-京东自营入驻解析.md` | 涉及一般纳税人、13% 增值税专票、平台合作资质。作为“增值税进销项与发票管理”的相关记忆。 |

## 6. 本轮不建议做的事

- 不建议直接删除原 `learning-paths` 目录。先迁移正式页，再把旧目录改成来源包或保留重定向索引。
- 不建议把 27 个页面全部合成一篇长文。会降低 Agent 路由能力。
- 不建议只改标题不改结构。中文标题能缓解找不到的问题，但不能解决课程来源和内容归属混杂的问题。
- 不建议一次性重构所有 learning paths。先用财税股权试点，稳定规则后再处理品牌、视觉、电商运营其他路径。

## 7. 迁移执行顺序草案

1. Peter 确认是否新增 `domains/财税与经营财务/`。
2. Peter 确认上表的内容域和合并关系。
3. 创建目标目录和中文 domains/视觉制作/05-小红书风格AI生图/index。
4. 用脚本批量移动文件，并保留英文 slug/aliases。
5. 自动更新所有 `[[wikilinks]]`。
6. 更新 `/Users/pechen/wiki/domains/视觉制作/05-小红书风格AI生图/index.md`、`domains/电商运营/domains/视觉制作/05-小红书风格AI生图/index.md` 和新 domain domains/视觉制作/05-小红书风格AI生图/index。
7. 将旧 learning path 转为课程包入口或重定向页。
8. 跑 placeholder scan、链接搜索、代表性查询路由检查。

## 8. 待确认问题

1. 是否新增一级 domain：`domains/财税与经营财务/`，中文显示为“财税与经营财务”？
2. 是否接受中文文件名作为正式知识页默认命名？
3. `domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略/11-Agent使用模板：心智产品力与大单品诊断.md` 是否迁移到 `queries/电商企业财税股权诊断.md`？
4. `08` 和 `20` 两个激励页面是合并成一页，还是保留“激励总论/股权条件专题”两页？
5. `24` 四类业务税务规划更适合放“电商财税合规”，还是“内控与组织能力”？
