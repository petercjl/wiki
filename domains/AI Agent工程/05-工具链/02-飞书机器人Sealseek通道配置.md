---
title: 飞书机器人 Sealseek 通道配置
type: playbook
created: 2026-07-10
tags:
  - feishu
  - lark
  - sealseek
  - channel
  - bot
  - 飞书
  - 机器人
  - 权限
  - 事件订阅
aliases:
  - Feishu bot setup
  - 飞书机器人配置
  - Lark bot channel config
---

# 飞书机器人 Sealseek 通道配置

将飞书自建机器人连接 Sealseek（Sealseek），实现私聊 AI 回复 + 群聊 @机器人 AI 回复。

## 前置条件

- 飞书企业管理员账号
- 飞书开放平台（https://open.feishu.cn/app）可创建自建应用
- Sealseek/Sealseek Gateway 运行中

## 配置流程

```
飞书侧：机器人能力 → 权限 → 事件订阅 → 发布
Sealseek 侧：配置凭证 → 重启 Gateway
```

### 飞书侧配置

#### 1. 添加机器人能力

应用管理 → 添加应用能力 → 添加「机器人」

#### 2. 权限配置（批量导入 JSON）

权限管理 → 批量导入/导出权限 → 导入：

```json
{
  "scopes": {
    "tenant": [
      "im:message.p2p_msg:readonly",
      "im:message.group_at_msg:readonly",
      "im:message",
      "im:chat:readonly",
      "contact:user.employee_id:readonly"
    ],
    "user": []
  }
}
```

**权限说明：**

| 权限 Scope ID | 用途 | 必须 |
|-------------|------|------|
| `im:message.p2p_msg:readonly` | 接收私聊消息 | ✅ |
| `im:message.group_at_msg:readonly` | 接收群聊 @消息 | ✅ |
| `im:message` | 发送消息 | ✅ |
| `im:chat:readonly` | 获取群信息 | ✅ |
| `contact:user.employee_id:readonly` | 获取用户 ID | ✅ |

**不推荐的权限：**

- `im:message.group_msg` / `im:message.group_msg:readonly`：敏感权限，获取群内所有消息（包括不 @机器人的消息）。Sealseek 的 `requireMention` 默认开启，不需要这个权限。

#### 3. 事件订阅

事件与回调 → 添加事件 → 搜索 `im.message.receive_v1` → 添加。

订阅方式选「通过长连接接收事件」（WebSocket），不需要公网回调 URL。

**⚠️ 权限与事件的区别：**

- **权限（Scope）**：格式如 `im:message.p2p_msg:readonly`（冒号分隔，`:readonly` 后缀），在「权限管理」页面添加
- **事件（Event）**：格式如 `im.message.receive_v1`（点号分隔），在「事件与回调」页面添加

#### 4. 发布

版本管理与发布 → 创建版本 → 填写版本号 → 设置可用性为「仅应用创建者」→ 提交审核。

### Sealseek 侧配置

填入飞书 App ID 和 App Secret，配置飞书通道。

**⚠️ 关键：配置完凭证后必须重启 Gateway。** 不重启时机器人只会 echo（你说什么它回什么），这不是 AI 回复，而是飞书的基础 echo 行为。重启后 Sealseek 才会接管消息处理。

## 应用身份 vs 用户身份

| | 应用身份 (tenant_access_token) | 用户身份 (user_access_token) |
|---|---|---|
| 谁在操作 | 机器人自己 | 某个具体用户 |
| 需要用户授权 | 否 | 是 |
| 数据范围 | 机器人能访问的数据 | 该用户能访问的数据 |
| 典型场景 | 收发消息、机器人创建文档 | 读用户日历、邮件 |

**Sealseek/Sealseek 全部选应用身份**，因为机器人收发消息是以自身身份进行。

## 控制同事可见性

飞书机器人能被谁搜索到，不是权限控制，而是**可用性范围**控制。

在「版本管理与发布 → 创建版本」中，将可用性设为「仅应用创建者」，其他同事就无法搜索到该机器人。

但创建者仍可手动将机器人添加到群聊中。

## 排障速查

| 现象 | 原因 | 解决 |
|------|------|------|
| 机器人 echo（你说啥它回啥） | Gateway 没重启 | 重启 Gateway |
| 机器人完全不回复 | 权限或事件未配 | 检查权限和 `im.message.receive_v1` 事件 |
| 群聊 @机器人 不回复 | 机器人未加入群 | 群设置 → 群机器人 → 添加 |
| 群聊 @机器人 不回复 | 缺少群聊权限 | 添加 `im:message.group_at_msg:readonly` |
| 发布后权限不生效 | 未创建版本发布 | 版本管理与发布 → 创建版本 |

## 相关记忆

- [[domains/AI Agent工程/03-Skill设计/00-Skill世界观|Skill 世界观]]
- [[domains/AI Agent工程/06-自动化工作流/index|自动化工作流]]
- 详细配置文档：`~/sealseek/飞书机器人权限配置指南/飞书机器人权限配置指南.md`