# GigsGigsCloud Shadowsocks 节点截图清单

采集日期：2026-08-03

这些截图来自用户已登录的 GigsGigsCloud 客户中心，仅作为私有知识库证据。截图可能包含实例 IP、服务编号、SSH 端口或密钥指纹，禁止直接发布到公开文档。

| 文件 | 页面 | 适合说明的知识点 | 敏感性 |
| --- | --- | --- | --- |
| `raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/01-instance-overview-loaded.jpg` | 实例概览 | 系统、CPU、内存、磁盘、月流量、登录用户与非标准 SSH 端口的位置 | 高：含实例端点信息 |
| `raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/02-security-group.jpg` | 安全组入站规则 | SSH 外部端口、ICMP、Shadowsocks TCP 443 与 UDP 443 均需放行 | 中：含开放端口与实例上下文 |
| `raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/03-reinstall-templates.jpg` | 重装服务器 | 重装会破坏全部数据；选择“新的操作系统模板”后再选系统，但不得误点提交 | 中：含实例上下文与会话 URL |
| `raw/assets/gigsgigscloud-shadowsocks-node-2026-08-03/04-ssh-keys.jpg` | SSH 密钥 | 已注册密钥的位置，以及 Register Key / Generate Key 入口 | 高：含密钥名称与指纹 |

## 正式文档使用建议

- 正文优先使用安全组截图，因为它最直接解释代理端口的 TCP/UDP 双栈放行要求。
- 实例概览截图用于解释如何核对系统、资源、流量限额和 SSH 入口。
- 重装截图只用于强调数据破坏风险与系统模板入口，不应把“重装服务器”按钮描述成普通下一步。
- SSH 密钥截图在正式文档中应裁切或打码密钥名称、指纹和实例标识后再使用。
- 所有可公开分享的版本都必须对 IP、IPv6、服务编号、主机名、SSH 端口、密钥指纹和地址栏会话参数做脱敏。

## 可用系统模板（页面无截图模式下的辅助记录）

通过页面的可访问性信息确认，模板列表包含 CentOS 7/8、Debian 9/10/11 with BBR、Fedora 34、FreeBSD 13、MikroTik RouterOS、VyOS，以及 Ubuntu 16.04/18.04/20.04。此次节点采用 Ubuntu 20.04。
