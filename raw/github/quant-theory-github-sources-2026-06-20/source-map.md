---
title: GitHub 量化理论资料源地图
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, quant-trading, github-source]
sources:
  - raw/github/quant-theory-github-sources-2026-06-20/
status: active
---

# GitHub 量化理论资料源地图

本目录归档 2026-06-20 从 GitHub 收集的量化研究方法论资料，用于补充 [[domains/量化交易/index|量化交易知识域]] 的理论层。资料选择标准是：能帮助 Peter 判断 ETF 策略研究应该先验证什么、如何避免过拟合、如何解释收益来源，而不是只提供某个现成策略。

## 来源清单

| 源 | GitHub URL | 本地 raw | 主要用途 |
| --- | --- | --- | --- |
| Alphalens | https://github.com/quantopian/alphalens | `alphalens-README.rst` | 因子/信号分析：收益、IC、换手、分组分析。 |
| Pyfolio | https://github.com/quantopian/pyfolio | `pyfolio-README.md` | 组合绩效与风险分析：tear sheet 思路。 |
| Qlib | https://github.com/microsoft/qlib | `qlib-README.md` | 量化研究工作流：数据、模型、回测、评估。 |
| Qlib benchmarks | https://github.com/microsoft/qlib/blob/main/examples/benchmarks/README.md | `qlib-benchmarks-README.md` | Alpha 的两层评估：预测相关性与组合回测。 |
| PyPortfolioOpt | https://github.com/PyPortfolio/PyPortfolioOpt | `pyportfolioopt-README.md` | 组合优化、均值方差、Black-Litterman、HRP、估计误差风险。 |
| ml4t/backtest | https://github.com/ml4t/backtest | `ml4t-backtest-README.md` | 事件驱动回测、点时正确性、真实执行和风控约束。 |
| purged-cross-validation | https://github.com/eslazarev/purged-cross-validation | `purged-cross-validation-README.md` | 时间序列交叉验证、purge/embargo、walk-forward、DSR/PBO。 |

## 入库定位

这批来源不直接形成“可交易策略”，而是形成研究准则：

- 选池和信号要先被当作 alpha 候选验证，再进入完整买卖器。
- 回测收益要拆成选池、信号、组合、买卖器、执行成本、风险暴露几层。
- 参数搜索必须记录搜索空间和样本外规则，否则高收益容易只是选择偏差。
- 买卖器不是越复杂越好；它应解释资金利用率、换手、滑点、回撤控制之间的取舍。

