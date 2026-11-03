# CHECKS-REPORT — Passing For The Wrong Reason

Written before the first slate compiled, per the PROOF GATE.

**13 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

Every beat names its on-screen artifact. Both OUTPUT beats are motion.

## Teaching arc

```
FRAMEWORK ✓        B02 — WHAT MAKES IT FAIL / HAS IT EVER FAILED / WHY IS IT
                   PASSING NOW, shown AS A STRUCTURE at 26.88s, ahead of the
                   first gate at 52.43s. The third question is new to the
                   series and is what the episode is about.
WORKED EXAMPLE ✓   B04→B05 (the old gate, run live) and B07→B08 (the new gate,
                   break-tested). Same rubric, before and after.
FALSIFIABILITY ✓   B09 — question 3 answered against the fix itself. The gate
                   still passes, and it passes because the failing condition
                   is unreachable. Capable of working is not working.
SCAFFOLDED TASK ✓  B11 — question 3 turned on the viewer's own green check,
                   with a GOOD/BAD discriminator; read aloud per HANDOFF LAW.
BOOKENDS ✓         B00 cold open · B11 "Your turn." · B12 title restate.
NO-SOURCE-NO-VERDICT ✓  Both CODE beats are verbatim recipe lines, one from
                   the previous commit and one from this one. Every result in
                   B05, B08 and B09 came from running a test live.
                   FACTCHECK.md carries 14 rows.
```

## Series continuity

Episode 5 is the first one where the series' own output changed the subject.
Episode 4 ended with a task for the viewer; this commit runs that task on the
repo and fixes what it found. B01 puts the previous episode's question on
screen before anything else, and B10 closes three loops the series logged
rather than hid — step 3's missing type field (episode 3), the report Reader
mismatch (episode 4), and the vacuous gates (episode 4).

## Notes

- **REVISION LAW satisfied**: two CLI→CODE→OUTPUT cycles (B03–B05, B06–B08).
- **ACTUAL-CODE LAW satisfied**: both CODE beats are real recipe lines.
- The six Manim beats were a GATE L library miss and are authored as data
  animations, not slated.
- The break test ran in a scratch tree; the subject repo was never written to.
