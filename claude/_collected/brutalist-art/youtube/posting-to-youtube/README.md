# Posting to YouTube — video 4

The fourth video in the **"Brutalist — Claude for Video Production"** playlist on
[@NikBearBrown](https://www.youtube.com/@NikBearBrown). The true record of publishing the first three
videos via the YouTube Data API — why the API instead of Studio drag-and-drop, what each video needs,
the publisher's job, the honest gotchas (the `position=`/`manualSortRequired` bug, unlisted-vs-audit
privacy, the ~6/day quota, credential resolution), the default cross-link funnel, and the split: the
machine posts, you decide what goes public. Narration is
[`docs/posting-to-youtube.md`](../../docs/posting-to-youtube.md) in spoken form; the facts come from
[`youtube/PUBLISH-LOG.md`](../PUBLISH-LOG.md). Meta by design — built from posting the videos before it.

## What's here

- `beat_sheet.json` — the heart. 15 beats, ~3.7 min, audio-first. Manim concept beats
  (B01/B02/B04/B07/B08/B09/B10/B11/B12) intercut with live terminal scenes reconstructing the real
  publish session (Remotion: B00/B03/B05/B06/B13/B99), using the three published videos and the
  "Brutalist" playlist as the worked example. Remotion props pre-matched to each component's zod
  schema. Validated against `runtime/schema/beat_sheet.schema.json`.
- `BUILD-PROMPT.md` — unattended build instructions for a fresh Claude Code session.

## Build it

```bash
./art todo    youtube/posting-to-youtube
./art fill-in youtube/posting-to-youtube
./art run     youtube/posting-to-youtube
```

Or hand a new Claude Code session `BUILD-PROMPT.md` and let it run unattended.

*Narration needs `ELEVENLABS_API_KEY` + `ELEVENLABS_VOICE_NIKBEARBROWN`. The silent cut builds with
no keys.*
