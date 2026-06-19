# Wiki Schema

## Domain

Peter 的个人 LLM Wiki，服务于 AI Agent 研发、电商运营、视觉制作、品牌策划、量化交易、SealSeek/玺承 BI/OpenClaw/Hermes 等项目知识沉淀。

## Architecture

采用“一库多域”架构：

- `domains/电商运营/`：电商运营。
- `domains/财税与经营财务/`：财税、经营财务、业财一体、股权激励和战略财务。
- `domains/视觉制作/`：视觉制作。
- `domains/品牌策略/`：品牌策略。
- `domains/AI Agent工程/`：AI Agent 工程、知识系统、Skill、工具链与自动化工作流。
- `domains/量化交易/`：量化交易平台、策略、回测兼容、数据 API 和交易 API。
- `shared/`：跨领域公共知识。
- `projects/`：具体项目资料。
- `entities/`：人、公司、产品、工具、Agent 等实体。
- `raw/`：原始资料，只读。
- `inbox/`：待整理输入。

## Frontmatter

```yaml
---
title: 页面标题
type: concept | entity | project | playbook | comparison | query | decision | source-summary
created: YYYY-MM-DD
updated: YYYY-MM-DD
domain: 电商运营 | 财税与经营财务 | 视觉制作 | 品牌策略 | AI Agent工程 | 量化交易 | shared | project | entity | meta
tags: [tag1, tag2]
sources:
  - raw/articles/example.md
status: active
---
```

## Page Placement Rules

- 长期专业能力：放 `domains/`。
- 跨领域底层知识：放 `shared/`。
- 具体项目上下文：放 `projects/`。
- 人、组织、产品、工具、Agent：放 `entities/`。
- 原始资料：放 `raw/`。
- 临时输入：放 `inbox/`。

## Tag Taxonomy

- ai-agent
- llm-wiki
- prompt-engineering
- skill
- context-engineering
- toolchain
- mcp
- automation
- ecommerce
- 财税与经营财务
- finance-accounting
- tax-compliance
- equity
- taobao
- tmall
- xicheng-bi
- sealseek
- product-design
- business-analysis
- courseware
- brand-strategy
- visual-production
- ai-agent-engineering
- codebase
- cli
- api
- quant-trading
- joinquant
- backtesting
- strategy
- browser-automation
- feishu
- gitee
- git
- data-pipeline
- knowledge-base
- obsidian
- workflow
- playbook
- decision
- comparison
- research

## Update Rules

- 新建正式页面后必须更新所属 domain 或目录的 `index.md`。
- 有意义修改后必须追加 `log.md`。
- 信息冲突时，不要静默覆盖；保留两个说法、标注来源和日期。
- 如果一次任务预计修改超过 10 个文件，先写计划并让 Peter 确认。
