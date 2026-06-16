# AI Agent 工程知识域

本目录沉淀可跨项目复用的 AI Agent / LLM / 知识系统 / 自动化工程方法，而不是某个单一项目的配置细节。

## 适用范围

- 多 Agent 协作
- LLM Wiki 与知识系统
- Skill 设计与上下文工程
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
- `90-Skill注册表/`：由同步脚本生成的跨 Agent skill 检索资产。

## 知识系统

- [[domains/AI Agent工程/01-知识系统/domains/视觉制作/05-小红书风格AI生图/index|知识系统]]：个人知识库、LLM Wiki、Obsidian、知识编译与维护相关方法入口。
- [[domains/AI Agent工程/01-知识系统/01-LLM Wiki个人知识库运行闭环|LLM Wiki 个人知识库运行闭环]]：用 Ingest / Query / Lint 三个动作，把知识库从“资料堆”变成持续复利的个人知识系统。

## Skill 设计

- [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]：只收录 Peter 自己创建、让 Agent 为项目定制、或明显服务于 Peter 项目/业务流程的 skill，是日常检索“有没有类似 skill”的优先入口。
- [[domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库|跨 Agent Skill 注册库]]：统一检索 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 skill，定位原始 `SKILL.md` 并判断复用或迁移可能。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|Codex Skill 注册页]]：Codex 本地业务 skill 与系统 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/视觉制作/03-AI商业视觉/03-可编辑海报PSD重建Skill|可编辑海报 PSD 重建 Skill]]：Codex skill `editable-poster-psd-rebuild`，把 AI 带字海报重建为授权字体可编辑 PSD。
- [[domains/AI Agent工程/90-Skill注册表/04-Hermes Skill注册页|Hermes Skill 注册页]]：Hermes 主 skill 目录的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/05-Lark Agent Skill注册页|Lark Agent Skill 注册页]]：飞书/Lark 相关 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/06-OpenClaw Skill注册页|OpenClaw Skill 注册页]]：OpenClaw workspace skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/07-SealSeek Skill注册页|SealSeek Skill 注册页]]：SealSeek 多来源 skill 的检索描述、输入方式、关键词和文件位置，覆盖 skill_pool、workspace、active/customized、standalone 和迁移包。
- [[domains/AI Agent工程/90-Skill注册表/08-Claude Code Skill注册页|Claude Code Skill 注册页]]：Claude Code plugin marketplace skill 的检索描述、输入方式、关键词和文件位置。

## Skill 注册表

- [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]：只收录 Peter 自己创建、让 Agent 为项目定制、或明显服务于 Peter 项目/业务流程的 skill，是日常检索“有没有类似 skill”的优先入口。
- [[domains/AI Agent工程/90-Skill注册表/02-跨Agent Skill注册库|跨 Agent Skill 注册库]]：统一检索 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 skill，定位原始 `SKILL.md` 并判断复用或迁移可能。
- [[domains/AI Agent工程/90-Skill注册表/03-Codex Skill注册页|Codex Skill 注册页]]：Codex 本地业务 skill 与系统 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/04-Hermes Skill注册页|Hermes Skill 注册页]]：Hermes 主 skill 目录的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/05-Lark Agent Skill注册页|Lark Agent Skill 注册页]]：飞书/Lark 相关 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/06-OpenClaw Skill注册页|OpenClaw Skill 注册页]]：OpenClaw workspace skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/AI Agent工程/90-Skill注册表/07-SealSeek Skill注册页|SealSeek Skill 注册页]]：SealSeek 多来源 skill 的检索描述、输入方式、关键词和文件位置，覆盖 skill_pool、workspace、active/customized、standalone 和迁移包。
- [[domains/AI Agent工程/90-Skill注册表/08-Claude Code Skill注册页|Claude Code Skill 注册页]]：Claude Code plugin marketplace skill 的检索描述、输入方式、关键词和文件位置。

## Toolchain

- [[domains/AI Agent工程/05-工具链/01-OpenAI图像生成API集成指南|OpenAI 图像生成 API 集成指南]]：Image API 与 Responses API 的选择、参数、编辑、流式、错误处理和成本判断。
- [[domains/视觉制作/03-AI商业视觉/02-Codex与Photoshop协作自动化能力边界|Codex 与 Photoshop 协作自动化能力边界]]：Codex 调度 Photoshop、OCR、PSD 检查和电商视觉生产工具链的本机验证结论。
- [[domains/视觉制作/03-AI商业视觉/03-可编辑海报PSD重建Skill|可编辑海报 PSD 重建 Skill]]：以 GPT Image 2 去字底图 + Photoshop 原生文字层实现字体合规的海报 PSD 重建工作流。

## 关联共享页面

- [[shared/knowledge-management/llm-wiki|LLM Wiki 个人知识库]]：LLM Wiki 的总模式说明。
- [[shared/knowledge-management/obsidian-plugin-stack-for-knowledge-base|Obsidian 插件武装知识库的七件套]]：知识库建设中常用的 Obsidian 插件组合。
- [[shared/ai-agent-workflows/domains/视觉制作/05-小红书风格AI生图/index|AI Agent 共享工作流]]：跨域共享的 Agent 工作流入口。
