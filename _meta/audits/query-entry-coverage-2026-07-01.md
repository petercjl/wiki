# Query Entry Coverage Audit

- audit_date: 2026-07-01
- wiki_root: `/Users/pechen/wiki`
- purpose: 检查 LLM Wiki 中 `queries/` 查询入口页是否足够支撑 Agent 路由。

## 结论

`queries/` 是当前 wiki 最重要的 Agent 路由层之一，但现有覆盖明显不足。

当前状态：

| 指标 | 数量 |
| --- | ---: |
| `domains/` 下 markdown 页面 | 约 438 |
| `queries/` 查询入口页 | 16 |
| 查询入口页中的 wikilink 出链 | 133 |
| 自动识别的高优先级候选路由点 | 157 |
| 已被 query 明确覆盖的高优先级候选 | 35 |
| 疑似缺少 query 入口的高优先级候选 | 98 |

说明：这个扫描是路由启发式审计，不是最终人工判定。它会把多页专题、Agent 使用模板、诊断页、SOP、Playbook 和领域 index 识别为候选入口，因此会有误报。但它足以说明：很多可复用知识已经编译成正式页，却没有一个 Agent 可以优先读取的查询入口卡。

## 已修正的流程规则

已在 LLM Wiki 相关 skill 中补充规则：

- `llm-wiki-ingest`：新增 **Query Entry Gate**，每次 ingest 必须判断是否需要 `queries/` 入口页；如果不需要，必须在 formal page plan 或 audit handoff 中记录 `query-entry: not-needed` 和理由。
- `llm-wiki-audit-and-optimization`：把缺少 query 入口纳入 route audit 和 post-ingest QA。
- `llm-wiki-recompile-runner`：修复/重组知识路径时，必须为 recurring task / diagnostic workflow / planning workflow / generation workflow / multi-page topic 补 query 入口，或记录不需要的理由。

已同步修改源仓库和当前安装副本：

- `/Users/pechen/.codex/skills/.llmwiki-source/skills/llm-wiki-ingest/SKILL.md`
- `/Users/pechen/.codex/skills/.llmwiki-source/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `/Users/pechen/.codex/skills/.llmwiki-source/skills/llm-wiki-recompile-runner/SKILL.md`
- `/Users/pechen/.codex/skills/llm-wiki-ingest/SKILL.md`
- `/Users/pechen/.codex/skills/llm-wiki-audit-and-optimization/SKILL.md`
- `/Users/pechen/.codex/skills/llm-wiki-recompile-runner/SKILL.md`

## 以后入库的 Query Entry Gate

创建或更新 query 入口页的条件：

1. 知识支持重复任务、诊断、规划、生成、比较、排障或 skill 创建。
2. 正式知识跨多个页面或目录。
3. Agent 需要特定读取顺序、边界条件或输出结构才能正确使用。
4. 用户未来更可能用自然语言提问，而不是精确说出页面标题。

query 入口页应该短而可执行：

- 触发语：什么时候用它。
- 读取顺序：先读哪些核心页。
- 分支页：特定场景才读哪些页。
- 边界：不能如何误用。
- 输出步骤：诊断、规划或生成时的标准结构。

## 现有高优先级缺口

优先补这些入口页，因为它们是多页专题、含 Agent 模板或明显支持重复任务。

### P0 / P1：Agent 经常会调用的能力区

| 建议 query 入口 | 当前核心路径 | 原因 |
| --- | --- | --- |
| Skill 设计与回归测试入口 | `domains/AI Agent工程/03-Skill设计/index.md` | 有多页 Skill 方法、注册表和 Agent 模板；未来创建/优化 skill 时非常常用。 |
| AI 视频导演与分镜入口 | `domains/视觉制作/06-AI视频/index.md` | AI 视频、导演知识、故事板、案例库已经很大，缺统一入口会让 Agent 乱读。 |
| AI 视频导演知识系统入口 | `domains/视觉制作/06-AI视频/20-导演知识系统/index.md` | 10 页导演知识，适合用 query 规定“脚本/分镜/运镜/prompt”读取顺序。 |
| 品牌策略诊断总入口 | `domains/品牌策略/index.md` | 品牌策略页很多，但缺一个总 query 把定位、品类心智、大单品、视觉资产、案例库串起来。 |
| 品牌案例库调用入口 | `domains/品牌策略/90-样本/index.md` | 案例库 20 页，Agent 需要知道按什么问题检索案例。 |
| 淘宝店铺运营诊断入口 | `domains/电商运营/02-淘宝天猫/01-淘宝运营速成指南/index.md` | 有 12 页淘宝运营基础和 Agent 模板，但没有 query 入口。 |
| 电商企业咨询诊断入口 | `domains/电商运营/01-通用电商方法/01-电商企业咨询与交付/index.md` | 11 页咨询交付方法，明显是重复诊断任务。 |
| 中小企业跨境出海诊断入口 | `domains/电商运营/20-跨境电商/01-中小企业跨境出海/index.md` | 8 页跨境出海系统，缺独立入口。 |
| 品牌视觉标准诊断入口 | `domains/视觉制作/02-品牌视觉标准化/01-可复制的电商品牌视觉玩法/index.md` | 8 页标准化系统和 Agent 模板，适合做独立 query。 |
| AI 商业视觉设计入口 | `domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践/index.md` | 7 页 AI 商业视觉方法，适合按任务路由。 |

### P1：已有专题但缺更细入口

| 建议 query 入口 | 当前核心路径 |
| --- | --- |
| 电商品牌增长诊断 | `domains/品牌策略/01-品牌基础与增长方法/01-电商品牌增长方法论/index.md` |
| 电商品牌竞争战略诊断 | `domains/品牌策略/02-品类心智与差异化/01-电商品牌竞争战略：品类心智与品牌打造/index.md` |
| 品牌差异化感知诊断 | `domains/品牌策略/02-品类心智与差异化/02-品牌差异化感知系统/index.md` |
| 细分品类品牌升级诊断 | `domains/品牌策略/02-品类心智与差异化/03-细分品类品牌升级与执行力落地/index.md` |
| 心智产品力与大单品诊断 | `domains/品牌策略/03-产品战略与大单品/01-电商品牌心智产品力与大单品战略/index.md` |
| 品牌大单品企划营销诊断 | `domains/品牌策略/03-产品战略与大单品/02-品牌大单品打造与产品企划营销/index.md` |
| 精益创业验证诊断 | `domains/品牌策略/03-产品战略与大单品/04-精益创业实战验证系统/index.md` |
| 商业模式诊断与重构 | `domains/品牌策略/03-产品战略与大单品/05-商业模式设计系统/index.md` |
| 选品与运营增长诊断 | `domains/电商运营/01-通用电商方法/04-选品与运营增长/01-电商运营与选品策略深度解析/index.md` |
| 平台入驻与自营合作诊断 | `domains/电商运营/01-通用电商方法/02-平台渠道与入驻合作/02-平台入驻与自营合作诊断模板.md` |

## 已有 query 入口示例

这些入口可以作为补齐其他 query 的模板：

- `queries/中国快递收费与物流成本诊断.md`
- `queries/产品开发与供应链管理诊断.md`
- `queries/产品类型与爆款运营诊断.md`
- `queries/淘宝全站推广诊断.md`
- `queries/淘宝智能推广与人群运营诊断.md`
- `queries/阿里巴巴国际站运营诊断.md`
- `queries/xiaohongshu-image-generation.md`

## 建议的补齐策略

不要一次性给所有页面创建 query。建议按“高频任务入口”批量补：

1. 先补 8-12 个 P0/P1 总入口页，让 Agent 能进入主要知识域。
2. 再为每个高频业务任务补细入口，比如“品牌差异化诊断”“AI 视频导演分镜”“淘宝店铺运营诊断”。
3. 后续每次 ingest 通过 Query Entry Gate 自动维护，不再靠事后补救。

