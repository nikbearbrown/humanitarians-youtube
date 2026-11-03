# BUILD-LOG — The Constraint Isn't Speed

Skill: `ai-explainer` chassis, `claude-hai` channel (@HumanitariansAI, Kokoro
`am_onyx`, Pragmatist, student audience).
Topic: the emergence of 6G, and its pros and cons for IoT.

## How the brief was handled

"Pros and cons" invites two bullet lists, which is the weakest possible shape —
nothing stops it becoming a feature inventory. The ask that fixed it:

```
claude "what actually decides whether an IoT deployment happens? Rank the real
constraints — then check whether the new generation's headline numbers are on
that list at all."
```

They are not. **POWER / COVERAGE / COST PER NODE** became the framework, and
both the upside (B04, B05) and the downside (B06) are scored on those same
three axes, so the verdict in B08 is a comparison rather than a tally.

## The falsifiability beat

```
claude "find the forecast that would embarrass this technology's marketing —
from a named source, about the year it launches."
```

Ericsson's own IoT forecast: in **2030**, 6G's launch year, **40%** of cellular
IoT connections are still projected to be NB-IoT and LTE-M — technologies
introduced **2015–2017**. A vendor with every incentive to sell the next
generation, projecting that four in ten connections will not use it.

## Discipline for a forward-looking topic

6G coverage is overwhelmingly projection, so three rules were applied:

1. **Only named standards bodies or named forecasts.** ITU-R, 3GPP, Ericsson.
   No trade-press figures.
2. **Forecasts are spoken as forecasts** — "projects", never "will be". Three
   rows in FACTCHECK.md are marked PASS-AS-FORECAST for exactly this.
3. **The most quotable number was cut.** IMT-2030's peak-rate and latency
   targets were available and are absent: they would undercut the thesis and
   date the reel the moment the targets are revised. Reasoning in FACTCHECK.md.

One claim was deliberately weakened. An early draft said 5G's massive-IoT
promise "never materialised" — commentary, not measurement, and a verdict on a
previous generation. The beat now makes only the narrower claim the forecast
supports.

## PROOF compliance

| Criterion | This cut |
|---|---|
| Explicit framework | B02 — POWER / COVERAGE / COST PER NODE at **26.90s**, ahead of the first 6G capability claim at 79.08s. Past PROOF's "~20s"; measured and recorded, not rounded |
| Reusable rubric | The three constraints apply to any connectivity decision, not just 6G |
| Worked example | B04→B05→B06, one constraint at a time, pros and cons on the same axes |
| Falsifiability | B07 — the framework predicts a generation will not displace what already satisfies the three; the 2030 forecast tests it |
| Active task | B09 — the viewer applies the three constraints to their own project, GOOD/BAD |
| Friction | B01 sets the two lists side by side before the viewer knows which one decides |

## Gate record

```
GATE L   searched before authoring; no reusable hit; 8 beats authored as Manim
GATE F   full paperwork set written up front
GATE A   clean on all eight, FIRST PASS
GATE W   clean on all eight, FIRST PASS
GATE B   pixel-true — 0 errors, 0 warnings, FIRST PASS, no re-renders
```

Seven reels in, the layout helpers have needed no changes for three
consecutive builds: kicker at buff 0.72, content-adaptive box widths,
`fit_src()` reserving the citation strip, every label composed into the fitted
group, `_fit()` scaling up as well as down, never a line through text.

`./art run` prints "22 BLOCKER" because GATE V reads `*-slate.mp4`, the review
cut, whose timecode burn-in sits outside title-safe by construction.

## 4K master

`./art final` recompiled at 2160 from the existing slots. **No beat was
re-rendered** — every source asset was already native 4K (Manim at 2160p24,
Remotion at `--scale=2`). Verified by `ffprobe`:

```
6G_UdaySonawane_09_18_2026.mp4   3840x2160 @ 24fps   231.45s (3:51)   15 MB
```

The `-slate.mp4` review cut stays 1080p by design.

Nothing here publishes.

## GATE V — measured against the 4K master

```
6G_UdaySonawane_09_18_2026.mp4   463 frames   BLOCKER 0   MAJOR 91
                                              (89 underfill · 2 low-contrast)
```

Underfill is 19% of sampled frames. Mapping every finding back to its beat
gives the useful result:

```
beat   frames   first occurrence
B01       3     +0.8s into the beat
B02       2     +1.1s
B03      16     +1.1s
B04      16     +0.9s
B05       4     +1.0s
B06       3     +0.9s
B07      23     +0.8s
B08      14     +1.0s
B09       1     +0.6s
B10       6     +0.5s   (the sparse outro card)
```

**Every finding begins within ~1.1s of a beat opening. None appears mid-beat or
late.** That is the diagnostic that matters: no settled frame is underfilled —
the flags are entirely the staggered reveals filling up, and the three worst
(B03, B04, B07) are precisely the beats with the most elements revealed one per
narration clause.

Removing the staggering would clear the flags and desynchronise the motion from
the voice, which is a worse reel. Accepted and documented rather than silenced
with `ART_STRICT=0` or padded with content that does not exist.
