---
title: Codex与SealSeek视频读取实现协议
type: playbook
created: 2026-07-23
updated: 2026-07-23
domain: AI Agent工程
tags: [ai-agent, codex, sealseek, openclaw, cli, video-understanding]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
  - _meta/extraction-notes/agent-video-understanding-2026-07-23/coverage-matrix.md
status: active
---

# Codex 与 SealSeek 视频读取实现协议

目标是让 Codex 与 SealSeek/OpenClaw 使用相同的中间产物和证据口径。Agent 框架可以不同，视频事实不能因框架更换而重算或漂移。

## 稳定执行面

长期重复使用时，应收敛为稳定 CLI，而不是保留大量一次性脚本。推荐能力拆分：

```text
video-reader probe <video>
video-reader transcribe <video>
video-reader detect-scenes <video>
video-reader extract-frames <video> [--strategy ...]
video-reader ocr <frames-or-video>
video-reader build-index <video-or-course>
video-reader query <index> --question "..."
video-reader qa <video> --goal <goal-file>
video-reader inspect <artifact-dir>
```

“定位目标”和“提取/分析目标”应是不同命令，使长视频工作流可以先检索再局部读取。

## 中立文件协议

### manifest.json

```json
{
  "schema_version": "1.0",
  "source": {"path": "...", "sha256": "..."},
  "media": {"duration_ms": 100080, "width": 1080, "height": 1920, "fps": 25},
  "tools": [{"name": "whisper-cli", "version": "...", "model": "local-model-id"}],
  "strategies": {"frames": "scene+dense-opening+uniform-fallback"},
  "artifacts": {"transcript": "transcript.srt", "scenes": "scenes.json"}
}
```

知识库或可分享 Skill 不应硬编码私人绝对路径；manifest 实例可以记录本机实际路径。

### scenes.json

每个场景至少有 `scene_id/start_ms/end_ms/representative_frames/detection_method`。

### transcript

SRT/VTT 供人阅读；JSONL 保存时间、文本、语言、置信度和说话人候选。

### ocr.jsonl

保存时间、区域、文本、置信度、图像路径和文本类别：`subtitle/ui/content/promo/unknown`。

### evidence-ledger.jsonl

```json
{
  "claim_id": "C07",
  "claim": "作者先展示线稿失败，再展示白模方案",
  "status": "confirmed",
  "evidence": [
    {"start_ms": 8100, "end_ms": 24500, "types": ["asr", "ocr", "frame"]}
  ],
  "notes": "术语已由字幕纠正"
}
```

## Agent 主线

1. 接收视频、问题和目标契约。
2. 检查是否存在同 SHA-256 的完整证据包。
3. `probe`，决定读取深度。
4. 执行必要的 ASR、场景、帧和 OCR 节点。
5. 长视频先 `build-index/query`，再读取候选片段。
6. 写证据账本，不在最终回答阶段临时编造证据。
7. 检查完成条件、冲突和未读取范围。
8. 输出报告和可复用产物。

异常处理后必须回到主线对应节点。

## Codex 的实现方式

Codex 擅长：

- 检查本机工具和文件；
- 调用 FFmpeg、whisper.cpp、OCR、Python/Node 解析器；
- 生成联系表、JSON、Markdown 和知识库；
- 根据目标读取关键帧并追踪证据；
- 扩展稳定 CLI、补测试和维护 Skill。

读取本地视频时应优先使用本机已有工具和模型；不要为了“可能更好”自动下载大模型。

## SealSeek/OpenClaw 的实现方式

SealSeek 适合作为长期对话和工作流入口：

- Skill 负责意图路由、主线、失败分支和输出契约；
- CLI 负责确定性媒体处理；
- Agent/VLM 负责解释候选证据；
- session memory 只保存任务状态，不替代文件型证据；
- 通过 `/Users/pechen/bin/sealseek-chat` 做干净会话回归时，应验证产物而不只看回答文本。

SealSeek 不必复刻 Codex 的内部工具调用；两者只需遵守同一 manifest 和 evidence ledger。

## 工具失败与降级

| 失败 | 合法降级 | 必须披露 |
| --- | --- | --- |
| ASR 不可用 | 只做 OCR/视觉读取 | 未读取语音内容 |
| OCR 不可用 | 人工/视觉模型读取关键帧 | 文字可能漏识别 |
| 场景检测失败 | 均匀采样 + 页面变化兜底 | 镜头边界不可靠 |
| VLM 不可用 | 生成证据包，暂停语义解释 | 只完成预处理 |
| 对象跟踪不可用 | 逐镜参考图人工比对 | 未做跨帧轨迹 |
| 长视频索引损坏 | 重建受影响 chunk | 哪些范围未恢复 |

不允许静默把“完整视频理解”降级成“只读转写”。

## 停止条件

- 核心问题均有直接证据或被标为无法确认；
- 连续一轮没有产生新候选或新证据；
- 达到工具/轮数预算；
- 所有高严重度冲突已复核；
- 产物通过结构检查，路径可读。

## 回归测试矩阵

至少保留：

- 有字幕、术语密集的短教程；
- 无字幕口播；
- 快切短视频；
- 两小时课程中的稀疏关键证据；
- 静音/音乐段，防止 ASR 幻觉；
- 故事广告角色连续性；
- 产品广告参考图一致性；
- 画中 UI 与平台 UI 混合；
- 可变帧率或旋转视频。

每次更换 ASR、OCR、场景算法或 VLM 后，比较证据覆盖、时间定位和误报，而不只比较摘要文字。

## 相关页面

- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
- [[domains/AI Agent工程/07-评测与调试/01-AI Agent执行链路审计方法|AI Agent 执行链路审计方法]]
- [[domains/AI Agent工程/09-多模态理解/06-开源项目与技术选型|开源项目与技术选型]]

