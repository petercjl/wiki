---
title: 聚宽策略 Agent 使用入口
type: query
created: 2026-06-19
updated: 2026-06-20
domain: 量化交易
tags: [joinquant, agent-template, quant-trading, strategy]
sources:
  - domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范.md
  - domains/量化交易/01-聚宽/02-聚宽API能力地图.md
  - domains/量化交易/01-聚宽/03-聚宽策略报错与排查.md
  - domains/量化交易/04-量化理论基础/index.md
status: active
---

# 聚宽策略 Agent 使用入口

## 什么时候读取

当用户要求：

- 写聚宽回测策略。
- 检查 JoinQuant/JQData 代码能否运行。
- 修复聚宽平台报错。
- 把普通 Python 量化逻辑改成聚宽策略。
- 研究、优化、比较或复盘聚宽量化策略。

## 读取顺序

1. [[domains/量化交易/01-聚宽/01-聚宽策略写作与回测兼容规范]]
2. [[domains/量化交易/01-聚宽/02-聚宽API能力地图]]
3. [[domains/量化交易/01-聚宽/03-聚宽策略报错与排查]]
4. 若任务是策略研究、策略优化、回测归因或防过拟合，先读 [[domains/量化交易/04-量化理论基础/index|量化理论基础]]；至少明确市场资产、数据口径、信号假设、组合/仓位、执行成本、回测真实性和样本外验证。
5. 需要具体签名时检索 `raw/api/joinquant/joinquant-api-2026-06-19.md`

## Codex Skill

优先触发本地 skill：

```text
/Users/pechen/.codex/skills/joinquant-strategy
```

写完策略必须运行：

```bash
python3 -m py_compile <strategy.py>
python3 /Users/pechen/.codex/skills/joinquant-strategy/scripts/check_joinquant_strategy.py <strategy.py>
```

## 默认策略交付标准

- 代码可复制到聚宽策略编辑器。
- 使用 `initialize(context)` 和全局调度函数。
- 启用真实价格和避免未来数据模式，除非用户明确要求关闭。
- 不依赖本地文件路径和未确认第三方库。
- 最终回复说明本地检查结果。
