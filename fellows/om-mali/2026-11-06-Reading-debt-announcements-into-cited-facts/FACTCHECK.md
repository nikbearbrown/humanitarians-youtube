# Fact-check gate — reading-debt-announcements-into-cited-facts (AI Debt Tracker, week 4)

Every number spoken or shown is a prop injected from `figdata.json` by `build_beat_sheet.py`
under assertions. Nothing is typed into a scene. `figdata.json` transcribes the author's own
saved results as published in `pantry/*.svg` and in `narration_script.md`'s source table; each
bar's geometry in those SVGs was recomputed as a ratio and had to agree with its printed
fraction before the value was accepted.

**Rows 2, 4, 5, 8, 11, 15, 17, 19 and 22 are the ones to read before signing.**

Verdict types, as in every earlier episode:

- `REPRODUCIBLE` — re-run the committed query/script against the AI Debt Tracker repository.
- `EXTERNALLY VERIFIABLE` — open the named filing or report and read it.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | The event reader works in three steps: code picks the passages, the model lists instruments and copies the exact words, code checks the words and parses the number | B00/B01/B09 | REPRODUCIBLE | `docs/reader.md`. The "model never types a number" rule is from DESIGN.md, written in week 1 and unchanged. |
| 2 | **The reader read 157 of 167 fields right (94%); B1 regex read 135 of 160 (84%); B2 — one model call typing each value — read 160 of 160 (100%)** | B00/B03/B04/B08/B09 | REPRODUCIBLE — **read this one** | `docs/reader.md`, `manifests/reader_truth.json`. The reel's framing assertion is that B2 > reader; the build fails if the reader ever overtakes it. The three denominators **differ** (167 / 160 / 160) and every row prints its own fraction — see row 4. |
| 3 | The week's check was "beat B1 on field accuracy", fixed in the design in week 1 before any method ran | B03/B08/B09 | AUTHOR-ASSERTED (design) / REPRODUCIBLE (result) | DESIGN.md. This is what makes "it passes" mean anything; a check chosen after the run would not. |
| 4 | **The three bars do not share a denominator** | B03 | REPRODUCIBLE — **read this one** | 157/167 vs 135/160 vs 160/160. The reader is scored over more fields because it reports more instruments (row 5). A viewer who reads the three bars as one scale is reading a comparison that was never run. The build asserts `reader.of != b1.of` so this can never quietly become a footnote. |
| 5 | **The reader reported 29 instruments the filings do not announce; B2 reported 9 and B1 reported 1** | B03/B09 | REPRODUCIBLE — **read this one** | `manifests/reader_truth.json`. The reader invents the most. This is the counterweight to 94% and the build asserts the ordering, so a frame cannot show the accuracy without the cost. |
| 6 | 24 filings, 66 instruments, labelled before any of the three methods ran; the label file has the same hash before and after | B03/B08/B09 | REPRODUCIBLE | `manifests/reader_truth.json`; FRICTIONAL.md. |
| 7 | The reader was developed only on the week 1 bake-off documents, which are not in the evaluation set — three rounds, then frozen, then run once | B03 | AUTHOR-ASSERTED (process) | FRICTIONAL.md. Not stated on screen; it is why the 94% is a held-out number rather than a fit. Worth saying if you want it said. |
| 8 | **62 of the 66 instruments were new notes in pricing documents; 4 were loans, amendments or redemptions** | B08 | REPRODUCIBLE — **read this one** | FRICTIONAL.md. This is the single largest limit on the 94%: the set is mostly easy documents, which is also why B2 did so well. Drawn on B08 as the first limit. |
| 9 | For Alphabet's euro notes the filing says €1,500,000,000 and the model "copied" $1,500,000,000 | B02/B09 | EXTERNALLY VERIFIABLE | Alphabet 8-K, 6 May 2025, passage `d0:s6`. Open the filing and read the sentence. |
| 10 | Those values were refused because the copied words are not in the cited passage | B02/B04/B09 | REPRODUCIBLE | `week4/reader_reader.json`. A refused value is recorded missing, not wrong. |
| 11 | **254 copied values in all: 227 found in the passage the model cited, 3 in a different passage, 24 refused** | B05/B09 | REPRODUCIBLE — **read this one** | `docs/reader.md`, `week4/reader_reader.json`. The build asserts the three outcomes sum to every copy made. B05 draws the 24 as 24 cells rather than as a 9% sliver of a band. |
| 12 | Of the 24 refused, 8 were currency signs rewritten (€ or CHF → $) and 16 were the word "null" written out as text | B05/B09 | REPRODUCIBLE | Same source. The build asserts 8 + 16 = 24. The 16 are a bookkeeping bug with no effect on any score, fixed in code afterwards; the reel says so rather than counting them as catches. |
| 13 | Fresh triage: 50 new filings labelled before the run, after last week's two rule fixes | B06/B09 | REPRODUCIBLE | `docs/triage.md`, `manifests/triage_labels_w4.json`. |
| 14 | Triage found 8 of the 9 debt filings — 89%, below the 95% pass line | B00/B06/B08/B09 | REPRODUCIBLE | Same source. The pass line was fixed in the design before the run. The build asserts the fresh score is **below** the line, so the reel cannot announce a failure that did not happen. |
| 15 | **This is a failed check, and the video says so on camera** | B06/B08/B09 | AUTHOR-ASSERTED — **read this one** | The miss is logged as P46 and was not tuned away. Confirm you are content for the reel to state a failed self-set check in the cold open, the body and the verdict. |
| 16 | The miss is an IBM euro prospectus whose cover is blank even where the year's "20" should be, and whose contents listed "Preferred Stock" | B06 | EXTERNALLY VERIFIABLE | The prospectus cover. The frame sets the cover as it reads — `€   % Notes due` — rather than describing it. |
| 17 | **Only 9 debt filings were in the 50-filing draw** | B06/B08 | REPRODUCIBLE — **read this one** | Nine positives cannot separate a rule problem from an unlucky draw. Said on camera and drawn as a limit on B08. |
| 18 | One of the 4 false alarms is probably a labelling error — an Applied Digital earnings release does announce a $150m Macquarie financing | B06 | AUTHOR-ASSERTED | FRICTIONAL.md. Labels are not changed after a run, so it stays scored as a false alarm. On the frame beneath the miss. |
| 19 | **The answer key agreed on 1 of 5 fresh reports; last week's 3 of 3 is a calibration** | B07/B09 | REPRODUCIBLE — **read this one** | `docs/handcheck.md`, `manifests/handcheck/`. Same shape as week 3: a set the fixes were made against clears any line. The build asserts fresh < last. |
| 20 | Four new defects, each in a different company's tagging: Constellation P41, Marvell P42, Intel P43, Applied Digital P44 | B07/B09 | REPRODUCIBLE | `docs/handcheck.md`; DESIGN.md P41–P44. The build asserts the four companies are distinct, because "each in a different company's tagging" is a sentence that can go stale. |
| 21 | Amazon's five totals agree exactly | B07 | EXTERNALLY VERIFIABLE | The printed debt table in Amazon's report, against `answer_key/`. |
| 22 | **One slip: the key's totals for the five reports were printed once before the transcriptions were written** | B07 | AUTHOR-ASSERTED — **read this one** | Disclosed in `docs/handcheck.md`. It weakens "chosen before reading" slightly and the reel discloses it on the frame rather than in the description only. |
| 23 | The labels, the reader truth and the transcriptions are Claude's reading — a model judgment, not a person's | B04/B08/B09 | AUTHOR-ASSERTED | FRICTIONAL.md; each file says so. The reel never says "I labelled". |
| 24 | Machine check on the labels: all 51 labelled new bonds with a coupon and a year appear in the next quarterly report's XBRL with the same coupon and year; the labelled principal agrees on 19 of 19 | B08 | REPRODUCIBLE | `docs/reader_truth.md`. This is a real check and it is not a person reading them; B08 says both halves. |
| 25 | Three reader defects are open and unfixed on purpose | B08 | AUTHOR-ASSERTED | FRICTIONAL.md names three (the currency sign; a "$500 million term loan facility" sentence scoring below the passage threshold; a blank preliminary prospectus read as new notes) and gives **no defect ids** for them, unlike P41–P46. None is invented here and no frame shows an id for them. |
| 26 | The week's gate is recorded DELEGATED, not CLEARED, and no person has reviewed the labels, the truth or the results | B00/B08/B09 | AUTHOR-ASSERTED | `manifests/week4_gate.json`; FRICTIONAL.md. Drawn as the largest object on B08. |
| 27 | Nothing was spent | all | REPRODUCIBLE | Kokoro TTS local, Remotion, ffmpeg. `$0.00`, no API key. |

## What is NOT claimed

- **The reader is not claimed to be more accurate than either baseline.** It beat B1, which was
  the check; B2 read every field right. Four separate frames carry both numbers.
- **The reader is not claimed to be production-ready.** Three of its defects are open.
- **Triage is not claimed to pass.** It failed its fresh check.
- **The answer key is not claimed to be fixed.** 1 of 5, with P41–P44 open.
- **Nothing here is claimed to have been reviewed by a person.** That is the open step, for
  week 3 as well as week 4.
