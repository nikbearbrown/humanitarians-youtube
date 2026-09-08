# Feedback: "Can AI Discover New Quantum Materials?" — Dhrumil Shah, film 2

**Verdict:** **unlisted-until-fixed.** Teaching score **12/12**. Production gate
**PASS**.

One line: this film attempts an evidence-first review of machine learning in
superconductor search and delivers it — a real reusable rubric, shown before any
example, stress-tested against a case it did not choose — but it is held off
public until one prominently displayed number is verified against its source.

The teaching is not the problem. The film's own standard is.

## Where it improved vs film 1 (Mycroft ThesisGuard)

| Criterion | Film 1 | Film 2 |
|---|---|---|
| Explicit framework | 2 — CLEAR, presenter-labelled, at 00:14 | 2 — CLAIM, presenter-labelled, at 00:26, ahead of every example |
| Reusable rubric | 2 — six-row reviewer scaffold | 2 — five-axis scaffold with an explicit decision rule |
| Worked example | 2 — the project's own holdout result | 2 — the rubric run live against an external case |
| Falsifiability | 2 — the system's own missing evidence | 2 — **stronger**: an adversarial external case (LK-99) the film did not select in its own favour |
| Active task | 2 — reviewer scaffold | 2 — scaffold plus a stop rule ("record candidate, not discovery") |
| Friction | 2 — weak performance treated as a governance signal | 2 — AI is simultaneously useful and structurally bounded; the viewer must hold both |

Film 1's known limitation was a missing asset. Film 2's is an unverified figure —
and unlike a missing plot, an unverified number that is *displayed as fact* is a
gate issue, not a footnote. Film 2 is the more rigorous film and gets the harsher
verdict, which is the system working.

## Rubric

| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | A structure is shown before examples | **2** — CLAIM lands at 00:26. The first example (the training table) does not appear until 00:35. The order is enforced by the composition, not by luck. |
| Reusable rubric | A viewer can score a new case on the axes | **2** — 02:46–02:59 gives five axes as questions plus a decision rule. Nothing about it is specific to superconductors except the vocabulary. |
| Worked example | A case is walked through, not asserted | **2** — 02:33–02:46 scores LK-99 row by row with per-row justification on screen. |
| Falsifiability / edge case | The framework is stress-tested | **2** — LK-99 produces four *different* verdicts across five axes (PRESENT / N/A / UNKNOWN / FAILED / FAILED). That non-uniformity is the evidence the axes are independent rather than reverse-engineered one-per-example. |
| Active task | The viewer does something structured | **2** — the scaffold ends in an executable rule, not "ask an AI". |
| Friction | The viewer resolves a real tension | **2** — the film gives the model a genuine, reproducible win at 01:00 and then reframes what that win measures at 01:10. It does not resolve the tension for the viewer. |
| **Total** | | **12/12** |

## Production gate

| Gate | Final-master evidence | Status |
|---|---|---|
| Evidence legible at the moment of assertion | Eleven 4K stills inspected in `_qc/final/`. No clipped headline, no overlapping text, no card overflow, no source tag obscured. Two defects were found in preflight and fixed *before* the master: the Tc chart's high-pressure labels collided with the 293 K line, and the funnel's two narrowest bars overflowed their text. Both re-inspected after fix. | **PASS** |
| Sources on screen, not just voiced | Every scene carries a persistent `SOURCE` plate at 36 px. Scene 03 displays the full bibliographic citation — author, year, title, journal, volume, pages — not merely a name. | **PASS** |
| Side-by-side at the moment of comparison | 02:10–02:33. The claimed column enters at 02:10, the replication column at 02:22, and **both are held together for 11.2 s** — far beyond the 2 s minimum. Confirmed in `_qc/final/08-lk99-sidebyside.png`. | **PASS** |

## Final technical QA

- Master: `output/can-ai-discover-new-quantum-materials-4k.mp4`
- Verified: 3840 × 2160, 24 fps, H.264 / AAC, **180.011 s**, ~24 MiB
- Verification: `scripts/check-video.ps1` — PASS on resolution, audio presence, and the 03:00 contract
- Visual review: eleven scripted QA stills in `_qc/final/`, all inspected

## The problem

**One number blocks public release.**

Scene 04 (01:00–01:15) displays **±9.5 K** at 190 px — the largest element in the
film — as the reported out-of-sample RMSE from Hamidieh 2018. That figure is
believed correct but was **not verified against the primary paper at build time**.

A film whose entire argument is *no source, no verdict*, and which spends its
climax convicting LK-99 on exactly that principle, cannot ship with its most
prominent number unverified. The film would fail its own rubric on axis **L**.

This is not a defect in the teaching. It is the teaching applied to the film.

## Do X next week

1. **[EDIT — BLOCKING]** Verify the ±9.5 K RMSE against Hamidieh 2018,
   *Computational Materials Science* 154:346–354, §4. If correct, change nothing
   and move the verdict to clear-for-public. If it differs, edit `MethodScene`
   in `src/CanAIDiscoverQuantumMaterials.tsx`, regenerate beat B05
   (`--only B05`), update `AUDIO_BEATS`, re-render.
2. **[RESHOOT/NEW SOURCE]** Scene 05 is the weakest scene: it teaches the
   screening funnel with a labelled illustrative schematic and no instance. The
   two 2026 results from the brief would fix this exactly — but neither came
   with a citation and neither could be verified, so neither is in the film.
   Supply the papers and the edit is contained (see `FACTCHECK.md`).
3. **[EDIT]** Align `@remotion/paths` (4.0.490) with the rest of the workspace
   (4.0.486) to clear the non-blocking version banner. Shared with film 1 —
   this is the second film to carry it, so it should become a workspace fix
   rather than a per-film note.
4. **[EDIT]** Consider a standing `SourceTag` + citation-card component shared
   across the series. Both films now hand-roll the same plate; a template makes
   the source-on-screen gate structurally impossible to fail.

## What works

The film's strongest choice is that it refuses the headline it was named after.
It could have used "Can AI discover new quantum materials?" as a hook and
answered yes with a montage. Instead it answers in the first twelve seconds —
*AI reorders the search queue; the laboratory still decides* — and then spends
three minutes earning that sentence.

The second strongest choice is the LK-99 case. A rubric tested only on examples
its author picked is decoration. LK-99 was a real, high-profile, genuinely
ambiguous event with a public resolution, and the rubric catches it on precisely
the two axes the film claims no model can supply. The argument and the evidence
are the same object, which is rare.

Keep both. Keep the illustrative-schematic label too — a film that discloses its
own weakest scene on screen is doing the thing it is teaching.
