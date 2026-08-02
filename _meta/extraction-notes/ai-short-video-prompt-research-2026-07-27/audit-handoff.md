---
title: 本机 AI 短视频生成提示词研究审计交接
type: source-summary
created: 2026-07-27
updated: 2026-07-27
domain: meta
tags: [llm-wiki, audit-handoff, ai-video, prompt-engineering, research]
sources:
  - raw/articles/ai-short-video-prompt-research-2026-07-27/video-generation-prompt-research-log.raw.md
status: active
---

# 本机 AI 短视频生成提示词研究审计交接

## Source

- Adapter: markdown-doc
- Raw path: `raw/articles/ai-short-video-prompt-research-2026-07-27/video-generation-prompt-research-log.raw.md`
- Original path: `/Users/pechen/AI/Video/experiments/video-generation-prompt-research-log.md`
- Capture date: 2026-07-27
- Current-doc verification: 不包含模型价格、接口或时长规格；结论是本机工作流观察，具体模型能力须在执行时复核。

## Outputs

- Source profile: `source-profile.md`
- Source inventory: `source-inventory.md`
- Knowledge-unit inventory: `knowledge-unit-inventory.md`
- Coverage matrix: `coverage-matrix.md`
- Omission audit: `omission-audit.md`
- Formal page plan: `formal-page-plan.md`
- Formal pages:
  - `domains/视觉制作/06-AI视频/13-AI短视频生成提示词方法论：TVC与剧情短片.md`
  - `queries/AI视频导演与分镜入口.md`（路由扩展）

## Placement Confirmation

- Source understanding: 已具备人物、场景、道具和风格资产时，怎样针对 5 秒 TVC 与 15 秒剧情写可控短视频生成提示词。
- Existing category considered: `domains/视觉制作/06-AI视频/`
- Recommended placement: `domains/视觉制作/06-AI视频/13-AI短视频生成提示词方法论：TVC与剧情短片.md`
- Recommended disposition: create-new + extend-existing query
- Alternatives considered: 扩写 `12-AI视频Prompt分层强控方法.md`
- User confirmation: confirmed
- Confirmation evidence: 用户于 2026-07-27 回复“可以的 入库吧”。
- Final confirmed path: `domains/视觉制作/06-AI视频/13-AI短视频生成提示词方法论：TVC与剧情短片.md`

## Coverage Summary

- Source units: 16
- formalized: 16
- merged: 0
- raw-only: 0
- omitted-with-reason: 0
- unresolved: 0

## Expected Agent Use

- Future questions this source should support:
  - 一个素材段到底应该生成 5 秒、6 秒还是 15 秒？
  - 已有角色/场景/产品参考图后，如何写简洁而可控的生成 Prompt？
  - 15 秒剧情里多人关系、对白对象和背景行为如何不被漏掉？
  - 参考图应该增加还是删减？如何做可归因测试？
  - 怎样避免分段视频自带 BGM、同时维持人物音色？
- Pages an Agent should read first: `13-AI短视频生成提示词方法论：TVC与剧情短片.md`；需要理论诊断时再读 `12-AI视频Prompt分层强控方法.md`。
- Query/playbook entries: `queries/AI视频导演与分镜入口.md`

## Known Risks

- Time-sensitive claims: 本机模型能力与生成参数可能变化。
- Sensitive data removed: 正式页不公开本机下载路径、个人音频参考文件与生成文件名。
- Weak source areas: 没有固定随机种子和统计样本；“约束负载”和“额外参考图竞争”均为实用假设，需持续单变量复测。
- User confirmation needed: no

## Self-Validation

- No formal write before placement confirmation: yes
- Ingest contract: passed (`run_ingest_validation.sh`, Python 3.14.3)
- Placeholder scan: passed by ingest validator
- Representative term search: passed for `约束负载`、`自然镜头`、`不要任何背景音乐`、`参考图`、`对白` and the confirmed page title
- Route audit: passed for `queries/AI视频导演与分镜入口.md`; active vault equals target wiki, 6 backlinks, 22 outgoing links, no target warnings. Global orphan/dead-end totals are pre-existing vault-wide signals and were not attributed to this ingest.
- Index/log check: passed; formal page appears in AI 视频索引、根索引与既有 query，且根日志已追加。
- Remaining gaps: 下一阶段的产品/故事大纲到脚本、场景、资产生成流程未在本次编译范围内。
