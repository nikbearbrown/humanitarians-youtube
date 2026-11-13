# FACTCHECK — Mycroft Phase 5 (9:16)

Every number and claim in the film, with its source.

**Source of truth:** `source/Mycroft_Phase5_Thesis_Resilience.ipynb` and its executed output, saved
verbatim as `docs/NOTEBOOK-OUTPUT.txt`. Both figures were extracted from that notebook's own
display data — not redrawn.

**Nothing was recomputed.** The notebook was not re-run and `Stock_Prices_Dataset.csv` is not in
this package. Every figure below is quoted from the author's executed run.

## Data

| # | Claim | Value | Source | Status |
|---|---|---|---|---|
| F1 | Rows | 184,138 | stdout line 1 | verbatim ✅ |
| F2 | Tickers | 120 | stdout line 1 | verbatim ✅ |
| F3 | Date range | 2020-01-03 → 2026-02-11 | stdout line 1 | verbatim ✅ |
| F4 | Required columns | Date, Ticker, Company_Name, Sector, Industry, Open, High, Low, Close, Adj_Close, Volume | `load_data()` | code ✅ |
| F5 | Engineered features shown on screen | returns 1/5/10/20/60d · close_to_sma 5/10/20/50 · volatility 5/10/20/60d · volume_ratio_20d · volume_zscore_20d · overnight_gap · intraday_range · rsi_14 · drawdown_60d · sector_relative_return_20d · market_relative_return_1d | `engineer_features()` | code ✅ |

## Thesis health score

| # | Claim | Value | Source | Status |
|---|---|---|---|---|
| F6 | Score range | 0–100 | `100 * np.average(...)` over percentile ranks | code ✅ |
| F7 | Ranks are cross-sectional per date | `groupby("Date")[col].rank(pct=True)` | code | ✅ — this is why a score is comparable across time |
| F8 | Weights | return_20d .20 · sector_relative_return_20d .18 · close_to_sma_50 .16 · drawdown_60d .15 · volatility_20d .13 · rsi_health .10 · volume_zscore_20d .08 | `weights` array against `score_columns` order | verbatim ✅ (sums to 1.00) |
| F9 | volatility is inverted (lower is better) | `rank_specs["volatility_20d"] = False` → `1 - pct` | code ✅ |
| F10 | RSI health peaks near 57.5 | `1 - (rsi_14 - 57.5).abs().clip(upper=42.5) / 42.5` | code ✅ |
| F11 | States | broken < 35 · weakening 35–50 · stable 50–65 · strong > 65 | `pd.cut(bins=[-inf,35,50,65,inf])` | verbatim ✅ |
| F12 | Deterioration tracked at 5 and 20 days, plus a state drop vs 20 days ago | `diff(5)`, `diff(20)`, `shift(20)` | code ✅ |

## Contradiction detection

| # | Claim | Source | Status |
|---|---|---|---|
| F13 | Flag fires on: health_change_20d ≤ −20, **or** state deterioration while sector-relative return < 0, **or** close_to_sma_50 < −0.08 **and** drawdown_60d < −0.15 | `contradiction_flag` | verbatim ✅ |
| F14 | Reason strings shown on screen | `thesis_health_fell_20_plus_points`, `underperforming_sector`, `more_than_8pct_below_sma50`, `drawdown_over_15pct`, `high_volatility` | `contradiction_reasons()` | verbatim ✅ |

## Stress testing

| # | Claim | Value | Source | Status |
|---|---|---|---|---|
| F15 | Simulations | 3,000 | `simulations=3000` | verbatim ✅ |
| F16 | Horizon | 20 days | `horizon=20` | verbatim ✅ |
| F17 | Lookback | 252 days | `lookback=252` | code ✅ |
| F18 | Volatility multiplier | ×1.8 | `volatility_multiplier=1.8` | verbatim ✅ |
| F19 | Day-1 market shock | −8% | `market_shock=-0.08`, applied as `m[:,0] += market_shock` | verbatim ✅ |
| F20 | Beta is to the **equal-weighted dataset market**, not an external index | `market = recent.mean(axis=1)` | code | ✅ — the film says "dataset market" |
| F21 | Idiosyncratic component separated before bootstrapping | `idio = r - beta * aligned_market` | code ✅ |
| F22 | VaR 95% / CVaR 95% definitions | `var95 = quantile(terminal, .05)`; `cvar95 = terminal[terminal <= var95].mean()` | code | ✅ — matches the on-screen wording |
| F23 | ORCL stress VaR 95% | −0.4609 → shown as **−46.1%** | queue output | verbatim ✅ |
| F24 | ORCL stress CVaR 95% | −0.5165 → shown as **−51.7%** | queue output | verbatim ✅ |

**Note on the S10 histogram:** the distribution *shape* is schematic, drawn to explain where VaR
and CVaR sit. The notebook does not output a loss histogram. The source line on that scene says
so, and only the two marked values are real.

## Resilience and review priority

| # | Claim | Source | Status |
|---|---|---|---|
| F25 | resilience_score = thesis_health×.55 + (1−prob_loss_20d)×100×.20 + (1−prob_loss_over_20pct)×100×.15 + rank_volatility_20d×100×.10 | code | verbatim ✅ |
| F26 | Bands: fragile < 40 · watch 40–55 · resilient 55–70 · high_resilience > 70 | `pd.cut(bins=[-inf,40,55,70,inf])` | verbatim ✅ |
| F27 | review_priority = contradiction×3 + (fragile or watch)×2 + (health_change_20d ≤ −15)×2 + (prob_loss_over_20pct ≥ .20)×2 | code | verbatim ✅ (max 9) |
| F28 | 17 names reached priority 9 on 2026-02-11 | counted from the printed queue: ORCL, UNH, SPGI, EL, AMZN, ELV, LLY, AMD, TMO, DIS, ISRG, DHR, INTC, BA, EMR, TGT, FCX | derived from the printed top-20 ✅ |
| F29 | Queue rows shown (ORCL 10.9/20.8, UNH 8.4/21.2, SPGI 9.9/22.2, EL 19.2/27.6, AMZN 18.9/29.7, all priority 9) | queue output, rounded to 1 dp on screen | verbatim ✅ |
| F30 | Queue sorted by priority desc, then resilience asc | `sort_values([...], ascending=[False,True])` | code ✅ |

## The honest diagnostic

| # | Claim | Value | Source | Status |
|---|---|---|---|---|
| F31 | Large move = \|5-day forward return\| ≥ 5% | `large_abs_move` | code ✅ |
| F32 | Flagged rows: n = 62,831, large-move rate **0.2194** | evaluation table | verbatim ✅ |
| F33 | Unflagged rows: n = 120,707, large-move rate **0.1914** | evaluation table | verbatim ✅ |
| F34 | "The flag fires on about a third of all rows" | 62,831 / 183,538 = 34.2% | arithmetic on F32 + F33 | ✅ |
| F35 | Labelled "a diagnostic, not a forecast" | the notebook itself prints "Historical diagnostic (not a forecast)" | ✅ **must stay on screen** |

The difference is **2.8 percentage points** on a base of 19%. The film calls it "a real
difference, but small" and shows both bars side by side. It must never be presented as predictive
skill.

## Advisory and scope

| # | Item | Status |
|---|---|---|
| A1 | "Research decision support. Not financial advice and not an autonomous trading system." | On S12, on the S14 card, and in the S01 source line ✅ |
| A2 | "Thesis" means a **quantitative** research thesis built from OHLCV data, not a fundamental analyst thesis | Stated in the notebook comment; the film says "quantitative thesis" throughout ✅ |
| A3 | Ticker symbols and company names are public identifiers used as research examples | No personal data anywhere in the package ✅ |
| A4 | No claim of profitability, investment performance or prediction accuracy | Audited — none present ✅ |

## Open items — work in progress, not achievements

| # | Item | Why |
|---|---|---|
| W1 | The contradiction flag is broad — about a third of all rows | Useful as a screen, weak as a signal; F34 |
| W2 | Stress test uses a fixed −8% shock and ×1.8 volatility | One scenario, chosen by hand; not a calibrated scenario set |
| W3 | Beta is to the equal-weighted dataset market | Not a true market index; sensitive to the 120-name universe |
| W4 | `thesis_health` weights are hand-set | Not fitted or validated against an objective |
| W5 | The diagnostic is in-sample over the whole history | No train/test separation for the flag itself |

## Gate before publication

| Gate | Status |
|---|---|
| Re-run the notebook and confirm F1–F35 on the publish date | ⏳ |
| Confirm the ticker examples are still appropriate to show | ⏳ |
| Narration read aloud against the animatic | ⏳ |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
