---
title: Real-ESRGAN 远程超分案例
type: project
created: 2026-07-24
updated: 2026-07-24
domain: AI Agent工程
tags: [gpu, tailscale, ssh, real-esrgan, image-upscale, case]
sources:
  - raw/articles/company-shared-gpu-worker-2026-07-24/observed-system-evidence.md
  - _meta/extraction-notes/company-shared-gpu-worker-2026-07-24/coverage-matrix.md
status: active
---

# Real-ESRGAN 远程超分案例

## 案例结论

这个项目已经验证：

- Mac 可以在本地或出差网络中，通过 Tailscale 到达公司的 Windows GPU 机器；
- 用户只需执行 `upscale-img`，脚本会完成上传、远端超分、下载和清理；
- Windows 的 RTX 3060 Ti 可以使用 Real-ESRGAN NCNN Vulkan 执行图片超分；
- Tailscale 与 OpenSSH 服务自动启动后，远端链路能跨物理局域网工作。

但它目前只是**单用户或少量受信任用户的初步测试原型**，不是公司级共享平台。它尚未实现多人身份、中央队列、并发控制、配额、公平调度、状态服务、审计和数据治理。

## 演进回顾

先建立统一入口 `upscale-img`，把普通缩放与 AI 超分隐藏在同一个命令后面。Windows GPU Worker 通过 OpenSSH 接受远端命令。

2026-07-08，Mac 和 Windows 加入同一个 Tailscale Tailnet。远端脚本的目标从依赖物理局域网的地址，改为 Windows 稳定的 Tailscale 地址。变化发生在网络层，CLI、SSH、文件传输和 GPU 命令保持不变：

```text
同一办公室：Mac -> Tailscale/局域网直连路径 -> Windows
异地出差：Mac -> Internet -> Tailscale NAT 穿透或 DERP -> Windows
```

## 已验证环境

| 项目 | 实际配置 |
| --- | --- |
| 客户端 | macOS |
| GPU Worker | Windows Server 2019 Standard |
| GPU | NVIDIA GeForce RTX 3060 Ti，8 GB |
| 虚拟局域网 | Tailscale |
| 远程协议 | 标准 OpenSSH + SSH 密钥 |
| 文件传输 | SCP |
| 超分执行器 | Real-ESRGAN NCNN Vulkan |
| 程序目录 | `C:\AI\tools\realesrgan-ncnn-vulkan\` |
| 默认模型 | `realesrgan-x4plus` |
| 动漫模型 | `realesrgan-x4plus-anime` |
| 轻量模型 | `realesr-animevideov3` |
| tile | 512 |

Windows 的 `Tailscale` 与 `sshd` 服务均为自动启动。2026-07-24 实测两端在线，Tailscale 建立了低延迟点对点路径。

## 真实执行链

```text
1. 用户运行 upscale-img INPUT [OUTPUT] --scale N --model MODEL
2. upscale-img 默认选择 true-scale
3. remote-upscale-ai 建立 SSH 连接
4. Windows 创建本次 job 的 in/out 目录
5. SCP 上传输入图片
6. PowerShell 调用 realesrgan-ncnn-vulkan.exe
7. SCP 把结果下载到 Mac
8. 删除 Windows 输入、输出和临时文件
9. 返回本机结果路径
```

每次调用以 `时间戳 + 客户端进程号` 生成 job_id，避免不同请求使用同一个输入输出文件名。

## 2×/3× 照片模型兼容补丁

当前 Windows NCNN 构建在照片模型直接请求 2×/3× 时，可能产生损坏的 tile 输出。脚本采用：

1. Windows 使用 `realesrgan-x4plus` 原生生成 4× PNG；
2. 下载 4× 临时文件；
3. Mac 使用 ImageMagick 或 Pillow + Lanczos 缩到 2×/3×；
4. 删除临时文件。

这是当前执行器版本的案例级补丁，不能直接推广为所有超分模型的通用步骤。更换模型或执行器后应重新做 2×、3×、4× 回归测试。

## 降级行为

若 Windows Worker 不可达或远端任务失败，`upscale-img` 会打印警告，并退回本机 ImageMagick 的 Lanczos resize 与轻度 unsharp，不进行 AI 细节重建。

这保证了“仍能得到一张放大图”，但调用者可能把普通插值结果误当成 AI 超分。下一版应返回结构化状态 `ai_succeeded`、`degraded_to_resize` 或 `failed`，并为必须真实 AI 超分的任务提供 strict 模式。

## 当前原型的能力边界

### 已实现

- [x] 异地到达 Windows GPU
- [x] WireGuard 加密的虚拟网络
- [x] 无需公网 SSH 端口映射
- [x] SSH 密钥认证
- [x] CLI 封装上传、执行、下载和清理
- [x] 独立 job 文件名
- [x] 照片、动漫和轻量模型映射
- [x] 失败告警与普通缩放 fallback

### 未实现

- [ ] 公司员工独立身份与权限
- [ ] Tailscale 组织级用户组/Worker 标签策略的落地证据
- [ ] 中央任务队列
- [ ] GPU 并发上限和显存调度
- [ ] 排队顺序、优先级、公平性和配额
- [ ] 任务状态查询、取消、超时和重试
- [ ] 审计日志、指标、告警和容量规划
- [ ] 输入输出保留期和敏感数据规则
- [ ] 多 Worker 与故障转移

不能把“多人各自复制脚本和同一 SSH 私钥”作为公司推广方案。那只会把远程执行扩散成不可治理的共享管理员访问。

## 从原型进入内部试运行的最低改造

1. 保留 `upscale-img` 作为用户入口，但改为调用任务 API；
2. 建立一个 GPU Gateway，绑定员工身份；
3. 增加持久化队列，单 GPU 初始并发为 1；
4. Windows Worker 以服务身份领取任务，不接受普通用户直连；
5. 返回 job_id，支持 `submit/status/cancel/download`；
6. 记录提交人、模型、参数、排队时间、耗时、结果和降级状态；
7. 制定输入输出保留期与自动清理；
8. 以真实商品图进行吞吐、显存和失败恢复压测。

完成这些后，项目才从“初步测试”进入“公司内部可控试运行”；仍需安全评审、配额和运维制度后，才能称为正式公司级共享平台。

## 可迁移经验

- 先把一个 GPU 能力做成稳定 CLI，再考虑共享。
- 用 overlay network 替换物理局域网依赖，不必同时重写上层协议。
- 用 job_id 隔离文件，但用队列隔离算力竞争。
- 网络连通、任务授权、资源调度和审计是四个不同问题。
- 原型阶段允许简单，推广阶段必须消除共享管理员身份。
- fallback 必须机器可读，否则容易出现假成功。

## 相关记忆

- [[domains/AI Agent工程/05-工具链/03-公司共享GPU工作节点与分时调度方法|公司共享 GPU 工作节点与分时调度方法]]
- [[queries/公司GPU共享与远程任务调度|公司 GPU 共享与远程任务调度]]

