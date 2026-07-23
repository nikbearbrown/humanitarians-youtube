# Installs, .env & Credentials — video 2

The second video in the **"Brutalist — Claude for Video Production"** playlist on
[@NikBearBrown](https://www.youtube.com/@NikBearBrown). The setup video: it shows where keys live,
what `npx`, `pip`, and virtual environments are and why the toolkit uses them, what the paid
services do — and it spends its hero beat on the single highest-leverage step, **cloning your
voice.** The narration is [`docs/Installs.md`](../../docs/Installs.md) in spoken form. Meta by
design: built by the toolkit, about the toolkit.

## What's here

- `beat_sheet.json` — the heart. 15 beats, ~3.4 min, audio-first (narration is the clock). Intercuts
  concept animations (Manim: B01, B03, B04, B06, B07, B09, B10, B11, B12) with live terminal scenes
  (Remotion: B00, B02, B05, B08, B13, B99). Validated against
  `runtime/schema/beat_sheet.schema.json`.
- `BUILD-PROMPT.md` — the unattended build instructions for Claude Code.

## Build it

Claude Code runs the whole build — you don't render scenes by hand. From the repo root:

```bash
./art todo    youtube/installs      # the beat ledger — what each beat needs
./art fill-in youtube/installs      # render every pipeline beat (all 15 here)
./art run     youtube/installs      # compile the cut
```

Or hand Claude Code `BUILD-PROMPT.md` and let it run the whole thing unattended
(`claude --dangerously-skip-permissions`).

## The labor split (this video, like video 1, proves it)

Run `./art todo` and every beat reports `pipeline` — **zero human beats.** Concept animations and
terminal scenes are exactly what Manim and Remotion are superhuman at, so `fill-in` renders all of
it and leaves no request cards. The human's contribution to this video is the part only a human can
do: writing and approving the narration, judging pacing, and watching the cut to decide whether it
lands.

*Narration needs `ELEVENLABS_API_KEY` + the NikBearBrown voice (`ELEVENLABS_VOICE_NIKBEARBROWN`).
The silent cut (terminal scenes + concept animations, no VO) builds with no keys.*
