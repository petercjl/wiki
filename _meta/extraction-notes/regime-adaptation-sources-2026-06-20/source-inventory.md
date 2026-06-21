---
title: 市场状态识别与策略自适应资料包 source inventory
type: source-summary
created: 2026-06-20
updated: 2026-06-20
domain: meta
tags: [llm-wiki, quant-trading, research]
sources:
  - _meta/extraction-notes/regime-adaptation-sources-2026-06-20/source-profile.md
status: active
---

# Source Inventory

| source_id | source_path | type | source_units |
| --- | --- | --- | --- |
| github-sakeeb91 | `raw/github/regime-adaptation-sources-2026-06-20/repos/Sakeeb91-market-regime-detection/README.md` | GitHub README | HMM/GMM/change point detection, regime-conditioned trading, walk-forward validation, bull/bear/transition regimes. |
| github-lseg | `raw/github/regime-adaptation-sources-2026-06-20/repos/LSEG-market-regime-detection/README.md` and notebook | GitHub notebook | Statistical and ML regime detection: HMM, k-means, GMM; normal/crash states; out-of-sample strategy comparison. |
| github-regime-allocation | `raw/github/regime-adaptation-sources-2026-06-20/repos/regime-allocation-strategy/README.md` and `.py` | GitHub code | VIX-derived HMM volatility regimes; SPY/TLT/GLD allocation; execution lag; performance attribution; limitations. |
| github-dynamic-allocation | `raw/github/regime-adaptation-sources-2026-06-20/repos/regime-aware-dynamic-asset-allocation/README.md` | GitHub README | Multi-model dynamic allocation: HMM/GMM/KMeans, XGBoost, LSTM, walk-forward, regime-conditioned optimization, PPO prototype. |
| article-quantstart-intro | `raw/articles/quant-regime-adaptation-2026-06-20/quantstart-hmm-introduction.html` | article | Market regimes as shifts in means, variances, serial correlation, covariances; HMM as latent-state inference. |
| article-quantstart-qstrader | `raw/articles/quant-regime-adaptation-2026-06-20/quantstart-hmm-qstrader.html` | article | HMM as risk manager that disallows trades in high-volatility regimes; regime filter layered over an SMA crossover strategy. |
| article-quantinsti | `raw/articles/quant-regime-adaptation-2026-06-20/quantinsti-regime-adaptive-trading-python.html` | article | Adaptive trading with HMM, regime-specialized Random Forests, weak signal filtering, walk-forward testing. |
| article-lseg | `raw/articles/quant-regime-adaptation-2026-06-20/lseg-market-regime-detection.html` | article | Statistical/ML regime detection for S&P 500; HMM, k-means, GMM; investment strategy around predicted states. |
| article-questdb-ml | `raw/articles/quant-regime-adaptation-2026-06-20/questdb-market-regime-change-detection-ml.html` | glossary/article | Regime change detection features, ML methods, strategy adaptation, risk monitoring, implementation considerations. |
| article-questdb-hmm | `raw/articles/quant-regime-adaptation-2026-06-20/questdb-hmm-market-regime-detection.html` | glossary/article | HMM state transition/emission framework, common regimes, trading system applications and limitations. |
| article-robotwealth | `raw/articles/quant-regime-adaptation-2026-06-20/robotwealth-regime-split-models.html` | article | Regime-based split models; extreme-volatility regimes may be difficult to predict and may justify no-trade periods. |
| paper-jump-model | `raw/papers/quant-regime-adaptation-2026-06-20/downside-risk-reduction-regime-switching-signals-arxiv-2402.05272v2.html` | paper | Statistical Jump Model for downside risk reduction; persistence penalty; out-of-sample tests, costs, delays. |
| paper-hmm-nn | `raw/papers/quant-regime-adaptation-2026-06-20/integrating-hmm-neural-networks-arxiv-2407.19858v6.html` | paper | HMM + neural network alpha architecture, Black-Litterman portfolio optimization, drawdown/trailing-stop risk models. |
| paper-hmm-rl | `raw/papers/quant-regime-adaptation-2026-06-20/regime-based-portfolio-allocation-hmm-rl-arxiv-2605.27848-abs.html` | paper abstract | HMM + RL allocation across SPY/TLT/GLD; BIC state selection; 30% out-of-sample; one-day execution lag. |

