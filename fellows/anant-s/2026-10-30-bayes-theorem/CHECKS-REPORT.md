# CHECKS-REPORT: Bayes' Theorem: The Positive That's Usually Wrong

Current as built (ai-explainer, converted 2026-11-24 from tldr). Words are counted from the narration; seconds are the measured audio. Body classes are carried over from the original proof-gate table; the new beats are SHOW.

| Beat | Role | Class | Words | Sec | On-screen artifact |
|---|---|---|---:|---:|---|
| B00 | ASK | SHOW | 33 | 10.5 | Claude composer: greeting, the ask types in, three result lines |
| B01 | BLUF | SHOW | 35 | 11.8 | hesitant writer: "means you're probably sick" → "can still be a false alarm" |
| B10 | HOOK | SHOW | 37 | 10.3 | "you" square, POSITIVE stamp, P(sick) = ? |
| B11 | INSTANCE | SHOW | 40 | 12.7 | 10,000-square grid counts up; scan over the 100 sick |
| B12 | INSTANCE | SHOW | 46 | 14.8 | scan over the 9,900 healthy; 495 stay lit |
| B13 | NAIVE | SHOW | 47 | 14.0 | box around the sick, 99/100, the 495 outside pulse |
| B14 | SHIFT | SHOW | 41 | 12.2 | the 594 positives regroup; predict hold |
| B15 | TRANSFORM | SHOW | 23 | 8.1 | squares morph into 99/594, then 1/6 |
| B16 | ABSTRACTION | SHOW | 51 | 17.0 | counts → probabilities → Bayes' theorem (MathTex, staged) |
| B17 | TANGENT | SHOW | 75 | 21.8 | five-zone tangent, box spotlight |
| B18 | PAYOFF | SHOW | 51 | 14.6 | the B10 "you" square returns into the block; 1/100 → 1/6 |
| B19 | BOUNDARY | SHOW | 46 | 13.8 | base-rate curve with a sweeping marker |
| BVDT | VERDICT | CARD | 64 | 20.6 | verdict artifact (recap, exempt) |
| BHTF | YOUR TURN | SHOW | 122 | 35.7 | composer prompt plus three check lines |
| BOUT | OUTRO | CARD | 11 | 5.5 | locked title outro |

**Total: 722 words · 223.4 s (3:43).**

## ai-explainer spine audit

| Slot | Required (ai-explainer SKILL.md) | This film | ✓ |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` cold open with result lines; Liam introduced in the first breath | "Hello, this is Liam, in for Bear. The ask: a tes…"; three output lines | ✓ |
| B01 | `BrutalistHesitantWriter` BLUF, 20–35 words, `lead_silence_s: 0.8`, window ≥ 9 s, whole-phrase correction | 35 words; lead 0.8 s; 11.8 s | ✓ |
| Body | Manim lesson beats | B10, B11, B12, B13, B14, B15, B16, B17, B18, B19 | ✓ |
| BVDT | `ClaudeVerdictArtifact`, opens "Let's recap with Claude." | 4 lines | ✓ |
| BHTF | `ClaudeComposerAsk`, greeting "Your turn.", prompt read verbatim | unchanged | ✓ |
| BOUT | `ClaudeTitleOutro` (locked) | unchanged | ✓ |

The final passed GATE V, GATE T, the bookend check, the label and bottom-strip check, the master check and loudness. See BUILD-LOG.md for the values.

## History: original tldr checks report (2026-11-22, kept verbatim)

Beat ids in this history are the pre-conversion ones; the body ids did not change. Retired beats: B00, B01, B02, B03.

> # CHECKS-REPORT — Bayes' Theorem: The Positive That's Usually Wrong
>
> Written at plan time, before any slate or audio (PROOF GATE). Generated from `beat_sheet.json`, which is built by `make_sheet.py`.
>
> ## SHOW / HOLD / CARD
>
> The 17 beats break down as 14 SHOW, 0 HOLD, 3 CARD and 0 PUNT:
> - **SHOW (14):** B00, B01, B02, B10–B19 and BHTF.
> - **CARD (3):** B03 (TERMS), BVDT (recap, exempt) and BOUT (locked outro).
> - **HOLD and PUNT:** none.
>
> | Beat | Class | On-screen artifact named in `shot.show` |
> |---|---|---|
> | B00 | SHOW | TL;DR page: the question writes on, three lines land on cues |
> | B01 | SHOW | TL;DR page two: the stake writes on, three dashes land |
> | B02 | SHOW | hesitant writer: "the test" → "a positive" |
> | B03 | CARD | three term rows land one at a time (prerequisites only) |
> | B10 | SHOW | "you" square, POSITIVE stamp, P(sick) = ? |
> | B11 | SHOW | 10,000-square grid counts up; scan over the 100 sick |
> | B12 | SHOW | scan over the 9,900 healthy; 495 stay lit |
> | B13 | SHOW | box around the sick, 99/100, the 495 outside pulse |
> | B14 | SHOW | the 594 positives regroup; predict hold |
> | B15 | SHOW | squares morph into 99/594, then 1/6 |
> | B16 | SHOW | counts → probabilities → Bayes' theorem (MathTex, staged) |
> | B17 | SHOW | five-zone tangent, box spotlight |
> | B18 | SHOW | the B10 "you" square returns into the block; 1/100 → 1/6 |
> | B19 | SHOW | base-rate curve with a sweeping marker |
> | BVDT | CARD | verdict artifact (recap, exempt) |
> | BHTF | SHOW | composer prompt plus three check lines |
> | BOUT | CARD | locked title outro |
>
> The PPT test passes: no two slide-like beats are adjacent. B03 is the only content CARD, and it sits between two SHOW beats.
>
> ## tldr role audit (pedagogy §4, Gate 2)
>
> | Order | Beat | Role | Check |
> |---|---|---|---|
> | 1 | B10 | HOOK | the key case, unsolved, opens the section ✓ |
> | 2 | B11 | INSTANCE | 1st moving instance (sensitivity as a count) ✓ |
> | 3 | B12 | INSTANCE | 2nd moving instance (false-positive rate as a count) ✓ |
> | 4 | B13 | NAIVE | the 99% walked to where it breaks: right fraction, wrong crowd ✓ |
> | 5 | B14 | SHIFT | representation: positives only. **predict: true** ✓ |
> | 6 | B15 | TRANSFORM | exactly one in the section ✓ |
> | 7 | B16 | ABSTRACTION | arrives after two INSTANCEs; lands an equation ✓ |
> | 8 | B17 | TANGENT | follows the equation's ABSTRACTION; five zones, about 29 s est (≤ 45 s) ✓ |
> | 9 | B18 | PAYOFF | returns B10's "you" square, the same persistent object ✓ |
> | 10 | B19 | BOUNDARY | base-rate dependence, plus the untaught case → BHTF ✓ |
>
> Audit counts:
> - **TRANSFORM:** 1 (rule: exactly 1) ✓
> - **INSTANCE before ABSTRACTION:** 2 (rule: ≥ 2) ✓
> - **predict beats before the TRANSFORM:** 1, at B14 ✓
> - **TANGENT after the equation:** ✓
> - **`learn` blocks:** present on all 10 LEARN beats. `next_question` chains through each beat and is empty only on B19, the section's last beat ✓
>
> ## Gate-1 audit table (pedagogy §13)
>
> | Check | Ref | Pass? |
> |---|---|---|
> | Key case named | §1.1 | ✓ 10,000 people, 1% sick, 99% / 95% test, one "you" positive |
> | Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10 uses no term; TERMS (B03) holds prerequisites only |
> | ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11, B12 |
> | Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ "Bayes' theorem" is named in B16 ("this thing deserves a name") |
> | Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13 |
> | One representation named in one sentence | §10 | ✓ "Keep only the people who match what you know: the positives, counted as people." |
> | Exactly one TRANSFORM per section | §4 | ✓ B15 |
> | Every landed equation followed by a TANGENT | §4 | ✓ B16 → B17. The B15 count fraction is arithmetic on screen and is explained by B16–B17 |
> | PAYOFF returns the HOOK's persistent object | §4 | ✓ "you" square + stamp |
> | Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: second positive (→ BHTF); odds form / likelihood ratio (cut); test independence (rubric line); continuous / Bayesian inference in general (cut) |
> | Mystery-framed opener; utility framing absent | §2 | ✓ "So how worried should you be? Hold on to your first answer." |
> | Discovery voice; no "it can be shown that" | §3 | ✓ "The natural answer…", "So change the crowd", "Before we count, commit" |
> | Every beat has a `learn` block; next_question chains | §9 | ✓ |
> | One `predict: true` beat before the TRANSFORM | §12 | ✓ B14 |
> | Boundary: not taught + transfer exercise → BHTF | §7 | ✓ B19 → BHTF "Test Positive Twice" |
> | Length derived + tier reported | §5 | ✓ single-insight; 860 words ≈ 4.1 min at 3.5 w/s, ≈ 5.5 min at 2.6 w/s |
>
> ## Learning checks (pedagogy §12)
>
> - **Prediction:** B14 asks the viewer to commit to a share before B15 counts.
> - **Explanation:** B18 gives the why (99 : 1 outnumbering). BVDT line 3 restates it.
> - **Transfer:** BHTF changes the case to a second positive.
>
> ## Teaching arc (ai-explainer parent)
>
> | Item | Status | Where |
> |---|---|---|
> | FRAMEWORK | ✓ | B11–B12 grid, B14 positives-only block |
> | WORKED EXAMPLE | ✓ | B15 (99/594 = 1/6), B17 zone 4 (0.99 × 0.01 / 0.0594) |
> | FALSIFIABILITY | ✓ | B13 (the 99% shown false as an answer); B19 (base-rate limits) |
> | SCAFFOLDED TASK | ✓ | BHTF, a prompt plus a three-point rubric |
> | BOOKENDS | ✓ | B00 TL;DR, BVDT, BHTF, BOUT; `bookend_check` PASS |
> | NO-SOURCE-NO-VERDICT | ✓ | every number traces to `evidence.json`; the B01 claim traces to Casscells 1978 |
>
> ## Gates run at plan time (2026-11-22)
>
> | Check | Command (from toolkit root) | Result |
> |---|---|---|
> | GATE BOOKEND | `python3 runtime/scripts/bookend_check.py <reel>` | **PASS**: four bookends correct |
> | Beat lint | `python3 runtime/qc/beat_lint.py <reel>` | **clean** |
> | Math layout | `python3 runtime/scripts/math_layout_check.py <reel>` | exit 0 |
> | Pace | `skills/make/duration-planner/scripts/pace_check.py <reel>` | advisories only (below) |
> | Remotion props | `scene_search.py --check <Pattern> --no-log` for all 7 patterns, plus schemas read | all RENDERABLE; props match the zod schemas |
> | Pronunciation | `generate_audio_kokoro.py --phonemize` on every line | "Bayes" /bˈeɪz/ ✓; "Salaam" pinned to /səlˈɑːm/; "You're" → "You are" (B18) |
>
> **Pace advisories.** These are estimates at 2.6 w/s and were accepted with reasons:
> - **B00 (27 s) and B01 (25 s):** "over ceiling 18 s". The SKILL mandates 45–70 and 45–65 words for these beats; they are at 70 and 65.
> - **B17 (29 s):** over the 24 s equation ceiling. A TANGENT may run ≤ 45 s (EQUATIONS.md).
> - **BVDT (25 s):** recap of four lines.
> - **BHTF (47 s):** the prompt is read verbatim (HANDOFF law).
> - **BOUT (4.2 s):** below the floor. The 1.0 s locked tail brings it to about 5.2 s.
>
> **Legibility contract**
> - The grid at 4K: each mark is about 15 px, with about 4 px gaps.
> - The positives block in B14 uses larger marks (27 × 22).
> - Comparisons in B12 (99 vs 495 counters) and B19 (four base rates) are held side by side for ≥ 2 s.
> - Negative space is 15–35%, to be verified at visual QC.
>
