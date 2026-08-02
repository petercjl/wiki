# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: ASR + OCR + burned-in subtitles + visual diagrams
- Evidence sources: original.mp4, transcript.raw.srt, 56 keyframes, 56 OCR files, repeated spoken context
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 00:38–00:45 | causal/technical | 有限计算部署 | 有限计算预算、有限步数 | frame 007–009 明示“有限步数，逐步收敛” + 语音上下文 | high | corrected | 用“有限计算预算/有限步数下的约束满足”，不声称具体采样步数 |
| A02 | 00:45–00:57 | definition | 语意 | 语义 | frame 011–012 的 semantic 标签 + 上下文 | high | corrected | 定义服从度的四维：语义、构图、运动、风格 |
| A03 | 00:57–01:09 | technical mechanism | 趋躁过程 | 去噪过程 | frame 013–014 明示“影响每一步去噪” | high | corrected | 用“影响每一步去噪” |
| A04 | 01:09–01:16 | technical concept | 高维语义相量 | 高维语义向量 | frame 013–016 图示与文本编码器上下文 | high | corrected | 用“高维语义向量” |
| A05 | 01:48–01:58 | conflict example | 35毫米广角感 / 面部特写；逆光剪影 / 清晰表情 | 维持原意 | frame 024 清晰列出两组 trade-off | high | accepted-as-is | 两组例子完整保留 |
| A06 | 02:06–02:10 | ordered framework | 三层 | 三个技术压力层面 | 后文依次列出文本编码、条件引导、时间维度 | high | accepted-as-is | 与后面的“三层写法”区分命名，避免混淆 |
| A07 | 02:14–02:26 | technical mechanism | Prompt在场；长距并列修饰；语异空间 | Prompt 再长；长句并列修饰；语义空间 | frame 027–031 + 语音上下文 | high | corrected | 用校正版，不修改 raw |
| A08 | 02:26–02:36 | signal granularity | 女声；细立度信号 | 女性；细粒度信号 | frame 027–031 明示“女生/细粒度信息” | high | corrected | 强/弱信号示例完整保留 |
| A09 | 02:36–03:03 | tool/mechanism | CFG | CFG（类似 classifier-free guidance 的条件引导） | frame 032–035 标题“CFG 像一根牵引绳” + 语音 | high | accepted-as-is | 作为通用解释；注明并非断言所有闭源模型实现一致 |
| A10 | frame 020–021 | numeric/diagram | 年龄8%、发型10%、服装14%、光线13%、焦段12%、运镜14%、表情12%、风格17% | 视觉示意数字，不是实验测量 | 图中总和 100%，无实验来源或口播论证 | high | excluded-from-formal | 保留“注意力/表达预算”概念，不把百分比写成事实 |
| A11 | 03:07–03:16 | comparison | 图片只需要一阵成立 | 图片只需要一帧成立 | frame 039–041 明示“一帧成立/连续成立” | high | corrected | 保留图片与视频的时间一致性对比 |
| A12 | 03:40–03:46 | ordered step | 硬约数 | 硬约束 | frame 043–050 明示“硬约束” | high | corrected | 第一层字段为主体、场景、动作、镜头目标 |
| A13 | 03:36–04:11 | ordered framework | 三个层级 | 硬约束 → 关键细节 → 风格控制 | frame 043–050 完整信息图 + 口播 | high | accepted-as-is | 保留顺序、字段和全部示例 |
| A14 | 04:17–04:24 | ordered step | 线索主体和构图 | 先锁主体和构图 | frame 052–054 流程图 | high | corrected | 复杂镜头工作流第一步 |
| A15 | 04:24–04:30 | control assets | 收尾针 | 首尾帧 | frame 052–054 “使用辅助控制”图示 + AI 视频语境 | high | corrected | 保留参考图、首尾帧、遮罩、后期校正四类手段 |
| A16 | 00:28–00:38 | testing method | AB测试 | A/B 测试 | 字幕与通用写法 | high | corrected | 作为经验验证方法，不虚构样本量 |

## Systematic Variant Search

- 已全文检索并统一解释 `部署/预算`、`趋躁/去噪`、`相量/向量`、`硬约数/硬约束`、`收尾针/首尾帧`。
- 原始 ASR 与 OCR 文件保持不变；所有校正仅进入 `normalized-transcript.md` 和后续正式页。
- 没有遗留会改变操作顺序、指标含义、否定关系或模型机制的低置信锚点。

## Scope Boundary

- 视频使用文本编码、交叉注意力、条件引导和 CFG 解释通用生成机制；正式知识应表述为“常见或类似机制”，不得据此断言每个闭源模型的实现细节。
- 信息图中的注意力百分比是示意，不是可复用参数。

