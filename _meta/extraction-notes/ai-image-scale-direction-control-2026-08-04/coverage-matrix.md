# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| KU01 | S01/问题一 | 主体放大先验与模糊比例词失败 | failure-mode | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 见“为什么真实比例通常无效” |
| KU02 | S01/2.2 + S02/A-D | 孤立数字不是硬约束 | limitation | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 已保留焦距、距离、百分比和抽象框边界 |
| KU03 | S01/2.3 | 常识参照关系锚定比例 | principle | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 见比例控制栈 |
| KU04 | S02/3.2 + S03 | 同平面尺度锚点 | decision-rule | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 明确同平面优先于孤立前景物 |
| KU05 | S01/2.3 + S02/3.2 | 连续透视尺度链 | method | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 近景→锚点→主体→远景 |
| KU06 | S02/3.2 + S03 | 画布占位只是保险线 | limitation | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | Prompt 模板与控制分级均保留 |
| KU07 | S01/问题二 | 世界方向语言存在歧义 | failure-mode | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 见朝向控制导言 |
| KU08 | S01/3.3 + S02/3.3 | 画布坐标与运动向量 | principle | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | +x、9→3 点和箭头示例 |
| KU09 | S02/3.3 | 主体自身轴与角度容差 | method | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 后端→前端轴与 ±5° 模板 |
| KU10 | S01/3.3 + S02/3.3 | 环境线与指定可见面 | method | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 朝向控制栈与通用句式 |
| KU11 | S01/3.3 + S02/3.4 | 多对象动作角色分解 | method | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 对象 A/B 动作阶段模板 |
| KU12 | S02/3.1 | 多参考图职责与优先级 | workflow | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 四类参考职责表与冲突优先级 |
| KU13 | S01 + S02 | 原始身份图与关系锁定 | safety-rule | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 与既有图片工作流双向链接 |
| KU14 | S02/A-C | 真实构图参考改善比例 | experimental-finding | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | IMG04/IMG06 对照 |
| KU15 | S02/D | 无构图参考时主体再度放大 | experimental-finding | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | IMG08 反证 |
| KU16 | S02/E | 抽象控制图不锁尺寸 | experimental-finding | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | IMG09 反证 |
| KU17 | S03 | 自拍机场景跨场景迁移成功 | validation | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | IMG10/IMG12/IMG13 对照 |
| KU18 | S03 | 门洞物理比例未严格命中 | limitation | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 跨场景回归边界 |
| KU19 | S03 | 方向比动作相位稳定 | limitation | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 朝向与动作分开验收 |
| KU20 | S02/结论 | 软控、稳定控、像素级控制三档 | decision-framework | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | 控制强度分级表 |
| KU21 | S02/4 | 可复用 Prompt 模板 | reusable-template | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md`; `queries/AI生图主体比例与朝向控制.md` | formalized | 正式页保留完整模板，查询页保留执行结构 |
| KU22 | S02/6 | 跨主体重复采样 QA | qa-method | `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md` | formalized | QA 指标与 n=1 边界 |

