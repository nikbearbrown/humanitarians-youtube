# CHECKS-REPORT.md — accountability-mesh (Expanded)

Written before the first slate compile, per PROOF GATE (ai-explainer SKILL.md).

## Per-beat classification (SHOW / HOLD / CARD — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; UI is the subject |
| B01 | SHOW | B01_TheMesh (Manim) | Names a structural claim (agent → gate → investor with three properties) — animated diagram |
| B02 | SHOW | B02_NakedConclusion (Manim) | Names a failure mode (unchecked hallucinated number flowing into grade) — animated diagram |
| B03 | SHOW | B03_RejectedApproaches (Manim) | Names a comparison (two rejected approaches) — drawn table, nopunt "comparison/leaderboard" row |
| B04 | SHOW | B04_ThreeMechanisms (Manim) | Names a structure (three mechanisms with definitions) — labeled node panel, "panel of N things" |
| B05 | SHOW | B05_ValidationLoop (Manim) | Names a mechanism + worked example (ADR-11 directive failure, polite → mechanical, halt) — animated diagram |
| B06 | SHOW | B06_TheHonestLimit (Manim) | Names the falsifiability claim (ADR-06, fabricated log passes checks) — text card held on screen |
| B07 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps on-screen, no new claim |
| B08 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed and read aloud with rubric |
| B09 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate |

**N SHOW / N justified-HOLD / N PUNT-flagged: 10 SHOW / 0 HOLD / 0 PUNT**

No beat requires archival photographs. Every claim is a structural mechanism,
a comparison, or a named failure mode — all animatable per nopunt SKILL.md.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 states the whole idea (the mesh sits between agent
  and human, enforces structure not accuracy). B04 additionally frames the
  three mechanisms before B05's worked example uses them.
- [x] **WORKED EXAMPLE** — B05 walks the ADR-11 directive failure (polite request
  breaks, mechanical fix works, halt on failure #2) through the validation-loop
  mechanism, visibly using the framework.
- [x] **FALSIFIABILITY / edge-case beat** — B06 is the dedicated stress-test:
  a fabricated log passes every structural check. Full beat, not a caveat.
- [x] **SCAFFOLDED viewer task** — B08 prompt ("Design a validation directive
  that fails loudly") ships with a 3-item rubric (logs failures / retries tracked /
  halts on failure #2) the viewer can check their output against.
- [x] **Four bookends** — B00 (cold open), B07 (verdict), B08 (Your Turn), B09 (outro).
- [x] **No source, no verdict** — every factual/structural beat (B01–B06) carries
  its claim on screen (the gate diagram, the funnel, the three-row table, the
  mechanism panel, the attempt sequence, the ADR-06 card) rather than only in
  narration. B07 (verdict) and B08 (Your Turn) are exempt (they recapitulate).

## Reading level check

- **Narration language:** Simpler words (hallucinated → made up, append-only
  explained on first use, fabricated not invented), shorter sentences, one idea
  per sentence. Suitable for high school to early college reader.
- **Explanation density:** Each mechanism is defined in the same beat it's named
  (B04 doesn't assume prior knowledge). Concepts introduced before use.
- **Concrete examples:** Four-agent company analysis (B02), polite vs. mechanical
  directive (B05), all grounded in specifics, not abstractions.

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact in `shot.manim.scene_class` or
`shot.remotion.pattern`; Manim scenes hold ~15–35% negative space (title at
top, single diagram centered); un-highlighted elements stay at INK/SOFT;
B03's three-row comparison and B04's three-node panel each hold their full
set on screen simultaneously.

## Status

Beat sheet, audio files, and this checks report are authored and internally
consistent. `scenes.py` (Manim scene source) is the next step — this pass
closes the PROOF GATE for authoring.
