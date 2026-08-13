---
title: Agent与Skill执行协议
type: playbook
created: 2026-08-12
updated: 2026-08-12
domain: 视觉制作
tags: [visual-production, ai-video, ai-agent, skill, workflow]
sources:
  - _meta/extraction-notes/higgsfield-blockbuster-4k/audit-handoff.md
  - raw/assets/higgsfield-blockbuster-4k/downloads/higgsfield-seedance-prompt/SKILL.md
  - raw/webpages/higgsfield/blockbuster-4k-academy/higgsfield-blockbuster-4k-lessons-02-10-2026-08-12.md
  - raw/webpages/higgsfield/higgsfield-blockbuster-4k-case4k-2026-08-12.md
status: active
---

# Agent与Skill执行协议

## 未来 Skill 不应只是 Prompt 模板

它应管理从需求澄清到交付验收的主线，并把剧本访谈、资产登记、镜头编译、生成反馈和连续性 QA 作为可组合节点。Higgsfield 官方 Skill 主要覆盖“镜头任务→Seedance Prompt”，而我们未来的 Skill 需要覆盖更完整的生产系统。

## 主流程

```text
接收一句话/剧本
→ 访谈并锁定时长、世界、转折、对白和限制
→ 拆场景、节拍、镜头
→ 生成资产缺口与资产句柄表
→ 对每镜头选择最小引用集
→ 编译独立 Prompt
→ 生成后按可见问题诊断
→ 决定重生、补资产、补草图、混剪或删镜头
→ 连续性与成片 QA
→ 记录失败补丁，回到主线
```

## 节点合同

| 节点 | 输入 | 输出 | 失败时 |
| --- | --- | --- | --- |
| 剧本访谈 | 一句话、目标 | 已确认约束与剧本 | 继续提问，不擅自填关键空白 |
| 资产规划 | 剧本、镜头表 | 句柄表、状态版本、缺口 | 标记待补资产，阻止盲目生成 |
| 镜头编译 | 任务卡、最小引用集 | 单镜头 Prompt、验收点 | 简化镜头或请求草图 |
| 生成复盘 | 候选片段、目标 | 保留段、失败类型、修复动作 | 只修主失败，保留有效部分 |
| 成片 QA | 时间线、连续性表 | 通过/返工清单 | 返回对应节点，不全流程推倒 |

## 必须保存的中间状态

剧本版本、镜头 ID、资产句柄与状态、参考图职责、Prompt 版本、批次编号、选用时间段、失败类型、修复指令、前后镜头接口。没有这些状态，Agent 无法判断“什么已经锁定”，只会反复重写。

## 分支

- 缺少镜头角度：从真实参考最小改写生成关键帧，先验收结构再用于视频。
- 空间关系复杂：转入草图/导演台节点，完成后返回镜头编译。
- 对话轴线不稳：补地点反打资产，返回资产规划。
- 状态中途变化：新建角色状态版本，更新后续镜头引用。
- 单镜头约束过载：拆成可剪辑的多个自然镜头。

## 设计与验证要求

真正创建 Skill 时，以 `portable-skill-creator` 为治理入口；精确加载依赖，不把外部 Skill 复制进新 Skill；固定步骤优先交给 CLI/API/脚本；在干净会话中做正向与失败测试。官方原始 Skill 保持只读，见 `raw/assets/higgsfield-blockbuster-4k/downloads/official-skill-reference-index.md`。
