# BUILD-PROMPT — Watch The Obvious Fix Fail.

Paste-ready Claude Code prompt that builds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root
(this reel lives in the book, not the toolkit — see CLAUDE.md rule 4).

```
Reel: C:\Users\vedan\Downloads\ai1-cli-main\youtube\2026-08-18-claude-cli-rag-the-problem

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, STOP —
   a human must review beat_sheet.json and sign off first. As of this
   writing the verdict is PENDING; do not proceed past step 1 until it reads
   "VERDICT: PASS — signed by Vedanshu Daxesh Patel".
2. Audio (Kokoro, free, voice already set in beat_sheet.json metadata):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   (add --only <BEAT_ID> to regenerate a single beat after a narration edit —
   never hand-edit actual_duration_s; audio is the master clock.)
3. Visuals — render every beat carrying shot.remotion.pattern:
   python runtime/scripts/remotion_scenes.py <REEL>
   (every pattern used here — ClaudeComposerAsk, RagExecutiveSummary,
   ClaudeCodeBeat, CliRunOutput, ClaudeTitleOutro — is already registered in
   runtime/remotion/src/Root.tsx; no new components need to be built.)
4. Assemble at 4K (Windows note: force UTF-8 stdout or compile.py's status-line
   arrow character crashes cp1252 consoles):
   PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL> --height 2160
   (explicit --height 2160 — compile.py's own bare default is 720p. Confirm
   the 4K request by checking the master's actual resolution after this step.)
5. Visual QC (mandatory, never skip — mp4 probe alone is not QC):
   ffmpeg -i <REEL>/claude-cli-rag-the-problem.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read a sample of the PNGs (especially B03/B06 code beats and B04/B07
   terminal-output beats, where long lines are most likely to overflow or
   collide), audit the 9-point rubric, update _qc/REPORT.md. Re-render
   (--force) and re-check until zero BLOCKER/MAJOR.
6. Confirm resolution: ffprobe -v error -select_streams v:0 -show_entries
   stream=width,height <REEL>/claude-cli-rag-the-problem.mp4 → must read 3840x2160.
7. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `code/naive_assistant.py` / `code/naive_bigcontext.py` — written, actually
  executed; verbatim stdout captured into B04/B07.
- `beat_sheet.json` — authored, GATE P signed PASS, audio generated (Kokoro
  `am_onyx`), all 11 beats rendered and compiled.
- `PEDAGOGY.md` / `SOURCES.md` / `CHECKS-REPORT.md` / `_qc/REPORT.md` — written.
- Visual QC: zero BLOCKER/MAJOR defects found on first pass — see
  `_qc/REPORT.md`.
- Master: `claude-cli-rag-the-problem.mp4` — **3840×2160, 154.3s**, 11/11 filled.
- GATE P: **PASS** — signed by Vedanshu Daxesh Patel, 2026-08-18.

## If re-running after a content edit

- Edit `narration_text` in `beat_sheet.json` → step 2 with `--only <ID>` →
  step 3 with `--force` for that beat if its visual props also changed →
  step 4 with `--force` → step 5 again. Never fix timing by hand.
- If the CODE beats change, re-run the corresponding script under `code/`
  and re-copy its real stdout into the matching OUTPUT beat's `lines` —
  never hand-edit captured output (THE ACTUAL-CODE LAW).
- 4K is a hard requirement for this reel per the original build request —
  step 4 must pass `--height 2160` explicitly and step 6 must confirm it.
