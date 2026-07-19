# QC REPORT — claude-liam-doc-coauthoring
Date: 2026-07-18
Auditor: automated visual QC

## File
- Path: `claude-liam-doc-coauthoring.mp4`
- Duration: 197.7s (3:18)
- Resolution: 1280×720
- Codec: H264 + AAC
- Streams: 2 (video + audio)

## Beat-by-beat

| Beat | Scene | Duration | Canvas Fill | Issues |
|------|-------|----------|-------------|--------|
| B00 | ClaudeComposerAsk | 18.7s | Good | None |
| B01 | DocCoauthoringAnatomy | 25.9s | ~60% | MINOR: lower canvas open |
| B02 | DocCoauthoringStage1 | 28.2s | ~55% | MINOR: lower canvas open |
| B03 | DocCoauthoringStage2 | 30.1s | ~80% | Fixed (STEP_H increased to H*0.52) |
| B04 | DocCoauthoringStage3 | 26.4s | ~75% | MINOR: gap between columns and exit bar |
| B05 | DocCoauthoringTell | 28.5s | ~55% | MINOR: lower canvas open below columns |
| BVDT | ClaudeVerdictArtifact | 18.7s | Good | None |
| BHTF | ClaudeComposerAsk | 18.1s | Good | None |
| BOUT | ClaudeTitleOutro | 3.0s | Good | None |

## 9-point rubric
1. **Palette** — PASS: CLAUDE.PAGE cream, CLAUDE.INK dark, CLAUDE.SPARK terracotta throughout
2. **Typography** — PASS: SERIF headings, MONO code, SANS UI labels
3. **TRIGGER / greeting** — PASS: "Guten Tag, Liam" in B00, IN-FOR-BEAR law satisfied
4. **Content accuracy** — PASS: 3 stages, 5 meta questions, 6-step section loop, exit conditions from SKILL.md
5. **SELF-DEMO** — PASS: B03 6-step loop verbatim from SKILL.md § Stage 2
6. **Verbatim quotes** — PASS: exit conditions and quality gate text exact from SKILL.md
7. **Verdict props** — PASS: `artifactTitle`/`artifactHeading`/`artifactLines` (not title/lines)
8. **Canvas fill** — B03 fixed (STEP_H increased). B01/B02/B05 have lower canvas open (MINOR)
9. **Audio sync** — PASS: 9 beats, Kokoro am_onyx, $0.00

## Fix applied
- B03 (DocCoauthoringStage2): STEP_H increased from H*0.35 to H*0.52 to eliminate dead zone between step cards and quality boxes. Re-rendered before final compile.

## BLOCKERs: 0
## MAJORs: 0 (B03 fixed before final)
## MINORs: 4
- B01 lower canvas: ~35% open (teardown pattern)
- B02 lower canvas: ~40% open (teardown pattern)
- B04 middle gap: ~20% between columns and exit bar
- B05 lower canvas: ~40% open (teardown pattern)

## VERDICT: PASS
