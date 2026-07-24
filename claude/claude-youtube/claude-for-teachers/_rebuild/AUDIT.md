# AUDIT — claude-for-teachers (-WCwbxmraIA)
Batch: 2026-07-18. claude-explainer compliance rebuild.

## Beat sheet summary
- B00: ClaudeComposerAsk — greeting="Your turn." (VIOLATION)
- B01: TeachersLayerStack pattern (UNREGISTERED in Root.tsx)
- B02: StandardsToCowork pattern (UNREGISTERED)
- B03: ConnectorGrid pattern (UNREGISTERED)
- B04: CoworkScheduleBeat pattern (UNREGISTERED)
- B05: PredictCard pattern (UNREGISTERED)
- B06: handoff ClaudeComposerAsk ✓
- B07: ClaudeTitleOutro ✓

## Violations

| beat | law violated | fix |
|------|-------------|-----|
| B00 | COLD-OPEN LAW — greeting="Your turn." reserved for handoff | Change greeting to world-language hello, e.g. "Salut, Kore" |
| B00 | IN-FOR-BEAR LAW — narration lacks "in for Humanitarians AI" phrase | Update narration_text; regen Kokoro audio |
| B01–B05 | LOGO LAW — unregistered patterns cannot render; will use PNG fallback from media/ | PNGs exist; compile.py will animate them with pan/zoom. Acceptable for now. |

## Notes
- B01–B05 patterns (TeachersLayerStack, StandardsToCowork, ConnectorGrid, CoworkScheduleBeat, PredictCard) are NOT registered as Remotion compositions in Root.tsx
- media/ contains PNG frames for these beats — compile.py will use PNG→animated fallback
- Registering these in Root.tsx would be ideal but is a large scope change; PNG fallback is acceptable for this compliance batch
- The PNGs do NOT have the NBB corner watermark (LOGO LAW) — this is a known limitation of PNG fallback

## Actions required
1. Edit beat_sheet.json: B00 greeting → world-language hello
2. Edit beat_sheet.json: B00 narration_text → integrate "in for Humanitarians AI"; regen Kokoro
3. Render B00, B06, B07 via remotion_scenes.py (ClaudeComposerAsk, ClaudeTitleOutro patterns)
4. Compile master via compile.py (B01–B05 use PNG fallback from media/)
5. Flag: LOGO LAW on B01–B05 PNGs — no corner bug possible without Remotion registration

## Status
AUDIT COMPLETE — VIOLATIONS FOUND: COLD-OPEN, IN-FOR-BEAR; LOGO LAW flagged (PNG fallback limitation)
