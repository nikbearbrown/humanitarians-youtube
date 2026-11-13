# BUILD-PROMPT — The Model Never Saw The Document.

Paste-ready Claude Code prompt that rebuilds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root
(this reel lives in the book, not the toolkit — see CLAUDE.md rule 4).

```
Reel: C:\Users\vedan\Downloads\ai1-cli-main\youtube\claude-liam-rag-introduction

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.
2. Audio (if not already generated / narration changed):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   (add --only <BEAT_ID> to regenerate a single beat after a narration edit —
   never hand-edit actual_duration_s; audio is the master clock.)
3. Visuals — render every beat carrying shot.remotion.pattern:
   python runtime/scripts/remotion_scenes.py <REEL>
   (bespoke components for this reel live in
   runtime/remotion/src/RagIllu.tsx, registered in runtime/remotion/src/Root.tsx:
   RagExecutiveSummary, RagRetrieveGenerate (reused B02+B06), RagThreeFixes,
   RagPredictCard, RagFitsInPrompt.)
4. Assemble (Windows note: force UTF-8 stdout or compile.py's status-line
   arrow character crashes cp1252 consoles):
   PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL>
5. Visual QC (mandatory, never skip — mp4 probe alone is not QC):
   ffmpeg -i <REEL>/claude-liam-rag-introduction.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read a sample of the PNGs, audit the 9-point rubric, update _qc/REPORT.md.
   Fix root causes in RagIllu.tsx and re-render (--force) until zero BLOCKER/MAJOR.
6. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `beat_sheet.json` — authored, GATE P signed PASS, audio generated (Kokoro
  `am_onyx`), all 10 beats rendered and compiled.
- `PEDAGOGY.md` / `SOURCES.md` / `CHECKS-REPORT.md` / `_qc/REPORT.md` — written.
- Master: `claude-liam-rag-introduction.mp4` (161.8s, 1280×720, 10/10 filled).

## If re-running after a content edit

- Edit `narration_text` in `beat_sheet.json` → step 2 with `--only <ID>` →
  step 3 with `--force` for that beat if its visual props also changed →
  step 4 with `--force` → step 5 again. Never fix timing by hand.
- Channel/persona is a personal-author channel (`@VedanshuDaxeshPatel`, Onyx
  voice, Kokoro, free) — not `claude-liam`/IN-FOR-BEAR. If Bear's own voice or
  the `@NikBearBrown` channel is wanted for a future cut, that's a beat-sheet
  metadata + narration change (persona, greeting, folderLabel, handle), not a
  re-authoring from scratch.
