# Fact-check gate — documenting-the-system-and-making-the-demo-runnable (week 11)

Every number spoken or shown was checked against `figdata.json`, which is generated at build
time by querying the live database, reading the generated findings file, and running
`git show HEAD` against the working tree. **Rows 5, 6, 13, 17 and 19 are the ones to read
before signing.**

Verdict types, as in weeks 1–10:

- `REPRODUCIBLE` — re-run the committed query/script against the project repository or database.
- `EXTERNALLY VERIFIABLE` — open the named artifact or filing and read it.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | The plan names six documents | B00/B01/B02/B09 | REPRODUCIBLE | `documents[]` has six entries. Asserted at injection; B02's headline counts them rather than stating a literal. |
| 2 | Three of them did not exist at all | B00/B01/B02/B09 | REPRODUCIBLE | `existed: false` for `proposal.md`, `system_architecture.md`, `data_architecture.md`. The "before" is `git show HEAD:<path>`, so "did not exist" means the path was absent from the last commit — not that it was empty. |
| 3 | 444 lines written from nothing, 104 added to what was there | B01/B02/B09 | REPRODUCIBLE | Derived: 126 + 155 + 163 = 444; (262−231) + (1016−956) + (441−428) = 104. Both asserted against their literal values, and the injection asserts no document shrank. |
| 4 | An absent file has no "before" number | B02 | REPRODUCIBLE (asserted) | The injection asserts `lines_before == 0` for exactly the three absent documents, and **B02 prints the words "did not exist" in that cell** rather than a 0 that would sit in the same column as 231 and 956. A 0 there reads as "a document with no lines", which is a weaker and different finding. |
| 5 | **The requirement sat at zero in TWO published documents, not three** | B01/B03/B09 | REPRODUCIBLE — **read this one** | `prior_art[]` has three rows at `before: 0`, but `proposal.md` carries `existed: false`. Its zero is an absent file, not a document that failed the requirement. `w12-priorart.png` tabulates all three in one BEFORE column; its own caption says "in either published document", which is the correct, narrower claim. **The injection asserts 2 published zeroes and 1 non-finding zero**, and B03 draws them apart. If that split ever changes, the beat's whole argument changes with it. |
| 6 | **The five prior-art names** | B03 | AUTHOR-ASSERTED — **read this one** | Caplight, Gornall & Strebulaev, Agarwal, Chernenko, Kwon. **Not in `figdata.json`** — it carries counts, not names. Passed as `PRIOR_ART_NAMES`, and B03's source line says so. The grep that produced the zero was case-insensitive over these names; a different name list would produce a different zero. |
| 7 | 22 citations added, 13 of them where the requirement bit | B04/B09 | REPRODUCIBLE | `prior_art[].after` sums to 9 + 8 + 5 = 22; the two published documents account for 8 + 5 = 13. Both asserted. B04 leads with the 13 rather than the 22 wherever the claim is about the requirement. |
| 8 | A citation count is not a literature review | B04/B08 | AUTHOR-ASSERTED | Stated on B08 as a limit attached to the 22, rather than left for a viewer to infer. |
| 9 | Gornall & Strebulaev established that funds write up every share class to the latest round price | B04/B09 | EXTERNALLY VERIFIABLE | The finding is theirs and is in the published literature. **The claim that it is load-bearing here is the author's** — see row 10. |
| 10 | That citation changed a rule: dispersion is measured per company with the share class recorded, overturning an earlier draft | B04/B09 | AUTHOR-ASSERTED | **Not in `figdata.json`.** Passed as `LOAD_BEARING`, and B04's source line says so. This is the distinction the beat exists for: a decorative citation can be added at the end, and this one had to be read before the measurement was correct. |
| 11 | 15 tables in 3 layers | B05/B09 | REPRODUCIBLE | `layers[]` has three entries whose `tables[]` arrays contain 8, 4 and 3 entries. The injection asserts the sum equals `tables_total` (15), so the figure's own count cannot drift from the tables it lists. |
| 12 | Each layer's row total is the sum of its own tables | B05 | REPRODUCIBLE (asserted) | raw 19,084 · judgment 5,908 · resolved 5,946, each asserted equal to the sum of that layer's tables rather than trusted as a separate number. |
| 13 | **Every filed holding carries exactly one match decision — 5,806 = 5,806** | B05/B09 | REPRODUCIBLE — **read this one** | `raw_holdings` 5,806 and `match_decisions` 5,806, asserted equal. This is the identity B05 is built around. It is an equality of counts, not a proof of a one-to-one mapping; the frame says "one judgment row per filed row" and claims nothing stronger. |
| 14 | 45 of them needed a named human | B05 | REPRODUCIBLE | `review_decisions` 45. The remainder were resolved by method rather than by a person. |
| 15 | The resolved layer holds 5,479 marks — 327 fewer than were filed | B05/B09 | REPRODUCIBLE | `marks` 5,479, derived 5,806 − 5,479 = 327, asserted. The 327 is the guards: unpriced marks and split-blocked series, measured in weeks 7 and 8. |
| 16 | 25.0% unchanged — 1,019 steps of 4,079, over 5,178 marks | B06/B09 | REPRODUCIBLE | `remark`, with 1,019/4,079 = 0.2498 asserted against the stored share. Same statistic as week 8, from the same guarded function. |
| 17 | **The chain is eight links, published sentence to SEC archive file** | B06/B09 | AUTHOR-ASSERTED (structure) / REPRODUCIBLE (figure) — **read this one** | The eight links are `data_architecture.md`'s own trace and are not in `figdata.json`; only the headline figure is. The claim is that each link can be followed, not that following it has been independently audited. Break-any-link is an argument about the design, not a measurement of it. |
| 18 | 5 acts, 0 write statements across 5 scanned files | B01/B07/B09 | REPRODUCIBLE | `demo`, all three asserted. **It is a static scan**, not a proof that nothing writes — B08 says so on the frame. |
| 19 | **The run log has 2 rows** | B08/B09 | REPRODUCIBLE — **read this one** | `runs` in the raw layer. B06 claims the chain is datable because the run log records which run produced each artifact; that log currently has two entries. The reel states this as a limit on its own provenance claim rather than omitting it. |
| 20 | Exactly two places a language model sits, neither touching a number | B08 | AUTHOR-ASSERTED | **Not in `figdata.json`.** Passed as `LM_SITES`, from the architecture document, and B08's source line says so. |

## What this cut deliberately does NOT claim

- **No company valuation.** These filings give a fund's share count, never the company's shares
  outstanding. Unchanged across all eleven weeks.
- **No claim that three documents failed the requirement.** Row 5 — two did.
- **No claim that 22 citations constitute a literature review.** Row 8. Exactly one changed a rule.
- **No claim that the demo provably writes nothing.** Row 18 — a static scan of five files.
- **No claim that the provenance chain has been audited end to end.** Row 17 — it is a design
  that can be followed, and the run log behind it has two rows.
- **No claim that the audit is complete.** It covers the six documents the plan names. A
  requirement the plan never wrote down stays invisible to this method.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "I grepped for every name. Zero." | same, then "two published documents were genuinely at zero; the third was the proposal, which did not exist yet" | Row 5. The script's next sentence already says "in either published document" — this cut puts that precision on the frame instead of only in the voice. |
| "It's in three places now" | "13 citations added where the requirement actually bit", with 22 shown as the total | Row 7. Three places includes the document that did not exist. |
| — (not in the script) | "most of those twenty two are context; one is load-bearing" | Row 10. The script treats the Gornall & Strebulaev citation as the point; this cut shows what makes it different from the other 21. |
| — (not in the script) | "the run log has two rows in it — a start, not a history" | Row 19. The script claims the chain is datable; the thing that makes it datable is small enough to say out loud. |

## Before publishing

Rows 6, 10, 17 and 20 are the values this reel asserts that `figdata.json` does not contain.
Each is passed as a named constant and each beat that uses one says so on screen. **Row 5 is the
one that matters most**: the source figure's table shows three documents at zero and this reel
shows two, because one of those zeroes is an absent file. If that reading is wrong, B03 is wrong
and B09's second finding goes with it. Row 19 is where the reel limits its own provenance claim.
Everything else traces to `figdata.json` under an assertion. Publishing remains a separate,
explicitly authorized step.
