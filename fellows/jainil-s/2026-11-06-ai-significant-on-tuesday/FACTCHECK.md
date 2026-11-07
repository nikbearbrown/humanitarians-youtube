# FACTCHECK — Significant On Tuesday

Week ending 2026-11-06 · `ai-` track.

Every figure spoken or shown comes from `peeking_evidence.py`, `beat_data.py`
or `power_tradeoff.py`, all three shipped in this folder. One seed
(`20261106`), one `numpy` Generator, no wall clock: re-run them and the numbers
reproduce exactly.

**The design, stated once.** 20,000 simulated A/B tests in which the two arms
are *identical by construction* — both convert at 10%, 2,000 visitors per arm,
a significance test every 100 visitors. Because there is no real difference,
every "winner" is a false positive and nothing has to be assumed about effect
sizes. This is an A/A test, and it is the only honest way to measure a
procedure's error rate.

---

## Verified — on screen or spoken

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Both arms convert at 10%; the true difference is exactly zero | ✅ | `peeking_evidence.py` `BASE_RATE`, both arms |
| 2 | 20,000 simulated experiments | ✅ | `N_SIM = 20_000` |
| 3 | 2,000 visitors per arm, a look every 100 → 20 looks | ✅ | `N_MAX`, `LOOK_EVERY`, `LOOKS` |
| 4 | One look at the end: **5.01%** false positives | ✅ | §1. Wilson 95% CI [4.72%, 5.33%] — brackets the advertised 5%, so the test itself is sound |
| 5 | Twenty looks, stop at the first crossing: **25.41%** | ✅ | §2. CI [24.81%, 26.01%] |
| 6 | That is **5.1×** the advertised rate | ✅ | §2, 25.41 / 5.01 |
| 7 | By number of looks: 1 → 5.0%, 2 → 8.6%, 5 → 14.6%, 10 → 19.6%, 20 → 25.4% | ✅ | §3 / `beat_data.json` `fpr_by_looks`. On-screen values are these rounded to 1dp |
| 8 | Hero run crosses at n=100 with z = −2.47 | ✅ | `beat_data.json` `hero.cross_at_n`, `hero.cross_z` |
| 9 | The same run ends at n=2,000 with z = −0.27 | ✅ | `hero.final_z` |
| 10 | It crosses the naive band once and the calibrated band zero times | ✅ | `hero.n_crossings_naive` = 1, `n_crossings_calibrated` = 0 |
| 11 | 5,081 of the 20,000 runs stopped "significant" | ✅ | `beat_data.py`, count of `first >= 0` |
| 12 | Median measured difference among them: **4.40 pp** (44% of baseline) | ✅ | `curse.median_abs_pp`. True difference is 0.00 |
| 13 | Smallest measured difference among them: **1.80 pp** | ✅ | `curse.min_abs_pp`. Narration says "none under one point eight" — correct, 1.80 is the floor |
| 14 | **Nothing** lands within 1.5 pp of zero | ✅ | `curse.share_within_1_5pp` = 0.00% |
| 15 | 97.6% of early stops measured ≥ 2 pp | ✅ | `curse.share_above_2pp` |
| 16 | Median stopping point n = 400 per arm | ✅ | `curse.median_stop_n`; 78% stopped in the first half (`peeking_evidence.py` §5) |
| 17 | Bonferroni boundary z > 3.02 → **1.8%** false positives | ✅ | §6 / `boundaries[1]`. α/(2·20), normal quantile |
| 18 | Calibrated boundary z > 2.66 → **5.1%** | ✅ | `beat_data.json` `boundaries[2]` |
| 19 | The calibrated boundary is fitted on a *separate* sample from the one it is scored on | ✅ | `peeking_evidence.py` §6 draws `cal_a`/`cal_b` fresh before quantiling |
| 20 | At 80% power the sequential design spends **19% fewer** visitors | ✅ | `power_tradeoff.py`, 10% vs 12%: fixed n=3,860 → sequential avg n=3,136 |
| 21 | Below roughly 65% power it spends **more** | ⚠️ see correction 3 | `power_tradeoff.py`: +15% at 50% power, −3% at 65%. The crossover lies between those two measured points and was not resolved more finely |

## Corrections applied during the build

**1 — The matched-power comparison (§7).** The first pass compared a
group-sequential test to a fixed test *at the same horizon* and reported
sequential as strictly worse: power 52.9% → 37.5%. That comparison is
rigged — a stricter boundary at a fixed horizon can only lose power, so it
makes the correct procedure look like a pure penalty. Rewritten to hold power
fixed and compare what each design *spends*. The honest answer is in rows
20–21, and it is not uniformly flattering.

**2 — The winner's-curse histogram range.** The density was first binned over
±8 pp. `np.histogram` silently **drops** values outside its range, and 16.5% of
the mass lay beyond ±8 pp — so both lobes rendered as if they ended exactly
where the axis did. Range widened to ±15 pp, which holds 99.76%, and the
remaining 0.24% is now *clipped into the end bins* rather than discarded. An
assertion (`hist.sum() == len(signed)`) now fails the script if mass is ever
dropped again. The published shape is the corrected one.

**3 — "Below about sixty-five percent power."** Measured points are +15% at
50% power and −3% at 65%. The crossover is therefore just *under* 65%, not at
it. The narration's "below about sixty-five percent" is a fair reading of a
bracket, not a measured threshold, and is recorded here as such.

**4 — A spoken rounding.** B03's narration says "five times, fifteen" where
the measured value is 14.56% and the on-screen figure reads 14.6%. Ordinary
rounding, and the exact value is visible on screen while it is spoken.

## Claims considered and cut

- **"A dashboard refreshing every 10 visitors gives you ~22%."** Measured
  (`peeking_evidence.py` §4: 151 looks from n=500 → 21.97%) but cut, because
  it is *lower* than the 20-look figure and the reason is a technicality —
  that run deliberately skips the first 500 visitors per arm, where the normal
  approximation is not usable and where most early crossings happen. Shown
  next to 25.4% it would read as "more looks is safer", which is false.
  Dropping it is the honest choice; keeping it would need a beat of its own.
- **"Peeking is why most published A/B wins don't replicate."** Plausible,
  widely asserted, and not something this simulation measures. No row, no
  narration line.
- **Any claim about how often real teams peek.** No source. The reel says
  what peeking *does*, never how common it is.
- **Sequential testing "saves sample size"** as an unqualified claim. It does
  not, below roughly 65% power — see correction 1. The reel states both
  directions.
- **mSPRT / always-valid p-values / alpha-spending by name.** Correct and
  relevant, but naming methods the reel does not demonstrate would be citing,
  not teaching. The calibrated boundary is shown because it is computed here.

## Register and scope

- `ai-` track: educational. Narrator **Jainil**, `@HumanitariansAI`, no
  `act: "REPORT"`.
- Handoff beat present (HANDOFF LAW applies on this track).
- The simulation is Bernoulli conversion data with equal arm sizes and a
  pooled two-proportion z-test. It is not a model of ratio metrics, variance
  reduction, clustered assignment, or unequal allocation — none of which the
  reel claims to cover.
