# Suno, Part Three — Voices, Remixes and Downloads

Part 3 of 3 in the Suno tutorial series for new **Lyrical Literacy**
volunteers — people who join the team with no background in music production, image
generation or AI tools, and until this series had no onboarding material. Internal
training, not promotion. Every screen is rebuilt as a native Remotion scene from the
[interface spec](../2026-09-04-suno-interface-research/) — nothing is screen-recorded.

| | |
|---|---|
| **Runtime** | 3:29 (12 beats) |
| **Format** | 16:9, 3840×2160, 30 fps |
| **Voice** | Kokoro `af_bella` |
| **Presenter** | Rohan V. |
| **Built** | 2026-08-31 |
| **Series** | [Part 1](../2026-09-04-suno-part-1-your-first-song/) · [Part 2](../2026-09-04-suno-part-2-the-advanced-tab/) · **Part 3** · [interface research](../2026-09-04-suno-interface-research/) |

## What it covers

- the attach row: + Audio, + Voice, + Inspo
- Create a Voice — record or upload, and its rules
- the Sounds tab
- the three-dot menu — ten actions
- Remix versus Edit
- Extend — keep and recreate
- Download — MP3 free, the rest on Pro

## Files

| | |
|---|---|
| [`beat_sheet.json`](./beat_sheet.json) | the build contract — beats, narration, scenes, props, cues |
| [`cues.json`](./cues.json) | cue name → anchor phrase, for the word clock |
| [`PLAN.md`](./PLAN.md) | the part's plan, scene briefs and the decisions behind them |
| [`SHOTLIST.md`](./SHOTLIST.md) | per-beat work order (generated from the beat sheet) |
| [`PROMPTS.md`](./PROMPTS.md) | design intent per scene |
| [`qc-sheet-16x9.png`](./qc-sheet-16x9.png) | Gate V contact sheet of the delivered master |
| [`FRICTIONAL.md`](./FRICTIONAL.md) | the frictional log for this piece of work |

## Sources

The Suno interface as I captured it, distilled into
[`SUNO-UI-SPEC.md`](../2026-09-04-suno-interface-research/SUNO-UI-SPEC.md). The
captures themselves are listed but not committed — see
[`CAPTURES.md`](../2026-09-04-suno-interface-research/CAPTURES.md). This part has no separate factcheck: its claims,
and the captures each rests on, are set out in [`PLAN.md`](./PLAN.md), including what the
new captures overturned.

## Renders

The 4K master is in Google Drive, not in git — renders go to Drive, source and build
assets stay here: [`Suno Tutorials/`](https://drive.google.com/drive/folders/1vvXtT8BbaO0B9NpUJmdDbyCJ3KQsp8Wq) — `suno-part-3.mp4`.

## Rebuild

With [brutalist.art](https://github.com/nikbearbrown/brutalist.art): generate audio
from `beat_sheet.json`, run `align.py` and `sync_cues.py` so every reveal lands on
its spoken word, render the scenes at `ART_REMOTION_SCALE=2`, then `./art final`.
The series' build playbook is in the [interface research](../2026-09-04-suno-interface-research/) folder.
