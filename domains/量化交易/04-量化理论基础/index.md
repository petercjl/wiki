---
title: 量化理论基础
type: concept
created: 2026-06-20
updated: 2026-06-20
domain: 量化交易
tags: [quant-trading, research-method, foundations]
sources:
  - raw/github/quant-foundations-github-sources-2026-06-20/
  - raw/github/regime-adaptation-sources-2026-06-20/
  - raw/articles/quant-regime-adaptation-2026-06-20/
  - raw/papers/quant-regime-adaptation-2026-06-20/
  - _meta/extraction-notes/quant-foundations-github-sources-2026-06-20/coverage-matrix.md
  - _meta/extraction-notes/regime-adaptation-sources-2026-06-20/coverage-matrix.md
status: active
---

# 量化理论基础

本目录不是某个 ETF 策略的说明书，而是量化交易的基础知识骨架。它回答的是：一个量化研究者在写任何策略之前，应该如何理解市场、数据、信号、组合、交易、回测、风险和实验纪律。

量化交易的本质不是“用代码炒股”，而是把一个可检验的市场假设变成可重复执行的交易系统。一个完整系统至少包含：可交易资产、数据口径、收益假设、信号构造、组合权重、订单执行、成本模型、风险控制、回测验证、样本外检验和持续监控。

## 阅读顺序

1. [[domains/量化交易/04-量化理论基础/01-量化交易全景与研究对象|量化交易全景与研究对象]]
2. [[domains/量化交易/04-量化理论基础/02-市场、资产与交易制度|市场、资产与交易制度]]
3. [[domains/量化交易/04-量化理论基础/03-数据体系与特征工程|数据体系与特征工程]]
4. [[domains/量化交易/04-量化理论基础/04-收益、风险与统计基础|收益、风险与统计基础]]
5. [[domains/量化交易/04-量化理论基础/05-策略类型与收益假设|策略类型与收益假设]]
6. [[domains/量化交易/04-量化理论基础/06-因子、信号与Alpha研究|因子、信号与 Alpha 研究]]
7. [[domains/量化交易/04-量化理论基础/07-组合构建与仓位管理|组合构建与仓位管理]]
8. [[domains/量化交易/04-量化理论基础/08-交易执行、成本与市场冲击|交易执行、成本与市场冲击]]
9. [[domains/量化交易/04-量化理论基础/09-回测系统与真实性检查|回测系统与真实性检查]]
10. [[domains/量化交易/04-量化理论基础/10-绩效评估、归因与报告|绩效评估、归因与报告]]
11. [[domains/量化交易/04-量化理论基础/11-过拟合、数据泄漏与样本外验证|过拟合、数据泄漏与样本外验证]]
12. [[domains/量化交易/04-量化理论基础/12-量化研究工作流与实验纪律|量化研究工作流与实验纪律]]
13. [[domains/量化交易/04-量化理论基础/13-市场状态识别与策略失效|市场状态识别与策略失效]]
14. [[domains/量化交易/04-量化理论基础/14-状态自适应策略与动态资产配置|状态自适应策略与动态资产配置]]
15. [[domains/量化交易/04-量化理论基础/15-策略失效监控与滚动验证|策略失效监控与滚动验证]]

## 基础框架

```mermaid
flowchart LR
  A["市场与资产"] --> B["数据与特征"]
  B --> C["假设与信号"]
  C --> D["组合与仓位"]
  D --> E["订单执行"]
  E --> F["回测与评估"]
  F --> G["样本外验证"]
  G --> H["实盘监控"]
  H --> B
```

量化研究中最重要的不是某个指标，而是这条链路是否闭合。任何一个环节不严谨，都会让最终收益失真：

- 数据口径错，信号会变成未来函数。
- 信号没有经济含义，回测会变成参数搜索。
- 组合构建忽略相关性，分散持仓也可能实际押同一风险。
- 交易成本和市场冲击忽略，净值曲线会比真实交易乐观。
- 样本外验证缺失，策略可能只是记住了历史。

## 与 ETF 研究的关系

ETF 轮动只是量化策略类型之一。它会用到本目录中的若干通用知识：资产池构建、动量/反转信号、组合集中度、调仓频率、交易成本、回测偏差和样本外验证。后续研究 ETF 策略时，应先读本目录，再回到具体策略案例。

## 主要来源

本目录吸收并归档了多个 GitHub 开源量化项目：

- Zipline / Backtrader / bt：回测框架与事件驱动交易系统。
- Alphalens / Qlib / Machine Learning for Trading：因子、机器学习与量化研究流程。
- Pyfolio / Empyrical / ffn：绩效与风险指标。
- PyPortfolioOpt / Riskfolio-Lib：组合优化、风险预算与约束。
- purged-cross-validation：时间序列验证、数据泄漏与选择偏差治理。
- Market regime/adaptive allocation sources：HMM、GMM、KMeans、Jump Model、状态过滤、动态资产配置和 walk-forward 状态策略验证。

完整仓库已下载到 `raw/github/quant-foundations-github-sources-2026-06-20/repos/`。
市场状态与自适应策略资料已下载到 `raw/github/regime-adaptation-sources-2026-06-20/`、`raw/articles/quant-regime-adaptation-2026-06-20/` 和 `raw/papers/quant-regime-adaptation-2026-06-20/`。

## 相关记忆

- [[domains/量化交易/00-股票量化知识地图|股票量化知识地图]]
- [[domains/量化交易/01-聚宽/index|聚宽 JoinQuant]]
- [[domains/量化交易/02-策略风控与资金管理/01-凯利公式与量化仓位管理|凯利公式与量化仓位管理]]
- [[domains/量化交易/03-策略案例/index|量化策略案例库]]
