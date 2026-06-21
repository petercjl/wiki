---
title: GitHub 量化基础资料源地图
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, quant-trading, github-source]
sources:
  - raw/github/quant-foundations-github-sources-2026-06-20/
status: active
---

# GitHub 量化基础资料源地图

本目录归档 2026-06-20 从 GitHub 下载的量化基础资料。与上一版只围绕 ETF 策略不同，本批资料覆盖完整量化交易基础：市场资产、数据、因子、组合、执行、回测、绩效、过拟合和研究工作流。

## 项目仓库

完整仓库均以浅克隆方式归档在 `repos/`：

| 项目 | GitHub URL | 本地路径 | 知识用途 |
| --- | --- | --- | --- |
| Zipline | https://github.com/quantopian/zipline | `repos/zipline/` | 事件驱动回测、算法交易系统。 |
| Backtrader | https://github.com/mementum/backtrader | `repos/backtrader/` | broker simulation、订单类型、佣金、滑点、交易日历。 |
| bt | https://github.com/pmorissette/bt | `repos/bt/` | 策略逻辑块、组合回测。 |
| Alphalens | https://github.com/quantopian/alphalens | `repos/alphalens/` | 因子收益、IC、换手、分组分析。 |
| Pyfolio | https://github.com/quantopian/pyfolio | `repos/pyfolio/` | 组合绩效与风险 tear sheet。 |
| Empyrical | https://github.com/quantopian/empyrical | `repos/empyrical/` | 金融风险与绩效指标。 |
| ffn | https://github.com/pmorissette/ffn | `repos/ffn/` | 金融函数、绩效统计与数据处理。 |
| PyPortfolioOpt | https://github.com/PyPortfolio/PyPortfolioOpt | `repos/pyportfolioopt/` | 均值方差、Black-Litterman、收缩估计、HRP。 |
| Riskfolio-Lib | https://github.com/dcajasn/Riskfolio-Lib | `repos/riskfolio-lib/` | 多风险度量、风险预算、约束优化。 |
| Qlib | https://github.com/microsoft/qlib | `repos/qlib/` | 数据、模型、回测、组合、执行的量化工作流。 |
| Machine Learning for Trading | https://github.com/stefan-jansen/machine-learning-for-trading | `repos/machine-learning-for-trading/` | 从数据来源到实盘执行的 ML 量化流程。 |
| purged-cross-validation | https://github.com/eslazarev/purged-cross-validation | `repos/purged-cross-validation/` | purge、embargo、walk-forward、PBO/DSR。 |

## 正式知识定位

这些仓库不是作为工具安装手册入库，而是作为量化基础知识的 evidence layer：

- 回测框架告诉我们一个真实回测系统应模拟什么。
- 因子分析工具告诉我们信号应如何先于策略验证。
- 绩效工具告诉我们回测报告不能只看收益。
- 组合优化工具告诉我们权重和风险约束的重要性。
- 交叉验证工具告诉我们时间序列不能随机切分。

