# FACTCHECK — How an AI Sells a Big Order (16:9 + Short)

Boopesh M. · 2026-11-22 · checked 2026-11-23

Every number in the film comes from `code/results.json`, written by `code/execution_rl.py`
(numpy only, seeds 20261122 train / 7 held-out). It was run twice and both outputs were
byte-identical (`code/determinism.txt`). `make_sheet.py` asserts each spoken number against
results.json before it writes the beat sheets. **The market is synthetic.** It is an
arithmetic random walk plus linear temporary impact, the linear model of Almgren & Chriss with
no permanent impact. It contains no real prices and no real order book.

## Sources

| Source | Status | What it supports |
|---|---|---|
| Almgren R., Chriss N., *Optimal Execution of Portfolio Transactions*, author version dated December 2000 (42 pp.), via the GitHub mirror `nosy0411/Optimal_Execution_Almgren_and_Chriss_Model` (PDF sha256 `49587f13…9d77`) | **Read** §Intro, §1.1–2.3 (eqs. 1–20) | price model, temporary impact, implementation shortfall, E + λV objective, closed-form trajectory (eq. 17) |
| Same paper, published *Journal of Risk* 3(2), 2000/2001 | ⚠️ The journal volume, issue and pages were seen only in search listings (risk.net, doi 10.21314/JOR.2001.041) | the year "2000" on screen follows the author version's date |
| Nevmyvaka Y., Feng Y., Kearns M., *Reinforcement Learning for Optimized Trade Execution*, ICML 2006 | ⚠️ **NOT READ.** The author page (cis.upenn.edu) and every mirror tried were blocked from this machine. The only GitHub "copy" found (luliu31415926/…) turned out to be an unrelated student report. Title, authors and venue come from search listings only (ACM DL 10.1145/1143844.1143929, UT Austin reading list, Waterloo CS885 slides) | the B70 "Read more" line, the narration and description.txt "see Nevmyvaka, Feng and Kearns, from 2006". **Nothing from it is quoted or paraphrased.** No result of theirs appears |

## Claims

| Beat | Claim (as spoken / shown) | Verdict | Evidence |
|---|---|---|---|
| B00 | "this is an AI voice reading my script" | ✓ | Kokoro `am_onyx`, metadata.voice_kokoro |
| B10/B20 | A huge order "walks the price down"; buyers at the best price only want so many | ✓ general; matches source | A&C §1.3: "the execution price may steadily decrease … due to exhausting the supply of liquidity at each successive price level" |
| B20 | "That's market impact" | ✓ | A&C §1.2: "We distinguish two kinds of market impact." Temporary impact is the one modelled here |
| B20 | Selling all 10,000 at $50 gets **$49.50** a share, costs **$5,000 = 100 bps**, 1% of the $500,000 order | ✓ code | results.json `strategies.dump`: mean_usd 5000.0, mean_bps 100.0, std 0 (ETA·X = 5e-5 × 10,000 = $0.50) |
| B30 | Ten equal slices: "impact falls about ten times" | ✓ code + algebra | twap mean 9.89 bps vs dump 100 (×10.1). Expected impact is 10.00 bps. Under linear impact, ΣηN(X/N)² = ηX²/N (A&C eqs. 10 and 13) |
| B30 | Holding longer lets the price wander; "on a bad day it drifts down while you wait" | ✓ code; matches source | random walk, σ = $0.10/step. Bad sample day (index 2 of 40 held-out days) costs 78.68 bps under TWAP. A&C intro: equal packets have "lower expected cost but … greater uncertainty" |
| B40 | Agent sees time left + shares left, picks a fraction to sell now (0%, 5% … 100%), score = cash received minus a small penalty on shares held | ✓ code | `train_q()`: state (k, lots left), 21 fractions. Reward = mark-to-market P&L − λσ²·held². Summed over a day this is −(shortfall + risk penalty) |
| B40 | "practiced forty million times on simulated days, keeping a table" | ✓ code, with a caveat | params.episodes 40,000,000 (4,000 × 10,000 batches). Tabular *double* Q-learning, off-policy, exploring starts. **Caveat:** each practice run starts at a random step and inventory, so many runs are only part of a day. The narration simplifies this to "practiced … on simulated days" |
| B50 | "sell more early, then taper off" | ✓ code | learned schedule 2500, 1500, 1000, 1000, 1000, 750, 750, 500, 500, 500 (non-increasing, asserted) |
| B50 | Dots = "the Almgren and Chriss formula from 2000", "the textbook answer for this exact model" | ✓ | A&C eq. 17 with γ = 0, ε = 0, τ = 1. It minimises E + λV for exactly this model. "Textbook" is a characterization |
| B50 | "The agent never saw that formula, and its bars land close to it" | ✓ code | the agent learns only from sampled rewards. Its max deviation from AC is 374 shares in one step, and its objective is 22.424 vs 22.053 bps (**+1.68%**). Exact optimum on the agent's own grid: 22.226 |
| B50 | on screen: "cost + risk, held-out days · agent 22.4 · formula 22.1 · within 1.7%" | ✓ code | objective_bps rl 22.424, ac 22.053. rl_objective_gap_vs_ac_pct 1.682 |
| B60 | 20,000 new simulated days | ✓ code | params.test_days, seed 7 (training used seed 20261122) |
| B60 | All at once 100 bps every time | ✓ code | dump std 0 |
| B60 | Equal slices "about ten on average", "one day in twenty costs sixty-five or more" | ✓ code | twap mean 9.89, p95 65.37 (by definition 5% of days ≥ p95) |
| B60 | Agent "pays a little more on average, about thirteen", "bad-day line drops to about fifty-four" | ✓ code | rl mean 13.31, p95 53.59, std 24.50 vs twap 33.70 |
| B70 | trade-off: fast → impact, slow → risk | ✓ | A&C intro (the two extreme strategies) |
| B70 | "this was a synthetic market. Real markets have order books, other traders who react, and sudden jumps" | ✓ general background | stated as a limitation. A&C themselves note serial correlation, scheduled news and "unanticipated events" outside their static model |
| B70 | "see Nevmyvaka, Feng and Kearns, from 2006"; on screen "Read more: Nevmyvaka et al. 2006 · Almgren & Chriss 2000" | ⚠️ bibliographic only (Nevmyvaka) | see Sources |
| Short B30 | "40M practice runs" | ✓ code | = 40,000,000 |

## Math (MATH-TYPESETTING.md)

On-screen formula, typeset by `code/make_formula.py` (toolkit `typeset_math.py`, MathText → SVG):
x_j = X · sinh κ(T − t_j) / sinh κT. Source: A&C eq. 17, with x_0 = X and x_N = 0.

- Domain: T = N = 10 steps > 0, τ = 1, t_j = j, j = 0…N; κ > 0.
- κ solves 2(cosh κτ − 1)/τ² = κ̃² = λσ²/η̃ with η̃ = η − γτ/2. With γ = 0, η̃ = η, so
  κ̃² = 3e-4 × 0.01 / 5e-5 = 0.06 and κ = 0.244341. Check: 2(cosh κ − 1) = 0.0600001 ✓.
- Numerical case: x_1 = 10,000 · sinh(0.244341 × 9)/sinh(0.244341 × 10) = 7,794.7, so the first
  sale is n_1 = 2,205.3. results.json `ac.n[0]` = 2205.3 ✓. Σn = 10,000.0 ✓.
- The dots on screen are n_j = x_{j−1} − x_j (shares sold per step). The formula gives holdings.
  B50 says so on screen ("formula: shares still held · dots: shares sold per step").
- Equation frames looked at in preview stills at 1920×1080 (B50) and 1080×1920 (Short B30).
  The fraction bar, subscripts and κ are legible.

## Honest notes on the simulation

- The first plain Q-learning attempts did **not** match the closed form. One had a bug: the forced
  last step's value was read from untrained actions. The other suffered optimistic max-bias from
  the noisy rewards, ending at objective gaps of +47% to +94%. Fixes: the forced-sale value
  bug, a mark-to-market reward, exploring starts, double Q-learning and 40M practice runs.
  A short scan tried σ ∈ {0.05, 0.07, 0.10} (with λ adjusted to keep κ fixed), 11 or 21
  actions, and 10M or 40M runs. I kept σ = 0.10 because it keeps the drift risk visible, and
  40M runs because that scan run ended closest to the formula. So the run length was chosen
  after seeing one outcome.
- During training the greedy schedule moves between 22.4 and 23.8 bps (objective), because the
  price noise is large. The film reports the **final** table, which is also the best checkpoint.
  Stopping at 36M runs would have given 22.8 bps (+3.4% vs AC). The headline "close to the formula"
  holds at every checkpoint after 6M (all within 8% of AC, all far below dump at 100 and below
  TWAP's 27.1).
- On average the agent costs more than TWAP (13.3 vs 9.9 bps). Its edge is lower risk (std 24.5 vs
  33.7, p95 53.6 vs 65.4). The narration says exactly that.
