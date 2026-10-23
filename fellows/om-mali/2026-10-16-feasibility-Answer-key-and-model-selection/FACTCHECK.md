# Fact-check gate — grounding-an-ai-debt-tracker-in-real-sec-filings (AI Debt Tracker, week 1)

Every number spoken or shown is a prop injected from `figdata.json` by `build_beat_sheet.py`
under assertions. Nothing is typed into a scene. `figdata.json` transcribes the author's own
saved results as published in `pantry/*.svg` and in `narration_script.md`'s source table.
**Rows 4, 7, 9, 12, 15 and 18 are the ones to read before signing.**

Verdict types, as in every earlier episode:

- `REPRODUCIBLE` — re-run the committed query/script against the AI Debt Tracker repository.
- `EXTERNALLY VERIFIABLE` — open the named filing or report and read it.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | $121bn of US bonds sold in 2025 by Amazon, Alphabet, Meta, Microsoft and Oracle | B01/B08/B09 | EXTERNALLY VERIFIABLE | Bank of America data, reported by Reuters / Yahoo Finance ("AI hyperscalers will drive higher US corporate bond supply in 2026"). **Not this project's measurement** — B08 says so on the frame. |
| 2 | Their 2020–2024 average was $28bn/yr, so 2025 is 4.3× it | B01/B09 | EXTERNALLY VERIFIABLE (figures) / REPRODUCIBLE (ratio) | Same source. The multiple is **derived** at injection from the two bars and asserted to equal the stored 4.3 — it is never stated as an independent number. |
| 3 | No Mycroft agent tracks debt | B01/B09 | AUTHOR-ASSERTED | The Mycroft repo's `recipes/` — ~99 recipes, none on debt or credit. **Not in `figdata.json`**; passed as `MYCROFT_RECIPES` and B01's own frame says where it comes from. A recipe added after this reel was cut would not be visible to it. |
| 4 | **The agent does not exist yet** | B00/B02/B03/B09 | AUTHOR-ASSERTED — **read this one** | The four-box pipeline on B02 is `DESIGN.md`, not status. Week 1 built the answer key, the point-in-time server, the matcher and the model test; the reader-and-ledger agent is unwritten. The script's Notes flag exactly this risk ("Keep the tense honest"), and B02 carries the correction **in writing on the frame** rather than only in the voice. |
| 5 | The universe is 25 AI-sector companies, with 75 non-AI companies alongside | B02/B05 | REPRODUCIBLE | `universe_v1.json`. The injection asserts the three grading levels sum to exactly the 25, so B05's bar cannot be drawn as a partition of a number it does not partition. |
| 6 | Every quarter is graded against that company's NEXT quarterly report | B03/B09 | AUTHOR-ASSERTED (design) | `DESIGN.md`. The claim is about how grading is defined, not a measurement. |
| 7 | **A point-in-time server refuses any filing published after the report being graded on** | B03/B09 | REPRODUCIBLE — **read this one** | `src/ai_debt_tracker/mcp_servers/edgar_pit_core.py`, `tests/test_edgar_pit.py`. This is the one claim every later number depends on: without the refusal, a model can be shown the answer. **Not in `figdata.json`** — it is a property of code, not a figure — and B03's source line names the two files. The claim is that the server refuses, not that every historical run was audited for leakage. |
| 8 | 87.5% of new bonds were announced before the report showed them — 56 of 64, over 46 company-quarters | B00/B04/B09 | REPRODUCIBLE | `figdata.json ← spike artifacts`; `docs/feasibility.md`. 56/64 = 0.875 asserted against the stored share and against its 0.80 pass line. |
| 9 | **56 of 64, not 56 of 73** | B04/B08 | REPRODUCIBLE — **read this one** | The denominator is *genuinely new bonds carrying a stated interest rate*. Nine old bonds that were only newly tagged are excluded; counting them gives 76.7%, which falls **below** the 80% line. The exclusion is therefore load-bearing, not cosmetic. The script's Notes say "Don't round 87.5% up to 'nearly ninety'" for the same reason. |
| 10 | 46 company-quarters cover 23 companies, not all 25 | B04 | REPRODUCIBLE (asserted) | The injection asserts `spike.companies < universe.ai`. B04's subtitle says 23 so the spike is not read as covering the whole universe. |
| 11 | Copying last quarter forward is wrong in 21 of 46 quarters | B04/B09 | REPRODUCIBLE | `figdata.json`; `docs/feasibility.md`. 21/46 = 45.6%, against a 0.30 pass line. |
| 12 | **21 of 46 is the conservative count; raw it is 33 of 46** | B04/B08 | REPRODUCIBLE — **read this one** | Carry-forward differed from the next report in 33 of 46 quarters, but part of that is companies changing how they tag rather than new debt. 21 is the count with a change confirmed by an announcement. The injection asserts `raw > conservative`, so the footnote can never be backwards, and B04 prints both numbers. |
| 13 | The answer key covers every quarterly report from Jul 2024 to Sep 2026 | B05 | REPRODUCIBLE | `manifests/generalisation.csv`, `universe_v1.json`. |
| 14 | Microsoft's 13 "bonds" are 13 batches of bonds; Oracle's 10-Qs list only the newest few | B05 | EXTERNALLY VERIFIABLE | The filings themselves; written up in `docs/universe_v1_review.md`. **Not in `figdata.json`** — passed as `COARSE_EXAMPLES`. These are the two concrete cases behind the recount; they illustrate it, they do not constitute it. |
| 15 | **15 companies can be graded bond by bond, not the 21 assumed** | B00/B05/B08/B09 | REPRODUCIBLE — **read this one** | 21 was a count of companies that *looked* per-bond by counting tagged members. Measured by coverage — itemised instruments must account for ≥ 80% of total debt — 14 qualified, and the gate moved one more up on a 4–4 tie: 15. **This is the reel's framing assertion**: the build fails if the measured count ever stops being lower than the assumed one, or if the three levels (15 / 4 / 6) stop summing to 25. `manifests/week1_gate.json`, DESIGN.md P22–P23. |
| 16 | 495 dated test cases: 95 to build on, 400 held back | B00/B06/B09 | REPRODUCIBLE | `manifests/dev.csv` + `test.csv`. The injection asserts 95 + 400 = 495 and that the held-back set is the larger of the two. "Never tuned on" is a statement about process, asserted by the author. |
| 17 | Bonds match report to report 93.4% of the time — 594 of 636, against a 90% line | B06/B09 | REPRODUCIBLE | `scripts/f1_matching.py dev`; `docs/feasibility.md`. 594/636 = 0.934 asserted, and asserted to clear the stored 0.90 line. |
| 18 | **93.4% is the per-bond quarters only; across every quarter it is 85%** | B06/B08 | REPRODUCIBLE — **read this one** | The gap is Intel and Oracle quarters that list few bonds and are graded on totals anyway. The injection asserts the all-quarters figure stays **below** the per-bond one, because the caveat only means something while that is true. Both beats print it; the voice keeps "from one report to the next". |
| 19 | Qwen3 4B read 99% of bond details (141/143) in ~6.1s a filing at $0, ahead of Llama 3.1 8B at 91% and Qwen3 8B at 88% | B00/B07/B09 | REPRODUCIBLE | `docs/bakeoff.md ← scripts/bakeoff.py report`. All three share the denominator 143, asserted, so one scale is honest. The injection also asserts the winner is the **smallest** model and wins outright — "the smallest won" is the beat, and a tie would be a different video. |
| 20 | 99% is after correcting 6 expected values the documents contradicted — 95% before, same winner — on 29 documents | B07/B08 | REPRODUCIBLE | `manifests/bakeoff_truth_corrections.json`. The injection asserts the before-figure is lower than the after-figure. 29 documents is a small set; B07's own caveat and B08's first row both say so, and the beat says "twenty-nine" aloud so nobody hears it as a benchmark. Two 8B runs looped on their own answers until cut off (3 and 2); the 4B never did. |

## What this cut deliberately does NOT claim

- **No claim that the agent exists.** Row 4. The ground under it was built; it was not.
- **No claim that 87.5% is "nearly ninety".** Row 9 — and on the wider denominator it is 76.7%,
  under the line.
- **No claim that carry-forward is wrong half the time.** Row 12 — 21 of 46 is the confirmed
  count; 33 of 46 is the raw one and includes re-tagging.
- **No claim that 21 was a mistake in the data.** Row 15 — it was a different, weaker way of
  counting. The recount changes what the agent may be graded on, not what the filings say.
- **No claim that 93.4% holds across the whole universe.** Row 18 — it is 85% there.
- **No claim that the bake-off is a benchmark.** Rows 19–20. One plain prompt, 29 documents,
  six truth corrections, and the finished extraction system is not this.
- **No claim about the point-in-time server's historical runs.** Row 7 — the server refuses;
  that is tested. Auditing every past run for leakage is not claimed.
- **No company valuation.** Unchanged across every episode: SEC filings give a company's debt,
  not a view on what the company is worth.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "The agent watches SEC filings … reads … keeps a ledger" | "The agent **will** watch … None of this is built yet", plus a tense note on the frame | Row 4. The script's own Notes offer this correction ("If that sounds too finished, say 'will watch'"). A four-box pipeline reads as a description of something that exists. |
| "wrong almost half the time" | "wrong in twenty-one of those forty-six", with 33 of 46 printed as the raw count | Row 12. "Almost half" is true of the conservative number and nearly true of nothing else said out loud; the fraction is unambiguous. |
| "bonds now match … ninety-three percent of the time" | same, kept with "from one report to the next", plus 85% across every quarter on the frame | Row 18. The script's Notes require the qualifier; this cut puts the other number beside it rather than only in the voice. |
| "Oracle's quarterly reports list only the newest few" | kept on the frame, dropped from the voice | The script marks this line as the one to drop if the cut runs long. It survives as a written example beside Microsoft's. |
| — (not in the script) | B08, a whole limits beat | Every episode in this series ends on its own limits. The content comes from the script's own Notes section, which otherwise would never reach the screen. |

## Before signing

Rows 3, 4, 6, 7 and 14 are the claims this reel makes that `figdata.json` does not contain.
Each is passed as a named constant and each beat that uses one says on the frame where it
came from.
