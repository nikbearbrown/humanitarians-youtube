# SOURCES — Financial Engineering with LLMs: The Mycroft Textbook Companion

**Source file:** `188220135.financial-engineering-with-llms-mycroft.html`  
**Publication:** Humanitarians-AI  
**Author:** Nik Bear Brown — Founder, Humanitarians AI  

## Statistics cited on-screen (all trace to this article, none invented)

- Logical Method: Arbitrage construction: borrow GBP1 @ 6.25%, convert to FFr9.52, invest @ 5.25%, required forward = FFr9.7699/GBP1.03125 = 9.4738—market deviations enable riskless profit; ERA vs FXA comparison shows equivalent settlement despite different fixing mechanisms.
- Logical Gaps: “Seesawing” convergence (odd steps underpriced, even overpriced) described but not explained mathematically; trinomial optimal λ cited as “often 3” without justification; control variate shows 11.5 vs 11.1 (3.6% error) without standard error or convergence analysis; bootstrap method mentioned but never demonstrated.
- Logical Method: Bootstrapping iteratively solves for spots: 6-month par 6.25% → spot 6.250%, 12-month par 6.50% → spot 6.504%; interest rate tree construction via three conditions (variance relationship, symmetry, forward rate consistency); OAS Goal Seek finds spread forcing calculated price = market price.
- Core Claim: Convertible bonds = corporate bond + long call on equity; delta-adjusted discount rates (Phillips method: r* = Δ·r_rf + (1-Δ)·r_credit) improve accuracy over constant spreads; bond floor unstable to yield changes (7% YTM: £90.15; 11.5% YTM: £79.93).
- Logical Gaps: Method 1 shows £435K shortfall with vague mitigation (”reduce 5% to 3%”); Method 2 sign error (shows losses when index rises despite “buying contracts”); Method 3 participation level (25%) derived without formula; basket assumes lognormal approximation despite components being non-lognormal combination; correlation stability ignored despite “notoriously unstable” warning.
- Methodological Soundness: VaR definition precise; CVaR formula rigorous; historical simulation algorithm correct; Monte Carlo generation sound; Greeks Taylor series orthodox; duration-convexity standard; PCA decomposition correct; out-of-sample VaR test clean (4.989% breach vs 5% theoretical).
- Core Claim: Quantitative trading exploits marginal inefficiencies (51% biased coin) via law of large numbers; requires rigorous alpha research, realistic transaction costs (5-10bp stocks, 5% options), out-of-sample validation expecting Sharpe decay (½ to ÷2); signal types include momentum, mean-reversion, pairs trading, factor models.
- Dimensionality Reduction: Apply PCA to large feature sets, retain principal components explaining 95% variance

## Source file

`188220135.financial-engineering-with-llms-mycroft.html`

_Generated 2026-07-17 01:40_
