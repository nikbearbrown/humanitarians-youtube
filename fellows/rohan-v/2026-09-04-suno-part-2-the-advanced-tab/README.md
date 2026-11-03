# Suno, Part Two — The Advanced Tab

Part 2 of 3 in the Suno tutorial series for new **Lyrical Literacy**
volunteers — people who join the team with no background in music production, image
generation or AI tools, and until this series had no onboarding material. Internal
training, not promotion. Every screen is rebuilt as a native Remotion scene from the
[interface spec](../2026-09-04-suno-interface-research/) — nothing is screen-recorded.

| | |
|---|---|
| **Runtime** | 3:09 (11 beats) |
| **Format** | 16:9, 3840×2160, 30 fps |
| **Voice** | Kokoro `af_bella` |
| **Presenter** | Rohan V. |
| **Built** | 2026-08-30 → 2026-08-31 |
| **Series** | [Part 1](../2026-09-04-suno-part-1-your-first-song/) · **Part 2** · [Part 3](../2026-09-04-suno-part-3-voices-remixes-and-downloads/) · [interface research](../2026-09-04-suno-interface-research/) |

## What it covers

- the Advanced panel, with the lid off
- the Styles box — and what to put in it
- the Lyrics box: Write, Prompt, Instrumental and structure tags
- More Options: exclude styles, vocal gender, Weirdness, Style Influence
- duration, song title, where it saves, and Create
- changing one thing at a time

## Files

| | |
|---|---|
| [`beat_sheet.json`](./beat_sheet.json) | the build contract — beats, narration, scenes, props, cues |
| [`cues.json`](./cues.json) | cue name → anchor phrase, for the word clock |
| [`PLAN.md`](./PLAN.md) | the part's plan, scene briefs and the decisions behind them |
| [`FACTCHECK.md`](./FACTCHECK.md) | every on-screen and spoken claim, and where it comes from |
| [`SHOTLIST.md`](./SHOTLIST.md) | per-beat work order (generated from the beat sheet) |
| [`PROMPTS.md`](./PROMPTS.md) | design intent per scene |
| [`BUILD-PROMPT.md`](./BUILD-PROMPT.md) | the build instructions for this part |
| [`CHECKS-REPORT.md`](./CHECKS-REPORT.md) | per-beat classification and register checks |
| [`qc-sheet-16x9.png`](./qc-sheet-16x9.png) | Gate V contact sheet of the delivered master |
| [`FRICTIONAL.md`](./FRICTIONAL.md) | the frictional log for this piece of work |

## Sources

The Suno interface as I captured it, distilled into
[`SUNO-UI-SPEC.md`](../2026-09-04-suno-interface-research/SUNO-UI-SPEC.md). The
captures themselves are listed but not committed — see
[`CAPTURES.md`](../2026-09-04-suno-interface-research/CAPTURES.md). Every claim in this part, and which
capture or documentation page it rests on, is in [`FACTCHECK.md`](./FACTCHECK.md).

## Renders

The 4K master is in Google Drive, not in git — renders go to Drive, source and build
assets stay here: [`Suno Tutorials/`](https://drive.google.com/drive/folders/1vvXtT8BbaO0B9NpUJmdDbyCJ3KQsp8Wq) — `suno-part-2.mp4`.

## Rebuild

With [brutalist.art](https://github.com/nikbearbrown/brutalist.art): generate audio
from `beat_sheet.json`, run `align.py` and `sync_cues.py` so every reveal lands on
its spoken word, render the scenes at `ART_REMOTION_SCALE=2`, then `./art final`.
The series' build playbook is in the [interface research](../2026-09-04-suno-interface-research/) folder.
