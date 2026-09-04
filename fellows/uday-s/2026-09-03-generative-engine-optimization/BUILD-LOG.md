# BUILD-LOG — The Brand That Didn't Exist

Skill: `ai-explainer` chassis, `claude-hai` channel (@HumanitariansAI, Kokoro
`am_onyx`, Pragmatist, student audience).
Subject: `D:/Projects/geo-main.zip` — a GEO research platform (code + results + paper).

## The decision that shaped this reel

The archive ships **both claims and the data behind them**, so the first pass
was verification, not summary. Recomputing every headline figure in the paper's
abstract from `results/` found **seven** that the shipped data does not support
(full table in FACTCHECK.md), including the model name and the direction of the
"context dilution effect".

Every finding's *direction* survives. The magnitudes and setup counts do not.
So the reel reports the measured values, cites the file each came from on
screen, and makes no dilution claim. The abstract's figures appear nowhere.

This is the DOUBLE-CHECK LAW doing exactly what it exists for: a reel that
named real companies while quoting unverifiable statistics would have been the
most damaging thing this pipeline could produce.

## Attribution

**No author names anywhere**, per the author's instruction — this is a topic
explainer, not a work report. On-screen credit is to `results/` filenames and
one external citation (KDD 2024, arXiv:2311.09735). The intro speaks no name.

## PROOF compliance

| Criterion | This cut |
|---|---|
| Explicit framework | B02 — PARAMETRIC / PRESENCE / QUALITY at **21.06s**, ahead of the first result at 39.47s |
| Reusable rubric | The three levers apply to any "why did the model recommend X" question |
| Worked example | B03→B04→B05 move one lever at a time across the same nine brands |
| Falsifiability | B07 — what mention rate does NOT measure, predicted by the framework: if presence dominates, fiction wins. Carried by B06, which is measured |
| Active task | B09 — prompt that makes a model separate its own levers, with GOOD/BAD |
| Friction | The strongest of the four reels: B06 lands the fictional-brand result *before* B07 explains it, so the viewer feels the problem first |

## Gate record

```
GATE L   searched before authoring; no reusable hit; 8 beats authored as Manim
GATE F   failed once — SHOTLIST.md and PROMPTS.md were missing. Written, passed
GATE A   clean on all eight after one fix (a stale duplicate assignment in bar_row)
GATE W   clean on all eight, first pass
GATE B   pixel-true — 0 errors, 0 warnings. One fix along the way: B03's mean
         label was positioned relative to the group AFTER fit(), so when the
         group grew it landed on the citation. Composed into the fitted group
GATE V   clean cut: 369 frames, BLOCKER 0, MAJOR 82 (78 underfill · 4 low-contrast)
```

### The FILL-THE-CANVAS bug worth recording

First compile showed **96** underfill frames — far worse than the previous
reels' 8.7%. Root cause was mine and structural: `fit()` only ever scaled
**down**. Content smaller than its band simply stayed small, which is precisely
the defect the FILL-THE-CANVAS LAW describes. `_fit()` now scales toward the
band in both directions, capped so a two-element beat cannot balloon.

That took 96 → 79. A second pass opening vertical spacing on the three sparsest
beats took 79 → 78, i.e. nothing — which is the useful result: **the remainder
is not a scaling problem.** The fill metric measures ink coverage, and beats
built from outlined boxes with a few numbers do not cover 55% of the safe area
at any size. Closing the gap would mean adding content that does not exist.
Stopped there and documented it rather than padding the frames or silencing the
gate with `ART_STRICT=0`.

The 4 `low-contrast` flags each co-occur with a 10–11% fill reading: near-blank
frames at beat openings with too little ink to measure a luminance separation.

## Deliverable

```
GenerativeEngineOptimization_2026-09-03.mp4   1920x1080   184.45s (3:04)
```

4K master needs no re-render: `./art final <reel>`. Nothing here publishes.
