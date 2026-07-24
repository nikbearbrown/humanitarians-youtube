# QC REPORT — claude-liam-claude-api
Date: 2026-07-18
Auditor: automated visual QC

## File
- Path: `claude-liam-claude-api.mp4`
- Duration: 171.2s (2:51)
- Resolution: 1280×720
- Codec: H264 + AAC
- Streams: 2 (video + audio)
- Size: ~2.7MB

## Beat-by-beat

| Beat | Scene | Duration | Canvas Fill | Issues |
|------|-------|----------|-------------|--------|
| B00 | ClaudeComposerAsk | 15.0s | Good | None |
| B01 | ClaudeApiAnatomy | 21.0s | ~65% | MINOR: lower canvas open |
| B02 | ClaudeApiSurfaces | 22.1s | ~85% | None |
| B03 | ClaudeApiDrift | 26.5s | ~90% | None |
| B04 | ClaudeApiModels | 24.6s | ~88% | None |
| B05 | ClaudeApiTell | 24.8s | ~65% | MINOR: lower canvas open below columns |
| BVDT | ClaudeVerdictArtifact | 16.6s | Good | None |
| BHTF | ClaudeComposerAsk | 17.6s | Good | None |
| BOUT | ClaudeTitleOutro | 2.9s | Good | None |

## 9-point rubric
1. **Palette** — PASS: CLAUDE.PAGE cream, CLAUDE.INK dark, CLAUDE.SPARK terracotta throughout
2. **Typography** — PASS: SERIF headings, MONO code/IDs, SANS UI labels
3. **TRIGGER / greeting** — PASS: "Bonjour, Liam" in B00, IN-FOR-BEAR law satisfied
4. **Content accuracy** — PASS: drift table, model IDs, and pricing verbatim from SKILL.md
5. **SELF-DEMO** — PASS: B03 drift table and B04 model table are SKILL.md data, not paraphrase
6. **Verbatim quotes** — PASS: TRIGGER text, drift rows, "non-negotiable" rule exact
7. **Verdict props** — PASS: `artifactTitle`/`artifactHeading`/`artifactLines` (not title/lines)
8. **Canvas fill** — B01 and B05 have ~35% lower open space (MINOR, consistent with teardown pattern)
9. **Audio sync** — PASS: all 9 beats present, Kokoro am_onyx, $0.00 cost

## BLOCKERs: 0
## MAJORs: 0
## MINORs: 2
- B01 lower canvas: ~35% open space below language chips (same accepted pattern as brand-guidelines/canvas-design)
- B05 lower canvas: ~35% open space below two columns (same accepted pattern)

## VERDICT: PASS
