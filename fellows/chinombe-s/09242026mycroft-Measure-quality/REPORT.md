# Sprint 5 — Measuring answer quality

**Week:** 21–25 Sep 2026
**Project:** Mycroft — Adaptive Model Routing & Inference Gateway
**Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/2a002da9e20c6887e1cac7dbbeb45ba93cd16152

- **Video:** 
- **Drive:** not yet created
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [Why Jev Is Fast](../09242026jev-speed/)

## What this sprint was for

Everything through Sprint 4 could tell whether an answer was **usable** , not
empty, not truncated, parseable, correctly labelled. Nothing could tell whether
an answer was **good**. Sprint 5 adds that in the only two ways it can be added:
a human answer key where a right answer exists, and a stronger model's judgment
where one cannot.

## What was built

| File | What it does |
|---|---|
| `bench/judge.py` | A strong model compares two answers to the same task. Each pair is judged **twice with the answers swapped**; disagreement is recorded as `inconsistent`, never resolved by picking a side. Verdicts are labelled model judgments. |
| `bench/judge_run.py` | Generates a cheap answer and a mid answer per open-ended fixture, then judges them. Dry run by default, cost ceiling up front, typed confirmation, one timestamped log per run, paced for the strong tier's rate cap. |
| `validators.py` fix | `cites_context` now accepts fullwidth brackets `【0】` as well as `[0]`. |
| `bench/label.py` | Answer-sheet mode: `--template` writes a JSON sheet with each fixture's own text inline; `--from` applies it after showing every before/after and waiting for confirmation. |
| `bench/fixtures.py` | `expected.values` — acceptable answers per field, validated. |
| 22 new tests | 168 passing in total. |

## Results  three runs on 2026-09-24

| Measure | Value |
|---|---|
| Comparisons | 14 |
| Judging calls | 28 |
| tie | 10 |
| mid won | 1 |
| **cheap won** | **0** |
| inconsistent (verdict flipped when the answers swapped) | 3 |
| unparsed | 0 |
| Cost — answers | $0.00240 |
| Cost — judging | $0.00588 |
| **Total** | **$0.00828** |

**Judging costs 2.4x what answering costs**  $0.000420 per comparison against
$0.000172 to produce the pair, plus two strong-tier calls of latency. This is the
quantitative reason the judge can never sit in the request path, and the reason a
"route by judged quality" design would cost more than always using the strong
model.

**Three of 28 correct answers were failed over a bracket glyph.** The mid model
cited `【0】` where the prompt asked for `[0]`, and the citation check saw no
citation at all. In production each is an escalation to a dearer tier bought by
punctuation. Second bug of this exact shape  both were invisible in the
pass/fail column and only appeared on reading the raw answers. After the fix, all
four rag fixtures passed.

**The judge's disagreements are about degree, not direction.** All three
inconsistent results were `tie` one way and a winner the other; never `a` one way
and `b` the other. All 28 replies parsed cleanly.

**The same pair judged twice gives different verdicts.** `rag-001`: tie, then
inconsistent, then inconsistent. One sweep is a sample, not a measurement  which
Sprint 7's baseline has to account for with repeats.

**On open-ended work, the mid tier bought nothing measurable over cheap.** Held
as a hypothesis with evidence behind it, not a result: these are model judgments
no human has checked, on 8 fixtures, with one- to two-sentence answers.

## What went wrong

Three consecutive attempts at the extraction answer key produced wrong keys  one
typed the tool's prompt text in as a field name, another keyed `extract-002` as
`direction: up` where the fixture says *"lowering"*  and the last was frozen
into the manifest before review. The files were restored from git, so **nothing
invented was committed**. The cause was the tool: interactive prompts show one
field at a time with the fixture text scrolled off screen and no way back.
Replaced with the answer-sheet flow, and the judge was moved ahead of the answer
key in the sprint since it did not depend on it.

## Evidence

- `logs/gateway/runs/2026-09-24T132939-`, `T134356-` and `T140037-sprint5-judge.jsonl`
  — every call, with cost
- `scripts/gateway/bench/results/2026-09-24T*-sprint5-judge.json` — both answers,
  both votes and the raw verdict text per comparison
- Commit [`2a002da`](https://github.com/nikbearbrown/mycroft/commit/2a002da9e20c6887e1cac7dbbeb45ba93cd16152)
- Tests: `python -m pytest scripts/gateway/tests -q` (168 passed)

## Limits and open items

- **No progress video or Drive folder for this week yet.**
- **The project's own record is incomplete as of 2026-09-25.** Commit `2a002da`
  replaced `FINDINGS.md` with its new section instead of appending it, dropping
  253 lines, and omitted the RUN_LOG entry entirely. Both are recoverable from
  the Sprint 4 commit; the fix is written but not yet run. Third logging slip on
  this project, which makes it a habit rather than an accident.
- The extraction answer key is still unwritten, and `sent-001` / `sent-004` are
  still keyed wrong.
- Open-ended coverage is 8 fixtures against a target of 30 per task type.
- No judged quality figure here should be quoted until Sprint 6 measures how far
  the judge agrees with a human.

## Next

Sprint 6 hand-scores the same pairs blind and measures agreement. If agreement is
poor, the honest output is that quality cannot be measured reliably for that
task — not a judge tuned until it agrees.