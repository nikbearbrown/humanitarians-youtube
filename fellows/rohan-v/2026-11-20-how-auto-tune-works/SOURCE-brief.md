# SOURCE-brief — "How Auto-Tune Works"

## What was asked for

One of two STEM videos for the week of 16–20 Nov, following the current Brutalist framework (see
[PROMPT.md](./PROMPT.md)), with its motion beats built in HyperFrames and three.js. Rohan chose the topic. It pairs
with this week's other explainer, "How Bluetooth Audio Works".

## Who it is for

Lyrical Literacy fellows and the wider Humanitarians AI audience: people who have heard the word Auto-Tune, and
maybe the robotic sound it can make, but have never been told what the software actually does to a voice. No music
theory or maths assumed.

## What it must leave them with

A sung note is a wave that repeats, and how often it repeats is its pitch; software finds it by sliding a copy of
the wave along itself until the two line up. A singer is usually off by a little, measured in cents (a hundred to a
semitone). Correction pulls each moment toward the nearest note in the key you choose, and retune speed decides how
fast: slow keeps the voice natural and the vibrato alive; zero snaps it, the robotic sound made famous by "Believe".
Moving a pitch by speeding the sound up changes its length and, for big shifts, the vowel too; re-spacing single
cycles keeps the vowel. So: set the key first, start with a slow retune speed, and turn it to zero only for the
effect.

## Evidence the reel stands on

`autotune.py` and its outputs in `evidence/`, including the three takes B05 plays; Auto-Tune's 1999 patent for how
it detects and shifts pitch; Antares, NPR and TIME for the release, "Believe" and retune speed; ISO 16 and
HyperPhysics for tuning and cents. Details in [SOURCES.md](./SOURCES.md).
