# PEDAGOGY — Gate P (narration review before audio)

Weekly work video · Friday 2026-09-11 · Mycroft Finance Investigator

## The one idea

**A review loop that can only ever return "verified" is a rubber stamp with extra steps.
This one returned one yes, one no, and one not yet, and closure stayed blocked.**

## Stands alone

No back-references, no week or episode number.

## PROOF

- **Framework before examples** — B01 and B02 establish bind, re-hash, replay before the
  first outcome appears at B04.
- **The falsifiability beat is B05, and it tests the feature rather than flattering it.**
  The question worth asking of any self-checking system is whether it is *capable* of
  failing. The real run rejected a causal claim a reviewer proposed and left a third request
  open. If all three had come back verified, the feature would be worthless and the video
  would say so.
- **Side-by-side** — B04 holds before and after for all three tasks in one frame.
- **Worked example** — three genuinely different request types run through the loop.

## Honesty notes confirmed at this gate

- [x] **Every figure is copied from the generated report**, not from a summary:
      `reports/generated/mycroft-finance-investigator-follow-up-week37.md`. The before/after
      table, `EXACT_MATCH`, `BLOCKED_PENDING_HUMAN_REVIEW`, and the 1/1/1 counts.
- [x] **B02 is verbatim** via `inspect.getsource(reinvestigation._replay_source)`. Eighteen
      lines, counted; the narration's "four separate conditions end the run" was counted from
      the shown block, not estimated.
- [x] **The before-column values are truncated on screen** from
      `EVIDENCE_COLLECTED_PENDING_OWNER` to `EVIDENCE_COLLECTED_PENDING` so the four columns
      fit without wrapping. Disclosed in FACTCHECK; no value is altered, only shortened, and
      the full string appears nowhere as a different claim.
- [x] **The `VERIFIED` / cause distinction is the spine of act three**, quoting the report's
      own line: *"Verified means the evidence replayed exactly; it does not verify a business
      cause."* This is the single most misreadable word in the feature and the video spends a
      whole beat on it rather than letting it pass.
- [x] **Synthetic review exercise**, stated in B00's framing and the verdict. The report's
      classification is `REVIEW_FOLLOW_UP_EXERCISE_NOT_APPROVAL`.
- [x] **No causal language anywhere**, and the one causal claim in the data is the one the
      system *rejected*.

## Verdict

- Plan: APPROVED — 13/13 Remotion, zero slates. A consecutive `ClaudeWindow` pair at B04/B05
  was caught at authoring time and B05 re-cast as a chip grid.
- Narration: APPROVED — body beats 40–61 words.
- Fact-check (`FACTCHECK.md`): CLEARED.

> VERDICT: PASS (FINAL scope) — prepared by the build agent under the fellow's standing
> delegation. Unlocks audio and the master render. Does not authorize publishing or upload.
