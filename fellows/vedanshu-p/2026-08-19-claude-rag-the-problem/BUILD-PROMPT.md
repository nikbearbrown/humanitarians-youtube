# BUILD-PROMPT — Confident, Frozen, Or Buried.

Paste-ready Claude Code prompt that builds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root
(this reel lives in the book, not the toolkit — see CLAUDE.md rule 4).

```
Reel: C:\Users\vedan\Downloads\ai1-cli-main\youtube\2026-08-18-claude-rag-the-problem

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, STOP —
   a human must review beat_sheet.json (and the animated previz once step 3
   has run once) and sign off first. As of this writing the verdict is
   PENDING; do not proceed past step 1 until it reads
   "VERDICT: PASS — signed by Vedanshu Daxesh Patel".
2. Audio (Kokoro, free, voice already set in beat_sheet.json metadata):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   (add --only <BEAT_ID> to regenerate a single beat after a narration edit —
   never hand-edit actual_duration_s; audio is the master clock.)
3. Visuals — render every beat carrying shot.remotion.pattern:
   python runtime/scripts/remotion_scenes.py <REEL>
   (bespoke components for this reel do not exist yet and must be authored in
   runtime/remotion/src/ProblemIllu.tsx, registered in runtime/remotion/src/Root.tsx:
   ProblemExecutiveSummary, ProblemHallucination, ProblemStaleKnowledge,
   ProblemContextLimits (bespoke — not a ScaleComparison wrap, see
   beat_sheet.json B04's bespoke_note), ProblemWorkedExample (wraps
   ChipGrid), ProblemBiggerWindowVerdict (wraps LayerStack), ProblemPredictCard
   (wraps PredictCard, unmodified props).)
4. Assemble at 4K (Windows note: force UTF-8 stdout or compile.py's status-line
   arrow character crashes cp1252 consoles):
   PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL> --height 2160
   (explicit --height 2160 — do not rely on compile.py's own bare default,
   which is 720p; only run.sh's wrapper overrides that. Confirm the request
   for 4K beats by checking the master's actual resolution after this step.)
5. Visual QC (mandatory, never skip — mp4 probe alone is not QC):
   ffmpeg -i <REEL>/claude-rag-the-problem.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read a sample of the PNGs, audit the 9-point rubric, update _qc/REPORT.md.
   Fix root causes in ProblemIllu.tsx and re-render (--force) until zero BLOCKER/MAJOR.
6. Confirm resolution: ffprobe -v error -select_streams v:0 -show_entries
   stream=width,height <REEL>/claude-rag-the-problem.mp4 → must read 3840x2160.
7. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `beat_sheet.json` — authored, GATE P signed PASS, audio generated (Kokoro
  `am_onyx`), all 11 beats rendered and compiled.
- `PEDAGOGY.md` / `SOURCES.md` / `CHECKS-REPORT.md` / `_qc/REPORT.md` — written.
- Bespoke components built: `runtime/remotion/src/ProblemIllu.tsx`
  (`ProblemExecutiveSummary`, `ProblemHallucination`, `ProblemStaleKnowledge`,
  `ProblemContextLimits`, `ProblemWorkedExample`, `ProblemBiggerWindowVerdict`,
  `ProblemPredictCard`), registered in `Root.tsx`.
- Visual QC: two BLOCKER collisions found and fixed at the source (B03 chip
  overlapping its subline; B04 bar labels overlapping the caption) — see
  `_qc/REPORT.md` for the full before/after. 0 BLOCKER / 0 MAJOR remaining.
- Master: `claude-rag-the-problem.mp4` — **3840×2160, 184.4s**, 11/11 filled.
- GATE P: **PASS** — signed by Vedanshu Daxesh Patel, 2026-08-18.

## If re-running after a content edit

- Edit `narration_text` in `beat_sheet.json` → step 2 with `--only <ID>` →
  step 3 with `--force` for that beat if its visual props also changed →
  step 4 with `--force` → step 5 again. Never fix timing by hand.
- Channel/persona is a personal-author channel (`@VedanshuDaxeshPatel`, Onyx
  voice, Kokoro, free) — not `claude-liam`/IN-FOR-BEAR, matching the three
  sibling reels already in this `youtube/` folder for Chapter 1.
- 4K is a hard requirement for this reel per the original build request —
  step 4 must pass `--height 2160` explicitly and step 6 must confirm it;
  do not ship a 720p/1080p draft as the master.
