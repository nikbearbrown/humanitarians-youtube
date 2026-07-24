# FACTCHECK — tests-pass-user-fails

## Claims requiring verification

### B03 — "The test suite was structurally incapable of catching the failure"
Source: Chapter 13, section on Pass 3: "The failure is not a bug in the code. It is a gap between the SDD's prose and the score's rows. The handoff conditions I wrote are all satisfied. The need the SDD named is not." ✓ Accurately drawn from source.

### B04 — "Code passes its self-generated tests at high rates while failing human-written tests at much lower rates"
Source: Chapter 13 footnote [llmcode]: "Recent empirical work on agentic code evaluation finds pass@k rates inflate 10–61% when tests are drawn from the same generation event as the code — sometimes called evaluation contamination. See SWE-bench-Live and LiveCodeBench (2024–2025)." Narration is a paraphrase of this footnote. The exact inflation percentage (10–61%) is not stated to avoid range confusion. Directionally accurate. ✓

### B05 — "Tony Hoare made the formal version of this argument in 1969"
Source: Chapter 13 footnote [hoare]: "C. A. R. Hoare, 'An Axiomatic Basis for Computer Programming,' Communications of the ACM 12, no. 10 (October 1969): 576–580. The Hoare triple {P} C {Q} is the formal statement of 'code is correct only with respect to a specification.'" ✓

### B05 — "A program is correct with respect to a specification — never in the abstract"
Source: Chapter 13: "Tony Hoare made the formal version of this argument in 1969. A program is correct with respect to a specification, never in the abstract. Correctness is a relation between code and spec, not a property of code alone." ✓ Direct quote from source.

### B01/B09 — "Nine of nine tests pass"
Source: Chapter 13: "`npm test` reports nine of nine passing." ✓

### B07 — "Claude writes a six-line change and one new test. Ten of ten pass."
Source: Chapter 13: "Claude produces a six-line change and one new test. `npm test` reports ten of ten passing." ✓

### B01 — "Six applications scattered in insertion order"
Source: Chapter 13: "Six applications visible, three submitted with strikethrough, list in insertion order — newest at the bottom." ✓

### B08 — "read each user-need sentence aloud against the running build"
Source: Chapter 13: "You open the SDD to the User Needs section. You read each sentence aloud. After each sentence, you check the running build against it — not by running a test, by using the build. By looking at it. By asking whether a person who had not just built it would experience the sentence as true." ✓ Paraphrase is accurate.

## Exclusions confirmed

No Hoare triple notation ({P} C {Q}) used. ✓
No ISO/IEC 25010 sections. ✓
No Therac-25 or Mars Climate Orbiter anecdotes. ✓
No mutation-testing tool names (mutmut, Stryker, PIT). ✓

## VERDICT: PASS
