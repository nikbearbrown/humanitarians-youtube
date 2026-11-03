# PEDAGOGY — ECIS Episode 7: The Bigger Picture (ai-explainer, narrated by Anjana)

Fresh build from the pre-authored `narration/*.txt` + `visuals/*.md` briefs in
this folder. One insight: every judgment ECIS made through Episode 6 looked at a
single company in isolation. Episode 7 is the episode where it starts looking
sideways — at what analysts already expected, at what peer companies are doing,
and at the sector rather than the index.

Sequel to Episodes 1–6.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B07 (verdict) / B08 (handoff) /
  B09 (outro). B01–B06 illustrate the mechanism — the pullback to parallel
  pipelines, the consensus delta, the surprise scatter, the correlation
  heatmap, the two-benchmark comparison, the full-architecture close ✓
- SHOW-DON'T-TELL LAW: every body beat carries a `show` block; the evidence
  (the delta bar, the two surprise scenarios, the heatmap cluster and its
  leading indicator, the +5% graded twice) lives on screen ✓
- your-turn closing standard: B07 VERDICT → B08 YOUR TURN → B09 TITLE outro ✓
- Narrator: Anjana, no channel handle. Source says `am_onyx` — overridden to
  `af_bella` per the series convention ✓
- Dark-stage deviation: B01–B06 on the dark ground, same PEDAGOGY-approved
  deviation as Episodes 1–6.
- **NARRATION BUDGET — no deviation this episode.** Body beats run 44–62 words,
  comfortably inside the 45–70 range. First episode in the series where this is
  true; Episodes 5 and 6 both needed logged exceptions.
- **No real company names or tickers anywhere** — Company A through H.

## Two authoring decisions, both confirmed with the author

**1. Palette.** The visual briefs state "Same shapes and colors as Ep1-Ep6" and
then list hex values that do *not* match what Episodes 1–6 shipped:

| Role | Briefs say | Series actually uses |
|---|---|---|
| Background | `#1A1A2E` navy | `#0a0a0f` near-black |
| Keyword reader | `#EAEAEA` white | `#3E7CB1` blue |
| FinBERT reader | `#4A90D9` blue | `#3EB8A8` teal |
| NER reader | `#27AE60` green | `#D9A757` amber |
| LLM reader | `#9B59B6` purple | `#9B6FD1` purple |
| Triangulator | `#2C3E50` slate | `#D97757` terracotta |
| Prediction | `#F1C40F` gold | `#D4A853` gold |

**Resolved: keep the established series palette**, honoring the briefs' stated
intent over their hex list. Episode 7 therefore looks identical to Episodes
1–6. The briefs' *roles* are all preserved — gold still means prediction,
blue still means extraction, grey means consensus/broad-market — they are just
rendered in the series' existing values. The one genuinely new color this
episode is **orange `#D9773F` for surprise and high correlation**, which the
briefs introduce and which does not collide with anything already in use.

**2. B06 was labelled "Your Turn" but is not one.** The source beat's narration
is a close ("…the system now sees beyond individual signals. Anjana here,
thanks for watching") and its brief is an architecture montage plus a title
card. Built as the close. A real your-turn handoff with a pasteable prompt was
added at B08 per HANDOFF LAW, and the "thanks for watching" sign-off moved to
B09 where this series always puts it. Logged because it is the one place the
source narration was edited rather than kept verbatim.

## Evidence discipline (DOUBLE-CHECK LAW)

Every figure comes from the pre-authored briefs in this folder. Rows are split
into claims about the real system (confirmed by the author before audio spend)
and illustrative placeholders.

### Claims about the real system — **human-confirmed 2026-09-18**

| Claim (as scripted) | Where | Confirmed? |
|---|---|---|
| The system pulls analyst consensus estimates per company and quarter | B02 | ☑ |
| It computes the delta between extracted guidance and consensus, and that delta becomes a feature in the prediction model | B02 | ☑ |
| A surprise score is derived from that delta | B03 | ☑ |
| **High-surprise signals are assigned lower confidence** (surprises are harder to predict) | B03 | ☑ |
| Pairwise correlations between guidance directions across all tracked companies | B04 | ☑ |
| Co-moving cluster detection | B04 | ☑ |
| Leading-indicator detection — a company that raises one quarter before peers | B04 | ☑ shipped, not aspirational |
| Grading moved from a broad-market index to a sector-specific benchmark | B05 | ☑ |
| Four readers → triangulator → pre-registered signal → graded against market (the Episode 1–6 recap) | B01 | ☑ carried over, already confirmed |

### Illustrative placeholders

| Figure | Where | Status |
|---|---|---|
| Signal badge "raised, 0.82" | B01 | ☑ illustrative |
| The semiconductor example: company +5%, broad market +2%, sector +8% | B05 | ☑ illustrative — the narration presents it as a hypothetical ("if the entire semiconductor sector rises eight percent…"), and the arithmetic is what carries the point |
| Companies A–H, the co-moving cluster {A, C, E, G}, and the heatmap values | B04 | ☑ illustrative — anonymous placeholders, no real tickers |
| The surprise/confidence scatter cloud | B03 | ☑ illustrative — shows the *direction* of the relationship the narration claims, not measured data |
| Five parallel pipelines in the B01 pullback | B01 | ☑ illustrative — the real system tracks more; five is what reads at that scale |

**One softening worth noting:** B01's recap says the system grades itself
"against actual stock movement thirty days later." Episodes 1–6 established
three horizons (30 / 90 / 180 days). Kept verbatim as a recap compression —
thirty days is the first and most concrete horizon — but it is a simplification
of what earlier episodes showed, not a change to the system.

## Friction protected

- Kept: the pullback to five parallel pipelines at the end of B01. It is the
  visual thesis of the whole episode — the single pipeline that carried six
  episodes becomes one row in a grid — and compressing it would waste the
  setup.
- Kept: both scenarios in B03. A surprise score means nothing without the
  low-surprise case beside it to compare against.
- Kept: the leading-indicator animation in B04 rather than just the cluster.
  Clusters are correlation; the one-quarter lead is the part that could
  actually be traded on, and it is the more interesting claim.
- Kept: showing the *same* +5% twice in B05 with opposite verdicts. The beat
  only works because the company's number never changes — only the benchmark
  does.

## Sign-off notes

1. Evidence table is per-figure and split into real-system claims vs
   illustrative placeholders. **Human confirmation obtained before audio spend
   (2026-09-18)**, including that
   leading-indicator detection has actually shipped.
2. Palette conflict resolved with the author in favour of series continuity;
   the mapping table above records exactly what was overridden.
3. The B06 relabel and the moved sign-off line are logged above as the one
   narration edit in the episode.
4. No narration-budget deviation this episode.
5. Animated-slate review after `remotion_scenes.py` renders — frame-grab QC per
   VISUAL QC LAW, both orientations.

VERDICT: PASS
