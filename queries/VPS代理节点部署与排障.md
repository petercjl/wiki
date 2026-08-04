---
title: VPS 代理节点部署与排障
type: query
created: 2026-08-03
updated: 2026-08-03
domain: AI Agent工程
tags: [query, network, remote-node, shadowsocks, mihomo, troubleshooting]
sources:
  - raw/articles/gigsgigscloud-shadowsocks-node-2026-08-03/source-evidence.md
  - _meta/extraction-notes/gigsgigscloud-shadowsocks-node-2026-08-03/coverage-matrix.md
status: active
---

# VPS 代理节点部署与排障

## 触发词

当用户提出以下问题时使用本入口：VPS 代理、自建节点、Shadowsocks、Mihomo/Clash 节点、线路测速、下载慢、丢包、SSH 非标准端口、安全组、TCP/UDP 443、`Invalid config path`、`ss://` 分享、Clash V-Ninja 不兼容。

## 阅读顺序

1. [[domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维|GigsGigsCloud 东京 Shadowsocks 节点部署与运维]]：主流程、配置契约、测试和故障路由。
2. [[domains/AI Agent工程/05-工具链/05-网络与远程节点/index|网络与远程节点]]：同类远程网络知识入口。

需要把代理节点扩展成公司级远程服务时，再读：

- [[domains/AI Agent工程/05-工具链/03-公司共享GPU工作节点与分时调度方法|公司共享 GPU 工作节点与分时调度方法]]：网络、身份、队列、资源和审计的分层。

## 标准诊断步骤

1. 明确目标地区、使用者位置、目标网站、协议、预算、带宽和流量限制。
2. 先测本机到服务器的延迟、抖动、丢包，再测服务器出口吞吐。
3. 核对 SSH 外部端口、系统版本、更新状态和密钥授权。
4. 检查服务配置、systemd 状态、TCP/UDP 监听和日志。
5. 检查云安全组是否同时放行 TCP 与 UDP 代理端口。
6. 校验 Mihomo 配置，热加载并确认代理组真正切换。
7. 显式经过本机代理端口验证出口 IP、国家、下载吞吐和负载丢包。
8. 用目标网页/API 做业务验证，并区分 200、401、403 所代表的层级。
9. 评估晚高峰、多用户、月流量和凭据轮换。

## 输出要求

诊断结论必须区分：

- 已验证事实；
- 线路或站点策略推断；
- 尚需晚高峰/账户/真实客户端复测的事项；
- 时间敏感的套餐、政策和软件版本；
- 可能暴露凭据或扩大持续访问权限的操作。

## 执行边界

- 不在聊天或 Wiki 中记录真实密码、SSH 私钥、订阅 token 或完整 `ss://` 链接。
- 购买、退款、删除实例、重装系统、修改安全组、轮换凭据和对外分享配置属于有副作用操作，必须获得明确授权，并在最终提交前遵循工具确认要求。
- 不把低 Ping 当作线路质量结论；不把 API 401/403 当作账户可用性结论。
- 不把标准 `type: ss` 通过改字段名伪装成客户端不支持的私有协议。
