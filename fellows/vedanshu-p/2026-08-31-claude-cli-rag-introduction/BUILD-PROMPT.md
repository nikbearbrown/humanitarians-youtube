# BUILD-PROMPT — Watch Retrieval Fix A Stale Answer.

Paste-ready Claude Code prompt that rebuilds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root
(this reel lives in the book, not the toolkit — CLAUDE.md rule 4).

```
Reel: C:\Users\vedan\Downloads\ai1-cli-main\youtube\claude-cli-rag-introduction

0. Verify the demo code still runs (THE ACTUAL-CODE LAW — before touching
   beats, confirm the source of truth hasn't drifted):
   python code/naive_answer.py
   python code/rag_answer.py
   If output changed, update B04/B07's `lines` props to the new verbatim
   stdout before doing anything else.
1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.
2. Audio: python runtime/scripts/generate_audio_kokoro.py <REEL>
   (--only <BEAT_ID> to regenerate one beat after a narration edit — never
   hand-edit actual_duration_s; audio is the master clock.)
3. Visuals: python runtime/scripts/remotion_scenes.py <REEL>
   (bespoke components: runtime/remotion/src/RagIllu.tsx —
   RagExecutiveSummary (reused B01+B08) — and runtime/remotion/src/RagCliIllu.tsx —
   CliRunOutput (reused B04+B07) — both registered in runtime/remotion/src/Root.tsx.
   IMPORTANT: each composition's durationInFrames is set BELOW the shortest
   real beat using it, on purpose — see the comment block above the Rag*
   registrations in Root.tsx before changing any of them. Registering a
   composition longer than its beat's audio silently truncates the
   animation instead of erroring; this bit the first build of this reel.)
4. Assemble (Windows: force UTF-8 stdout or compile.py's arrow-glyph status
   line crashes cp1252 consoles):
   PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL>
5. Visual QC (mandatory, never skip — the mp4 probe is not QC):
   ffmpeg -i <REEL>/claude-cli-rag-introduction.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read a sample of PNGs, audit the 9-point rubric, update _qc/REPORT.md.
   For any OUTPUT-beat (CliRunOutput) props change, also spot-check that
   verdict text doesn't collide with wrapped stdout lines — CliRunOutput
   lays verdict out in the SAME document-flow column as the lines
   specifically so wrapped text doesn't need manual offset math; don't
   reintroduce a fixed pixel offset for it.
6. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `code/naive_answer.py` + `code/rag_answer.py` — real, runnable, verified.
- `beat_sheet.json` — authored (cli-explainer required spine, all 11 beats),
  GATE P signed PASS, audio generated (Kokoro `am_onyx`), all beats rendered
  and compiled TWICE (a duration-mismatch bug and a text-collision bug were
  both found during QC and fixed — see `_qc/REPORT.md` for the full account).
- `PEDAGOGY.md` / `SOURCES.md` / `CHECKS-REPORT.md` / `_qc/REPORT.md` — written.
- Master: `claude-cli-rag-introduction.mp4` (145.6s, 1280×720, 11/11 filled).

## If re-running after a content edit

- Same personal-author channel as the sibling reel: `@VedanshuDaxeshPatel`,
  Kokoro `am_onyx` ("Onyx"), no IN-FOR-BEAR framing.
- If you add a THIRD cycle (a second revision) or a different demo entirely,
  re-verify THE ACTUAL-CODE LAW end to end: write the script, run it for
  real, capture real stdout, THEN author the beat — never the reverse.
