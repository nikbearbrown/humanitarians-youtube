# When Cowork Can Help Claude Code — video 3

The third video in the **"Brutalist — Claude for Video Production"** playlist on
[@NikBearBrown](https://www.youtube.com/@NikBearBrown). The true story of building the `installs`
video (video 2): Claude Code stalled for an hour on six Remotion beats — "just a couple more minutes"
— chased a phantom "43 stale Chrome processes" that were the user's real browser, and got unstuck in
four commands once a second agent looked from outside. The lesson: any single agent can tunnel; a
different seat with no sunk cost breaks the loop, and the human is the one who calls for it. Narration
is [`docs/cowork-and-claude-code.md`](../../docs/cowork-and-claude-code.md) in spoken form.

## What's here

- `beat_sheet.json` — the heart. 16 beats, ~3.8 min, audio-first. Manim concept beats
  (B01/B03/B05/B06/B07/B08/B10/B11/B13/B14) intercut with live terminal scenes reconstructing the
  actual transcript (Remotion: B00/B02/B04/B09/B12/B99). Remotion props are pre-matched to each
  component's zod schema. Validated against `runtime/schema/beat_sheet.schema.json`.
- `BUILD-PROMPT.md` — unattended build instructions for a fresh Claude Code session.

## Build it

From the repo root:

```bash
./art todo    youtube/when-cowork-helps-claude-code
./art fill-in youtube/when-cowork-helps-claude-code
./art run     youtube/when-cowork-helps-claude-code
```

Or hand a new Claude Code session `BUILD-PROMPT.md` and let it run unattended.

## The point it proves by getting built

Every beat is `pipeline` — zero human beats. If the build stalls, that stall is itself the video's
subject: stop, get a second vantage, use `runtime/scripts/remotion_scenes.py` (foreground), and
verify the result by looking at a rendered frame — not by trusting a green "ok".

*Narration needs `ELEVENLABS_API_KEY` + `ELEVENLABS_VOICE_NIKBEARBROWN`. The silent cut builds with
no keys.*
