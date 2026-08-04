# Knowledge Unit Inventory

| knowledge_unit_id | source_unit_id | reusable_knowledge |
| --- | --- | --- |
| KU-01 | SU-01 | 代理线路选择必须同时验证延迟、丢包、吞吐、晚高峰和目标服务可达性 |
| KU-02 | SU-02 | 重复购买退款前不得先取消实例，应先核对当前退款资格和财务工单要求 |
| KU-03 | SU-03 | 服务商非标准 SSH 端口必须显式写入终端/Termius 配置 |
| KU-04 | SU-03 | 重装后处理 known_hosts，并在部署前完成系统更新与重启 |
| KU-05 | SU-04 | 用专用 SSH 密钥接管自动化，禁止通过聊天传递服务器密码 |
| KU-06 | SU-05 | 部署前先做本机到服务器和服务器到下载源的双向基准 |
| KU-07 | SU-06 | 优先发行版官方包而非来源不明的一键脚本 |
| KU-08 | SU-07 | TCP/UDP 443、AEAD 密码和强随机口令的服务端配置契约 |
| KU-09 | SU-08 | DynamicUser 服务无法读取 600 root-only 配置时会报 Invalid config path |
| KU-10 | SU-09 | `tcp_and_udp` 要求安全组同时开放 TCP 与 UDP 443 |
| KU-11 | SU-10 | 公网 authentication error 多为扫描，不等于凭据泄漏 |
| KU-12 | SU-11 | Mihomo file provider 中 Shadowsocks 节点使用 `type: ss` 和 `cipher` |
| KU-13 | SU-12 | 先 `mihomo -t`，再 Controller API 热加载，避免断开当前代理 |
| KU-14 | SU-12 | 动态读取代理组的 `clash_switch` 比硬编码节点辅助脚本更可维护 |
| KU-15 | SU-13 | 真实测试必须显式经过代理端口，并核对出口 IP/国家 |
| KU-16 | SU-13 | HTTP 401/403 只能证明不同层级的可达性，不能直接证明账户服务可用 |
| KU-17 | SU-14 | 标准 Mihomo/Clash Meta 可使用完整 YAML 或 provider YAML |
| KU-18 | SU-15 | Shadowsocks 客户端使用 SIP002 `ss://`，不能把它当 HTTP 订阅 URL |
| KU-19 | SU-16 | V-Ninja 的 `type: ninja` 是协议差异，不是把 `ss` 改名即可转换的格式差异 |
| KU-20 | SU-17 | 分享节点配置等价于持续授权服务器流量，必须管理信任、流量和密码轮换 |
| KU-21 | SU-18 | 运维最小检查覆盖 systemd、自启、监听、日志、资源、配置校验和节点测速 |
| KU-22 | SU-19 | 套餐、政策、线路与软件版本都属于时间快照，执行前必须复核 |
