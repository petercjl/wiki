---
title: Agent 视频理解来源清单
type: source-summary
created: 2026-07-23
updated: 2026-07-23
domain: meta
tags: [llm-wiki, source-inventory, video-understanding]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
status: active
---

# 来源清单

| ID | 来源 | 类型 | 主要贡献 | 主要限制 |
| --- | --- | --- | --- | --- |
| S01 | whisper.cpp README + Whisper 论文 | 项目/论文 | 本地 ASR、时间戳、VAD、多语种鲁棒转写 | 转写不是视觉理解；专有名词和同音词会错 |
| S02 | PySceneDetect README | 项目 | 内容/阈值式镜头切分，生成代表性场景单元 | 渐变、长镜头和屏录页面变化需要调参 |
| S03 | PaddleOCR README | 项目 | 中文字幕、PPT、UI、商品文字和文档结构识别 | OCR 需按区域/清晰度/语言做预处理 |
| S04 | Qwen3-VL README + 论文 | 项目/论文 | 原生视频、多图输入、可配置 FPS/帧数/视觉 token | “原生视频”仍受抽帧和上下文预算约束 |
| S05 | VideoITG README + 论文 | 项目/论文 | 先粗看后按指令定位时间片和关键帧 | 依赖可靠查询；非查询式通读仍需全局索引 |
| S06 | LongVideoAgent README + 论文 | 项目/论文 | 字幕定位、局部视觉查询、迭代证据轨迹 | 训练/完整实现较重，实际系统宜先复刻协议 |
| S07 | VideoRAG README + 论文 | 项目/论文 | 图索引、层级上下文、自适应检索、跨视频问答 | 构建索引有成本，不适合一次性短视频 |
| S08 | OmAgent README + 论文 | 项目/论文 | 图式多模态 Agent、分治、记忆和视频 QA | 框架较通用，需自行定义视频证据契约 |
| S09 | SAM 2 README + 论文 | 项目/论文 | 视频对象分割和跨帧跟踪 | 不能单独判断叙事、语义或产品是否正确 |
| S10 | Video-MME-v2 README + 论文 | 项目/论文 | 将理解拆成查找、时间建模、跨时推理并测音频作用 | Benchmark 不等于业务验收标准 |
| S11 | Q-Bench-Video README + 论文 | 项目/论文 | 技术、美学、时序、AIGC 失真和成对质量比较 | 偏感知质量，不能覆盖广告目标和品牌规范 |
| S12 | 既有 FFmpeg/ffprobe | 本机工具 | 解封装、转码、音轨/关键帧/时长/码率检查 | 不提供语义理解 |
| S13 | 本地抖音教学案例证据包 | 本机验证 | 展示 ASR、字幕、场景帧交叉读取的必要性 | 单案例，不能替代多类型回归测试 |

## 资料完整性

- GitHub 项目 README：11/11 已归档。
- 核心论文：9/9 PDF 与文本已归档，共 211 页。
- 模型权重与数据集：0，按研究边界未下载。
- 当前版本/运行可用性：仅核验项目文档与仓库，不宣称 11 个项目均已安装运行。
