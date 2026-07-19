# AUDIT — preserve-cognitive-demand-differentiation (oPI3c6pf1N4)
Batch: 2026-07-18. claude-explainer compliance rebuild.

## Beat sheet summary
- B00: ClaudeComposerAsk (cold open) ✓
- B01: ClaudeWindow — shows Claude UI in use
- B02: K12Fig scene (figure)
- B03–B05: K12Fig scenes
- YTV01: ClaudeVerdictArtifact ✓ (position after B00)
- B06: handoff ClaudeComposerAsk ✓
- B07: ClaudeTitleOutro ✓

## Violations

| beat | law violated | fix |
|------|-------------|-----|
| B02–B05 (K12Fig) | LOGO LAW — K12Fig Remotion components lack @NikBearBrown corner watermark | Add NBB watermark to K12Fig component source files (K12Fig01–K12Fig12 in src/scenes/) |
| B01 (ClaudeWindow) | ILLUSTRATE LAW check — ClaudeWindow is appropriate only when UI is the subject | PASS: this beat narrates "giving Claude context" — UI is the subject ✓ |

## Notes
- Structural laws all pass: ORDER, COLD-OPEN, HANDOFF, OUTRO
- Voice: kokoro am_onyx — audio untouched
- Existing mp4 backed up as preserve-cognitive-demand-differentiation-pre-rebuild.mp4
- K12Fig scenes are Remotion comps — fix by editing src/scenes/K12Fig*.tsx to add watermark

## Status
AUDIT COMPLETE — fix: LOGO LAW on K12Fig beats
