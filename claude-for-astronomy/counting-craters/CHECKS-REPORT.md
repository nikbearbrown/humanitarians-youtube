# CHECKS-REPORT — Ep. 18, *counting-craters*

Written **before the first slate compiles**, per the PROOF GATE.

---

## Beat classification

```
14 SHOW / 0 justified-HOLD / 0 PUNT-flagged
```

Every beat names its on-screen artifact in `shot.show`. No beat is a bare
CARD; no beat makes a factual claim the viewer cannot see being made.

| beat | class | the artifact it names |
|---|---|---|
| B00 | SHOW | composer types the ask; three output lines land in order |
| B01 | SHOW | name card; a card splits down a centre rule, halves fill |
| B02 | SHOW | three lines type on, the third underlined in the accent |
| B03 | SHOW | `surface.png`; two counters run to 14 and 80 |
| B04 | SHOW | `pile.png`; three rows label against decade rails |
| B05 | SHOW | `spread.png`; ±45% lands, legend teaches filled vs open |
| B06 | SHOW | two bars grow to 92% and 57%; 42% lands in the accent |
| B07 | SHOW | `curve.png`; two brackets mark flat middle and steep end |
| B08 | SHOW | `cost.png`; the two relative bars are called out in turn |
| B09 | SHOW | `anchors.png`; the empty middle is labelled, then filled |
| B10 | SHOW | a wide bar COLLAPSES to a tick; the counterweight types in |
| B11 | SHOW | artifact page; five lines land in order |
| B12 | SHOW | the prompt types itself while the voice reads it aloud |
| B13 | SHOW | title restates poster-style, handle and subline land |

**The PPT test.** No beat is exportable as a static slide. The two that came
closest were B06 (two numbers) and B10 (type only); both were authored as
motion that *enacts* the sentence — bars that grow to their spoken value, and
a bar that collapses to a tick on the spoken contrast.

## Teaching arc

```
FRAMEWORK ✓   WORKED EXAMPLE ✓   FALSIFIABILITY ✓
SCAFFOLDED TASK ✓   BOOKENDS ✓   NO-SOURCE-NO-VERDICT ✓
```

- **FRAMEWORK before examples** — B02 states the whole idea in one breath
  (count → curve → rock) before any specific lands. B03 is the first exhibit.
- **WORKED EXAMPLE** — B08 is the episode worked end to end: take the
  published ±45%, push it through the published chronology function, read the
  age error back out, twice, at two ages.
- **FALSIFIABILITY** — B10 ships the attack on the episode's own headline: the
  Chang'e-5 recalibration moved the curve by at most 0.24 Gyr, and the rock's
  answer landed *inside* the counted window. The narration says "not wrong,
  just loose" because the evidence says that and not something stronger.
  B06 does the same at beat scale, placing the raw 57% recall beside the 92%.
- **SCAFFOLDED TASK** — B12's prompt applies the lesson to the viewer's own
  work (separate the measured from the calibrated-against) and the narration
  reads it aloud, then says what to look for in the answer.
- **BOOKENDS** — cold open (B00) → BLUF (B02) → body → verdict (B11) →
  handoff (B12) → title outro (B13).
- **NO-SOURCE-NO-VERDICT** — every verdict line in B11 traces to FACTCHECK.

## Laws checked at authoring time

| law | state |
|---|---|
| COLD OPEN | B00 is `ClaudeComposerAsk` with its result lines ✓ |
| EXECUTIVE-SUMMARY (Beat 2 = BLUF) | B02, plain language, states the gist, spends no reveals ✓ |
| ILLUSTRATE | the Claude UI appears only at B00, B11, B12, B13. Ten inner beats illustrate ✓ |
| SHOW-DON'T-TELL | every beat carries a `show` block authored before its narration ✓ |
| NARRATION BUDGET | body beats 27–38 words; bookends exempt ✓ |
| HANDOFF | B12's prompt is read aloud verbatim and discussed ✓ |
| OUTRO | B13 restates the episode title ✓ |
| LOGO | `@HumanitariansAI` chip on B00/B12 (set explicitly), corner bug on every Manim beat ✓ |
| ACCENT | one terracotta moment per beat ✓ |
| DOODLE-BANNED | none emitted ✓ |
| REBUILD | no screenshots, no lifted figures; six generated plates ✓ |
| DOUBLE-CHECK | 7 corrections logged in SOURCES ✓ |

## Runtime

```
417 words
x 0.3744 s/word (Ep. 17 measured: 159.49 s / 426 w)   = 156.1 s  (2:36.1)
worst observed model error across Ep. 06-17, +10.4%   = 172.4 s  (2:52.4)
ceiling                                                 180.0 s  (3:00)
```

Under the ceiling in the worst observed case. Measured MP3 durations replace
this estimate entirely at the audio stage — the estimate is a planning tool,
never the clock.

## Spend

```
$0.00
```

Kokoro `af_bella` local · Manim CE · Remotion · PIL. No key is read by any
step in this build. Fellow Tier throughout.

---

## STOP

**GATE P binds here.** `PEDAGOGY.md` is signed (Om Mali, 11/20/2026, on the
human's explicit written instruction in the build request). Audio generation
follows.

---

# Post-GATE-P — what ran after the signature

| stage | result |
|---|---|
| Audio (Kokoro `af_bella`) | 14 beats, **159.75 s** measured · $0.00 |
| Runtime prediction | 417 w × 0.3744 = 156.1 s; actual 159.75 s (**+2.3%**) |
| Pacing solve | RT 1.550 (capped) / HOLD 0.148–0.719; mean tail 0.45 s |
| `RT_PORTRAIT` | **none needed** — every scene plays identical reveals in both aspects |
| GATE A | 10/10 clean |
| GATE W | 10/10 clean |
| GATE B (`--curve-strict`) | **20/20 clean**, both aspects — after 5 portrait fixes |
| Remotion prop audit | 4 beats × 2 aspects, 0 unknown props |
| compile 16:9 | 14/14 slots, no slates → 3840×2160 |
| compile 9:16 | 14/14 slots, no slates → 2160×3840 |
| GATE V | 0 BLOCKER both cuts (1 MAJOR 16:9, 2 MAJOR 9:16 — measured) |

## Where the gates were right, and where they were not

**Right, and expensive to ignore:** portrait GATE B failed **5 of 10 scenes**
on the first pass — a numeral on a plate frame, a note on a row label, a
caption off the right edge at x = 2.10 on a ±1.80 frame, and two outright
text-on-text collisions at 29% and 73% overlap. Landscape had passed 10/10.
A layout is two layouts.

**Wrong, and measured rather than argued:**

- *16:9, B08_50 `low-contrast`.* GATE V averages every non-background pixel
  into one ink colour, so a pale plate drags it. Swept at eight points, the
  type runs **6.9:1 to 10.7:1** WCAG against a 4.5:1 floor, with 79–90% of the
  averaged "ink" being plate. The flagged frame is additionally caught
  **mid-fade** — the `90%` numeral is at partial opacity as it reveals.
- *9:16, B11 `underfill` 54% vs 55%.* The `916` card reserves 13.5% top and
  12.5% bottom for platform UI by design; measured, it occupies **64.2% of
  the frame**. GATE V's reference box is 16:9-derived.

**Missed entirely, found by reading frames:** two landscape collisions that
passed GATE B 20/20 strict — `175x tighter` printed through the counterweight
line on B10, and the `42%` numeral touching the caption above it on B06.
Both are recorded with their root causes in `VISUAL-QC.md`.

**Nothing was passed with `--lenient`.**
