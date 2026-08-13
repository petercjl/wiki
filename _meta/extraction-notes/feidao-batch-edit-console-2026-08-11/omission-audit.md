# Omission Audit

| item | status | reason |
| --- | --- | --- |
| Cookie value | omitted-with-reason | 会话秘密，知识只需载体和寿命 |
| 32 位短会话 Token | omitted-with-reason | 会话秘密，知识只需签发流程 |
| 24 位续期凭证 | omitted-with-reason | 长期敏感凭证，绝不写入 Wiki |
| 授权码 | omitted-with-reason | 店铺添加敏感信息 |
| 登录 IP | omitted-with-reason | 个人/账号敏感数据 |
| 店铺 ID、积分、期限 | omitted-with-reason | 私密且随时间变化 |
| 商品标题、价格、库存明细 | omitted-with-reason | 经营敏感且不影响能力建模 |
| 头像和装饰图片 | raw-only | 不含独有功能知识，且可能识别账号 |
| admin/restricted API | raw-only | 与商家日常只读查询无关或敏感 |
| write API | raw-only | 用户明确 CLI 只允许查看 |
| unknown API | unresolved | 端点语义未确认，不执行探针 |

