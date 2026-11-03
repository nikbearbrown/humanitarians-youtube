# PROMPT — "How AI Image Generators Turn Noise Into a Picture"

The brief, and how each constraint was resolved.

## Constraints given

Rohan, 2026-09-25 — the week's standing brief:

> the other stem video can be something audio related or AI related or an
> intersection of both. I want oyu to plan these cout really carefully. use
> amazing visuals and motion graphics and follow the brutalist framework and the
> recent updates we made too. also download any code changes to brutalist if
> available before starting.

then, on the first proposed topic (how music generators turn sound into tokens):

> i feel like we have already done something similar to video 1. check if thats
> the case.

It was checked against all eleven earlier videos: no tokens video existed, but
two of its planned beats repeated the MP3 video's bitrate point and the
Nyquist/MP3 "lost detail cannot be restored" lesson. It was dropped. Then:

> any other suggestions?

> i want more topics

Fifteen topics were offered in total. Rohan chose:

> let sdo the midjourney one

— topic #12, *How Midjourney Makes an Image from Noise*.

On the framework:

> do whatever the brutalist framework is asking. follow it to the T

## How each constraint was resolved

| Constraint | Resolution |
|---|---|
| Pull Brutalist changes first | origin/main merged before any authoring (two upstream commits: SEIS skills + NEU brand kit, and godot/riff/repoloop + math typesetting). Local scene work committed first; 5 conflicts resolved keeping both sides; scene index regenerated. Toolkit at `11f51b0` + this week's scenes |
| "Recent updates" — MATH-TYPESETTING.md | B03's equations are outlined SVG from the house `typeset_math.py` — no text fallback. matplotlib (its one dependency) was missing on this machine and was installed into `<toolkit>/.pydeps` rather than silently falling back. Algebra checked separately in FACTCHECK.md |
| "Recent updates" — EXECUTABLE-EVIDENCE.md | No pantry stills, no generated pictures of a model. A toy diffusion model was trained from scratch in numpy and every picture in B01–B05 is its recorded output |
| FELLOWS-SUBMISSION.md, to the letter | the exact opening line; AI narration disclosed on screen and in metadata; 3840×2160 + native 2160×3840; `ImageDiffusion_RohanV.mp4` in `landscape/` and `vertical/`; SHA-256 + source commit per export; README in the guide's template |
| Not a repeat of earlier videos | image generation has never been covered; audio is not touched at all |
| "Amazing visuals and motion graphics" | five new components, each driven by real data and the word clock — see PROMPTS.md |
| Midjourney-specific but honest | Midjourney's architecture is not published. The reel quotes only Midjourney's own Seeds page and shows the mechanism on an open toy labelled "not Midjourney" |
| Voice | Kokoro `af_bella` — the persistent voice of every Rohan V. episode, recorded in the fellow README |
