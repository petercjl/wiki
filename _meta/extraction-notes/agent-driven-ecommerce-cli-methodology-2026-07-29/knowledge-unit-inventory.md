# Knowledge Unit Inventory

| unit_id | knowledge_unit | role | expected_use |
| --- | --- | --- | --- |
| KU-01 | Agent 负责理解和编排，CLI 负责确定性执行 | architecture | 定义产品边界 |
| KU-02 | 核心框架跨渠道复用，平台差异进入适配器 | architecture | 新建 dycli、jdcli、alicli |
| KU-03 | CLI 同时提供人读和 Agent 读的能力清单 | discoverability | 能力发现与自然语言路由 |
| KU-04 | 命令注册表是路由、说明和测试的单一事实源 | governance | 防止文档漂移 |
| KU-05 | 业务、内部、开发能力分层展示 | product-design | 避免向业务用户暴露技术细节 |
| KU-06 | 专用浏览器身份和持久登录态可复用 | browser-runtime | 降低首次使用门槛 |
| KU-07 | 不导出 Cookie，请求在已登录页面上下文执行 | security | 减少凭据暴露 |
| KU-08 | 稳定数据命令必须先验证登录 | safety | 未登录即停止 |
| KU-09 | 每次 API 请求与重试前随机延时 | safety | 降低请求密度并统一节奏 |
| KU-10 | 登录、验证码、滑块、受限和风控信号立即停止 | safety | 不绕过平台安全机制 |
| KU-11 | 探测工具只服务发现，复用需求必须折回正式命令 | evolution | CLI持续演化 |
| KU-12 | 数据获取按结构化接口、运行时、渲染、OCR依次降级 | extraction | 选择可靠数据路径 |
| KU-13 | 价格混淆案例要求精确 ID、可验证还原和完整性门 | case | 处理展示值与接口值差异 |
| KU-14 | 开发数据与最终业务交付分层 | delivery | 隐藏中间技术细节 |
| KU-15 | 业务文件需有稳定工作表、字段和命名契约 | delivery | 可直接交付和复核 |
| KU-16 | 跨平台差异集中封装，业务命令保持一致 | portability | macOS/Windows复用 |
| KU-17 | npm全局安装、GitHub Release和OIDC发布形成分发闭环 | distribution | 团队安装更新 |
| KU-18 | 单元、打包、全新安装和真实小样本共同构成测试门 | qa | 防止只在开发机成功 |
| KU-19 | AGENTS.md、公共代码和测试形成三层治理 | governance | Codex长期维护 |
| KU-20 | 写网页需要预览、确认、幂等、防重复、回读和审计 | write-safety | 未来填写能力 |
| KU-21 | 平台特有登录、域名、接口、字段和风险信号不能硬编码进核心 | adapter-boundary | 多渠道扩展 |
| KU-22 | 首次登录等待、非Chrome支持与高风险写操作仍是待设计边界 | limitation | 防止把未来目标写成现状 |
