# It Tested Clean

**Track:** educational (STEM / AI) · **Week ending:** 2026-11-20

> It passed every test, then the feature broke. The model is fine — it was fit
> once on correct data and nobody has touched it since. What changed is how one
> number gets computed at the moment it is asked for.

Two cuts delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short at
2160×3840, both 2:31. **No video files are in this repo** — this is the record
of how they were built and why each claim holds.

## The argument

A model goes to production. Offline it scores **73.4%** accuracy, and it keeps
scoring 73.4% forever. In production it is getting **41.5%**. Nobody changed
the model, nobody deployed anything, and no error appears in any log.

The model really is innocent here: it is fit once, on correct data, to
convergence, and never retrained. The standardiser is fitted on train and
frozen. The **only** thing that varies is how one feature — a 30-day spend
aggregate — is computed at the moment of prediction.

Break it four ordinary ways:

| What changed at serving | Model scored | Lost |
|---|---|---|
| Aggregate only 80% complete | 72.9% | 0.5 pts |
| 12% of lookups filled with 0 | 72.0% | 1.4 pts |
| 30-day window served as 7-day | 64.2% | 9.2 pts |
| Dollars served as cents | **41.5%** | **31.9 pts** |

The offline number is **73.4% on every single row of that table**, because the
offline test reads the warehouse and the model reads the feature store.

**The worst case is worse than having no model.** Fed cents, the average
predicted probability goes from 0.42 to 0.99 — it stops being a classifier and
becomes a machine that says yes. At 41.5% it is beaten by ignoring the model
entirely and always guessing the majority class, which gets 59.1%.

## Would monitoring catch it?

Yes — if it is pointed at the right thing. The same drift check, same
thresholds, two different inputs:

| Pointed at | Result |
|---|---|
| The serving log | PSI **5.91** and **2.04** — alarms on both big skews |
| The warehouse table | PSI **0.001** — identical for all four |

The check is not weak. The warehouse never saw the problem, so a check reading
it is blind by construction — and the warehouse is where monitoring usually
ends up wired, because it is the convenient table that everything else reads.

**So the fix is not a better metric. It is a wire.** Log the features the model
actually received, at the moment it received them, and compare those against
training. That is the only place both numbers exist at once.

## Reproduce it

```bash
python skew_evidence.py
```

Seed `20261120`, **numpy only** — the logistic regression, the AUC and the PSI
are written out in the script rather than imported. Seconds to run.

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 73% offline, 41% live, nothing changed |
| B01 | BLUF | `BrutalistHesitantWriter` | types **model**, deletes it, types **feature** |
| B02 | SETUP | `StageRail` | Warehouse → feature store → model; nothing compares them |
| B03 | BODY | `PairedBars` | Offline flat at 73.4, served collapsing to 41.5 |
| B04 | BODY | `ClaudeBarChart` | Mean predicted probability 0.42 → 0.99 |
| B05 | BODY | `CardSet` | The same check at the serving log vs at the warehouse |
| B06 | LAND | `StageRail` | Model → serving log → compare to training |
| B07 | HANDOFF | `ClaudeComposerAsk` | Compare one feature across both paths |
| B08 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

**Nothing.** `PairedBars` shipped the week before with
`ai-every-group-the-other-way` and carries this reel's central figure
unchanged — here with `total: null`, since these are four independent
comparisons rather than parts of an aggregate. `StageRail`, `CardSet` and
`ClaudeBarChart` are long-standing library.

## Honesty notes

- **The first model was wrong, and it would have proved the wrong thing.** An
  unstandardised, unconverged fit reached AUC 0.61 and two of the four "skews"
  *improved* it — a monotone rescale raising the score means the fit was
  over-weighting that feature, not that skew is harmless. Refit with
  standardisation, logit clipping and convergence before any figure was used.
- **The angle I expected is false here.** I went in assuming the skews a drift
  check misses would be the damaging ones. The opposite holds: the two low-PSI
  cases cost 0.5 and 1.4 points; the two that alarm cost 9.2 and 31.9. The
  angle was dropped, not written around, and what replaced it is the stronger
  finding about *where* monitoring points.
- **Accuracy, not AUC, is the headline** — it is what a product acts on, and
  AUC understates calibration damage. Under the cents skew AUC falls to 0.59
  while accuracy falls below majority-class guessing. Both are in the JSON.
- **The four skews are a chosen catalogue**, not a sample of real incidents,
  and the reel does not present them as one.
- **No claim about how common skew is in industry.** No source for that.

Full ledger in `FACTCHECK.md`, method in `SOURCES.md`, build record in
`FRICTIONAL.md`.
