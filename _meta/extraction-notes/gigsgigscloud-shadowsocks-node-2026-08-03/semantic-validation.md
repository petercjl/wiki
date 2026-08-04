# Semantic Validation

- Status: passed
- Raw evidence preserved: yes
- Validation scope: browser accessibility text, screenshots, terminal output, and manually structured operational evidence
- Evidence sources: source-evidence.md, GigsGigsCloud rendered screenshots, Chrome accessibility tree, terminal commands and repeated runtime checks
- Systematic variant search: passed
- Formal text checked against normalized anchors: passed

## High-Risk Anchor Inventory

| anchor_id | source_location | anchor_type | raw_form | normalized_form | evidence | confidence | disposition | formal_handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | raw §1–§3 + screenshots | platform-or-product | GigsGigs / GigsGigsCloud；JP: Premium China Route | GigsGigsCloud；东京 Premium China Route | 客户中心品牌、产品侧栏、实例页面和 source-evidence.md 重复一致 | high | accepted-as-is | 正式标题使用 GigsGigsCloud；线路名按 2026-08-03 页面快照处理 |
| A02 | raw §3 + instance overview | UI-and-parameter | 默认实例端口不是 22 | 服务商显示的外部 SSH 端口必须显式配置，不假设为 22 | 实例概览、Termius connection refused 日志和随后非标准端口成功登录相互印证 | high | accepted-as-is | 正式页只保留 `<SSH_PORT>` 占位符，不记录真实端口 |
| A03 | raw §5–§7 + security-group image | command-and-network-rule | `mode: tcp_and_udp`；TCP 443；UDP 443 | Shadowsocks 同时监听并在云防火墙放行 TCP 443 与 UDP 443 | 服务配置、`ss -lntup` 验证、控制台规则及脱敏派生图一致 | high | accepted-as-is | 正式页保留配置、命令、规则和语义图注 |
| A04 | raw §1、§4、§9、§13 | metrics-and-limits | 50 Mbps、200 GB、42–45 ms、0% 丢包、45.9–46.3 Mbps | 2026-08-03 单实例测试快照，不是服务商长期承诺 | 套餐页面、服务器下载、代理下载和 Ping 测试记录交叉一致 | high | accepted-as-is | 所有数字均附时间快照、单 IP 和继续晚高峰复测边界 |
| A05 | raw §3、§5、§6、§13 | version-and-causal-claim | Ubuntu 20.04；shadowsocks-libev；`DynamicUser=true`；`Invalid config path` | 本次 Ubuntu 20.04 发行版服务因动态用户无法读取 root-only 配置而启动失败 | systemd unit、status/journal、文件权限和调整后成功监听相互印证 | high | accepted-as-is | 正式页保留诊断顺序，不泛化为所有发行版/版本 |
| A06 | raw §10 | protocol-boundary | `unsupported proxy type: ss`；`type: ninja` | V-Ninja 内核协议不兼容标准 Shadowsocks，不能靠改 YAML 类型名转换 | 可用 V-Ninja 参考配置与实际导入错误一致 | high | accepted-as-is | 正式页明确区分配置载体与服务端协议 |

## Validation Notes

- 未使用 OCR 读取配置或端口；安全组字段来自页面可访问性结构和原始截图的双重证据。
- 正式页未保留浏览器地址栏中的会话参数、真实端点、端口、密码、指纹或分享链接。
- 全局检索确认 `GigsGigsCloud`、`DynamicUser`、`tcp_and_udp`、`V-Ninja` 和关键实测数字在 raw、提取笔记和正式页中含义一致。
