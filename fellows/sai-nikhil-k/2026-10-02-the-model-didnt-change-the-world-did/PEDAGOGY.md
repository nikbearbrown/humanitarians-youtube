# PEDAGOGY — The Model Didn't Change. The World Did.

Reel `weekly_updates/2026-10-02-the-model-didnt-change-the-world-did/` · slug
`claude-sai-the-model-didnt-change-the-world-did` · host Sai (Kokoro `am_onyx`) ·
`@HumanitariansAI` · Computational Skepticism, the week's second reel.

Intake (2026-10-02): Sai asked for a **generic AI topic, not his project**, gave
Chip Huyen's MLOps guide (https://huyenchip.com/mlops/) as the reference and
proposed MLOps. From three proposed angles he chose "the world moved" (data
distribution shift and label-free monitoring), with the evidence run on **real
public data** (ELEC2). He named nothing to leave out.

## The ONE idea

**A deployed model goes stale without changing, because the world it predicts
moves — and you can see the move before the right answers arrive.** Monitoring
is the "ops" that catches it.

Shown, not asserted: a model trained once on the first year of the New South
Wales electricity market and left alone scores 0.838, then 0.629, and 0.548 by
weeks 45–48 (always guessing DOWN: 0.544). Nothing in it changed; the price
distribution did (KS 0.22 → 0.92). The gap between its training-year scores and
its live scores — computed with no labels — tracked its accuracy across 20
blocks (r = −0.85). A year on, the prices came back and so did the model (0.849).

Two honest edges the reel keeps:

- **Fast labels beat everything here.** ELEC2's answer arrives 30 minutes later,
  so "copy the last answer" averages 0.86 and leads both models in 19 of 20
  blocks. The reel says so, and uses it to make the point: most systems wait
  far longer for their labels, which is why you watch the scores.
- **Retraining is not a free fix.** Refit every four weeks, the model never fell
  below 0.623, but it lost 7 of 20 blocks — including the year the world came
  back (0.623 vs the frozen model's 0.810).

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | "This is Sai." A general topic this week. The skeptical ask: why is an untouched model wrong a year later, and how would I know first? |
| B01 | THE WORD | `ClaudeScienceChipGrid` | MLOps per Huyen's guide: deploying, monitoring, maintaining — plus pipelines, late labels, retraining. |
| B02 | THE DECAY | `ExecutedData` | ELEC2, frozen after year one: 0.838 → 0.629 → 0.548; always DOWN 0.544. |
| B03 | THE NAMES | `TypesetMath` | Covariate shift P(X), concept drift P(Y∣X) (after Huyen 2022), and the KS statistic D. |
| B04 | THE ALARM | `BinaryBranch` | Labels arrive late: wait for them, or watch the scores. The 30-minute-label footnote. r = −0.85. |
| B05 | THE FIX? | `DivergentFates` | Refit every 4 weeks vs left frozen: 12 wins, 7 losses; the frozen model's recovery. |
| B06 | VERDICT | `ClaudeVerdictArtifact` | One page, four bare sentences. |
| B07 | HANDOFF | `ClaudeComposerAsk` (`greeting: "Your turn."`) | A monitoring prompt for any model in production. |
| B08 | OUTRO | `LogoOutro` | "The model didn't change. The world did. Sai." (8 words, inside the 4 s card) |

## ILLUSTRATE LAW check

- Claude UI only at B00, B06, B07. ✔
- Every body beat illustrates; no two consecutive share a pattern: ChipGrid ·
  ExecutedData · TypesetMath · BinaryBranch · DivergentFates. ✔
- SHOW-DON'T-TELL: every beat has an ordered `show` block. ✔
- MATH + EVIDENCE: B03 from Huyen's definitions + the KS statistic used in the
  run; B02 from `evidence/drift_run.out`. ✔
- No positional references in narration. ✔

## 9:16 constraint

`shorts.py --vertical`, same film. All nine beats rewire to registered `*916`
siblings (ComposerAsk916, ChipGrid916, ExecutedData916, TypesetMath916,
BinaryBranch916, DivergentFates916, VerdictArtifact916, LogoOutro916). B01
`sparkLine` "THE OPS IN MLOPS" is 16 chars (one line in portrait).

## Evidence and honesty

- `evidence/drift_run.py` → `drift_run.out`, `drift_run.csv`: ELEC2 from OpenML
  (md5 matches OpenML's checksum), HistGradientBoosting `random_state=0`, a
  protocol fixed in the script's docstring. KS is checked against a by-hand
  sup|F − F′| on every block.
- `evidence/sources_check.out`: Huyen's sentences found verbatim on the live pages.
- **A protocol change, logged:** the first run used all seven columns. A check
  showed the three Victoria columns are a constant fill until the last day of the
  training year, and the frozen model had learned from that one day (its scores
  moved by up to 0.48 when they were reset). The reel's model uses the four NSW
  columns instead. Both runs are in `drift_run.out`; the decay, recovery and alarm
  are the same either way (worst 0.548 vs 0.550; r −0.853 vs −0.846).
- **Data quirks, logged:** the file's normalised `date` column decreases at five
  rows, so time is measured by row order (48 rows a day); the row count implies
  944 days where OpenML's description says 7 May 1996 – 5 Dec 1998. The reel
  speaks in weeks after training, not calendar dates.
- **Not used:** Huyen's citation of a Google study ("60 out of these 96
  failures…") — not re-checked at its source, so not on screen.
- **Not claimed:** that KS predicts decay *ahead* of time. It rose in the same
  blocks accuracy fell; its value is that it needs no labels. It was not perfect:
  0.52 in the first recovered block.

## Attribution

Topic and reference chosen by Sai. Definitions credited to Chip Huyen on screen
(B01 caption, B03 note) and in DESCRIPTION.md. Data: ELEC2, M. Harries (1999),
normalised by A. Bifet, OpenML dataset 151.

## Attribution override

Hosted by Sai in his own name (B00 "This is Sai", B08 "Sai."), Kokoro `am_onyx`,
`@HumanitariansAI`; IN-FOR-BEAR LAW suspended for this series (`greeting_note`).

## Expected build noise (not bugs)

- SKIN LINT asks for `ClaudeTitleOutro` — wrong for this channel.
- GATE V `underfill` on centred cards; B08 declares `qc.sparse`.
- The portrait slate reports edge-bleed on every frame; trust `./art final`.

## Portrait-only edits (in `vertical/beat_sheet.json`, not the parent)

**None.** The derived vertical was rendered as is; every portrait beat passed the
frame review without a portrait-only edit.

## Human review checklist

- [ ] The ONE idea is the one you want, in your words.
- [ ] B01 represents Huyen's guide fairly (it is a reading list; the definition is hers).
- [ ] B04: you're comfortable saying the persistence baseline beats both models here.
- [ ] B05: "retraining is a choice with a cost" is the takeaway you want.
- [ ] The narration below reads as you.

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 18.4s measured (68 words)

> A model passes its tests the day it ships. Eleven months later it is barely
> better than always guessing the same answer, and nobody changed a line of it.
> This is Sai. This week, a general one: MLOps, and the part of it that catches
> this. We will watch a real model go stale on real data, and find an alarm that
> does not need the right answers.

### B01 · THE WORD — `ClaudeScienceChipGrid` · 18.7s measured (61 words)

> First, the word. MLOps borrows its ops from DevOps. In Chip Huyen's guide, to
> operationalize something is to bring it into production: deploying it,
> monitoring it, maintaining it. The model is one piece. The rest is what keeps
> it right after launch: the pipelines that feed it, the answers that arrive
> late, the retraining. This video is about the middle word.

### B02 · THE DECAY — `ExecutedData` · 17.7s measured (55 words)

> Here is a real one. Australia's electricity market, nineteen ninety-six to
> ninety-eight: every half hour, does the price go up or down? I trained a model
> on the first year and froze it. The next four weeks, eighty-four percent
> right. Then sixty-three. By week forty-eight, fifty-five; always guessing down
> scores fifty-four. Nobody changed a line.

### B03 · THE NAMES — `TypesetMath` · 15.4s measured (54 words)

> So what broke? Nothing in the model. The prices it saw after the freeze were
> not the prices it learned on. That is covariate shift. When the same prices
> start meaning something else, that is concept drift. Either can be caught
> without labels: compare this month's scores with training's, and take the
> biggest gap.

### B04 · THE ALARM — `BinaryBranch` · 18.9s measured (68 words)

> In most products the right answer comes later, if at all. Here it arrives in
> thirty minutes, and just copying the last one averages eighty-six percent,
> ahead of both models in nineteen blocks of twenty. Most teams are not that
> lucky. So watch what you have today: the model's own scores. That gap rose as
> the accuracy fell, and fell as it came back, without a single label.

### B05 · THE FIX? — `DivergentFates` · 18.3s measured (63 words)

> So retrain it? It helps, but it is not free. Refit every four weeks on the
> year before, the model never fell below sixty-two percent, against fifty-five
> frozen. But a year after the freeze, prices came back to where they started,
> and the frozen model came back with them, to eighty-five. Retraining had
> chased the strange year, and lost seven blocks of twenty.

### B06 · VERDICT — `ClaudeVerdictArtifact` · 13.8s measured (46 words)

> So: one page. The model did not change; its world did, and later changed back.
> Accuracy needs the right answers, and they come late. The model's own scores
> do not: their shift tracked the decay. And retraining is a choice with a cost,
> not a reflex.

### B07 · HANDOFF — `ClaudeComposerAsk` · 15.3s measured (59 words)

> Your turn. If you have a model in production, paste this. Ask which of its
> right answers you will not see for weeks, and what you can see today instead:
> the inputs, and the model's own scores against training. Then ask what you
> will do when they move: retrain, roll back, or wait for the world to come
> back.

### B08 · OUTRO — `LogoOutro` · 3.3s measured (8 words)

> The model didn't change. The world did. Sai.

**Total: 482 words** → 139.9s measured (2:19). No 180s cap applies to the --vertical cut; audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: PASS — reviewer: Sai Nikhil Kunapareddy date: 10/02/2026
