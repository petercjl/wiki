# Formal Page Plan

## Source Understanding

材料包含两层知识：

1. 真实原型回顾：Mac 通过 Tailscale 虚拟局域网和 SSH/SCP 调用公司 Windows GPU，运行 Real-ESRGAN 超分。
2. 可复用方法论：如何把一台公司 GPU 从个人远程命令升级为多人可治理的分时共享服务。

## Existing Memory Search

- 未找到 Tailscale、共享 GPU Worker、远程 GPU 任务队列或 Real-ESRGAN 部署的正式页面。
- `domains/AI Agent工程/05-工具链/` 已负责 CLI、MCP、API 与自动化工具组合，是最接近且足够具体的现有分类。
- `domains/视觉制作/` 虽包含超分使用场景，但不能承载公司级网络、权限和调度方法。

## Recommended Placement

- `domains/AI Agent工程/05-工具链/03-公司共享GPU工作节点与分时调度方法.md`
  - 作为主方法页，覆盖接入层、身份层、任务层、调度层、执行层、存储层、观测层、安全治理与演进路线。
- `domains/AI Agent工程/05-工具链/04-Real-ESRGAN远程超分案例.md`
  - 作为案例页，回顾当前实现、真实链路、兼容补丁、已解决问题和原型缺口。
- `queries/公司GPU共享与远程任务调度.md`
  - 作为未来 Agent 收到“共享公司 GPU、远程 GPU、多人排队、GPU Worker”等请求时的入口。

Disposition: `create-new`，并更新 AI Agent 工程索引、总索引和日志。

## Alternative

可新建 `domains/AI Agent工程/10-算力基础设施/`。但目前只有一个案例，新建顶层子主题过早；当未来出现多 GPU、推理服务、训练集群和成本核算页面时再拆分更合适。

## Confirmation

- Status: confirmed
- Confirmation evidence: 用户于 2026-07-24 回复“可以的，先按照这个路径入库吧”，并要求明确当前只是初步测试，尚未上升为公司级共享平台。
- No formal write before confirmation: yes
