---
title: 拼多多运营基础视频来源档案
type: source-summary
created: 2026-07-12
updated: 2026-07-12
domain: meta
tags: [llm-wiki, ecommerce, pinduoduo]
sources:
  - raw/videos/pinduoduo-operations-foundations/
status: active
---

# 拼多多运营基础视频来源档案

- 来源类型：本地课程视频，中文口播、思维导图、手写算例混合。
- 已处理范围：ch00—ch09；其中 ch04 与 ch03 字节级完全重复。
- 本次新增原始路径：`/Users/pechen/拼多多/3.标签人群定义.mp4` 至 `9.平台核心规则红线认知.mp4`。
- 本次新增时长：ch03/ch04 各 00:11:54，ch05 00:04:03，ch06 00:05:59，ch07 00:09:25，ch08 00:10:44，ch09 00:19:32；去重后约 61 分钟。
- 媒体规格：1280×720，H.264 视频、AAC 音频。
- 处理日期：2026-07-12。
- ASR：whisper.cpp，`ggml-large-v3-turbo.bin`，中文提示词增强。
- OCR：Tesseract `chi_sim+eng`，每 15 秒抽帧。
- 文本脱敏：原视频保持不变；ASR、SRT、JSON 与 OCR 中可检索的来源名称、讲师身份、联系方式和水印已机械替换为中性占位符。
- 归属：`domains/电商运营/04-拼多多`。
- 组织原则：按知识点融合，不建立 learning path，不对应课程节次建页。
- 来源去标识：正式页、索引、查询入口、提取笔记和日志不保留讲师、课程品牌、联系方式、二维码及促销信息。
- 时效风险：平台算法为黑盒；视频中的 2026 年判断、广告产品和活动入口均需按当前后台复核。

## 融合结论

- `create-new`：拼多多平台流量结构与入口协同。
- `create-new`：拼多多链接权重与量率诊断模型。
- `create-new`：拼多多流量与权重诊断查询入口。
- `raw-only`：课程目的、适用对象、观看权益、课程模块目录、工具促销与服务销售信息。
- `duplicate-source`：ch04 与 ch03 SHA-256 均为 `89dab3c04051502844c3d6db0c5207621b3b00f2ec52e791fa7f30d2178913f9`，不按文件名虚构内容。
- `omitted-with-reason`：短期号码、购买号码、批量主体资源、错放类目抢流量等规避式做法不进入操作知识，仅转为合规风险。
