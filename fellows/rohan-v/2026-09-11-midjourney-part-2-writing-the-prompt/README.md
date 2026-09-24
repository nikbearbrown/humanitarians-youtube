# Midjourney, Part Two — Writing the Prompt

Part 2 of 6 in the Midjourney tutorial series for new **Lyrical Literacy**
volunteers — people who join the team with no background in music production, image
generation or AI tools, and until this series had no onboarding material. Internal
training, not promotion. Every screen is rebuilt as a native Remotion scene from the
[interface spec](../2026-09-11-midjourney-interface-research/) — nothing is screen-recorded.

| | |
|---|---|
| **Runtime** | 3:16 (11 beats) |
| **Format** | 16:9, 3840×2160, 30 fps |
| **Voice** | Kokoro `af_bella` |
| **Presenter** | Rohan V. |
| **Built** | 2026-09-07 |
| **Series** | [Part 1](../2026-09-11-midjourney-part-1-your-first-image/) · **Part 2** · [Part 3](../2026-09-11-midjourney-part-3-what-to-do-with-one-you-like/) · [Part 4](../2026-09-11-midjourney-part-4-the-settings-panel/) · [Part 5](../2026-09-11-midjourney-part-5-getting-the-same-look-twice/) · [Part 6](../2026-09-11-midjourney-part-6-the-editor-and-where-your-work-lives/) · [interface research](../2026-09-11-midjourney-interface-research/) |

## What it covers

- Midjourney's own seven prompt elements
- subject and medium
- environment and lighting
- colour and mood
- composition
- a real prompt, scored
- what to leave out

## Files

| | |
|---|---|
| [`beat_sheet.json`](./beat_sheet.json) | the build contract — beats, narration, scenes, props, cues |
| [`cues.json`](./cues.json) | cue name → anchor phrase, for the word clock |
| [`PLAN.md`](./PLAN.md) | the part's plan, scene briefs and the decisions behind them |
| [`FACTCHECK.md`](./FACTCHECK.md) | every on-screen and spoken claim, and where it comes from |
| [`SHOTLIST.md`](./SHOTLIST.md) | per-beat work order (generated from the beat sheet) |
| [`PROMPTS.md`](./PROMPTS.md) | design intent per scene |
| [`check_beats.py`](./check_beats.py) | this part's own pre-render checker |
| [`qc-sheet-16x9.png`](./qc-sheet-16x9.png) | Gate V contact sheet of the delivered master |
| [`FRICTIONAL.md`](./FRICTIONAL.md) | the frictional log for this piece of work |

## Sources

The Midjourney interface as I captured it, distilled into
[`MIDJOURNEY-UI-SPEC.md`](../2026-09-11-midjourney-interface-research/MIDJOURNEY-UI-SPEC.md). The
captures themselves are listed but not committed — see
[`CAPTURES.md`](../2026-09-11-midjourney-interface-research/CAPTURES.md). Every claim in this part, and which
capture or documentation page it rests on, is in [`FACTCHECK.md`](./FACTCHECK.md).

## Renders

The 4K master is in Google Drive, not in git — renders go to Drive, source and build
assets stay here: [`Midjourney Tutorials/`](https://drive.google.com/drive/folders/1ibvpFnBZ5tzc1aHFZ0H8dTTspnLSGsfg) — `2026-09-16_midjourney-part-2_16x9.mp4`.

## Rebuild

With [brutalist.art](https://github.com/nikbearbrown/brutalist.art): generate audio
from `beat_sheet.json`, run `align.py` and `sync_cues.py` so every reveal lands on
its spoken word, render the scenes at `ART_REMOTION_SCALE=2`, then `./art final`.
The series' build playbook is in the [interface research](../2026-09-11-midjourney-interface-research/) folder.
