---
title: 可编辑海报 PSD 重建 Skill
type: playbook
created: 2026-06-15
updated: 2026-06-15
domain: 视觉制作
tags: [visual-production, ai-agent, skill, photoshop, psd, typography, ecommerce]
sources:
  - /Users/pechen/.codex/skills/editable-poster-psd-rebuild/SKILL.md
status: active
---

# 可编辑海报 PSD 重建 Skill

`editable-poster-psd-rebuild` 是一个 Codex skill，用于把 GPT Image 2 等 AI 生成的带文案电商海报，重建为可交给美工继续编辑的 PSD。

核心目的不是“复刻 AI 字体”，而是把 AI 图中的未知字体风险拆出来：AI 负责画面、光影和版式参考，Photoshop 负责用指定授权字体生成可编辑文字层。

## Skill 名称与位置

- Skill 名称：`editable-poster-psd-rebuild`
- Skill 文件：`/Users/pechen/.codex/skills/editable-poster-psd-rebuild/SKILL.md`
- 适用环境：Codex + Photoshop 2025 + 本机已安装默认字体

## 触发场景

当用户提出以下需求时优先使用：

- 把 AI 生成的带字电商海报变成可编辑 PSD。
- 去掉 GPT Image 2 图里的文案，再用指定字体重建文字层。
- 保留原图作为参考层，按原图版式重建文字。
- 避免 AI 生成图片中的未知字体带来商用侵权风险。

## 默认字体标准

当用户没有指定字体时，必须按以下默认标准执行：

```text
中文大标题 思源宋体 CN Regular
中文辅助文案 思源黑体 CN Regular
英文眉题 思源黑体 CN Regular
右上英文注释 思源黑体 CN Regular
```

默认英文字距：

```text
英文品牌字 / 英文眉题 / 英文注释：Photoshop tracking = 200
```

当前本机默认字体文件：

```text
/Library/Fonts/SourceHanSerifCN-Regular.otf
/Library/Fonts/SourceHanSansCN-Regular.otf
/Library/Fonts/SourceHanSansCN-Medium.otf
```

Photoshop 脚本名：

```text
SourceHanSerifCN-Regular
SourceHanSansCN-Regular
SourceHanSansCN-Medium
```

## 强约束

- 字体不存在时必须停止，不能自动 fallback 到系统字体。
- 不允许静默使用 Songti、PingFang、Helvetica、阿里字体等替代默认字体。
- 不允许把文字层栅格化后交付为“可编辑 PSD”。
- PSD 必须读回验证存在 Photoshop `type` 图层。
- 原始完整图必须作为隐藏参考层保留，方便美工对照。

## 工作流

1. 输入一张带文案海报图。
2. 用 GPT Image 2 仅移除文案，保留画面、光影、产品、人物、构图和比例。
3. 把原始完整图缩放到无文案底图尺寸，作为隐藏参考层。
4. 按原图版式写 `layout-spec.json`。
5. 使用默认字体标准或用户指定字体生成 Photoshop 原生文字层。
6. 保存 PSD，并导出 Photoshop 真实预览图。
7. 使用 `verify_psd_layers.py` 检查 PSD 中的 `type` 图层数量。

## 输出结构

典型输出目录包含：

```text
background-no-text.png
original-reference-resized.png
font-plan.json
layout-spec.json
editable-poster-rebuild.psd
editable-poster-rebuild-preview.png
psd-layer-report.json
```

PSD 图层结构：

```text
01 no-text gpt-image background
00 original complete image reference   # 默认隐藏
brand latin - ...
brand cn - ...
english eyebrow
headline line 1
headline line 2
support copy ...
bottom tagline ...
```

## 已验证样例

测试图片：

```text
/Users/pechen/Downloads/generated_1781416593194_b128f49b.png
```

输出：

```text
/Users/pechen/AI/Research/gpt-image-2-font-layout-test/skill-run-generated-1781416593194/editable-poster-rebuild-english-tracking-200.psd
```

验证结果：

- PSD 尺寸：`973 x 1616`
- 可编辑 Photoshop `type` 文字层：8 个
- 原始参考层：存在，默认隐藏
- 默认字体：思源宋体 CN Regular + 思源黑体 CN Regular
- 英文字距：`tracking = 200`

## 与其他页面关系

- [[domains/视觉制作/03-AI商业视觉/02-Codex与Photoshop协作自动化能力边界|Codex 与 Photoshop 协作自动化能力边界]]：记录 Codex 控制 Photoshop、PSD 和 OCR 的底层能力边界。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|Codex Skill 注册页]]：登记 skill 名称、位置和检索描述。
- [[domains/视觉制作/03-AI商业视觉/01-AI在商业视觉设计中的应用方法与实践/04-图片工作流：提示词结构与参考控制|图片工作流：提示词结构与参考控制]]：说明 AI 生图中参考图、提示词和可控后期的关系。

