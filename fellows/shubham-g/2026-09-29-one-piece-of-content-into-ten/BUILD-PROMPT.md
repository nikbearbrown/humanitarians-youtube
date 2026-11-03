# BUILD-PROMPT — one-piece-of-content-into-ten

Paste into Claude Code, run from the brutalist.art toolkit folder (Git Bash, `PYTHONUTF8=1`):

> Build the reel at `~/Documents/brutalist-reels/youtube/one-piece-of-content-into-ten/` end to end.
> Read its beat_sheet.json, FACTCHECK.md and BUILD-LOG.md first. Gate check → audio
> (`python3 runtime/scripts/generate_audio_kokoro.py <reel>`, voice af_bella) → stamp each
> Remotion beat's `props.durationSeconds` from `actual_duration_s` → render beats with
> `python3 runtime/scripts/remotion_scenes.py <reel>` → `ART_NO_DRAWTEXT=1 ./art run <reel>` →
> frame-level visual QC (read the _qc PNGs, fix scene source until zero BLOCKER/MAJOR) →
> `./art final <reel> --out <reel>/renders`. Then `./art vertical <reel>`, apply the portrait-only
> props in BUILD-LOG.md, render with `python3 runtime/scripts/remotion_scenes.py <reel>/vertical`,
> run and QC it, and `./art final <reel>/vertical --height 3840 --out <reel>/renders`.
> No statistics may be added. Never publish; report the two output paths and their verified receipts.
