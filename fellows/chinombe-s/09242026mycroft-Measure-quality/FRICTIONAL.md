# Frictional log — Adaptive Model Routing Gateway, Sprint 5

## 2026-09-24 — measuring answer quality, not just answer shape

- **Video:** 
- **Drive:** https://drive.google.com/drive/folders/1qJOzaQNE3GbWStgf9_dqkrWMGw8rJnQ6?usp=sharing
- **Report:** [REPORT.md](REPORT.md)
- **Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/2a002da9e20c6887e1cac7dbbeb45ba93cd16152

**What I was working on.** Sprint 5 of the routing gateway: giving it a way to
say an answer is *good*, not just well-formed. Written the same day.

**What I tried, and what I expected.**
- Two pieces: a human answer key for the four extraction fixtures, and a judge
   a strong model comparing a cheap model's answer against a mid model's.
- I expected the answer key to be the quick half and the judge to be the hard
  half. That was backwards.
- For the judge I expected the mid tier to win most comparisons. That is the
  assumption the whole "escalate to a better model" design rests on.

**Where it resisted, and what I did next.**
- Three attempts at the answer key produced three wrong keys. The first typed
  the prompt text in as an answer ("Enter to keep" became a required field
  name). The last one keyed `extract-002` as `direction: up` when the CFO in
  the fixture says "lowering". I froze that into the manifest before anyone
  checked it.
- Root cause was not carelessness with the fixtures so much as the tool: the
  terminal prompts show one field at a time with the fixture text already
  scrolled off screen, and there is no way back. I restored the files from git
   nothing invented reached a commit  and we replaced the flow with an
  answer sheet (`label.py --template`) that writes the fixture text and the
  answer into one JSON file I edit in VS Code, then prints every before/after
  and waits for confirmation. That is still unfinished; it is a ten-minute job
  now rather than a blocked one.
- The judge's first full run failed three of eight answers with `no_citation`.
  The answers were correct and cited the right passage  the mid model wrote
  its citation as 【0】, fullwidth brackets, and the validator only matched
  ASCII `[0]`. In production every one of those is an escalation to a more
  expensive model bought by a punctuation character. Fixed in `validators.py`
  by translating fullwidth brackets before matching, with a test that an
  out-of-range citation still fails. This is the second bug of exactly this
  shape (Sprint 4 had one with quote spans), and both were only visible by
  reading the raw model output rather than the pass/fail column.
- Judging the same pair twice does not give the same verdict. `rag-001` came
  back `tie` in one run and `inconsistent` in the next two. The models rewrite
  their answers each run, so one sweep is one sample.
- My Sprint 5 commit then replaced `FINDINGS.md` with its new section instead
  of appending it, dropping 253 lines, and left the RUN_LOG entry out
  altogether. Recoverable from the previous commit, and being fixed forward
  rather than by rewriting pushed history. Third logging slip on this project,
  which makes it a habit rather than an accident  the pattern is that I treat
  the record as the last step, when it should be part of the same edit.

**What Claude contributed, and what I did with it.**
- I wrote `bench/judge.py`, `bench/judge_run.py` with the guidance of Claude and their tests, and the
  fullwidth-bracket fix. I ran every command myself; nothing was executed on
  my behalf.
- Claude helped with the structure and debugging
- Accepted: running every comparison twice with the answers swapped, and
  recording a disagreement as `inconsistent` instead of picking a winner. I
  had not thought about position bias at all, and three of fourteen
  comparisons turned out to flip.
- Accepted: keeping the judge out of the request path. The run proved why —
  judging a pair costs 2.4x what producing the pair costs.
- Rejected/changed: after three failed labelling sessions I said this was
  taking too long and had become the same loop repeating. We dropped the
  interactive tool for the answer sheet and moved the judge ahead of the key,
  since it did not depend on it.
- Evidence: commit
  [`2a002da`](https://github.com/nikbearbrown/mycroft/commit/2a002da9e20c6887e1cac7dbbeb45ba93cd16152);
  `logs/gateway/runs/2026-09-24T*-sprint5-judge.jsonl` (every call, with cost)
  and `scripts/gateway/bench/results/2026-09-24T*-sprint5-judge.json`.

**What I understand now, and what I still do not.**
- Understood: a free check can only see an answer's *shape*. Nothing in the
  request path can catch an answer that is fluent and wrong, and buying that
  ability costs more than the answer did.
- Understood: across 14 comparisons the cheap model never lost  10 ties, one
  mid win, no cheap wins. If that survives checking, the case for routing
  cheap by default gets much stronger, because the expensive tier is buying
  almost nothing on this kind of work.
- Not understood: whether the judge's verdicts mean anything. They are model
  judgments no human has checked. Sprint 6 is me hand-scoring the same pairs
  blind and measuring how often we agree  and if agreement is poor, the
  honest outcome is reporting that quality cannot be measured this way for
  these tasks, not tuning the judge until it agrees with me.
- Not understood: how much of the tie rate is real and how much is the judge
  defaulting to TIE on short answers. Longer fixtures would test that.
- Open: 8 open-ended fixtures against a target of 30 per type; the extraction
  answer key; `main` is 25 commits behind.