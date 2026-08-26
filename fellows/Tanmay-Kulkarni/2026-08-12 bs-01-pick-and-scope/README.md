# Your Job Description Is Too Generic for AI — Four Questions That Fix It

> ### Topic
> ## `claude-for-artificial-intelligence/bs-01-pick-and-scope`
>
> | | |
> |---|---|
> | **Collection** | `claude-for-artificial-intelligence` |
> | **Topic name** | `bs-01-pick-and-scope` |
> | **Folder on disk** | `claude-for-artificial-intelligence/claude-liam-bs-01-pick-and-scope` |
> | **Source title** | *Pick a Botspeak Prompt & Nail 'Specific Enough'* |
> | **Series / episode** | The Botspeak Prompt Adaptation (INFO 7375) — episode 1 of 3 in the repo |
> | **Next in series** | `bs-02-five-component-spec` · `bs-03-adapt-and-justify` |
>
> The on-disk folder keeps its historical `claude-liam-` prefix so existing paths, manifests
> and links continue to resolve; the topic itself is `bs-01-pick-and-scope`.

An **8:26** film at **3840×2160**. It asks a plain question — how precisely do you have to
describe your own job before a generic prompt becomes useful for it? — and spends most of its
runtime on the part that turned out to matter more: **which of the four questions you can
actually trust yourself to answer.**

Presented by Tanmay Kulkarni for Humanitarians AI. Narration is local Kokoro (`am_onyx`); no
paid APIs in the build.

---

## Where this came from

**Source topic:**
[`claude-for-artificial-intelligence/claude-liam-bs-01-pick-and-scope`](../../../claude-for-artificial-intelligence/claude-liam-bs-01-pick-and-scope)
— *"Pick a Botspeak Prompt & Nail 'Specific Enough'"*, episode 1 of the Botspeak Prompt
Adaptation series for INFO 7375.

**Its core craft is kept, not replaced.** Bounding a role description until it fits one person
is real skill, and the closest-job test — swap your description into a neighbour's job and see
if it still fits — is a genuinely clever move. This film adopts both and hands them to the
viewer as its own deliverable.

What the rebuild adds is the check nobody had run. The source episode tells you to hand your
description to an AI and let it apply the test. That is a useful habit — and it rests on the AI
giving you a steady answer, which turned out to be measurable. Six further places the episode
can be strengthened are set out in [PEDAGOGY.md](PEDAGOGY.md).

## The framework the film hands over

Four questions, run in order, on any description you write:

1. **Does it rule anyone out, or just describe you?** Most of what people write is true of
   them and equally true of the person at the next desk.
2. **Who has the closest job to yours?** Pick someone far away and you pass for free.
3. **Which words rule that person out?** If you can't point at them, it isn't specific — it's
   just long.
4. **Would someone else agree with you?** If only you can run your own test and get your own
   answer, that's an opinion, not a test.

**Question four is the payoff, and the film proves it the hard way.** The worked example — a
night-shift pharmacist checking discharge medicines against the Beers Criteria — passes
questions one to three and then **fails**. The Beers Criteria turns out to be written by a
panel of doctors, pharmacists *and* nurses, and published by a nursing institute in a series
for nurses. The nurse could write that phrase. The retraction happens on screen, against the
source, because a framework that catches its own author is worth more than a clean example.

## What was measured

The film's central claim is not borrowed. **480 API calls, two models, 24 job descriptions,
five repeats each.** Ask an AI who has the closest job to yours, five times over, and you get
roughly two and a half different answers — for 79% of descriptions on one model, 71% on the
other. Since the pass-or-fail depends on which job it picked, that moves too.

Then the useful part: **name the closest job yourself instead of asking.** Verdict flips fall
from 42% to 17% on one model and 17% to 8% on the other; the two models' agreement with each
other rises from 67% to 88%. One sentence of change, a measurably steadier test.

**The bound is stated on screen with the finding, not after it:** 24 descriptions, two models,
one task, and the author wrote the descriptions. This does not show AI is bad at the task — it
shows the answer moves, and where it moves is something you control.

Two earlier revisions of the experiment **failed**, and both are shipped in the zip. The second
failed because the author's own ground truth was wrong on three of six descriptions. That is in
[EXPERIMENT.md](EXPERIMENT.md) because it is the reason the film teaches a procedure rather
than a verdict.

## Sourcing

Three classes of source, treated differently on screen:

- **Published literature** — cited on screen **with preprint status stated in frame beside the
  numbers**. Both papers are preprints and the film says so out loud:
  [arXiv 2603.18507](https://arxiv.org/abs/2603.18507) (expert personas damage accuracy) and
  [arXiv 2605.29420](https://arxiv.org/abs/2605.29420) (when persona prompting helps).
- **Primary documents** — the [2023 AGS Beers Criteria](https://pubmed.ncbi.nlm.nih.gov/37139824/)
  and its [HIGN nursing-series publication](https://hign.org/consultgeri/try-this-series/american-geriatrics-society-ags-2023-updated-ags-beers-criteria-r),
  both legible at the moment the retraction is made.
- **Our own measurement** — cited to the results JSON, which ships here.

The film never claims the source episode's advice is wrong, never claims either preprint is
refuted, states the limits of its own null out loud, and **names no person**. A verbatim quote
is kept verbatim even where it conflicts with the film's own plainer vocabulary
([FACTCHECK.md](FACTCHECK.md) §1).

Twelve claims present in the source draft were cut rather than shipped unsourced — every
rubric figure among them. That audit is in [FACTCHECK.md](FACTCHECK.md) §4.

## Files

| File | What it is |
|---|---|
| `2026-08-18-your-job-description-is-too-generic.mp4` | the final cut — 3840×2160, 8:26 |
| `beat_sheet.json` | the complete build: narration, measured audio durations, every component and prop |
| `EXPERIMENT.md` | the primary source for every number on screen — method, all three revisions including two failures, and the limits of the result |
| **`neighbour-bench/`** | **the harness itself, readable in the browser — no download needed** |
| ↳ [`neighbour-bench/items.py`](neighbour-bench/items.py) | the 24 job descriptions and their four variants, with a built-in audit proving `full` and `swapped` are matched on word count **and** domain-term count. Run `python3 items.py` to print it. |
| ↳ [`neighbour-bench/neighbour_bench.py`](neighbour-bench/neighbour_bench.py) | the runner and scorer. Reliability is the primary measure; correctness is explicitly demoted with the reason in the docstring. |
| ↳ `neighbour-bench/results-*.json` | all three revisions, including the two that failed, with every model reply in full |
| `neighbour-bench-experiment.zip` | the same files as a single download, for running rather than reading |
| `FACTCHECK.md` | claim-by-claim audit: 18 supported, 3 qualified, 1 retracted on purpose, 12 cut |
| `PEDAGOGY.md` | thesis, framework, falsifiability, evidence discipline, and both GATE P sign-offs |
| `QC-REPORT.md` | build log — every defect found by looking at frames, and a toolkit issue worth fixing upstream |
| `SOURCES.md` | research, citations and verification status |

## Reproducing the measurement

The harness is in [`neighbour-bench/`](neighbour-bench/) — readable directly, or run it:

```bash
cd neighbour-bench
python3 -m venv .venv && ./.venv/bin/pip install anthropic
./.venv/bin/python items.py                         # print the item-matching audit
./.venv/bin/python neighbour_bench.py --dry-run      # no key, no spend
./.venv/bin/python neighbour_bench.py --score results-20260818T043656Z.json
```

Then supply your own `ANTHROPIC_API_KEY` for a real run — 480 calls, about **$0.76**. The full
three-revision spend was **$0.996**. `--dry-run` output is labelled **NOT EVIDENCE** everywhere
it appears, because canned responses cannot support a finding.

## Review status

| Gate | Result |
|---|---|
| GATE P — premise | ✅ signed |
| GATE P — narration | ✅ signed after a read-aloud pass |
| Gate L — beat-mix lint | ✅ clean |
| Gate V — frame-level visual QC | ✅ **0 blockers, 0 majors** |
| Silence sweep | ✅ no gap over 0.55s in 17 beats |
| PROOF Phase 3 | ✅ clear-for-public · teaching **12/12** · production gate **PASS** |

**One known weakness, carried openly:** 16 of 17 beats are Remotion cards (94%), over the
toolkit's ~40% guidance. The teaching spine and legibility are clean; visual variety is thin.
It needs beats rebuilt in another motion language rather than a prop edit, and it is the
standing item for the next two episodes in this series.

## Note before pushing

This repo's `.gitignore` excludes `*.mp4` and `*.mp3`, so **`git add` will silently skip the
video.** Check with `git check-ignore -v <file>.mp4` before assuming it was staged; upload it
through the web UI, or `git add -f`.

Never run a broad `git add .` here, and confirm the branch first — this is a shared repo.

Built with the [Brutalist](https://github.com/nikbearbrown/brutalist.art) free, local video
toolkit (Kokoro TTS + Remotion) — no paid APIs, no keys.
