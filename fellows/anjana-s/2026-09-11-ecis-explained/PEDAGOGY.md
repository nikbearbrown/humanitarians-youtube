# PEDAGOGY — ECIS Episode 6: From Reading to Predicting (ai-explainer, narrated by Anjana)

Fresh build from the pre-authored `narration/*.txt` + `visuals/*.md` briefs in
this folder (`script.md` and `README.md). One insight: the
system did not acquire any new data to start predicting. Every feature the
model uses is computed from the decision log it had already been keeping — and
the prediction is locked before the call under exactly the same append-only
rule that has governed every extraction since Episode 1.

Sequel to Episodes 1–5. Episode 5 closed the loop on self-correction; Episode 6
turns the accumulated log forward.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B07 (verdict) / B08 (handoff) /
  B09 (outro). B01–B06 illustrate the mechanism — the pipeline recap, the
  feature vector, the locked prediction record, the two-tier scorecard, the
  forecast view, the past/bridge/future close ✓
- SHOW-DON'T-TELL LAW: every body beat carries a `show` block; the evidence
  (the six feature boxes, the record fields, the checkmarks and the red X, the
  three forecast cards, the open Q4 dot) lives on screen ✓
- your-turn closing standard: B07 VERDICT → B08 YOUR TURN (prompt read aloud
  and discussed per HANDOFF LAW) → B09 TITLE outro ✓
- Narrator: Anjana, no channel handle. Source files say `am_onyx` — overridden
  to `af_bella` per the series convention ✓
- Dark-stage deviation: B01–B06 render on the dark ground (`#0a0a0f`), same
  PEDAGOGY-approved deviation as Episodes 1–5.
- **Color law, new this episode:** gold (`#D4A853`) is the PREDICTION color and
  appears nowhere else. Extraction stays blue, market outcome is white. This is
  the visual argument that predictions and extractions are different objects
  graded by different scorecards. Logged so a future episode doesn't reuse gold
  for something unrelated.
- **Spatial law, new this episode:** extraction lives on the LEFT, prediction
  on the RIGHT, split by a dotted border introduced at the end of B01 and
  echoed in B06 (past / bridge / future).
- **NARRATION BUDGET — logged deviation.** B01 (~105 words), B02 (~100), B03
  (~85), B04 (~115) run over the 45–70-word range. Kept verbatim per the series
  convention; every one carries a dense `show` block. B04 is the longest and is
  built as a genuine two-tier build followed by a divergence flash, so it fills
  its ~40s rather than freeze-holding.
- **No real company names or tickers anywhere** — Company A / B / C throughout,
  matching Episodes 4 and 5.

## Evidence discipline (DOUBLE-CHECK LAW)

Every figure below comes from the pre-authored `narration/*.txt` and
`visuals/*.md` briefs in this folder. **Nothing was invented for the video.**
Rows are split into claims about the real system (which a human confirms before
audio) and illustrative placeholders (which need no confirmation).

### Claims about the real system

| Claim (as scripted) | Where | Source | Confirmed? |
|---|---|---|---|
| The prediction model is a **logistic regression** | B02, B06, B07 | `narration/02_features.txt` | ☑ |
| Features are computed only from the existing decision log — no new sources, no new APIs | B02, B07 | `narration/02_features.txt` | ☑ |
| The six features: prior direction, trend length, stock momentum, sector aggregate, days since last call, prior confidence | B02 | `visuals/02_features.md` | ☑ |
| A prediction record stores: ticker, direction, confidence, feature-vector snapshot, model version, timestamp | B03 | `narration/03_preregistered.txt` | ☑ |
| Predictions are pre-registered (append-only, locked before the call) and cannot be revised after | B03, B07 | `narration/03_preregistered.txt` | ☑ |
| Two-level scorecard: L1 grades prediction vs extraction, L2 grades extraction vs market; graded independently | B04, B07 | `narration/04_two_levels.txt` | ☑ |
| A forecast view exists in the dashboard showing direction, confidence, top driver, sector agreement, and a per-company accuracy timeline | B05 | `narration/05_forecast.txt` | ☑ |
| Four readers, triangulator, 30/90/180-day grading (the Episode 5 recap, unchanged) | B01 | `narration/01_intro.txt` | ☑ carried over from Ep 5, already confirmed |

### Illustrative placeholders (Company A / B / C)

| Figure | Where | Status |
|---|---|---|
| Prediction confidences 0.73 / 0.68 / 0.61 | B02–B05 | ☑ illustrative |
| Stock momentum +4.2% / −6%; sector aggregate 60% raised; 87 days since last call | B02, B05 | ☑ illustrative |
| Excess returns +3.2% (correct case) / −1.4% (divergence case) | B04 | ☑ illustrative |
| Model version "v1.0" and the two dates | B03 | ☑ illustrative |
| Company A's Q1–Q4 prediction track record (right, right, wrong, pending) | B05 | ☑ illustrative |
| The three-company signal history in the log | B02 | ☑ illustrative |

**Standing rule for this table:** if any real-system row stops describing the
pipeline — the model type changes, a feature is added or dropped, the record
fields change — fix the beat's narration and on-screen text before
re-rendering. Every row names its source file for that reason.

## Friction protected

- Kept: all six feature boxes in B02, not a representative three. The
  narration's argument is that the log is *rich* — that there are many patterns
  in what the system already has — and three boxes would undercut it.
- Kept: the waiting period in B03, with days visibly ticking past between the
  locked prediction and the call. It is the beat's whole point: the prediction
  is committed *before* the outcome, and the empty time makes that legible.
- Kept: the divergence case in B04 (green on top, red on bottom). Without it
  the two-level scorecard reads as redundant. With it, the independence of the
  two questions is the insight.
- Kept: the open, unfilled Q4 dot in B05. A dashboard that only shows graded
  history is a report; the open dot is what makes it a forecast.

## Sign-off notes

1. Evidence table is per-figure and split into real-system claims vs
   illustrative placeholders; every real-system row names its source file.
   **Human confirmation obtained before audio spend (2026-09-11)**.
2. Narration-budget deviation on B01–B04 logged and accepted; each beat's
   component is built to fill its real audio span.
3. Dark-stage deviation for B01–B06 approved, continuing Episodes 1–5.
4. Gold-for-prediction and left/right spatial laws logged for series continuity.
5. Animated-slate review after `remotion_scenes.py` renders — frame-grab QC per
   VISUAL QC LAW, both orientations.

VERDICT: PASS
