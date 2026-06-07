---
title: Hermes Skill 注册页
type: concept
created: 2026-06-05
updated: 2026-06-05
domain: ai-agent-engineering
tags: [ai-agent, hermes, skill, registry]
sources:
  - /Users/pechen/.hermes/skills
status: active
---
# Hermes Skill 注册页

本页记录 Hermes 环境中的 skill，用于 AI Agent 检索“是否已有类似 skill”并定位原始 SKILL.md。

## 维护范围

来源目录：

- `/Users/pechen/.hermes/skills`

- 说明：Hermes main skills directory, excluding duplicated hermes-agent optional skill trees.
- 当前记录数量：167

归属分类统计：

- 个人/项目自定义: 52
- 归档/备份: 1
- 通用安装/不确定: 114

## 使用规则

- 先用本页的名称、功能检索描述、输入方式和关键词判断是否存在类似 skill。
- 日常优先检索 [[domains/ai-agent-engineering/skill-design/personal-ai-agent-skill-registry|个人/项目 Skill 注册库]]；只有找不到时再回到全量库。
- 找到候选后，必须打开 `Skill 文件位置` 中的 `SKILL.md` 阅读完整流程、依赖和约束。
- skill 多数可以跨 Agent 迁移，但执行前要检查工具、路径、权限、环境变量和脚本依赖。

## 按能力分类快速索引

### 知识库 / 知识管理 / LLM Wiki

- `baoyu-comic` (个人/项目自定义 / local)：Knowledge comics (知识漫画): educational, biography, tutorial.
- `obsidian` (通用安装/不确定 / local)：Read, search, create, and edit notes in the Obsidian vault.
- `course-transcript-to-knowledge` (个人/项目自定义 / local)：Reconstruct, analyze, and enrich full knowledge systems from course/audio transcripts into Peter's LLM Wiki. Use for cla…
- `douyin-link-to-knowledge` (个人/项目自定义 / local)：Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style b…
- `llm-wiki` (个人/项目自定义 / local)：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compil…
- `llm-wiki-audit-and-optimization` (个人/项目自定义 / local)：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or w…

### 视觉 / 内容 / 课件生产

- `ecommerce-single-image-optimization` (归档/备份 / archived-or-backup)：Design and iterate a reusable e-commerce single-image optimization workflow. Use when building or running a skill that t…
- `architecture-diagram` (通用安装/不确定 / local)：Dark-themed SVG architecture/cloud/infra diagrams as HTML.
- `ascii-art` (通用安装/不确定 / local)：ASCII art: pyfiglet, cowsay, boxes, image-to-ascii.
- `ascii-video` (通用安装/不确定 / local)：ASCII video: convert video/audio to colored ASCII MP4/GIF.
- `baoyu-article-illustrator` (个人/项目自定义 / local)：Article illustrations: type × style × palette consistency.
- `baoyu-infographic` (个人/项目自定义 / local)：Infographics: 21 layouts x 21 styles (信息图, 可视化).
- `claude-design` (通用安装/不确定 / local)：Design one-off HTML artifacts (landing, deck, prototype).
- `comfyui` (通用安装/不确定 / local)：Generate images, video, and audio with ComfyUI — install, launch, manage nodes/models, run workflows with parameter inje…
- `ideation` (通用安装/不确定 / local)：Generate project ideas via creative constraints.
- `dashscope-happyhorse-video` (通用安装/不确定 / local)：Research and use Alibaba Cloud DashScope / Model Studio HappyHorse 1.0 video generation and editing APIs with DASHSCOPE_…
- `design-md` (通用安装/不确定 / local)：Author/validate/export Google's DESIGN.md token spec files.
- `detail-page-batch-optimization` (通用安装/不确定 / local)：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared prod…
- `ecommerce-image-skill-architecture` (个人/项目自定义 / local)：Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use w…
- `evolink-gpt-image-2` (个人/项目自定义 / local)：Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and t…
- `excalidraw` (通用安装/不确定 / local)：Hand-drawn Excalidraw JSON diagrams (arch, flow, seq).
- `gpt-image-2-12api` (个人/项目自定义 / local)：Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavio…
- `gpt生图` (个人/项目自定义 / local)：Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, de…
- `humanizer` (通用安装/不确定 / local)：Humanize text: strip AI-isms and add real voice.
- `lingerie-model-product-replacement` (通用安装/不确定 / local)：Test and run safer workflows for replacing bras/lingerie products on model images, avoiding unstable full-face intimate-…
- `manim-video` (通用安装/不确定 / local)：Manim CE animations: 3Blue1Brown math/algo videos.
- `p5js` (通用安装/不确定 / local)：p5.js sketches: gen art, shaders, interactive, 3D.
- `pixel-art` (通用安装/不确定 / local)：Pixel art w/ era palettes (NES, Game Boy, PICO-8).
- `popular-web-designs` (通用安装/不确定 / local)：54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.
- `pretext` (通用安装/不确定 / local)：Use when building creative browser demos with @chenglou/pretext — DOM-free text layout for ASCII art, typographic flow a…
- `shopping-basket-visual-planning` (个人/项目自定义 / local)：Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the use…
- `single-image-optimization` (个人/项目自定义 / local)：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/st…
- `sketch` (通用安装/不确定 / local)：Throwaway HTML mockups: 2-3 design variants to compare.
- `songwriting-and-ai-music` (通用安装/不确定 / local)：Songwriting craft and Suno AI music prompts.
- `taobao-gpt-image-creative-main-image` (个人/项目自定义 / local)：Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably …
- `toapis-gpt-image-2` (个人/项目自定义 / local)：Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working reque…
- `touchdesigner-mcp` (通用安装/不确定 / local)：Control a running TouchDesigner instance via twozero MCP — create operators, set parameters, wire connections, execute P…
- `hermes-platform-tool-availability-debugging` (通用安装/不确定 / local)：Diagnose why Hermes on a messaging platform used the wrong tool (for example vision_analyze instead of image_generate) o…
- `clip` (通用安装/不确定 / local)：OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-mo…
- `segment-anything-model` (通用安装/不确定 / local)：SAM: zero-shot image segmentation via points, boxes, masks.
- `stable-diffusion-image-generation` (通用安装/不确定 / local)：State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating im…
- `conference-static-html-courseware-review-loop` (个人/项目自定义 / local)：Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review,…
- `course-html-ppt-16x9-image-pages` (个人/项目自定义 / local)：Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy sl…
- `dual-source-chapterized-html-ppt-courseware` (个人/项目自定义 / local)：Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to av…
- `ecommerce-bi-operation-skill-planning` (个人/项目自定义 / local)：Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡…
- `feishu-product-feature-doc` (个人/项目自定义 / local)：Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-orien…
- `goal-driven-daily-report-templates` (个人/项目自定义 / local)：Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use whe…
- `hermes-feishu-session-debugging` (个人/项目自定义 / local)：Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session …
- `html-course-deck` (通用安装/不确定 / local)：Create polished browser-based HTML slide decks for courses or presentations when PPTX generation looks rigid, dated, or …
- `html-ppt-conference-review-loop` (个人/项目自定义 / local)：Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with ex…
- `html-ppt-course-deck` (个人/项目自定义 / local)：Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid o…
- `html-ppt-font-standardization` (个人/项目自定义 / local)：Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run …
- `html-ppt-screenshot-review-loop` (个人/项目自定义 / local)：Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-s…
- `html-ppt-stage-fit-and-background-cleanup` (个人/项目自定义 / local)：Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds wit…
- `html-ppt` (个人/项目自定义 / local)：HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by t…
- `powerpoint` (通用安装/不确定 / local)：Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide d…
- `pptx-template-python-pptx` (通用安装/不确定 / local)：Generate a PowerPoint deck from an existing .pptx template using python-pptx when no dedicated PPT CLI is installed or w…
- `review-driven-static-html-courseware` (个人/项目自定义 / local)：Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML…
- `sealseek-static-html-courseware-workflow` (个人/项目自定义 / local)：Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server depend…
- `shopping-basket-visual-reference-discovery` (个人/项目自定义 / local)：docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual refe…
- `single-file-static-html-courseware` (个人/项目自定义 / local)：Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live…
- `static-html-courseware-feedback-loop` (个人/项目自定义 / local)：Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review st…
- `static-html-courseware-review-loop` (个人/项目自定义 / local)：Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of s…
- `static-html-courseware-review-loop-v2` (个人/项目自定义 / local)：Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimiz…
- `static-html-courseware-shared-assets-and-merge` (个人/项目自定义 / local)：Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapt…
- `static-html-deck-to-editable-ppt` (个人/项目自定义 / local)：Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into tru…
- `xicheng-bi-feishu-feature-doc` (个人/项目自定义 / local)：Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise s…
- `research-paper-writing` (通用安装/不确定 / local)：Write ML papers for NeurIPS/ICML/ICLR: design→submit.
- `hermes-s6-container-supervision` (通用安装/不确定 / local)：Modify, debug, or extend the s6-overlay supervision tree inside the Hermes Agent Docker image — adding new services, deb…
- `sealseek-gpt-image-skill-migration` (个人/项目自定义 / local)：Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use…
- `sealseek-skill-sync-and-toolcall-fix` (个人/项目自定义 / local)：Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-p…

### 电商 / 商品 / 品牌运营

- `real-chrome-web-reader` (个人/项目自定义 / local)：使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。
- `taobao-native-search-to-excel` (个人/项目自定义 / local)：使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排…
- `taobao-search-to-excel` (个人/项目自定义 / local)：使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。

### Agent 工程 / Skill / Plugin / MCP

- `apple-notes` (通用安装/不确定 / local)：Manage Apple Notes via memo CLI: create, search, edit.
- `apple-reminders` (通用安装/不确定 / local)：Apple Reminders via remindctl: add, list, complete.
- `findmy` (通用安装/不确定 / local)：Track Apple devices/AirTags via FindMy.app on macOS.
- `imessage` (通用安装/不确定 / local)：Send and receive iMessages/SMS via the imsg CLI on macOS.
- `macos-computer-use` (通用安装/不确定 / local)：Drive the macOS desktop in the background — screenshots, mouse, keyboard, scroll, drag — without stealing the user's cur…
- `claude-code` (通用安装/不确定 / local)：Delegate coding to Claude Code CLI (features, PRs).
- `codex` (通用安装/不确定 / local)：Delegate coding to OpenAI Codex CLI (features, PRs).
- `hermes-agent` (通用安装/不确定 / local)：Complete guide to using and extending Hermes Agent — CLI usage, setup, configuration, spawning additional agents, gatewa…
- `hermes-custom-provider-validation` (通用安装/不确定 / local)：Validate Hermes custom model providers (especially Gemini/OpenAI-compatible relays) for real usability, latency, and out…
- `hermes-model-provider-diagnostics` (通用安装/不确定 / local)：Diagnose Hermes model/provider behavior: effective context windows, provider-specific caps, routing surprises, and confi…
- `kanban-codex-lane` (通用安装/不确定 / local)：Use when a Hermes Kanban worker wants to run Codex CLI as an isolated implementation lane while Hermes keeps ownership o…
- `opencode` (通用安装/不确定 / local)：Delegate coding to OpenCode CLI (features, PR review).
- `jupyter-live-kernel` (通用安装/不确定 / local)：Iterative Python via live Jupyter kernel (hamelnb).
- `kanban-orchestrator` (通用安装/不确定 / local)：Decomposition playbook + anti-temptation rules for an orchestrator profile routing work through Kanban. The "don't do th…
- `kanban-worker` (通用安装/不确定 / local)：Pitfalls, examples, and edge cases for Hermes Kanban workers. The lifecycle itself is auto-injected into every worker's …
- `webhook-subscriptions` (通用安装/不确定 / local)：Webhook subscriptions: event-driven agent runs.
- `dogfood` (通用安装/不确定 / local)：Systematic exploratory QA testing of web applications — find bugs, capture evidence, and generate structured reports
- `himalaya` (通用安装/不确定 / local)：Himalaya CLI: IMAP/SMTP email from terminal.
- `minecraft-modpack-server` (通用安装/不确定 / local)：Host modded Minecraft servers (CurseForge, Modrinth).
- `pokemon-player` (通用安装/不确定 / local)：Play Pokemon via headless emulator + RAM reads.
- `codebase-inspection` (通用安装/不确定 / local)：Inspect codebases w/ pygount: LOC, languages, ratios.
- `github-auth` (通用安装/不确定 / local)：GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login.
- `github-code-review` (通用安装/不确定 / local)：Review PRs: diffs, inline comments via gh or REST.
- `github-issues` (通用安装/不确定 / local)：Create, triage, label, assign GitHub issues via gh or REST.
- `github-pr-workflow` (通用安装/不确定 / local)：GitHub PR lifecycle: branch, commit, open, CI, merge.
- `github-repo-management` (通用安装/不确定 / local)：Clone/create/fork repos; manage remotes, releases.
- `find-nearby` (通用安装/不确定 / local)：Find nearby places (restaurants, cafes, bars, pharmacies, etc.) using OpenStreetMap. Works with coordinates, addresses, …
- `mcporter` (通用安装/不确定 / local)：Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc ser…
- `native-mcp` (通用安装/不确定 / local)：MCP client: connect servers, register tools (stdio/HTTP).
- `gif-search` (通用安装/不确定 / local)：Search/download GIFs from Tenor via curl + jq.
- `heartmula` (通用安装/不确定 / local)：HeartMuLa: Suno-like song generation from lyrics + tags.
- `songsee` (通用安装/不确定 / local)：Audio spectrograms/features (mel, chroma, MFCC) via CLI.
- `spotify` (通用安装/不确定 / local)：Spotify: play, search, queue, manage playlists and devices.
- `youtube-content` (通用安装/不确定 / local)：YouTube transcripts to summaries, threads, blogs.
- `modal-serverless-gpu` (通用安装/不确定 / local)：Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure ma…
- `evaluating-llms-harness` (通用安装/不确定 / local)：lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.).
- `weights-and-biases` (通用安装/不确定 / local)：W&B: log ML experiments, sweeps, model registry, dashboards.
- `huggingface-hub` (通用安装/不确定 / local)：HuggingFace hf CLI: search/download/upload models, datasets.
- `gguf-quantization` (通用安装/不确定 / local)：GGUF format and llama.cpp quantization for efficient CPU/GPU inference. Use when deploying models on consumer hardware, …
- `guidance` (通用安装/不确定 / local)：Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and bu…
- `llama-cpp` (通用安装/不确定 / local)：llama.cpp local GGUF inference + HF Hub model discovery.
- `obliteratus` (通用安装/不确定 / local)：OBLITERATUS: abliterate LLM refusals (diff-in-means).
- `outlines` (通用安装/不确定 / local)：Guarantee valid JSON/XML/code structure during generation, use Pydantic models for type-safe outputs, support local mode…
- `serving-llms-vllm` (通用安装/不确定 / local)：vLLM: high-throughput LLM serving, OpenAI API, quantization.
- `audiocraft-audio-generation` (通用安装/不确定 / local)：AudioCraft: MusicGen text-to-music, AudioGen text-to-sound.
- `whisper` (通用安装/不确定 / local)：OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and lan…
- `dspy` (通用安装/不确定 / local)：DSPy: declarative LM programs, auto-optimize prompts, RAG.
- `axolotl` (通用安装/不确定 / local)：Expert guidance for fine-tuning LLMs with Axolotl - YAML configs, 100+ models, LoRA/QLoRA, DPO/KTO/ORPO/GRPO, multimodal…
- `grpo-rl-training` (通用安装/不确定 / local)：Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training
- `peft-fine-tuning` (通用安装/不确定 / local)：Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) …
- `pytorch-fsdp` (通用安装/不确定 / local)：Expert guidance for Fully Sharded Data Parallel training with PyTorch FSDP - parameter sharding, mixed precision, CPU of…
- `fine-tuning-with-trl` (通用安装/不确定 / local)：Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRP…
- `unsloth` (通用安装/不确定 / local)：Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization
- `airtable` (通用安装/不确定 / local)：Airtable REST API via curl. Records CRUD, filters, upserts.
- `client-facing-excel-reporting` (通用安装/不确定 / local)：Create or polish client-facing Excel workbooks from raw business/operations data, especially e-commerce or advertising r…
- `feishu-cli-isolated-config` (个人/项目自定义 / local)：Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentia…
- `google-workspace` (通用安装/不确定 / local)：Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.
- `hermes-feishu-gateway-setup` (个人/项目自定义 / local)：Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credential…
- `linear` (通用安装/不确定 / local)：Linear: manage issues, projects, teams via GraphQL + curl.
- `macos-wechat-cli` (个人/项目自定义 / local)：Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to ins…
- `macos-wechat-history-decrypt` (个人/项目自定义 / local)：Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process exi…
- `maps` (通用安装/不确定 / local)：Geocode, POIs, routes, timezones via OpenStreetMap/OSRM.
- `nano-pdf` (通用安装/不确定 / local)：Edit PDF text/typos/titles via nano-pdf CLI (NL prompts).
- `node-docx-generation` (通用安装/不确定 / local)：Create polished Microsoft Word .docx files using Node.js and the docx npm package, especially when python-docx is unavai…
- `node-docx-word-output` (通用安装/不确定 / local)：Use Node.js docx package to generate polished Word .docx documents with system fonts, colored callouts, headings, bullet…
- `notion` (通用安装/不确定 / local)：Notion API + ntn CLI: pages, databases, markdown, Workers.
- `ocr-and-documents` (通用安装/不确定 / local)：Extract text from PDFs/scans (pymupdf, marker-pdf).
- `official-lark-cli-feishu-workflows` (个人/项目自定义 / local)：Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenCla…
- `reduce-paid-ratio-link-agent-mvp` (个人/项目自定义 / local)：Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for c…
- `reduce-paid-ratio-plan-evaluator` (个人/项目自定义 / local)：Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from tw…
- `sealseek-feature-compare-doc` (个人/项目自定义 / local)：Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” doc…
- `teams-meeting-pipeline` (通用安装/不确定 / local)：Operate the Teams meeting summary pipeline via Hermes CLI — summarize meetings, inspect pipeline status, replay jobs, ma…
- `godmode` (通用安装/不确定 / local)：Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.
- `arxiv` (通用安装/不确定 / local)：Search arXiv papers by keyword, author, category, or ID.
- `blogwatcher` (通用安装/不确定 / local)：Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.
- `polymarket` (通用安装/不确定 / local)：Query Polymarket: markets, prices, orderbooks, history.
- `openhue` (通用安装/不确定 / local)：Control Philips Hue lights, scenes, rooms via OpenHue CLI.
- `xitter` (通用安装/不确定 / local)：Interact with X/Twitter via the x-cli terminal client using official X API credentials. Use for posting, reading timelin…
- `xurl` (通用安装/不确定 / local)：X/Twitter via xurl CLI: post, search, DM, media, v2 API.
- `cross-agent-skill-packaging` (个人/项目自定义 / local)：Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when pu…
- `debugging-hermes-tui-commands` (通用安装/不确定 / local)：Debug Hermes TUI slash commands: Python, gateway, Ink UI.
- `hermes-agent-skill-authoring` (通用安装/不确定 / local)：Author in-repo SKILL.md: frontmatter, validator, structure.
- `node-inspect-debugger` (通用安装/不确定 / local)：Debug Node.js via --inspect + Chrome DevTools Protocol CLI.
- `plan` (通用安装/不确定 / local)：Plan mode: write markdown plan to .hermes/plans/, no exec.
- `python-debugpy` (通用安装/不确定 / local)：Debug Python: pdb REPL + debugpy remote (DAP).
- `requesting-code-review` (通用安装/不确定 / local)：Pre-commit review: security scan, quality gates, auto-fix.
- `spike` (通用安装/不确定 / local)：Throwaway experiments to validate an idea before build.
- `stateful-skill-runner-pattern` (通用安装/不确定 / local)：Build a lightweight file-backed state-machine runner for multi-turn skills so user branch choices resume the intended wo…
- `subagent-driven-development` (通用安装/不确定 / local)：Execute plans via delegate_task subagents (2-stage review).
- `systematic-debugging` (通用安装/不确定 / local)：4-phase root cause debugging: understand bugs before fixing.
- `test-driven-development` (通用安装/不确定 / local)：TDD: enforce RED-GREEN-REFACTOR, tests before code.
- `writing-plans` (通用安装/不确定 / local)：Write implementation plans: bite-sized tasks, paths, code.
- `yuanbao` (通用安装/不确定 / local)：Yuanbao (元宝) groups: @mention users, query info/members.

## Skill 详情

### `ecommerce-single-image-optimization`

- Agent / 环境：Hermes
- 归属分类：归档/备份
- 归属依据：路径或来源类型显示为备份/归档，不作为日常优先使用 skill。
- 来源类型：archived-or-backup
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/_archived_confusing_skills/ecommerce-single-image-optimization__20260501-165300/SKILL.md`
- 功能检索描述：Design and iterate a reusable e-commerce single-image optimization workflow. Use when building or running a skill that takes one existing product image, analyzes its current communication task, offers optimization routes, then generates an optimized final image. Emphasizes intent preservation so the output does not drift away from what the original image was trying to sell.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-single-image-optimization E-commerce Single-Image Optimization Design and iterate a reusable e-commerce single-image optimization workflow. Use when building or running a skill that takes one existing product image, analyzes its current communication task, offers optimization routes, then generates an optimized final image. Emphasizes intent preservation so the output does not drift away from what the original image was trying to sell. _archived_confusing_skills/ecommerce-single-image-optimization__20260501-165300/SKILL.md archived-or-backup

### `apple-notes`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/apple/apple-notes/SKILL.md`
- 功能检索描述：Manage Apple Notes via memo CLI: create, search, edit.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：apple-notes Apple Notes Manage Apple Notes via memo CLI: create, search, edit. apple/apple-notes/SKILL.md local

### `apple-reminders`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/apple/apple-reminders/SKILL.md`
- 功能检索描述：Apple Reminders via remindctl: add, list, complete.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：apple-reminders Apple Reminders Apple Reminders via remindctl: add, list, complete. apple/apple-reminders/SKILL.md local

### `findmy`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/apple/findmy/SKILL.md`
- 功能检索描述：Track Apple devices/AirTags via FindMy.app on macOS.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：findmy Find My (Apple) Track Apple devices/AirTags via FindMy.app on macOS. apple/findmy/SKILL.md local

### `imessage`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/apple/imessage/SKILL.md`
- 功能检索描述：Send and receive iMessages/SMS via the imsg CLI on macOS.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：imessage iMessage Send and receive iMessages/SMS via the imsg CLI on macOS. apple/imessage/SKILL.md local

### `macos-computer-use`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/apple/macos-computer-use/SKILL.md`
- 功能检索描述：Drive the macOS desktop in the background — screenshots, mouse, keyboard, scroll, drag — without stealing the user's cursor, keyboard focus, or Space. Works with any tool-capable model. Load this skill whenever the `computer_use` tool is available.
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：macos-computer-use macOS Computer Use (universal, any-model) Drive the macOS desktop in the background — screenshots, mouse, keyboard, scroll, drag — without stealing the user's cursor, keyboard focus, or Space. Works with any tool-capable model. Load this skill whenever the computer_use tool is available. apple/macos-computer-use/SKILL.md local

### `claude-code`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/autonomous-ai-agents/claude-code/SKILL.md`
- 功能检索描述：Delegate coding to Claude Code CLI (features, PRs).
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：claude-code Claude Code — Hermes Orchestration Guide Delegate coding to Claude Code CLI (features, PRs). autonomous-ai-agents/claude-code/SKILL.md local

### `codex`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/autonomous-ai-agents/codex/SKILL.md`
- 功能检索描述：Delegate coding to OpenAI Codex CLI (features, PRs).
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：codex Codex CLI Delegate coding to OpenAI Codex CLI (features, PRs). autonomous-ai-agents/codex/SKILL.md local

### `hermes-agent`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/autonomous-ai-agents/hermes-agent/SKILL.md`
- 功能检索描述：Complete guide to using and extending Hermes Agent — CLI usage, setup, configuration, spawning additional agents, gateway platforms, skills, voice, tools, profiles, and a concise contributor reference. Load this skill when helping users configure Hermes, troubleshoot issues, spawn agent instances, or make code contributions.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-agent Hermes Agent Complete guide to using and extending Hermes Agent — CLI usage, setup, configuration, spawning additional agents, gateway platforms, skills, voice, tools, profiles, and a concise contributor reference. Load this skill when helping users configure Hermes, troubleshoot issues, spawn agent instances, or make code contributions. autonomous-ai-agents/hermes-agent/SKILL.md local

### `hermes-custom-provider-validation`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/autonomous-ai-agents/hermes-custom-provider-validation/SKILL.md`
- 功能检索描述：Validate Hermes custom model providers (especially Gemini/OpenAI-compatible relays) for real usability, latency, and output quality before relying on them for HTML reports, frontend generation, or multi-agent routing.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-custom-provider-validation Validate Hermes custom model providers (especially Gemini/OpenAI-compatible relays) for real usability, latency, and output quality before relying on them for HTML reports, frontend generation, or multi-agent routing. autonomous-ai-agents/hermes-custom-provider-validation/SKILL.md local

### `hermes-model-provider-diagnostics`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/autonomous-ai-agents/hermes-model-provider-diagnostics/SKILL.md`
- 功能检索描述：Diagnose Hermes model/provider behavior: effective context windows, provider-specific caps, routing surprises, and config-vs-runtime mismatches before recommending model changes.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-model-provider-diagnostics Hermes Model Provider Diagnostics Diagnose Hermes model/provider behavior: effective context windows, provider-specific caps, routing surprises, and config-vs-runtime mismatches before recommending model changes. autonomous-ai-agents/hermes-model-provider-diagnostics/SKILL.md local

### `kanban-codex-lane`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/autonomous-ai-agents/kanban-codex-lane/SKILL.md`
- 功能检索描述：Use when a Hermes Kanban worker wants to run Codex CLI as an isolated implementation lane while Hermes keeps ownership of task lifecycle, reconciliation, testing, and handoff.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：kanban-codex-lane Kanban Codex Lane Use when a Hermes Kanban worker wants to run Codex CLI as an isolated implementation lane while Hermes keeps ownership of task lifecycle, reconciliation, testing, and handoff. autonomous-ai-agents/kanban-codex-lane/SKILL.md local

### `opencode`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/autonomous-ai-agents/opencode/SKILL.md`
- 功能检索描述：Delegate coding to OpenCode CLI (features, PR review).
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：opencode OpenCode CLI Delegate coding to OpenCode CLI (features, PR review). autonomous-ai-agents/opencode/SKILL.md local

### `architecture-diagram`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/architecture-diagram/SKILL.md`
- 功能检索描述：Dark-themed SVG architecture/cloud/infra diagrams as HTML.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：architecture-diagram Architecture Diagram Skill Dark-themed SVG architecture/cloud/infra diagrams as HTML. creative/architecture-diagram/SKILL.md local

### `ascii-art`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/ascii-art/SKILL.md`
- 功能检索描述：ASCII art: pyfiglet, cowsay, boxes, image-to-ascii.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：ascii-art ASCII Art Skill ASCII art: pyfiglet, cowsay, boxes, image-to-ascii. creative/ascii-art/SKILL.md local

### `ascii-video`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/ascii-video/SKILL.md`
- 功能检索描述：ASCII video: convert video/audio to colored ASCII MP4/GIF.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：ascii-video ASCII Video Production Pipeline ASCII video: convert video/audio to colored ASCII MP4/GIF. creative/ascii-video/SKILL.md local

### `baoyu-article-illustrator`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-article-illustrator/SKILL.md`
- 功能检索描述：Article illustrations: type × style × palette consistency.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：baoyu-article-illustrator Article Illustrator Article illustrations: type × style × palette consistency. creative/baoyu-article-illustrator/SKILL.md local

### `baoyu-comic`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-comic/SKILL.md`
- 功能检索描述：Knowledge comics (知识漫画): educational, biography, tutorial.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求
- 检索关键词：baoyu-comic Knowledge Comic Creator Knowledge comics (知识漫画): educational, biography, tutorial. creative/baoyu-comic/SKILL.md local

### `baoyu-infographic`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/baoyu-infographic/SKILL.md`
- 功能检索描述：Infographics: 21 layouts x 21 styles (信息图, 可视化).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：baoyu-infographic Infographic Generator Infographics: 21 layouts x 21 styles (信息图, 可视化). creative/baoyu-infographic/SKILL.md local

### `claude-design`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/claude-design/SKILL.md`
- 功能检索描述：Design one-off HTML artifacts (landing, deck, prototype).
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：claude-design Claude Design for CLI/API Agents Design one-off HTML artifacts (landing, deck, prototype). creative/claude-design/SKILL.md local

### `comfyui`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/comfyui/SKILL.md`
- 功能检索描述：Generate images, video, and audio with ComfyUI — install, launch, manage nodes/models, run workflows with parameter injection. Uses the official comfy-cli for lifecycle and direct REST/WebSocket API for execution.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：comfyui ComfyUI Generate images, video, and audio with ComfyUI — install, launch, manage nodes/models, run workflows with parameter injection. Uses the official comfy-cli for lifecycle and direct REST/WebSocket API for execution. creative/comfyui/SKILL.md local

### `ideation`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/creative-ideation/SKILL.md`
- 功能检索描述：Generate project ideas via creative constraints.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：ideation Creative Ideation Generate project ideas via creative constraints. creative/creative-ideation/SKILL.md local

### `dashscope-happyhorse-video`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/dashscope-happyhorse-video/SKILL.md`
- 功能检索描述：Research and use Alibaba Cloud DashScope / Model Studio HappyHorse 1.0 video generation and editing APIs with DASHSCOPE_API_KEY. Covers model IDs, async task flow, curl/Python examples, polling, and common pitfalls.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：dashscope-happyhorse-video DashScope HappyHorse 1.0 Video API Research and use Alibaba Cloud DashScope / Model Studio HappyHorse 1.0 video generation and editing APIs with DASHSCOPE_API_KEY. Covers model IDs, async task flow, curl/Python examples, polling, and common pitfalls. creative/dashscope-happyhorse-video/SKILL.md local

### `design-md`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/design-md/SKILL.md`
- 功能检索描述：Author/validate/export Google's DESIGN.md token spec files.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：design-md DESIGN.md Skill Author/validate/export Google's DESIGN.md token spec files. creative/design-md/SKILL.md local

### `detail-page-batch-optimization`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/detail-page-batch-optimization/SKILL.md`
- 功能检索描述：Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：detail-page-batch-optimization Detail Page Batch Optimization Orchestrate batch optimization of a same-product e-commerce detail-page image set. Use one batch-wide route, shared product/style/typography constraints, and call single-image-optimization in batch_worker mode for each image. Designed for multi-image detail pages that must stay visually and commercially consistent. creative/detail-page-batch-optimization/SKILL.md local

### `ecommerce-image-skill-architecture`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/ecommerce-image-skill-architecture/SKILL.md`
- 功能检索描述：Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use when designing or refactoring agent skills for product-image analysis, route selection, prompt planning, and staged image generation.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-image-skill-architecture E-commerce Image Skill Architecture Architect an e-commerce image optimization/generation skill as a phased harness, not a single monolithic workflow. Use when designing or refactoring agent skills for product-image analysis, route selection, prompt planning, and staged image generation. creative/ecommerce-image-skill-architecture/SKILL.md local

### `evolink-gpt-image-2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/evolink-gpt-image-2/SKILL.md`
- 功能检索描述：Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and test script locations.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：evolink-gpt-image-2 Use EvoLink.AI GPT Image 2 through its async image generation API; covers docs lookup, config files, task polling, and test script locations. creative/evolink-gpt-image-2/SKILL.md local

### `excalidraw`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/excalidraw/SKILL.md`
- 功能检索描述：Hand-drawn Excalidraw JSON diagrams (arch, flow, seq).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：excalidraw Excalidraw Diagram Skill Hand-drawn Excalidraw JSON diagrams (arch, flow, seq). creative/excalidraw/SKILL.md local

### `gpt-image-2-12api`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/gpt-image-2-12api/SKILL.md`
- 功能检索描述：Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavior, reproducible probing, and known channel quirks.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：gpt-image-2-12api Investigate and use GPT Image 2 through 12API. Covers auth, endpoint differences from Gemini, key-group fallback behavior, reproducible probing, and known channel quirks. creative/gpt-image-2-12api/SKILL.md local

### `gpt生图`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/gpt生图/SKILL.md`
- 功能检索描述：Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, design, or produce any image, illustration, photo, artwork, diagram, infographic, logo, poster, or visual content. Also use when asked to edit, modify, restyle, or transform an existing image. GPT Image 2 is the primary and only generation model in this skill. Supports text-to-image, reference-image generation, local-reference upload, transparent PNG output, and multi-turn iteration. Outputs PNG files.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：gpt生图 GPT Image 2 Generation Generate, edit, and iterate on images using GPT Image 2 via ToAPIs. Use when the user asks to create, generate, draw, design, or produce any image, illustration, photo, artwork, diagram, infographic, logo, poster, or visual content. Also use when asked to edit, modify, restyle, or transform an existing image. GPT Image 2 is the primary and only generation model in this skill. Supports text-to-image, reference-image generation, local-reference upload, transparent PNG output, and multi-turn iteration. Outputs PNG files. creative/gpt生图/SKILL.md local

### `humanizer`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/humanizer/SKILL.md`
- 功能检索描述：Humanize text: strip AI-isms and add real voice.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：humanizer Humanizer: Remove AI Writing Patterns Humanize text: strip AI-isms and add real voice. creative/humanizer/SKILL.md local

### `lingerie-model-product-replacement`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/lingerie-model-product-replacement/SKILL.md`
- 功能检索描述：Test and run safer workflows for replacing bras/lingerie products on model images, avoiding unstable full-face intimate-apparel reference edits.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：lingerie-model-product-replacement Lingerie / Bra Product Replacement on Model Images Test and run safer workflows for replacing bras/lingerie products on model images, avoiding unstable full-face intimate-apparel reference edits. creative/lingerie-model-product-replacement/SKILL.md local

### `manim-video`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/manim-video/SKILL.md`
- 功能检索描述：Manim CE animations: 3Blue1Brown math/algo videos.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：manim-video Manim Video Production Pipeline Manim CE animations: 3Blue1Brown math/algo videos. creative/manim-video/SKILL.md local

### `p5js`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/p5js/SKILL.md`
- 功能检索描述：p5.js sketches: gen art, shaders, interactive, 3D.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：p5js p5.js Production Pipeline p5.js sketches: gen art, shaders, interactive, 3D. creative/p5js/SKILL.md local

### `pixel-art`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/pixel-art/SKILL.md`
- 功能检索描述：Pixel art w/ era palettes (NES, Game Boy, PICO-8).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：pixel-art Pixel Art Pixel art w/ era palettes (NES, Game Boy, PICO-8). creative/pixel-art/SKILL.md local

### `popular-web-designs`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/popular-web-designs/SKILL.md`
- 功能检索描述：54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：popular-web-designs Popular Web Designs 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS. creative/popular-web-designs/SKILL.md local

### `pretext`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/pretext/SKILL.md`
- 功能检索描述：Use when building creative browser demos with @chenglou/pretext — DOM-free text layout for ASCII art, typographic flow around obstacles, text-as-geometry games, kinetic typography, and text-powered generative art. Produces single-file HTML demos by default.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：pretext Pretext Creative Demos Use when building creative browser demos with @chenglou/pretext — DOM-free text layout for ASCII art, typographic flow around obstacles, text-as-geometry games, kinetic typography, and text-powered generative art. Produces single-file HTML demos by default. creative/pretext/SKILL.md local

### `shopping-basket-visual-planning`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/shopping-basket-visual-planning/SKILL.md`
- 功能检索描述：Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the user needs to know what other products, brands, scenes, or content to study BEFORE visual collection, visual decomposition, or shooting planning.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：shopping-basket-visual-planning Shopping Basket Visual Reference Discovery Discover e-commerce visual reference sources using the “shopping basket” / consumer relationship model. Use when the user needs to know what other products, brands, scenes, or content to study BEFORE visual collection, visual decomposition, or shooting planning. creative/shopping-basket-visual-planning/SKILL.md local

### `single-image-optimization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/single-image-optimization/SKILL.md`
- 功能检索描述：Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：single-image-optimization Single Image Optimization Optimize one e-commerce image at a time through a structured workflow: analyze the image, extract page intent/product/style, propose optimization routes, let the user choose a route, generate a prompt plan, then produce the final image with GPT-image-2 using the source image as reference. Supports optional user-provided style reference images for multi-image visual consistency across a detail page. creative/single-image-optimization/SKILL.md local

### `sketch`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/sketch/SKILL.md`
- 功能检索描述：Throwaway HTML mockups: 2-3 design variants to compare.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：sketch Sketch Throwaway HTML mockups: 2-3 design variants to compare. creative/sketch/SKILL.md local

### `songwriting-and-ai-music`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/songwriting-and-ai-music/SKILL.md`
- 功能检索描述：Songwriting craft and Suno AI music prompts.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：songwriting-and-ai-music Songwriting & AI Music Generation Songwriting craft and Suno AI music prompts. creative/songwriting-and-ai-music/SKILL.md local

### `taobao-gpt-image-creative-main-image`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/taobao-gpt-image-creative-main-image/SKILL.md`
- 功能检索描述：Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably via post-processing to avoid AI text乱码.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-gpt-image-creative-main-image Add tag pills as needed... Create Taobao/e-commerce 1:1 creative main images from product refs using GPT Image 2, with Chinese copy added reliably via post-processing to avoid AI text乱码. creative/taobao-gpt-image-creative-main-image/SKILL.md local

### `toapis-gpt-image-2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/toapis-gpt-image-2/SKILL.md`
- 功能检索描述：Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working request formats, task polling, local-image upload flow, supported sizes/quality/background, and known limitations discovered by live testing.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：toapis-gpt-image-2 Use ToAPIs gpt-image-2 for text-to-image and reference-image generation via an async task workflow. Covers working request formats, task polling, local-image upload flow, supported sizes/quality/background, and known limitations discovered by live testing. creative/toapis-gpt-image-2/SKILL.md local

### `touchdesigner-mcp`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/creative/touchdesigner-mcp/SKILL.md`
- 功能检索描述：Control a running TouchDesigner instance via twozero MCP — create operators, set parameters, wire connections, execute Python, build real-time visuals. 36 native tools.
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求
- 检索关键词：touchdesigner-mcp TouchDesigner Integration (twozero MCP) Control a running TouchDesigner instance via twozero MCP — create operators, set parameters, wire connections, execute Python, build real-time visuals. 36 native tools. creative/touchdesigner-mcp/SKILL.md local

### `jupyter-live-kernel`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/data-science/jupyter-live-kernel/SKILL.md`
- 功能检索描述：Iterative Python via live Jupyter kernel (hamelnb).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：jupyter-live-kernel Jupyter Live Kernel (hamelnb) Iterative Python via live Jupyter kernel (hamelnb). data-science/jupyter-live-kernel/SKILL.md local

### `kanban-orchestrator`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/devops/kanban-orchestrator/SKILL.md`
- 功能检索描述：Decomposition playbook + anti-temptation rules for an orchestrator profile routing work through Kanban. The "don't do the work yourself" rule and the basic lifecycle are auto-injected into every kanban worker's system prompt; this skill is the deeper playbook when you're specifically playing the orchestrator role.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：kanban-orchestrator Kanban Orchestrator — Decomposition Playbook Decomposition playbook + anti-temptation rules for an orchestrator profile routing work through Kanban. The "don't do the work yourself" rule and the basic lifecycle are auto-injected into every kanban worker's system prompt; this skill is the deeper playbook when you're specifically playing the orchestrator role. devops/kanban-orchestrator/SKILL.md local

### `kanban-worker`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/devops/kanban-worker/SKILL.md`
- 功能检索描述：Pitfalls, examples, and edge cases for Hermes Kanban workers. The lifecycle itself is auto-injected into every worker's system prompt as KANBAN_GUIDANCE (from agent/prompt_builder.py); this skill is what you load when you want deeper detail on specific scenarios.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：kanban-worker Kanban Worker — Pitfalls and Examples Pitfalls, examples, and edge cases for Hermes Kanban workers. The lifecycle itself is auto-injected into every worker's system prompt as KANBAN_GUIDANCE (from agent/prompt_builder.py); this skill is what you load when you want deeper detail on specific scenarios. devops/kanban-worker/SKILL.md local

### `webhook-subscriptions`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/devops/webhook-subscriptions/SKILL.md`
- 功能检索描述：Webhook subscriptions: event-driven agent runs.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：webhook-subscriptions Webhook Subscriptions Webhook subscriptions: event-driven agent runs. devops/webhook-subscriptions/SKILL.md local

### `dogfood`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/dogfood/SKILL.md`
- 功能检索描述：Systematic exploratory QA testing of web applications — find bugs, capture evidence, and generate structured reports
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：dogfood Dogfood: Systematic Web Application QA Testing Systematic exploratory QA testing of web applications — find bugs, capture evidence, and generate structured reports dogfood/SKILL.md local

### `hermes-platform-tool-availability-debugging`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/dogfood/hermes-platform-tool-availability-debugging/SKILL.md`
- 功能检索描述：Diagnose why Hermes on a messaging platform used the wrong tool (for example vision_analyze instead of image_generate) or why a tool appears enabled globally but is missing from an actual session.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-platform-tool-availability-debugging Diagnose why Hermes on a messaging platform used the wrong tool (for example vision_analyze instead of image_generate) or why a tool appears enabled globally but is missing from an actual session. dogfood/hermes-platform-tool-availability-debugging/SKILL.md local

### `himalaya`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/email/himalaya/SKILL.md`
- 功能检索描述：Himalaya CLI: IMAP/SMTP email from terminal.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：himalaya Himalaya Email CLI Himalaya CLI: IMAP/SMTP email from terminal. email/himalaya/SKILL.md local

### `minecraft-modpack-server`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/gaming/minecraft-modpack-server/SKILL.md`
- 功能检索描述：Host modded Minecraft servers (CurseForge, Modrinth).
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求
- 检索关键词：minecraft-modpack-server Minecraft Modpack Server Setup Host modded Minecraft servers (CurseForge, Modrinth). gaming/minecraft-modpack-server/SKILL.md local

### `pokemon-player`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/gaming/pokemon-player/SKILL.md`
- 功能检索描述：Play Pokemon via headless emulator + RAM reads.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：pokemon-player Pokemon Player Play Pokemon via headless emulator + RAM reads. gaming/pokemon-player/SKILL.md local

### `codebase-inspection`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/github/codebase-inspection/SKILL.md`
- 功能检索描述：Inspect codebases w/ pygount: LOC, languages, ratios.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：codebase-inspection Codebase Inspection with pygount Inspect codebases w/ pygount: LOC, languages, ratios. github/codebase-inspection/SKILL.md local

### `github-auth`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/github/github-auth/SKILL.md`
- 功能检索描述：GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：github-auth GitHub Authentication Setup GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login. github/github-auth/SKILL.md local

### `github-code-review`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/github/github-code-review/SKILL.md`
- 功能检索描述：Review PRs: diffs, inline comments via gh or REST.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：github-code-review GitHub Code Review Review PRs: diffs, inline comments via gh or REST. github/github-code-review/SKILL.md local

### `github-issues`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/github/github-issues/SKILL.md`
- 功能检索描述：Create, triage, label, assign GitHub issues via gh or REST.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：github-issues GitHub Issues Management Create, triage, label, assign GitHub issues via gh or REST. github/github-issues/SKILL.md local

### `github-pr-workflow`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/github/github-pr-workflow/SKILL.md`
- 功能检索描述：GitHub PR lifecycle: branch, commit, open, CI, merge.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：github-pr-workflow GitHub Pull Request Workflow GitHub PR lifecycle: branch, commit, open, CI, merge. github/github-pr-workflow/SKILL.md local

### `github-repo-management`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/github/github-repo-management/SKILL.md`
- 功能检索描述：Clone/create/fork repos; manage remotes, releases.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：github-repo-management GitHub Repository Management Clone/create/fork repos; manage remotes, releases. github/github-repo-management/SKILL.md local

### `find-nearby`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/leisure/find-nearby/SKILL.md`
- 功能检索描述：Find nearby places (restaurants, cafes, bars, pharmacies, etc.) using OpenStreetMap. Works with coordinates, addresses, cities, zip codes, or Telegram location pins. No API keys needed.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：find-nearby Find Nearby — Local Place Discovery Find nearby places (restaurants, cafes, bars, pharmacies, etc.) using OpenStreetMap. Works with coordinates, addresses, cities, zip codes, or Telegram location pins. No API keys needed. leisure/find-nearby/SKILL.md local

### `mcporter`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mcp/mcporter/SKILL.md`
- 功能检索描述：Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation.
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求
- 检索关键词：mcporter mcporter Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation. mcp/mcporter/SKILL.md local

### `native-mcp`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mcp/native-mcp/SKILL.md`
- 功能检索描述：MCP client: connect servers, register tools (stdio/HTTP).
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求
- 检索关键词：native-mcp Native MCP Client MCP client: connect servers, register tools (stdio/HTTP). mcp/native-mcp/SKILL.md local

### `gif-search`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/media/gif-search/SKILL.md`
- 功能检索描述：Search/download GIFs from Tenor via curl + jq.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：gif-search GIF Search (Tenor API) Search/download GIFs from Tenor via curl + jq. media/gif-search/SKILL.md local

### `heartmula`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/media/heartmula/SKILL.md`
- 功能检索描述：HeartMuLa: Suno-like song generation from lyrics + tags.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：heartmula HeartMuLa - Open-Source Music Generation HeartMuLa: Suno-like song generation from lyrics + tags. media/heartmula/SKILL.md local

### `songsee`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/media/songsee/SKILL.md`
- 功能检索描述：Audio spectrograms/features (mel, chroma, MFCC) via CLI.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：songsee songsee Audio spectrograms/features (mel, chroma, MFCC) via CLI. media/songsee/SKILL.md local

### `spotify`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/media/spotify/SKILL.md`
- 功能检索描述：Spotify: play, search, queue, manage playlists and devices.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：spotify Spotify Spotify: play, search, queue, manage playlists and devices. media/spotify/SKILL.md local

### `youtube-content`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/media/youtube-content/SKILL.md`
- 功能检索描述：YouTube transcripts to summaries, threads, blogs.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：youtube-content YouTube Content Tool YouTube transcripts to summaries, threads, blogs. media/youtube-content/SKILL.md local

### `modal-serverless-gpu`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/cloud/modal/SKILL.md`
- 功能检索描述：Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs with automatic scaling.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；MCP server、工具配置、连接或封装需求
- 检索关键词：modal-serverless-gpu Modal Serverless GPU Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs with automatic scaling. mlops/cloud/modal/SKILL.md local

### `evaluating-llms-harness`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/evaluation/lm-evaluation-harness/SKILL.md`
- 功能检索描述：lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：evaluating-llms-harness lm-evaluation-harness - LLM Benchmarking lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.). mlops/evaluation/lm-evaluation-harness/SKILL.md local

### `weights-and-biases`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/evaluation/weights-and-biases/SKILL.md`
- 功能检索描述：W&B: log ML experiments, sweeps, model registry, dashboards.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：weights-and-biases Weights & Biases: ML Experiment Tracking & MLOps W&B: log ML experiments, sweeps, model registry, dashboards. mlops/evaluation/weights-and-biases/SKILL.md local

### `huggingface-hub`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/huggingface-hub/SKILL.md`
- 功能检索描述：HuggingFace hf CLI: search/download/upload models, datasets.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：huggingface-hub Hugging Face CLI ( hf ) Reference Guide HuggingFace hf CLI: search/download/upload models, datasets. mlops/huggingface-hub/SKILL.md local

### `gguf-quantization`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/inference/gguf/SKILL.md`
- 功能检索描述：GGUF format and llama.cpp quantization for efficient CPU/GPU inference. Use when deploying models on consumer hardware, Apple Silicon, or when needing flexible quantization from 2-8 bit without GPU requirements.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：gguf-quantization GGUF - Quantization Format for llama.cpp GGUF format and llama.cpp quantization for efficient CPU/GPU inference. Use when deploying models on consumer hardware, Apple Silicon, or when needing flexible quantization from 2-8 bit without GPU requirements. mlops/inference/gguf/SKILL.md local

### `guidance`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/inference/guidance/SKILL.md`
- 功能检索描述：Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build multi-step workflows with Guidance - Microsoft Research's constrained generation framework
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：guidance Guidance: Constrained LLM Generation Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build multi-step workflows with Guidance - Microsoft Research's constrained generation framework mlops/inference/guidance/SKILL.md local

### `llama-cpp`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/inference/llama-cpp/SKILL.md`
- 功能检索描述：llama.cpp local GGUF inference + HF Hub model discovery.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：llama-cpp llama.cpp + GGUF llama.cpp local GGUF inference + HF Hub model discovery. mlops/inference/llama-cpp/SKILL.md local

### `obliteratus`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/inference/obliteratus/SKILL.md`
- 功能检索描述：OBLITERATUS: abliterate LLM refusals (diff-in-means).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：obliteratus OBLITERATUS Skill OBLITERATUS: abliterate LLM refusals (diff-in-means). mlops/inference/obliteratus/SKILL.md local

### `outlines`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/inference/outlines/SKILL.md`
- 功能检索描述：Guarantee valid JSON/XML/code structure during generation, use Pydantic models for type-safe outputs, support local models (Transformers, vLLM), and maximize inference speed with Outlines - dottxt.ai's structured generation library
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：outlines Outlines: Structured Text Generation Guarantee valid JSON/XML/code structure during generation, use Pydantic models for type-safe outputs, support local models (Transformers, vLLM), and maximize inference speed with Outlines - dottxt.ai's structured generation library mlops/inference/outlines/SKILL.md local

### `serving-llms-vllm`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/inference/vllm/SKILL.md`
- 功能检索描述：vLLM: high-throughput LLM serving, OpenAI API, quantization.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：serving-llms-vllm vLLM - High-Performance LLM Serving vLLM: high-throughput LLM serving, OpenAI API, quantization. mlops/inference/vllm/SKILL.md local

### `audiocraft-audio-generation`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/models/audiocraft/SKILL.md`
- 功能检索描述：AudioCraft: MusicGen text-to-music, AudioGen text-to-sound.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：audiocraft-audio-generation AudioCraft: Audio Generation AudioCraft: MusicGen text-to-music, AudioGen text-to-sound. mlops/models/audiocraft/SKILL.md local

### `clip`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/models/clip/SKILL.md`
- 功能检索描述：OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval. Trained on 400M image-text pairs. Use for image search, content moderation, or vision-language tasks without fine-tuning. Best for general-purpose image understanding.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：clip CLIP - Contrastive Language-Image Pre-Training OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval. Trained on 400M image-text pairs. Use for image search, content moderation, or vision-language tasks without fine-tuning. Best for general-purpose image understanding. mlops/models/clip/SKILL.md local

### `segment-anything-model`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/models/segment-anything/SKILL.md`
- 功能检索描述：SAM: zero-shot image segmentation via points, boxes, masks.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：segment-anything-model Segment Anything Model (SAM) SAM: zero-shot image segmentation via points, boxes, masks. mlops/models/segment-anything/SKILL.md local

### `stable-diffusion-image-generation`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/models/stable-diffusion/SKILL.md`
- 功能检索描述：State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translation, inpainting, or building custom diffusion pipelines.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求
- 检索关键词：stable-diffusion-image-generation Stable Diffusion Image Generation State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translation, inpainting, or building custom diffusion pipelines. mlops/models/stable-diffusion/SKILL.md local

### `whisper`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/models/whisper/SKILL.md`
- 功能检索描述：OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and language identification. Six model sizes from tiny (39M params) to large (1550M params). Use for speech-to-text, podcast transcription, or multilingual audio processing. Best for robust, multilingual ASR.
- 输入 / 触发方式：音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：whisper Whisper - Robust Speech Recognition OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and language identification. Six model sizes from tiny (39M params) to large (1550M params). Use for speech-to-text, podcast transcription, or multilingual audio processing. Best for robust, multilingual ASR. mlops/models/whisper/SKILL.md local

### `dspy`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/research/dspy/SKILL.md`
- 功能检索描述：DSPy: declarative LM programs, auto-optimize prompts, RAG.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：dspy DSPy: Declarative Language Model Programming DSPy: declarative LM programs, auto-optimize prompts, RAG. mlops/research/dspy/SKILL.md local

### `axolotl`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/training/axolotl/SKILL.md`
- 功能检索描述：Expert guidance for fine-tuning LLMs with Axolotl - YAML configs, 100+ models, LoRA/QLoRA, DPO/KTO/ORPO/GRPO, multimodal support
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：axolotl Axolotl Skill Expert guidance for fine-tuning LLMs with Axolotl - YAML configs, 100+ models, LoRA/QLoRA, DPO/KTO/ORPO/GRPO, multimodal support mlops/training/axolotl/SKILL.md local

### `grpo-rl-training`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/training/grpo-rl-training/SKILL.md`
- 功能检索描述：Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：grpo-rl-training GRPO/RL Training with TRL Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training mlops/training/grpo-rl-training/SKILL.md local

### `peft-fine-tuning`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/training/peft/SKILL.md`
- 功能检索描述：Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) with limited GPU memory, when you need to train <1% of parameters with minimal accuracy loss, or for multi-adapter serving. HuggingFace's official library integrated with transformers ecosystem.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：peft-fine-tuning PEFT (Parameter-Efficient Fine-Tuning) Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) with limited GPU memory, when you need to train <1% of parameters with minimal accuracy loss, or for multi-adapter serving. HuggingFace's official library integrated with transformers ecosystem. mlops/training/peft/SKILL.md local

### `pytorch-fsdp`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/training/pytorch-fsdp/SKILL.md`
- 功能检索描述：Expert guidance for Fully Sharded Data Parallel training with PyTorch FSDP - parameter sharding, mixed precision, CPU offloading, FSDP2
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：pytorch-fsdp Pytorch-Fsdp Skill Expert guidance for Fully Sharded Data Parallel training with PyTorch FSDP - parameter sharding, mixed precision, CPU offloading, FSDP2 mlops/training/pytorch-fsdp/SKILL.md local

### `fine-tuning-with-trl`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/training/trl-fine-tuning/SKILL.md`
- 功能检索描述：Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for reward optimization, and reward model training. Use when need RLHF, align model with preferences, or train from human feedback. Works with HuggingFace Transformers.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：fine-tuning-with-trl TRL - Transformer Reinforcement Learning Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for reward optimization, and reward model training. Use when need RLHF, align model with preferences, or train from human feedback. Works with HuggingFace Transformers. mlops/training/trl-fine-tuning/SKILL.md local

### `unsloth`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/mlops/training/unsloth/SKILL.md`
- 功能检索描述：Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：unsloth Unsloth Skill Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization mlops/training/unsloth/SKILL.md local

### `obsidian`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/note-taking/obsidian/SKILL.md`
- 功能检索描述：Read, search, create, and edit notes in the Obsidian vault.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：obsidian Obsidian Vault Read, search, create, and edit notes in the Obsidian vault. note-taking/obsidian/SKILL.md local

### `airtable`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/airtable/SKILL.md`
- 功能检索描述：Airtable REST API via curl. Records CRUD, filters, upserts.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：airtable Airtable — Bases, Tables & Records Airtable REST API via curl. Records CRUD, filters, upserts. productivity/airtable/SKILL.md local

### `client-facing-excel-reporting`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/client-facing-excel-reporting/SKILL.md`
- 功能检索描述：Create or polish client-facing Excel workbooks from raw business/operations data, especially e-commerce or advertising reports. Use when the user asks to improve Excel readability, format store/marketing data, add analysis sheets, or提炼工作价值/经营价值 while preserving source data.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：client-facing-excel-reporting Client-facing Excel reporting Create or polish client-facing Excel workbooks from raw business/operations data, especially e-commerce or advertising reports. Use when the user asks to improve Excel readability, format store/marketing data, add analysis sheets, or提炼工作价值/经营价值 while preserving source data. productivity/client-facing-excel-reporting/SKILL.md local

### `conference-static-html-courseware-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/conference-static-html-courseware-review-loop/SKILL.md`
- 功能检索描述：Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review, Git-backed iteration, and explicit review standards instead of ad-hoc CSS tweaking.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：conference-static-html-courseware-review-loop 大会版静态 HTML 课件重建与审阅闭环 Rebuild training/course decks as standalone static chapter HTML files for conference use, using screenshot-based review, Git-backed iteration, and explicit review standards instead of ad-hoc CSS tweaking. productivity/conference-static-html-courseware-review-loop/SKILL.md local

### `course-html-ppt-16x9-image-pages`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/course-html-ppt-16x9-image-pages/SKILL.md`
- 功能检索描述：Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy slide layouts.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：course-html-ppt-16x9-image-pages Build and debug chapterized course HTML-PPT pages with a centered 16:9 stage, shared assets, and reliable image-heavy slide layouts. productivity/course-html-ppt-16x9-image-pages/SKILL.md local

### `course-transcript-to-knowledge`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/course-transcript-to-knowledge/SKILL.md`
- 功能检索描述：Reconstruct, analyze, and enrich full knowledge systems from course/audio transcripts into Peter's LLM Wiki. Use for class recordings, Get/Feishu notes, or noisy spoken-course material. The goal is NOT summary or simple extraction; it is segmented knowledge reconstruction with coverage tracking and source-language removal.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：course-transcript-to-knowledge Course Transcript to Knowledge Reconstruction Reconstruct, analyze, and enrich full knowledge systems from course/audio transcripts into Peter's LLM Wiki. Use for class recordings, Get/Feishu notes, or noisy spoken-course material. The goal is NOT summary or simple extraction; it is segmented knowledge reconstruction with coverage tracking and source-language removal. productivity/course-transcript-to-knowledge/SKILL.md local

### `douyin-link-to-knowledge`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/douyin-link-to-knowledge/SKILL.md`
- 功能检索描述：Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transcribing/validating content, and reconstructing durable knowledge pages. Trigger on natural-language requests like “帮我把这个抖音内容整理到知识库”.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：douyin-link-to-knowledge Douyin Link to Knowledge Ingest a Douyin video link into Peter's LLM Wiki by resolving the share URL, downloading the video with luminote-style backend logic, transcribing/validating content, and reconstructing durable knowledge pages. Trigger on natural-language requests like “帮我把这个抖音内容整理到知识库”. productivity/douyin-link-to-knowledge/SKILL.md local

### `dual-source-chapterized-html-ppt-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/dual-source-chapterized-html-ppt-courseware/SKILL.md`
- 功能检索描述：Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to avoid renumbering cascades.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：dual-source-chapterized-html-ppt-courseware Build courseware with paired teacher MD + learner HTML-PPT, using chapter-isolated page IDs and split JSON sources to avoid renumbering cascades. productivity/dual-source-chapterized-html-ppt-courseware/SKILL.md local

### `ecommerce-bi-operation-skill-planning`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/ecommerce-bi-operation-skill-planning/SKILL.md`
- 功能检索描述：Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡检 SOPs, priority engines, or product-level diagnostic skills for Taobao/e-commerce operations.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：ecommerce-bi-operation-skill-planning E-commerce BI Operation Skill Planning Plan e-commerce BI AI-agent operation Skills/SOPs from available store/product/promotion data. Use when designing daily巡检 SOPs, priority engines, or product-level diagnostic skills for Taobao/e-commerce operations. productivity/ecommerce-bi-operation-skill-planning/SKILL.md local

### `feishu-cli-isolated-config`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/feishu-cli-isolated-config/SKILL.md`
- 功能检索描述：Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentials; use an isolated config file via FEISHU_CONFIG because the CLI's built-in account support is incomplete.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：feishu-cli-isolated-config Install and configure @fanfanv5/feishu-cli on macOS/Linux without overwriting existing OpenClaw/default Feishu credentials; use an isolated config file via FEISHU_CONFIG because the CLI's built-in account support is incomplete. productivity/feishu-cli-isolated-config/SKILL.md local

### `feishu-product-feature-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/feishu-product-feature-doc/SKILL.md`
- 功能检索描述：Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-oriented copy, callouts, comparison tables, and embedded images via official lark-cli.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：feishu-product-feature-doc 玺承BI特色功能介绍 Create user-facing Feishu product feature introduction docs from screenshots plus rough notes, using concise sales-oriented copy, callouts, comparison tables, and embedded images via official lark-cli. productivity/feishu-product-feature-doc/SKILL.md local

### `goal-driven-daily-report-templates`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/goal-driven-daily-report-templates/SKILL.md`
- 功能检索描述：Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use when Peter asks to design job-specific daily/weekly report templates or examples for e-commerce, operations, design, video,客服,外贸,亚马逊等岗位.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；音视频链接/文件、转录稿、会议纪要或内容处理需求
- 检索关键词：goal-driven-daily-report-templates Goal-Driven Daily Report Templates Create concise goal-driven employee daily report templates, especially for DingTalk/Feishu-style workplace logs. Use when Peter asks to design job-specific daily/weekly report templates or examples for e-commerce, operations, design, video,客服,外贸,亚马逊等岗位. productivity/goal-driven-daily-report-templates/SKILL.md local

### `google-workspace`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/google-workspace/SKILL.md`
- 功能检索描述：Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：google-workspace Google Workspace Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python. productivity/google-workspace/SKILL.md local

### `hermes-feishu-gateway-setup`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-gateway-setup/SKILL.md`
- 功能检索描述：Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credentials; use isolated FEISHU_CONFIG for CLI and FEISHU_* env vars plus platforms.feishu for Hermes gateway.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-feishu-gateway-setup Configure a Feishu/Lark bot app for Hermes Agent and feishu-cli without overwriting existing default/OpenClaw credentials; use isolated FEISHU_CONFIG for CLI and FEISHU_* env vars plus platforms.feishu for Hermes gateway. productivity/hermes-feishu-gateway-setup/SKILL.md local

### `hermes-feishu-session-debugging`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/hermes-feishu-session-debugging/SKILL.md`
- 功能检索描述：Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session JSON files, and tool availability. Use when Feishu shows long-running “Still working...”, when a user says a message got no reply, or when uploaded image+text prompts seem to arrive incorrectly.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求
- 检索关键词：hermes-feishu-session-debugging Hermes Feishu Session Debugging Debug stuck or misrouted Hermes conversations on Feishu/Lark by correlating gateway logs, SQLite session state, session JSON files, and tool availability. Use when Feishu shows long-running “Still working...”, when a user says a message got no reply, or when uploaded image+text prompts seem to arrive incorrectly. productivity/hermes-feishu-session-debugging/SKILL.md local

### `html-course-deck`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-course-deck/SKILL.md`
- 功能检索描述：Create polished browser-based HTML slide decks for courses or presentations when PPTX generation looks rigid, dated, or visually weak. Use for full-screen teaching decks with keyboard/remote clicker navigation, especially when the user cares more about visual quality and presentation flow than editable PowerPoint text.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；已打开网页、浏览器页面、插件功能或页面 API 线索；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：html-course-deck HTML Course Deck Skill Create polished browser-based HTML slide decks for courses or presentations when PPTX generation looks rigid, dated, or visually weak. Use for full-screen teaching decks with keyboard/remote clicker navigation, especially when the user cares more about visual quality and presentation flow than editable PowerPoint text. productivity/html-course-deck/SKILL.md local

### `html-ppt-conference-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-conference-review-loop/SKILL.md`
- 功能检索描述：Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with explicit readability and layout standards for large venue projection.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt-conference-review-loop HTML-PPT Conference Review Loop Build and refine conference-grade HTML-PPT decks by using screenshot-based review instead of code-only judgment, with explicit readability and layout standards for large venue projection. productivity/html-ppt-conference-review-loop/SKILL.md local

### `html-ppt-course-deck`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-course-deck/SKILL.md`
- 功能检索描述：Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid or visually weak. Use slides.json/slides.yaml for content, CSS for fixed templates, browser full-screen for presenting, and optional in-page editing/export. Especially useful when a mandated PPT template must be reproduced as fixed HTML backgrounds.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：html-ppt-course-deck HTML-PPT Course Deck Create editable full-screen HTML presentation decks (“HTML-PPT”) for course delivery when PPTX generation is too rigid or visually weak. Use slides.json/slides.yaml for content, CSS for fixed templates, browser full-screen for presenting, and optional in-page editing/export. Especially useful when a mandated PPT template must be reproduced as fixed HTML backgrounds. productivity/html-ppt-course-deck/SKILL.md local

### `html-ppt-font-standardization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-font-standardization/SKILL.md`
- 功能检索描述：Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run an overflow audit after replacement.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：html-ppt-font-standardization HTML-PPT 字体规范方案 Standardize fonts in an HTML-PPT deck, embed project-local font assets, switch dark-theme text to light colors, and run an overflow audit after replacement. productivity/html-ppt-font-standardization/SKILL.md local

### `html-ppt-screenshot-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-screenshot-review-loop/SKILL.md`
- 功能检索描述：Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-style decks where readability, layout balance, and consistency matter more than code-level aesthetics.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt-screenshot-review-loop Build and refine HTML-PPT decks by reviewing per-slide screenshots instead of judging raw HTML/CSS. Use for conference-style decks where readability, layout balance, and consistency matter more than code-level aesthetics. productivity/html-ppt-screenshot-review-loop/SKILL.md local

### `html-ppt-stage-fit-and-background-cleanup`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-stage-fit-and-background-cleanup/SKILL.md`
- 功能检索描述：Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds with clean backgrounds plus a separate sharp logo layer, and verify stage safety in browser.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；已打开网页、浏览器页面、插件功能或页面 API 线索
- 检索关键词：html-ppt-stage-fit-and-background-cleanup HTML-PPT 固定画布适配与背景去 Logo Fit an HTML-PPT deck to a fixed 16:9 presentation canvas with letterboxing, replace blurry embedded-logo backgrounds with clean backgrounds plus a separate sharp logo layer, and verify stage safety in browser. productivity/html-ppt-stage-fit-and-background-cleanup/SKILL.md local

### `html-ppt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/html-ppt-studio-agentskill/SKILL.md`
- 功能检索描述：HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by templates. Use when the user asks for a presentation, PPT, slides, keynote, deck, slideshow, "幻灯片", "演讲稿", "做一份 PPT", "做一份 slides", a reveal-style HTML deck, a 小红书 图文, or any kind of multi-slide pitch/report/sharing document that should look tasteful and be usable with keyboard navigation. Triggers include keywords like "presentation", "ppt", "slides", "deck", "keynote", "reveal", "slideshow", "幻灯片", "演讲稿", "分享稿", "小红书图文", "talk slides", "pitch deck", "tech sharing", "technical presentation".
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：html-ppt html-ppt — HTML PPT Studio HTML PPT Studio — author professional static HTML presentations in many styles, layouts, and animations, all driven by templates. Use when the user asks for a presentation, PPT, slides, keynote, deck, slideshow, "幻灯片", "演讲稿", "做一份 PPT", "做一份 slides", a reveal-style HTML deck, a 小红书 图文, or any kind of multi-slide pitch/report/sharing document that should look tasteful and be usable with keyboard navigation. Triggers include keywords like "presentation", "ppt", "slides", "deck", "keynote", "reveal", "slideshow", "幻灯片", "演讲稿", "分享稿", "小红书图文", "talk slides", "pitch deck", "tech sharing", "technical presentation". productivity/html-ppt-studio-agentskill/SKILL.md local

### `linear`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/linear/SKILL.md`
- 功能检索描述：Linear: manage issues, projects, teams via GraphQL + curl.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：linear Linear — Issue & Project Management Linear: manage issues, projects, teams via GraphQL + curl. productivity/linear/SKILL.md local

### `macos-wechat-cli`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-cli/SKILL.md`
- 功能检索描述：Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to install or troubleshoot a WeChat CLI on macOS.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：macos-wechat-cli macOS WeChat CLI Install and verify a macOS WeChat CLI for local WeChat automation using Accessibility API. Use when the user asks to install or troubleshoot a WeChat CLI on macOS. productivity/macos-wechat-cli/SKILL.md local

### `macos-wechat-history-decrypt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/macos-wechat-history-decrypt/SKILL.md`
- 功能检索描述：Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process existing WeChat chat history, list sessions/groups, search old messages, or export historical chats rather than monitor new messages.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：macos-wechat-history-decrypt macOS WeChat History Decryption Decrypt and export historical chat records from macOS WeChat 4.x local databases. Use when the user wants to process existing WeChat chat history, list sessions/groups, search old messages, or export historical chats rather than monitor new messages. productivity/macos-wechat-history-decrypt/SKILL.md local

### `maps`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/maps/SKILL.md`
- 功能检索描述：Geocode, POIs, routes, timezones via OpenStreetMap/OSRM.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：maps Maps Skill Geocode, POIs, routes, timezones via OpenStreetMap/OSRM. productivity/maps/SKILL.md local

### `nano-pdf`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/nano-pdf/SKILL.md`
- 功能检索描述：Edit PDF text/typos/titles via nano-pdf CLI (NL prompts).
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：nano-pdf nano-pdf Edit PDF text/typos/titles via nano-pdf CLI (NL prompts). productivity/nano-pdf/SKILL.md local

### `node-docx-generation`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/node-docx-generation/SKILL.md`
- 功能检索描述：Create polished Microsoft Word .docx files using Node.js and the docx npm package, especially when python-docx is unavailable or Python package installs are blocked by PEP 668. Use for generating Chinese/English Word documents with system fonts, headings, bullets, numbered lists, callout boxes, colors, and reusable scripts.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：node-docx-generation Node DOCX Generation Create polished Microsoft Word .docx files using Node.js and the docx npm package, especially when python-docx is unavailable or Python package installs are blocked by PEP 668. Use for generating Chinese/English Word documents with system fonts, headings, bullets, numbered lists, callout boxes, colors, and reusable scripts. productivity/node-docx-generation/SKILL.md local

### `node-docx-word-output`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/node-docx-word-output/SKILL.md`
- 功能检索描述：Use Node.js docx package to generate polished Word .docx documents with system fonts, colored callouts, headings, bullets, and simple filenames under ~/hermes. Use when the user asks to output text/content as a Word document, especially with richer formatting or system-standard fonts.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：node-docx-word-output Node docx Word Output Use Node.js docx package to generate polished Word .docx documents with system fonts, colored callouts, headings, bullets, and simple filenames under ~/hermes. Use when the user asks to output text/content as a Word document, especially with richer formatting or system-standard fonts. productivity/node-docx-word-output/SKILL.md local

### `notion`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/notion/SKILL.md`
- 功能检索描述：Notion API + ntn CLI: pages, databases, markdown, Workers.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：notion Notion Notion API + ntn CLI: pages, databases, markdown, Workers. productivity/notion/SKILL.md local

### `ocr-and-documents`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/ocr-and-documents/SKILL.md`
- 功能检索描述：Extract text from PDFs/scans (pymupdf, marker-pdf).
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：ocr-and-documents PDF & Document Extraction Extract text from PDFs/scans (pymupdf, marker-pdf). productivity/ocr-and-documents/SKILL.md local

### `official-lark-cli-feishu-workflows`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/official-lark-cli-feishu-workflows/SKILL.md`
- 功能检索描述：Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenClaw setup already uses ~/.lark-cli. Prefer this over third-party feishu-cli packages for stable bot/user identity handling and less confusing auth behavior.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：official-lark-cli-feishu-workflows Use the official @larksuite/cli (lark-cli) for Feishu/Lark docs and Base automation, especially when an existing OpenClaw setup already uses ~/.lark-cli. Prefer this over third-party feishu-cli packages for stable bot/user identity handling and less confusing auth behavior. productivity/official-lark-cli-feishu-workflows/SKILL.md local

### `powerpoint`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/powerpoint/SKILL.md`
- 功能检索描述：Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：powerpoint Powerpoint Skill Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill. productivity/powerpoint/SKILL.md local

### `pptx-template-python-pptx`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/pptx-template-python-pptx/SKILL.md`
- 功能检索描述：Generate a PowerPoint deck from an existing .pptx template using python-pptx when no dedicated PPT CLI is installed or when preserving the user’s template/master/layouts matters. Use for course decks, training PPTs, and iterative PPT generation where content starts as an outline and must be rendered into a provided template.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：pptx-template-python-pptx PPTX Template Generation with python-pptx Generate a PowerPoint deck from an existing .pptx template using python-pptx when no dedicated PPT CLI is installed or when preserving the user’s template/master/layouts matters. Use for course decks, training PPTs, and iterative PPT generation where content starts as an outline and must be rendered into a provided template. productivity/pptx-template-python-pptx/SKILL.md local

### `real-chrome-web-reader`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/real-chrome-web-reader/SKILL.md`
- 功能检索描述：使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：real-chrome-web-reader 使用本机真实 Chrome（保留登录态）+ Playwright 附加 + DOM 压缩读取网页。适合淘宝、生意参谋、千牛等需要登录态且反爬较强的网站。优先用于读取页面、压缩 DOM、点击、输入、滚动、截图。 productivity/real-chrome-web-reader/SKILL.md local

### `reduce-paid-ratio-link-agent-mvp`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-link-agent-mvp/SKILL.md`
- 功能检索描述：Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for close, reduce, keep, or observe actions.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：reduce-paid-ratio-link-agent-mvp 单链接推广花费占比优化 Agent（MVP） Use when analyzing a single high paid-ratio product link from structured context and returning JSON-only decisions for close, reduce, keep, or observe actions. productivity/reduce-paid-ratio-link-agent-mvp/SKILL.md local

### `reduce-paid-ratio-plan-evaluator`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/reduce-paid-ratio-plan-evaluator/SKILL.md`
- 功能检索描述：Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from two source reports, then exporting a decision Excel.
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：reduce-paid-ratio-plan-evaluator 降低店铺付费占比：推广计划关停评估 Use when evaluating which store promotion plans can be shut down, and estimating spend savings versus sales risk from two source reports, then exporting a decision Excel. productivity/reduce-paid-ratio-plan-evaluator/SKILL.md local

### `review-driven-static-html-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/review-driven-static-html-courseware/SKILL.md`
- 功能检索描述：Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML-native presentation instead of service-based editable HTML-PPT or PPT-first thinking.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：review-driven-static-html-courseware Review-driven static HTML courseware Build courseware as static standalone chapter HTML files with MD teacher scripts, using screenshot-based review and HTML-native presentation instead of service-based editable HTML-PPT or PPT-first thinking. productivity/review-driven-static-html-courseware/SKILL.md local

### `sealseek-feature-compare-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/sealseek-feature-compare-doc/SKILL.md`
- 功能检索描述：Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” document where each core module gets its own 3-column comparison table versus traditional tools.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-feature-compare-doc Create or continue a Feishu comparison-style introduction document for SealSeek, especially a multi-chapter “功能对比总览” document where each core module gets its own 3-column comparison table versus traditional tools. productivity/sealseek-feature-compare-doc/SKILL.md local

### `sealseek-static-html-courseware-workflow`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/sealseek-static-html-courseware-workflow/SKILL.md`
- 功能检索描述：Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server dependency, and conference-first readability rules.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-static-html-courseware-workflow Sealseek 静态 HTML 课件工作流 Rebuild Sealseek courseware as standalone static chapter HTML files with screenshot-based review, no local server dependency, and conference-first readability rules. productivity/sealseek-static-html-courseware-workflow/SKILL.md local

### `shopping-basket-visual-reference-discovery`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/shopping-basket-visual-reference-discovery/SKILL.md`
- 功能检索描述：docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual reference sources for an e-commerce product. Stops at “what should we look at for visual references”; does not produce shooting plans, design plans, copy, or image-generation prompts. ---
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：shopping-basket-visual-reference-discovery Shopping Basket Visual Reference Discovery docs --- name: shopping-basket-visual-reference-discovery description: Use shopping-basket logic to discover visual reference sources for an e-commerce product. Stops at “what should we look at for visual references”; does not produce shooting plans, design plans, copy, or image-generation prompts. --- productivity/shopping-basket-visual-reference-discovery/SKILL.md local

### `single-file-static-html-courseware`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/single-file-static-html-courseware/SKILL.md`
- 功能检索描述：Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live editable served HTML. Optimized for polished HTML delivery rather than PPT conversion.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：single-file-static-html-courseware Single-file Static HTML Courseware Build courseware as static, directly-openable HTML chapters and a combined deck, using screenshot review instead of live editable served HTML. Optimized for polished HTML delivery rather than PPT conversion. productivity/single-file-static-html-courseware/SKILL.md local

### `static-html-courseware-feedback-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-feedback-loop/SKILL.md`
- 功能检索描述：Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review standards instead of code-only judgment.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-feedback-loop 静态 HTML 课件反馈闭环 Rebuild courseware as standalone static chapter HTML files, merge them into one deck, and use screenshot-based review standards instead of code-only judgment. productivity/static-html-courseware-feedback-loop/SKILL.md local

### `static-html-courseware-review-loop`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop/SKILL.md`
- 功能检索描述：Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of service-based editing.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-review-loop Static HTML 课件重建与审阅循环 Rebuild and review courseware as static per-chapter HTML files opened via file://, with screenshot-first QA instead of service-based editing. productivity/static-html-courseware-review-loop/SKILL.md local

### `static-html-courseware-review-loop-v2`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-review-loop-v2/SKILL.md`
- 功能检索描述：Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimized for Sealseek-style dark-theme courseware, file:// review, large-font conference display, and screenshot-based QA instead of in-page editing.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：static-html-courseware-review-loop-v2 Static HTML Courseware Review Loop v2 Rebuild a course deck as static standalone chapter HTML files, then merge into one combined HTML-PPT for review. Optimized for Sealseek-style dark-theme courseware, file:// review, large-font conference display, and screenshot-based QA instead of in-page editing. productivity/static-html-courseware-review-loop-v2/SKILL.md local

### `static-html-courseware-shared-assets-and-merge`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-courseware-shared-assets-and-merge/SKILL.md`
- 功能检索描述：Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapters into one final HTML without CSS collisions.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：static-html-courseware-shared-assets-and-merge When to use Build courseware as standalone chapter HTML files with one shared assets folder, review via screenshots, and merge chapters into one final HTML without CSS collisions. productivity/static-html-courseware-shared-assets-and-merge/SKILL.md local

### `static-html-deck-to-editable-ppt`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/static-html-deck-to-editable-ppt/SKILL.md`
- 功能检索描述：Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into truly editable PowerPoint, instead of relying on served HTML decks or screenshot-only PPT export.
- 输入 / 触发方式：课程大纲、逐页内容、PPT/XMind/课件制作或修改需求
- 检索关键词：static-html-deck-to-editable-ppt Static HTML Deck → Editable PPT workflow Build presentation decks as standalone static HTML files that are intentionally structured for later conversion into truly editable PowerPoint, instead of relying on served HTML decks or screenshot-only PPT export. productivity/static-html-deck-to-editable-ppt/SKILL.md local

### `taobao-native-search-to-excel`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/taobao-native-search-to-excel/SKILL.md`
- 功能检索描述：使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-native-search-to-excel 使用淘宝桌面版（taobao-native / cli-rpc）搜索指定关键词，支持综合/销量排序与多页翻页，导出 Excel 到 ~/hermes/skills/taobao-native-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 productivity/taobao-native-search-to-excel/SKILL.md local

### `taobao-search-to-excel`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：电商 / 商品 / 品牌运营
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/taobao-search-to-excel/SKILL.md`
- 功能检索描述：使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。
- 输入 / 触发方式：Excel/CSV/表格文件、字段信息或数据分析需求；已打开网页、浏览器页面、插件功能或页面 API 线索；agent/skill/plugin 名称、目标能力、运行环境或迁移需求；电商平台页面、商品/店铺/关键词数据、运营规则或视觉策划需求
- 检索关键词：taobao-search-to-excel 使用真实 Chrome 登录态抓取淘宝搜索结果，按“综合/销量”排序抓取指定页数，并导出为 Excel 到 ~/hermes/skills/taobao-search-to-excel/<搜索词>_<排序方式>_<页数>_<时间戳>/。 productivity/taobao-search-to-excel/SKILL.md local

### `teams-meeting-pipeline`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/teams-meeting-pipeline/SKILL.md`
- 功能检索描述：Operate the Teams meeting summary pipeline via Hermes CLI — summarize meetings, inspect pipeline status, replay jobs, manage Microsoft Graph subscriptions.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：teams-meeting-pipeline Teams Meeting Pipeline Operate the Teams meeting summary pipeline via Hermes CLI — summarize meetings, inspect pipeline status, replay jobs, manage Microsoft Graph subscriptions. productivity/teams-meeting-pipeline/SKILL.md local

### `xicheng-bi-feishu-feature-doc`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/productivity/xicheng-bi-feishu-feature-doc/SKILL.md`
- 功能检索描述：Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise sales-conversion-oriented but user-appropriate language, callouts, images, and whiteboard diagrams.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：xicheng-bi-feishu-feature-doc Create or continue the user-facing Feishu document《玺承BI特色功能介绍》from feature screenshots plus brief notes, using concise sales-conversion-oriented but user-appropriate language, callouts, images, and whiteboard diagrams. productivity/xicheng-bi-feishu-feature-doc/SKILL.md local

### `godmode`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/red-teaming/godmode/SKILL.md`
- 功能检索描述：Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：godmode G0DM0D3 Jailbreaking Skill Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN. red-teaming/godmode/SKILL.md local

### `arxiv`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/arxiv/SKILL.md`
- 功能检索描述：Search arXiv papers by keyword, author, category, or ID.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：arxiv arXiv Research Search arXiv papers by keyword, author, category, or ID. research/arxiv/SKILL.md local

### `blogwatcher`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/blogwatcher/SKILL.md`
- 功能检索描述：Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.
- 输入 / 触发方式：MCP server、工具配置、连接或封装需求
- 检索关键词：blogwatcher Blogwatcher Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool. research/blogwatcher/SKILL.md local

### `llm-wiki`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/llm-wiki/SKILL.md`
- 功能检索描述：Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki Karpathy's LLM Wiki Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency. research/llm-wiki/SKILL.md local

### `llm-wiki-audit-and-optimization`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：知识库 / 知识管理 / LLM Wiki
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/llm-wiki-audit-and-optimization/SKILL.md`
- 功能检索描述：Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base.
- 输入 / 触发方式：wiki 路径、资料来源、剪藏文件、知识库查询或维护需求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求
- 检索关键词：llm-wiki-audit-and-optimization LLM Wiki Audit and Optimization Audit and optimize an LLM Wiki's compile-routing-reasoning quality. Use after a wiki/domain/learning path is built, or when a question-answer result needs diagnosis against the wiki, to find whether issues come from compilation, routing, or reasoning and to patch the knowledge base. research/llm-wiki-audit-and-optimization/SKILL.md local

### `polymarket`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/polymarket/SKILL.md`
- 功能检索描述：Query Polymarket: markets, prices, orderbooks, history.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：polymarket Polymarket — Prediction Market Data Query Polymarket: markets, prices, orderbooks, history. research/polymarket/SKILL.md local

### `research-paper-writing`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/research/research-paper-writing/SKILL.md`
- 功能检索描述：Write ML papers for NeurIPS/ICML/ICLR: design→submit.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：research-paper-writing Research Paper Writing Pipeline Write ML papers for NeurIPS/ICML/ICLR: design→submit. research/research-paper-writing/SKILL.md local

### `openhue`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/smart-home/openhue/SKILL.md`
- 功能检索描述：Control Philips Hue lights, scenes, rooms via OpenHue CLI.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：openhue OpenHue CLI Control Philips Hue lights, scenes, rooms via OpenHue CLI. smart-home/openhue/SKILL.md local

### `xitter`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/social-media/xitter/SKILL.md`
- 功能检索描述：Interact with X/Twitter via the x-cli terminal client using official X API credentials. Use for posting, reading timelines, searching tweets, liking, retweeting, bookmarks, mentions, and user lookups.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：xitter Xitter — X/Twitter via x-cli Interact with X/Twitter via the x-cli terminal client using official X API credentials. Use for posting, reading timelines, searching tweets, liking, retweeting, bookmarks, mentions, and user lookups. social-media/xitter/SKILL.md local

### `xurl`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/social-media/xurl/SKILL.md`
- 功能检索描述：X/Twitter via xurl CLI: post, search, DM, media, v2 API.
- 输入 / 触发方式：API 文档 URL、接口规格、鉴权/参数/示例需求
- 检索关键词：xurl xurl — X (Twitter) API via the Official CLI X/Twitter via xurl CLI: post, search, DM, media, v2 API. social-media/xurl/SKILL.md local

### `cross-agent-skill-packaging`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/cross-agent-skill-packaging/SKILL.md`
- 功能检索描述：Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when publishing to git, syncing into Sealseek, or building a full test bundle with runtime credentials.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：cross-agent-skill-packaging Cross-Agent Skill Packaging Package a skill developed in Hermes for reuse across Hermes, Sealseek/OpenClaw, and trusted tester machines. Use when publishing to git, syncing into Sealseek, or building a full test bundle with runtime credentials. software-development/cross-agent-skill-packaging/SKILL.md local

### `debugging-hermes-tui-commands`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/debugging-hermes-tui-commands/SKILL.md`
- 功能检索描述：Debug Hermes TUI slash commands: Python, gateway, Ink UI.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：debugging-hermes-tui-commands Debugging Hermes TUI Slash Commands Debug Hermes TUI slash commands: Python, gateway, Ink UI. software-development/debugging-hermes-tui-commands/SKILL.md local

### `hermes-agent-skill-authoring`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/hermes-agent-skill-authoring/SKILL.md`
- 功能检索描述：Author in-repo SKILL.md: frontmatter, validator, structure.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-agent-skill-authoring Authoring Hermes-Agent Skills (in-repo) Author in-repo SKILL.md: frontmatter, validator, structure. software-development/hermes-agent-skill-authoring/SKILL.md local

### `hermes-s6-container-supervision`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/hermes-s6-container-supervision/SKILL.md`
- 功能检索描述：Modify, debug, or extend the s6-overlay supervision tree inside the Hermes Agent Docker image — adding new services, debugging profile gateways, understanding the Architecture B main-program pattern.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：hermes-s6-container-supervision Hermes s6-overlay Container Supervision Modify, debug, or extend the s6-overlay supervision tree inside the Hermes Agent Docker image — adding new services, debugging profile gateways, understanding the Architecture B main-program pattern. software-development/hermes-s6-container-supervision/SKILL.md local

### `node-inspect-debugger`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/node-inspect-debugger/SKILL.md`
- 功能检索描述：Debug Node.js via --inspect + Chrome DevTools Protocol CLI.
- 输入 / 触发方式：已打开网页、浏览器页面、插件功能或页面 API 线索；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求
- 检索关键词：node-inspect-debugger Node.js Inspect Debugger Debug Node.js via --inspect + Chrome DevTools Protocol CLI. software-development/node-inspect-debugger/SKILL.md local

### `plan`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/plan/SKILL.md`
- 功能检索描述：Plan mode: write markdown plan to .hermes/plans/, no exec.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：plan Plan Mode Plan mode: write markdown plan to .hermes/plans/, no exec. software-development/plan/SKILL.md local

### `python-debugpy`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/python-debugpy/SKILL.md`
- 功能检索描述：Debug Python: pdb REPL + debugpy remote (DAP).
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：python-debugpy Python Debugger (pdb + debugpy) Debug Python: pdb REPL + debugpy remote (DAP). software-development/python-debugpy/SKILL.md local

### `requesting-code-review`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/requesting-code-review/SKILL.md`
- 功能检索描述：Pre-commit review: security scan, quality gates, auto-fix.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：requesting-code-review Pre-Commit Code Verification Pre-commit review: security scan, quality gates, auto-fix. software-development/requesting-code-review/SKILL.md local

### `sealseek-gpt-image-skill-migration`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/sealseek-gpt-image-skill-migration/SKILL.md`
- 功能检索描述：Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use when migrating image-generation capability from another skill (e.g. gemini-image), configuring Sealseek skill manifests, or debugging EvoLink async GPT Image 2 workflows.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-gpt-image-skill-migration Sealseek GPT 生图 Skill 迁移与维护 Install, consolidate, and maintain a GPT-only image generation skill in Sealseek/OpenClaw using EvoLink GPT Image 2. Use when migrating image-generation capability from another skill (e.g. gemini-image), configuring Sealseek skill manifests, or debugging EvoLink async GPT Image 2 workflows. software-development/sealseek-gpt-image-skill-migration/SKILL.md local

### `sealseek-skill-sync-and-toolcall-fix`

- Agent / 环境：Hermes
- 归属分类：个人/项目自定义
- 归属依据：Hermes skill 命中 Peter 项目/业务/知识库/电商/课程/视觉等定制关键词。
- 来源类型：local
- 能力分类：视觉 / 内容 / 课件生产
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/sealseek-skill-sync-and-toolcall-fix/SKILL.md`
- 功能检索描述：Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-promotion bug in AgentScope.
- 输入 / 触发方式：图片路径、视觉目标、品类/风格/生成或编辑要求；代码仓库、文件路径、PR/Issue、调试或开发任务；MCP server、工具配置、连接或封装需求；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：sealseek-skill-sync-and-toolcall-fix Sealseek skill sync and tool-call fix Sync Hermes-developed skills to Gitee and Sealseek, verify parity, and patch Sealseek/OpenClaw's multi-tool-call image-promotion bug in AgentScope. software-development/sealseek-skill-sync-and-toolcall-fix/SKILL.md local

### `spike`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/spike/SKILL.md`
- 功能检索描述：Throwaway experiments to validate an idea before build.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：spike Spike Throwaway experiments to validate an idea before build. software-development/spike/SKILL.md local

### `stateful-skill-runner-pattern`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/stateful-skill-runner-pattern/SKILL.md`
- 功能检索描述：Build a lightweight file-backed state-machine runner for multi-turn skills so user branch choices resume the intended workflow instead of drifting into free-form replanning.
- 输入 / 触发方式：agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：stateful-skill-runner-pattern Stateful Skill Runner Pattern Build a lightweight file-backed state-machine runner for multi-turn skills so user branch choices resume the intended workflow instead of drifting into free-form replanning. software-development/stateful-skill-runner-pattern/SKILL.md local

### `subagent-driven-development`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/subagent-driven-development/SKILL.md`
- 功能检索描述：Execute plans via delegate_task subagents (2-stage review).
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务；agent/skill/plugin 名称、目标能力、运行环境或迁移需求
- 检索关键词：subagent-driven-development Subagent-Driven Development Execute plans via delegate_task subagents (2-stage review). software-development/subagent-driven-development/SKILL.md local

### `systematic-debugging`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/systematic-debugging/SKILL.md`
- 功能检索描述：4-phase root cause debugging: understand bugs before fixing.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：systematic-debugging Systematic Debugging 4-phase root cause debugging: understand bugs before fixing. software-development/systematic-debugging/SKILL.md local

### `test-driven-development`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/test-driven-development/SKILL.md`
- 功能检索描述：TDD: enforce RED-GREEN-REFACTOR, tests before code.
- 输入 / 触发方式：代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：test-driven-development Test-Driven Development (TDD) TDD: enforce RED-GREEN-REFACTOR, tests before code. software-development/test-driven-development/SKILL.md local

### `writing-plans`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/software-development/writing-plans/SKILL.md`
- 功能检索描述：Write implementation plans: bite-sized tasks, paths, code.
- 输入 / 触发方式：飞书/钉钉资源 URL/ID、文档/表格/日程/消息等操作需求；代码仓库、文件路径、PR/Issue、调试或开发任务
- 检索关键词：writing-plans Writing Implementation Plans Write implementation plans: bite-sized tasks, paths, code. software-development/writing-plans/SKILL.md local

### `yuanbao`

- Agent / 环境：Hermes
- 归属分类：通用安装/不确定
- 归属依据：Hermes 通用能力库 skill，未命中个人项目关键词；保留在全量库，不进入个人库。
- 来源类型：local
- 能力分类：Agent 工程 / Skill / Plugin / MCP
- Skill 文件位置：`/Users/pechen/.hermes/skills/yuanbao/SKILL.md`
- 功能检索描述：Yuanbao (元宝) groups: @mention users, query info/members.
- 输入 / 触发方式：用户任务描述；执行前打开 SKILL.md 查看完整输入契约
- 检索关键词：yuanbao Yuanbao Group Interaction Yuanbao (元宝) groups: @mention users, query info/members. yuanbao/SKILL.md local

