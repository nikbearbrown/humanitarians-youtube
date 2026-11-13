# It Was Still Learning

**Track:** educational (STEM / AI) · **Week ending:** 2026-10-23

> A network can memorise its training set thousands of steps before it works
> out the pattern underneath. In between, every held-out number looks like
> failure.

Two cuts delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short at
2160×3840, both 2:23. **No video files are in this repo** — this is the record
of how they were built and why each claim holds.

## The argument

Grokking: delayed generalisation long after training accuracy saturates. The
task is modular addition, (a + b) mod 23 — all 529 pairs, 60% training, 40%
held out, no pair on both sides. One hidden layer, 96 units, squared
activation, full-batch Adam, weight decay 0.8.

1. **It memorises early.** Training accuracy passes 99% at **step 500**, in
   every one of 8 seeds, and never moves again.
2. **Held-out accuracy at that moment is 0.5%.** Chance across 23 classes is
   4.3%, so it is doing *worse than guessing* — and it stays there for roughly
   another 1,500 steps.
3. **Then it generalises.** Median **step 6,125** to pass 95%, range across
   seeds 4,750–7,750. That is **12× later** than memorisation. 8 of 8 seeds
   get there; final held-out accuracy is 99.8%.
4. **Weight decay is the cause, not a detail.** Same task, same seeds, 10,000
   steps, only the decay changes: 0.0 → 0.9%, 0.3 → 10.4%, 0.5 → 86.3%,
   0.8 → 99.5%. With no decay the memorising solution is stable and the
   network simply stays on it.

The practical point: an early-stopping rule watching training loss, or
validation patience measured in hundreds of steps, discards this model during
the flat stretch.

## Reproduce it

```bash
python grokking_evidence.py
```

Pure numpy, no download, about 70 seconds for the 8-seed main run plus the
weight-decay ablation. It prints every figure spoken or shown in the video,
including the median train/val series plotted on B03 and the four ablation bars
on B04.

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | The stopping decision that looks obviously right |
| B01 | BLUF | `BrutalistHesitantWriter` | "It is not failing" → **still learning** |
| B02 | SETUP | `CardSet` | The task and the model, both deliberately small |
| B03 | EVIDENCE | `DoubleDescentCurve` | Both curves: training flat at 100%, held-out climbing 12× later |
| B04 | MECHANISM | `ClaudeBarChart` | The weight-decay ablation |
| B05 | SOURCE | `FormACard` | Power et al., 2022, verbatim phrase |
| B06 | HANDOFF | `ClaudeComposerAsk` | A prompt for your own early-stopping config |
| B07 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

**Nothing.** This is the first reel where GATE L returned a usable hit for
every beat. `DoubleDescentCurve` (2026-10-09), `CardSet` (2026-10-16) and
`FormACard` all rendered unmodified.

One component was **created during this build but not for this beat**:
`ClaudeBarChart`, a Claude-palette landscape bar chart. The library's existing
`BarChart` imports `../tokens/vox`, where the page is flat white and the accent
is plain ink — so it had been rendering Claude reels off-brand since
2026-09-18. See the ledger entry A15.

`ClaudeBarChart916` gained an adaptive row height during GATE V: at a fixed
height, four bars filled only 38% of a 3840px-tall frame.

## Honesty notes

- **Every number is a property of this experiment**, not of language models.
  "Step 6,125" means nothing outside (a + b) mod 23 at this width and this
  decay, and the reel does not imply otherwise.
- **The squared activation is load-bearing and is stated on screen.** Modular
  addition has Fourier structure that a quadratic unit represents directly,
  which is why this groks in seconds rather than hours.
- **ReLU did not grok here.** At P=31 and P=23 it gave delayed *partial*
  generalisation that plateaued at 53–60% — a different phenomenon, and it was
  not used. Recorded in `FACTCHECK.md`.
- **"Worse than guessing" is a measured claim**: 0.5% observed against 4.3%
  chance, not a figure of speech.

Full ledger in `FACTCHECK.md`, sources in `SOURCES.md`, build record in
`FRICTIONAL.md`.
