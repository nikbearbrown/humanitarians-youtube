# BUILD-PROMPT — "Memory and Context"

Paste-ready prompt that rebuilds both cuts. Run from `/Users/adwaitchangan/Study/Brutalist/`.

---

Build the Humanitarians AI fellows video at
`humanitarians-youtube/fellows/adwait-changan/2026-08-28-agent-memory/` with the
`brutalist.art` `ai-explainer` skill, in **both aspect ratios**.

**Activate the toolkit venv first** — the scripts call bare `python3`, which otherwise
resolves to system Python and has no `kokoro_onnx`:

```bash
source brutalist.art/.venv/bin/activate && cd brutalist.art
```

1. **Gates.** `PEDAGOGY.md` must read `VERDICT: PASS`, `FACTCHECK.md` `FACT GATE: CLEARED`.
2. **Run the source first.** `python3 context.py`. Check B03 against the budget table, B07
   against the `first_overflow` block, and B05 against
   `inspect.getsource(context.budget_row)` — **count the lines** and confirm the narration's
   "ten lines". If `first_overflow` ever prints `None`, the horizon is too short and the
   falsifiability beat is broken — raise it, do not soften the script.
3. **Audio** → **render** → **compile `--height 2160`**.
4. **VISUAL QC.** Read the PNGs; the mp4 probe is not QC. Both `ClaudeWindow` beats must
   render `numbered: false` with columns intact.
5. **Shorts.** `shorts.py <REEL> --drop B04 B05 B06 B09 --handle "@HumanitariansAI"`.
   Then audio → render → `compile.py <REEL>/short --height 3840`.
6. **Report** duration, beat count, slate count, defects found and fixed.

**Do not publish, upload, or notify anyone.**

## Rules that cost real re-renders here

- **Never say or show an episode or week number** — not in narration, `greeting`, or
  `subline`. Say "this week"; open with "Today we are going to learn about …"; the outro
  names the title and teases with "Next time".
- **Pass explicit `--drop` to shorts.py.** The auto-plan drops BVDT and BHTF — the verdict
  and the viewer task — which guts the Short. Protect B00 (it carries the required intro
  line), the framework beat, the worked example, the falsifiability beat, BVDT and BHTF.
- **`shorts.py` defaults the endcard handle to `@nikbearbrown`** — always pass `--handle`.
- **Hand-write the Short's outro.** The auto-rewrite splices truncated narration fragments
  and reads as broken text.
- **`short/` needs its own signed `PEDAGOGY.md`** or Kokoro refuses the outro audio.
- **Do not edit `beat_sheet.json` until the render process has exited.** It re-dumps the
  sheet on finish and will silently clobber a concurrent patch; waiting for the last
  `media/*.mp4` to appear is not enough. Re-read the JSON after patching.
- `ClaudeWindow` / `ClaudeVerdictArtifact` **auto-number `artifactLines`** — never write
  `"1. "` into a string.

---

Expected: 13 beats 16:9 at 3840×2160, 10 beats 9:16 at 2160×3840, zero slates, `_qc/REPORT.md`
clean, $0.00.
