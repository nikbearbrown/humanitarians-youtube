# FACTCHECK — Can AI Catch Its Own Mistakes? I Ran the Experiment

Beat-by-beat audit, run 2026-08-12 against `beat_sheet.json`. Every claim checked
against the strongest available source. Nothing was silently repaired — every
correction below was proposed first and applied only after author review.

Sources fall into three classes, and the film labels them differently on screen:

| Class | Treatment |
|---|---|
| **Verbatim from the source draft** | Quoted, with its `beat_sheet.json` path on screen |
| **Published literature** | Cited on screen, **with peer-review status stated** |
| **Our own measurement** | Cited to the results JSON; full transcripts shipped |

---

| Beat | Claim | Verdict | Evidence | Source | Correction |
|---|---|---|---|---|---|
| B1 | "A system cannot reliably audit its own output." | SUPPORTED as a **quotation** — not as a fact | Verbatim; the film never asserts it in its own voice | `nbb-cli-agent-self-verification-failure/beat_sheet.json`, B01 | None — quote rule + source line on screen |
| B1 | The draft contains no measured number anywhere | SUPPORTED | Verified programmatically across every `narration_text` field | Same file | None |
| B2 | "I picked this topic expecting to confirm it" | Statement about the author's own prior | — | — | None — first-person, not a factual claim |
| B2 | "Thirty-three wrong answers, three model setups" | SUPPORTED — **our own data** | Forward reference to B8's result | `results-20260812T014950Z.json` | **ADDED 2026-08-12** — B2 was rewritten to name the film's subject in plain words, which introduced this number. Source line added to the beat, fading in at 34% of the composition; the number is spoken at ~68%. Verified on the frame |
| B3 | The four questions | Framework, not a factual claim | — | The film's own instrument | None |
| B4 | The draft's claimed cause is self-reference — "same weights, same activations, same direction of error" | SUPPORTED — **verbatim** | Direct quote | Same file, **B03** | **FIXED** — first draft named the quote in narration with no source on screen. Source line added, fading by ~14% of the beat |
| B4 | The draft's experiment has two arms | SUPPORTED | Self-verify step, then a Python evaluator | Same file, B02–B06 | None |
| B4 | "This is a subtle mistake. It is absolutely everywhere." | Editorial judgement, flagged as such | — | The film's own view | None — concession is deliberate; the film does not mock the draft |
| B5 | Arms A and B differ only in provenance | SUPPORTED | Identical expression, identical question; only the framing changes | `verify_bench.py`, `run_trial()` | None — both prompts shown side by side, held ≥2s |
| B6 | Sonnet 5 solved 9/10, then 10/10 | SUPPORTED — **our own data** | Revision-1 run | `results-20260811T065935Z.json` | None |
| B6 | The `sonnet5-think` arm had zero trials | SUPPORTED — our own data | `summary.sonnet5-think.first_answer_wrong = 0` | Same file | None — our own defect, shown on screen |
| B7 | The published work uses controlled error injection at three complexity levels | SUPPORTED | Method described in the paper | Tsui, arXiv:2507.02778 (2025) — **PREPRINT** | **FIXED** — citation was voiced only. Source line added on screen, **labelled `preprint`**. This is the film's only appearance of the paper and the only place the peer-review distinction is visible |
| B7 | Corrupting one operator keeps the same four numbers and never equals 24 | SUPPORTED | Enforced and asserted in code for every mutation | `verify_bench.py`, `mutations()` | None |
| B8 | 33 wrong expressions, 99 verdicts, zero missed, gap 0.0 in all three configs | SUPPORTED — **our own data** | Full transcripts shipped | `results-20260812T014950Z.json` | None |
| B8 | "I re-ran the grader twice, because I didn't believe it" | True statement about process | — | — | None |
| B9 | 95% upper bound = 8.7% | SUPPORTED | Exact binomial, n=33, 0 events | Computed; reproducible | None — bound and count welded into one component so they cannot appear apart |
| B9 | Does not refute Tsui — that paper measured 14 open non-reasoning models | SUPPORTED | Model class stated in the paper | Tsui, arXiv:2507.02778 | None |
| B9 | One task; arithmetic with decidable ground truth | SUPPORTED | Task definition | `verify_bench.py` | None |
| B10 | The draft advises adding an external verifier | SUPPORTED — **verbatim** | Direct quote | Same draft file, **B07** | None — shown intact beside the struck claim |
| B10 | The draft claims a model *cannot* audit itself | SUPPORTED — **verbatim** | Direct quote | Same draft file, **B01** | None — shown struck through |
| B10 | "The external check isn't the safety net. It's the instrument." | Interpretive conclusion — the film's own synthesis | Grounded: the rate is knowable only because a deterministic evaluator graded every answer | The film's own reasoning | None — framed as the film's conclusion, not a source's |
| B11 | "A null isn't a failed experiment. It's an experiment that answered." | Editorial argument | — | The film's own view | None |
| B12 | The viewer task | Not a factual claim | — | — | None |
| B13 | Links and attribution | Not a factual claim | — | — | None |

---

## Corrections applied (2026-08-12)

Both came from a PROOF checkpoint run at the Phase 2 → Phase 3 boundary, before
the beat sheet was written. Both are Behavioral Rule 3 — *never let a claim ship
without a visible source at the moment of assertion*.

1. **B4** — the draft's verbatim cause claim was spoken with no quote and no
   source on screen. Added a source line carrying the quote and its
   `beat_sheet.json` B03 path.
2. **B7** — the Tsui citation was voiced only. Added on screen, labelled
   `preprint`.

3. **B2 (2026-08-12, second pass)** — the beat was rewritten after author
   review, because it never named the film's subject in plain words. The rewrite
   introduced a forward reference to *thirty-three*. A source line naming the
   results JSON was added in the same edit rather than after it, so the number
   never existed on screen without its source.

**The timing was the actual defect, not just the absence.** A footer *is* an
artifact, but the footer lands at 80% of a beat, and both claims are made in the
first third. The new source slot fades in by **~14%**. Verified on the shipped
master: B4 at 28% into the beat, B7 at 32%.

## Not asserted anywhere in this film

- That self-verification is reliable in general — B9 caps it at one task and
  below ~9%
- That Tsui is refuted — stated as model-dependence, not error
- That the draft's author is careless — B4 ends on the concession that the design
  mistake is subtle and common, and **no person is named anywhere in the film**

## Deliberately excluded, though true

The draft calls `claude-3-5-haiku-20241022`, **retired 19 February 2026** — the
script as written cannot run. It is a legitimate finding and is documented in
`PEDAGOGY.md`, but it is kept **out of the narration**: it invites a cheap laugh,
and the film's argument is about experimental design, not code rot.

## Causal-language check (PLAYBOOK §1)

The film's own central claim is **negative** — provenance made no difference —
which is the safe direction to be wrong in. Where it describes the draft's
reasoning it quotes rather than paraphrases. B10 separates mechanism from
practice explicitly rather than leaving the audience to infer it.
