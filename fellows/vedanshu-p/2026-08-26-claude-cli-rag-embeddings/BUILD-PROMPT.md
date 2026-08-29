# BUILD-PROMPT — Watch Embeddings Beat The Wrong Words.

Paste-ready Claude Code prompt that builds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit
root (this reel lives in the book, not the toolkit — CLAUDE.md rule 4). The
book root for this reel is `D:\ai1-cli-main`, same as its sibling
ai-explainer reel `2026-08-26-claude-rag-embeddings`.

```
Reel: D:\ai1-cli-main\youtube\2026-08-26-claude-cli-rag-embeddings

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.
2. Audio (if not already generated / narration changed):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   (add --only <BEAT_ID> to regenerate a single beat after a narration edit —
   never hand-edit actual_duration_s; audio is the master clock.)
3. Visuals — render every beat carrying shot.remotion.pattern:
   python runtime/scripts/remotion_scenes.py <REEL>
   (no new Remotion components needed for this reel — reuses
   ClaudeComposerAsk, RagExecutiveSummary, ClaudeCodeBeat, CliRunOutput,
   ClaudeTitleOutro, all already registered in runtime/remotion/src/Root.tsx
   from the two sibling cli-explainer reels.)
4. Assemble at 4K (Windows note: force UTF-8 stdout or compile.py's status-line
   arrow character crashes cp1252 consoles):
   PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL> --height 2160
   (explicit --height 2160 — compile.py's own bare default is 720p. 4K is a
   hard requirement per the original build request, matching the sibling
   ai-explainer reel.)
5. Visual QC (mandatory, never skip — mp4 probe alone is not QC):
   ffmpeg -i <REEL>/claude-cli-rag-embeddings.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read a sample of the PNGs — especially B03/B06 (code cards, check for
   overflow/wrapping of the trimmed snippets) and B04/B07 (CLI output +
   verdict stamp, check the "bad"/"good" tone renders distinctly and the
   ranking numbers don't collide with the verdict line) — audit the 9-point
   rubric, update _qc/REPORT.md. Fix root causes and re-render (--force)
   until zero BLOCKER/MAJOR.
6. Confirm resolution: ffprobe -v error -select_streams v:0 -show_entries
   stream=width,height <REEL>/claude-cli-rag-embeddings.mp4 → must read 3840x2160.
7. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `code/naive_similarity.py` and `code/embedding_similarity.py` — written,
  both REAL and actually executed (THE ACTUAL-CODE LAW); verbatim stdout
  captured and logged in `SOURCES.md`/`PEDAGOGY.md`.
- `beat_sheet.json` — authored, GATE P signed PASS, audio generated (Kokoro
  `am_onyx`), all 11 beats rendered and compiled.
- `PEDAGOGY.md` (GATE P PASS) / `SOURCES.md` / `CHECKS-REPORT.md` /
  `_qc/REPORT.md` — all written.
- No new Remotion components needed — reuses `ClaudeComposerAsk`,
  `RagExecutiveSummary`, `ClaudeCodeBeat`, `CliRunOutput`,
  `ClaudeTitleOutro` from the two sibling cli-explainer reels.
- Master: `claude-cli-rag-embeddings.mp4` — **3840×2160, 147.8s, 11/11
  filled, zero slates.**
- GATE P: **PASS** — signed by Vedanshu Daxesh Patel, 2026-08-26.

## If re-running after a content edit

- Edit `narration_text` in `beat_sheet.json` → step 2 with `--only <ID>` →
  step 3 with `--force` for that beat if its visual props also changed →
  step 4 with `--force` → step 5 again. Never fix timing by hand.
- If either code file is edited, re-run it for real
  (`python code/naive_similarity.py` on the toolkit's ordinary Python;
  `<venv>/python code/embedding_similarity.py` in a venv with
  `sentence-transformers` installed — NOT the toolkit's shared system
  Python, see `SOURCES.md`) and re-capture verbatim stdout into
  `beat_sheet.json`'s B04/B07 `lines` before touching audio.
- 4K is a hard requirement for this reel, matching its ai-explainer sibling
  — step 4 must pass `--height 2160` explicitly and step 6 must confirm it.
