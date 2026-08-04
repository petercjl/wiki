---
title: AI Agent 工程知识域
type: concept
created: 2026-06-14
updated: 2026-08-03
domain: AI Agent工程
tags: [ai-agent-engineering, index]
sources:
  - raw/articles/company-shared-gpu-worker-2026-07-24/observed-system-evidence.md
  - _meta/extraction-notes/company-shared-gpu-worker-2026-07-24/coverage-matrix.md
  - raw/articles/agent-driven-ecommerce-cli-methodology-2026-07-29/source-evidence.md
  - _meta/extraction-notes/agent-driven-ecommerce-cli-methodology-2026-07-29/coverage-matrix.md
  - raw/webpages/word-document-format-design-research-2026-07-30/
  - _meta/extraction-notes/word-document-format-design-research-2026-07-30/coverage-matrix.md
  - raw/articles/gigsgigscloud-shadowsocks-node-2026-08-03/source-evidence.md
  - _meta/extraction-notes/gigsgigscloud-shadowsocks-node-2026-08-03/coverage-matrix.md
status: active
---

# AI Agent 工程知识域

本目录沉淀可跨项目复用的 AI Agent / LLM / 知识系统 / 自动化工程方法，而不是某个单一项目的配置细节。

## 适用范围

- 多 Agent 协作
- LLM Wiki 与知识系统
- Skill 设计与上下文工程
- Agent 插件封装、分发与治理
- CLI / MCP / 浏览器 / API 工具链
- 自动化工作流与评测调试

## 子主题

- `01-知识系统/`：个人知识库、LLM Wiki、Obsidian、知识编译与维护。
- `02-Agent架构/`：Agent 分工、memory、tool orchestration、多 Agent 结构。
- `03-Skill设计/`：Skill 设计、状态机、执行契约、工作流抽象。
- `04-提示词与上下文/`：提示词结构、上下文注入、长期记忆和规则文件。
- `05-工具链/`：CLI、MCP、Git、浏览器自动化、API 组合方式。
- `06-自动化工作流/`：可执行的多步自动化流程。
- `07-评测与调试/`：质量门、lint、回归测试、故障定位。
- `08-插件工程/`：Plugin、CLI、Skill、MCP、Connector、Hook 的封装、治理与分发。
- `09-多模态理解/`：Agent 对视频等多模态资料的证据化读取、检索、推理与质量验收。
- `格式化文档/`：Agent 对 Word、PDF、电子表格、演示文稿和在线文档的结构化、格式化与质量验收；当前先建立 Word 体系。
- `90-Skill注册表/`：由同步脚本生成的跨 Agent skill 检索资产。

## 知识系统

- [[domains/AI Agent工程/01-知识系统/domains/视觉制作/05-小红书风格AI生图/index|知识系统]]：个人知识库、LLM Wiki、Obsidian、知识编译与维护相关方法入口。
- [[domains/AI Agent工程/01-知识系统/01-LLM Wiki个人知识库运行闭环|LLM Wiki 个人知识库运行闭环]]：用 Ingest / Query / Lint 三个动作，把知识库从“资料堆”变成持续复利的个人知识系统。

## Skill 设计

- [[domains/AI Agent工程/03-Skill设计/index|Skill 设计]]：Agent skill 的设计、测试、演化和注册方法入口。
- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]：把 skill 定义为大模型执行复杂任务的说明书、定向知识库和可演化执行知识体，强调主线、补丁、工作流节点和回主线机制。
- [[domains/AI Agent工程/03-Skill设计/03-主对话与干净子Agent的Skill回归测试方法|主对话与干净子 Agent 的 Skill 回归测试方法]]：用主 agent 设计/修 skill，用干净子 agent 验证落盘和独立执行能力。
- [[domains/AI Agent工程/03-Skill设计/04-可分享跨Agent Skill创建方法|可分享跨 Agent Skill 创建方法]]：用 portable 扩展组合当前基础 creator，并以隐私扫描、平台隔离和干净上下文测试保证可分享性。
- [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]：只收录 用户自己创建、让 Agent 为项目定制、或明显服务于 用户项目/业务流程的 skill，是日常检索“有没有类似 skill”的优先入口。
- [[domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库|跨 Agent Skill 注册库]]：统一检索 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 skill，定位原始 `SKILL.md` 并判断复用或迁移可能。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|Codex Skill 注册页]]：Codex 本地业务 skill 与系统 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/视觉制作/03-AI商业视觉/03-可编辑海报PSD重建Skill|可编辑海报 PSD 重建 Skill]]：Codex skill `editable-poster-psd-rebuild`，把 AI 带字海报重建为授权字体可编辑 PSD。
- [[domains/AI Agent工程/90-Skill注册表/04-Hermes Skill注册页|Hermes Skill 注册页]]：Hermes 主 skill 目录的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/05-Lark Agent Skill注册页|Lark Agent Skill 注册页]]：飞书/Lark 相关 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/06-OpenClaw Skill注册页|OpenClaw Skill 注册页]]：OpenClaw workspace skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/07-SealSeek Skill注册页|SealSeek Skill 注册页]]：SealSeek 多来源 skill 的检索描述、输入方式、关键词和文件位置，覆盖 skill_pool、workspace、active/customized、standalone 和迁移包。
- [[domains/AI Agent工程/90-Skill注册表/08-Claude Code Skill注册页|Claude Code Skill 注册页]]：Claude Code plugin marketplace skill 的检索描述、输入方式、关键词和文件位置。

## 插件工程

- [[domains/AI Agent工程/08-插件工程/index|Agent 插件工程]]：把 CLI、Skill、MCP、Connector、Hook、脚本和 Runtime 组织为可安装、可升级、可治理能力包的方法入口。
- [[domains/AI Agent工程/08-插件工程/01-Agent插件架构与设计方法论|Agent 插件架构与设计方法论]]：用认知、执行、连接、治理、分发五面模型解释 Plugin 的本质、组件边界和成熟度。
- [[queries/Agent插件设计与CLI改造|Agent 插件设计与 CLI 改造]]：插件化诊断、架构设计与 CLI 改造的 Agent 查询入口。

## 插件、Skill 与 CLI

- [[domains/AI Agent工程/10-插件Skill与CLI/index|插件、Skill 与 CLI]]：从业务需求、稳定 CLI、Skill 编排到 Plugin 分发的连续工程模块。
- [[domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范|Agent 驱动型电商 CLI 设计与开发规范]]：先建立能力自描述、安全、交付、测试和发布契约。
- [[domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件|从 CLI 与 Skill 演进为 Codex 插件]]：通过 Plugin Readiness Gate 后，选择外部依赖、随包 Runtime 或 MCP Adapter，并完成 Skill、Manifest、Marketplace 和安装生命周期。

## 多模态理解

- [[domains/AI Agent工程/09-多模态理解/index|Agent 多模态理解]]：把视频编译为带时间坐标、可检索、可验证的证据，而不是只生成摘要。
- [[domains/AI Agent工程/09-多模态理解/01-Agent读懂视频的证据化架构|Agent 读懂视频的证据化架构]]：统一媒体、分段、语言、视觉、时间和意图六层证据。
- [[domains/AI Agent工程/09-多模态理解/02-短教学视频读取工作流|短教学视频读取工作流]]：抖音、视频号和短教程的场景、ASR、OCR 与术语纠错。
- [[domains/AI Agent工程/09-多模态理解/03-长教学视频分层索引与检索|长教学视频分层索引与检索]]：长课程和跨视频资料的索引、检索与局部精读。
- [[domains/AI Agent工程/09-多模态理解/04-广告故事与产品视频质检|广告故事与产品视频质检]]：故事、镜头、声音、产品一致性和 AIGC 质量验收。
- [[domains/AI Agent工程/09-多模态理解/05-Codex与SealSeek视频读取实现协议|Codex 与 SealSeek 视频读取实现协议]]：共享中间产物、证据账本、失败降级和回归测试。
- [[domains/AI Agent工程/09-多模态理解/06-开源项目与技术选型|Agent 视频理解开源项目与技术选型]]：11 个 GitHub 项目的采用层级和三类视频最小组合。
- [[queries/Agent读懂视频入口|Agent 读懂视频入口]]：Agent 收到“读、理解、分析或质检视频”请求时的路由入口。

## 格式化文档

- [[domains/AI Agent工程/格式化文档/index|格式化文档]]：研究 Agent 如何把内容编译成结构清晰、易读、美观、可编辑、可维护的正式文档。
- [[domains/AI Agent工程/格式化文档/word文档/index|Word 文档格式化]]：Word 的格式系统、模板菜谱、常用文档结构和验收入口。
- [[queries/Word文档格式与模板选择入口|Word 文档格式与模板选择入口]]：Agent 收到 Word 排版、美化、模板或验收请求时的路由入口。

## Skill 注册表

- [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]：只收录 用户自己创建、让 Agent 为项目定制、或明显服务于 用户项目/业务流程的 skill，是日常检索“有没有类似 skill”的优先入口。
- [[domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库|跨 Agent Skill 注册库]]：统一检索 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 skill，定位原始 `SKILL.md` 并判断复用或迁移可能。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|Codex Skill 注册页]]：Codex 本地业务 skill 与系统 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/04-Hermes Skill注册页|Hermes Skill 注册页]]：Hermes 主 skill 目录的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/05-Lark Agent Skill注册页|Lark Agent Skill 注册页]]：飞书/Lark 相关 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/06-OpenClaw Skill注册页|OpenClaw Skill 注册页]]：OpenClaw workspace skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/07-SealSeek Skill注册页|SealSeek Skill 注册页]]：SealSeek 多来源 skill 的检索描述、输入方式、关键词和文件位置，覆盖 skill_pool、workspace、active/customized、standalone 和迁移包。
- [[domains/AI Agent工程/90-Skill注册表/08-Claude Code Skill注册页|Claude Code Skill 注册页]]：Claude Code plugin marketplace skill 的检索描述、输入方式、关键词和文件位置。

## 自动化工作流

- [[domains/AI Agent工程/06-自动化工作流/index|AI Agent 自动化工作流]]：沉淀目标、工具、证据、评审、循环、停止条件和经验回写组成的执行系统。
- [[domains/AI Agent工程/06-自动化工作流/01-Loop Engineering个人方法论|Loop Engineering 个人方法论]]：把 loop engineering 定义为围绕可证据化目标设计 Agent 执行、评审、修正、记录和停止的循环系统。
- [[domains/AI Agent工程/06-自动化工作流/02-Loop项目规划模板|Loop 项目规划模板]]：新建 loop 项目前，要求 Agent 先定义目标契约、证据面、工作基座、执行节点、评审节点、轮数预算和入库规则。
- [[queries/Loop项目启动入口|Loop 项目启动入口]]：用户要求“做一个 loop”“循环优化”“多轮自动改进”时，Agent 应优先读取的执行入口。

## 评测与调试

- [[domains/AI Agent工程/07-评测与调试/index|AI Agent 评测与调试]]：结果评测、执行链路审计、故障定位与回归验证入口。
- [[domains/AI Agent工程/07-评测与调试/01-AI Agent执行链路审计方法|AI Agent 执行链路审计方法]]：用“结果验收 + 过程验收”发现 Agent 绕路、静默降级、契约绕过和假成功。
- [[domains/AI Agent工程/07-评测与调试/02-Agent执行链路审计报告模板|Agent 执行链路审计报告模板]]：统一记录预期主线、实际轨迹、输出物验证、最终分类和回归要求。

## Toolchain

- [[domains/AI Agent工程/05-工具链/01-OpenAI图像生成API集成指南|OpenAI 图像生成 API 集成指南]]：Image API 与 Responses API 的选择、参数、编辑、流式、错误处理和成本判断。
- [[domains/AI Agent工程/05-工具链/02-飞书机器人Sealseek通道配置|飞书机器人 Sealseek 通道配置]]：飞书自建机器人连接 Sealseek 的完整配置流程，含权限（批量导入 JSON）、事件订阅、排障速查。
- [[domains/AI Agent工程/05-工具链/03-公司共享GPU工作节点与分时调度方法|公司共享 GPU 工作节点与分时调度方法]]：区分远程 GPU 原型与公司级共享平台，定义网络、身份、队列、调度、数据和观测方法。
- [[domains/AI Agent工程/05-工具链/04-Real-ESRGAN远程超分案例|Real-ESRGAN 远程超分案例]]：已验证 Tailscale + SSH/SCP + Windows GPU 超分链路；当前仍是初步测试原型。
- [[domains/AI Agent工程/05-工具链/05-网络与远程节点/index|网络与远程节点]]：VPS、代理线路、云安全组、客户端接入和网络验证的工具链入口。
- [[domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维|GigsGigsCloud 东京 Shadowsocks 节点部署与运维]]：从线路基准到 Shadowsocks、Mihomo、真实代理测速和运维治理的完整实践。
- [[queries/VPS代理节点部署与排障|VPS 代理节点部署与排障]]：收到 VPS 代理、自建节点、下载慢、丢包或客户端不兼容任务时的查询入口。
- [[queries/公司GPU共享与远程任务调度|公司 GPU 共享与远程任务调度]]：GPU 共享、异地 Worker 与多人排队任务的诊断入口。
- [[domains/AI Agent工程/10-插件Skill与CLI/01-Agent驱动型电商CLI设计与开发规范|Agent 驱动型电商 CLI 设计与开发规范]]：适用于淘宝、抖音、京东、1688等渠道的Agent CLI能力、自描述、安全、交付、测试和发布契约。
- [[queries/Agent驱动型电商CLI开发入口|Agent 驱动型电商 CLI 开发入口]]：创建、扩展或审查电商渠道CLI时的标准路由。
- [[domains/视觉制作/03-AI商业视觉/02-Codex与Photoshop协作自动化能力边界|Codex 与 Photoshop 协作自动化能力边界]]：Codex 调度 Photoshop、OCR、PSD 检查和电商视觉生产工具链的本机验证结论。
- [[domains/视觉制作/03-AI商业视觉/03-可编辑海报PSD重建Skill|可编辑海报 PSD 重建 Skill]]：以 GPT Image 2 去字底图 + Photoshop 原生文字层实现字体合规的海报 PSD 重建工作流。

## 关联共享页面

- [[shared/knowledge-management/llm-wiki|LLM Wiki 个人知识库]]：LLM Wiki 的总模式说明。
- [[shared/knowledge-management/obsidian-plugin-stack-for-knowledge-base|Obsidian 插件武装知识库的七件套]]：知识库建设中常用的 Obsidian 插件组合。
- [[shared/ai-agent-workflows/domains/视觉制作/05-小红书风格AI生图/index|AI Agent 共享工作流]]：跨域共享的 Agent 工作流入口。
