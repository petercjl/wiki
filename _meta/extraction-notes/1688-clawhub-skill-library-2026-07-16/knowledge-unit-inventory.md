---
title: 1688 牛顿Hub 电商 AI 技能库知识单元清单
type: source-summary
created: 2026-07-16
updated: 2026-07-16
domain: meta
tags: [llm-wiki, ecommerce, 1688, knowledge-unit]
sources:
  - raw/webpages/1688-clawhub-skill-library-2026-07-16/
status: active
---

# 知识单元清单

> 当前按可复用的业务/执行单元分组。正式编译时，每个单元中的命令、字段、条件、例外、示例和错误分支都必须在目标页可恢复。

| knowledge_unit_id | source_id | source_location | knowledge_role | 内容 |
| --- | --- | --- | --- | --- |
| KU01 | S01 | L13-L25 | intent-and-guardrail | 供应商/工厂/产业带查询触发语义；不编造、不改写关键词、数据与分析分层 |
| KU02 | S01 | L27-L40 | tool-contract | `ali_1688_source_suppliers`、`configure`、统一 JSON 输出、能力 reference 前置 |
| KU03 | S01 | L42-L64 | workflow | 提取关键词、缺参追问、执行查询、状态检查、追加官方供应商入口 |
| KU04 | S01 | L65-L93 | output-contract | 公司名称/合作方式/服务完整性、输出顺序和 JSON 示例 |
| KU05 | S01 | L95-L120 | error-and-risk | AK/参数/限流/服务异常矩阵；明确关键词时可直接读取 |
| KU06 | S02 | L15-L47 | environment-and-security | workspace 拷贝、Windows 权限、标准库依赖、AK 设备绑定加密与泄漏处置 |
| KU07 | S02 | L49-L78 | intent-and-tools | 招商活动、建议价、商机推荐意图边界和 6 个 CLI 能力 |
| KU08 | S02 | L79-L113 | workflow | 统一 JSON；活动查询→建议价→价格确认→提交报名；商机筛选与翻页 |
| KU09 | S02 | L115-L129 | write-safety | 只读/写入分级；报名必须先查建议价并由商家明确确认 |
| KU10 | S02 | L130-L156 | telemetry | Skill 环境变量、系统环境变量优先级、调用埋点及静默失败 |
| KU11 | S02 | L158-L196 | progressive-disclosure-auth | 每能力 reference 前置；`browser_use` 授权回调、localhost 端口和 300 秒时限 |
| KU12 | S02 | L198-L231 | error-and-dialogue | 鉴权、参数、限流、报名、JSON、投放类型、类目错误和参数补齐话术 |
| KU13 | S03 | L11-L38 | global-guardrail | 分销统一输出；不编造、不自动铺货、不铺未授权品牌、不改筛选、不浏览器降级、不猜命令 |
| KU14 | S03 | L42-L66 | auth | AK 存储、会话内状态检查、静默 browser_use 授权、手动兜底和重置 |
| KU15 | S03 | L70-L97 | router | 选品铺货、订单、知识、店铺、AK 重置的意图路由；各业务 reference 前置 |
| KU16 | S03 | L101-L145 | distribution-workflow | 选品超量请求策略、候选排序、分销参谋、品牌授权门禁、多店确认、铺货及续铺 |
| KU17 | S03 | L149-L163 | order-workflow | 默认当天订单、风险订单识别、按卖家催发、5-10 分钟后按 task_id 查回复 |
| KU18 | S03 | L167-L199 | knowledge-and-shop | query 原话传递、渠道/工具补齐、过期店铺过滤、绑店步骤与入口 |
| KU19 | S03 | L203-L240 | output-contract | 商品链接强制、卡片/表格阈值、品牌风险、铺货原样输出、订单展示模板 |
| KU20 | S03 | L244-L273 | tool-and-error | 8 个分销/订单/知识工具与异常矩阵；失败不旁路获取数据 |
| KU21 | S04 | L15-L32 | tool-and-guardrail | `procurement` 与 `configure`；禁止编造、禁止错路由、禁止浏览器/搜索降级 |
| KU22 | S04 | L34-L93 | journey-router | 模糊需求→商品搜索→供应商→询盘→下单旅程；确定性/动作/表述决策矩阵与边界例子 |
| KU23 | S04 | L95-L110 | parameter-workflow | `offerName`、纯数字 `count`、`demand` 的抽取与逐字段追问 |
| KU24 | S04 | L112-L152 | write-and-error | 采购询盘写入规则、reference 前置、鉴权/缺参/限流错误与引导话术 |
| KU25 | S05 | L15-L51 | search-router | 禁止项；文本、图片、链接、比价的触发边界与命令决策树 |
| KU26 | S05 | L53-L78 | tool-contract | 6 个工具、统一 JSON、每个能力对应 reference 前置 |
| KU27 | S05 | L80-L102 | compare-workflow | 直接比价一步到位、选品后从结果取图、默认 TOP3、明确比价意图才用 compare |
| KU28 | S05 | L104-L136 | output-and-export | 完整表格不可截断/改写；详情链接；钉钉表格 16 个导出字段；禁用商品墙说明 |
| KU29 | S05 | L138-L162 | error-and-dialogue | AK、401、图片、主图、限流、HTTP500、权限错误；不得网页搜索兜底；补参话术 |
| KU30 | S05 | L166-L224 | implementation-history | 环境变量、埋点、文件清单、无状态上下文拼接、v1.0-v1.7 版本能力变化 |
| KU31 | S06 | L15-L38 | tool-and-lifecycle | 12 个账号/采购单/配置能力与典型采购单状态路径 |
| KU32 | S06 | L40-L52 | risk-and-confirmation | 只读/配置/写入分级；资金与状态变化二次确认；写后查询最新状态 |
| KU33 | S06 | L54-L89 | error-and-reference | AK、主账号、签约实名绑卡、限流错误；每能力 reference；通用规则硬约束 |
| KU34 | S06 | L91-L104 | business-boundary | 仅主账号、仅采购单、支付转网页、角色同义与免责声明 |
| KU35 | S07 | L15-L36 | shopkeeper-state-machine | `search/shops/publish/configure/check`；check 后按 AK、店铺数、授权过期状态分支 |
| KU36 | S07 | L38-L50 | reference-and-onboarding | 搜索/铺货/配置 reference 前置；AK 获取和一键开店引导 |
| KU37 | S07 | L52-L63 | faq-router | 平台选择、选品、定价、履约、售后、新店、内容合规按需加载 reference |
