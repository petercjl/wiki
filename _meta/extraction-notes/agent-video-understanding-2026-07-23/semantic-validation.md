---
title: Agent 视频理解资料语义校验
type: source-summary
created: 2026-07-23
updated: 2026-07-23
domain: meta
tags: [llm-wiki, semantic-validation, video-understanding]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
status: active
---

# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: PDF machine extraction、GitHub README 与本地案例 ASR
- Evidence sources: 9 篇原始 PDF、逐页文本、11 个项目 README、案例 SRT、联系表和视频标题上下文
- Systematic variant search: passed；已在全部论文文本、README、案例 SRT 和正式页面检索下列项目名与纠错词形
- Formal text checked against normalized anchors: passed；正式页面使用项目官方写法，并将案例 ASR 的“白毛”规范为有画面证据支持的“白模”

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | case-study SRT lines 7-131 | technical-term | 3D白毛故事版 / 白毛风格 | 3D 白模故事板 / 白模风格 | 视频标题明确写“3D白模风格”；联系表显示灰白无材质 3D 故事板；6 处语境均讨论模型体块与空间关系 | high | corrected | 正式页只使用“3D 白模故事板”，原 SRT 保持不变 |
| A02 | Whisper PDF title + whisper.cpp README | platform-or-product | Whisper / whisper.cpp | Whisper / whisper.cpp | 论文标题和项目 README 双重一致 | high | accepted-as-is | 论文模型与 C++ 实现分别按官方名称书写 |
| A03 | Qwen3-VL PDF title + README | platform-or-product | Qwen3-VL | Qwen3-VL | 论文标题与官方仓库 README 一致 | high | accepted-as-is | 使用官方连字符和大小写 |
| A04 | VideoITG PDF title + README | platform-or-product | VideoITG | VideoITG | 论文标题、GitHub 项目名和方法章节一致 | high | accepted-as-is | 使用官方名称；不把论文榜单写成本机实测 |
| A05 | LongVideoAgent PDF title + README | platform-or-product | LongVideoAgent | LongVideoAgent | PDF 与中英文 README 一致 | high | accepted-as-is | 使用官方名称；采用其迭代取证协议 |
| A06 | VideoRAG PDF title + README | platform-or-product | VideoRAG | VideoRAG | PDF 与 README 一致 | high | accepted-as-is | 使用官方名称；区分项目算法与通用 video RAG 概念 |
| A07 | OmAgent PDF title + README | platform-or-product | OmAgent | OmAgent | PDF、GitHub URL 与 README 一致 | high | accepted-as-is | 使用官方大小写 |
| A08 | SAM 2 PDF title + README | platform-or-product | SAM 2 | SAM 2 | 论文标题与 Meta 官方 README 一致 | high | accepted-as-is | 使用带空格的官方名称 |
| A09 | Video-MME-v2 PDF title + README | platform-or-product | Video-MME-v2 / Video-MME v2 | Video-MME-v2 | 官方仓库名和 README 标题支持带连字符写法 | high | accepted-as-is | 项目名统一为 Video-MME-v2，论文语境不改变 |
| A10 | Q-Bench-Video PDF title + README | platform-or-product | Q-Bench-Video | Q-Bench-Video | PDF 和 README 一致 | high | accepted-as-is | 使用官方名称 |
| A11 | Qwen3-VL README video processor | metric-or-limit | default fps=2、视觉 token 示例预算 | 可配置 FPS/帧数/token 预算 | README 明确这些是默认值或示例参数，不是所有视频的最佳固定值 | high | accepted-as-is | 正式页只说明可配置与预算约束，不把示例值写成通用标准 |
| A12 | LongVideoAgent README method | ordered-step | request_grounding → visual_query → answer | 字幕定位 → 局部视觉查询 → 证据充分后回答 | 中英文 README 的迭代循环和论文方法一致 | high | accepted-as-is | 编译成框架中立协议，不声称已部署其训练模型 |
| A13 | VideoITG README frame selection | ordered-step | 512 → sort → Top-K | 粗筛大量帧 → 按查询排序 → 精读 Top-K | README “How frame selection works”与论文方法一致 | high | accepted-as-is | 正式页保留机制，不把 512 固化为本机阈值 |
| A14 | Video-MME-v2 paper/README | evaluation-dimension | finding information / modeling time / cross-temporal reasoning | 信息查找 / 时间建模 / 跨时推理 | 论文与 README 的能力雷达说明一致 | high | accepted-as-is | 作为评测维度，不把 benchmark 分数写成业务结果 |
| A15 | Q-Bench-Video paper/README | evaluation-dimension | technical / aesthetic / temporal / AIGC distortions | 技术 / 美学 / 时序 / AIGC 特有失真 | 论文任务定义和 README 构建说明一致 | high | accepted-as-is | 作为质量分类，仍叠加广告业务目标 |

## 校验结论

- 原始 PDF 文本和案例 ASR 未被覆写。
- 项目名均由论文标题和官方 README 双重核对。
- 数字、榜单、checkpoint 与训练参数没有被编译为本机实测或默认生产配置。
- 唯一系统性词形纠错是案例 SRT 中 6 处“白毛”→“白模”；正式页不使用未经支持的 ASR 原词。
