# Suno, Part One — Your First Song

Part 1 of 3 in the Suno tutorial series for new **Lyrical Literacy**
volunteers — people who join the team with no background in music production, image
generation or AI tools, and until this series had no onboarding material. Internal
training, not promotion. Every screen is rebuilt as a native Remotion scene from the
[interface spec](../2026-09-04-suno-interface-research/) — nothing is screen-recorded.

| | |
|---|---|
| **Runtime** | 3:56 (12 beats) |
| **Format** | 16:9, 3840×2160, 30 fps |
| **Voice** | Kokoro `af_bella` |
| **Presenter** | Rohan V. |
| **Built** | 2026-08-29 → 2026-08-31 |
| **Series** | **Part 1** · [Part 2](../2026-09-04-suno-part-2-the-advanced-tab/) · [Part 3](../2026-09-04-suno-part-3-voices-remixes-and-downloads/) · [interface research](../2026-09-04-suno-interface-research/) |

## What it covers

- what Suno does, and how it works
- getting Pro access through Humanitarians AI
- the interface — the six-item sidebar
- Simple mode and the prompt formula
- generating, and what credits are
- song cards and the three-dot menu

## Files

| | |
|---|---|
| [`beat_sheet.json`](./beat_sheet.json) | the build contract — beats, narration, scenes, props, cues |
| [`cues.json`](./cues.json) | cue name → anchor phrase, for the word clock |
| [`FACTCHECK.md`](./FACTCHECK.md) | every on-screen and spoken claim, and where it comes from |
| [`SHOTLIST.md`](./SHOTLIST.md) | per-beat work order (generated from the beat sheet) |
| [`PROMPTS.md`](./PROMPTS.md) | design intent per scene |
| [`SOURCES.md`](./SOURCES.md) | sources |
| [`BUILD-PROMPT.md`](./BUILD-PROMPT.md) | the build instructions for this part |
| [`CHECKS-REPORT.md`](./CHECKS-REPORT.md) | per-beat classification and register checks |
| [`qc-sheet-16x9.png`](./qc-sheet-16x9.png) | Gate V contact sheet of the delivered master — the Staff Picks artist line in the workspace tile is blurred (other creators' names) |
| [`FRICTIONAL.md`](./FRICTIONAL.md) | the frictional log for this piece of work |

## Sources

The Suno interface as I captured it, distilled into
[`SUNO-UI-SPEC.md`](../2026-09-04-suno-interface-research/SUNO-UI-SPEC.md). The
captures themselves are listed but not committed — see
[`CAPTURES.md`](../2026-09-04-suno-interface-research/CAPTURES.md). Every claim in this part, and which
capture or documentation page it rests on, is in [`FACTCHECK.md`](./FACTCHECK.md).

## Renders

The 4K master is in Google Drive, not in git — renders go to Drive, source and build
assets stay here: [`Suno Tutorials/`](https://drive.google.com/drive/folders/1vvXtT8BbaO0B9NpUJmdDbyCJ3KQsp8Wq) — `suno-part-1.mp4`.

## Rebuild

With [brutalist.art](https://github.com/nikbearbrown/brutalist.art): generate audio
from `beat_sheet.json`, run `align.py` and `sync_cues.py` so every reveal lands on
its spoken word, render the scenes at `ART_REMOTION_SCALE=2`, then `./art final`.
The series' build playbook is in the [interface research](../2026-09-04-suno-interface-research/) folder.
