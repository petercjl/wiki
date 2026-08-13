---
title: 产品销售型短视频剧本第一批 Audit Handoff
type: source-summary
created: 2026-08-13
updated: 2026-08-13
domain: meta
tags: [llm-wiki, audit-handoff, screenplay, advertising]
sources:
  - raw/webpages/ai-video-sales-screenwriting-2026-08-13/source-evidence.md
  - raw/articles/life-edge-chair-pillow-case-2026-08-13/source-manifest.md
status: active
---

# 产品销售型短视频剧本第一批 Audit Handoff

## Source

- Adapter: book 定向重编译 + web-clipping + mixed local case
- Raw path: `raw/books/` 三本既有书；`raw/webpages/ai-video-sales-screenwriting-2026-08-13/`；`raw/articles/life-edge-chair-pillow-case-2026-08-13/`；`raw/assets/life-edge-chair-pillow-case-2026-08-13/`。4 个 CDN 响应虽然原 URL 以 `.jpg` 结尾，二进制实际为 WebP；原始归档未改，另在 `normalized/` 保存正确后缀副本供正式页引用和格式校验。
- Original URL/path: 见 source-evidence 与 source-manifest
- Capture date: 2026-08-13
- Current-doc verification: 公开网页于 2026-08-13 在线读取；法规保留公布和施行日期。

## Outputs

- Source profile: `source-profile.md`
- Source inventory: `source-inventory.md` 与 raw source manifest
- Image inventory: `image-inventory.md`
- Image analysis: `image-analysis.md`
- Knowledge-unit inventory: `knowledge-unit-inventory.md`
- Coverage matrix: `coverage-matrix.md`
- Omission audit: `omission-audit.md`
- Formal page plan: `formal-page-plan.md`
- Formal pages: 7 个剧本方法页 + 1 个双路线案例页

## Placement Confirmation

- Source understanding: 产品销售型短视频从广告命题进入产品型 A/V 或故事型文学剧本。
- Existing category considered: `01-项目定义与剧本` 与 `90-案例库`。
- Recommended placement: 方法进入前者，固定案例进入后者。
- Recommended disposition: create-new；旧页只关联。
- Alternatives considered: 新建独立“商业剧本”子目录；当前数量尚不需要增加层级。
- User confirmation: confirmed
- Confirmation evidence: 2026-08-13 用户回复“好的 开始吧”。
- Final confirmed path: 见 formal-page-plan。

## Coverage Summary

- Source units: 25 类
- formalized: 20
- merged: 4
- raw-only: 1 个 GitHub 数据集候选；图片另计
- omitted-with-reason: 0（延后和排除项记录在 omission-audit）
- unresolved: 0
- Image coverage: 26 archived / 3 formalized / 0 merged / 23 raw-only / 0 unresolved / 3 embedded

## Expected Agent Use

- Future questions: 产品适合哪种剧本；文学剧本怎么写；TVC A/V 稿怎么写；如何写动作对白潜台词；如何改稿；同一产品两条路线有何不同。
- Pages an Agent should read first: `16-产品销售型短视频剧本双路线.md` 与 `22-Agent使用模板：产品销售型短视频剧本.md`。
- Query/playbook entries: `queries/AI短视频故事策划.md`。

## Known Risks

- Time-sensitive claims: 平台创意建议和法规需要执行前复核。
- Sensitive data removed: 无。
- Sensitive image handling: 无；商品图仅在私有 Wiki 使用。
- Weak source areas: 本批是定向重编，不等于三本电子书全量重编。
- User confirmation needed: 无。

## Self-Validation

- No formal write before placement confirmation: passed
- Ingest contract: passed；8 个新增正式页、3 类 durable raw、来源清单、覆盖矩阵和图片合同全部通过。
- Raw immutability: passed；`raw-baseline.sha256` 中 28 个首批原始文件逐一通过 SHA-256 复核。后增的 4 个规范 WebP 副本不替换原文件。
- Placeholder scan: passed；`01-项目定义与剧本` 20 页为 0 shell、0 skeleton、0 thin、20 OK。
- Representative term search: passed；A/V、文学剧本、改稿、潜台词和广告命题均能命中新增知识页。
- Index/log check: passed；剧本目录索引、案例索引、AI 视频总索引、查询页、Wiki 根索引和日志均已接入。
- Link audit: 8 个页面全部存在且有回链；11 个非图片 Wiki 链接全部解析。通用路由脚本把案例页 3 个图片嵌入报告为 unresolved，但三张图均存在且已通过图片合同，因此属于脚本把媒体当页面解析的已知误报。
- Duration check: 案例产品 TVC 时间码连续覆盖 `00:00–02:00`，结尾品牌段为 8 秒。
- Remaining gaps: 未来可补真实已发布 TVC 逐稿拆解、中文商业剧本行业样稿和可执行格式工具。
