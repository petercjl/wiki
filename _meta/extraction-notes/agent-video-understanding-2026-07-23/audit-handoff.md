---
title: Agent 视频理解开源资料审计交接
type: source-summary
created: 2026-07-23
updated: 2026-07-23
domain: meta
tags: [llm-wiki, audit-handoff, video-understanding]
sources:
  - raw/articles/agent-video-understanding-2026-07-23/
status: active
---

# Agent 视频理解开源资料审计交接

## Source

- Adapter: Markdown 文档、Web/GitHub 快照、PDF 文本抽取。
- Raw path: `raw/articles/agent-video-understanding-2026-07-23/`
- Original URL/path: 见 `source-manifest.md`。
- Capture date: 2026-07-23。
- Current-doc verification: Git commit 和抓取日期已记录；运行命令在使用前仍需回查。

## Outputs

- Source profile: `_meta/extraction-notes/agent-video-understanding-2026-07-23/source-profile.md`
- Source inventory: `_meta/extraction-notes/agent-video-understanding-2026-07-23/source-inventory.md`
- Knowledge-unit inventory: `_meta/extraction-notes/agent-video-understanding-2026-07-23/knowledge-unit-inventory.md`
- Semantic validation: `_meta/extraction-notes/agent-video-understanding-2026-07-23/semantic-validation.md`
- Coverage matrix: `_meta/extraction-notes/agent-video-understanding-2026-07-23/coverage-matrix.md`
- Omission audit: `_meta/extraction-notes/agent-video-understanding-2026-07-23/omission-audit.md`
- Formal page plan: `_meta/extraction-notes/agent-video-understanding-2026-07-23/formal-page-plan.md`
- Formal pages: `domains/AI Agent工程/09-多模态理解/` 下 1 个索引与 6 个正式页面；另有 `queries/Agent读懂视频入口.md`。

## Placement Confirmation

- Source understanding: 这是 Agent 视频理解的证据化架构、三类工作流和工具选型资料包。
- Existing category considered: `domains/AI Agent工程/` 与 `domains/视觉制作/06-AI视频/`。
- Recommended placement: `domains/AI Agent工程/09-多模态理解/`。
- Recommended disposition: 6 个正式知识页 + 1 个分类索引 + 1 个查询入口。
- Alternatives considered: AI 视频创作域；AI Agent 工具链单页。
- User confirmation: confirmed。
- Confirmation evidence: 用户于 2026-07-23 回复“可以的：domains/AI Agent工程/09-多模态理解/”。
- Final confirmed path: `domains/AI Agent工程/09-多模态理解/`。

## Coverage Summary

- Source units: 35 个可复用知识单元 + 12 类 raw-only/omitted 项。
- formalized: 35。
- merged: 0。
- raw-only: 11 类。
- omitted-with-reason: 1 类。
- unresolved: 0。

## Expected Agent Use

- Future questions this source should support: 如何读取短教程、长课、广告片；何时抽帧/OCR/转写/检索；如何让 Codex 和 SealSeek 共用证据；如何评测“读懂”。
- Pages an Agent should read first: 计划中的总架构页，再按视频类型进入场景页。
- Query/playbook entries: `queries/Agent读懂视频入口.md`。

## Known Risks

- Time-sensitive claims: 模型版本、安装命令、项目 API、benchmark 排名。
- Sensitive data removed: 无凭证；本机模型绝对路径只作为本机能力说明，不进入可移植 Skill。
- Weak source areas: 缺少三类视频的完整本机回归测试；研究模型未部署。
- User confirmation needed: 无。

## Self-Validation

- No formal write before placement confirmation: 是。
- Placeholder scan: passed；ingest validator 未发现占位符或过薄正文。
- Representative term search: passed；白模、Evidence Ledger、VideoITG、LongVideoAgent、VideoRAG、SAM 2、Video-MME-v2、Q-Bench-Video 均可在目标正式页检索。
- Index/log check: 已更新 AI Agent 工程、AI 视频、根索引和日志。
- Ingest contract: passed；`llm-wiki-ingest contract OK`。
- Route audit: passed；活动 Obsidian vault 为 `/Users/pechen/wiki`，查询入口有 3 个反向入口和 6 个正式页出口，分类索引有 2 个反向入口，无目标页警告。
- Remaining gaps: 无阻断项；研究模型仍未部署，已在正式页明确为能力边界。
