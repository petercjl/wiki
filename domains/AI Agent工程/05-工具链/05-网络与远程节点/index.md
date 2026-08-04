---
title: 网络与远程节点
type: concept
created: 2026-08-03
updated: 2026-08-03
domain: AI Agent工程
tags: [toolchain, network, remote-node, index]
sources:
  - raw/articles/gigsgigscloud-shadowsocks-node-2026-08-03/source-evidence.md
  - _meta/extraction-notes/gigsgigscloud-shadowsocks-node-2026-08-03/coverage-matrix.md
status: active
---

# 网络与远程节点

本目录沉淀远程服务器、代理节点、线路验证、网络安全和客户端接入的可复用方法。核心原则是先验证线路，再部署服务；把服务端、云防火墙、本机代理和真实业务可达性分层验收。

## 页面

- [[domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维|GigsGigsCloud 东京 Shadowsocks 节点部署与运维]]：从购买门禁、SSH 初始化到服务端配置、安全组、Mihomo 接入、测速和客户端兼容性。

## Agent 入口

- [[queries/VPS代理节点部署与排障|VPS 代理节点部署与排障]]：收到选线路、搭节点、测速、排障或分享配置任务时的读取顺序和执行边界。

## 相关记忆

- [[domains/AI Agent工程/05-工具链/03-公司共享GPU工作节点与分时调度方法|公司共享 GPU 工作节点与分时调度方法]]：远程工作节点的网络、身份、队列和治理分层。
- [[domains/AI Agent工程/05-工具链/04-Real-ESRGAN远程超分案例|Real-ESRGAN 远程超分案例]]：Tailscale、SSH/SCP 和远程任务的实测案例。
