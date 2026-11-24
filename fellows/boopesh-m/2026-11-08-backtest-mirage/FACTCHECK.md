# FACTCHECK — The Backtest Mirage (Boopesh M., AI in finance)

Sources and how strongly each claim is backed:

- **[PAPER]** = David H. Bailey, Jonathan M. Borwein, Marcos López de Prado & Qiji Jim Zhu, "Pseudo-Mathematics and
  Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance", *Notices of the American
  Mathematical Society* 61(5), 458–471, May 2014, DOI 10.1090/noti1105.
  **⚠️ Not read directly.** From the build container `ams.org`, `carmamaths.org` (author copy), `scholarworks.wmich.edu`,
  `core.ac.uk` and `phys.org` were all unreachable (proxy 403 / host not allowed; tried 2026-11-08). Everything below
  about the paper comes from **WebSearch result summaries**: the WMU ScholarWorks record, the Newcastle (NOVA)
  repository record, ScienceDaily / EurekAlert / phys.org press coverage (April 2014), a CXO Advisory summary and a
  companion Bailey et al. paper on stock-portfolio design. One ScienceDaily reference lists the year as 2015 for the
  same volume/issue; the repository records and press coverage say 2014 (May 2014 issue), which the film uses.
- **[RUN]** = output of `code/backtest_mirage.py` in this folder (`code/results.json`, `code/curves.npz`,
  `code/run.log`), numpy 2.5.4, seed 42. **Synthetic noise data**, said on screen (B00 composer, B20, B30, B40, B50,
  B60 curve caption, B70 limits, outro) and in narration (B00, B20, B30 "on pure noise", B50 "noise markets", B70).
  Run twice (second run in a scratch folder): `results.json` identical apart from `runtime_s`, `run.log` identical,
  every array in `curves.npz` identical.
- **[MATH]** = arithmetic / standard statistics checked below.

No quotation from the paper is used anywhere. The paper's title appears on screen as a title (B60), not as a quote.
"Backtest overfitting" is shown in quotation marks as the name of the effect.

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | best backtest Sharpe 1.69 → on new data −0.37 | [RUN] main world winner: in-sample 1.687, out-of-sample −0.369 | ✅ |
| B00 | "the market: synthetic noise data, so no real edge exists" | [RUN] by construction: returns iid N(0, 1 %); a rule uses only past returns, so E[position_t · r_t] = E[position_t]·E[r_t] = 0 | ✅ |
| B10 | "your best backtest isn't skill, it's just the luckiest draw" | the film's thesis, shown by B30–B70 on noise data | editorial (backed by [RUN]) |
| B20 | seven years of daily returns; first 5 years (1,260 days) searched, last 2 (504 days) locked | [RUN] 252 trading days/year | ✅ |
| B20 | "no rule can have a real edge" | [RUN] construction (see B00) | ✅ |
| B30 | 10,000 simple rules; each looks at the last 2–20 days and goes long or short | [RUN] position = sign(Σ wᵢ r₍t−i₎), random weights, lookback 2–20 | ✅ |
| B30 | Sharpe ratio = return per unit of risk | standard definition; [RUN] mean / sd of daily P&L × √252 | ✅ |
| B30 | "above one is usually called good" | common practitioner rule of thumb, not from the paper | opinion / convention |
| B30 | most rules land near zero | [RUN] main world: in-sample Sharpe mean −0.005, sd 0.52 | ✅ |
| B30 | the best of 10,000 scores "one point seven" (1.69 on screen) | [RUN] 1.687 | ✅ (rounded) |
| B40 | the winner's line climbs for five years, "stalls, then slips" | [RUN] winner P&L sum +129.7 % in-sample; out-of-sample it rises for about a year, then falls, ending at −12.3 % for the two years (seen on the chart) | ✅ |
| B40 | out-of-sample Sharpe "minus point four" (−0.37 on screen) | [RUN] −0.369 | ✅ (rounded) |
| B50 | repeated on 200 fresh noise markets | [RUN] 200 worlds, seeds spawned from 42 | ✅ |
| B50 | best of 1: near zero; of 10: 0.7; of 100: 1.1; of 10,000: 1.6 (1,000: 1.34 on screen only) | [RUN] medians −0.075 / 0.689 / 1.055 / 1.337 / 1.575 | ✅ (rounded) |
| B50 | "out of sample, the winners averaged about zero" (10,000: −0.02 on screen) | [RUN] winner out-of-sample mean −0.022 ± 0.052 (s.e.) at N = 10,000; below zero in 52 % of worlds. Across all N tried the means range −0.089 … +0.137 (s.e. ≈ 0.05 each; the N = 100 value is 2.7 s.e. above zero, read as chance — the true value is exactly 0 by construction) | ✅ with the caveat noted |
| B60 | Sharpe noise ≈ 1/√years; 1/√5 ≈ 0.45 | [MATH] large-sample standard error of an annualised Sharpe ratio for iid returns is ≈ √((1 + SR²/2)/years) ≈ 1/√years near SR = 0; 1/√5 = 0.447. [RUN] measured spread across rules, averaged over 200 worlds: 0.443 | ✅ |
| B60 | best of 10,000 = 1.69 = 3.8 noise-widths up | [MATH] 1.687 / 0.447 = 3.77 | ✅ |
| B60 | authors, title, Notices of the AMS 61(5), 2014 | [PAPER] via search results | ⚠️ not read directly |
| B60 | they called this "backtest overfitting" | [PAPER] search summaries paraphrase the paper as: high simulated performance is easily achievable after backtesting a relatively small number of alternative strategy configurations, a practice the authors call backtest overfitting (paraphrase from summaries, not a verified quote, not shown as a quote) | ⚠️ |
| B60 | their warning: with 5 years of data, about 45 tries can reach a Sharpe near 1 by luck | [PAPER] secondary summaries (ScienceDaily/press, CXO Advisory, companion paper): with five years of data, testing more than ~45 independent configurations is almost guaranteed to give an in-sample annualised Sharpe of 1 with an expected out-of-sample Sharpe of 0. [MATH/RUN] independent-trials check: E[max of 45 standard normals] / √5 = 0.987; my rule search (correlated rules) gives a median best-of-45 of 0.91 | ⚠️ paper wording unverified; the number is reproduced by my own calculation ✅ |
| B70 | count trials and report them; hold out data; demand more as you test more | fix from the brief; the "report the number of trials" point matches the paper as summarised in search results | ⚠️ (paper link) / editorial |
| B70 | one rule beats 0.8 by luck only one time in twenty | [RUN] 95th percentile of the single-rule Sharpe over 200 worlds: 0.78 (independent-trials theory 0.74) | ✅ |
| B70 | with 10,000 rules the bar is 1.9, so the 1.7 winner fails | [RUN] 95th percentile of the best-of-10,000 over 200 worlds: 1.91 (theory for independent trials 1.97); winner 1.687 < 1.91 | ✅ |
| B70 | limits: synthetic noise, no trading costs, real markets may hide small real edges | honest limits of [RUN] | opinion, labelled as a limit |
| B80 | prompt: add a small real edge + trading costs; does the search find it? | not answered in the film | — |
| framing | "an AI that searches thousands of trading strategies" | the experiment's search is a simple random-rule search, not a trained model; it stands in for any automated strategy search | editorial framing |

## Arithmetic checks
- 5 × 252 = 1,260 in-sample days; 2 × 252 = 504 out-of-sample days.
- 1/√5 = 0.4472; 1.687 / 0.4472 = 3.77 → "3.8 noise-widths".
- Expected best of N independent zero-edge Sharpe ratios over 5 years (theory, [RUN]): N=10 0.69, 45 0.99, 100 1.12,
  1,000 1.45, 10,000 1.72. The rule search sits slightly below (0.69, 0.91, 1.06, 1.34, 1.58) because its rules are
  correlated (they all trade the same noise series), so 10,000 rules are worth fewer than 10,000 independent tries.

## Experiment details (all [RUN])
Daily returns iid N(0, 0.01), 20 warm-up days + 1,260 + 504. Rule k: lookback L ~ U{2,…,20}, weights w ~ N(0,1) on
the last L returns, position = sign(Σ wᵢ r₍t−i₎) ∈ {−1, +1}, P&L = position · r_t; no trading costs. Sharpe = mean/sd
(ddof 1) × √252, in-sample and out-of-sample separately. Main world: 10,000 rules; correlation between in-sample and
out-of-sample Sharpe across rules +0.12 (one world; the average over 200 worlds is +0.03, 5–95 % −0.27…+0.34 — a
shared-noise-path effect, not an edge). 200 extra worlds: the same search, new noise and new rules each time.
