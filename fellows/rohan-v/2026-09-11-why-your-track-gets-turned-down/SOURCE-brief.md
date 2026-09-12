# SOURCE-brief — "Why Your Track Gets Turned Down"

## What was asked for

Rohan asked for two STEM topic suggestions, both in audio, then chose:

> Lets go with the loudness and lufs but keep in mind that a lot of people are
> not audio professionals. so they might not understand what a master or a
> squeezed mix is so keep that in mind

Two candidates were offered. The other was "why AI music sounds off" —
generative-audio artifacts. Loudness won on one criterion above all: **it is
measurable locally.** ffmpeg ships an EBU R128 scanner, so every claim could be
produced by experiment rather than recalled, the way the week-02 MP3 reel was.
The AI-artifacts topic would have rested mostly on established results.

## What it was built from

An experiment, run before the beat sheet existed. Full log:
[MEASUREMENTS.txt](./MEASUREMENTS.txt); method and limits:
[SOURCES.md](./SOURCES.md).

| Claim on screen | Where it came from |
|---|---|
| −1.0 / −0.2 dBFS tallest points | measured true peak on both versions |
| −15.3 / −6.6 LUFS | measured integrated loudness |
| +1.3 dB / −7.4 dB platform gains | arithmetic to a −14 target from those measurements |
| 12.0 / 0.7 LU gap | measured EBU R128 loudness range |
| loudness moved, the gap did not | measured after applying an identical −7.4 dB to both files |
| how loudness perception differs from peak | established psychoacoustics, stated in plain language with no invented numbers |
| ≈−14 as a playback target | the most commonly published streaming figure; hedged in both narration and label |

## How the audience note shaped the build

The instruction not to assume audio professionals changed more than the script.
It changed the **component labels**, which are the part a viewer reads without
being told what to look at:

| Would have been | Became |
|---|---|
| TRUE PEAK | TALLEST SINGLE MOMENT |
| INTEGRATED LOUDNESS (LUFS) | HOW LOUD IT ACTUALLY SOUNDS |
| LOUDNESS RANGE (LRA) | GAP BETWEEN THE QUIETEST AND LOUDEST MOMENTS |
| limited / compressed | SQUEEZED LOUDER |

It also set the through-line. For a professional the interesting question is
"what target should I hit". For everyone else it is "why did turning it up
achieve nothing", which is the question B00 actually asks.

## What the measurement changed about the reel

The first attempt at a test signal had no transients, so the "squeezed" version
measured **quieter** than the untouched one — the opposite of the point. The
signal was rebuilt with decaying hits to give it real crest factor, and only
then did compression buy loudness the way it does with music. Recorded in
BUILD-LOG.

## What was deliberately excluded

- **The loudness war history.** Interesting, not actionable, and B04 needed the
  time.
- **Any named platform in the graphics.** Spotify appears once, in B00's typed
  question, because that is how a viewer would phrase it. Every label says
  "the platform".
- **Upward normalisation detail.** Platforms cap or limit when raising quiet
  tracks; the reel's argument only needs the downward case, which is universal.
- **Any claim that loud is bad.** The argument is that loudness is not bankable,
  not that dynamics are virtuous.
- **No individuals named beyond the presenter.**
