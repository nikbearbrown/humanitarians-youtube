# NARRATION — "BLIP: Noisier Data, Better Model?"

Kokoro `am_onyx` · **11 beats · 118.74s (1.98 min) · 328 words · 166 wpm**

Durations are MEASURED from the generated mp3s, not estimated — they are the clock every
scene conforms to (`conform_durations.py` pushes each one into that beat's `durationS`,
and Root.tsx turns it into `durationInFrames`). The two orientations share these exact
files, so the cuts cannot drift apart in time.

**This is the GATE P read:** the eleven lines below, against the animated beats.

| Beat | Act | Length | Words | Narration |
|---|---|---|---|---|
| `B00` | ASK | 6.49s | 18 | A model writes its own training captions, then throws a quarter away. Cleverness, or grading its own homework? |
| `B01` | SUMMARY | 12.22s | 35 | Web images come with junk captions. BLIP makes two copies of itself: one writes new captions, one throws out the bad ones. Retrained on the survivors, fourteen million images beat nine times more raw data. |
| `B02` | FRAMEWORK | 10.39s | 34 | Here’s the audit — four questions for anything trained on data it made itself. Who writes the labels. Is the judge independent. Does the writer take risks. Is there a run with it switched off. |
| `B03` | MECHANISM | 12.18s | 33 | One transformer, three jobs: encode text alone, encode it against an image, or generate it from one. Everything’s shared except the self-attention layers — so a writer and a judge cost two cheap finetunes. |
| `B04` | WORKED-EXAMPLE | 11.78s | 35 | Watch it run. This image’s web caption is metadata, not description, so the filter kills it. The captioner writes a real sentence; that one survives. Corpus-wide, the filter rejects a quarter of what it’s handed. |
| `B05` | EDGE-CASE | 12.52s | 32 | Now break it. Let the filter share weights with the captioner and rejection collapses from twenty-five percent to eight — it stops recognising its twin’s mistakes. Every downstream number drops. Confirmation bias, measured. |
| `B06` | FRICTION | 12.27s | 30 | Here’s the part that should bother you. Beam search writes safe captions: nineteen percent rejected. Sampling writes stranger ones: twenty-five percent rejected. The noisier generator wins — diversity is the payload. |
| `B07` | ABLATION | 13.82s | 34 | Axis four. Same images, same backbone. Bootstrap off: 78.4. Filter alone, captioner alone, then both: 80.6. Nine times the data, unbootstrapped, stops at 79.6 — though on captioning, raw still edges it. |
| `B08` | VERDICT | 10.30s | 28 | So bootstrapping isn’t self-congratulation. It’s generate-and-judge: the judge is a separate copy, the writer is allowed to be weird, and someone published the run with it turned off. |
| `B09` | HANDOFF | 11.88s | 38 | Your turn. Paste this into Claude: run the bootstrap audit on a paper that trains on synthetic data. Quote and grade all four axes, then name the one it leaves unproven. Most papers ace three and skip one. |
| `B10` | OUTRO | 4.89s | 11 | Noisier data, better model — if something independent throws the noise out. |
| | | **118.74s** | **328** | |

## Budget check

SHOW-DON'T-TELL LAW puts body beats at ~45–70 words with the evidence on screen. This reel
runs leaner than that band because the 2:00 cap is the binding constraint and every number
is a counter or a bar rather than a spoken figure. The five body beats average **33 words**;
each one's `shot.show` block lists what the viewer watches while they land.

## Spoken numbers

Kokoro expands decimals, so `80.6` costs four spoken words. B07 carries five figures and is
the longest beat in the reel at 13.82s for 33 written words. That is deliberate: the ablation
is the load-bearing receipt and the bars grow as each figure lands.

## What changed after the first measurement

The first pass measured **122.33s** — over the 2:00 cap. Six beats (B01, B03, B05, B06, B07,
B08) lost a trailing clause each, taking the reel to **118.74s**. Nothing was cut from the
*evidence*; every clause removed was a restatement of something already on screen (B06's
"the filter makes it affordable" survives as that beat's closing card — it just stopped being
said out loud as well).

## What a human still owes this script

Read these eleven lines against the beats and check two things the build agent cannot judge
for itself: **register** (is this the channel's voice, for students who are new to this?) and
**claim calibration** (does the confidence of each line match the strength of the number under
it?). Audio is Kokoro — free and local — so a change costs one regeneration and a re-conform.
