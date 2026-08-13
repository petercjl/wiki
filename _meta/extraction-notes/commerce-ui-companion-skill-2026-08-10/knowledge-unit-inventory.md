# Knowledge Unit Inventory

| id | knowledge unit |
| --- | --- |
| KU01 | Skill 可显式组合，但当前开放格式不保证自动依赖注入。 |
| KU02 | 调用方必须按精确名称加载被调用 Skill 的当前完整说明和相对资源。 |
| KU03 | 稳定 CLI 可以拥有并分发伴生 Skill，CLI 目录应是唯一源码。 |
| KU04 | Agent 目录只应保存链接或受管副本，不应演化成独立源码。 |
| KU05 | CLI 应提供 source、status、install、update 和 doctor 发现面。 |
| KU06 | 链接即时继承更新；受管副本必须执行 update；未受管内容不得覆盖。 |
| KU07 | 调用 Skill 必须声明依赖名、解析方式、版本/contract、I/O、失败与回主线。 |
| KU08 | CLI 存在不等于 Agent 自动得知伴生 Skill；必须存在发现触点。 |
| KU09 | 宿主可能缓存 Skill catalog，安装或更新后可能需要刷新会话。 |
| KU10 | 向后兼容更新可自动流入，破坏性 contract 变化必须共存或迁移。 |
| KU11 | 自动声明与显式加载必须在干净上下文分别测试。 |
| KU12 | `commerce-ui` 1.1.0 是上述协议的已验证实例。 |
