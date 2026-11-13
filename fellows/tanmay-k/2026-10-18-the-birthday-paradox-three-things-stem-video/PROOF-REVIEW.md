# Feedback: "The Birthday Paradox: Three Things You Could Change" — Tanmay Kulkarni, Week 27 topic film

**Stage:** beat draft 2, 18 beats, 943 words, about 4.9 min including one 8 s hold. Draft 1 (Gate P signed 2026-10-16) was restructured after PROOF's first pass. No audio, no renders, no frames. Reviewed from `BEATS-DRAFT.md`, `READ-ALOUD.md`, `FACTCHECK.md`, `RESULTS.md`, `sqrt-rule.json` and the form sweeps. PROOF cannot judge frames that do not exist, so the production gate is checked at **prop level** and must be re-run on rendered stills before any audio. The first-pass review (10/12, unlisted-until-fixed) was replaced by this one; its findings and fixes are in the tables below.

**Verdict:** **cleared for the Gate P re-read of 12 changed beats.** Not yet shippable: unlisted-until-fixed applies to any cut until rendered frames pass. Teaching **12/12** at beat-sheet level (to be re-scored on stills). Production gate **PASS at prop level**.

One line: this film tries to teach which of three assumptions decides a coincidence-odds claim, and it delivers that by turning each one in turn, then handing the viewer a rule they can use on a case the film never ran.

## Where it improved vs the first pass of this film

| Criterion | Draft 1 | Draft 2 | What changed |
|---|---|---|---|
| Reusable rubric | 1 | **2** | The single rule "change one assumption" became a testable formula, shown fitting seven windows, applied to a new case (B15), and checked on 1,999 slot counts (B13) |
| Active task | 1 | **2** | A vague question became a scaffold: the rule on screen, a practice case (1 to 50), the tempting wrong answer named, an 8 s hold, then the worked answer (B16–B17) |
| Production gate | FAIL (no sources on screen) | **PASS at prop level** | Every beat that states a figure now carries a source line and a held display (legibility contract in the beat sheet) |
| Form | overlapped `vox-prediction-lock` | **clear** | The written-prediction device is gone |

## Rubric

| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Shown as a structure before the examples | **2.** B02 (0:16–0:42) puts three cards on screen and keeps them as the chapter index: PEOPLE, EVENNESS, DAYS. They are the problem's own three parameters, and they appear before the first change is made |
| Reusable rubric | A viewer could apply the same axes to a new case | **2.** Axes: how many people, how even the slots, how many slots. Rule: people for even odds ≈ round(1.2 × √slots + ½). B15 applies it to birth months (a case not run before); B16 hands the viewer another |
| Worked example | One case walked through live | **2.** B15 and B17 show the working step by step (square root, times 1.2, add a half, round) and check the answer against exact percentages |
| Falsifiability / edge | Stress-tested against a counterexample | **2.** B05 (match-me vs match-anyone), B12 (does evenness still matter inside windows: a tenth of a point at most), B14 (school-year objection). B13 puts the rule's own failures on screen: exact for 1,161 of 1,999 slot counts, off by one for 838, never more |
| Active task | The viewer does something structured | **2.** B16: slots (50), the rule printed, the wrong answer named (25), an 8 s silent hold; B17 gives nine people at 53% against eight at 45%. Scaffolded, not "ask Claude" |
| Friction | The viewer must resolve a tension | **2.** B02 sets a three-way puzzle (one barely matters, one as expected, one decides almost everything), held open until B12. B16's hold is a second, smaller one |

**Total: 12/12.** What would drop it on stills: the B13 table or the B16 rule line unreadable at the held moment (Framework, Rubric, Task each fall to 1), or the 8 s hold not measured in the compiled cut (Task to 1).

## Production gate (prop level)

| Check | Result |
|---|---|
| **Sources on screen, not just voiced** | **PASS.** Every figure-bearing beat (B01, B03–B13, B15, B17) has a `Source:` line naming our simulation or calculation, or the NCHS/SSA credit (B06) |
| **Evidence legible at the moment of assertion** | **PASS (intent).** Each spoken figure is printed in the same beat. B13's table is held ≥3 s, other tables ≥2 s |
| **Side-by-side at the moment of comparison** | **PASS.** B05 (any pair vs you), B07 (even vs real calendar), B09 (full year vs 90 days), B12 (real vs even for the 90-day window), B15 (4 vs 5 people), B17 (9 vs 8, and the wrong answer struck) |

**Watch items (eyes-only, at render):**
- B13's table, tally line and rule line carry a lot. Check they fit in 9:16 and 16:9 without shrinking below readable size.
- B16's 8 s hold must be measured in the compiled master, not trusted from the sheet.
- The rule says "round halves up". Check the ties (25 and 100 slots) are not in any on-screen example.
- B04's 10 / 30 / 50 / 57 labels: confirm all four are printed with percentages.

## Findings from this pass (fixed in draft 2)

| # | Finding in draft 1 | Fix |
|---|---|---|
| 1 | **Form overlap:** the "locked prediction before each result" device is the stated thesis of `claude-for-artificial-intelligence/vox-prediction-lock` and its variants. Our B02 line and B08 restaged its lesson | Device removed. No predictions, no "my call", no gap-as-evidence framing |
| 2 | **B13 error:** "The first test changed the shape of the calendar" (it was the second) | Beat rewritten; the draft 2 B12 names the three changes by name instead of by number |
| 3 | **Unsupported claim in B09 (old):** "nearly every ordinary day sits within a few percent of average." The lowest day is 0.567 of average | Replaced with a measured figure: 96.4% of days within 10% (new B08, FACTCHECK row) |
| 4 | **B06 invited a wrong inference** ("February twenty ninth runs at about a quarter of a normal day") | Added "because it only exists one year in four" |
| 5 | **"The same twenty three people"** implied the same individuals | Now "same group size" (B09) |
| 6 | **"Your gut, trained on small rooms"** was an unsourced psychology claim | Removed |
| 7 | **No on-screen sources** in any beat | Legibility contract written into every beat (`Visual:` and `Source:`) |

**Form sweep, for the record.** All 65 refs, 20,811 narration, script and beat files: the square-root-of-slots rule has **0** hits. The only device overlap was `vox-prediction-lock`, now cleared. Phrases such as "change one thing at a time" appear in unrelated advice lines (Suno, image-generator and recipe videos) and this film never uses that slogan. Our own Weeks 17–26: no use of the device. Not read in context: `ecis-explained` (ref lookup failed) and the tower-defense game; their hits were phrase-only and read as unrelated, not confirmed.

**Boundary notes.** Not W20's instrument being read (no gauges or scales), not W21's same-move-one-size-up (each change turns a different parameter), not W22's witnesses and verdict, not W25's coin experiment, and no staged rooms (W23, W24, W26).

## Do X next

1. **[EDIT] Gate P re-read of the 12 beats marked RE-READ NEEDED in `READ-ALOUD.md`** (B02, B04, B06, B07, B08, B09, B12, B13, B15, B16, B17, B18). Six beats are unchanged and signed (B01, B03, B05, B10, B11, B14).
2. **[EDIT] Check Kokoro phonemes** for "Kulkarni", "fortnight" and "February twenty ninth", and that "one point two, plus a half" is clear in the ear.
3. **[EDIT] Build the grid, dots, counter and card slates** from the `Visual:` lines; render stills; re-run the production gate on the stills before any audio.
4. **[EDIT] Measure B16's hold** in the compiled master once audio exists.
5. **[RESHOOT/NEW SOURCE]** None. Every figure is our own or federal.

## What works

- **The chapters are the problem.** Three parameters, three changes, no borrowed structure.
- **An honest null.** The evenness change finds almost nothing, and the film says so instead of manufacturing a gap.
- **A rule that survives its own check.** The film shows where its rule is exact and where it is off by one, rather than claiming it always works.
- **A task the viewer can finish.** The rule is on screen, the wrong answer is named, there is a held pause, and the answer comes with its working.
- **Clean sourcing.** US federal counts plus our own simulations, no third-party media, no political content.
