---
title: AI 生图主体比例与朝向控制方法论实验 audit handoff
type: source-summary
created: 2026-08-04
updated: 2026-08-04
domain: meta
tags: [llm-wiki, audit-handoff, visual-production, prompt-engineering]
sources:
  - raw/articles/ai-image-scale-direction-control-2026-08-04/01-original-study.md
  - raw/articles/ai-image-scale-direction-control-2026-08-04/02-cross-method-experiment.md
  - raw/articles/ai-image-scale-direction-control-2026-08-04/03-selfie-booth-validation.md
status: active
---

# AI 生图主体比例与朝向控制方法论实验 Audit Handoff

## Source

- Adapter: markdown-doc
- Raw path: `raw/articles/ai-image-scale-direction-control-2026-08-04/`
- Original paths: 见 `source-profile.md`
- Capture date: 2026-08-04
- Current-doc verification: not applicable；属于本地实验方法与当日模型能力快照

## Outputs

- Source profile: `source-profile.md`
- Source inventory: `source-inventory.md`
- Image inventory: `image-inventory.md`
- Image analysis: `image-analysis.md`
- Knowledge-unit inventory: `knowledge-unit-inventory.md`
- Coverage matrix: `coverage-matrix.md`
- Omission audit: `omission-audit.md`
- Formal page plan: `formal-page-plan.md`
- Formal pages:
  - `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md`
  - `queries/AI生图主体比例与朝向控制.md`
  - cross-links in existing image workflow, storyboard control, AI commercial visual query and indexes

## Placement Confirmation

- Source understanding: 通用 AI 生图比例、朝向、参考职责和能力边界方法；两种鞋子场景只是验证样本
- Existing category considered: `domains/视觉制作/03-AI商业视觉/`
- Recommended placement: `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md`
- Recommended disposition: create-new with cross-links
- Alternatives considered: `domains/视觉制作/06-AI视频/`，仅作为关键帧控制交叉入口
- User confirmation: confirmed
- Confirmation evidence: 用户在 2026-08-04 收到具体归位提案后回复“确认”
- Final confirmed path: `domains/视觉制作/03-AI商业视觉/05-AI生图主体比例与朝向控制方法.md`

## Coverage Summary

- Source units: 22
- formalized: 22
- merged: 0
- raw-only: 0
- omitted-with-reason: 0
- unresolved: 0
- Image coverage: 13 archived / 9 formalized / 0 merged / 4 raw-only / 0 unresolved / 9 embedded

## Expected Agent Use

- Future questions this source should support: 主体太大、产品比例失真、方向不听指令、朝向镜头、两对象动作关系错误、构图参考如何分工、关键帧尺寸不准
- Pages an Agent should read first: `queries/AI生图主体比例与朝向控制.md`，再读正式 playbook
- Query/playbook entries: `queries/AI生图主体比例与朝向控制.md`

## Known Risks

- Time-sensitive claims: 结论来自 2026-08-04 当前模型，未来模型可能提升数字/布局服从度
- Sensitive data removed: none
- Sensitive image handling: none
- Weak source areas: 每种方案多数仅 n=1，属于机制筛选，不是统计成功率
- User confirmation needed: none

## Self-Validation

- No formal write before placement confirmation: yes
- Ingest contract: passed；`run_ingest_validation.sh` exit 0
- Placeholder scan: passed by ingest validator
- Representative term search: passed；同平面、主角放大、9→3、抽象占位、动作相位、确定性合成和 n=1 边界均可检索
- Image validation: passed；9 张 formalized 图片均有耐久资产、正式嵌入和逐字语义锚点，4 张 raw-only 图片均有具体理由
- Route audit: passed；活动 Vault 与目标 Wiki 一致，查询入口有 4 个反向入口、4 个有效外链、无目标页警告
- Index/log check: passed；AI 商业视觉、视觉制作、根索引、AI 商业视觉查询入口和日志均已更新
- Diff check: passed；`git diff --check` 无输出
- Remaining gaps: none
