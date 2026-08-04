# Image Analysis

## IMG-02D：脱敏后的安全组规则

- visual_claim: GigsGigsCloud 的入站安全组中，SSH 管理端口与 Shadowsocks 代理端口是不同规则；代理服务同时存在 TCP 443 和 UDP 443，CIDR 为公网来源。
- visible_text: `Protocol`、`Start Port`、`End Port`、`CIDR`、TCP 443、UDP 443、ICMP，以及安全组 `Ingress` 页面结构。
- relation_to_source: 直接支持 SU-09/KU-10，即 `mode: tcp_and_udp` 需要服务端监听与云安全组的 TCP/UDP 双重放行。
- semantic_anchor: 正式页“七、安全组必须同时允许 TCP 与 UDP”章节。
- sensitive_handling: 从原图 IMG-02 派生；地址栏 URL、实例/服务标识和 SSH 外部端口以不透明灰色矩形遮盖。原图不进入正式页。
- confidence: high；TCP/UDP 443 和 CIDR 在源截图与页面可访问性文本中一致。
- ambiguity: 截图只能证明 2026-08-03 当时的规则形态，不能证明服务端一直在监听或规则之后未被修改；运行时仍需用 `ss`、systemd 和当前控制台复核。
