# FACTCHECK — State Space Models and Mamba Architecture

Status: **GATE F SIGNED — 2026-08-27. 16 rows PASS, 2 PASS-WITH-WORDING.
No unresolved fixes.**

Third-party sources (published research), so the standard is stricter than for
the previous reel: nothing is paraphrased into a stronger claim than the source
makes, and every number on screen is quoted from an abstract rather than
recalled. Derivations in SOURCES.md.

| # | Claim | Verdict | Basis | Fix applied |
|---|---|---|---|---|
| 1 | Attention is quadratic in sequence length | ✓ PASS | Standard property of full self-attention | — |
| 2 | SSMs keep a fixed-size state → linear cost | ✓ PASS | Mamba abstract: "linear scaling in sequence length" | — |
| 3 | `h'(t) = A h(t) + B x(t)`, `y(t) = C h(t)` | ✓ PASS | Standard continuous-time SSM | Set as plain Text — no LaTeX available |
| 4 | S4 is Gu, Goel & Ré, 2021 | ✓ PASS | arXiv:2111.00396 | — |
| 5 | S4 first to a non-trivial Path-X result | ✓ PASS | Reported for S4 on LRA Path-X | Narration says "first architecture to get a non-trivial result" — matches the source's framing, not "solved" |
| 6 | S4's matrices are identical per token | ✓ PASS | S4 is time-invariant; this is exactly what selection removes | — |
| 7 | Mamba is Gu & Dao, 2023 | ✓ PASS | arXiv:2312.00752, v1 1 Dec 2023 | Narration says "twenty twenty-three" — v1 year, correct |
| 8 | Selection makes Δ, B, C input-dependent | ✓ PASS-WITH-WORDING | Abstract says SSM parameters become "functions of the input". The specific naming of Δ, B and C is the paper's selective-SSM construction | Narration names Δ, B, C; the abstract's own phrase "selectively propagate or forget" is quoted rather than reworded |
| 9 | Input-dependence breaks the convolution path, hence the scan | ✓ PASS | The hardware-aware scan exists because time-varying parameters lose the LTI convolution form | Stated as mechanism, not as a quoted sentence |
| 10 | 5× higher inference throughput | ✓ PASS | Abstract, verbatim | On-screen card credits arXiv:2312.00752 |
| 11 | Linear scaling in sequence length | ✓ PASS | Abstract, verbatim | — |
| 12 | Improves to million-length sequences | ✓ PASS | Abstract, verbatim | — |
| 13 | Mamba-3B ≥ same size, matches 2× size | ✓ PASS | Abstract, verbatim | — |
| 14 | Drops attention and MLP blocks | ✓ PASS | Abstract: eliminates "attention or even MLP blocks" | — |
| 15 | SSMs can't copy unless state grows with sequence | ✓ PASS | Jelassi et al. 2024, arXiv:2402.01032 — theoretical result plus experiments | On-screen line states the conditional exactly: "cannot copy unless the state grows with the sequence" |
| 16 | Not a Mamba flaw; any fixed-memory model shares it | ✓ PASS | Same paper attributes the limit to fixed state size, not to Mamba's design | Narration says this explicitly, so the beat reads as a property, not a hit piece |
| 17 | "Use it for audio, genomics, streaming" | ✓ PASS-WITH-WORDING | Mamba abstract names language, audio and genomics as modalities where it reaches state-of-the-art. "Streaming" is my inference from linear cost + constant state, NOT a paper claim | Narration frames these as advice ("use it when…"), and no performance number is attached to any of them |
| 18 | "Be careful with retrieval / literal recall" | ✓ PASS | Direct consequence of row 15–16 | Stated as guidance, tied to the axis that predicts it |

## Where a weaker claim was chosen deliberately

- **"Non-trivial result on Path-X"**, not "solved Path-X". The stronger phrasing
  circulates informally; the sourced framing is the weaker one, so the reel uses it.
- **"Competed on language"**, not "beat Transformers". The abstract's comparisons
  are size-relative and specific; the reel keeps them that way.
- **No efficiency number is claimed as measured.** Every figure is attributed
  on screen to the paper. The reel benchmarks nothing itself and says so by
  putting the citation under the numbers.

## PROOF's own rule, applied to this reel

"A video that says 'no source, no verdict' must show its own sources on screen,
or it is self-refuting." Every claim beat carries a visible citation: B05 shows
arXiv:2111.00396, B06 and B07 show arXiv:2312.00752, B08 shows arXiv:2402.01032.
The equations beat shows the formulation itself. No claim is voiced without its
receipt on screen at the moment it is made.
