# PEDAGOGY — ECIS Episode 10: The Business Layer (ai-explainer, narrated by Anjana)

Fourth folder running to arrive with a **pre-written `script.md` and
`README.md`**. Both were **preserved and extended, not rewritten**.

One insight: nine episodes built a thing that reads one earnings call at a time
and grades itself honestly. None of that answers the question a desk would
actually ask, which is "so what". Episode 10 is the layer that turns a signal
per company per call into sector mood, speaker behaviour, and a ranked answer to
which features have ever actually moved a price.

Sequel to Episodes 1–9.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B07 (verdict) / B08 (handoff) /
  B09 (outro). B01–B06 illustrate the mechanism — the pipeline extending into a
  new section, the funnel and mood index and heatmap, the confidence gauge and
  the CEO/CFO gap, the ranked features and the surprise matrix, the three
  reaction curves, the full-architecture close ✓
- SHOW-DON'T-TELL LAW: every body beat carries a `show` block; the evidence (the
  mood line crossing its mean, the 27-point gap bracketed in red, the gold
  quadrant where the model saw what consensus missed, three curves that
  visibly do three different things) lives on screen ✓
- your-turn closing standard: B07 VERDICT → B08 YOUR TURN → B09 TITLE outro ✓
- Narrator: Anjana, no channel handle. Source says `am_onyx` — overridden to
  `af_bella` per the series convention ✓
- Dark-stage deviation: B01–B06 on the dark ground, same PEDAGOGY-approved
  deviation as Episodes 1–9.
- **NARRATION BUDGET:** body beats run 44–92 words. B01 (92), B04 (90), B05 (89)
  and B02 (73) are over the 45–70 range — logged as deviations below.
- **No real company names or tickers** — GICS sector names only (Tech,
  Healthcare, Finance, Energy), which are categories rather than companies.

## Three authoring decisions

**1. The pre-written `script.md` and `README.md` were extended, not replaced.**
B01–B06 narration and visual direction are the author's text word for word.
Added: B00 ask, B07 verdict, B08 handoff, B09 outro, and a header block. The
script carries a note recording which parts are authored and which were added.

**2. Palette — the Episode 7 resolution, now series law.** The README specifies
its own hexes and a continuity block (Llama `#9B59B6`, Mistral `#1ABC9C`, Qwen
`#F39C12`, prediction gold `#F1C40F`). Every role is preserved and rendered in
the established series values. No model is named in this episode's narration, so
the llama/mistral/qwen mapping is inert here and is noted rather than applied —
the same treatment as Episodes 8 and 9.

**3. B06 was labelled "Your Turn" but is not one.** Fourth episode running with
this mismatch. Its narration is a close that ends by naming the episode ("ECIS
Episode 10: The Business Layer") and its brief is an architecture montage plus a
title card. Built as the close. A real pasteable handoff was added at B08 per
HANDOFF LAW, and a sign-off line was added at B09 where the series always puts
it — note that unlike Episodes 7–9 the source narration here contains no
"thanks for watching" at all, so B09's line is new text rather than moved text.

## Narration budget deviations

Four of six body beats run long, for the same structural reason as Episode 9:
**each beat is a list of separately shipped modules**, named one at a time.

- **B01 (92 words)** — the recap now carries more detail than any previous one:
  four readers, five dynamic weighting dimensions, the prediction layer, three
  grading horizons, and five Episode 9 additions. It is doing the work of a
  standalone entry point, which the README explicitly asks for ("opens with
  standalone 20s recap so new viewers can follow").
- **B04 (90 words)** — two modules, each needing its statistical method named
  (Pearson and Spearman, three horizons) plus the three-way cross-tabulation and
  the point of it ("the model saw something analysts missed").
- **B05 (89 words)** — three distinct market behaviours (immediate pricing,
  continued drift, mean reversion) each need naming *and* distinguishing, plus
  the confidence-tier grouping.
- **B02 (73 words)** — marginally over; three modules in three sentences.

All four get correspondingly long visual builds. Logged rather than waived.

## Evidence discipline (DOUBLE-CHECK LAW)

Every figure comes from the pre-authored script and briefs. Rows are split into
claims about the real system (confirmed by the author before audio spend) and
illustrative placeholders.

### Claims about the real system — **human-confirmed 2026-10-09**

| Claim (as scripted) | Where | Confirmed? |
|---|---|---|
| Sector sentiment aggregator — market-cap-weighted composites of tone, hedging and forward-looking density across a GICS sector | B02 | ☑ |
| Mood index tracking that composite quarter over quarter, flagging regime changes | B02 | ☑ |
| Cross-sector heatmap benchmarking each sector's language metrics by z-score | B02 | ☑ |
| Management confidence score — hedging ratio, forward-looking density, definitive statement ratio, numerical specificity → 0–100, per speaker per call | B03 | ☑ |
| CEO-versus-CFO tone divergence detector | B03 | ☑ |
| Signal-to-price correlation — Pearson and Spearman, every extracted feature against excess returns at 1 / 5 / 30 days, ranked by informativeness | B04 | ☑ |
| Surprise score module cross-tabulating NLP prediction × consensus × actual | B04 | ☑ |
| Reaction window module — cumulative abnormal returns at 0 / 1 / 2 / 5 / 10 / 30 days, grouped by confidence tier | B05 | ☑ |
| Four readers triangulated with **dynamic weights across reader, model, speaker, chunk quality and section type** | B01 | ☑ |
| Predictions pre-registered and graded at **30, 90 and 180 days** | B01 | ☑ |
| Episode 9's additions (bootstrap CIs, permutation tests, drift detection, lineage, ChromaDB, Grafana) | B01 | ☑ carried over, confirmed last episode |

**A correction worth recording.** Episodes 7, 8 and 9 all compressed the grading
horizons to "thirty days later", and each time that was logged here as a
simplification of the three horizons Episodes 1–6 established. **This episode's
recap states all three — 30, 90 and 180 — and the author confirmed that is
correct.** So Episode 10 is not introducing a new claim; it is the first recap
in four episodes to state the horizons accurately. The earlier compression stays
logged where it was.

### Illustrative placeholders

| Figure | Where | Status |
|---|---|---|
| The four sector rows (Tech, Healthcare, Finance, Energy) and their heatmap z-scores | B02 | ☑ illustrative — GICS categories, no companies |
| The mood-index line and the point where it crosses its historical mean | B02 | ☑ illustrative |
| Confidence gauge at 72; the four input weights | B03 | ☑ illustrative |
| CEO 78 / CFO 51, "divergence: 27 points" | B03 | ☑ illustrative — and the arithmetic is right, 78 − 51 = 27 |
| Feature ranking and the r values (e.g. r = 0.34) | B04 | ☑ illustrative — plausible magnitudes for this kind of correlation, drawn in rank order so the bars and the numbers agree |
| The 2×2 surprise matrix counts | B04 | ☑ illustrative |
| The three reaction curves and their shapes | B05 | ☑ illustrative — the three *behaviours* are real and named in the literature; the specific curves are drawn, not measured |


## Friction protected

- Kept: the mood index crossing its mean **on screen** rather than a static
  "regime change detected" badge. The crossing is the detection.
- Kept: both executives' bars in B03 with the gap bracketed. A single
  "divergence: 27" number would be a claim; two bars and the space between them
  is the evidence.
- Kept: all three reaction curves in B05 on one axis. Immediate pricing,
  continued drift and mean reversion only mean anything relative to each other,
  and the whole point of the beat is that they are different shapes.
- Kept: the gold quadrant in B04's matrix rather than highlighting the diagonal.
  The valuable cell is specifically the disagreement — model raised, consensus
  lowered — and putting the glow anywhere else would teach the wrong thing.

## Sign-off notes

1. Evidence table is per-figure and split into real-system claims vs
   illustrative placeholders. **Human confirmation obtained before audio spend
   (2026-10-09)** on all eleven rows, in three groups: the sector
   and management modules, the market-impact analytics, and the three grading
   horizons.
2. The author's `script.md` and `README.md` were extended rather than replaced.
3. B06 built as the close; B09's sign-off is new text, not moved text, because
   the source narration contains none.
4. Four narration-budget deviations (B01, B02, B04, B05) argued above rather
   than waived.
5. Animated-slate review after `remotion_scenes.py` renders — frame-grab QC per
   VISUAL QC LAW, both orientations.

VERDICT: PASS
