---
title: 《Film Directing Shot by Shot》重编译覆盖差额审计
type: source-summary
created: 2026-08-12
updated: 2026-08-12
domain: meta
tags: [llm-wiki, compile-audit, ai-video, directing]
sources:
  - raw/books/film-directing-shot-by-shot-2019/source.epub
  - _meta/extraction-notes/film-directing-shot-by-shot-2019/coverage-matrix.md
status: active
---

# 《Film Directing Shot by Shot》重编译覆盖差额审计

## 结论

现有正式页已经建立了可视化、故事板、制片周期、连续性、剪辑、场面调度、POV、移动摄影和转场等主题骨架，但不能据此认定原书已完成知识单元级覆盖。

证据：

- 原书正文目录包含 25 章，四个主部分。
- 四个主文本切分文件约 54 万字符。
- 现有覆盖矩阵的知识单元层只有 6 行：Visualization、Storyboards、Continuity、Camera Angles/POV、Moving Camera、Transitions。
- 原审计自己注明 chapter-level starter matrix 仍需扩展，却在 handoff 中把正式编译标为完成。
- 十个导演系统正式页合计约 3.4 万字节，具有实用价值，但大量原书例证、比较分支、选择条件和失败边界没有逐项登记。

因此本轮不覆盖或删除既有页面，而把它们视为第一版主题骨架；后续重新从 raw 建立细粒度 inventory，再决定扩展旧页或增加新页。

## 25章到新生产阶段的重编译批次

| 批次 | 原书章节 | 新结构主归属 | 重编译重点 |
| --- | --- | --- | --- |
| D1 | Introduction、1–5 | 02-导演思维、04-图片与控制资产 | 戏剧中心、可视化发现、概念图/技术图/故事板分工、预演工具、生产周期 |
| D2 | 6–7 | 03-分镜脚本、06-视频剪辑与连续性 | 空间连接、时间连接、因果、问题/答案、coverage 与剪辑选择 |
| D3 | 8–16 | 02-导演思维、03-分镜脚本 | 两人/三人/多人调度、移动调度、画面深度、机位、开放/封闭构图、POV |
| D4 | 17–25 | 03-分镜脚本、05-视频生成、06-视频剪辑与连续性 | pan、crane、tracking、运动编舞、转场、画幅、shadowing、现场补救与收束 |

## 无损规则

1. raw EPUB、章节文本和图片保持不变。
2. 既有十个导演系统页面不删除；新增知识优先扩展或在新阶段建立更可执行页面。
3. 每章重新建立知识单元、案例、决策条件、反例和 AI 迁移边界。
4. 重复与冲突先并列保存并标来源，清理留到用户指定的后续阶段。
5. AI 图片/视频 Prompt 的映射必须单独标注为知识库应用编译，不能伪装成原书内容。

## 当前优先级

先完成 D1，因为它直接回答“导演意图如何先于分镜”，并连接用户刚确认的视频方法；随后处理 D2，把导演决定落入分镜与剪辑；D3、D4 再补齐调度和移动摄影的细节。
