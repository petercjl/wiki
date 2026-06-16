---
title: 无限画板 Skill 写作 Agent 使用模板
type: domains/视觉制作/04-AI生图风格库/01-极简北欧风/variants/shanju-light-kitchen-living/playbook
created: 2026-06-11
updated: 2026-06-14
domain: AI Agent工程
tags: [ai-agent-engineering, skill, infinite-canvas, domains/视觉制作/domains/视觉制作/05-小红书风格AI生图/index/domains/视觉制作/05-小红书风格AI生图/index, prompt-engineering]
sources:
  - raw/my-temp-data/infinite-canvas-skill.md
  - /Users/pechen/.sealseek/workspaces/default/skills/skill-builder/SKILL.md
status: active
---

# 无限画板 Skill 写作 Agent 使用模板

本页规定未来 Agent 在创建或优化无限画板 skill 前，如何使用本知识库。

## 使用目标

减少重复沟通、重复踩坑和重复修正，让 Agent 在写新 skill 前自动吸收历史规则。

## 标准流程

### 1. 识别任务类型

先判断用户需求属于：

- 电商图片营销优化
- 风格迁移 + 产品保真
- 主图生成
- 详情页规划与分批生图
- 批量图片优化
- 电商主图视频
- 成套电商视觉生成
- 产品设计生图
- 其他混合流程

### 2. 读取知识库页面

最低读取：

1. [[domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/01-核心规则|核心规则]]
2. [[domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/02-工具规范|工具规范]]
3. [[domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/05-常见反坑库|常见反坑库]]
4. [[domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/06-质量检查清单|质量检查清单]]

按任务补读：

- 图像/视频/详情页/主图/成套视觉 → [[domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/03-任务范式|任务范式]]
- Prompt 设计 → [[domains/AI Agent工程/03-Skill设计/02-无限画板Skill写作知识库/04-Prompt模板|Prompt 模板]]

### 3. 输出规划

除非用户明确要求直接生成，先输出：

```markdown
【需求理解】
- 用户目标：
- 输入内容：
- 输出内容：
- 涉及能力：
- 复杂度判断：
- 用户指定模型：

【知识库命中】
- 任务范式：
- 需要遵守的核心规则：
- 主要反坑项：

【Skill 规划】
1. Skill 名称：
2. 触发条件：
3. 核心执行流程：
4. 工具使用策略：
5. Prompt 结构：
6. 输出方式：
7. 需要用户确认的点：

确认后，我再生成完整 skill.md。
```

### 4. 生成 skill.md

生成时必须把知识库命中的规则落进正文，而不是只在规划里提到。

尤其要检查：

- 是否使用正确工具。
- 是否显式传入默认模型。
- 是否设置产品保真约束。
- 是否设置批次和 QA。
- 是否设置失败/追问条件。

### 5. 优化已有 skill

优化时先判断问题来源：

| 问题表现 | 优先检查 |
| --- | --- |
| 产品变形 | 产品保真、reference_to_image prompt、是否复述产品细节 |
| 风格不统一 | 风格参考图角色、风格迁移规则、批次继承 |
| 文案乱/假 | 文案入图、营销真实性、图位任务 |
| 批量混乱 | 批次规则、每图独立处理 |
| 工具失败 | 工具参数、模型、分辨率、比例、不存在参数 |
| 视频不动/无镜头 | 视频 prompt 是否包含动作和镜头运动 |

遵守最小改动原则：只改和反馈相关的章节，不重写无关逻辑。

## Agent 自检句式

在生成前，Agent 应在内部确认：

```text
我是否把无限画板 skill 当成单文件 Markdown，而不是 SealSeek skill？
我是否先规划并等待确认？
我是否使用了真实工具和参数？
我是否避免了 reference_to_image 的产品细节复述？
我是否加入产品保真、营销真实性、批次和 QA 规则？
我是否把历史反坑项转成了本次 skill 的明确约束？
```

## 推荐查询入口

未来用户说：

- “帮我写一个无限画板 skill”
- “优化这个无限画板 skill”
- “之前这些坑不要再犯”
- “参考之前的无限画板 skill 规则”

Agent 应优先读取本页面和 domains/视觉制作/05-小红书风格AI生图/index，而不是只查 skill 注册库。
