---
title: 1688 牛顿Hub 电商 AI 技能库覆盖矩阵
type: source-summary
created: 2026-07-16
updated: 2026-07-16
domain: meta
tags: [llm-wiki, ecommerce, 1688, coverage]
sources:
  - raw/webpages/1688-clawhub-skill-library-2026-07-16/
status: active
---

# 覆盖矩阵

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| KU01 | S01 L13-L25 | 供应商查询意图与禁止项 | intent-and-guardrail | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | 供应商能力与禁止项已保留 |
| KU02 | S01 L27-L40 | 供应商查询命令与 reference 前置 | tool-contract | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | 命令和 reference 规则已保留 |
| KU03 | S01 L42-L64 | 供应商查询流程 | workflow | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 工作流 B |
| KU04 | S01 L65-L93 | 供应商输出完整性与示例 | output-contract | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 供应商输出契约 |
| KU05 | S01 L95-L120 | 供应商异常与读取风险 | error-and-risk | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 错误恢复与读取边界 |
| KU06 | S02 L15-L47 | 环境与 AK 安全 | environment-and-security | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | AK 与环境快照 |
| KU07 | S02 L49-L78 | 营销意图与工具 | intent-and-tools | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | 招商活动与商机能力 |
| KU08 | S02 L79-L113 | 报名与商机流程 | workflow | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 工作流 D |
| KU09 | S02 L115-L129 | 营销写入安全 | write-safety | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 活动报名确认门禁 |
| KU10 | S02 L130-L156 | 环境变量与埋点 | telemetry | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 环境与版本快照 |
| KU11 | S02 L158-L196 | reference 与 browser_use 授权 | progressive-disclosure-auth | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 运行包与授权流程 |
| KU12 | S02 L198-L231 | 营销异常与话术 | error-and-dialogue | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 错误恢复矩阵 |
| KU13 | S03 L11-L38 | 分销全局禁止项 | global-guardrail | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 全局禁止事项 |
| KU14 | S03 L42-L66 | 分销 AK 授权 | auth | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 分销授权差异 |
| KU15 | S03 L70-L97 | 分销意图与 reference 路由 | router | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 阶段路由和 reference 前置 |
| KU16 | S03 L101-L145 | 选品铺货工作流 | distribution-workflow | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 工作流 E |
| KU17 | S03 L149-L163 | 分销订单与催发 | order-workflow | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 工作流 F |
| KU18 | S03 L167-L199 | 知识检索与店铺查询 | knowledge-and-shop | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 店铺分支与 FAQ/reference 路由 |
| KU19 | S03 L203-L240 | 分销输出契约 | output-contract | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 分销输出契约 |
| KU20 | S03 L244-L273 | 分销工具与异常 | tool-and-error | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | 分销工具表；异常共性在安全页 |
| KU21 | S04 L15-L32 | 询盘工具与禁止项 | tool-and-guardrail | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | 采购询盘能力与边界 |
| KU22 | S04 L34-L93 | 采购旅程路由 | journey-router | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 阶段路由与典型判断 |
| KU23 | S04 L95-L110 | 询盘参数补齐 | parameter-workflow | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 工作流 C |
| KU24 | S04 L112-L152 | 询盘写入与异常 | write-and-error | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 确认门禁与错误恢复 |
| KU25 | S05 L15-L51 | 找货与比价路由 | search-router | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 工作流 A |
| KU26 | S05 L53-L78 | 找货工具与 reference | tool-contract | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | 商品搜索命令表 |
| KU27 | S05 L80-L102 | 比价工作流 | compare-workflow | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 一步比价与 TOP3 |
| KU28 | S05 L104-L136 | 输出与钉钉导出 | output-and-export | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 完整输出和 16 个导出字段 |
| KU29 | S05 L138-L162 | 找货异常与话术 | error-and-dialogue | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 错误恢复矩阵 |
| KU30 | S05 L166-L224 | 实现结构与版本历史 | implementation-history | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 环境、埋点、无状态和版本矛盾 |
| KU31 | S06 L15-L38 | 88 生意通工具与生命周期 | tool-and-lifecycle | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | 采购单命令与典型路径 |
| KU32 | S06 L40-L52 | 交易风险与二次确认 | risk-and-confirmation | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 风险与确认门禁 |
| KU33 | S06 L54-L89 | 交易异常与 reference | error-and-reference | domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约.md | formalized | 错误恢复与运行包规则 |
| KU34 | S06 L91-L104 | 业务限制与免责声明 | business-boundary | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | 主账号、采购单、支付边界 |
| KU35 | S07 L15-L36 | 店管家状态机 | shopkeeper-state-machine | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | 工作流 H |
| KU36 | S07 L38-L50 | 店管家 reference 与开店 | reference-and-onboarding | domains/电商运营/07-1688/01-1688CLI/02-从找货到采购铺货的意图路由与工作流.md | formalized | reference、AK、开店分支 |
| KU37 | S07 L52-L63 | 经营 FAQ 路由 | faq-router | domains/电商运营/07-1688/01-1688CLI/01-1688采购与分销Agent能力地图.md | formalized | FAQ 主题路由已保留 |
