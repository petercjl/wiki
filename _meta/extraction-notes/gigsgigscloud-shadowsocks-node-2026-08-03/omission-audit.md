# Omission Audit

| item | disposition | reason |
| --- | --- | --- |
| 真实服务器 IP 与实例编号 | omitted-with-reason | 私人基础设施端点，不影响方法复用 |
| SSH 外部端口和登录密码 | omitted-with-reason | 认证与攻击面信息；正式知识使用占位符 |
| Shadowsocks 密码和 ss:// 链接 | omitted-with-reason | 持续访问凭据，不进入知识库 |
| 支付账号、邮箱、信用卡和支付流水 | omitted-with-reason | 财务与身份敏感信息 |
| 退款工单编号 | omitted-with-reason | 私人账户记录；保留流程即可 |
| 第三方机场订阅 URL、token 和节点密码 | omitted-with-reason | 第三方凭据，不属于本知识主题 |
| 聊天中的逐句交互 | raw-only | 已抽取为操作证据手册；逐句界面往返不增加知识价值 |
| AWS 实例的具体 IP 和已删除资源标识 | omitted-with-reason | 已终止资源且属于私人基础设施历史 |
| 实例概览原始截图 | raw-only | 含真实 IP、IPv6、服务编号、主机名和 SSH 端口；知识已文字化，原图仅作私有证据 |
| 安全组原始截图 | raw-only | 含实例上下文和 SSH 外部端口；正式页使用脱敏派生图 |
| 重装页面原始截图 | raw-only | 地址栏含实例和会话参数；破坏性警告及模板入口已文字化 |
| SSH 密钥页面原始截图 | raw-only | 含密钥名称和指纹；正式页不需要这些私人细节 |
