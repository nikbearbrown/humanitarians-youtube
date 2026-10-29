# CHECKS-REPORT — kavya-opentelemetry-ai-agents

Written before the first compile, per the PROOF GATE in `skills/make/ai-explainer/SKILL.md`.

7 SHOW / 2 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Why |
|---|---|---|
| B00 | SHOW | Composer types the ask; the output lines answer it with the demo's real results |
| B01 | SHOW | Hesitant writer strikes "just more logging" and types "the agent's flight recorder" |
| B02 | SHOW | Four trace parts appear as each is named, between AGENT RUN and ANY BACKEND |
| B03 | SHOW | Real terminal run; the plain log prints line by line, ending on "not recorded" |
| B04 | SHOW | Real terminal run; the span tree prints span by span, with the 0-hit search highlighted |
| B05 | SHOW | Limits appear first, then the demo caveat, then what tracing shows |
| B06 | HOLD | Verdict page; bookend, the spoken lines are on screen |
| B07 | SHOW | Handoff prompt types into the composer and is read aloud |
| B08 | HOLD | Credit card with the AI-voice disclosure; bookend |

Teaching arc: FRAMEWORK ✓ (B02) | WORKED EXAMPLE ✓ (B03–B04) | FALSIFIABILITY ✓ (B05)
              SCAFFOLDED TASK ✓ (B07) | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓ (verdict rests on demo output, `FACTCHECK.md`)

Known deviation: OUTRO LAW wants `ClaudeTitleOutro`, which hardcodes `@NikBearBrown`, so B08 uses `ClaudeVerdictArtifact`.
