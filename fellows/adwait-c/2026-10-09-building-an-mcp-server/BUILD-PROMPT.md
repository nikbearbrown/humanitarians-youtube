# BUILD-PROMPT — "Building a Tool Server"

Paste-ready prompt that rebuilds both cuts. Run from `/Users/adwaitchangan/Study/Brutalist/`.

---

Build the Humanitarians AI fellows video at
`humanitarians-youtube/fellows/adwait-c/2026-10-09-building-an-mcp-server/` with the `brutalist.art`
`ai-explainer` skill, in **both aspect ratios**.

**Activate the toolkit venv first** — the scripts call bare `python3`, which otherwise
resolves to system Python and has no `kokoro_onnx`:

```bash
source brutalist.art/.venv/bin/activate && cd brutalist.art
```

1. **Gates.** `PEDAGOGY.md` must read `VERDICT: PASS`, `FACTCHECK.md` `FACT GATE: CLEARED`.
2. **Run the source first.** `python3 server.py`. Every number on screen must appear in that output. Do not transcribe it by hand; build the beat props from the captured run.
3. **Audio** → **render** → **compile `--height 2160`**.
4. **VISUAL QC.** Read the PNGs. The mp4 probe is not QC: it reported healthy files for
   every defect this series has had.
5. **Shorts.** `shorts.py <REEL> --drop … --handle "@HumanitariansAI"`, then audio →
   render → `compile.py <REEL>/short --height 3840`.
6. **Report** duration, beat count, defects found and fixed.

**Do not publish, upload, or notify anyone.**

## Rules that cost real re-renders in this series

- **Never say or show an episode or week number**, and never refer back to a previous
  video. Say "this week".
- **Pass explicit `--drop` to `shorts.py`.** The auto-plan drops BVDT and BHTF — the
  verdict and the viewer task — which guts the cut.
- **Drop the code beat from the 9:16 cut.** Portrait is 1080 wide and these functions run
  70 to 86 characters per line. Code cannot reflow, so type sized to the longest line
  lands near 21px, which is not readable on a phone.
- **`shorts.py` defaults the endcard handle to `@nikbearbrown`** — always pass `--handle`.
- **Hand-write the Short's outro.** The auto-rewrite splices truncated narration fragments
  and reads as broken text.
- **`short/` needs its own signed `PEDAGOGY.md`** or Kokoro refuses the outro audio.
- **Do not edit `beat_sheet.json` until the render process has exited.** It re-dumps the
  sheet on exit, silently reverting a patch written in that window, and the render still
  reports success.
- **Check the 95%-of-span frame, not the contact sheet**, before believing a missing item.
  The sheet samples one frame per beat, so staged grids routinely look half-revealed there.
- **Never show code attributed to a file it is not in.** Generate code props from the real
  file at authoring time.
