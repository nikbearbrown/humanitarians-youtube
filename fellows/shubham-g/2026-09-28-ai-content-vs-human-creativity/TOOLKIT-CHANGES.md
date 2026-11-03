# TOOLKIT-CHANGES — local patches to brutalist.art used for this build

New files (copies in `scenes/`):
- `runtime/remotion/src/scenes/ContentRepurpose.tsx` — RepurposeSource, RepurposeClips, RepurposeCascade, RepurposeVoiceCheck, CreativityBalance (16:9), plus shared Glyph / Phone / DraftBody helpers.
- `runtime/remotion/src/scenes/ContentRepurpose916.tsx` — native 9:16 versions (serif ≥ 90 / sans ≥ 76 px).

Edits to existing toolkit files (not copied here):
- `Root.tsx` — import both files and register each scene as `<Name>` (1920×1080) and `<Name>916` (1080×1920) in a `ContentRepurpose` folder, with `calculateMetadata` from `durationSeconds`.
- `runtime/remotion/src/scenes.json` — regenerated with `./art scene-index`.

Relies on the earlier patches listed in `../2026-09-26-social-ai-brand-visibility/TOOLKIT-CHANGES.md`
(Windows fixes, `claude-shubh` brand label, `HandleTitleOutro`, `SocialAiVisibility.tsx` helpers).
