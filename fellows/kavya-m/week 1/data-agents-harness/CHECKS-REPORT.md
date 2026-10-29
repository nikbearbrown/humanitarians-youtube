# CHECKS-REPORT — kavya-data-agents-harness

Written before the first compile, per the PROOF GATE in `skills/make/ai-explainer/SKILL.md`.

7 SHOW / 2 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Why |
|---|---|---|
| B00 | SHOW | Composer types the ask; output lines answer it (ASK→RESULT starts at the cold open) |
| B01 | SHOW | Hesitant writer strikes "a bigger model" and types "a better harness" |
| B02 | SHOW | Four parts light in narration order between QUESTION and CHECKED ANSWER |
| B03 | SHOW | Real terminal run; the wrong answer and `checks run: 0` print as they're spoken |
| B04 | SHOW | Real terminal run; CHECK FAILED prints, then the passing retry |
| B05 | SHOW | Left zone checks in, divider draws, right zone (the limits) appears |
| B06 | HOLD | Verdict artifact page; bookend, the spoken lines are on screen |
| B07 | SHOW | Handoff prompt types into the composer and is read aloud |
| B08 | HOLD | Credit card with the AI-voice disclosure; bookend |

Teaching arc: FRAMEWORK ✓ (B02) | WORKED EXAMPLE ✓ (B03–B04) | FALSIFIABILITY ✓ (B05)
              SCAFFOLDED TASK ✓ (B07) | BOOKENDS ✓ (B00, B01, B07, B08) | NO-SOURCE-NO-VERDICT ✓ (verdict rests on the demo output, `FACTCHECK.md`)

Known deviation: OUTRO LAW wants `ClaudeTitleOutro`, but that component hardcodes `@NikBearBrown`.
Using it would credit this fellow's film to another channel, so B08 uses `ClaudeVerdictArtifact`.
