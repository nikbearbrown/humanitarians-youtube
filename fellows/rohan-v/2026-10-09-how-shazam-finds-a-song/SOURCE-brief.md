# SOURCE-brief — "How Shazam Finds a Song"

## What was asked for

One of two STEM videos for the week of 5–9 Oct, following the current Brutalist framework (see
[PROMPT.md](./PROMPT.md)). Rohan chose Shazam's fingerprinting from four options.

## Who it is for

Lyrical Literacy fellows and the wider Humanitarians AI audience: people who have used Shazam, or put
music under a video, and never been told how a phone names a song from a few noisy seconds. No maths
or signal processing assumed.

## What it must leave them with

The fingerprint is the loudest points of the sound and the timing between them, and matching is a
vote on one moment. So: a recording under your voice can still be found; a cover or a hum is a
different recording; and not being matched isn't the same as being allowed.

## Evidence the reel stands on

`fingerprint.py` and its outputs in `evidence/`; the 2003 Shazam paper for the method; YouTube's
Content ID help page; Google Research on Hum to Search. Details in [SOURCES.md](./SOURCES.md).
