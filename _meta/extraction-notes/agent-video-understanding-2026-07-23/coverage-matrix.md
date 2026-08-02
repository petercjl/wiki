---
title: Agent 视频理解覆盖矩阵
type: source-summary
created: 2026-07-23
updated: 2026-07-23
domain: meta
tags: [llm-wiki, coverage-matrix, video-understanding]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
status: active
---

# 覆盖矩阵

用户已于 2026-07-23 确认正式位置 `domains/AI Agent工程/09-多模态理解/`，35 个可复用知识单元已正式编译。

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| KU01 | S01-S12 总结 | 结论、时间范围、证据和置信度 | 核心方法 | `domains/AI Agent工程/09-多模态理解/01-Agent读懂视频的证据化架构.md` | formalized | 定义合格交付物与 Evidence Ledger |
| KU02 | S01-S03、S12 | 视频解复用与统一时间轴 | 核心方法 | `domains/AI Agent工程/09-多模态理解/01-Agent读懂视频的证据化架构.md` | formalized | 六层证据模型和 JSON 时间字段 |
| KU03 | S02、S05 | 均匀、场景、查询驱动采样 | 核心方法 | `domains/AI Agent工程/09-多模态理解/01-Agent读懂视频的证据化架构.md` | formalized | 三种采样的适用和组合 |
| KU04 | S01、S03-S05、S13 | ASR/OCR/视觉交叉校正 | 核心方法 | `domains/AI Agent工程/09-多模态理解/01-Agent读懂视频的证据化架构.md` | formalized | 含白模/白毛案例 |
| KU05 | S04-S11 | 按问题选择读取深度 | 路由规则 | `domains/AI Agent工程/09-多模态理解/01-Agent读懂视频的证据化架构.md` | formalized | D0-D4 深度表 |
| KU06 | S04-S11 | 区分事实、推断和解释 | 证据规则 | `domains/AI Agent工程/09-多模态理解/01-Agent读懂视频的证据化架构.md` | formalized | claim 状态和完成条件 |
| KU07 | S01-S05、S12 | 短视频完整证据包 | 短视频工作流 | `domains/AI Agent工程/09-多模态理解/02-短教学视频读取工作流.md` | formalized | 产物树与标准主线 |
| KU08 | S02、S13 | 开头 3—10 秒密集采样 | 采样规则 | `domains/AI Agent工程/09-多模态理解/02-短教学视频读取工作流.md` | formalized | 给出推荐采样密度 |
| KU09 | S01、S03、S13 | 术语必须跨通道校正 | 准确性规则 | `domains/AI Agent工程/09-多模态理解/02-短教学视频读取工作流.md` | formalized | 高风险词清单与纠错步骤 |
| KU10 | S13 | 问题—方法—步骤—案例—限制结构 | 编译模板 | `domains/AI Agent工程/09-多模态理解/02-短教学视频读取工作流.md` | formalized | 标准输出模板 |
| KU11 | S03、S13 | 平台 UI、字幕和内容 OCR 分层 | 解析规则 | `domains/AI Agent工程/09-多模态理解/02-短教学视频读取工作流.md` | formalized | 四类 OCR 文本 |
| KU12 | S05-S08、S10 | 长视频固定抽帧/压缩会漏证据 | 核心判断 | `domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索.md` | formalized | 一次性上下文失败原因 |
| KU13 | S05-S08 | 索引—检索—局部精读 | 长视频主线 | `domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索.md` | formalized | 离线建库和在线回答 |
| KU14 | S06-S08 | 字幕定位与视觉查询分工 | 工具路由 | `domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索.md` | formalized | 问题路由表 |
| KU15 | S05-S06、S08 | 有上限的迭代取证循环 | Agent 协议 | `domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索.md` | formalized | 3—5 轮与无新证据停止 |
| KU16 | S06-S08 | 缓存索引和 chunk 产物 | 复用规则 | `domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索.md` | formalized | course-index 目录协议 |
| KU17 | S07-S08 | 跨视频图/层级索引 | 扩展架构 | `domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索.md` | formalized | 图索引升级条件 |
| KU18 | S06-S08 | 摘要必须回链原始时间片 | 证据规则 | `domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索.md` | formalized | 回答要求 |
| KU19 | S10-S11、广告方法 | 故事目标与商业任务 | 广告 QA | `domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检.md` | formalized | 故事与商业线 |
| KU20 | S02、S04、S11 | 镜头级字段 | 广告 QA | `domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检.md` | formalized | 逐镜字段表 |
| KU21 | S10-S11 | 技术、美学、时序、AIGC 与业务分层 | 质量模型 | `domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检.md` | formalized | 五条读取线与严重度 |
| KU22 | S09 | 对象轨迹辅助连续性检查 | 专项工具 | `domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检.md` | formalized | 说明 SAM 2 能力边界 |
| KU23 | 参考图生成规则、S09 | 产品参考一致性逐镜核对 | 产品 QA | `domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检.md` | formalized | 参考为事实源，列出关系性核对项 |
| KU24 | S10-S11 | 目标检查表优于开放摘要 | QA 路由 | `domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检.md` | formalized | S0-S3 严重度 |
| KU25 | S10-S11 | 声音和画面共同构成叙事 | 多模态规则 | `domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检.md` | formalized | 五条读取线和两遍法 |
| KU26 | S01-S09、S12 | 可组合 CLI 能力面 | 实施规范 | `domains/AI Agent工程/09-多模态理解/05-Codex与SealSeek视频读取实现协议.md` | formalized | probe 到 qa 的命令边界 |
| KU27 | S01-S09、S12 | 共享文件型中间产物 | 跨 Agent 协议 | `domains/AI Agent工程/09-多模态理解/05-Codex与SealSeek视频读取实现协议.md` | formalized | manifest/scenes/transcript/OCR/ledger |
| KU28 | S05-S08 | 先定位再提取 | 执行规则 | `domains/AI Agent工程/09-多模态理解/05-Codex与SealSeek视频读取实现协议.md` | formalized | 主线与长视频局部读取 |
| KU29 | S01-S12 | 确定性工具、VLM、RAG、QA 分工 | 工具路由 | `domains/AI Agent工程/09-多模态理解/05-Codex与SealSeek视频读取实现协议.md` | formalized | Codex/SealSeek 角色和降级表 |
| KU30 | S01-S12 | 单一输出不可作为唯一判据 | 失败规则 | `domains/AI Agent工程/09-多模态理解/05-Codex与SealSeek视频读取实现协议.md` | formalized | 禁止静默降级 |
| KU31 | S01-S12 | 三类视频回归矩阵 | QA 规则 | `domains/AI Agent工程/09-多模态理解/05-Codex与SealSeek视频读取实现协议.md` | formalized | 九类失败样本 |
| KU32 | S10 | 查找、时间建模、跨时推理、音频利用 | 理解评测 | `domains/AI Agent工程/09-多模态理解/06-开源项目与技术选型.md` | formalized | Video-MME-v2 维度 |
| KU33 | S11 | 技术、美学、时序、AIGC 失真 | 质量评测 | `domains/AI Agent工程/09-多模态理解/06-开源项目与技术选型.md` | formalized | Q-Bench-Video 维度 |
| KU34 | S01-S12 | 采用、借鉴协议、专项、评测分级 | 选型规则 | `domains/AI Agent工程/09-多模态理解/06-开源项目与技术选型.md` | formalized | 12 项选型表 |
| KU35 | 用户 CLI 演进原则、S01-S12 | 成熟需求收敛到稳定 CLI | 演进规则 | `domains/AI Agent工程/09-多模态理解/06-开源项目与技术选型.md` | formalized | 部署门槛与实现协议互链 |
| S01-install | whisper.cpp README 安装/硬件章节 | 各平台编译、量化和加速细节 | 工具参考 | raw archive | raw-only | 本机已有可用 whisper-cli；运行前回查当前 README |
| S02-install | PySceneDetect README 安装章节 | 安装和 GUI 用法 | 工具参考 | raw archive | raw-only | 正式页只保留能力和接口位置，版本命令时效强 |
| S03-updates | PaddleOCR README 更新/榜单 | 版本新闻、排行榜、在线演示 | 项目宣传 | raw archive | raw-only | 与稳定架构无关且时效强 |
| S04-bench | Qwen3-VL README 性能榜单 | 各 benchmark 分数 | 模型评测 | raw archive | raw-only | 不把论文/官方榜单当本机实测 |
| S05-train | VideoITG 训练/数据章节 | checkpoint、训练数据、命令 | 研究复现 | raw archive | raw-only | 当前目标是借鉴选帧协议，不训练模型 |
| S06-train | LongVideoAgent 训练/数据章节 | GRPO 和 LongTVQA 训练流程 | 研究复现 | raw archive | raw-only | 当前目标是借鉴迭代取证协议 |
| S07-benchmark | VideoRAG LongerVideos | benchmark 构建和结果 | 研究评测 | raw archive | raw-only | 正式页只编译可迁移的索引/检索原则 |
| S08-framework | OmAgent 安装和示例项目 | 通用框架配置 | 框架参考 | raw archive | raw-only | SealSeek/OpenClaw 不必迁移到 OmAgent |
| S09-checkpoints | SAM 2 checkpoint/训练章节 | 权重、训练与数据集 | 研究复现 | raw archive | raw-only | 未获授权安装权重，知识库只保留跟踪用途 |
| S10-pipeline | Video-MME-v2 评测命令 | VLMEvalKit 命令和数据配置 | benchmark 复现 | raw archive | raw-only | 目前编译能力分类，不运行完整 benchmark |
| S11-pipeline | Q-Bench-Video 评测命令 | 数据下载和模型评测命令 | benchmark 复现 | raw archive | raw-only | 目前编译质量维度，不下载数据 |
| project-boilerplate | 11 个 README | citation、贡献、社区、star、license 展示 | 项目元信息 | raw archive | omitted-with-reason | 保留原文；正式知识页不复制导航和宣传内容 |
