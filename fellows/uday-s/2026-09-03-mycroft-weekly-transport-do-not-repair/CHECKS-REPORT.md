# CHECKS-REPORT — Transport, Do Not Repair

Written before the first slate compiled, per the PROOF GATE.

**13 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, week's ask answered; name spoken |
| B01 | PROBLEM | SHOW | last week's open ledger, two rows closing (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards: DECIDES / REFUSES / EVIDENCE (Manim) |
| B03 | CLI | SHOW | composer, step-2 ask |
| B04 | CODE | SHOW | the TRANSPORT, DO NOT REPAIR docstring, verbatim |
| B05 | OUTPUT | SHOW | step 2 scored on the three axes (Manim) |
| B06 | CLI | SHOW | composer, step-3 ask |
| B07 | CODE | SHOW | the SCOPE docstring, verbatim |
| B08 | OUTPUT | SHOW | live run: clean vs defective, 4/3/1, exit 1 (Manim) |
| B09 | FALSIFIABILITY | SHOW | one file, two line endings, two real digests (Manim) |
| B10 | SUMMARY | SHOW | closed / still-open ledger (Manim) |
| B11 | NEXT STEPS | SHOW | composer, scaffolded prompt + GOOD/BAD test |
| B12 | OUTRO | SHOW | title-restate card, name in subline |

## Teaching arc

```
FRAMEWORK ✓        B02 — three questions shown AS A STRUCTURE at 20.16s,
                   ahead of step 2 at 47.10s.
WORKED EXAMPLE ✓   B04→B05 and B07→B08 — both steps scored on the same
                   three axes, the reasoning shown, not just the verdict.
FALSIFIABILITY ✓   B09 — axis 3 broken in practice. The framework predicts
                   it: "evidence a reviewer can re-check" fails if the
                   digest moves with the platform. Real bug, real digests.
SCAFFOLDED TASK ✓  B11 — question two turned on the viewer's own code, with
                   a GOOD/BAD discriminator; read aloud per HANDOFF LAW.
BOOKENDS ✓         B00 cold open · B11 "Your turn." · B12 title restate.
NO-SOURCE-NO-VERDICT ✓  Both CODE beats are verbatim source. Every count in
                   B08 is from a live run. B09's digests are recomputed, not
                   invented. See FACTCHECK.md (14 rows).
```

## Notes

- **REVISION LAW satisfied**: two full CLI→CODE→OUTPUT cycles (B03–B05, B06–B08),
  and they are genuinely opposite jobs — one refuses to judge, one judges.
- **ACTUAL-CODE LAW satisfied**: B04 and B07 are copied from the scripts, not retyped.
- The six Manim beats were a GATE L library miss and are authored as data
  animations, not slated. Searches logged to the toolkit's TEMPLATE-MISSES.md.
