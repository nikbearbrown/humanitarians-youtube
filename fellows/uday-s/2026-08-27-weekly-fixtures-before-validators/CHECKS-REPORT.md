# CHECKS-REPORT — weekly-fixtures-before-validators

Written before the first slate compiled, per the cli-explainer PROOF GATE.
Revised for the 13-beat cut (framework beat added, male voice, name in intro).

**13 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

Every beat names its on-screen artifact in `shot.show` (Remotion) or
`shot.visual_intent` (Manim). Both OUTPUT beats are motion, per the spine's
never-a-still rule. No beat is a bare CARD.

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, opening ask answered; name spoken |
| B01 | PROBLEM | SHOW | six `[TODO: DEV]` rows + empty ledger (Manim) |
| B02 | FRAMEWORK | SHOW | four method cards — the reusable rubric (Manim) |
| B03 | CLI | SHOW | composer, fixture-corpus ask |
| B04 | CODE | SHOW | `fixture-manifest.json` D05 record, verbatim |
| B05 | OUTPUT | SHOW | 18 chips into 7 class rows (Manim) |
| B06 | CLI | SHOW | composer, step-1 revision ask |
| B07 | CODE | SHOW | `verify-provenance.py` digest_basis, verbatim |
| B08 | OUTPUT | SHOW | 14 source rows resolving + tally bar (Manim) |
| B09 | FALSIFIABILITY | SHOW | clean row vs wrong-entity verdict, side by side (Manim) |
| B10 | SUMMARY | SHOW | shipped/still-open ledger (Manim) |
| B11 | NEXT STEPS | SHOW | composer, scaffolded prompt + GOOD/BAD test |
| B12 | OUTRO | SHOW | title-restate card, name in subline |

## Teaching arc

```
FRAMEWORK ✓        B02 — the four-step method shown AS A STRUCTURE at 19.05s,
                   ahead of the first example (B03). This is new in this cut;
                   the previous cut only stated a principle in narration.
WORKED EXAMPLE ✓   B04 → B05 — method step 3 walked through on the real D05
                   record, then the full catalogue it belongs to.
FALSIFIABILITY ✓   B09 — the wrong-entity class, which breaks method step 1
                   specifically, quoted from the manifest's not_covered.
SCAFFOLDED TASK ✓  B11 — a copyable prompt plus what a GOOD and a BAD answer
                   look like; read aloud, per HANDOFF LAW.
BOOKENDS ✓         B00 cold open (name spoken) · B11 "Your turn." ·
                   B12 title restate. Channel @HumanitariansAI.
NO-SOURCE-NO-VERDICT ✓  Every on-screen number traces to commit 9ef4e7f or a
                   live run — see SOURCES.md / FACTCHECK.md. Every Manim beat
                   names its source file in the kicker, so the receipt is on
                   screen at the moment of the claim.
```

## Notes

- **REVISION LAW satisfied**: two full CLI→CODE→OUTPUT cycles (B03–B05, B06–B08).
- **ACTUAL-CODE LAW satisfied**: B04 and B07 show real source, copied not retyped.
- The six Manim beats were a genuine GATE L library miss and are authored as
  data animations (output-beat option 1), not slated.
