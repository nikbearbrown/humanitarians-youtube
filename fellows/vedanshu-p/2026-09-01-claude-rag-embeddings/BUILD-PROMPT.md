# BUILD-PROMPT — Meaning, As A Number.

Paste-ready Claude Code prompt that builds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit
root (this reel lives in the book, not the toolkit — CLAUDE.md rule 4).
The book root for this reel is `D:\ai1-cli-main` (confirmed via
`metadata.yaml`), NOT the `C:\Users\vedan\Downloads\ai1-cli-main` copy used
for the Chapter 1–2 reels earlier this session.

```
Reel: D:\ai1-cli-main\youtube\2026-08-26-claude-rag-embeddings

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.
2. Audio (if not already generated / narration changed):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   (add --only <BEAT_ID> to regenerate a single beat after a narration edit —
   never hand-edit actual_duration_s; audio is the master clock.)
3. Visuals — render every beat carrying shot.remotion.pattern:
   python runtime/scripts/remotion_scenes.py <REEL>
   (bespoke components for this reel live in
   runtime/remotion/src/EmbedIllu.tsx, registered in runtime/remotion/src/Root.tsx:
   EmbedScatterPlot, EmbedVectorArithmetic, EmbedWordToPassage, EmbedSpeedLeap,
   EmbedCosineSimilarity, EmbedRevealPairs. B01/B07 reuse ProblemExecutiveSummary
   [runtime/remotion/src/ProblemIllu.tsx, built for the Chapter 2 reel]; B08
   reuses the shared PredictCard. No Manim/scenes.py in this build.)
4. Assemble at 4K (Windows note: force UTF-8 stdout or compile.py's status-line
   arrow character crashes cp1252 consoles):
   PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL> --height 2160
   (explicit --height 2160 — compile.py's own bare default is 720p.)
5. Visual QC (mandatory, never skip — mp4 probe alone is not QC):
   ffmpeg -i <REEL>/claude-rag-embeddings.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read a sample of the PNGs — especially B02/B09 (2D scatter plots, check
   dot/label collisions) and B03/B05 (text-heavy cards, check overflow) —
   audit the 9-point rubric, update _qc/REPORT.md. Fix root causes in
   EmbedIllu.tsx and re-render (--force) until zero BLOCKER/MAJOR.
6. Confirm resolution: ffprobe -v error -select_streams v:0 -show_entries
   stream=width,height <REEL>/claude-rag-embeddings.mp4 → must read 3840x2160.
7. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `beat_sheet.json` — authored, GATE P signed PASS, audio generated (Kokoro
  `am_onyx`), all 13 beats rendered and compiled.
- `PEDAGOGY.md` (GATE P PASS) / `SOURCES.md` / `CHECKS-REPORT.md` /
  `_qc/REPORT.md` — all written.
- Six new Remotion components in `EmbedIllu.tsx`, registered in `Root.tsx`,
  rendered. One BLOCKER collision found in B05 by visual QC, fixed at the
  source, re-rendered, re-verified clean.
- Master: `claude-rag-embeddings.mp4` — **3840×2160, 204.2s, 13/13 filled,
  zero slates.**
- GATE P: **PASS** — signed by Vedanshu Daxesh Patel, 2026-08-26.

## If re-running after a content edit

- Edit `narration_text` in `beat_sheet.json` → step 2 with `--only <ID>` →
  step 3 with `--force` for that beat if its visual props also changed →
  step 4 with `--force` → step 5 again. Never fix timing by hand.
- 4K is a hard requirement for this reel per the original build request —
  step 4 must pass `--height 2160` explicitly and step 6 must confirm it;
  do not ship a 720p/1080p draft as the master.
