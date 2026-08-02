---
title: Agent 驱动型电商 CLI 开发入口
type: query
created: 2026-07-29
updated: 2026-07-29
domain: AI Agent工程
tags: [ai-agent, ecommerce, cli, query, toolchain]
sources:
  - raw/articles/agent-driven-ecommerce-cli-methodology-2026-07-29/source-evidence.md
  - _meta/extraction-notes/agent-driven-ecommerce-cli-methodology-2026-07-29/coverage-matrix.md
status: active
---

# Agent 驱动型电商 CLI 开发入口

## 何时使用

- “做一个淘宝、抖音、京东或1688的CLI。”
- “给现有电商CLI新增一个网页数据能力。”
- “让Agent知道这个CLI能做什么。”
- “把一次性网页探测整理成正式命令。”
- “设计电商CLI的登录、延时、风控和写入规范。”
- “把CLI发布到npm或交给同事安装。”
- “检查一个电商CLI是否达到可发布标准。”

## 必读顺序

1. [[domains/AI Agent工程/10-插件Skill与CLI/index|插件、Skill 与 CLI]]
2. [[domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范|Agent 驱动型电商 CLI 设计与开发规范]]
3. 如果准备封装为Plugin：[[domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论|Agent 插件架构与设计方法论]]
4. 如果准备改造为Codex插件：[[domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件|从 CLI 与 Skill 演进为 Codex 插件]]
5. 如果实施1688能力：[[domains/电商运营/07-1688/01-1688CLI/03-1688电商Skill执行安全与输出契约|1688 电商 Skill 执行安全与输出契约]]

## 标准执行步骤

1. 明确渠道、业务用户、自然语言目标和最终交付物。
2. 检查现有CLI的 `capabilities --json`，确认是新增能力还是已有能力。
3. 划分 Agent、CLI核心、渠道适配器和导出器职责。
4. 判断连接方式：官方API、浏览器登录态、页面结构化请求或其他已授权连接。
5. 先定义登录、随机延时、验证停止、错误码和完整性门。
6. 对写入能力确定风险等级、dry-run、确认、幂等、回读和审计。
7. 必要时使用开发模式探索，但需求稳定后折回正式命令。
8. 更新命令注册表、业务能力描述和自然语言示例。
9. 完成单元、契约、负向、打包、全新安装和真实小样本测试。
10. 通过PR、Release、CI和可信发布者完成分发。

## Agent 必须先问清的输入

- 目标电商渠道；
- 用户想完成的业务结果；
- 读取还是写入；
- 目标店铺、商品、订单、时间范围或页面链接；
- 交付格式；
- 是否已有CLI、仓库和稳定浏览器身份；
- 是否需要发布给其他用户。

## 标准输出

- 业务能力定义；
- 自然语言示例；
- 命令与参数契约；
- 渠道适配边界；
- 登录、延时、验证和写入安全规则；
- 数据与交付schema；
- 目录与模块设计；
- 测试矩阵；
- 新能力完成清单；
- 发布与升级方案。

## 强制边界

- 不绕过平台验证或风控。
- 不在未登录时继续请求。
- 每次数据请求与重试前必须经过随机延时和安全检查。
- 不把一次性探测当成正式能力。
- 不让Agent猜命令或解析不稳定日志。
- 不把部分数据、未知写入结果或错配展示值宣称为成功。
- 高影响写入必须显式确认并在提交后回读。
- 运行事实以当前CLI版本、能力注册表和测试结果为准。
