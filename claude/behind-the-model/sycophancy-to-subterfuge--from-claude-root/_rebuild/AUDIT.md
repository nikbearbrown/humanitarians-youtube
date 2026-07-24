# AUDIT — sycophancy-to-subterfuge (Dm8-lZ-Y0ZE)
Batch: 2026-07-18. claude-explainer compliance rebuild.

## Beat sheet summary
- B00: ClaudeComposerAsk — greeting="Your turn." (VIOLATION)
- B01–BN: body beats (media/ empty — no renders exist)
- Handoff beat: ClaudeComposerAsk ✓
- Outro: ClaudeTitleOutro ✓

## Violations

| beat | law violated | fix |
|------|-------------|-----|
| B00 | COLD-OPEN LAW — greeting prop is "Your turn." (reserved for handoff) | Change greeting prop to world-language hello, e.g. "Konnichiwa, Kore" |
| B00 | IN-FOR-BEAR LAW — B00 narration does not introduce Kore "in for Humanitarians AI" | Update narration_text to include "Kore, in for Humanitarians AI" phrase; regen Kokoro audio |

## Actions required
1. Edit beat_sheet.json: B00 greeting → world-language hello
2. Edit beat_sheet.json: B00 narration_text → integrate "in for Humanitarians AI" phrase
3. Regen Kokoro audio for B00 (free, af_kore)
4. Render ALL beats via remotion_scenes.py (media/ is empty)
5. Compile master via compile.py

## Status
AUDIT COMPLETE — VIOLATIONS FOUND: COLD-OPEN, IN-FOR-BEAR
