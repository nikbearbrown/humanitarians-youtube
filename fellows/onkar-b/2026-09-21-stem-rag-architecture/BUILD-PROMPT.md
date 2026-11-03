# BUILD-PROMPT.md — hai-liam-rag-triangle

Paste-ready prompt that rebuilds this reel end to end, from the beat sheet to
verified 4K masters in both aspects. Deterministic and free: Kokoro + Remotion,
no key, no paid call, never publishes.

Run from the toolkit root (`brutalist.art/`).

---

```
Rebuild the reel at ../brutalist-reels/youtube/hai-liam-rag-triangle
("Claude, Retrieved." — Week 3 STEM: Retrieval-Augmented Generation,
@HumanitariansAI, Liam / Kokoro am_onyx).

Read these first, completely: skills/make/ai-explainer/SKILL.md,
RENDER-TARGETS.md, OUTRO-LOCK.md, and the reel's own BUILD-LOG.md —
BUILD-LOG.md records six deliberate deviations from the source script; keep
every one of them.

Then:

1. GATE CHECK. Confirm the paperwork set is present and non-empty:
   FACTCHECK.md, SHOTLIST.md, PROMPTS.md, CHECKS-REPORT.md, SOURCES.md.
   Confirm every beat's shot.remotion.pattern is renderable:
     ./art scenes --check RagTriangle
     ./art scenes --check RagPromptCompare
     ./art scenes --check RagEmbeddingSpace
     ./art scenes --check HaiTitleOutro
   plus ClaudeComposerAsk, BrutalistHesitantWriter, ClaudeVerdictArtifact.
   If any 916 companion is missing, register it before rendering — do not
   centre-crop a generated graphic.

2. AUDIO IS THE CLOCK. Regenerate narration and let the measured durations
   drive everything downstream:
     python3 runtime/scripts/generate_audio_kokoro.py <REEL>
   Expect 10 beats, voice am_onyx, ~164s total, $0.00. Never hand-edit a
   duration; if a beat runs long, change its words and regenerate.

3. RENDER THE BEATS at 4K:
     python3 runtime/scripts/remotion_scenes.py <REEL>
   (--scale=2, PNG frames, crf 16. Use --force --only <BID> to redo one beat.)

4. COMPILE THE REVIEW CUT:
     ./art run <REEL>
   QC gates run here. There are no Manim beats, so the Manim stage skips and
   no scenes.py is needed in the folder.

5. VISUAL QC LAW — the part that is not optional. The mp4 probe is a file
   check, not QC. Sample frames and LOOK at them:
     ffmpeg -i <REEL>/hai-liam-rag-triangle-slate.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   plus each beat at ~15/50/85% of its span from beat_sheet.json. Read the
   PNGs and audit the 9-point rubric: edge bleed/clipping, title-safe margins,
   container overflow, collision, offscreen anchors, legibility, brand-bug
   placement, aspect, and CANVAS FILL. Log defects and fixes in _qc/REPORT.md.
   Fix root causes in the scene source and re-render until zero BLOCKER and
   zero MAJOR remain.

6. CLEAN MASTER (4K landscape):
     ./art final <REEL>
   Writes to --out DIR, else $ART_OUT, else brutalist.art/renders/.

7. VERTICAL COMPANION (its own beat sheet, never a crop):
     ./art vertical <REEL>
   Then render the portrait beats from vertical/beat_sheet.json (every pattern
   has a registered 916 id) and QC the vertical frames separately — portrait
   type sizes and safe margins are a different layout, not the same one
   scaled.

Report: measured runtime, per-beat durations, QC defects found and fixed, and
where both masters landed. Do not publish anything, and do not enable any
upload path — this toolkit has none by design.
```

---

## Expected output

| Artifact | Path |
|---|---|
| Review cut (beat labels + timecode) | `hai-liam-rag-triangle-slate.mp4` |
| Clean 4K landscape master | `$ART_OUT` / `brutalist.art/renders/hai-liam-rag-triangle.mp4` |
| Vertical companion | `vertical/` |
| Per-beat clips | `clips/`, `media/` |
| Narration + timings | `mp3/`, `mp3/timings.json` |
| QC evidence | `_qc/REPORT.md`, `_qc/frames/`, `_qc/contact_sheet.png` |
