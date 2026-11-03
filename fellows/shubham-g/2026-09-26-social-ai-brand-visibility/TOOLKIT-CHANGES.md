# TOOLKIT-CHANGES — local patches to brutalist.art used for this build

New files (copies in `scenes/`):
- `runtime/remotion/src/scenes/SocialAiVisibility.tsx` — SocialOneToMany, SocialCadenceGrid, SocialTrendWindow, SocialAudienceBranch, SocialLoop, SocialHumanSplit, HandleTitleOutro (16:9).
- `runtime/remotion/src/scenes/SocialAiVisibility916.tsx` — native 9:16 versions (serif ≥ 90 / sans ≥ 76 px).
- `runtime/remotion/src/tokens/ebGaramond.ts` + `public/fonts/EBGaramond-*.ttf` — load the bundled house serif inside the bundle (headless Chrome on Windows fell back to Georgia).

Edits to existing toolkit files (not copied here):
- `Root.tsx` — register each scene as `<Name>` (1920×1080) and `<Name>916` (1080×1920) with `calculateMetadata` from `durationSeconds`; add `calculateMetadata` to ClaudeComposerAsk916, ClaudeVerdictArtifact916 and BrutalistHesitantWriter916 (fallback = previous fixed length).
- `runtime/scripts/compile.py` — escape the drawtext font path (Windows); size review labels from the frame's short side.
- `runtime/scripts/remotion_scenes.py` — resolve `npx` with `shutil.which` (Windows `npx.cmd`).
- `runtime/qc/brand_labels.json` — channel `claude-shubh` (chip `@Shubh & @HumanitariansAI`).
- `ClaudeVerdictArtifact916.tsx` — render `brandLabel`; optional `largeText`.
