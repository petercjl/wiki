# Formal Page Plan

## Placement Confirmation

- Source understanding: HTML 生成能力的 CLI/Skill 单一来源、跨 Agent 安装，以及通用嵌套 Skill 组合协议。
- Existing category considered: `03-Skill设计` 有通用可移植性方法；本来源同时直接规定网页 HTML 执行入口，最常从网页报告任务检索。
- Recommended placement: `domains/AI Agent工程/11-网页设计规范/`
- Recommended disposition: create one execution/governance page and cross-link the existing UI query.
- Alternative considered: 独立放入 `03-Skill设计`；未采用，因为会切断网页报告执行入口，但正式页会链接通用 Skill 方法。
- User confirmation: confirmed
- Confirmation evidence: 用户 2026-08-06 明确指定网页设计规范目录，本轮继续要求把该规范写入知识库。
- Final confirmed path: `domains/AI Agent工程/11-网页设计规范/07-HTML生成CLI与伴生Skill组合规范.md`
- No formal write before confirmation: yes

## Outputs

| page | disposition | purpose |
| --- | --- | --- |
| 07-HTML生成CLI与伴生Skill组合规范.md | create-new | 单一源码、安装、嵌套调用、版本和 QA |
| 11-网页设计规范/index.md | extend-existing-with-section | 加入第七页读取入口 |
| queries/网页报告与SaaS界面设计入口.md | extend-existing-with-section | HTML 执行时先加载 CLI/Skill 协议 |
| domains/AI Agent工程/index.md | extend-existing-with-section | 域级路由 |
| index.md | extend-existing-with-section | 根级网页规范说明增加执行层 |

## Query Entry

- query-entry: update-existing
- page: `queries/网页报告与SaaS界面设计入口.md`
- reason: 现有入口已经覆盖 HTML 报告任务，不创建重复查询页。
