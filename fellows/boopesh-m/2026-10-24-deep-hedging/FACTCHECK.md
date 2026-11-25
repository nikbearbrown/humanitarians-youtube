# FACTCHECK — Hedging When Trading Isn't Free (Boopesh M., Deep Hedging)

Paper: H. Buehler, L. Gonon, J. Teichmann, B. Wood, "Deep Hedging", *Quantitative Finance* 19(8):1271–1291,
2019, DOI 10.1080/14697688.2019.1571683, arXiv:1802.03042. arXiv / publisher pages were **blocked** in the build
container, so the paper PDF itself was **not read**. Sources actually used, and how strongly each claim is backed:

- **[README]** = verified from the first author's public code README,
  `raw.githubusercontent.com/hansbuehler/deephedging/main/README.md` (fetched 2026-10-24).
- **[ABSTRACT*]** = paraphrased from search-result summaries of the published abstract (not verbatim, not
  read from the paper). Treat as needing a human check against the PDF.
- **[RUN]** = output of `code/deep_hedge.py` in this folder (`code/results.json`, `code/arrays.npz`, `code/run.log`).
- **[MATH]** = standard result, algebra checked below.

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | Title, authors, 2019, *Quantitative Finance* | citation supplied in brief (DOI/arXiv id) | ⚠️ not opened (blocked) |
| B00 | J.P. Morgan + ETH Zurich | [ABSTRACT*] / brief | ⚠️ needs human check |
| B40 | Objective: maximise a utility of payoff + hedge gains − proportional costs | [README] `sup_a U[Z_T + Σ a(s_t)·DH_t … γ_t·|a(s_t)H_t|]`; README prints the cost term with "+", but its own output definition is `gains = payoff + pnl − cost` (cost subtracted) — film shows the cost subtracted | ✅ (README typo noted) |
| B40 | Entropic utility U(X) = −(1/λ) log E[exp(−λX)], "from Buehler's own code" | [README] "A classic example is the entropy … The code base supports a number of utility-based monetary utilities" | ✅ |
| B40 | Network decides the position each day from state features | [README] `a(s_t)` "action given state s_t"; recurrent agents | ✅ |
| B40 | "The paper allows convex risk measures" — not spoken; only on screen implicitly | [ABSTRACT*] | ⚠️ |
| B70 | Paper goes further: S&P 500 data and Heston model | [ABSTRACT*] | ⚠️ needs human check |
| B70 | "only as good as the simulator" | editorial judgement (the policy is trained on simulated paths) | opinion, labelled as a limit |
| B20 | Δ = N(d₁), d₁ = (ln(S/K) + ½σ²τ)/(σ√τ), r = 0 | [MATH] | ✅ |
| B30 | 0.5% fee; daily BS hedge trades 2.23 shares/option, pays $1.11 fees; option price $2.75; ≈40% | [RUN] turnover_bs 2.229, mean_cost 1.1139, premium_bs 2.7524 → 40.5% | ✅ |
| B50 | 40,000 fresh test paths (different seed from 40,000 training paths) | [RUN] setup | ✅ |
| B50 | Average P&L: BS −$1.11, deep −$0.65 | [RUN] −1.1125 / −0.6456 | ✅ |
| B50 | Spread wider for deep (std $0.57 → $0.75) | [RUN] 0.5653 / 0.7478 | ✅ (stated honestly) |
| B50 | Worst 5% (CVaR 5%) improves: −$2.56 → −$2.14 | [RUN] −2.5597 / −2.1359 | ✅ |
| B50 | "Risk score it was trained to maximise" (entropic utility) improves −1.31 → −0.92 (shown in table) | [RUN] −1.3059 / −0.9201 | ✅ |
| B60 | Deep trades 1.30 shares vs 2.23; fees $0.65 vs $1.11 | [RUN] 1.298 / 2.229; 0.6488 / 1.1139 | ✅ |
| B60 | On the shown path (test index 3) the deep hedge "moves more smoothly, skips small back-and-forth" | [RUN] arrays `gamma_0.005_path_*` — visible in chart. Earlier draft said "holds still"; the path does not show that, so the line was changed. | ✅ |
| B70 | γ = 0: average |deep − BS| position gap 0.024 shares; utility −0.127 (deep) vs −0.096 (BS) — "close, slightly worse" | [RUN] 0.0238; −0.1273 / −0.0961 | ✅ |
| B70 | No-hedge for reference (not spoken): std $4.21, entropic −21.4 | [RUN] | ✅ |

## Algebra / numerical checks
- Black–Scholes call with r = 0: C = S N(d₁) − K N(d₂), d₂ = d₁ − σ√τ, and ∂C/∂S = N(d₁). Numerical case:
  S = K = 100, σ = 0.2, τ = 30/252 → σ√τ = 0.06901, d₁ = 0.03450, N(d₁) = 0.5138, C = 2.752 — matches
  `premium_bs` = 2.7524 printed by the script, and the first-day BS trade 0.51 shares shown in B30.
- Objective (shown on screen in plain words as "score = option money + hedge gains − fees"; formula kept here): max over δ of U(Z_T + Σ δ_t ΔS_t − γ Σ S_t |δ_t − δ_{t−1}|), Z_T = p₀ − (S_T − K)⁺,
  δ_{−1} = 0, S_t = price at the trade. This is exactly `pnl()` in `code/deep_hedge.py` (no liquidation cost at expiry).
- Entropic utility: the script uses the log-sum-exp form −(1/λ)(logsumexp(−λX) − log n) = −(1/λ) log mean exp(−λX). λ = 1.
- Implementation check: the hand-written backprop-through-time gradient matches central finite differences,
  worst relative error 3.8e-7 (`python code/deep_hedge.py --gradcheck`; also asserted at the start of every run).

## Replication details (all [RUN])
Black–Scholes world, S₀ = 100, σ = 20 %, r = 0, 30 daily steps, short one ATM call at its BS price;
MLP 3-32-32-1 (SiLU), inputs (time left, log S/K, previous position), output squashed to [−0.1, 1.1];
Adam lr 3e-3, 60 epochs × 20 batches of 2,000; seed 7; numpy (PyTorch could not be installed in time —
`code/deep_hedge_torch_reference.py` is the original PyTorch draft, NOT run). Runtime ≈ 6.5 min on 2 CPU threads.
