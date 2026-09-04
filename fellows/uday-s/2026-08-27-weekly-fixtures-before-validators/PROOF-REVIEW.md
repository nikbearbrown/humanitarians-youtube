# PROOF self-review — "Build the Defects First"

Scored against `brutalist.art/PROOF.md`. This is the creator's own scoring, run
before asking anyone else to watch — which is the point of having a rubric.
Frames were inspected at the moment of each claim; nothing here is scored from
the beat sheet alone.

**Verdict:** meets PROOF's ship bar on teaching and passes the production gate.
Publication is still a human decision — this toolkit ships nothing.

## Rubric

| Criterion | What it means | This cut | Score |
|---|---|---|---|
| **Explicit framework** | Organizing idea shown as a structure *before* the examples | B02 — four method cards (ENUMERATE / PLANT / NAME THE CATCHER / FREEZE), on screen at **19.05s**, ahead of the first example at 31.20s | **2** |
| **Reusable rubric** | A viewer could apply the axes to a new case without guessing | The four steps are stated as operations on *any* validator suite, not on market data. B11 hands the viewer the same four to run | **2** |
| **Worked example** | One case walked through the framework live — the reasoning, not the conclusion | B04 — D05 walked through step 3: different id, different url, identical headline, therefore an id-only dedupe misses it and inflates the denominator | **2** |
| **Falsifiability / edge case** | The framework stress-tested against a case that breaks it | B09 — wrong-entity signals. Named as breaking **step 1 specifically** (you cannot enumerate a class that isn't a shape), and quoted from the manifest's own `not_covered`, not invented for the video | **2** |
| **Active task** | CTA requires structured doing — never "ask Claude" | B11 — a copyable prompt, plus the discriminator: GOOD = a fixture and line for every check; BAD = "all tests pass" | **2** |
| **Friction** | The viewer must resolve a tension, not just receive facts | B09 creates the real moment — a row passes all four checks and is still wrong. But most of the runtime delivers conclusions rather than making the viewer sit in ambiguity. Honest score, not a generous one | **1** |

**Teaching: 11 / 12.** Ship bar is ≥ 8.

## Production gate (binary — can veto regardless of teaching score)

| Check | Verdict | Evidence |
|---|---|---|
| **Evidence legible at the moment of assertion** | PASS | GATE B (pixel-true) clean on all six Manim scenes; GATE W clean on contrast/margins/overlap. Frames inspected at 33s, 128s, 148s, 164s, 175s. No element below the ~40% opacity floor, no clipped labels |
| **Sources on screen, not just voiced** | PASS | Every Manim beat names its source file in the kicker (`recipes/…part-1.md`, `sample/fixture-manifest.json`, `fixture-manifest.json → not_covered`, `mycroft · commit 9ef4e7f`). Both CODE beats show the artifact itself, verbatim |
| **Side-by-side at the moment of comparison** | PASS | B09 holds the four passing checks and the failing verdict on screen together for the remainder of the beat — the comparison is visible while it is asserted, not stated once and gone |

## Where this cut improved on the previous one

| Criterion | Cut 1 | Cut 2 |
|---|---|---|
| Explicit framework | **0** — a principle narrated in B01, no structure on screen. PROOF's own words for this: "That's not a framework yet — it's a slogan" | **2** — B02, shown before any example |
| Reusable rubric | 1 — implied, never stated as axes | **2** — four named steps, referenced by number in five later beats |
| Active task | 1 — a prompt, but no way to tell a good answer from a bad one | **2** — GOOD/BAD discriminator stated on screen and aloud |

## Honest limitations

- **Friction is the weak criterion**, scored 1. A three-minute work report is
  mostly delivery. Raising it would mean posing the wrong-entity case as a
  question the viewer answers before the reveal — a real structural change,
  not a polish pass. Logged for next week rather than claimed as done.
- **`underfill` findings remain** (48 frames of 364, ~13%). All are build-in
  ramps where a staggered reveal has not yet filled the canvas, plus the
  deliberately sparse outro card. Documented in BUILD-LOG.md; not silenced.
- **The composer chrome shows a model name.** That is the house Remotion
  component's own UI, not a claim the reel makes, but it does date the video —
  the DOUBLE-CHECK LAW's concern. Flagged for the component, not fixable from
  the beat sheet.
- **No accuracy claim appears anywhere**, because none exists. `logs/RUN_LOG.md`
  records that no accuracy rate has been established for this system and that
  none may be quoted. PROOF's "no source, no verdict" applied to itself.
