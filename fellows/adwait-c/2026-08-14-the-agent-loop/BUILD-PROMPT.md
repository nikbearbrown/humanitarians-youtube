# BUILD-PROMPT — Episode 2, "The Agent Loop"

The single paste-ready prompt that rebuilds this cut end to end. Run from
`/Users/adwaitchangan/Study/Brutalist/`.

---

Build the Humanitarians AI Fellows episode at
`humanitarians-youtube/fellows/adwait-changan/2026-08-14-the-agent-loop/` using the
`brutalist.art` toolkit's `ai-explainer` skill. This is episode 2 of the 10-part playlist
`PLAYLIST-agentic-ai.md` — read that file first, then read Episode 1's `README.md`, because
this episode extends its code artifact and pays off two of its claims.

**Before anything else:** activate the toolkit venv. The `./art` subscripts call bare
`python3`, which otherwise resolves to system Python 3.13 and has no `kokoro_onnx`:

```bash
source brutalist.art/.venv/bin/activate
cd brutalist.art
```

Then, in order:

1. **Gate check.** Confirm `PEDAGOGY.md` carries `VERDICT: PASS` and `FACTCHECK.md` reads
   `FACT GATE: CLEARED`. If either is open, stop and report.
2. **Run the source before rendering anything that shows it.** `python3 trace_loop.py` in
   the reel folder. Three blocks print: the lazy pass, the honest pass, and the lazy loop
   run to its step budget. Then check all three against the beat sheet:
   - B03's `artifactLines` against the first two blocks (the two OBSERVATION *values* must
     match verbatim; the `(lazy)` / `(honest)` labels are on-screen annotations, disclosed
     in FACTCHECK row 4);
   - B06's `code` prop against the real `record()`, character-for-character — and **count
     the rendered lines** to confirm the narration's "the comment on line five";
   - B07's `artifactLines` against the eight-pass block plus `stopped: step budget
     exhausted`.
   If any differ, fix the beat sheet — never the claim.
3. **Audio (the clock).** `python3 runtime/scripts/generate_audio_kokoro.py <REEL>` —
   Kokoro `am_onyx`, free. Durations are ground truth.
4. **Render every beat.** `python3 runtime/scripts/remotion_scenes.py <REEL>` — foreground.
   All 13 beats use existing patterns, so expect zero slates.
5. **Review cut.** `python3 runtime/scripts/compile.py <REEL> --review`.
6. **VISUAL QC LAW.** The mp4 probe is a file check and does not count. Sample frames at
   ≥2 fps plus each beat at ~15/50/85 % of its span, **Read the PNGs**, and audit the
   9-point rubric. Log defects and fixes in `_qc/REPORT.md`. Re-render until zero BLOCKER
   and zero MAJOR remain. Pay particular attention to B03 and B07: both are printed program
   output and must render unnumbered, in mono, with column alignment intact
   (`numbered: false`).
7. **Clean master.** `./art final <REEL>` → 4K `<slug>.mp4`.
8. **Report.** Duration, beat count, slate count, QC defects found and fixed.

**Do not publish.** No publishing machinery exists here and none is authorized.

**Three traps this build actually hit:**
- `ClaudeWindow` auto-numbers `artifactLines` unless you pass `numbered: false`. A numbered
  terminal trace is a factual misrepresentation, not a style choice.
- `ClaudeWindow` ignored its own `width`/`fontSize` props until they were wired up (see
  Episode 1's `_qc/REPORT.md` D3). If a card renders at 1100 px, the toolkit copy is stale.
- **Do not edit `beat_sheet.json` until the render process has actually exited.**
  `remotion_scenes.py` and `compile.py` re-dump the sheet on finish and will silently
  clobber a concurrent patch. Waiting for the last `media/*.mp4` to appear is *not* enough —
  it happened here, the beat re-rendered with the old props, and only reading the
  verification frame caught it. Re-read the sheet after patching.

---

Expected result: 13 beats, zero slates, ~3 min 25 s, `_qc/REPORT.md` clean, master at
`TheAgentLoop_AdwaitChangan_2026-08-14.mp4`. Cost $0.00.
