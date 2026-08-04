# Image Inventory

| image_id | source_location | archived_path | image_class | semantic_anchor | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMG-01 | GigsGigsCloud 实例概览 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/01-instance-overview-loaded.jpg | sensitive | 实例概览显示系统、资源、月流量、登录用户和非标准 SSH 端口的位置 | 无 | raw-only | 含真实 IP、IPv6、服务编号、主机名和 SSH 端口；文字知识已在 SU-03、SU-19 正式化，原图仅留私有证据 |
| IMG-02 | GigsGigsCloud 安全组规则 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/02-security-group.jpg | sensitive | 入站规则同时包含 TCP 443 与 UDP 443 | 无 | raw-only | 含实例上下文和真实 SSH 外部端口；不嵌入正式页 |
| IMG-02D | IMG-02 脱敏派生图 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/derived-security-group-redacted.png | procedural | 安全组必须把 SSH 管理端口与代理端口分离，并同时开放 TCP 443 和 UDP 443 | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 地址栏、实例标识和 SSH 外部端口已使用不透明色块遮盖；正式页已嵌入 |
| IMG-03 | GigsGigsCloud 重装页面 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/03-reinstall-templates.jpg | sensitive | 重装会破坏全部数据；新的系统模板从此入口选择 | 无 | raw-only | 地址栏含实例和会话参数；正式页以文字警告承载，不嵌入原图 |
| IMG-04 | GigsGigsCloud SSH 密钥页面 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/04-ssh-keys.jpg | sensitive | SSH 密钥页面提供已注册密钥、Register Key 和 Generate Key 入口 | 无 | raw-only | 含密钥名称、指纹和实例上下文；不进入正式页 |
| IMG-DUP-01 | Computer Use 首次载入截图 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/capture-failed-instance-overview.jpeg | duplicate | 页面尚未完成载入的空白/不完整实例概览 | 无 | raw-only | 首次抓取失败副本；由 IMG-01 替代，仅留作采集审计 |
| IMG-DUP-02 | IMG-01 的早期副本 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/duplicate-instance-overview.jpeg | duplicate | 与 IMG-01 相同的实例概览内容 | 无 | raw-only | 早期重复采集文件；已机械修正为匹配 JPEG 内容的扩展名，由 IMG-01 替代 |
| IMG-DUP-03 | IMG-02 的早期副本 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/duplicate-security-group.jpeg | duplicate | 与 IMG-02 相同的安全组内容 | 无 | raw-only | 早期重复采集文件；由 IMG-02 和 IMG-02D 替代 |
| IMG-DUP-04 | IMG-03 的早期副本 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/duplicate-reinstall-templates.jpeg | duplicate | 与 IMG-03 相同的重装警告页面 | 无 | raw-only | 早期重复采集文件；由 IMG-03 替代 |
| IMG-DUP-05 | IMG-04 的早期副本 | raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/duplicate-ssh-keys.jpeg | duplicate | 与 IMG-04 相同的 SSH 密钥页面 | 无 | raw-only | 早期重复采集文件；由 IMG-04 替代 |

## Counts

- archived original/early-capture files: 9
- derived redacted images: 1
- formalized: 1
- merged: 0
- raw-only: 9
- omitted-with-reason: 0
- unresolved: 0
- embedded: 1
