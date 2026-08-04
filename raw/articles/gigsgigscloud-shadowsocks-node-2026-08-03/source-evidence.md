# GigsGigsCloud 东京 Shadowsocks 节点实践记录（脱敏原始证据）

- 记录日期：2026-08-03
- 来源形态：Codex 与用户协作完成的真实购买、部署、接入、测速与排障过程
- 地区：东京、日本
- 服务商：GigsGigsCloud
- 敏感信息处理：真实 IP、SSH 端口、实例编号、密码、支付信息、订阅令牌和节点分享链接均未写入

## 1. 目标与线路选择

原始目标不是单纯追求低 Ping，而是建立一个在中国大陆访问稳定、能使用常见网页与 AI 服务、可被 Mihomo/Clash/Shadowsocks 客户端使用的自建代理节点。

此前依次测试过 Vultr 新加坡、AWS 新加坡和 AWS 日本。AWS 两个地区在真实下载中不稳定，最终放弃。GigsGigsCloud 的东京 Premium China Route / CN Premium 线路被选作下一轮候选。

购买时使用的套餐快照：1 vCPU、1 GB 内存、20 GB SSD、200 GB 月流量、50 Mbps 端口。价格、库存、产品名和线路标签属于 2026-08-03 快照，后续购买必须以当前页面为准。

## 2. 重复购买与退款经验

因购物车和页面状态不够清晰，曾误购两台相同实例。处理原则：

1. 先通过延迟测试比较两个 IP，选定保留实例。
2. 不要先手工取消待退款实例。
3. 在财务部门提交英文退款工单，明确“退款哪台、保留哪台、重复购买、未使用、流量低于限制、退回原支付方式”。
4. 当时查到的服务商退款条件包括：新订单时间窗口、使用量阈值、无滥用、原路退款、必须提交 Finance 工单。政策和处理时效会变化，未来必须重新查当前官方条款。

这一步的关键经验是：退款资格与“手工取消”可能冲突；在没看清政策前不要删除或取消目标服务。

## 3. 操作系统与实例初始化

可选模板较旧，最终选择 Ubuntu 20.04 Server。虽然不是当前最新 LTS，但可以安装 Ubuntu 官方仓库中的 `shadowsocks-libev`，满足本次节点需求。

实例提供商使用非标准外部 SSH 端口，并显示默认登录用户与实例密码。客户端必须填写服务商页面给出的外部 SSH 端口，不能假设为 22。Termius 首次失败的直接原因就是仍然连接 22 端口。

首次连接形式：

```bash
ssh -p <SSH_PORT> <LOGIN_USER>@<SERVER_IP>
```

重装系统后如果出现主机密钥变化：

```bash
ssh-keygen -R '[<SERVER_IP>]:<SSH_PORT>'
```

登录后先更新系统：

```bash
sudo -i
apt update && apt full-upgrade -y
reboot
```

为了让自动化 Agent 后续安全接管，使用 Mac 上已有的服务器专用 Ed25519 公钥写入远端用户的 `~/.ssh/authorized_keys`，权限设置为目录 `700`、文件 `600`。不要在聊天中传输服务器密码。

## 4. 部署前线路基准测试

先测线路，再安装代理，避免在劣质线路上浪费配置时间。

测试由两部分组成：

- 本机到服务器：连续 Ping，观察基础延迟、平均值、最高值、标准差和丢包。
- 服务器到下载源：用 `curl` 下载东京测速源的大文件到 `/dev/null`，观察是否接近套餐 50 Mbps 上限。

当时结果：基础 Ping 约 42–45 ms，30 次测试 0% 丢包；服务器下载 100 MB 文件约 17.2 秒，约 48.7 Mbps，基本跑满 50 Mbps 端口。线路偶尔出现 90–130 ms 瞬时尖峰，因此仍需在真实代理负载下复测。

## 5. 安装 Shadowsocks 服务端

使用 Ubuntu 官方仓库软件包，避免来源不明的一键脚本：

```bash
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y shadowsocks-libev jq
```

服务端配置文件：

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

密码应使用密码学随机数生成器独立生成，不复用登录密码。启动并设置自启：

```bash
sudo systemctl restart shadowsocks-libev
sudo systemctl enable shadowsocks-libev
sudo systemctl is-active shadowsocks-libev
sudo systemctl is-enabled shadowsocks-libev
```

确认监听：

```bash
sudo ss -lntup | grep ':443 '
```

## 6. DynamicUser 配置权限故障

首次把 `/etc/shadowsocks-libev/config.json` 设置为 `600 root:root` 后，服务启动失败，日志提示：

```text
ERROR: Invalid config path.
```

原因是 Ubuntu 20.04 的 `shadowsocks-libev.service` 使用 `DynamicUser=true`；动态用户无法读取仅 root 可读的配置文件。将配置权限调整为可被服务读取后，服务正常启动并监听 `0.0.0.0:443` 的 TCP 和 UDP。

排障命令：

```bash
systemctl cat shadowsocks-libev
sudo systemctl status shadowsocks-libev --no-pager -l
sudo journalctl -u shadowsocks-libev -n 50 --no-pager
ls -l /etc/shadowsocks-libev/config.json
```

安全含义：配置文件包含代理密码。使用发行版默认动态用户服务时，要在“服务可读”和“最小暴露”之间平衡；实例上不应创建不受信任的本地账号。

## 7. GigsGigsCloud 安全组

入站安全组至少包含：

- 服务商分配的外部 SSH TCP 端口；
- ICMP（仅在需要 Ping 测试时开放）；
- TCP 443，来源 `0.0.0.0/0`；
- UDP 443，来源 `0.0.0.0/0`。

Shadowsocks 的 `tcp_and_udp` 需要同时开放 TCP 和 UDP 443。只开放 TCP 会导致部分 UDP 场景、语音、游戏或 QUIC 失败。

公网 443 开放后，日志很快出现来自不同 IP 的 `authentication error`。这是公网端口扫描和错误握手的常见表现；只要使用强随机密码、没有异常流量、服务版本受维护，不能仅凭这条日志判定节点泄漏。

## 8. 接入本机 Mihomo

本机个人节点文件：

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

主配置通过 file provider 引用该文件。修改后先校验：

```bash
mihomo -t -d /usr/local/etc/mihomo
```

再通过本机 Mihomo Controller API 热加载 provider，避免停止代理导致 Codex 和其他联网任务断线。热加载成功应返回 HTTP 204。随后确认 `Proxy` 组能看到新节点，再通过 API 切换。

本机 `clash_switch` 会读取 `Proxy` 组、对每个节点独立调用延迟测试、显示当前节点和最快节点，再让用户选择，不需要把节点名硬编码进脚本。

## 9. 真实代理测试结果

测试必须显式经过本机 Mihomo 代理端口，不能只测服务器自身下载：

```bash
curl -x http://127.0.0.1:7890 https://api.ipify.org
curl -x http://127.0.0.1:7890 -o /dev/null <LARGE_TEST_FILE_URL>
```

当时验证结果：

- 出口 IP 与东京服务器一致；
- 出口国家为 JP；
- Mihomo 节点延迟多次测量约 43–48 ms；
- 两次各 100 MB 的真实代理下载约 45.9–46.3 Mbps，接近 50 Mbps 上限；
- 负载期间 50 次 Ping 为 0% 丢包；
- 实际网页测试响应约 76–162 ms；
- OpenAI API 可建立连接并返回未授权 401，Gemini 返回 200；Claude 页面返回 403，只能说明到站可达但被站点策略或反自动化拦截，不能直接判定账户可用性。

结论：基础延迟和吞吐优秀，存在偶发 100 ms 以上尖峰；需要继续观察晚高峰、持续下载、长连接和多用户共享后的表现。

## 10. 客户端格式与协议兼容性

同一个服务端可以用不同“配置载体”，但协议必须一致：

### Mihomo / 标准 Clash Meta

使用完整 YAML 或 provider YAML，节点 `type: ss`，加密字段名为 `cipher`。

### Shadowsocks 客户端

使用 SIP002 `ss://` 分享链接，或手工填写服务器、443 端口、`chacha20-ietf-poly1305`、密码和 UDP。`ss://` 是单节点分享链接，不能粘贴到只接受 HTTP/HTTPS 的“订阅地址”输入框。

### Clash V-Ninja

实际可用的参考订阅包含 49 个 `type: ninja` 节点，并带 `method`、`password`、`node_password`、`tls` 等字段。该客户端导入标准 `type: ss` 时提示：

```text
unsupported proxy type: ss
```

这不是 YAML 缩进错误，而是客户端内核只接受其定制 Ninja 协议。不能把 `type: ss` 文本改成 `type: ninja` 来“转换”，因为服务端协议并没有改变。解决方法是改用标准 Mihomo/Clash Verge Rev 或普通 Shadowsocks 客户端；如果必须使用 V-Ninja，需要部署其兼容服务端和协议，不能靠改配置完成。

## 11. 分享与多用户风险

把包含密码的 YAML、JSON 或 `ss://` 链接发给同事，就等于授予其持续使用服务器流量的权限。分享前需要明确：

- 只发给可信用户；
- 200 GB 月流量会被多人共同消耗；
- 任何人转发链接都会扩大访问范围；
- 出现异常流量时应轮换 Shadowsocks 密码并重新分发；
- 不要把节点密码、服务器登录密码、SSH 私钥混为一谈；
- 分享文件本地权限可设为 `600`，但文件发送出去后无法依赖本地权限继续保护。

## 12. 日常运维检查表

```bash
# 服务状态
sudo systemctl is-active shadowsocks-libev
sudo systemctl is-enabled shadowsocks-libev

# 端口监听
sudo ss -lntup | grep ':443 '

# 最近日志
sudo journalctl -u shadowsocks-libev --since '1 hour ago' --no-pager

# 资源
free -h
uptime

# 本机配置校验和节点切换
mihomo -t -d /usr/local/etc/mihomo
clash_switch
```

长期运行还应补充：月流量监控、系统安全更新、密码轮换记录、晚高峰抽测、磁盘/内存告警和服务商线路/退款政策复核。

## 13. 当前边界

- 这是 2026-08-03 的单机真实实践，不代表所有 GigsGigsCloud IP 或所有运营商路径。
- 50 Mbps 和 200 GB 是购买快照，不应写成服务商永久承诺。
- Ubuntu 20.04 和 `shadowsocks-libev 3.3.4` 属于当时可用组合，未来应优先选择仍在安全维护期的系统和实现。
- 本轮没有建立服务端多用户独立账号、每用户流量计量或自动封禁系统。
- V-Ninja 的 Ninja 协议没有在本服务器部署。
