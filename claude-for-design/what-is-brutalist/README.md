# What is Brutalist? — the intro video

The first video in the **"Brutalist — Claude for Video Production"** playlist on
[@NikBearBrown](https://www.youtube.com/@NikBearBrown). It argues the conductor idea — *you decide,
the machine plays* — and shows the real terminal workflow. Meta by design: it's made **by** the
toolkit, **about** the toolkit. The narration is the repo `README.md` in spoken form.

## What's here

- `beat_sheet.json` — the heart. 16 beats, ~2.8 min, audio-first (narration is the clock). Intercuts
  concept animations (Manim) with live terminal scenes (Remotion): `art fill-in`, `./setup`,
  `art --list / todo / run`. Validated against `runtime/schema/beat_sheet.schema.json`.

## A self-contained folder

Everything for this video lives in this one folder — the beat sheet, the rendered scenes
(`manim/`, `media/`), the audio (`mp3/`), the compiled cut, and the derived ledger (`todo.json`,
`STATUS.md`). You can copy the folder, point the pipeline at it, and it builds in place; nothing
reaches outside it except the shared `runtime/`. One folder = one video.

## Rebuild it

Claude Code runs the whole build — you don't render scenes by hand. Point it at this folder:

```bash
# from the repo root
./art todo    youtube/what-is-brutalist          # the beat ledger — what each beat needs
./art fill-in youtube/what-is-brutalist           # render every pipeline beat (all 16 here)
./art run     youtube/what-is-brutalist           # compile the cut
```

Then swap the narration and beats for your own and run again.

## The render contract (retry, then hand back to you)

When Claude Code renders a scene it **retries up to five times**, fixing its own errors between
attempts. If a scene still won't render after five tries, it **leaves that beat unrendered and moves
on to the next one** rather than stalling the whole build — the beat shows up as a slate in the cut
and stays flagged in `todo.json`/`STATUS.md`. So a finished pass can legitimately contain a few
missing or rough beats.

That's by design: **the human is expected to look at the result and redo some scenes.** Watch the
cut, find the beats that came out unrendered or just bad, and rebuild only those — adjust the beat's
spec in `beat_sheet.json` (the heart) and re-run `fill-in` on it, or fix the scene and re-render.
Running unattended (e.g. `claude --dangerously-skip-permissions`) is fine and fast, but it means
exactly this: the machine gets you a full draft with a few beats left for your judgment, and you
finish the ones only a human should. That review-and-redo pass *is* the human's job — see
`runtime/README.md` for the general contract.

## A note on the labor split (this video proves it)

Run `./art todo` and every beat reports `pipeline` — **zero human beats.** This explainer is
entirely machine-buildable: concept animations and terminal scenes are exactly what Manim and
Remotion are superhuman at. So `fill-in` renders all of it and leaves no request cards.

Which means the human's entire contribution to *this* video is the part only a human can do:
writing and approving the narration (the script), judging the pacing, and watching the finished cut
to decide whether it lands. The score is yours; the playing is the machine's. That is the video's
whole argument, demonstrated by how the video itself gets made.

*Narration needs `ELEVENLABS_API_KEY` + the NikBearBrown voice (`ELEVENLABS_VOICE_NIKBEARBROWN`).
The silent cut (slates/terminal scenes, no VO) builds with no keys.*
