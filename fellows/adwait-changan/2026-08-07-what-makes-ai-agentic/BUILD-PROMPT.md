# BUILD-PROMPT — Episode 1, "What Makes an AI Agentic"

The single paste-ready prompt that rebuilds this cut end to end. Run from
`/Users/adwaitchangan/Study/Brutalist/`.

---

Build the Humanitarians AI Fellows episode at
`humanitarians-youtube/fellows/adwait-changan/2026-08-07-what-makes-ai-agentic/`
using the `brutalist.art` toolkit's `ai-explainer` skill. This is episode 1 of the
10-part playlist `PLAYLIST-agentic-ai.md` — read that file first for the arc and the
continuity rules.

**Before anything else:** activate the toolkit venv. The `./art` subscripts call bare
`python3`, which otherwise resolves to system Python 3.13 and has no `kokoro_onnx`:

```bash
source brutalist.art/.venv/bin/activate
cd brutalist.art
```

Then, in order:

1. **Gate check.** Confirm `PEDAGOGY.md` carries `VERDICT: PASS` and `FACTCHECK.md` reads
   `FACT GATE: CLEARED`. If either is open, stop and report — do not generate audio.
2. **Verify the code beat before you render it.** Run
   `python3 agent_loop.py` in the reel folder and confirm it prints
   `rows in the sales file: 3`. Then diff the `code` prop of beat B06 against the real
   `run()` function character-for-character. ACTUAL-CODE LAW: if they differ, fix the beat
   sheet, never the claim.
3. **Audio (the clock).**
   `python3 runtime/scripts/generate_audio_kokoro.py <REEL>` — Kokoro `am_onyx`, free.
   Durations are ground truth; never hand-tune timing afterwards.
4. **Render every beat.**
   `python3 runtime/scripts/remotion_scenes.py <REEL>` — foreground, never hand-rolled
   `npx remotion render`. All 13 beats are Remotion patterns that already exist, so the
   first pass should produce zero slates. `--only <BID>` re-renders one beat; deleting
   `media/<BID>.mp4` and re-running (without `--force`) re-renders just what is missing.
5. **Review cut.**
   `python3 runtime/scripts/compile.py <REEL> --review` → `<slug>-slate.mp4`.
6. **VISUAL QC LAW — the part that is not optional.** The mp4 probe is a file check and
   does not count. Sample frames at ≥2 fps plus each beat at ~15/50/85 % of its span,
   **actually Read the PNGs**, and audit the 9-point rubric: edge bleed, title-safe
   margins, container overflow, collision, offscreen anchors, legibility, brand bug,
   aspect, and canvas fill. Log every defect and fix in `_qc/REPORT.md`. Fix root causes
   in the beat sheet or the scene source and re-render until zero BLOCKER and zero MAJOR
   remain.
7. **Clean master.** `./art final <REEL>` → 4K `<slug>.mp4`, no review labels.
8. **Report.** Duration, beat count, slate count, QC defects found and fixed.

**Do not publish.** There is no publishing machinery in this toolkit and none is
authorized. The master stays in the reel folder.

**Two known traps in this repo:**
- Do not edit `beat_sheet.json` while `remotion_scenes.py` or `compile.py` is running —
  both re-dump the sheet on finish and will clobber concurrent edits.
- `git add` on the whole folder pulls in `mp3/`, `media/`, `clips/`, and `_qc/*.png`;
  `.gitignore` only excludes `*.mp4`/`*.mp3`. Add source files explicitly.

---

Expected result: 13 beats, zero slates, ~3 min 20 s, `_qc/REPORT.md` clean, master at
`WhatMakesAIAgentic_AdwaitChangan_2026-08-07.mp4`. Cost $0.00.
