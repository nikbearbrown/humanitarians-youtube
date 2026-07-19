# BUILD-NOTES — claude-oversimplified remotion sources

`remotion-src/` holds the full composition, authored and previz-rendered in a
Cowork cloud sandbox. Contract:

- `Previz.tsx` — the whole reel: ClaudeComposerAsk cold open (B00) → six
  ClaudePosterBeat claim beats (callout N draws at beat start, earlier callouts
  pre-settled via negative delay) → ClaudePosterV2 verdict → ClaudeTitleOutro
  (restated title). `BEATS` mirrors `beat_sheet.json`.
- `beats_timing.json` — GENERATED: per-beat frames from measured mp3 durations
  (`ceil((dur + 0.4s) * 30)`). Regenerate after real ElevenLabs audio lands.
- The caption bar (`Caption` component) is PREVIZ-ONLY — remove for the final cut.
- Import paths were sandbox-relative and need rewiring locally:
  - onda bench: `vox/remotion/_bench/onda/registry/components/{claude-window,claude-callout}`
  - runtime: `brutalist-art/runtime/remotion/src/scenes/ClaudeComposerAsk`, `tokens/claude`
  - The `skills/make/component-showcase/remotion` project already has remotion+zod
    installed and the bench wired — host the composition there.
- Authored at 1280×720 px constants. Render final with `--scale=1.5` for 1920×1080.
- mp3s belong in the host project's `public/mp3/beat-BXX.mp3` (staticFile paths).
- `mp3-scratch/` in this folder is the espeak scratch voice — timing reference only,
  never publish it.
