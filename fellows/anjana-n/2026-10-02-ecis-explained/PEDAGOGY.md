# PEDAGOGY — ECIS Episode 9: Proving It Works (ai-explainer, narrated by Anjana)

This folder arrived with a **pre-written `script.md` and `README.md`** alongside the `narration/*.txt` and `visuals/*.md` briefs. The script's narration matches the narration files verbatim. Both authored files were **preserved and extended, not rewritten** — see the authoring decisions below.

Sequel to Episodes 1–8.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B07 (verdict) / B08 (handoff) /
  B09 (outro). B01–B06 illustrate the mechanism — the recap and the shield, the
  three statistical panels, the drift curves and decay chart, the Chroma before/after and the Grafana wall, the full-architecture close ✓
- your-turn closing standard: B07 VERDICT → B08 YOUR TURN → B09 TITLE outro ✓
- Narrator: Anjana, no channel handle. Source says `am_onyx` — overridden to
  `af_bella` per the series convention ✓
- **NARRATION BUDGET:** body beats run 42–97 words. B02 (97), B03 (78), B04 (77)
  and B05 (76) are over the 45–70 range — logged as deviations below.
- **No real company names or tickers anywhere** — Company A through D.

## One authoring decisions

**1. The pre-written `script.md` was extended, not replaced.** B01–B06 — their
narration *and* their visual direction — are the author's text kept word for
word. What was added: the B00 cold-open ask, B07 verdict, B08 your-turn handoff,
B09 title outro, and a header block naming the voice override and target length.
A note at the top of the file records which parts are authored and which were
added, so the distinction survives in the file itself rather than only here.

## Narration budget deviations

This episode runs long in four of six body beats, and the reason is structural
rather than prose-level: **each body beat is a list of three or four separately
shipped facilities**, and the narration names them one at a time.

- **B02 (97 words)** — bootstrap intervals, permutation tests, power analysis,
  plus the framing question and the closing line that gives the beat its point. This is the longest beat in nine episodes. It survives whole because the three facilities answer three different questions — is the difference real, is it bigger than chance, and do we even have enough data to tell — and dropping any one leaves a gap a viewer would notice.
- **B03 (78 words)** — profiling, lineage, completeness. Three modules, one
  sentence each, plus the closing line.
- **B04 (77 words)** — PSI/KL drift detection and the tracker, each with
  the condition that fires it.
- **B05 (76 words)** — HNSW tuning, exemplar rebalancing, and the Grafana
  wall. This one is a genuine double beat: retrieval optimisation and monitoring
  are unrelated work bundled under one heading by the source. Kept as authored
  rather than split, because splitting would mean rewriting the author's script.

## Evidence discipline (DOUBLE-CHECK LAW)

Every figure comes from the pre-authored script and briefs. Rows are split into
claims about the real system (confirmed by the author before audio spend) and
illustrative placeholders.

### Claims about the real system — **human-confirmed 2026-10-02**

| Claim (as scripted) | Where | Confirmed? |
|---|---|---|
| Bootstrap confidence intervals wrap every Scorecard metric, 1,000 resamples, around Brier and skill scores | B02 | ☑ |
| Paired permutation tests, 10,000 shuffled assignments, producing p-values between models | B02 | ☑ |
| A power-analysis module reporting how many more signals a difference needs to become detectable | B02 | ☑ |
| A profiling module running after every ingestion batch — distributions, missing values, outliers | B03 | ☑ |
| A lineage tracker tracing a signal back through raw transcript → cleaned text → chunk → reader outputs → triangulation weights → dedup decision | B03 | ☑ |
| A per-ticker completeness monitor flagging missing consensus, price holes and unresolved outcomes | B03 | ☑ |
| Concept drift via PSI and KL divergence over rolling quarterly windows | B04 | ☑ |
| A tracker for a retraining alert after 10 consecutive predictions below the naive baseline | B04 | ☑ |
| ChromaDB HNSW indexes tuned for financial text (ef_construction / M / ef_search) | B05 | ☑ |
| Exemplar store deduplicated and rebalanced, with adversarial examples added at the maintained-none boundary | B05 | ☑ |
| Live Grafana dashboards — reader health, latency percentiles, throughput, completeness — with threshold alerts | B05 | ☑ |
| Four readers → triangulator → pre-registered signal → graded against market (the Ep1–8 recap) | B01 | ☑ carried over, already confirmed |

### Illustrative placeholders

| Figure | Where | Status |
|---|---|---|
| Signal badge "raised, 0.82" | B01 | ☑ illustrative, carried from earlier episodes |
| The two Brier scores and their overlapping intervals | B02 | ☑ illustrative — drawn to overlap *partially*, which is the honest picture of a difference that needs a test rather than an eyeball |
| "p = 0.03" and the shape of the permuted null | B02 | ☑ illustrative |
| "need 340 more signals" and the power curve | B02 | ☑ illustrative |
| "2 of 850 missing", "1 outlier detected", "chunk 47" | B03 | ☑ illustrative |
| The per-ticker completeness grid and its two red cells | B03 | ☑ illustrative — Company A–D, no real tickers |
| "PSI = 0.31" and the two distribution curves | B04 | ☑ illustrative — 0.31 is above the conventional 0.25 "significant shift" threshold, so the number and the drawn gap agree |
| The rolling-accuracy line and its ten highlighted points | B04 | ☑ illustrative |
| The Grafana panel values — ~95% reader success, p50/p95/p99 bands, throughput bars | B05 | ☑ illustrative |


## Sign-off notes

1. Evidence table is per-figure and split into real-system claims vs
   illustrative placeholders. **Human confirmation obtained before audio spend
   (2026-10-02)** on all eleven rows, in three groups: the
   statistical facilities, the data-quality and drift machinery, and the
   ChromaDB plus Grafana work.
2. The author's `script.md` and `README.md` were extended rather than replaced;
   the script carries a note recording which beats are authored and which were
   added.
3. Palette follows the Episode 7 precedent; the inert `color_continuity` block
   is noted rather than applied.
4. Four narration-budget deviations (B02, B03, B04, B05) are argued above
   rather than waived.
5. Animated-slate review after `remotion_scenes.py` renders — frame-grab QC per
   VISUAL QC LAW, both orientations.

VERDICT: PASS
