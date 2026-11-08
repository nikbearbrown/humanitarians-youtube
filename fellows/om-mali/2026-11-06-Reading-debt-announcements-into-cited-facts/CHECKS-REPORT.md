# CHECKS-REPORT — reading-debt-announcements-into-cited-facts

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the week's actual instruction — *read every filing into structured facts; the model never types a number* — and lands three answer lines. COLD OPEN LAW: the ask lands ANSWERED, and the answer carries its own bad news from the first beat: the pass, the baseline that beat it, and the failed triage check. |
| B01 | SHOW | Claim: the model is bracketed by code. Three cards, and **the middle one is the only one in the accent and the only one not labelled CODE**. The rule sits above them as the thing the shape exists to satisfy. |
| B02 | SHOW | Claim: it rewrote the currency sign while claiming to copy. The passage is set as the filing reads it with **€1,500,000,000 highlighted**, the copy beneath it with **$1,500,000,000 highlighted**, and REFUSED lands in the accent. One character is the beat, so one character is what is marked. |
| B03 | SHOW | Claim: it passed its check, and the third bar is the honest one. Three bars, **three printed denominators**, and the extras on a second scale past a divider. |
| B04 | SHOW | Claim: the same value, twice, and only one of them can be checked. Two cards. The left one is **correct and bare**; the right one carries the passage id and the sentence. Nothing on the frame says the reader is more accurate. |
| B05 | SHOW | Claim: 24 refusals, 8 of them real. The refused tail is drawn as **24 countable cells with 8 filled**, not as a 9% sliver of a 254-wide band. |
| B06 | SHOW | Claim: a check I set myself, and did not pass. Two bars under **one dashed pass line drawn through both tracks**, the fresh one stopping short of it, with the blank cover set as the cover actually reads. |
| B07 | SHOW | Claim: one of five, and four defects with names on them. Five cells, one filled, then four companies each with a defect id. |
| B08 | SHOW | Claim: five numbers and the limit that narrows each — and nobody has checked any of it. The **gate record is drawn as the largest object on the frame**. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## ILLUSTRATE LAW — no two consecutive body beats share a scheme

```
B01  three step cards in a row, the middle one accented — a flow, no chart
B02  a document passage, a copied value, and one highlighted character in each
B03  three bars on an accuracy scale, extras on a SECOND scale past a divider
B04  two value cards side by side, one cited and one bare
B05  a tally in plain figures, then 24 cells, 8 of them filled
B06  two bars under ONE dashed pass line, plus the cover that caused the miss
B07  five report cells, one filled, then four named defects with ids
B08  claim/limit pairs, a boxed gate record, then a next-steps list
```

The two bar beats, **B03 and B06, are deliberately not adjacent**, and they are different
objects: B03's three bars have three different denominators and carry no pass line at all,
because the week's check was a comparison rather than a threshold; B06's two bars share one
threshold that was written down before the run and is drawn through both tracks.

The two cell beats, **B05 and B07, are also not adjacent**, and are different: B05's cells
are 24 identical refusals where only the count matters; B07's five cells each stand for a
named report, and four of them get a name and an id underneath.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B03's
  extras track at `GHOST` 0.9 on a dashed outline, and B05's unfilled refusal cells, which
  are outlined at full border weight
- Comparisons shown side-by-side, held ≥2s ✓ — B03's three bars, B04's two cards, B06's two
  bars under one line and B07's five cells all persist to the end of their beats

## Teaching arc

```
MECHANISM ✓      B01/B02 — how the reader works, and the check that makes it mean anything,
                 worked once on a filing where it caught the model red-handed
MEASUREMENT ✓    B03 — three methods, three denominators, one of them the baseline nobody
                 wanted to run
COMPLICATION ✓   B04 — the measurement does not say what the design expected it to say
EVIDENCE ✓       B05 — what the copy check actually refused, and how much of it was real
FAILURE ✓        B06/B07 — two fresh checks, both of which the project did not pass
LIMITS ✓         B08 — every number above, paired with what narrows it, and the gate record
HANDOFF ✓        B10 — run the dumb baseline before you build the clever thing
```

## SHOW-DON'T-TELL spot checks

- "The model never types a number" is drawn by putting CODE on both sides of it, and by
  making the model's card the only one in the accent.
- "It rewrote the currency sign" is drawn by highlighting the € in the filing and the $ in
  the copy, and nothing else on the frame.
- "The denominators differ" is drawn by printing `135 of 160`, `157 of 167`, `160 of 160`
  beside their own bars.
- "What the reader adds is a cited sentence" is drawn by showing the same number twice, once
  with a passage id and the sentence, once with neither.
- "A refused value is missing, not wrong" is drawn by counting the refusals as cells rather
  than scoring them as errors.
- "Below my line" is drawn by a bar stopping short of a mark that was already on the frame.
- "Nobody has reviewed this" is drawn by making the gate record the largest box on B08.
- B04's left-hand card and B08's gate row are the two places the reel tells rather than
  shows: there is no honest way to *draw* the absence of a provenance record, or the absence
  of a review.

## Known risks carried into QC

1. **B02's highlight depends on the exact string.** `Highlight` marks the first occurrence of
   `passageMark` in `passage`; if either prop is edited and the mark no longer occurs, the
   component falls back to plain text and the beat silently loses its entire argument while
   still rendering a correct-looking frame. The build asserts `€` is in the passage and `$`
   is in the copy. **Read this frame.**
2. **B03 is the widest row in the file** — name, bar, percentage, fraction, divider, extras
   track, extras count. Week 3's B04 clipped every figure in portrait by forgetting that the
   label column stacks above the track in 9:16 while the value columns do not. `BESIDE` is
   computed separately for each orientation here; check at 4K that nothing touches the edge.
3. **B05's 24 cells must stay countable.** At 12 per row in landscape and 8 in portrait they
   form two and three tidy rows; if the cell size changes, a ragged final row makes the count
   look approximate, which is the opposite of the claim.
4. **B06's dashed line sits at 95% of a track whose top bar is full.** On last week's 24 of 24
   the mark falls inside the fill. Check at 4K that the dashes read against the ink.
5. **B07's defect rows carry long "what" strings beside a fixed-width company column.** Check
   they wrap rather than clip, in both orientations.
6. **B08 is the densest beat in the reel** — five claim/limit pairs, a boxed gate record and
   three next steps. It is the most likely to overflow its column and let the Source line draw
   across something. Check the foot of the frame.
7. **Portrait will underfill.** It has every week since week 5. Budget for a rescale pass.
