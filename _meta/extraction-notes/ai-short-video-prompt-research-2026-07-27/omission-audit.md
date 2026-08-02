# Omission Audit

## Final Result

- Meaningful knowledge units found: 16
- Formalized knowledge units: 16
- Merged units: 0
- Raw-only units: 0
- Omitted-with-reason units: 0
- Unresolved units: 0

## Must-Keep Anchor Check

| anchor | preserved in inventory | formal requirement |
| --- | --- | --- |
| 最小必要提示词 | KU02 | 说明“简洁”不等于删除核心约束，且失败后才加最小补丁。 |
| 单镜头公式 | KU03 | 保留镜头、动作、结果、环境、声音、风格的字段关系。 |
| 5 秒不是硬限制 | KU04, KU13–KU14 | 明确镜头优先、约束负载假设与自然镜头拆分。 |
| 无 BGM 与三类声音 | KU05–KU06 | 区分环境声、人物声音和后期统一 BGM。 |
| 双镜头与显式运镜 | KU07–KU08 | 保留切镜和镜头路径需要明确写出的结论。 |
| 参考图职责 | KU09, KU15 | 保留身份/场景/关键构图/道具/风格分工与单变量测试。 |
| 15 秒剧情关系控制 | KU10–KU12 | 保留共享约束、对白对象、背景人流方向。 |
| 研究边界 | KU16 | 不把上游脚本、场景和资产规划误写成本页已经完成的内容。 |

## Interpretation Boundary

- “约束负载”是根据多个本机生成结果提出的编写与拆镜头启发式，不是对 Seedance 或其他闭源模型内部注意力、token 或算力配额的测量。
- “两张参考图更稳定”仅是一个观察；正式页要求单变量复测，不宣称参考图越少越好。
- 对具体模型的时长、参考图数量、音频接口与效果，不从本页推导当前产品规格；执行前仍需查看当前模型文档和实际结果。
