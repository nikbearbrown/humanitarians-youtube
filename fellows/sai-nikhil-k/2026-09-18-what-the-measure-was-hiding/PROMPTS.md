# PROMPTS — What the Measure Was Hiding

**There are no open generation slots in this reel.** All nine beats are
registered Remotion compositions rendered from props in `beat_sheet.json`. No
image model, no stock purchase, no Higgsfield clip, no pantry still. No key is
required and nothing costs money — this is a Fellow Tier build end to end.

This file exists because GATE F requires it, and because two beats carry prompts
that matter — they are just not generation prompts.

---

## B00 — the on-screen typed ask

The `command` prop of `ClaudeComposerAsk`. It is **typed on screen and not
spoken**; the spoken words are `narration_text`, which differs.

> Prot2Vec shipped v0.2.0 and v0.3.0 in one week: nine representations, thirteen
> projections, thirty-one metrics, 411 tests. Don't tell me it got bigger. Tell
> me what the new metrics are defending against — and whether the instrument
> doing the measuring was itself being measured.

---

## B07 — the handoff prompt

The `command` prop of the second `ClaudeComposerAsk`. This one is **both typed on
screen and discussed in narration**, because it is the thing the viewer is meant
to take away and paste.

> Here is a benchmark result I am about to publish. Before you tell me whether
> the score is good, tell me three things: what a random control would have
> scored on the same data, what the result becomes if the representation encodes
> only sequence length, and whether the tooling I used to check my own work is
> itself being checked. Then tell me which of those three I forgot.

---

## The two executed scripts

Not prompts, but they are the reel's only generated content and belong in the
work order. Both are preserved with their stdout under `evidence/`.

| Script | Produces | Deps |
|---|---|---|
| `evidence/coverage_exclusion.py` | every number in B04 | `coverage` 7.8.2 + a Prot2Vec checkout |
| `evidence/lcmc_chance.py` | the numeric check behind B02's algebra | `numpy`, `scikit-learn`, Prot2Vec on `PYTHONPATH` |

Neither imports anything that needs a network or a key. `coverage_exclusion.py`
never executes Prot2Vec — it drives coverage's parser, which is the component
that misfired.

---

## Why there is no Higgsfield beat

The three-way contract in `CLAUDE.md` applies per beat: CLI present and approved
→ clip; present and declined → free path; absent → free path silently. **No beat
here was authored as a candidate.** This reel's argument is that a number can
look fine while measuring less than it claims; every frame is therefore either a
typeset equation, a recorded measurement, or text the author wrote. A generated
video clip would be the one thing in it that stands for nothing.
