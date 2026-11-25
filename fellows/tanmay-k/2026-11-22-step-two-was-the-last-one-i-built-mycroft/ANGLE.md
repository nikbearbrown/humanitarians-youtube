# Week 32 work video: what we did, and the angle (proposal, 2026-11-23)

## 1. The work, as it happened
**Recipe:** `portfolio-price-fetcher` (ours since Week 26). **Merged:** nikbearbrown/mycroft#94 as `fef5caa`, 2026-11-23 (one commit `4c9d10f`, 19 files, all added, 0 edited, 0 removed; `verify` passed). It adds step 2, "ingest declared inputs", the last step of the recipe's main table that had no script (steps 1, 3 and 5 came in Week 26, 4 and 6 in Week 31).
**What step 2 does:** reads the run envelope, the declared workflow and the fixtures against the SHA-256 frozen in two manifests; keeps each response body unchanged; rejects a file that is unlisted, changed, missing or not JSON; accounts for every source node (Fetch Stock Prices is approval-required and never called); does not judge a response (steps 3 and 4 do).
**Checked:** 28 self-test checks, all as expected, including break tests; outputs byte-identical on rerun; the same file population as step 3 reads in all six fixture sets.
**What we noticed on the way** (each one is in the repository's own files):
1. The recipe's step 3 says it reads the fixtures "directly, since step 2 is still open"; step 5 says it reads step 3's output "since step 4 is still open". Our own words, left in the recipe for a month.
2. `snickerdoodle check` told us the first draft of the script did not implement `--sample`, which the recipe's step-command table advertises. Fixed before the commit.
3. A digit pair swapped in one fixture (NVDA 504.5625 to 540.5625), run through the old chain on a scratch copy: **step 1 stops** ("fixture changed since the manifest froze it"), **step 3 on its own says "pass: 5 promoted, 0 rejected"**, and step 5 then prices the portfolio at 66,898.13 against the committed 65,098.13 (gain 13,098.13 against 11,298.13; return 24.35% against 21.00%). The new step 2 reads the same folder and rejects the file: "differs from the SHA-256 frozen in manifest.json".
4. Step 2 and step 3 see the same files in all six sets (5, 5 and 5; 4 and 5 with one not JSON; and so on). The stand-in was faithful about *which* files; it was blind to *whether they are the ones that were frozen*.
5. The other stand-in is still standing: step 5 still reads step 3's output, not step 4's.

## 2. The five axes, against the fourteen earlier work videos (Weeks 18 to 31)
Corpus: every work-video beat sheet, Short line and read-aloud (279 distinct texts). The vocabulary below was searched with the word-run check (the word-run check, Weeks 18 to 31).

| Candidate | Nearest earlier film and why | Verdict |
|---|---|---|
| **A. The Stand-In** (a stand-in for an unbuilt step is a loan; when the real step lands, run both on one bad input and read the difference) | **W26** asks the viewer what a number is "quietly taking on trust" at a hand-off; **W31** reads a recipe's status text as a claim. A's claim, move and shape differ (a build-history stand-in, a two-door comparison, a pipeline whose dashed arrows turn solid), but it shares the recipe-text-as-evidence ground with W31 and the hand-off ground with W26. | **PASS with watch items** |
| **B. The Clock Is an Input** (pin the date; rerun with another and see what moves) | **W29 B10:** "run again with the clock pinned it produces the same bytes". | **FAIL** (claim, in a sentence) |
| **C. Frozen Is Not Right** (a hash proves a file is unchanged, not that it is good; two checks, two blind spots) | **W30 B06** ("a fingerprint recorded when the set was fixed, checked before each one is kept"); **W23** (a matrix). | **FAIL as a film, fine as a beat inside A** |
| **D. Keep the Evidence** (ingest does not judge, so the later audit can say why) | **W30** (a step that deliberately knows less: presence, never value); **W26** ("quietly"); W22 (leave the hole). | **FAIL** (move) |
| **E. Count Every File** (files in = records + rejects, across steps) | **W28** (a number is a sum), **W24** (a receipt read line by line), **W25 B11** ("nothing deleted"). | **FAIL as a thesis; fine as a beat** |

Vocabulary search (weeks that already use it): `stand-in`, `stood in`, `shortcut`, `since step`, `temporary`, `real step`, `hash`, `checksum`, `SHA-256`, `time of use`, `on paper`: **none**. Taken, so avoided: `trust` / `on trust` (W24, W26), `hand-off` (W19, W26, W29, W30), `quietly` (W18, W19, W20, W25, W26), `tamper` (W24, Mastercard's own words), `fingerprint` (W30), `same bytes` (W29), `ledger` (W18 to W20), `still open` (W20, W27, W28, other senses), `draft` as a closing line about the recipe (W27, W28, W30).

## 3. Recommendation: A, "The Stand-In"
**Working title:** "Step Two Was the Last One I Built" (slug `step-two-was-the-last-one-i-built`).
**Claim:** each step built before its predecessor carries a stand-in for it, written in the recipe's own words ("since step 2 is still open"); when the real step arrives, the stand-in is a loan to be audited, not a fact.
**Hook (cold open):** "Step two was the last step I built." (a count, not a number-with-two-answers; not W25's hook form.)
**What the viewer can do afterwards that no earlier film gave them:** list every stand-in in their own build; for each, write what it skipped, then run the stand-in and the real step on one deliberately wrong input and read where they disagree.
**Shape (derived from the subject, not a template):** the six-step pipeline as a row from the first frame; the two stand-ins drawn as dashed arrows with the recipe's own sentence beside each; step 2 slots into the row and one dashed arrow turns solid; then one bad file is walked through the old route and the new one (stop, pass, total moves by 1,800.00, rejected).
**Beats (about 11):** B00 hook; B01 the row and the two stand-ins (the recipe's words on screen); B02 what the stand-in got right (same files in six of six sets); B03 one wrong input (a digit pair swapped); B04 the old route: step 1 stops, step 3 alone passes, step 5 prices 66,898.13; B05 the new door: rejected, with the reason; B06 what the stand-in skipped (listing, hash, per-file JSON at the moment of reading); B07 the stand-in still standing (step 5 reads step 3, not step 4), named not fixed; B08 the viewer's turn (their own list); B09 what was not tested (sample mode, invented prices, one swapped pair, one recipe, step 1 does catch it when it is run and heeded, no live call); B10 close.
**Short:** one scene, the row with its two dashed arrows; hook, the swapped digit, three results (stop, pass, 66,898.13), the new door, the viewer's list, the title.
**Tone:** first person, learning register; our own stand-in, our own gap; no verdict on anyone else's work; "step 1 does catch it" said plainly so the film does not overclaim.

## 4. Watch items for the drafts
1. No `trust`, `hand-off`, `quietly`, `fingerprint`, `tamper`, `same bytes`; do not retell W26's previous-close or W31's file-order finding (step 5 pricing a duplicate by file order).
2. Say that step 1 stops the changed file; the finding is that **step 3 on its own passes it**, not that the pipeline is unguarded.
3. Do not close on "it says draft, on purpose" (W27, W28, W30) or on "nothing deleted" (W25); no fellow's recipe on screen; only our recipe and our own words.
4. Run the word-run check on every draft (long and Short) before Gate P; record the result in `PROOF-REVIEW.md`.
5. The digit-swap run is a **scratch-copy test we did on purpose**; it is not committed and the film must say so.
