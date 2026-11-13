# SOURCE-brief — "How AI Voices Read a Script"

## What was asked for

One of two STEM videos for the week of 26–30 Oct, following the current Brutalist framework (see
[PROMPT.md](./PROMPT.md)). Rohan chose AI voices from four options; its sibling this week is the auto-captions
video, which reuses this reel's audio check.

## Who it is for

Lyrical Literacy fellows and the wider Humanitarians AI audience: people who hear an AI voice read their script
every week, and have heard it say a name or a price wrong without knowing why. Nothing assumed beyond reading.

## What it must leave them with

An AI voice never sees the spelling. The text is cleaned up and turned into sounds first, and the voice says
those sounds; that step is where its mistakes come from. Words spelled the same but said two ways, prices and
names are the usual trouble, so: write numbers out, respell names, and reword a line that comes out wrong.

## Evidence the reel stands on

`voice.py` and its outputs in `evidence/`, run on our narrator's own pronunciation step; the Kokoro model card,
kokoro-onnx and espeak-ng's documentation for how that step works. Details in [SOURCES.md](./SOURCES.md).
