# Fact-check gate — building-the-filing-timeline-triage-and-document-server (AI Debt Tracker, week 3)

Every number spoken or shown is a prop injected from `figdata.json` by `build_beat_sheet.py`
under assertions. Nothing is typed into a scene. `figdata.json` transcribes the author's own
saved results as published in `pantry/*.svg` and in `narration_script.md`'s source table; each
bar's geometry in those SVGs was recomputed as a ratio and had to agree with its printed
fraction before the value was accepted.
**Rows 3, 5, 9, 12, 13, 16 and 19 are the ones to read before signing.**

Verdict types, as in every earlier episode:

- `REPRODUCIBLE` — re-run the committed query/script against the AI Debt Tracker repository.
- `EXTERNALLY VERIFIABLE` — open the named filing or report and read it.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | Last week's three data problems are fixed, and its three test reports now all agree | B01/B08/B09 | REPRODUCIBLE | `docs/handcheck.md`, DESIGN.md P35–P37. See row 3 — this number is a calibration. |
| 2 | Five fresh reports were drawn before reading and graded once | B01/B02/B09 | AUTHOR-ASSERTED (process) / REPRODUCIBLE (result) | `manifests/handcheck/*.json`. The draw is by a fixed seed; that it was done before reading is the author's own account of his process. |
| 3 | **Two of the five had no debt on either side, so 1 of 3 — not 1 of 5** | B01/B08/B09 | REPRODUCIBLE — **read this one** | Cipher Mining and TeraWulf had no debt at those dates. Scoring 1 of 5 would penalise the key for reports with nothing in them; dropping the two silently would hide a denominator change. **B01 draws them as a dashed, excluded tail beyond the bar**, and the injection asserts gradable + not-gradable = drawn. |
| 4 | Dell's totals agree exactly | B02/B09 | EXTERNALLY VERIFIABLE | The printed debt table in Dell's report, against `answer_key/`. |
| 5 | **The answer key counted the banks' over-allotment on a Super Micro convertible as a second bond (P38)** | B02/B08/B09 | REPRODUCIBLE — **read this one** | `docs/handcheck.md`; DESIGN.md P38. A real defect in the key, found by a report it had not been tuned on. **Left open deliberately** — fixing it against the report that found it would turn next week's check into another calibration. |
| 6 | Core Scientific's small notes have no due date anywhere in the data (P39) | B02/B08/B09 | REPRODUCIBLE | Same source, DESIGN.md P39. Also left open. |
| 7 | One reading mistake in the hand-check was the author's own | B02 | AUTHOR-ASSERTED | A Super Micro coupon was transcribed from the notes' *original* terms; they were amended in 2025. **The transcription was done by Claude in the hand-check**, and the author records it as his. Disclosed in `docs/handcheck.md`; it does not change the verdict, because the double-counted allotment alone makes that report disagree. The script's Notes offer this line; it is said on camera. |
| 8 | 593 filings gathered across the dev-quarter windows — 469 8-Ks, 94 prospectuses, 30 term sheets | B00/B03/B09 | REPRODUCIBLE | `week3/pool.json` ← `scripts/triage_eval.py pool`. The injection asserts the three types sum to 593, so B03 can draw them as the composition of the window. |
| 9 | **The windows include the subsidiaries that borrow on a company's behalf** | B03 | AUTHOR-ASSERTED (design) — **read this one** | A company's debt is often issued by a financing subsidiary. If those CIKs were not in the window, the filing announcing a bond would simply not be there and the miss would be invisible to every later check. This is a design decision, stated on the frame. |
| 10 | The window ends at the report the quarter is graded on | B03/B07/B09 | REPRODUCIBLE | Week 1's point-in-time rule, unchanged. The window's right edge is drawn as the one solid accent rule on B03. |
| 11 | Five rules decide 394 of 593; 199 go to the model; 184 are kept (163 by rule, 21 by model) | B00/B04/B09 | REPRODUCIBLE | `week3/triage_qwen3_4b.json` ← `triage_eval.py run qwen3:4b`; `docs/triage.md`. The injection asserts 394 + 199 = 593 and 163 + 21 = 184 — every filing is decided somewhere, and what is kept is what each decider kept. |
| 12 | **qwen3:4b at a median 3.1 s per filing, asked only about the doubtful third** | B04/B09 | REPRODUCIBLE — **read this one** | Same source. The model is not the filter; it decides a third of it. Presenting triage as "a model reads the filings" would overstate the model's role by two thirds, and understate how much a plain rule can do. |
| 13 | **Triage found all 24 debt filings in the 50-filing sample; the pass line was 95%** | B00/B05/B08/B09 | REPRODUCIBLE — **read this one** | `docs/triage.md`, `manifests/triage_labels.json`. 24 of 24 is **recall**, on 24 positives inside a 50-filing sample. The injection asserts recall is perfect AND that both other scores are lower, because the beat is a flattering number with its qualifiers beneath it. |
| 14 | Precision 24 of 26; event type right on 20 of 24 | B05/B08/B09 | REPRODUCIBLE | Same source. Both are on screen directly beneath the recall bar, on the same scale. |
| 15 | The two false alarms: a tender offer for Alphabet shares (not notes), and a TeraWulf acquisition | B05 | REPRODUCIBLE | Same source. The injection asserts that **the two named alarms are exactly the gap between 24 found and 26 kept** — a frame that names two mistakes while its arithmetic implies a different number would be lying quietly. |
| 16 | **The 50 labels are Claude's judgment, made before triage ran** | B05/B08/B09 | AUTHOR-ASSERTED — **read this one** | `docs/triage_labels.md`. 30 drawn at random, 20 from filings containing debt words, labelled against a written definition, and the labels file is byte-for-byte unchanged after the run. **A different model from the one being tested — but not a person.** The script's Notes require this phrasing; the reel never says "I labelled". |
| 17 | All 22 filings that last week's search found announcing a bond change are kept | B05/B09 | REPRODUCIBLE | `docs/triage.md`. The first version of that report said 21 of 22; the "missed" one was last week's own bug — see row 18. |
| 18 | The check exposed a bug in last week's search: "0%" matched inside "20%" | B06/B09 | REPRODUCIBLE | DESIGN.md P40, `logs/RUN_LOG.md` 2026-10-31. A 0% 2031 convertible had been credited to an earnings release because "0%" matched inside "escalates 20%". Fixed; **last week's published counts did not change.** |
| 19 | **8 of the model's 21 "yes" quotes were not word for word in the text it was given** | B06/B08/B09 | REPRODUCIBLE — **read this one** | `docs/triage.md`. The check compares the first 80 characters of the model's quote with the text it read. **A mismatch can be a paraphrase rather than an invention**, so the reel does not say "made up", the filing is still kept, and the limit beat says the event reader must re-check every fact. |
| 20 | The first run crashed on a cut-off model answer; now an unreadable answer keeps the filing | B06 | REPRODUCIBLE | `docs/triage.md` (Notes on this run). The fail-open direction is the point: an unparseable answer must not silently drop a filing. |
| 21 | The docs server resolves `search("4.200% Notes due 2029")` to `s5` of Oracle's 8-K, and refuses the graded report | B07/B09 | REPRODUCIBLE | `src/ai_debt_tracker/documents/`, `mcp_servers/docs.py`. The figure was built by a live call to `documents/store.py`. |

## What this cut deliberately does NOT claim

- **No claim that the agent can read a filing.** It finds filings and makes them citable.
- **No claim that the answer key is fixed.** Row 3 — 1 of 3 on fresh reports, two defects open.
- **No claim that 3 of 3 is evidence.** Row 1 — the fixes were made against those reports.
- **No claim that triage is accurate.** Row 13 — it is *complete* on this sample; precision is
  24 of 26 and the event type is right 20 times in 24.
- **No claim that 24 of 24 will hold.** 24 positives is a small set; next week runs a fresh check.
- **No claim that a person labelled the sample.** Row 16 — a different model did.
- **No claim that the model invented quotes.** Row 19 — not verbatim is not the same as invented.
- **No claim that the rules are the model's work, or the reverse.** Row 12 — two thirds of the
  decisions never reach a model at all.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "Of the three that had any debt, only one agreed" | same, preceded by "**two of them had no debt on either side, so there was nothing to grade**" | Row 3. The script's Notes carry the exclusion; this cut says it before the fraction so the denominator is never heard as 5 or as a silent 3. |
| "last week's three test reports now all agree" | same, with "**that score is a calibration, not a measurement**" on the frame | Row 1. Same distinction the reel drew in week 2, and it applies again here. |
| — (the script offers it optionally) | "**and one reading mistake was mine**" | Row 7. The script's Notes offer the line "if you have time". It costs two seconds and removes an asymmetry where only the key's mistakes are named. |
| "Triage found all twenty-four debt filings" | same, with precision and event type on the same scale directly beneath | Rows 13–14. The script's Notes insist 24 of 24 is recall and not accuracy. |
| "a quote that isn't word for word in what it read" | kept verbatim; the frame adds "**can be a paraphrase rather than an invention**" | Row 19. The script's Notes forbid "made up". |
| — (the script's closing section is on camera) | B08, a limits beat, with the three next steps inside it | Every episode in this series ends on its own limits. |

## Before signing

Rows 2, 7, 9 and 16 are the claims this reel makes that `figdata.json` does not measure. Each
is passed as a named constant or stated as a design property, and each beat that uses one says
on the frame where it came from.
