# PEDAGOGY — Gate P (narration review before audio)

*Agentic AI: From the Loop to MCP* · Friday 2026-09-11

## The one idea

**A citation survives three checks. Two are string comparisons a machine can do. The third —
does the quote actually support the claim — is judgement about meaning, and it is the only
one that decides whether the answer is true.**

## Stands alone

No back-references, no week or episode number.

## PROOF

- **Framework before examples** — B01 states the three checks before the first table at B03.
- **The falsifiability beat is B05, and it attacks the belief the video's own subject rests
  on.** "If it cites a source, it is grounded" is tested: a claim saying *within 14 days*
  cites a real document and quotes it verbatim, and that quote says *30 days*. Every
  automatic check passes and the answer is false. No stricter string matching would catch it.
- **Side-by-side** — B03 holds all four claims in one frame; B05 puts the claim directly
  above the quote that contradicts it, which is the whole argument in one image.
- **Worked example** — four claims run through all three checks with real output.

## Honesty notes confirmed at this gate

- [x] **No model is called anywhere, and that is deliberate.** `grounding.py` uses only
      string comparison. If a check can be done with string work it should never be
      delegated to a model, and the file demonstrates that rather than asserting it.
- [x] **The code is honest about its own limits.** `check()`'s docstring names what it does
      NOT do, and B06 reads that aloud. A checker that quietly implies it validates meaning
      would be the exact failure the video is about.
- [x] **"Twelve lines" was counted, not estimated.** An earlier draft said nine; corrected
      before audio.
- [x] **The corpus and claims are invented test data**, and the video presents them as test
      answers rather than as a captured product transcript.
- [x] **No vendor, model, benchmark or retrieval product is named.**
- [x] **The verdict names the limit**: only the first two checks can be automated.

## Verdict

- Plan: APPROVED — 13/13 Remotion, zero slates, no consecutive pattern repeats.
- Narration: APPROVED — body beats 29–62 words.
- Fact-check (`FACTCHECK.md`): CLEARED.

> VERDICT: PASS (FINAL scope) — prepared by the build agent under the fellow's standing
> delegation. Unlocks audio and the master render. Does not authorize publishing or upload.
