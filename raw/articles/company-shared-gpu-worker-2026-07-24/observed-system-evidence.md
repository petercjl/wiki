# 公司共享 GPU Worker：现有超分原型观察记录

- 观察日期：2026-07-24
- 观察方式：读取本机命令脚本、检查 macOS 路由与 Tailscale 状态、通过现有 SSH 通道只读检查 Windows 服务/GPU/模型。
- 敏感信息处理：未记录登录邮箱、公网地址、节点公钥、SSH 私钥内容和真实 Tailnet 地址；主机名和地址均用角色名替代。

## 1. 时间线证据

- 2026-07-06 11:51：本机 `upscale-img` 入口脚本创建。
- 2026-07-06 12:33：独立 SSH 客户端密钥创建。
- 2026-07-06 12:36：Windows 端 `realesrgan-ncnn-vulkan.exe` 安装到 `C:\AI\tools\realesrgan-ncnn-vulkan\`。
- 2026-07-06 12:41：本机 `remote-upscale-ai` 脚本创建。
- 2026-07-08 05:52—06:01 UTC：Windows GPU Worker 与 Mac 客户端加入同一个 Tailscale Tailnet。
- 2026-07-08 14:06：`remote-upscale-ai` 最后修改，默认远端地址已换成 Windows 的 Tailscale 固定地址。

这说明原型先完成局域网/SSH 远程调用，随后用 Tailscale 把同一调用方式扩展到异地网络。

## 2. 当前网络实现

- Mac 与 Windows 都运行 Tailscale，并加入同一个 Tailnet。
- Windows 获得稳定的 Tailscale IPv4 地址；`remote-upscale-ai` 直接以该地址作为 SSH 目标。
- macOS 对该地址的路由落在 `utun0` 虚拟网卡，不经过普通局域网默认路由。
- 2026-07-24 实测 `tailscale ping` 为约 5 ms，并显示当前建立了点对点直连路径。
- 当点对点 NAT 穿透失败时，Tailscale 可退回 DERP 中继；中继只转发端到端加密数据。
- Windows 的 `Tailscale` 与 `sshd` 服务均为 `Running / Automatic`。
- Windows 防火墙启用了 OpenSSH Server 入站规则。
- 当前原型使用标准 OpenSSH + SSH 密钥认证；不是 Tailscale SSH。

## 3. 当前执行链

```text
用户
  -> upscale-img
  -> remote-upscale-ai
  -> SSH（在 Windows 创建独立 job 目录）
  -> SCP 上传输入图片
  -> PowerShell 调用 realesrgan-ncnn-vulkan.exe
  -> SCP 下载输出图片
  -> 清理 Windows 临时文件
  -> 返回本机输出路径
```

每次请求用 `时间戳 + 本地进程号` 生成 `job_id`，输入和输出文件名彼此隔离。这解决了文件覆盖问题，但没有解决多个 GPU 进程同时争抢显存和算力的问题。

## 4. Windows GPU Worker

- 操作系统：Windows Server 2019 Standard。
- GPU：NVIDIA GeForce RTX 3060 Ti，8 GB 显存。
- 执行器：`Real-ESRGAN-ncnn-vulkan`。
- 默认照片模型：`realesrgan-x4plus`。
- 动漫模型：`realesrgan-x4plus-anime`。
- 轻量模型：`realesr-animevideov3`。
- 默认 tile：512。
- 默认入口模式：`true-scale`，优先使用 Windows GPU。
- Windows 不可达或远端命令失败时，`upscale-img` 会警告并退回本机 ImageMagick/Lanczos 缩放和轻度锐化；该结果不是 AI 超分。

照片模型请求 2× 或 3× 时，当前脚本先在 Windows 运行原生 4×，再在 Mac 用 Lanczos 缩到目标倍率。这是对该 NCNN 构建直接输出 2×/3× 时可能出现损坏 tile 的兼容补丁。

## 5. 当前原型已经解决的问题

- 不要求两台机器处于同一物理局域网。
- 不需要为 SSH 做公网端口映射。
- 用户端只记住一个稳定命令，不需要了解 Windows 路径和模型命令。
- 输入、输出和临时文件有基础隔离。
- Worker 端服务可随 Windows 自动启动。
- 网络失败时有显式告警和可用性降级。

## 6. 当前原型尚未解决的问题

- 所有人若复制同一 SSH 私钥，会形成共享管理员身份，无法准确追责。
- 没有组织级 Tailscale 用户组、设备标签和最小端口授权证据。
- 没有中央任务队列；同时提交会启动多个 GPU 进程并争抢显存。
- 没有并发上限、优先级、公平调度、超时、取消、重试和配额。
- 没有任务状态 API、审计日志、指标监控和容量规划。
- 没有输入文件保留期、自动清理、敏感图片分类和数据处理边界。
- fallback 会产出非 AI 结果；若调用方只检查“文件存在”，可能把降级结果误判为成功。
- 客户端脚本写死了当前 Worker 地址和环境路径，不适合直接分发给全公司。

因此，现有实现是一个可靠的“单用户远程 GPU 命令原型”，还不是可直接面向全公司的“GPU 分时共享平台”。

## 7. 官方技术依据

- Tailscale 使用 WireGuard 建立加密点对点连接，并提供 NAT 穿透、访问控制和必要时的 DERP 中继：
  - https://tailscale.com/docs/concepts/what-is-tailscale
  - https://tailscale.com/docs/concepts/wireguard
  - https://tailscale.com/docs/reference/derp-servers
- 新部署应优先使用 Tailscale Grants，以用户组、设备标签、目标端口和设备姿态实施最小权限：
  - https://tailscale.com/docs/features/access-control/grants
- Real-ESRGAN 官方仓库说明 NCNN Vulkan 是面向 Windows/Linux/macOS GPU 的便携推理实现：
  - https://github.com/xinntao/Real-ESRGAN

