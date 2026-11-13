# BUILD-PROMPT — The Geometry Of Meaning.

Paste-ready Claude Code prompt that builds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit
root (this reel lives in the book, not the toolkit — CLAUDE.md rule 4).
The book root for this reel is `D:\ai1-cli-main`, same as its ai-explainer
and cli-explainer siblings for this chapter.

```
Reel: D:\ai1-cli-main\youtube\2026-08-26-claude-rag-embeddings-deep-explainer

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.
2. Audio (if not already generated / narration changed):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   (add --only <BEAT_ID> to regenerate a single beat after a narration edit —
   never hand-edit actual_duration_s; audio is the master clock.)
3. Manim (8 scenes in this reel's own scenes.py — B04, B08, B09, B11, B13,
   B19, B21, B26):
   cd <REEL> && manim -qk --disable_caching scenes.py <SceneClass> [<SceneClass> ...]
   Then move the rendered clip(s) into the flat manim/ folder compile.py
   expects: cp media/videos/scenes/2160p60/<Scene>.mp4 manim/<BID>.mp4
   *** WARNING: Manim's own cache directory is ALSO named `media/` and
   lives at this same reel root — do NOT `rm -rf media` to clean up after
   a render, it will also delete the toolkit's Remotion clips and/or
   pantry stills sitting in the real media/ folder (this happened twice
   during this build — see BUILD-LOG.md). Only remove Manim's own
   subpaths: `rm -rf media/videos media/images media/texts __pycache__`. ***
4. Visuals — render every beat carrying shot.remotion.pattern:
   python runtime/scripts/remotion_scenes.py <REEL>
   (zero new Remotion components needed — reuses ProblemExecutiveSummary
   ×11, DeepActCard ×3 from the Chapter 2 sibling, and EmbedSpeedLeap ×1
   from this chapter's own ai-explainer sibling, all already registered
   in runtime/remotion/src/Root.tsx.)
5. Pantry — if any pantry/<BID>.png changes, re-run intake and restore the
   real sidecars (pantry.py only writes generic FILL-IN stubs into media/):
   python runtime/scripts/pantry.py <REEL>
   cp pantry/<BID>.source.txt media/<BID>.source.txt   # for each changed BID
6. Assemble at 4K (Windows note: force UTF-8 stdout or compile.py's status-line
   arrow character crashes cp1252 consoles):
   PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL> --height 2160
   (explicit --height 2160 — compile.py's own bare default is 720p.)
7. Visual QC (mandatory, never skip — mp4 probe alone is not QC):
   ffmpeg -i <REEL>/claude-rag-embeddings-deep-explainer.mp4 -vf fps=1 <REEL>/_qc/frames/%05d.png
   Read a sample of the PNGs — especially the 8 Manim scenes (dense label
   layouts) and all 7 pantry stills (check for legible real text/brands,
   not just collisions) — audit the 9-point rubric, update _qc/REPORT.md.
   Fix root causes (scenes.py for Manim, re-source for pantry legibility
   issues) and re-render/re-compile until zero BLOCKER/MAJOR.
8. Confirm resolution: ffprobe -v error -select_streams v:0 -show_entries
   stream=width,height <REEL>/claude-rag-embeddings-deep-explainer.mp4 → must read 3840x2160.
9. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `beat_sheet.json` — authored, GATE P signed PASS, audio generated (Kokoro
  `am_onyx`), all 34 beats rendered and compiled.
- `scenes.py` — 8 Manim scenes, all rendered at 4K; two (B09, B19) fixed at
  the source after visual QC found real layout/claim-mismatch defects.
- `SHOPPING.md` (Gate D2, written after audio lock) / `pantry/` (7 real
  stock photos, two replaced after visual QC found legibility issues) /
  `PEDAGOGY.md` (GATE P PASS) / `SOURCES.md` / `FACTCHECK.md` (GATE F
  CLOSED) / `CHECKS-REPORT.md` / `_qc/REPORT.md` — all written.
- Master: `claude-rag-embeddings-deep-explainer.mp4` — **3840×2160, 433.1s,
  34/34 filled, zero slates.**
- GATE P: **PASS** — signed by Vedanshu Daxesh Patel, 2026-08-26.

## If re-running after a content edit

- Edit `narration_text` in `beat_sheet.json` → step 2 with `--only <ID>` →
  step 3/4 with `--force`/re-render for that beat if its visual props also
  changed → step 6 with `--force` → step 7 again. Never fix timing by hand.
- If a pantry still needs re-sourcing, actually zoom into any text-bearing
  region of the candidate photo before accepting it — this exact check
  caught two real problems (a legible real book's sentences, a legible
  real charting-library brand name) that a thumbnail-level glance missed.
- 4K is a hard requirement for this reel per the original build request —
  step 6 must pass `--height 2160` explicitly and step 8 must confirm it;
  do not ship a 720p/1080p draft as the master.
