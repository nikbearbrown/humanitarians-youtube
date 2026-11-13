# ECIS Episode 9: Proving It Works

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source `beats.json` says `am_onyx`; overridden per
the series convention set in Episode 1 (Anjana narrates, no channel handle)
**Target length:** ~3:40 (16:9 master) / ~2:50 (9:16 short)
**Register:** Teardown
**Series:** Sequel to Episodes 1–8. Episode 8 taught the system to read the
delivery. Episode 9 turns the instruments on the system itself and asks the
only question that was still outstanding: how do you know any of this works?

---

## B00 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~13s

**Narration:**

Eight episodes of building, and one question had gone unanswered the whole
time: how would we know if any of it actually worked? I'm Anjana — this week
the system turns the instruments on itself.

**Composer ask:**

> ECIS reports Brier scores, skill scores, model comparisons. But a number on a
> dashboard isn't evidence. How does the system show that a difference is real
> and not noise, that the data underneath it is sound, and that it still holds
> next quarter?

**Output lines (resolved on screen):**
- confidence intervals and p-values on every metric
- every signal traceable back to its raw transcript
- drift and decay watched, with alerts before they bite

---

## B01 — Recap (~20s)

**Narration:**
Hello, Anjana here. Quick recap. ECIS reads earnings call transcripts through four independent readers, triangulates their outputs into a single confidence-scored signal, pre-registers that signal, and grades itself against actual stock movement thirty days later. Last episode, the system added linguistic profiling, market impact scoring, and migrated to PostgreSQL. This week, it proves its own claims with statistics, tracks every byte of data from source to signal, and watches itself in real time.

**Visual direction:**
Fast animated recap of the ECIS pipeline: transcript enters, four reader nodes light up in parallel, arrows converge at the triangulator, signal badge appears, prediction layer glows gold, linguistic gauges and market impact charts flash briefly (Ep8 additions), PostgreSQL box pulses (Ep8 addition), arrow to the 30-day market check. 

---

## B02 — Statistical Rigor (~12s)

**Narration:**
When the system says one model outperforms another, how do you know that is real and not noise? Bootstrap confidence intervals now wrap every Scorecard metric. One thousand resamples of the signal set produce upper and lower bounds around each Brier score and skill score. Paired permutation tests compare models head to head: ten thousand shuffled assignments compute p-values that separate real differences from random variation. And a power analysis module reports how many more signals are needed before a given difference becomes detectable. The system no longer just reports numbers. It reports how much to trust them.

**Visual direction:**
Three panels stacked vertically. Top panel: a horizontal bar for "Model A Brier score" with a point estimate dot and whisker lines extending left and right showing the 95% confidence interval. A second bar below it for "Model B" with its own CI. The intervals overlap partially. Label: "bootstrap 95% CI." Middle panel: a histogram of 10,000 permuted differences, bell-shaped, with the observed difference marked as a vertical red line in the tail. Label: "permutation test, p = 0.03." Bottom panel: a curve showing statistical power (y-axis, 0 to 1) vs sample size (x-axis). A horizontal dashed line at 0.80 marks the power threshold. A vertical dashed line drops from the intersection to the x-axis showing "need 340 more signals." Label: "power analysis."

---

## B03 — Data Quality (~12s)

**Narration:**
The system now tracks data quality end to end. A profiling module runs after every ingestion batch, computing distributions, missing values, and outliers across all fields. A lineage tracker traces each final signal back through every transformation: raw transcript, cleaned text, chunk index, reader outputs, triangulation weights, deduplication decision. And a completeness monitor flags gaps per ticker: missing consensus estimates, price data holes, unresolved outcomes past their evaluation horizon. Nothing slips through unnoticed.

**Visual direction:**
Left column: a small data profile card showing a mini histogram of confidence scores, a missing values count (2 of 850), and an outlier flag (1 detected). Label: "data profiling." Center: a vertical chain of linked boxes representing lineage stages, top to bottom: "raw transcript" to "cleaned text" to "chunk 47" to "FinBERT + LLM outputs" to "triangulated signal" to "validated signal." Each box connected by a thin arrow. Label: "data lineage." Right column: a checklist grid per ticker (rows: Company A, B, C, D; columns: consensus, prices, outcomes). Most cells have green checks, two cells have red X marks. Label: "completeness monitor."

---

## B04 — Concept Drift and Decay (~10s)

**Narration:**
Markets change. Language patterns shift. A model trained on last year's transcripts may not work on this year's. The system now monitors concept drift by computing distribution shifts across rolling quarterly windows using Population Stability Index and KL divergence. When feature distributions move significantly, the system flags assumptions. A parallel decay tracker watches the prediction layer: if rolling accuracy drops below the naive baseline for ten consecutive predictions, it triggers a retraining alert.

**Visual direction:**
Left side: two overlapping distribution curves. The first curve (blue, labeled "Q1-Q2") is centered. The second curve (orange, labeled "Q3-Q4") has shifted right. The gap between them is shaded and labeled "PSI = 0.31, drift detected." An icon pulses. Right side: a rolling accuracy line chart. The line trends downward over the last segment. A horizontal dashed line marks the "naive baseline." The accuracy line crosses below it, and a red alert badge appears: "retraining recommended." Ten consecutive dots below the baseline are highlighted.

---

## B05 — ChromaDB Optimization and Grafana (~12s)

**Narration:**
The retrieval layer got faster and smarter. ChromaDB's HNSW indexes were tuned for financial text, balancing recall against speed. The exemplar store was deduplicated and rebalanced, with adversarial examples added at the maintained-none boundary where the model struggles most. And the system now watches itself through Grafana: real-time dashboards tracking reader health, extraction latency percentiles, signal throughput, and data completeness, all with threshold alerts that fire before problems compound.

**Visual direction:**
Top half: a before-and-after for ChromaDB. Left: a messy cluster of dots with some near-duplicates circled (labeled "before: duplicates, imbalanced"). Right: a clean, evenly spaced set of dots with a few new dots at the boundary region (labeled "after: deduplicated, boundary exemplars added"). HNSW parameter labels float nearby: "ef_construction, M, ef_search." Bottom half: a Grafana-style dashboard mockup with four panels arranged 2x2. Top-left: a time-series line for reader success rate (green line ~95%). Top-right: latency percentile lines (p50, p95, p99 in blue shades). Bottom-left: signal throughput bar chart per batch. Bottom-right: a data completeness grid with green/red cells. A small alert bell icon glows on the latency panel where p95 is spiking.

---

## B06 — Your Turn (~7s)

**Narration:**
Bootstrap intervals. Permutation tests. Full data lineage. Concept drift detection. And Grafana dashboards watching everything in real time. The system does not just run. It proves it works. Anjana here, thanks for watching.

**Visual direction:**
Wide pullback showing the full ECIS architecture. This episode's additions glow gold in sequence: CI whiskers on the Scorecard, lineage chain on the data path, drift curves on the feature pipeline, Grafana dashboard panels floating alongside. All settle. Fade to title card: "ECIS Episode 9: Proving It Works."

---

## B07 — Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~26s

**Narration:**

Let's recap with Claude. Every number on the Scorecard now carries an interval
around it and a p-value beside it, so "model A is better" is a claim with
evidence rather than a reading. Every signal can be walked backwards to the raw
transcript it came from. The system watches its own inputs for drift and its own
accuracy for decay, and says so before either becomes a problem. And all of it
is on a dashboard that alerts rather than waits to be looked at.

**Artifact lines:**
- Bootstrap intervals and permutation p-values wrap every Scorecard metric —
  differences are tested, not asserted.
- A power analysis says how many more signals a given comparison still needs.
- Lineage traces each signal back through every transformation to its raw
  transcript; a completeness monitor flags the gaps.
- PSI and KL divergence watch for drift, a decay tracker watches accuracy
  against the naive baseline, and Grafana alerts on both.

---

## B08 — Your Turn

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~34s

**Narration:**

Your turn. Take a number you report regularly — a metric, a score, a win rate —
and ask what would have to be true for a change in it to count as real. Whether
you could trace any single figure back to the raw thing it came from. And
whether you would notice if the ground underneath it had quietly shifted since
you built it.

**Composer ask:**

> I report a number regularly — a metric, a score, a conversion rate, a win
> rate. Can you help me: one, work out what would have to be true for a change
> in it to count as a real difference rather than noise, and what test would
> actually show that; two, check whether I could trace any single reported
> figure back through every transformation to the raw thing it came from, and
> where that chain breaks; and three, tell me honestly how I'd find out if the
> conditions it was built under had shifted — and what the first symptom would
> look like?

---

## B09 — Title outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~5s

**Narration:**

Anjana here, thanks for watching.

**Title:** ECIS — Episode 9
**Subline:** proving it works · episode nine
**Handle:** (none)
