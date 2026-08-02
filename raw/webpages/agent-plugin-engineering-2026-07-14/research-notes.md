# Agent 插件工程调研原始记录

- 调研日期：2026-07-14
- 主题：Agent Plugin、Skill、CLI、MCP、Connector、Hook 与 Marketplace 的关系
- 目标：解释已有“CLI + Skill + 外部连接”体系如何演进为真正可安装、可分发、可治理的 Codex 插件
- 说明：本文是研究过程记录，正式结论见 `domains/AI Agent工程/08-插件工程/`。

## 1. OpenAI Codex 官方资料

### 1.1 Codex Manual / Build plugins

- URL：https://developers.openai.com/codex/codex-manual.md
- 原始页面入口：https://learn.chatgpt.com/docs/build-plugins.md
- 读取日期：2026-07-14
- 关键事实：
  - 单项目、个人工作流和快速迭代优先从本地 Skill 开始；需要跨团队共享、捆绑 Connector/MCP、生命周期 Hook 或稳定发布时再做 Plugin。
  - Plugin 可包含 Skills、MCP-backed App，或两者兼有。
  - 每个 Codex Plugin 必须有 `.codex-plugin/plugin.json`。
  - 可选组件包括 `skills/`、`.app.json`、`.mcp.json`、hooks 和 assets。
  - Manifest 同时承担身份、组件索引、安装界面元数据三类职责。
  - Marketplace 可来自 repo、个人目录、Git、npm；安装后进入本地 cache，并按插件独立启停。
  - 官方发布形态可以是 skills-only、app-only 或 app-plus-skills。
  - 带 MCP 的公开提交需要工具元数据、权限注解、测试用例、隐私说明、域名与身份验证。

### 1.2 Codex 本机 CLI 验证

执行日期：2026-07-14。已验证 `codex plugin --help`、`codex plugin marketplace --help` 和 `codex plugin marketplace list`。

本机 `codex plugin` 支持 `add`、`list`、`marketplace`、`remove`；Marketplace 支持 `add`、`list`、`upgrade`、`remove`。

## 2. OpenAI 公开 GitHub 插件仓库

- URL：https://github.com/openai/plugins
- 读取日期：2026-07-14
- 关键事实：
  - 每个插件位于 `plugins/<name>/`，必需入口是 `.codex-plugin/plugin.json`。
  - 公开仓库展示了 `skills/`、`.app.json`、`.mcp.json`、agents、commands、hooks、assets 等组合。
  - Figma、Notion、Web App、iOS/macOS、Expo、Netlify、Remotion 等示例表明 Plugin 是多种 Agent 扩展表面的打包层，而非某一种执行协议。

## 3. Agent Skills 开放规范

- URL：https://github.com/agentskills/agentskills
- 文档：https://agentskills.io/
- 读取日期：2026-07-14
- 关键事实：
  - Skill 是包含 `SKILL.md` 的目录，可携带 scripts、references、assets。
  - Skill 的价值是领域知识、可重复工作流和跨产品复用。
  - 采用三阶段渐进披露：Discovery 只加载 name/description；Activation 读取完整 `SKILL.md`；Execution 再读取引用文件或执行脚本。
  - Skill 解决“Agent 如何理解和执行任务”，但不独自解决安装、版本、连接、权限和分发。

## 4. Model Context Protocol

- URL：https://modelcontextprotocol.io/docs/learn/architecture
- 读取日期：2026-07-14
- 关键事实：
  - MCP 是 Host—Client—Server 架构，聚焦上下文交换协议，不规定宿主如何使用模型或管理上下文。
  - 数据层基于 JSON-RPC 2.0，包含 lifecycle、capability negotiation、tools、resources、prompts、notifications。
  - Transport 包括本地 stdio 和远程 Streamable HTTP；远程连接可配合 OAuth。
  - MCP 提供跨宿主的结构化发现与调用契约，适合动态工具、远程服务、统一认证和多 Agent 客户端复用。

## 5. Claude Code 插件作为跨生态对照

- 创建插件：https://code.claude.com/docs/en/plugins
- 插件参考：https://code.claude.com/docs/en/plugins-reference
- 读取日期：2026-07-14
- 关键事实：
  - 官方同样将 Plugin 定义为可跨项目和团队分享的自包含能力包。
  - 单项目快速实验使用 standalone 配置；跨项目、版本更新和 Marketplace 分发时再做 Plugin。
  - Plugin 可捆绑 Skills、Agents、Hooks、MCP、LSP、Monitors 和默认设置。
  - 插件命名空间用于避免不同插件组件冲突。
  - 调试重点包括 Manifest、组件注册、MCP 初始化、相对路径和版本缓存。

## 6. 本机已安装 Codex 插件样本

### 6.1 GitHub：Connector-first，CLI fallback

路径：`~/.codex/plugins/cache/openai-curated-remote/github/0.1.8-2841cf9749ae/`

组成：Manifest、`.app.json` GitHub Connector、通用路由 Skill、review/CI/publish 专项 Skills 和 assets。PR、Issue、评论等优先 Connector；本地分支、commit、push、Actions 日志等使用 `git` 和 `gh` 补位。这证明 Plugin 可以组合 Connector 和外部 CLI，无需把所有执行统一重写为 MCP。

### 6.2 Figma：Connector + 远程 MCP + 多 Skill

路径：`~/.codex/plugins/cache/openai-curated-remote/figma/2.0.14/`

组成：Manifest、Figma Connector、`https://mcp.figma.com/mcp`、多个专项 Skill、agents、commands、scripts、hooks、UI 和 assets。共享连接能力由 MCP/Connector 提供，多个 Skill 负责创建、读取、设计系统、Code Connect、SwiftUI、Motion 等分支。

### 6.3 Sites：Connector + 本地 MCP + Skills + 脚本

路径：`~/.codex/plugins/cache/openai-bundled/sites/0.1.27/`

组成：Sites Connector、Node 本地 MCP server、building/hosting Skills 和初始化、打包、预览脚本。Plugin 同时携带确定性工程脚本、Agent 工作流、工具协议和托管连接。

### 6.4 Computer Use：本地 MCP + Skill + 原生 Runtime

路径：`~/.codex/plugins/cache/openai-bundled/computer-use/1.0.1000387/`

`.mcp.json` 启动本地原生可执行程序；Skill 负责告诉 Agent 何时使用以及如何控制风险。说明插件可携带本机 Runtime，不限于云端 API。

## 7. 用户现有 tbcli 样本

- CLI：`~/.local/share/tbcli/`
- Skill：`~/.codex/skills/wdt-dingtalk-logistics-dashboard/`

现有三层：

1. CLI：`tbcli browser open`、`tbcli logistics get`。
2. 连接：Playwright 通过 CDP 接入已登录 Chrome，并在页面上下文调用淘宝物流接口。
3. Skill 与编排：物流看板 Skill 调用 `wdtcli`、`tbcli`、`dws`，包含限速、风控、状态映射和日志。

尚未具备的 Plugin 层：Manifest、统一插件目录和相对路径、Marketplace 安装和版本升级、插件级能力/权限/认证说明、独立安装与负向测试，以及 CLI 是随包 Runtime 还是外部 prerequisite 的明确决策。

## 8. 研究推导

1. Plugin 是分发与治理边界，不是新的执行方式。
2. CLI、API、浏览器、MCP、Connector 都可以位于 Plugin 的执行/连接层。
3. Skill 是认知与调度层，负责让 Agent 在正确场景使用正确工具并处理异常。
4. Manifest、版本、Marketplace、命名空间、权限、认证、测试和资产把内部工具体系升级为产品化能力包。
5. 成熟插件至少同时考虑：认知面、执行面、连接面、治理面、分发面。
6. CLI-first 架构无需推倒重来；应先稳定 CLI 契约，再选择直接随包、作为依赖，或增加 MCP 适配层。

