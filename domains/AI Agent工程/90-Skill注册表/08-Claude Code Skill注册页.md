---
title: Claude Code Skill 注册页
type: concept
created: 2026-06-14
updated: 2026-06-14
domain: AI Agent工程
tags: [ai-agent, claude-code, skill, registry]
sources:
  - /Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak
status: active
---
# Claude Code Skill 注册页

本页记录 Claude Code 环境中的 skill，用于 AI Agent 检索“是否已有类似 skill”并定位原始 SKILL.md。

## 维护范围

来源目录：

- `/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak`

- 说明：Claude Code plugin marketplace backup skills.
- 当前记录数量：26

归属分类统计：

- 归档/备份: 26

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/AI Agent工程/90-Skill注册表/01-个人与项目Skill注册库|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 视觉 / 内容 / 课件生产

- `frontend-design` (归档/备份 / archived-or-backup)：Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to …
- `build-mcp-server` (归档/备份 / archived-or-backup)：This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap…
- `playground` (归档/备份 / archived-or-backup)：Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually …

### Agent 工程 / Skill / Plugin / MCP

- `access` (归档/备份 / archived-or-backup)：Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, …
- `configure` (归档/备份 / archived-or-backup)：Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, …
- `access` (归档/备份 / archived-or-backup)：Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair,…
- `configure` (归档/备份 / archived-or-backup)：Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set …
- `access` (归档/备份 / archived-or-backup)：Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair,…
- `configure` (归档/备份 / archived-or-backup)：Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token…
- `claude-automation-recommender` (归档/备份 / archived-or-backup)：Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user…
- `claude-md-improver` (归档/备份 / archived-or-backup)：Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md…
- `example-command` (归档/备份 / archived-or-backup)：An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout
- `example-skill` (归档/备份 / archived-or-backup)：This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or…
- `writing-hookify-rules` (归档/备份 / archived-or-backup)：This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add …
- `math-olympiad` (归档/备份 / archived-or-backup)："Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-v…
- `build-mcp-app` (归档/备份 / archived-or-backup)：This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server,…
- `build-mcpb` (归档/备份 / archived-or-backup)：This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local…
- `agent-development` (归档/备份 / archived-or-backup)：This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatte…
- `command-development` (归档/备份 / archived-or-backup)：This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "de…
- `hook-development` (归档/备份 / archived-or-backup)：This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate too…
- `mcp-integration` (归档/备份 / archived-or-backup)：This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.…
- `plugin-settings` (归档/备份 / archived-or-backup)：This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable p…
- `plugin-structure` (归档/备份 / archived-or-backup)：This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "…
- `skill-development` (归档/备份 / archived-or-backup)：This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improv…
- `session-report` (归档/备份 / archived-or-backup)：Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) fr…
- `skill-creator` (归档/备份 / archived-or-backup)：Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a sk…

## Skill 详情

### `access`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/external_plugins/discord/skills/access/SKILL.md`
- 功能检索描述：Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Discord channel.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：access /discord:access — Discord Channel Access Management Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Discord channel. external_plugins/discord/skills/access/SKILL.md archived-or-backup

### `configure`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/external_plugins/discord/skills/configure/SKILL.md`
- 功能检索描述：Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：configure /discord:configure — Discord Channel Setup Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status. external_plugins/discord/skills/configure/SKILL.md archived-or-backup

### `access`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/external_plugins/imessage/skills/access/SKILL.md`
- 功能检索描述：Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the iMessage channel.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：access /imessage:access — iMessage Channel Access Management Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the iMessage channel. external_plugins/imessage/skills/access/SKILL.md archived-or-backup

### `configure`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/external_plugins/imessage/skills/configure/SKILL.md`
- 功能检索描述：Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set this up" or "who can reach me," or wants to know why texts aren't reaching the assistant.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：configure /imessage:configure — iMessage Channel Setup Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set this up" or "who can reach me," or wants to know why texts aren't reaching the assistant. external_plugins/imessage/skills/configure/SKILL.md archived-or-backup

### `access`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/external_plugins/telegram/skills/access/SKILL.md`
- 功能检索描述：Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Telegram channel.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：access /telegram:access — Telegram Channel Access Management Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Telegram channel. external_plugins/telegram/skills/access/SKILL.md archived-or-backup

### `configure`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/external_plugins/telegram/skills/configure/SKILL.md`
- 功能检索描述：Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token, asks to configure Telegram, asks "how do I set this up" or "who can reach me," or wants to check channel status.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：configure /telegram:configure — Telegram Channel Setup Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token, asks to configure Telegram, asks "how do I set this up" or "who can reach me," or wants to check channel status. external_plugins/telegram/skills/configure/SKILL.md archived-or-backup

### `claude-automation-recommender`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`
- 功能检索描述：Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求
- 检索关键词：claude-automation-recommender Claude Automation Recommender Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use. plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md archived-or-backup

### `claude-md-improver`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`
- 功能检索描述：Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：claude-md-improver CLAUDE.md Improver Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization". plugins/claude-md-management/skills/claude-md-improver/SKILL.md archived-or-backup

### `example-command`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/example-plugin/skills/example-command/SKILL.md`
- 功能检索描述：An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：example-command Example Command (Skill Format) An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout plugins/example-plugin/skills/example-command/SKILL.md archived-or-backup

### `example-skill`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/example-plugin/skills/example-skill/SKILL.md`
- 功能检索描述：This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：example-skill Example Skill This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills. plugins/example-plugin/skills/example-skill/SKILL.md archived-or-backup

### `frontend-design`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/frontend-design/skills/frontend-design/SKILL.md`
- 功能检索描述：Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：frontend-design Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics. plugins/frontend-design/skills/frontend-design/SKILL.md archived-or-backup

### `writing-hookify-rules`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/hookify/skills/writing-rules/SKILL.md`
- 功能检索描述：This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：writing-hookify-rules Writing Hookify Rules This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns. plugins/hookify/skills/writing-rules/SKILL.md archived-or-backup

### `math-olympiad`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/math-olympiad/skills/math-olympiad/SKILL.md`
- 功能检索描述："Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. Activates when asked to 'solve this IMO problem', 'prove this olympiad inequality', 'verify this competition proof', 'find a counterexample', 'is this proof correct', or for any problem with 'IMO', 'Putnam', 'USAMO', 'olympiad', or 'competition math' in it. Uses pure reasoning (no tools) — then a fresh-context adversarial verifier attacks the proof using specific failure patterns, not generic 'check logic'. Outputs calibrated confidence — will say 'no confident solution' rather than bluff. If LaTeX is available, produces a clean PDF after verification passes."
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求
- 检索关键词：math-olympiad Math Olympiad Solver "Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. Activates when asked to 'solve this IMO problem', 'prove this olympiad inequality', 'verify this competition proof', 'find a counterexample', 'is this proof correct', or for any problem with 'IMO', 'Putnam', 'USAMO', 'olympiad', or 'competition math' in it. Uses pure reasoning (no tools) — then a fresh-context adversarial verifier attacks the proof using specific failure patterns, not generic 'check logic'. Outputs calibrated confidence — will say 'no confident solution' rather than bluff. If LaTeX is available, produces a clean PDF after verification passes." plugins/math-olympiad/skills/math-olympiad/SKILL.md archived-or-backup

### `build-mcp-app`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`
- 功能检索描述：This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：build-mcp-app Build an MCP App (Interactive UI Widgets) This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets. plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md archived-or-backup

### `build-mcp-server`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
- 功能检索描述：This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：build-mcp-server Build an MCP Server This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills. plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md archived-or-backup

### `build-mcpb`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`
- 功能检索描述：This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：build-mcpb Build an MCPB (Bundled Local MCP Server) This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up. plugins/mcp-server-dev/skills/build-mcpb/SKILL.md archived-or-backup

### `playground`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/playground/skills/playground/SKILL.md`
- 功能检索描述：Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求
- 检索关键词：playground Playground Builder Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic. plugins/playground/skills/playground/SKILL.md archived-or-backup

### `agent-development`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/plugin-dev/skills/agent-development/SKILL.md`
- 功能检索描述：This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：agent-development Agent Development for Claude Code Plugins This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins. plugins/plugin-dev/skills/agent-development/SKILL.md archived-or-backup

### `command-development`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/plugin-dev/skills/command-development/SKILL.md`
- 功能检索描述：This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：command-development Command Development for Claude Code This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code. plugins/plugin-dev/skills/command-development/SKILL.md archived-or-backup

### `hook-development`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/plugin-dev/skills/hook-development/SKILL.md`
- 功能检索描述：This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：hook-development Hook Development for Claude Code Plugins This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API. plugins/plugin-dev/skills/hook-development/SKILL.md archived-or-backup

### `mcp-integration`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
- 功能检索描述：This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：mcp-integration MCP Integration for Claude Code Plugins This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration. plugins/plugin-dev/skills/mcp-integration/SKILL.md archived-or-backup

### `plugin-settings`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/plugin-dev/skills/plugin-settings/SKILL.md`
- 功能检索描述：This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：plugin-settings Plugin Settings Pattern for Claude Code Plugins This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content. plugins/plugin-dev/skills/plugin-settings/SKILL.md archived-or-backup

### `plugin-structure`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
- 功能检索描述：This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：plugin-structure Plugin Structure for Claude Code This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices. plugins/plugin-dev/skills/plugin-structure/SKILL.md archived-or-backup

### `skill-development`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/plugin-dev/skills/skill-development/SKILL.md`
- 功能检索描述：This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：skill-development Skill Development for Claude Code Plugins This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins. plugins/plugin-dev/skills/skill-development/SKILL.md archived-or-backup

### `session-report`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/session-report/skills/session-report/SKILL.md`
- 功能检索描述：Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：session-report Session Report Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. plugins/session-report/skills/session-report/SKILL.md archived-or-backup

### `skill-creator`

- Agent / 环境：Claude Code
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/skill-creator/skills/skill-creator/SKILL.md`
- 功能检索描述：Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：skill-creator Skill Creator Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy. plugins/skill-creator/skills/skill-creator/SKILL.md archived-or-backup

