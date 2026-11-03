# SOURCE-brief — "How Apps Find a Song's Tempo"

## What was asked for

The STEM video for the week of 12–16 Oct, following the current Brutalist framework (see
[PROMPT.md](./PROMPT.md)). Rohan chose tempo detection from four options, tested on Western grooves.

## Who it is for

Lyrical Literacy fellows and the wider Humanitarians AI audience: people who have seen a BPM number in
a DJ app, a music library or a song generator's style prompt, and never been told where it comes from.
No maths or signal processing assumed.

## What it must leave them with

An app finds tempo in three steps: where new sounds start, which gap keeps repeating, and which repeat
to call the beat. The last step is the hard one, so the common mistake is a tempo exactly double or
half. So: when a BPM feels wrong, check it against your own tapping, halve or double it, and on live
recordings check the beat grid, not just the number.

## Evidence the reel stands on

`tempo.py` and its outputs in `evidence/`, cross-checked against librosa 0.11.0; Ellis 2007 for the
method; the ISMIR 2004 / MIREX scoring rules for the octave error. Details in [SOURCES.md](./SOURCES.md).
