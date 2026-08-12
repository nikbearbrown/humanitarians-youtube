# Feedback: "Can AI Catch Its Own Mistakes? I Ran the Experiment" — Tanmay Kulkarni, film 4

**Verdict: clear-for-public. Teaching 12/12. Production gate PASS.**

One line: *This film attempts to test a claim about AI self-verification and
delivers something better — a reusable instrument for testing causal claims,
demonstrated three times including once on the film's own failed attempt.*

Run 2026-08-12 against the **shipped master** (`can-ai-catch-its-own-mistakes.mp4`,
322.3s, 3840×2160), after the B2/B3 review revision. Frames were sampled at the
**moment of assertion** for each of the thirteen beats and inspected — not
inferred from the components, and not from a settled tail frame (PROOF Rule 5).

---

## Where it improved vs film 3 (Lemonade / "Claude, Untangled?")

| Criterion | Film 3 | Film 4 |
|---|---|---|
| Sources on screen at assertion | **Caught late** — B06 shipped a third-party-coverage claim with no source; found by audit *after* the cut existed, verdict moved to unlisted-until-fixed | **Caught early** — two of the same class (B4, B7) found at the Phase 2→3 boundary, *before* audio; a third (B2) fixed inside the edit that created it |
| Falsifiability case | Present but hypothetical | The film's **own revision 1**, shown on screen with its `n=0` table |
| Own standard applied to itself | Partial | The instrument is run on the film's own work, and the film's own hypothesis is the thing that gets falsified |
| Framework position | First third | 0:52, **7s later than the first cut** — the one thing that moved the wrong way |

**Film 3's punch list was self-applied.** The recurring defect — a claim voiced
without a visible source — was caught two phases earlier this time, at the stage
where the fix costs a prop string rather than a rebuild.

---

## Rubric

| Criterion | This cut | Score |
|---|---|---|
| **Explicit framework** | B3 (0:52–1:17) resolves the four questions as a structure and holds complete. Zero overlap with the first example — B3 ends at 1:17.31, B4 starts at 1:17.31. Narrated *as* it is drawn, not after. | **2** |
| **Reusable rubric** | The questions are stated domain-generally — *"any time somebody says a system fails because of something"* — not scoped to models or to this task. B12 returns them as a copyable card, same component as B3, so the taught set and the handed-over set cannot diverge. | **2** |
| **Worked example** | Two, both walked live through the reasoning step rather than stated as conclusions. B4 runs the source draft: claimed cause → rival explanation → is there an arm where only the cause changes → *no, both arms change everything*. B6 runs the film's own revision 1. | **2** |
| **Falsifiability / edge case** | The strongest element in the film. Revision 1 **passes Q1–Q3 and fails Q4** — a case that clears three axes and is caught by the fourth, which is precisely the test that a framework is real rather than decorative (Rule 1). Beyond that, the film's own hypothesis is the thing falsified: it set out to confirm the blind spot and found none. | **2** |
| **Active task** | B12 is a four-step structured task — write the cause in one sentence, write one rival that looks identical from outside, describe the isolating test, ask whether it collects data — plus a built-in self-check: *"if everything you own passes on the first read, you graded yourself gently."* No vague pointer anywhere (Rule 2). | **2** |
| **Friction** | B10 is real tension the viewer has to resolve: the same advice is correct **and** its stated reason is wrong, and both are on screen at once — one intact, one struck. B9 forces holding "observed zero" against "not zero, below ~9%." B6 makes the viewer sit inside the author's own dead end before the recovery arrives. | **2** |

**Total: 12/12.**

### Rule 1 check — is the framework reverse-engineered?

The tell is one-per-example mapping. It does not appear here:

| Artifact | Q1 cause | Q2 rival | Q3 isolating arm | Q4 collects data |
|---|:--:|:--:|:--:|:--:|
| Source draft | pass | **fail** | **fail** | — |
| Our revision 1 | pass | pass | pass | **fail** |
| Our revision 2 | pass | pass | pass | pass |

The draft fails **two** axes at once and revision 1 fails **one**. An invented
framework produces a clean diagonal; this does not have one.

---

## Production gate — PASS

| Gate condition | Result |
|---|---|
| **Evidence legible at the moment of assertion** | PASS — 13/13 frames sampled at claim time, all legible at 4K. No element below readable opacity, no center overlap, no clipped labels. |
| **Sources on screen, not just voiced** | PASS — B1 draft path; **B2 results JSON** (new); B4 verbatim quote + `beat_sheet.json` B03 path; B7 `arXiv:2507.02778 (2025), preprint`; B9 `exact binomial, n = 33, 0 events`; B10 both verbatim sentences with B07/B01 paths. |
| **Side-by-side at the moment of comparison, held ≥2s** | PASS with large margin — B4 two arms (34.1s), B5 the two prompts with the identical expression in both (22.5s), B10 kept vs struck (34.2s). |

**Peer-review status is visible, not just the citation.** B7 carries the word
`preprint` on the frame. This is the only place in the film that distinction
appears, and it is on the one paper that is not peer-reviewed.

**The B2 timing was checked, not assumed.** The rewrite introduced a forward
reference to *thirty-three*. The source line fades in at 34% of the composition
(~2.7s); the number is spoken at ~68% of the beat (~22.5s). Verified on the
frame at 40.3s — source present, claim not yet made.

---

## Does the film pass its own standard?

Its own rule is *no arm, no finding* — and it is a film about a video script that
asserted without measuring. Held to that:

- **It has the arm.** Arms A and B differ only in apparent ownership; the
  expression is character-for-character identical. That is shown, not described.
- **It reports the result it did not want.** The hypothesis was the blind spot;
  the finding is a null, and B11 argues for publishing it rather than quietly
  binning it.
- **It runs the instrument on itself.** Revision 1 is in the film as a failure,
  with its `n=0` table on screen.
- **It states its own ceiling.** B9 refuses the clean number the film had earned
  the right to say. "Zero" is on screen at B8; "below about nine percent" is on
  screen at B9, with the count and the bound welded into a single component so
  they cannot drift apart in a future edit.
- **It never names a person**, and B4 ends on the concession that the design
  mistake is subtle and common.

---

## Pacing — runtime budget

| Segment | Time | % |
|---|---:|---:|
| Framework shown (B3) + handed over (B12) | 58.6s | 18.2% |
| Framework **applied** to cases (B4, B6) | 55.9s | 17.3% |
| Method construction (B5, B7) | 45.8s | 14.2% |
| **Results recitation — facts** (B8) | **20.1s** | **6.2%** |
| Limits, synthesis, argument (B9–B11) | 81.1s | 25.2% |
| Hook, subject, close (B1, B2, B13) | 60.6s | 18.8% |

**Method and its application take 49.8% of runtime; fact recitation takes 6.2%.**
PROOF flags when fact recitation exceeds ~50%. This is the opposite shape — the
result the film went looking for occupies twenty seconds, and the method
occupies half the film. That is the correct allocation for this material,
because the method is the transferable part.

---

## The problem

**One deviation, and this revision made it slightly worse.**

PROOF's Phase 2 gate asks for the framework graphic in the **first ~20s**. B3
starts at **0:52** — 16.1% into the runtime — and completes at 1:17. In the
first cut it started at 0:45. The B2 rewrite pushed it **7 seconds later**.

Logged as a deviation, not argued as a pass. The reasoning for accepting it:

- The **binding** constraint — framework *before* any example — holds exactly,
  with zero overlap.
- The 7 seconds bought the fix for a defect that was worse. A viewer of the
  first cut reached 1:00 without ever hearing what the film was about. A
  framework of abstract meta-questions arriving at 0:45 to a viewer who does not
  yet know the subject is early in wall-clock terms and late in comprehension
  terms.
- PROOF's "~20s" is written for a 3–4 minute explainer. As a **fraction**, 16%
  into a 5:22 film is roughly where 20s falls in a 2-minute one.

That reasoning is offered, not asserted as a pass. If the framework needs to
land earlier, the cheap move is trimming B1 (17.8s, the hook) rather than
touching B2 — but B1 is the claim under test, and cutting it costs the film its
provocation.

---

## Do X next week

1. **[EDIT] Q1 never discriminates.** Across all three artifacts, *"what is the
   claimed cause?"* is passed every time — it is a precondition for asking Q2,
   not a filter. That is not a defect (the framework is demonstrably not
   reverse-engineered), but a future cut could earn a fourth axis by showing one
   artifact whose claimed cause cannot even be stated. Worth one sentence in the
   next film, not a re-edit of this one.
2. **[EDIT] Make the source-line check a pipeline step, not a habit.** The
   "claim voiced without a visible source" fix has now been applied **three
   times on this film alone** (B4, B7, B2) and once on film 3. The *component*
   already exists — `source` on both `SkepticSplit` and `SkepticStatement`,
   fading at ~14% and 34%. What is missing is the check. A script that flags any
   beat whose `narration_text` contains a digit, a quotation mark or "arXiv" and
   whose props carry an empty `source` would have caught all four automatically.
   This is exactly the "solve it once as a standing template" case (`/series`).
3. **[EDIT] Add the TTS gap sweep before compile.** One
   `silencedetect=n=-40dB:d=0.55` pass over `mp3/` costs seconds and catches
   one-word-sentence pauses while the fix is still punctuation. Now in
   PLAYBOOK §1d.
4. **[EDIT] Add a "does beat 2 name the subject?" line item to the phase-2
   check.** Now in PLAYBOOK §1c. Both defects in this cut survived a clean PROOF
   audit, a full claims audit and a frame-by-frame QC sweep — neither is a claim
   error, and no rubric in use scores comprehension or delivery.

Nothing tagged `[RESHOOT/NEW SOURCE]`.

---

## What works — keep this

- **The falsifiability case is the film's own failure, with its data on screen.**
  Most explainers stress-test a framework against a hypothetical. This one runs
  it on a real dead end the author hit two days earlier and shows the `n=0`
  table. That is the single most credible thing in the cut and it should become
  the house pattern.
- **B10 separates mechanism from practice.** *"Right advice. Wrong reason."* —
  with the surviving sentence intact beside the contradicted one struck through,
  both verbatim, both sourced. It resists the easy version of this film, which
  would have been dunking on the draft.
- **B9 exists at all.** The film earned "zero" and refuses to say it. Peak at B8,
  discipline at B9 — the shape that makes a finding trustworthy.
- **The two structural safeguards.** `figure` and `bound` on one component so the
  count and its ceiling cannot drift apart; B3 and B12 sharing one component so
  the taught framework and the handed-over framework cannot diverge. Constraints
  enforced in code rather than left to discipline.
- **The plain visual language.** Type-led, one accent colour, one fade per
  element. PROOF names "clean motion around an empty center" as a failure mode;
  this cut has the opposite problem profile and is better for it.

---

## Ship verdict

**Teaching 12/12 ≥ 8. Production gate PASS. Passes its own standard.**

→ **clear-for-public.**
