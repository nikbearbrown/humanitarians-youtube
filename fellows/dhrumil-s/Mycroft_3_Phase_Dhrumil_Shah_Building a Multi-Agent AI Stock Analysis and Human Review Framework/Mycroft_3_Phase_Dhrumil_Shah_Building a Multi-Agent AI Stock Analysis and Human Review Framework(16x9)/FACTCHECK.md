# FACTCHECK — Mycroft Phase 3 (16:9)

Every claim and every number that appears on screen, with where it comes from and what this
package can and cannot vouch for.

## The rule this package follows

This folder was rebuilt from the author's delivered **landscape** master. The Phase 3 dataset, notebooks and
model outputs are **not** in this package, so **nothing here was recomputed**. Each figure is
reproduced exactly as it appears in the author's own film and is attributed to the author's
Phase 3 notebook run. No figure was re-derived, re-estimated, rounded differently, or invented.

That means this document verifies **fidelity to the master**, not the statistics themselves.
Re-verifying the underlying analysis requires the Phase 3 notebooks and data.

## Numbers shown on screen

| # | Claim on screen | Beat | Source | Status |
|---|---|---|---|---|
| F1 | `0.148` mean pairwise correlation | S04 | author's Phase 3 notebook, as shown in the master | carried over verbatim ✅ · not recomputed ⏳ |
| F2 | `19.7%` PC1 share of variance | S04 | author's Phase 3 notebook | carried over verbatim ✅ · not recomputed ⏳ |
| F3 | `normal` market state on 2026-02-11 | S04 | author's Phase 3 notebook | carried over verbatim ✅ |
| F4 | `12` stress windows flagged | S04 | author's Phase 3 notebook; also printed in notebook chart 1's legend (`stress windows (n=12)`) | carried over verbatim ✅ · internally consistent ✅ |
| F5 | `9,636` anomaly events | S05 | author's Phase 3 notebook; notebook chart 3 caption reads `9,636 events at \|modified z\| >= 4` | carried over verbatim ✅ · internally consistent ✅ |
| F6 | attribution split `3,972 / 3,397 / 2,267` | S05 | author's Phase 3 notebook | carried over verbatim ✅ · **sums to 9,636, consistent with F5** ✅ |
| F7 | tier thresholds −3.0 / −4.5 / −6.5%, −25 / −40 / −60%, 20 / 30 / 45% | S07 | the master's own "Documented tier thresholds" table | carried over verbatim ✅ |
| F8 | overall ROC-AUC `0.516` | S08 | author's Phase 3 notebook; chart 9 shows `overall · all holdout rows`, n=27,600 | carried over verbatim ✅ · not recomputed ⏳ |
| F9 | bull / high-volatility ROC-AUC `0.774` | S08 | author's Phase 3 notebook; chart 9 shows `regime · Bull / High volatility (v3)`, n=720 | carried over verbatim ✅ · not recomputed ⏳ |
| F10 | `33/33` validation checks passed | S11 | author's Phase 3 validation suite | carried over verbatim ✅ · not re-run ⏳ |
| F11 | `120` names in the universe | S04 narration, chart 1 title | author's Phase 1 cleaned panel | carried over verbatim ✅ |
| F12 | review-queue rows EL, HAL, COF, SPGI, NOW — all `yes / yes / High / uncertain / 6` | S10 | the master's own table | carried over verbatim ✅ |
| F13 | queue sectors: EL Consumer Defensive · HAL Energy · COF Financial Services · SPGI Financial Services · NOW Technology | S10 | the landscape master's Sector column (not shown in the 9:16 cut) | carried over verbatim ✅ · sector labels match the public classification of each ticker ✅ |
| F14 | stage runtimes: MarketStructureAgent complete 1.61 s; AnomalyEventAgent 1.95 s; PeerCohortBenchmarkAgent 0.22 s; TailRiskLiquidityAgent 0.49 s; PredictionReliabilityAgent 13.23 s | S09 | the landscape master's stage cards (not shown in the 9:16 cut) | carried over verbatim ✅ · **not re-measured** ⏳ · these are one run's wall-clock times on the author's machine, not a benchmark |

## Method claims

| # | Claim | Beat | Assessment |
|---|---|---|---|
| M1 | Rolling **modified z-scores built on medians, not means** | S05 | Consistent with the code shown: median + MAD with a MAD scale factor. Standard robust outlier practice. ✅ |
| M2 | Expanding percentiles "so nothing looks ahead" | S04 | An expanding-window percentile uses only history up to each point, so the claim is coherent. This package did not execute it. ⏳ |
| M3 | Cohort fallback `INDUSTRY (>= 5 names) → SECTOR:: → UNIVERSE::all` | S06 | Stated on screen in the master and reproduced verbatim. ✅ |
| M4 | **Ticker-clustered** bootstrap intervals | S08 | Clustering resamples by ticker rather than by row, which is the right treatment for repeated measures on the same name. Coherent. ⏳ not re-run |
| M5 | Reliability labelling rule (CI above 0.50 → reliable, below → unreliable, spanning → uncertain) | S08 | Matches the code card shown in the master and chart 9's legend. ✅ internally consistent |
| M6 | "A failed agent degrades the run instead of stopping it" | S09 | Consistent with `BaseAgent` error isolation and the `attention_required` statuses shown. ⏳ not executed here |
| M7 | Amihud illiquidity | S07 | Named correctly (Amihud's 2002 illiquidity measure: mean of \|return\| / dollar volume). The code card shows a mean over a dropna'd input scaled by 1e6, consistent with the standard construction. ✅ |
| M8 | `human_decision` / `human_rationale` created empty by design | S10 | Shown in the aggregation code (`frame["human_decision"] = None`) and stated in narration. ✅ internally consistent |
| M9 | "Degrade, don't stop" — BaseAgent.run catches the exception, returns a failed AgentResult, and the pipeline continues; the validation suite proves it with an empty-context run | S09 | Stated on screen in the landscape master and reproduced verbatim. Consistent with the `agent execution` and `inter-agent communication` check families in S11. ⏳ not executed here |

## Advisory and scope

| # | Item | Status |
|---|---|---|
| A1 | "Educational research output from Mycroft. Not personalised financial advice or an investment recommendation." | Present in the narration, on the S10 advisory card, and on the S11 end card — as in the master ✅ |
| A2 | The film shows a ranked **review queue for a human**, not trade recommendations | ✅ consistent throughout |
| A3 | Ticker symbols shown (EL, HAL, COF, SPGI, NOW) are public equity identifiers used as research examples, carried over from the master | ✅ no personal data anywhere in the package |
| A4 | ROC-AUC values near 0.50 are presented as *uncertain*, not as predictive success | ✅ the film's own framing; the 33-check suite and the labels exist to make that visible |

## What a reviewer must still do before this is published

| Gate | Status |
|---|---|
| Re-run the Phase 3 notebooks and confirm F1–F14 still hold on the publish date | ⏳ |
| Note that F14's runtimes are machine- and run-dependent; re-measure before presenting them as performance | ⏳ |
| Confirm the ticker examples and the 2026-02-11 market-state date are still appropriate to show | ⏳ |
| Read the narration against the animatic (Gate P) | ⏳ |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
