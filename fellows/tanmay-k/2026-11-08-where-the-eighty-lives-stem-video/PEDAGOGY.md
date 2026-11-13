# Week 30 topic video: PEDAGOGY (Gate P verdict log, append-only)

## Gate P, the long film, draft 2: 2026-11-07

**Verdict: PASS** (Tanmay, "sign gate-p"), read from `READ-ALOUD-v2-signed.md` (13 beats, 728 words). The form: **one dial and one object.** A single time step is drawn first; two tiny models share the same weight block and the same arithmetic (about 200,000 multiply-adds per step, 20 million over a hundred steps); the dial says how much the chip can do at once. The three-panel frame (parameters store, operations compute, overlap waits) is on screen empty from the first frame and fills as each number is earned. With nothing to overlap the two models take the same time (B05); turning the dial up opens the gap (B07); sequence length is a quiet second axis (B08); the gap is shown to belong to model and chip together (B09); the boundary is stated (B11); the viewer counts one step and asks which steps must wait (B12).

## What the read-aloud went through before the pass
- Draft 1 (13 beats, 706 words), then `PROOF-REVIEW.md`: 10/12, gate pending. Wording edits applied in draft 2: B02 to B12 calibrated (B04 "Not roughly. Exactly the same.", B05 "In this test", B06 "mostly one specific thing", B07 "optimized", B09 "I would expect more room", B10 reworded, B12 given the formula and both answers). Picture-side items went into the beat sheet (the empty frame from the start, source lines for the eighty and the memory idea).
- Lint (`GATE-P-LINT.out`): short-sentence flags kept as rhythm; one digit chain (B12's answer, on screen); weight/wait kept with a condition (captions show the spelling).

## Gate P, the Short, draft 2: 2026-11-07

**Verdict: PASS** (Tanmay, "sign gate-p"), read from `READ-ALOUD-SHORT-v2-signed.md` (11 lines, 302 words). Draft 1 (9 lines, 278 words) was reviewed as `PROOF-REVIEW-SHORT.md` (9/12): the heaviest line was split (S02 into S02 and S03, S04 into S04 and S05), the operation count was scoped ("over a hundred steps, ... one multiply and one add"), and S06 now says which model falls behind. Context comes before the first measurement; the Short ends on its own thought (the three numbers) before naming the full film.

## Audio stage decisions: 2026-11-08
Whisper heard "weight" for "wait" in S04, S07, S10 and B07; Tanmay kept all four. B00 (4.00 words per second) and B09 (4.20) run fast; Tanmay kept the pace. No narration changed.

## Gate P re-sign, draft 3: 2026-11-08

**Verdict: PASS** (Tanmay, "Sign Gate P"), after `FACTCHECK.md` found the first timing comparison was not like for like. Six lines changed, all others unchanged from draft 2:
- B02: "That multiplication is the part we count." (was "the whole cost")
- B05: "six point one milliseconds ... six point four ... within five percent" (was six point nine, six point seven, three percent)
- B07: "one point three times ... three point seven times" (was one point four, five point seven)
- B09: "about four times" (was about six)
- S06: "six point one milliseconds ... six point four" (was six point nine, six point seven)
- S07: "One point three times slower. Then three point seven." (was one point four, five point seven)
Signed copies: `READ-ALOUD-v3-signed.md`, `READ-ALOUD-SHORT-v3-signed.md`. Lint: only the weight/wait and digit-chain flags already decided.

## Teaching score at the film level
`PROOF-REVIEW-VIDEO-2.md` (compiled films): the long film 12/12 on the teaching rubric with the production gate passing; the Short 12/12 on the Shorts rubric with all measured checks passing. Figures in that review were updated to the corrected set.

## Open
None for the narration. Fonts (Arial and Menlo) are a recorded open question for staging.
