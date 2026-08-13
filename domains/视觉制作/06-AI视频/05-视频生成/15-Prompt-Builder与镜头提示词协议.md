---
title: Prompt-Builder与镜头提示词协议
type: playbook
created: 2026-08-12
updated: 2026-08-12
domain: 视觉制作
tags: [visual-production, ai-video, prompt-engineering, skill]
sources:
  - _meta/extraction-notes/higgsfield-blockbuster-4k/blog-prompt-structure-analysis.md
  - raw/assets/higgsfield-blockbuster-4k/downloads/higgsfield-seedance-prompt/SKILL.md
  - raw/webpages/higgsfield/higgsfield-blockbuster-4k-case4k-2026-08-12.md
  - raw/webpages/higgsfield/blockbuster-4k-academy/higgsfield-blockbuster-4k-lessons-02-10-2026-08-12.md
status: active
---

# Prompt-Builder与镜头提示词协议

## 两层输入

参考资产负责“它是谁、长什么样、空间是什么”；文字负责“这次发生什么、摄影机如何看、哪些小细节不能丢”。已有清晰参考时，身份描述应最小化，避免用长文本重画角色或道具。

## 每个镜头是密封文件

视频生成通常不记得前一镜头。每条 Prompt 必须自足，但只包含当前镜头需要的内容：不写“同上”“继续上一幕”，不附未出场标签，不把全片摘要塞入当前镜头。连续性通过明确的起始状态、资产版本和结束状态传递。

## 固定主干，可选控制块

推荐顺序：

```text
SCENE CONTEXT
ACTIVE REFERENCES
LOCATION MAP（需要空间控制时）
FIRST FRAME / BLOCKING（需要构图和站位时）
FORMAT MODE
OPTICS / CAMERA
ACTION
PERFORMANCE（表演重要时）
PHYSICS
LIGHTING
COLOR GRADE / WARDROBE（需要时）
AUDIO
STYLE / OUTPUT SETTINGS（技术后缀，需要时）
POSITIVE LOCKS
```

所有案例都有主干，但不是所有镜头都应使用全部区块。控制粒度按任务选择：单一连续镜头、按顺序切镜、定时多镜头或自由 B-roll。复杂度来自镜头需要，而不是模板越长越专业。

## 写“可见、可测量、可验收”的事实

把“紧张”改成视线、停顿、握拳、呼吸和侧光；把“史诗”改成景别、距离、速度、规模比较和环境反应；把相机与主体运动分开写；把质量风险放到简短的正向锁定中。风格分布到负责它的区块：光在灯光，表演在表演，惯性和水花在物理，格式和颗粒放在末尾。

## 输入输出合同

输入：镜头任务卡、当前资产及句柄、目标时长/画幅、必须对白、已知失败风险。输出：一条可独立执行的镜头 Prompt，加上引用资产清单和生成后验收点。若站位、首帧、动作顺序或结尾含糊，Prompt-Builder 应先提问，不应自行填空。

官方 Skill 原文只作为结构研究样本，见 `raw/assets/higgsfield-blockbuster-4k/downloads/official-skill-reference-index.md`。
