# SOURCE-brief — "How Auto-Captions Find Each Word"

## What was asked for

One of two STEM videos for the week of 26–30 Oct, following the current Brutalist framework (see
[PROMPT.md](./PROMPT.md)). Rohan chose auto-captions from four options; it pairs with this week's AI voices video
and borrows that reel's audio check.

## Who it is for

Lyrical Literacy fellows and the wider Humanitarians AI audience: people who turn on auto-captions, or publish
videos with them, and have seen a name or a number come out wrong. Nothing technical assumed.

## What it must leave them with

The recogniser turns sound into a picture, predicts the words, then works out when each was said from where it
was looking. It is very good on clean speech and falls apart once the noise is as loud as the speech, and it
writes what it expects, even when that isn't what was said. So: read the captions before publishing, check names
and numbers first, and record somewhere quiet.

## Evidence the reel stands on

`captions.py` and its outputs in `evidence/`; the Whisper paper and code for the method; YouTube's own help page
on automatic captions. Details in [SOURCES.md](./SOURCES.md).
