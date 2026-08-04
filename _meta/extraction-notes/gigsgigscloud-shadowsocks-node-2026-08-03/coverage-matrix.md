# Coverage Matrix

| source_unit_id | source_location | source_unit | knowledge_role | target_pages | status | reason_or_notes |
| --- | --- | --- | --- | --- | --- | --- |
| SU-01 | raw §1 | 目标与线路选择 | decision | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第一节定义五维验收标准并保留实测快照 |
| SU-02 | raw §2 | 重复购买与退款经验 | caveat | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第二节保留退款动作顺序并标记政策时效 |
| SU-03 | raw §3 | OS、SSH 与更新 | procedure | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第三节包含系统选择、非标准 SSH 端口、known_hosts、更新与重启 |
| SU-04 | raw §3 | SSH 公钥授权 | security | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | merged | 合并进第三节的专用密钥和首次授权边界 |
| SU-05 | raw §4 | 部署前线路基准 | validation | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第四节分离本机到服务器与服务器出口基准 |
| SU-06 | raw §5 | 安装 shadowsocks-libev | installation | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第五节保留官方仓库安装命令 |
| SU-07 | raw §5 | 服务端配置 | configuration | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第五节保留完整脱敏 JSON、强口令和 systemd/监听验收 |
| SU-08 | raw §6 | DynamicUser 权限故障 | troubleshooting | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第六节保留错误、根因、诊断命令和最小权限边界 |
| SU-09 | raw §7 | 安全组规则 | network-security | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第七节和脱敏截图明确 TCP/UDP 443 双重放行 |
| SU-10 | raw §7 | 公网扫描日志 | caveat | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | merged | 合并进第七节的扫描解释与轮换条件 |
| SU-11 | raw §8 | Mihomo 接入 | integration | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第八节保留 provider 路径和 `type: ss` 配置 |
| SU-12 | raw §8 | 校验、热加载与切换 | operations | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第八节包含配置校验、Controller 热加载和动态 clash_switch 原则 |
| SU-13 | raw §9 | 真实代理测试 | validation | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第九节保留代理端口、出口、吞吐、负载和 HTTP 状态分层 |
| SU-14 | raw §10 | Mihomo/Clash YAML | compatibility | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第十节兼容性表 |
| SU-15 | raw §10 | Shadowsocks ss:// | compatibility | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第十节说明 SIP002 单节点链接与订阅框差异 |
| SU-16 | raw §10 | V-Ninja 协议边界 | troubleshooting | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第十节保留错误文本、协议根因和不可伪转换边界 |
| SU-17 | raw §11 | 多用户分享风险 | governance | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第十一节覆盖信任、流量、转发、轮换和身份隔离 |
| SU-18 | raw §12 | 日常运维检查 | playbook | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 第十二节保留命令与长期检查项 |
| SU-19 | raw §13 | 时间与能力边界 | limitation | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 开头警告、来源与版本及完成定义均标记时间快照和未实现能力 |
| IMG-02D | image-inventory IMG-02D | 脱敏安全组截图：SSH 管理端口与 TCP/UDP 443 规则分离 | procedural-image | domains/AI Agent工程/05-工具链/05-网络与远程节点/01-GigsGigsCloud东京Shadowsocks节点部署与运维.md | formalized | 正式页第七节已嵌入并提供可搜索语义图注 |
