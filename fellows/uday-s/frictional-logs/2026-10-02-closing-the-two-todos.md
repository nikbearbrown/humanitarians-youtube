# Frictional log — closing the DEFINE and APPROVE TODOs

**Date:** 2026-10-02 · **Recipe:** `recipes/market-sentiment-analysis-part-1.md` · `todos_open: 2 → 0`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Close the two typed TODOs the recipe declares openly — a DEFINE on step 5's unattributed
scoring constants, and an APPROVE on gate 5 — and log the run evidence behind them.

## Where the work resisted

- **The RUN_LOG entry was already written.** The task described it as the last unevidenced
  piece, but the steps 1–6 entry had been committed on 2026-09-25. What was actually missing
  was an entry for the gate fixes and the rebase. Writing a second steps 1–6 entry would have
  duplicated the record and made the log less trustworthy, not more.

- **Neither TODO could be closed by doing what it appeared to ask.** The DEFINE wanted the
  scoring constants justified, but no derivation exists — they were copied from an n8n node
  that records no author or backtest. The APPROVE wanted gate 5 cleared, but live mode is
  unimplemented, so approving would have authorised a capability that does not exist.

- **Writing the deny record immediately recreated the defect it was meant to close.** Gate 5's
  test at that moment read `test -f <record>.json || …`. The moment a gate-5 record existed —
  a record whose decision was **no** — the test short-circuited to pass. A refusal cleared the
  gate exactly as an approval would.

- **`-X theirs` on the earlier cherry-picks could have silently dropped other people's RUN_LOG
  entries.** The branch was rebuilt onto a different lineage with a conflict strategy that
  prefers the incoming side wholesale.

## What was done about it

- Checked the log before writing: 18 entries against `origin/main`'s 13, with none of theirs
  missing. Then wrote a 2026-10-02 entry covering only what was genuinely unlogged, pointing
  at the 2026-09-25 entry for the run itself.

- Closed the DEFINE by **defining, not endorsing**: every weight, threshold and keyword list
  restated in the recipe, with the reasoning that they exist so any score the original produced
  can be recomputed — and carry no claim of being analytically sound.

- Closed the APPROVE with a logged **deny**. The closure rule is "a logged gate decision", not
  "an approval", so a recorded refusal closes it honestly. Four grounds and four preconditions
  to reopen are named in the record.

- Rewrote the gate-5 test to read `approved_for_live_action` out of the record rather than
  checking that the file exists. Break-tested four ways: no-call/no-record passes,
  no-call/deny passes, **live-call/deny fails**, live-call/approve passes.

## What was learned

**The same defect reappeared one layer along, within minutes of being fixed.** Gate 5's test had
just been changed from *marker exists* to *no live call recorded*. Adding the decision record —
the right artifact, with the right answer — reintroduced a pass-on-existence check through the
other branch of the same `||`. A test that asks whether a file is there will keep being wrong in
this way; it has to ask what the file says.

**A deny is a closure.** The instinct was to treat the APPROVE TODO as unfinished until someone
said yes. But an unexamined gate and a gate decided *no* are different states, and only one of
them is recorded. Leaving it open indefinitely is how a gate becomes decoration.

**Verify the task's premise before doing the task.** The RUN_LOG entry was described as missing
and was not. Two minutes of checking replaced what would have been a duplicate entry arguing
with itself.

---

# Appended — the attestation, and declining to promote

**Commits:** `8c13b87` (attestation) · branch rebased onto `origin/main` and force-pushed

## What was tried

Write the attestation and promote the recipe to `VERIFIED`, and rebase the branch onto the
current `origin/main`.

## Where the work resisted

- **The promotion could not be done honestly.** `VERIFIED` sits two transitions away, not one.
  Reaching it requires passing through `RUNNABLE-LIVE`, whose gate test is *a live run with a
  human clearing every gate*. No live run has ever happened, and gate 5 was recorded `deny`
  earlier the same day. Setting the field would have asserted both a run that never occurred
  and a clearance that had just been explicitly refused — in a recipe whose whole purpose is
  reconstructable evidence.

- **`origin/main` had moved 33 commits** and now contained steps 4–6, so the branch's own
  steps 4–5 commit was redundant while four others were not.

- **The rebase conflicted on seven generated artifacts.** Reports and agent logs are outputs,
  so a textual merge of them means nothing.

- **The push was rejected** after the rebase, as the remote still held the pre-rebase lineage.

## What was done about it

- Wrote the attestation and left `status: RUNNABLE-SAMPLE` alone, recording the reasoning in
  the attestation, the RUN_LOG and the frontmatter note rather than leaving it implicit — and
  named the five things `VERIFIED` would require, in order.

- Let the rebase drop the redundant commit; resolved every artifact conflict by taking one side
  and then **regenerating** from the scripts, so the committed outputs match the final tree
  rather than a merge of two stale versions.

- Re-ran the full pipeline and all six gate tests on the new base before pushing, then
  force-pushed with `--force-with-lease`.

## What was learned

**The Did-not-test section did the real work.** Writing it honestly — live execution, whether
the score is correct, wrong-entity signals, HTTP failure modes, encoding, volume, the untestable
`redditMentions > 20` branch, the absence of any unit tests, cross-platform behaviour — made the
`VERIFIED` question answer itself. It is hard to write that list and then claim the thing is
verified. An empty one would have been the new "it works".

**A conflict in a generated file is a signal to regenerate, not to merge.** Choosing a side
would have left reports whose cited hashes described neither parent.

**An attestation that cannot promote is still worth recording.** It fixes what was exercised, at
which version, with its boundary stated — which is what makes the next one comparable.
