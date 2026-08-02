---
title: 公司共享 GPU Worker 超分原型 source profile
type: source-summary
created: 2026-07-24
updated: 2026-07-24
domain: meta
tags: [llm-wiki, gpu, toolchain]
sources:
  - raw/articles/company-shared-gpu-worker-2026-07-24/observed-system-evidence.md
status: active
---

# Source Profile

- Source title: 公司共享 GPU Worker：现有超分原型观察记录
- Slug: `company-shared-gpu-worker-2026-07-24`
- Source type: 本机系统观察、脚本审阅与官方文档核验
- Adapter: `markdown-doc`
- Capture date: 2026-07-24
- Language: 中文
- Original local sources:
  - `/Users/pechen/.local/bin/upscale-img`
  - `/Users/pechen/.local/bin/remote-upscale-ai`
  - macOS `tailscale status / ping / route`
  - Windows PowerShell、服务状态、GPU 与模型目录的只读检查
- Sensitivity: 已从归档观察记录中移除邮箱、公网 IP、节点公钥、SSH 私钥内容、真实 Tailnet 地址。
- Current-doc verification: Tailscale 与 Real-ESRGAN 的架构和权限建议已在 2026-07-24 对官方资料核验。
- Domain candidate: `domains/AI Agent工程/05-工具链/`
- Proposed disposition: 新建“共享 GPU 工作节点与分时调度”方法页，并将超分原型作为案例页。
- Placement confirmation: confirmed by user on 2026-07-24
- Expected formal artifacts:
  - 公司共享 GPU 工作节点与分时调度方法论
  - Real-ESRGAN 远程超分案例
  - Agent 查询入口
