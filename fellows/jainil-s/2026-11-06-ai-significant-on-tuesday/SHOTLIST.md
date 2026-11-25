# SHOTLIST — Significant On Tuesday

Week ending 2026-11-06 · `ai-` track · 9 beats · master 16:9 3840×2160.

SHOW authored before narration (SHOW-DON'T-TELL LAW). Durations are the
measured Kokoro `am_onyx` MP3s — the master clock, not estimates.

| # | Act | Scene | Audio | What the viewer WATCHES |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 16.92s | Serif greeting lands · the question types itself · send arms terracotta · two output lines answer it |
| B01 | BLUF | `BrutalistHesitantWriter` | 10.62s (+0.8 lead) | The line types out ending on **truth** · the word goes terracotta, hesitates, deletes · **noise** types in its place |
| B02 | SETUP | `ThresholdWalk` | 18.26s | The band draws and holds · the walk draws left to right · the first point sits *outside* and lights terracotta · it wanders back and settles on zero |
| B03 | BODY | `ClaudeBarChart` | 17.86s | Five bars grow in narration order, 5.0 → 25.4, the twenty-look bar taking the accent as it passes the rest |
| B04 | BODY | `DistributionShape` | 18.75s | The density fills in — two lobes with a visible hole across zero · the empty middle marks terracotta · the readout lands |
| B05 | BODY | `CardSet` | 18.52s | Three boundary cards land left to right · the calibrated one takes the accent |
| B06 | LAND | `ThresholdWalk` | 18.41s | The same walk returns against a **wider** band · nothing lights terracotta · "never crosses" |
| B07 | HANDOFF | `ClaudeComposerAsk` | 19.35s | "Your turn." · the prompt types in and is read aloud · send arms and holds |
| B08 | OUTRO | `HaiTitleOutro` | 3.75s | Title restate, terracotta period, `@HumanitariansAI` beneath |

**Total 142.4s — 2:22.4.** Master minimum 2:00 ✓ · Short cap 3:00 ✓.

---

## The spine

Cold open → hesitant-writer BLUF → body → land → handoff → title outro.
Typing appears in exactly three beats (B00 the ask, B01 the overview being
thought through, B07 the viewer's prompt), as the law requires.

## Why B02 and B06 are the same component

Deliberate rhyme, not wallpaper. B06 replays **the identical twenty numbers**
from B02 and changes one thing: the band. The run that looked like a winner on
Tuesday never reaches the calibrated line. Showing the fix on *the same data
that fooled us* is the argument — a different dataset would prove nothing.
ILLUSTRATE LAW's concern is consecutive beats sharing a scheme; these are four
beats apart and carry opposite conclusions.

## Visual scheme, beat to beat

Walk → bars → density → cards → walk. No two adjacent beats share a shape.

## Accent discipline

One terracotta moment per beat:

- B01 the word being deleted
- B02 the band **and** the point outside it — the same fact stated twice
- B03 the twenty-look bar
- B04 the empty middle
- B05 the calibrated card
- B06 the band alone, with nothing lit against it — the absence *is* the point

## Fill (GATE V)

`ThresholdWalk` is sized on paper before rendering, not adjusted after: plot
0.72W inside a 0.90W safe box = 80% of safe width; the stack ≈ 0.69H against
0.90H = 76% of safe height; ≈ 61% cover against a 55% floor. Portrait swaps
the axes and runs time downward — keeping the landscape layout measured ≈ 55%,
sitting *on* the floor rather than clear of it.

Portrait budget, after the collision fix below: title 0.052 + gap 0.040 +
axis 0.036 + gap 0.040 + start label 0.035 + gap 0.028 + plot 1.060 + gap
0.028 + end label 0.035 + gap 0.040 + caption 0.090 = **1.484** against a
1.600 safe box — 3,205px of 3,456, ≈ 74% cover.

B01 and B08 carry `qc.sparse` waivers, as on every prior reel: the hesitant
writer and the brand card are deliberately empty.

## What GATE V did not catch

Recorded here because the gate's clean report is easy to over-read.

The first portrait cut of B02/B06 had the title overlapping `n = 100 per arm`,
the `ship it?` callout on the title, and `nothing here` on `test statistic` —
and GATE V returned **18 frames, 0 BLOCKER, 0 MAJOR**. Overlapping labels are
still inside the content bounding box, so fill, edge-bleed and clustering all
pass. Caught by reading the PNG. Fixed by giving the labels real rows instead
of floating them as absolutes (A22).

`CardSet916` at three cards *was* caught — `edge-bleed`, and `compile.py`
refused to write the cut — because that one crossed the frame edge (A21).

The lesson for the next reel: a clean GATE V means the frame is correctly
**sized**, not that it is **readable**.
