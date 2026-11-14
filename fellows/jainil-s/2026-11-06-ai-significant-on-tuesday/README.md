# Significant On Tuesday

**Track:** educational (STEM / AI) · **Week ending:** 2026-11-06

> Keep checking an A/B test, and you will eventually see noise. Not because
> the test is broken — because looking is itself a decision, and nobody
> counted how many times you looked.

Two cuts delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short at
2160×3840, both 2:22. **No video files are in this repo** — this is the record
of how they were built and why each claim holds.

## The argument

Run an A/B test. Check it every hundred visitors and stop the moment it reads
significant. That is the habit almost every dashboard encourages, and it does
not do what it looks like it does.

Simulate it honestly: 20,000 experiments in which the two arms are **identical
by construction**, both converting at 10%, 2,000 visitors per arm, a test every
100 visitors. Nothing is being measured except the procedure itself, so every
"winner" is a false positive.

| How you look | False winners |
|---|---|
| Once, at the end | **5.0%** — exactly what a 5% test promises |
| Twice | 8.6% |
| Five times | 14.6% |
| Ten times | 19.6% |
| Twenty times | **25.4%** |

The test never got worse. It was given more chances to be wrong.

**The second finding is the one that should worry you.** Among the 5,081 runs
that did stop early, the *measured* difference was never small. The smallest
was 1.8 percentage points; the median was 4.4. The true difference was zero.
There is a visible hole in the distribution across zero — not one run in 5,081
stopped having measured a difference within 1.5 points of the truth.

The reason is mechanical, not statistical bad luck: a small effect is never
significant at a small sample, so the only way to cross the line early is to
have measured a large one. Every early stop is therefore an *overstatement* by
construction. If your past wins were called early, this is what they looked
like.

**The fix is not to stop looking — it is to move the line.**

| Boundary | False winners | |
|---|---|---|
| `z > 1.96` | 25.4% | the textbook line, built for one look |
| `z > 3.02` | 1.8% | Bonferroni — safe, but over-corrected |
| `z > 2.66` | **5.1%** | calibrated for twenty looks |

Same data, same peeking, one number changed.

And it is not free. A wider boundary needs a bigger cap, so below roughly 65%
power a group-sequential design spends **more** visitors than a single fixed
test. Above that it spends fewer — 19% fewer at 80% power, 35% fewer at 90% —
because a real effect gets called early and the test stops. The reel states
both directions.

## Reproduce it

```bash
python peeking_evidence.py && python beat_data.py && python power_tradeoff.py
```

Seed `20261106`, `numpy` and `scipy` only, a few seconds each. Every figure in
the video is printed by these scripts; the beat sheet is populated from their
JSON output rather than retyped.

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Significant Tuesday, not today — which reading do you trust? |
| B01 | BLUF | `BrutalistHesitantWriter` | types **truth**, deletes it, types **noise** |
| B02 | SETUP | `ThresholdWalk` | One A/A run crosses at n=100 and settles back to zero |
| B03 | BODY | `ClaudeBarChart` | 5.0 → 8.6 → 14.6 → 19.6 → 25.4 |
| B04 | BODY | `DistributionShape` | What the early stoppers measured, and the hole across zero |
| B05 | BODY | `CardSet` | Three boundaries, three error rates |
| B06 | LAND | `ThresholdWalk` | The same twenty numbers against the calibrated band |
| B07 | HANDOFF | `ClaudeComposerAsk` | A prompt that reproduces the finding on your own data |
| B08 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

`ThresholdWalk` and `ThresholdWalk916` — a series walking against a symmetric
decision band, with the excursions called out. GATE L turned up nothing
reusable: `PositionCurve` has no band and lights the minimum rather than the
excursions, `DoubleDescentCurve` carries a reference line but is welded to a
log-log error-against-capacity argument, and every other near hit was a
single-reel figure exposing only a `sparkLine`. The punt is logged in
`TEMPLATE-MISSES.md`.

The portrait companion **swaps the axes** and runs time down the frame rather
than across it. Keeping the landscape orientation left the plot at about 55%
cover — sitting on the GATE V fill floor instead of clear of it — and the
vertical layout reaches about 73%. `TimelineSplit916` made the same call for
the same reason.

Every other beat rendered on existing shared components, unmodified.

## Honesty notes

- **This is an A/A test, and that is the point.** The arms are identical by
  construction, so no effect size is assumed and every significant result is
  false by definition. It measures the *procedure*, not a product.
- **Two errors were caught during the build and both are recorded.** The
  power comparison was first made at a fixed horizon, which rigs the result
  against the correct procedure; it was redone at matched power, and the
  honest answer is less flattering than the usual claim. The winner's-curse
  histogram was first binned over ±8 pp, which silently discarded a sixth of
  the mass and drew both lobes as if they ended at the axis; the range is now
  ±15 pp with the remainder clipped rather than dropped, and an assertion
  fails the script if mass is ever lost again. Full detail in `FACTCHECK.md`.
- **"Below about 65% power" is a bracket, not a measured threshold.** The
  measured points are +15% at 50% power and −3% at 65%; the crossover lies
  between them and was not resolved more finely.
- **No claim about how often teams actually peek,** and no attribution of the
  replication crisis to this mechanism. Both were available as rhetoric and
  both were cut.
- **Sequential testing is not sold as a free saving.** It costs visitors below
  roughly 65% power, and the reel says so in the same breath as the benefit.
- **Scope.** Bernoulli conversion data, equal arms, pooled two-proportion z.
  Not ratio metrics, variance reduction, clustered assignment, or unequal
  allocation.

## A note on `qc/`

This folder carries the **final-cut** GATE V reports and contact sheets for
both cuts. It deliberately does **not** carry the `qc-sheet.png` review-cut
images that earlier folders here include.

A review compile burns a beat-marker slate across the bottom of every frame.
That slate genuinely crosses title-safe, so GATE V reports `edge-bleed` on
100% of frames — and the run overwrites `_qc/REPORT.md` in place, replacing a
clean reel's report with one that says it is broken. The trap is recorded as
A18 in `bugs-and-fixes/authoring-gotchas.md`. The evidence that matters —
what the delivered frames actually look like, and what the gate said about
them — is here in full.

## What the gates did and did not catch

Worth stating, because "GATE V: 0 BLOCKER, 0 MAJOR" appears twice in this
folder and is easy to over-read.

Seven defects were found building this reel. **One** failed a command: three
cards overflowing title-safe in the portrait cut, which `compile.py` refused
to write. The other six exited 0 and looked correct — a power comparison
rigged at a fixed horizon, a histogram silently discarding 16.5% of its mass,
a hand-transcribed array that did not match its source, a band tint
highlighting the wrong side of its own threshold, a 720p file compiled as the
"master", and three labels stacked on top of one another that GATE V passed
18 frames 0/0.

The gate measures the content bounding box: fill, edge bleed, clustering. Two
labels that overlap each other are both inside that box and both count toward
fill. **A clean GATE V means the frame is correctly sized, not that it is
readable.** All seven are written up as A19–A22 in the ledger and in
`FRICTIONAL.md`.

Full ledger in `FACTCHECK.md`, method and prior work in `SOURCES.md`, build
record in `FRICTIONAL.md`.
