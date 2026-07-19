# QC REPORT — claude-liam-collage-ads
# "Claude, Collaged." | collage-ads skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Build facts
- Runtime: 225.9s | Beats: 11/11 VIDEO | Audio: Kokoro am_onyx (free)
- Streams: video + audio confirmed (compile.py)

## Frame verification
| Timestamp | Beat | Pattern | Result |
|---|---|---|---|
| 1s | B00 | ClaudeComposerAsk | PASS — "COLLAGE-ADS · SKILL TEARDOWN", "Liam, in for Bear.", "Cześć, Liam", 4 output lines |
| 130s | B05 | SkillTeardownMechanism | PASS — "MECHANISM · ACT 1", "Every attribute independently swappable.", verbatim quote visible |
| 207s | BVDT | ClaudeVerdictArtifact | PASS — "Claude, Collaged.", "COLLAGE-ADS: WHAT IT DELIVERS", 4 lines |
| 223s | BOUT | ClaudeTitleOutro | PASS — "Claude, Collaged." / @NikBearBrown / "Liam, in for Bear." |

## 9-point rubric
1. IN-FOR-BEAR: "Liam, in for Bear." visible at 1s — PASS
2. HELLO: "Cześć, Liam" (Polish) in B00 — PASS
3. ILLUSTRATE LAW: 5 UI (B00, B03, BVDT, BHTF, BOUT) + 6 illustration (B01, B02, B04, B05, B06, B07) — PASS
4. SELF-DEMO: B03/B04 Phase A decode — MORNING BREW coffee ad → collage JSON spec with medium, color_field (#1B4FD8 cobalt), 2 elements (halftone cup + sun), composition, idea, label (burned in at generation) — genuine Phase A, no Arcads MCP calls, no nano-banana-2 spend — PASS
5. VERBATIM QUOTES: "The driving question is: 'If I had to regenerate this exact frame from scratch on nano-banana-2, what would I need to specify?'" (B05), "Labels are burned in at generation, never via arcads_add_text_overlay." (B06), "Consistency across scenes is what makes it read as a brand rather than one-offs." (B07) — all from SKILL.md — PASS
6. MECHANISM × 3: B05 over-analyze mindset + independently swappable fields, B06 labels burned in never overlaid, B07 one-model + lock-look-vary-idea scaling law — PASS
7. HANDOFF: BHTF "./art collage-ads <reference>" with 2 forcing questions (spec field-specific? model decided?) — PASS
8. OUTRO: BOUT "Claude, Collaged." — PASS
9. MINOR-COSMETIC: B04 ClaudeCodeBeat slow-mo 3.7× (10s Remotion stretched to 37.5s narration) — known, non-blocking; sparkLine empty (B00, B03, BHTF) — known, non-blocking

**VERDICT: QC PASS | 0 BLOCKER | 0 MAJOR | 4 MINOR-COSMETIC (B04 slow-mo + sparkLine)**
