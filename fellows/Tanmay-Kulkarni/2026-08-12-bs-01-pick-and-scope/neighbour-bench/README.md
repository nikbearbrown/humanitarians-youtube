# neighbour-bench — can a model run the adjacent-profession test?

The measurement behind beats B10 and B10B of *Your Job Description Is Too Generic for AI*.

## The question

The source exercise tells students to paste a role description into an AI and ask it to name
the closest job, then judge whether the description rules that person out. Sensible advice —
and nobody had measured how steady the AI's answer is. This measures it.

| | |
|---|---|
| Claimed cause | the verdict tracks whether the description rules people out |
| Rival | it tracks word count / density of domain jargon |
| Isolating arm | `swapped` — matched to `full` on words **and** domain terms, but not identifying |
| Falsifier | `stripped` — if removing the identifying phrase doesn't flip the verdict, that phrase wasn't doing the work |
| Guarantee | `full` (expect PASS) and `generic` (expect FAIL) anchors, so a run can't silently collect no signal |

## Run it

```bash
python3 -m venv .venv && ./.venv/bin/pip install anthropic
./.venv/bin/python neighbour_bench.py --dry-run          # no key, no spend, NOT evidence
export ANTHROPIC_API_KEY=...                             # or a .env beside the script
./.venv/bin/python neighbour_bench.py --pilot            # 96 calls, ~$0.15
./.venv/bin/python neighbour_bench.py --repeats 5        # 480 calls, ~$0.76
./.venv/bin/python neighbour_bench.py --score results-20260818T043656Z.json
```

`--dry-run` output is labelled **NOT EVIDENCE** everywhere it appears, because canned
responses cannot support a finding about model behaviour.

## The three results files, including the two failures

| File | Revision | Outcome |
|---|---|---|
| `results-20260818T040606Z.json` | 1 | **Failed the gate.** The verdict was dominated by *which* job the model picked, not by the description. Three failure modes: same-profession picks, far-neighbour picks that pass trivially, and near-neighbour picks that fail honestly. |
| `results-20260818T041433Z.json` | 2 | **Failed again.** Pinning the neighbour helped but exposed the real problem: three of six `full` descriptions did not in fact rule out their designated neighbour. **The author's ground truth was the broken component.** |
| `results-20260818T043656Z.json` | 3 | **Measured.** Correctness abandoned as the primary measure; reliability needs no adjudication of who is right. 480 calls, 0 errors. |

## What revision 3 found

Same description, same question, five runs:

| Model | Distinct jobs named / description | Descriptions given >1 answer |
|---|---:|---:|
| `claude-haiku-4-5` | 2.25 | **79%** |
| `claude-sonnet-5` | 2.46 | **71%** |

Pass/fail flipped on **42%** of descriptions (Haiku, free arm). Name the closest job yourself
and that falls to **17%**; Sonnet 5 goes 17% → **8%**. Cross-model agreement rises 67% → 88%.

**Bound:** 24 descriptions, two models, one task, and the author wrote the descriptions. This
does not show models are bad at the task. It shows the answer moves, and that where it moves
is something you control.

**Not claimed:** the `full`/`swapped`/`stripped` correctness rates are excluded from the film.
Revision 2 established they measure the author's item-writing, not model capability.
