# BUILD-PROMPT — Episode 3, "Tools: Giving a Model Hands"

The single paste-ready prompt that rebuilds this cut end to end. Run from
`/Users/adwaitchangan/Study/Brutalist/`.

---

Build the Humanitarians AI Fellows episode at
`humanitarians-youtube/fellows/adwait-changan/2026-08-21-tools-and-function-calling/`
using the `brutalist.art` toolkit's `ai-explainer` skill. Episode 3 of the 10-part playlist
`PLAYLIST-agentic-ai.md` — read that first, then Episodes 1 and 2, because this one carries
their code artifact forward and its `_qc/REPORT.md` files list the pattern traps.

**Before anything else:** activate the toolkit venv. The `./art` subscripts call bare
`python3`, which otherwise resolves to system Python 3.13 and has no `kokoro_onnx`:

```bash
source brutalist.art/.venv/bin/activate
cd brutalist.art
```

Then, in order:

1. **Gate check.** `PEDAGOGY.md` must read `VERDICT: PASS` and `FACTCHECK.md`
   `FACT GATE: CLEARED`. If either is open, stop and report.
2. **Run the source, then re-derive the beats from it.** `python3 tools.py` in the reel
   folder. Three blocks print: the raw JSON payload, the laid-out wire view, and the
   two-contracts A/B. Then verify:
   - B05's `code` prop against `inspect.getsource(tools.to_schema)` — these were generated
     from the source, so they should match exactly. **Count the lines** and confirm the
     narration's "fourteen lines".
   - B03's `artifactLines` against the `wire_view()` block, line for line.
   - B07's `artifactLines` against the two-contracts block, and confirm the program still
     prints `function bodies identical: True` — that line is the control for the episode's
     central claim. If it ever prints `False`, the claim is broken; fix `tools.py`, not the
     script.
   - The measured figures in B07's narration: 3 words / 13 chars for the vague docstring,
     292 chars for the specific one.
3. **Audio (the clock).** `python3 runtime/scripts/generate_audio_kokoro.py <REEL>` —
   Kokoro `am_onyx`, free. Durations are ground truth; never hand-tune timing.
4. **Render every beat.** `python3 runtime/scripts/remotion_scenes.py <REEL>` — foreground,
   never hand-rolled `npx remotion render`. All 13 beats use existing patterns; expect zero
   slates.
5. **Review cut.** `python3 runtime/scripts/compile.py <REEL> --review`.
6. **VISUAL QC LAW.** The mp4 probe is a file check and does not count. Sample frames at
   ≥2 fps plus each beat at ~15/50/85 % of span, **Read the PNGs**, audit the 9-point
   rubric, log everything in `_qc/REPORT.md`, and re-render until zero BLOCKER and zero
   MAJOR remain. Watch specifically:
   - **B03 and B07** must render unnumbered, in mono, with column alignment intact
     (`numbered: false`). A numbered payload or trace is a factual misrepresentation.
   - **B07's longest line is ~80 characters** at `fontSize: 22` in a 1700 px card — check it
     does not wrap, because a wrapped alignment column is unreadable.
7. **Clean master.** `./art final <REEL>` → 4K `<slug>.mp4`.
8. **Report.** Duration, beat count, slate count, QC defects found and fixed.

**Do not publish.** No publishing machinery exists here and none is authorized.

**Traps inherited from Episodes 1–2 — all three cost real re-renders:**
- `ClaudeWindow` and `ClaudeVerdictArtifact` **auto-number `artifactLines`**. Never write
  `"1. "` into a string, and never put a disclaimer in the list — it renders as another
  numbered item and inverts its meaning.
- `MedhavyConceptCard` and `CwcConceptCard` have **no size props** and badly underfill the
  frame. Use them only for act cards (short breathing beats). For anything the narration
  *enumerates*, use `ClaudeScienceLayerStack` or `ClaudeScienceChipGrid`.
- **Do not edit `beat_sheet.json` until the render process has actually exited.**
  `remotion_scenes.py` and `compile.py` re-dump the sheet on finish and will silently
  clobber a concurrent patch. Waiting for the last `media/*.mp4` to appear is *not* enough.
  Re-read the sheet after patching to confirm the write survived.

Also: beat durations should sit at or under their composition's length —
`ClaudeComposerAsk` 900f/30 s, `ClaudeScience*` 360f/12 s, `ClaudeCodeBeat` 300f/10 s,
`ClaudeVerdictArtifact` 1020f/34 s. Longer beats freeze-hold; shorter ones truncate.

---

Expected result: 13 beats, zero slates, ~3 min 17 s, `_qc/REPORT.md` clean, master at
`ToolsAndFunctionCalling_AdwaitChangan_2026-08-21.mp4`. Cost $0.00.
