# TOOLKIT-CHANGES — local patches to brutalist.art used for this build

New files (copies in `scenes/`):
- `runtime/remotion/src/scenes/ContentPerformance.tsx`

Copied dependencies (as they stood at build time): `SocialAiVisibility.tsx`, `ContentRepurpose.tsx`, `OneIntoTen.tsx`.

Edits to existing toolkit files (not copied here):
- `Root.tsx` — import the new scene file(s) and register each scene as `<Name>` (1920×1080) and `<Name>916` (1080×1920) with `calculateMetadata` from `durationSeconds`.
- `runtime/remotion/src/scenes.json` — regenerated with `./art scene-index`.

Relies on the earlier patches listed in `../2026-09-26-social-ai-brand-visibility/TOOLKIT-CHANGES.md`.
