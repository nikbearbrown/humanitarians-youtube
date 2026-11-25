# FACTCHECK — Every Input, Not Just Some

The post's own numbers are Anthropic's (Oct 22, 2026; archived in
`research/anthropic_formal_verification_2026-10-22.html`) and are cited as such.
Numbers we measured are marked so.

| # | Claim | Where | Checked against | Result |
|---|---|---|---|---|
| 1 | Anthropic says AI can prove a program won't crash, on every input (within limits) | B00 | post §01–02: no crash for any input up to 64 MB, on the compiled RISC-V binary | ✅ (post) |
| 2 | seL4: 2 person-years to write, 20 to verify; ten times | B01 | post §01 (citing the seL4 paper); 20 ÷ 2 = 10 asserted | ✅ (post) |
| 3 | ~180 million lines of proof, 239 entry points, a few weeks; ≈ 750,000 each | B01 | post §02: "about 180 million lines of Rocq", 239 entry points in 123 libraries, "a few weeks"; 180,000,000 ÷ 239 = 753,138 | ✅ (post) + arithmetic |
| 4 | Fuzzers sample random inputs; a proof covers every input up to 64 MB, about the RISC-V machine code, machine-checked | B02, B03 | post §02 | ✅ (post) |
| 5 | Recipe: OSS-Fuzz test → RISC-V binary → theorem → Claude's proof → Rocq checks; trust model, wording, checker | B03 | post §02 trust argument; Theorem README "What you have to trust" | ✅ |
| 6 | Toy: 1,000,000 random tests ≤ 1 MiB, 0 crashes; solver finds the crash; after the patch, none ≤ 64 MiB | B04, B00, B07 | `evidence/fuzz_vs_proof.out` (16,777,220-byte input, 0.013 s, unsat after fix) | ✅ measured |
| 7 | Fuzzers cap inputs around 1 MB | B04 | post §03: "typically capped at 1 MB" (links AFL++ config) | ✅ (post) |
| 8 | Hundreds of bugs fixed on the way | B05 | post §03 "hundreds of bugs" | ✅ (post) |
| 9 | Shared workspace: proofs reuse files; 30 of 34 cheaper than alone | B05 | post §4.2 + chart caption; the chart frame shows "Files reused 324 · 30 of 34" | ✅ (post) |
| 10 | Opus 5.5 needs ~40% fewer tokens than Opus 5 | B05 | post §4.1: proves half of 36 tasks with about 40% fewer tokens | ✅ (post) |
| 11 | Theorem has published 90 entry points (32 libraries) | B05 | `evidence/theorem_index.out` at f1fdc8dd; README "90 entry points in 32 libraries" | ✅ measured |
| 12 | "Formally verified" does not mean "bug-free"; x86/ARM + glibc not covered; wrong answers; unproved entry points | B06, B07 | post §05 (modeling + coverage gaps); Theorem README "What a proof does not say" | ✅ (post) |
| 13 | Airbus / avionics use of formal methods | B07 ("not only for avionics") | post §01, citing Astrée on Airbus avionics | ✅ (post) |

## The math (B01)

1. `20 ÷ 2 = 10` — seL4 verification vs implementation effort, in person-years.
2. `180,000,000 ÷ 239 ≈ 753,000` — the post's total lines of Rocq over its proved entry points.

Both asserted in `build_beats.py`. Row 2 is a mean; the post says a *typical*
proof is about 600,000 lines, which the conditions line states.

**Rendered-frame math review (2026-11-09, both aspects):** B01 at 15/50/85/95% of
its 17.74 s and at each row's reveal (2.1 / 8.3 s), in `media/B01.mp4` and the
portrait master. ÷, = and ≈ render; thin-space digit groups (180 000 000, 753 000);
no tofu, no clipping; both reveals inside the 15 s comp. 16:9: both rows at full
size. 9:16: row 2 is the wider and renders smaller, about 2.9% of frame height
(floor 2%).
