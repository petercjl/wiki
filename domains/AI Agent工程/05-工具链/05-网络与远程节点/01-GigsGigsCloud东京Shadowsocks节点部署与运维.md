---
title: GigsGigsCloud 东京 Shadowsocks 节点部署与运维
type: playbook
created: 2026-08-03
updated: 2026-08-03
domain: AI Agent工程
tags: [toolchain, network, remote-node, shadowsocks, mihomo, playbook]
sources:
  - raw/articles/gigsgigscloud-shadowsocks-node-2026-08-03/source-evidence.md
  - _meta/extraction-notes/gigsgigscloud-shadowsocks-node-2026-08-03/coverage-matrix.md
  - _meta/extraction-notes/gigsgigscloud-shadowsocks-node-2026-08-03/image-inventory.md
status: active
---

# GigsGigsCloud 东京 Shadowsocks 节点部署与运维

这是一套从候选线路到可长期使用代理节点的完整验收方法。它来自 2026-08-03 的真实东京 Premium China Route 实践，但真正可复用的部分不是某个 IP，而是“线路基准—服务部署—云防火墙—客户端接入—真实业务验证—持续运维”的闭环。

> [!warning] 时间与安全边界
> 套餐、库存、退款政策、线路质量、系统模板和软件版本都会变化，执行时必须重新核对当前页面。文中的 IP、SSH 端口和密码均使用占位符；不要把服务器登录密码、SSH 私钥、Shadowsocks 密码或完整 `ss://` 链接写入知识库或聊天记录。

## 一、先定义“好节点”的验收标准

低 Ping 只能说明基础往返时延，不能代替真实代理体验。一个候选节点至少要同时通过五项检查：

| 维度 | 观察方式 | 判断重点 |
| --- | --- | --- |
| 基础延迟 | 本机连续 Ping | 平均值、最大值、抖动、丢包 |
| 服务器出口 | 服务器下载大文件到 `/dev/null` | 是否接近套餐端口上限 |
| 代理吞吐 | 明确经过本机 Mihomo 端口下载 | 服务、加密和链路叠加后的真实速度 |
| 负载稳定性 | 下载同时连续 Ping | 是否出现丢包或大幅延迟尖峰 |
| 目标服务可达性 | 通过代理访问实际网页/API | 出口地区、TCP/TLS 可达性、站点策略和账户可用性要分开判断 |

本次案例的时间快照是：基础延迟约 42–45 ms、30 次 Ping 0% 丢包；服务器下载约 48.7 Mbps；两次 100 MB 代理下载约 45.9–46.3 Mbps；Mihomo 延迟约 43–48 ms。偶尔出现 100 ms 以上尖峰，因此仍需观察晚高峰和多人负载。

## 二、购买与重复订单门禁

不要在购物车状态不清晰时重复点击购买。若误购两台相同实例：

1. 先分别测试两个 IP，确定保留哪一台。
2. 在没有看清退款条款前，不要先手工取消或删除待退款实例。
3. 向财务部门提交工单，写清“退款哪台、保留哪台、重复购买、未使用、流量低于限制、希望原路退回”。
4. 重新核对当前退款窗口、流量阈值、滥用条款和工单部门。

退款资格与“实例已取消”可能冲突。先查政策、再交工单、最后按客服要求处理资源。

## 三、系统模板、SSH 与初始化

本次可用模板较旧，最终选用 Ubuntu 20.04，因为官方仓库仍能提供 `shadowsocks-libev`。未来部署应优先选择仍处于安全维护期、且能稳定安装所需实现的系统。

GigsGigsCloud 会在实例概览中显示登录用户和外部 SSH 端口。该端口不一定是 22；Termius 或终端必须显式填写服务商给出的端口：

```bash
ssh -p <SSH_PORT> <LOGIN_USER>@<SERVER_IP>
```

重装后主机密钥变化时，删除对应的旧记录：

```bash
ssh-keygen -R '[<SERVER_IP>]:<SSH_PORT>'
```

首次登录后更新并重启：

```bash
sudo -i
apt update && apt full-upgrade -y
reboot
```

自动化接管优先使用专用 Ed25519 公钥。远端 `~/.ssh` 目录权限设为 `700`，`authorized_keys` 设为 `600`。不要把实例密码发给 Agent；由用户在可信终端完成首次登录和密钥授权。

> [!danger] 重装操作
> “重装服务器”会立即破坏系统上的全部数据。只查看模板不等于提交重装；执行前必须确认实例、备份、目标系统和停机影响。

## 四、部署前先测线路

先测本机到服务器：

```bash
ping -c 30 <SERVER_IP>
```

再从服务器下载与机房接近的测速文件，避免磁盘成为变量：

```bash
curl -L -o /dev/null <LARGE_TEST_FILE_URL>
```

若服务器出口本身长期远低于套餐上限，先换 IP、机房或服务商；不要急着安装代理。若服务器出口正常、本机到服务器丢包明显，问题更可能在跨境线路或本地运营商路径。

## 五、安装 Shadowsocks 服务端

优先使用发行版官方仓库，不使用来源不明的一键脚本：

```bash
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y shadowsocks-libev jq
```

服务端配置文件通常为：

```text
/etc/shadowsocks-libev/config.json
```

脱敏配置结构：

```json
{
  "server": "0.0.0.0",
  "server_port": 443,
  "password": "<RANDOM_STRONG_PASSWORD>",
  "timeout": 300,
  "method": "chacha20-ietf-poly1305",
  "mode": "tcp_and_udp",
  "fast_open": false
}
```

口令必须由密码学随机数生成器独立生成，不得复用服务器登录密码。启动、自启并验证：

```bash
sudo systemctl restart shadowsocks-libev
sudo systemctl enable shadowsocks-libev
sudo systemctl is-active shadowsocks-libev
sudo systemctl is-enabled shadowsocks-libev
sudo ss -lntup | grep ':443 '
```

完成条件是服务状态为 active/enabled，且 TCP、UDP 443 都在监听。

## 六、处理 DynamicUser 配置权限故障

如果日志出现：

```text
ERROR: Invalid config path.
```

不要只检查 JSON 语法。Ubuntu 20.04 的发行版服务可能使用 `DynamicUser=true`；当配置文件为 `600 root:root` 时，动态用户无法读取它。

按以下顺序诊断：

```bash
systemctl cat shadowsocks-libev
sudo systemctl status shadowsocks-libev --no-pager -l
sudo journalctl -u shadowsocks-libev -n 50 --no-pager
ls -l /etc/shadowsocks-libev/config.json
```

确认服务账户模型后，把配置权限调整到“服务可读、其他本地用户尽量不可读”的最小范围，再重启验证。配置内含代理密码，因此不要为了图省事把文件无条件开放给所有本地用户；实例也不应创建不受信任的本地账号。

## 七、安全组必须同时允许 TCP 与 UDP

入站规则至少包括：

- 服务商分配的 SSH TCP 端口；
- TCP 443，来源 `0.0.0.0/0`；
- UDP 443，来源 `0.0.0.0/0`；
- ICMP 仅在需要 Ping 诊断时开放，并按安全策略决定是否长期保留。

`mode: tcp_and_udp` 要求云防火墙同时开放 TCP 与 UDP 443。只开放 TCP 可能表现为网页能开，但 QUIC、语音、游戏或其他 UDP 场景失败。

安全组必须把 SSH 管理端口与代理端口分离，并同时开放 TCP 443 和 UDP 443。

![[raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/derived-security-group-redacted.png]]

图：脱敏后的 GigsGigsCloud 入站安全组。关键关系是 SSH 管理端口与代理端口分离，同时存在 TCP 443 和 UDP 443；地址栏、实例标识和 SSH 外部端口已遮盖。

公网端口开放后出现零散 `authentication error`，通常是扫描或错误握手，不等于凭据已泄漏。仍需使用强随机口令、监控异常流量、保持服务版本受维护，并在怀疑泄漏时立即轮换密码。

## 八、接入 Mihomo

个人节点可放入 file provider，例如：

```text
/usr/local/etc/mihomo/providers/provider-peter.yaml
```

节点结构：

```yaml
proxies:
  - name: "Japan-GigsGigs-SS"
    type: ss
    server: <SERVER_IP>
    port: 443
    cipher: chacha20-ietf-poly1305
    password: "<RANDOM_STRONG_PASSWORD>"
    udp: true
```

修改后先校验：

```bash
mihomo -t -d /usr/local/etc/mihomo
```

再通过 Mihomo Controller API 热加载 provider，避免 `clash_stop` 造成当前 Codex 或其他联网任务断线。热加载成功通常返回 HTTP 204。随后确认 `Proxy` 组出现新节点，再切换。

`clash_switch` 应动态读取 `Proxy` 组，为每个节点独立测速，并显示当前节点和最快节点；不要把节点名硬编码到辅助脚本。

## 九、真实代理验证

服务器自身测速通过后，还必须显式经过本机 Mihomo 端口：

```bash
curl -x http://127.0.0.1:7890 https://api.ipify.org
curl -x http://127.0.0.1:7890 -o /dev/null <LARGE_TEST_FILE_URL>
```

建议按以下顺序记录：

1. 出口 IP 是否等于目标服务器。
2. 出口国家/地区是否符合预期。
3. 100–200 MB 文件的平均吞吐。
4. 下载期间的 Ping、丢包和尖峰。
5. 晚高峰、长连接和多用户同时使用表现。
6. 实际网页与 AI 服务能否使用。

HTTP 状态码要分层解释：

- `200`：该请求层面成功。
- `401`：通常说明网络、DNS、TCP/TLS 和服务入口可达，但缺少有效授权。
- `403`：说明到站可达，但可能被地区、站点策略、账户规则或反自动化机制阻止。

因此，API 返回 401/403 不能直接证明“账户可以使用”，只能证明不同层级的可达性。

## 十、客户端与协议兼容性

| 客户端 | 正确载体 | 核心字段/注意点 |
| --- | --- | --- |
| Mihomo / Clash Meta | 完整 YAML 或 provider YAML | `type: ss`、`cipher`、`udp: true` |
| 普通 Shadowsocks 客户端 | SIP002 `ss://` 或手工填写 | 服务器、443、加密方法、密码、UDP |
| 只接受 HTTP/HTTPS 的订阅框 | 不能直接粘贴单节点 `ss://` | 需要真正的订阅服务或改用单节点导入入口 |
| Clash V-Ninja | 定制 Ninja 协议 | 标准 `type: ss` 会报 `unsupported proxy type: ss` |

V-Ninja 的问题不是 YAML 缩进，也不能把 `type: ss` 文本改成 `type: ninja` 来转换；配置载体变了，服务端协议并没有变。必须改用支持标准 Shadowsocks 的客户端，或另外部署其兼容协议服务端。

## 十一、分享给同事的治理边界

发送 YAML、JSON 或 `ss://` 链接等价于授予持续使用服务器流量的权限：

- 只分享给可信用户；
- 多人共同消耗月流量；
- 转发会扩大访问范围，发送后无法依靠本地文件权限继续保护；
- 出现异常流量时轮换 Shadowsocks 密码并重新分发；
- 代理密码、服务器登录密码和 SSH 私钥必须分离；
- 需要按用户计量、撤销或审计时，单口令单实例模式已经不够，应改用支持独立身份和配额的方案。

## 十二、日常运维清单

```bash
# 服务状态与自启
sudo systemctl is-active shadowsocks-libev
sudo systemctl is-enabled shadowsocks-libev

# TCP/UDP 监听
sudo ss -lntup | grep ':443 '

# 最近日志
sudo journalctl -u shadowsocks-libev --since '1 hour ago' --no-pager

# 资源
free -h
uptime

# 本机配置与节点切换
mihomo -t -d /usr/local/etc/mihomo
clash_switch
```

长期运行还应建立月流量监控、系统安全更新、密码轮换记录、晚高峰抽测、磁盘/内存告警，以及服务商线路和政策复核。

## 十三、故障路由表

| 症状 | 优先检查 |
| --- | --- |
| Termius 显示 connection refused | 是否仍连接 22；核对服务商外部 SSH 端口和安全组 |
| 服务报 `Invalid config path` | `DynamicUser`、配置文件属主/权限、服务日志 |
| TCP 网页正常但 UDP 应用失败 | 服务端 `tcp_and_udp`、UDP 监听、云防火墙 UDP 443 |
| 服务器测速快、代理下载慢 | 本机代理配置、加密实现、Mihomo 端口、客户端规则和本地网络 |
| 出口 IP 没变化 | 测试请求没有显式走 Mihomo，或节点未真正切换 |
| YAML 导入报不支持 `ss` | 客户端内核不支持标准 Shadowsocks，而非简单格式错误 |
| 日志出现大量认证错误 | 先判断公网扫描，再看流量、来源和凭据泄漏迹象 |
| AI 网站 403 | 分开检查地区、账户、浏览器验证和反自动化策略 |

## 完成定义

只有以下条件同时成立，节点才算完成：

- 服务端 active/enabled，TCP 与 UDP 443 均监听；
- 云安全组允许必要的 TCP/UDP 流量；
- Mihomo 配置校验通过并成功加载节点；
- 代理出口 IP 和地区正确；
- 大文件代理吞吐、负载丢包和晚高峰表现达到可接受标准；
- 目标网页和 AI 服务经过真实客户端验证；
- 凭据、分享对象、流量监控和轮换机制有明确边界。

## 相关记忆

- [[domains/AI Agent工程/05-工具链/05-网络与远程节点/index|网络与远程节点]]
- [[queries/VPS代理节点部署与排障|VPS 代理节点部署与排障]]
- [[domains/AI Agent工程/05-工具链/03-公司共享GPU工作节点与分时调度方法|公司共享 GPU 工作节点与分时调度方法]]
- [[domains/AI Agent工程/05-工具链/04-Real-ESRGAN远程超分案例|Real-ESRGAN 远程超分案例]]

## 来源与版本

- 实践日期：2026-08-03。
- 来源证据：[[raw/articles/gigsgigscloud-shadowsocks-node-2026-08-03/source-evidence|GigsGigsCloud 东京 Shadowsocks 节点实践记录]]。
- 覆盖记录：[[_meta/extraction-notes/gigsgigscloud-shadowsocks-node-2026-08-03/coverage-matrix|Coverage Matrix]]。
- 本次只验证单实例、单共享口令模式；未实现每用户独立账号、流量计量、自动封禁或 V-Ninja 协议服务端。
