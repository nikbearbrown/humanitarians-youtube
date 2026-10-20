# PROOF review (stills): "The Birthday Paradox: Three Things You Could Change" — Tanmay Kulkarni, Week 27 topic film

**Stage:** 18 review stills, 3840×2160, one per beat at the moment of assertion (`_stills/B01-16x9.png` to `B18-16x9.png`), after one round of Tanmay's fixes. Reviewed from the actual frames (looked at every slate), the narration (`READ-ALOUD.md`, Gate P signed 2026-10-16), `FACTCHECK.md`, and a mechanical pass (`check_onscreen.py`). No motion, no audio. PROOF cannot judge reveals, timing, or the 8 s hold from stills, so those are listed as not assessable.

**Verdict:** **unlisted-until-fixed.** No cut exists to publish; of the stills, **clear to go on to animation and audio once the three MAJOR flags below are fixed.** Teaching **12/12** (conditional on motion keeping the structures below visible). Production gate: **PASS on core evidence, with 3 MAJOR and 3 MINOR flags** on secondary text.

One line: this film's slates show their evidence (every spoken figure is on screen, sourced, and sits beside its comparison), but its small type, small accent-coloured labels and low source lines are the weak point.

## Rubric (from the stills)

| Criterion | This cut |
|---|---|
| Explicit framework | **2.** B02 shows the three cards (PEOPLE, EVENNESS, DAYS) before any change; the same strip stays on every chapter beat (B03–B11) with the active card in the accent, and returns with readings in B12 |
| Reusable rubric | **2.** B13 prints the rule as a structured equation (real radical, fraction bar, sized parentheses), with variables defined and a seven-row fit table |
| Worked example | **2.** B15 and B17 show the working line by line, then the exact percentages for either side of the threshold (43% / 62%, 53% / 45%) |
| Falsifiability / edge | **2.** B05 (some pair vs you), B13 tally ("exact for 1,161 of 1,999 slot counts; off by one for the other 838; never more"), B14 (school-year cohort). The rule's own failures are on screen |
| Active task | **2.** B16 gives the setting (50 slots), the rule, the variables and the tempting wrong answer; B17 shows the answer, the working and the wrong answer struck through |
| Friction | **2.** B02 sets the three-way puzzle and B12 resolves it with the three readings side by side |

**Total: 12/12.** What could drop it once animated: B16's 8 s hold not measured in the compiled cut (Task to 1); B13's table too small on a phone (Rubric to 1).

## Production gate

| Check | Result |
|---|---|
| **Sources on screen** | **PASS.** Every figure-bearing beat carries a source line. B06 adds the NCHS/SSA credit as a held line; B18 repeats it in the end card. Illustrations are labelled (B01, B09: "Not data") |
| **Every spoken figure printed in the same beat** | **PASS.** `check_onscreen.py` checks a list of 100+ spoken figures against the text actually drawn on each slate; all 18 beats pass. Caveat: it checks the figures we listed, not unlisted text |
| **Side-by-side at the moment of comparison** | **PASS.** B05 (23-person pair vs you), B07 (50.7% vs 50.8%), B09 (95.4% vs 50.8%), B12 (95.44 vs 95.40), B15 (43% vs 62%), B17 (53% vs 45% with 25 struck) |
| **Evidence legible at the moment of assertion** | **PASS for core artifacts** (every headline number is 90–200 px at 1080p; the rule, tables and charts are large). **FLAGS** on secondary text below |

## Beat by beat

| Beat | What the slate shows | Verdict |
|---|---|---|
| B01 | 23 dots on a month × day grid, one shared cell ringed, 50.7% | OK. Illustration labelled "Not data" |
| B02 | Three cards, "Hold a guess" line | OK. Lower third empty by design |
| B03 | 23 points, all 253 chords, the fraction (23 × 22) / 2 = 253 | OK |
| B04 | Odds-vs-people curve, 5 labelled points, 50.7% and exact 50.73% | OK after fix: 50 left, 57 right, above their dots |
| B05 | "Any pair" 50.7% beside "someone shares YOUR birthday" 5.9%, 253 other people | OK |
| B06 | Calendar heat map, Feb 29 ringed, +12% and 25%, held credit line | OK. Colour scale has words, not numbers (MINOR 6) |
| B07 | 50.7% beside 50.8%, "a difference of 0.1 points" | OK |
| B08 | 365 day-bars, ±10% band, "96% of days sit within 10% of average" | OK. Axis ticks small (MAJOR 1) |
| B09 | 90-cell band, dots inside it, 95.4% beside "full year 50.8%" | OK. Illustration labelled |
| B10 | Five-row window table with shrinking-band bars, "7 days" line | OK |
| B11 | Six-row head-count table with bars | OK |
| B12 | Three cards with readings, verdict line under each, 95.44 vs 95.40 | OK after fix |
| B13 | Rule, variable key, seven-row fit table with check marks, the honest tally | OK. Densest slate (MAJOR 2, watch item) |
| B14 | Full-year grid shaded from Sep 1, 50.8%, "cutoff: Sep 1" | OK |
| B15 | Month cards, √12 and the working, 43% vs 62% | OK |
| B16 | "50 slots", question, rule, variable key, wrong answer, 8 s bar | OK. Hold not assessable from a still |
| B17 | The working, 9 people 53% vs 8 people 45%, 25 struck | OK |
| B18 | The rule alone, wording matches the outro, name and credit | OK |

## Flags

**MAJOR (fix before the render): FIXED 2026-10-16, see `STILLS-QC.md`; `check_onscreen.py` now enforces them**

1. **Type too small for a phone.** Smallest text per beat, in px on a 1080p frame: month labels 17 (B01, B06, B09, B14), axis ticks 19 (B04, B08), table headers and chapter sub-labels 20–21 (B10, B11, B12, B13), source lines 22. At phone width these fall to roughly 3 dp. Target: nothing below 24 on a data label, 26 on a source line. [EDIT]
2. **Source lines sit 52 px from the bottom edge.** The player's control bar covers roughly the bottom 5–6% of a 16:9 frame when it shows, and the source line is the one thing the production gate depends on. Raise the source baseline so its bottom is at least ~90 px from the frame bottom (B16's countdown bar and "8 s" are also low, 98 px). [EDIT]
3. **Small accent text fails contrast.** SPARK on cream is 2.96:1 and on white 3.12:1, below the 4.5:1 small-text bar (and just under 3:1 for large). It is used for 22 px labels ("PEOPLE", "5 PEOPLE", "9 PEOPLE", "SOMEONE SHARES YOUR BIRTHDAY", the "cutoff: Sep 1" label) and for large numerals and italic verdicts. Keep SPARK for large numerals and rules, but use a deeper shade for small text: **`#B5532F` is 4.7:1 on cream and 4.95:1 on white**. [EDIT]

**MINOR**

4. Inactive chapter cards use GHOST (2.37:1). They repeat what B02 already showed, so acceptable, but a darker ghost would read better in the 3-beat stretch where they are the only context. [EDIT]
5. B02's lower third is empty (bottom margin 340 px). Fine as breathing room; B02 is the only slate where the plan is held, so consider using the space to print the guess prompt larger. [EDIT, optional]
6. B06's colour scale says "quieter days / busier days" but gives no numbers. The +12% and 25% callouts carry the figures, so this passes, but one tick label at each end ("25%", "112%") would close it. [EDIT, optional]

## Not assessable from stills

- **Animation:** dots dropping, counter climbing, band shrinking, the strip's active card moving. Re-run the gate on frames at 15% / 50% / 85% of each beat in the compiled cut.
- **Audio sync:** every held figure and comparison must be on screen for ≥2 s at the moment it is spoken (B13 ≥3 s).
- **B16's 8 s hold** measured in the compiled master.
- **Equation states** at 15 / 50 / 85% of B13, B15, B16, B17 (toolkit math rule).
- **Phone-width legibility** after the type-size fix, checked on rendered frames at 360 dp.

## Do X next

1. **[EDIT]** Raise every secondary text size (flag 1) and the source line position (flag 2) in `build_slates.py`; use `#B5532F` for small accent text (flag 3). Re-run `check_onscreen.py`, then re-send the changed stills.
2. **[EDIT]** Optional polish (flags 4–6).
3. **[EDIT]** Build the motion for the 18 beats from these slates, then Kokoro audio, then compile once (front-load checks).
4. **[EDIT]** Re-run this review on frames from the compiled cut, including the 8 s hold and the 15 / 50 / 85% equation frames.
5. **[RESHOOT/NEW SOURCE]** None. All figures are our own or federal; no third-party media.

## What works

- **Evidence is on screen.** Each spoken figure is printed where it is spoken, with its source, and checked by script.
- **Comparisons are literal.** Every "this versus that" in the narration is two numbers side by side.
- **The honest tally.** B13 prints where the rule fails, not just where it works.
- **A clean visual language.** One calendar grid, one strip, one accent; no third-party images, no political content, no real individuals.
