---
title: 公司 GPU 共享与远程任务调度
type: query
created: 2026-07-24
updated: 2026-07-24
domain: AI Agent工程
tags: [gpu, toolchain, scheduling, tailscale, query]
sources:
  - raw/articles/company-shared-gpu-worker-2026-07-24/observed-system-evidence.md
  - _meta/extraction-notes/company-shared-gpu-worker-2026-07-24/coverage-matrix.md
status: active
---

# 公司 GPU 共享与远程任务调度

## 何时使用

- “怎么让公司的一台 GPU 给多人使用？”
- “出差时如何访问公司的 GPU 电脑？”
- “用 Tailscale、SSH 还是 API？”
- “多人提交 GPU 任务怎么排队？”
- “把远程 GPU 脚本升级成公司服务。”
- “复盘 `upscale-img` / Real-ESRGAN 远程超分方案。”

## 必读顺序

1. [[domains/AI Agent工程/05-工具链/03-公司共享GPU工作节点与分时调度方法|公司共享 GPU 工作节点与分时调度方法]]
2. [[domains/AI Agent工程/05-工具链/04-Real-ESRGAN远程超分案例|Real-ESRGAN 远程超分案例]]
3. 若要产品化为 Agent 能力：[[domains/AI Agent工程/10-插件Skill与CLI/02-从CLI与Skill演进为Codex插件|从 CLI 与 Skill 演进为 Codex 插件]]

## 先问成熟度

必须先判断项目处于本机验证、远程 GPU 原型、单 Worker 内部试运行、公司级共享平台，还是多 Worker GPU 资源池。

远程运行成功不等于公司级平台。当前 Real-ESRGAN 超分案例只处于“远程 GPU 原型”阶段。

## 标准诊断

1. 盘点 GPU、显存、操作系统、驱动、模型和执行器。
2. 定义输入、输出、参数、错误码和资源需求。
3. 判断用户与 Worker 是否跨物理网络。
4. 设计 Tailnet/overlay 的用户组、设备标签和最小端口权限。
5. 分离普通用户、网关服务和管理员身份。
6. 检查是否存在共享管理员密钥。
7. 检查是否有中央队列、并发上限、租约和心跳。
8. 检查任务状态、取消、超时、重试和幂等。
9. 检查输入输出隔离、保留期和敏感数据边界。
10. 建立排队时间、成功率、OOM、降级率和 GPU 占用指标。
11. 用真实任务做容量压测，再决定是否提高并发或增加 Worker。

## 输出要求

- 当前成熟度与证据；
- 已实现/未实现能力表；
- 网络、身份、队列、调度、Worker、存储和观测架构；
- 任务和结果契约；
- 权限与数据治理边界；
- 分阶段实施路线；
- 验收清单；
- 明确标注哪些是现状、哪些是建议，禁止把目标架构写成已实现。

