# SOURCE-brief — "How Bluetooth Audio Works"

## What was asked for

One of two STEM videos for the week of 16–20 Nov, following the current Brutalist framework (see
[PROMPT.md](./PROMPT.md)), with its motion beats built in HyperFrames and three.js. Rohan chose the topic. It pairs
with this week's other explainer, "How Auto-Tune Works".

## Who it is for

Lyrical Literacy fellows and the wider Humanitarians AI audience: people who listen on wireless earbuds every day
and have noticed the sound cut out in a pocket or run behind the picture, but have never been told what happens
between the phone and their ears. Nothing technical assumed.

## What it must leave them with

CD-quality music is too much data for Bluetooth's audio link to carry reliably, so the phone squeezes it first
with a codec, to about a quarter with SBC, the one every device supports. The radio hops between 79 channels and
shares them with Wi-Fi; adaptive hopping skips the busy ones. Lost packets are sent again, so the earbuds keep a
little music in reserve, and that reserve is the main reason Bluetooth lags. Videos can hold the picture back to
match; games can't. LE Audio brings a new codec and broadcast to many earbuds at once. So: keep your phone close,
pick a better codec if your phone offers one, and use game mode for games.

## Evidence the reel stands on

`bluetooth.py` and its outputs in `evidence/`, including the two clips B04 plays; the Bluetooth SIG, Rohde &
Schwarz and the A2DP documents for the radio and SBC; Apple (via MacRumors), Qualcomm and Sony for the codecs;
SoundGuys and RTINGS for measured latency; Android and Apple for delay reporting; the Bluetooth SIG for LE Audio,
LC3 and Auracast. Details in [SOURCES.md](./SOURCES.md).
