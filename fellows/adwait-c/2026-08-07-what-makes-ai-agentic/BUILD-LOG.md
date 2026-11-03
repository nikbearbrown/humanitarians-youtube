# BUILD-LOG — Episode 1, "What Makes an AI Agentic"

Built 2026-08-13 (episode dated Friday 2026-08-07). Toolkit: `brutalist.art` pared-down
edition, skill `ai-explainer`. **Total cost: $0.00** — no API key touched at any point.

## Environment

- Python 3.12.6 via `brutalist.art/.venv` (system `python3` is 3.13 and has no `kokoro_onnx`)
- ffmpeg 8.1.2 · Node v22.23.1
- Kokoro `am_onyx`, local model, no download

## Sequence

| Step | Result |
|---|---|
| Authored `beat_sheet.json` | 13 beats, 3 acts, all Remotion patterns that already exist → zero slates expected |
| Wrote + ran `agent_loop.py` | `python3 agent_loop.py` → `rows in the sales file: 3`. B06's `code` prop diffed against the real `run()` — character-for-character match |
| Gate P (`PEDAGOGY.md`) | Signed; audio unlocked. First attempt to generate audio was **correctly blocked** by `generate_audio_kokoro.py` until the gate file existed — the gate works |
| Audio | 13 MP3s, 199.5 s total. Durations are the master clock; no timing was hand-tuned at any point |
| Remotion render | 13/13 beats, foreground via `remotion_scenes.py`, ~80 s per beat |
| Review cut | `…-slate.mp4`, 199.5 s, 13/13 filled, **0 slates** |
| **Visual QC** | 4 defects found (1 BLOCKER, 3 MAJOR) — see `_qc/REPORT.md` |
| Fixes + re-render | B03, B09 re-rendered; one toolkit component bug fixed |
| Clean master | `./art final` → 3840×2160, 199.5 s, 11.9 MB |

## Verification actually performed

Not just claimed:

- **The code runs.** `agent_loop.py` executed; output checked against the file's own logic
  (three data rows in a three-row CSV, header excluded).
- **The frames were read.** Contact sheet plus per-beat PNGs at 50 / 88 / 98 % were opened
  and inspected, not probed. This is how all four defects were found — the mp4 probe
  reported a perfectly healthy 199.5 s file the whole time.
- **The fixes were re-verified by frame**, not assumed from a successful render.

## Toolkit change made during this build

`runtime/remotion/src/scenes/ClaudeWindow.tsx` — the component declared `width`, `height`
and `fontSize` in its zod schema but never read them; the JSX hardcoded 1100 px and
19/32/26/20 px type. Wired the declared props through (`cardW = width ?? 1100`,
`fs = fontSize ?? 19`, derived heading/title/spark sizes) and added an optional
`numbered` prop, default `true`, so printed traces can render unnumbered in mono with
column alignment preserved. **Defaults unchanged — no existing reel re-renders differently.**

This is a local toolkit edit in `brutalist.art`, not in this repo. It sits alongside the
existing local edit from the previous reel (three `ClaudeScience*` compositions shortened
900f → 360f in `Root.tsx`).

## Known-good notes for the next episode

- Beat duration should sit at or under the composition's own length. `remotion_scenes.py`
  truncates a render at the beat's audio duration and freeze-holds if the beat is longer —
  so a 30 s comp on a 12 s beat loses its ending, and a 10 s comp on a 20 s beat freezes for
  half the shot. `ClaudeComposerAsk` is 900f/30 s; the `ClaudeScience*` patterns are
  360f/12 s; `ClaudeCodeBeat` 300f/10 s; `ClaudeVerdictArtifact` 1020f/34 s.
- `ClaudeWindow` and `ClaudeVerdictArtifact` auto-number their `artifactLines`. Never write
  `"1. "` into the string.
- `MedhavyConceptCard` and `CwcConceptCard` have no size props. For anything the narration
  *enumerates*, reach for `ClaudeScienceLayerStack` or `ClaudeScienceChipGrid` — they fill
  the canvas and they show the enumeration.

## Status

Master rendered, QC clean, gates signed. **Not published** — no publishing machinery exists
in this toolkit and no gate here authorizes it.
