---
title: GitHub 量化理论资料 source inventory
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, source-inventory, quant-trading]
sources:
  - raw/github/quant-theory-github-sources-2026-06-20/
status: active
---

# Source Inventory

| id | raw file | meaningful units |
| --- | --- | --- |
| S1 | `alphalens-README.rst` | 因子 tear sheet、returns analysis、information coefficient、turnover、grouped analysis、factor/pricing data cleaning workflow. |
| S2 | `pyfolio-README.md` | portfolio performance/risk analysis、tear sheet、Zipline 组合回测分析入口。 |
| S3 | `qlib-README.md` | qrun 自动化研究工作流、dataset/model/backtest/evaluation、with-cost 与 without-cost 结果区分、IC 分析。 |
| S4 | `qlib-benchmarks-README.md` | alpha 通过未来收益相关性与组合构建收益两层评估。 |
| S5 | `pyportfolioopt-README.md` | 均值方差、Black-Litterman、风险模型、协方差估计误差、约束、HRP、样本外零权重风险。 |
| S6 | `ml4t-backtest-README.md` | 事件驱动回测、point-in-time correctness、无前视偏差、真实执行、止损止盈、组合约束、回测限制。 |
| S7 | `purged-cross-validation-README.md` | purge/embargo、walk-forward、CPCV、PBO、DSR、时间序列泄漏与选择偏差控制。 |

## Source Unit Groups

- G1 Alpha/signals: S1, S3, S4.
- G2 Performance/risk: S2, S3.
- G3 Portfolio construction: S5.
- G4 Backtest realism/execution: S6.
- G5 Overfit/leakage control: S6, S7.

