# AI Agent 工程知识域

本目录沉淀可跨项目复用的 AI Agent / LLM / 知识系统 / 自动化工程方法，而不是某个单一项目的配置细节。

## 适用范围

- 多 Agent 协作
- LLM Wiki 与知识系统
- Skill 设计与上下文工程
- CLI / MCP / 浏览器 / API 工具链
- 自动化工作流与评测调试

## 子主题

- `knowledge-systems/`：个人知识库、LLM Wiki、Obsidian、知识编译与维护。
- `agent-architecture/`：Agent 分工、memory、tool orchestration、多 Agent 结构。
- `skill-design/`：Skill 设计、状态机、执行契约、工作流抽象。
- `toolchain/`：CLI、MCP、Git、浏览器自动化、API 组合方式。
- `prompt-and-context/`：提示词结构、上下文注入、长期记忆和规则文件。
- `automation-workflows/`：可执行的多步自动化流程。
- `evaluation-and-debugging/`：质量门、lint、回归测试、故障定位。

## 知识系统

- [[domains/ai-agent-engineering/knowledge-systems/index|知识系统]]：个人知识库、LLM Wiki、Obsidian、知识编译与维护相关方法入口。
- [[domains/ai-agent-engineering/knowledge-systems/llm-wiki-personal-knowledge-base-operating-loop|LLM Wiki 个人知识库运行闭环]]：用 Ingest / Query / Lint 三个动作，把知识库从“资料堆”变成持续复利的个人知识系统。

## Skill 设计

- [[domains/ai-agent-engineering/skill-design/personal-ai-agent-skill-registry|个人/项目 Skill 注册库]]：只收录 Peter 自己创建、让 Agent 为项目定制、或明显服务于 Peter 项目/业务流程的 skill，是日常检索“有没有类似 skill”的优先入口。
- [[domains/ai-agent-engineering/skill-design/ai-agent-skill-registry|跨 Agent Skill 注册库]]：统一检索 Codex、Hermes、Lark Agent、OpenClaw、SealSeek、Claude Code 的 skill，定位原始 `SKILL.md` 并判断复用或迁移可能。
- [[domains/ai-agent-engineering/skill-design/codex-skill-inventory|Codex Skill 注册页]]：Codex 本地业务 skill 与系统 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/ai-agent-engineering/skill-design/hermes-skill-registry|Hermes Skill 注册页]]：Hermes 主 skill 目录的检索描述、输入方式、关键词和文件位置。
- [[domains/ai-agent-engineering/skill-design/lark-agent-skill-registry|Lark Agent Skill 注册页]]：飞书/Lark 相关 skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/ai-agent-engineering/skill-design/openclaw-skill-registry|OpenClaw Skill 注册页]]：OpenClaw workspace skill 的检索描述、输入方式、关键词和文件位置。
- [[domains/ai-agent-engineering/skill-design/sealseek-skill-registry|SealSeek Skill 注册页]]：SealSeek 多来源 skill 的检索描述、输入方式、关键词和文件位置，覆盖 skill_pool、workspace、active/customized、standalone 和迁移包。
- [[domains/ai-agent-engineering/skill-design/claude-code-skill-registry|Claude Code Skill 注册页]]：Claude Code plugin marketplace skill 的检索描述、输入方式、关键词和文件位置。

- [[domains/ai-agent-engineering/skill-design/infinite-canvas-skill-writing/index|无限画板 Skill 写作知识库]]：面向无限画板 `skill.md` 创建/优化的规则库、工具规范、任务范式、Prompt 模板、反坑清单和 Agent 使用模板。

## Toolchain

- [[domains/ai-agent-engineering/toolchain/openai-image-generation-api|OpenAI 图像生成 API 集成指南]]：Image API 与 Responses API 的选择、参数、编辑、流式、错误处理和成本判断。

## 关联共享页面

- [[shared/knowledge-management/llm-wiki|LLM Wiki 个人知识库]]：LLM Wiki 的总模式说明。
- [[shared/knowledge-management/obsidian-plugin-stack-for-knowledge-base|Obsidian 插件武装知识库的七件套]]：知识库建设中常用的 Obsidian 插件组合。
- [[shared/ai-agent-workflows/index|AI Agent 共享工作流]]：跨域共享的 Agent 工作流入口。
