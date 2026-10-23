# Fact-check gate — entity-resolution-and-the-golden-set (week 4)

Every number spoken or shown was checked against `figdata_week4.json` (which the Mycroft repo
queries at render time, before anything is drawn), `README.md`, or `docs/worklog.md` in that
repo. **Rows 2, 12 and 16 are the ones to read before signing.**

Verdict types, as in weeks 1 and 2:

- `EXTERNALLY VERIFIABLE` — open the named filing on EDGAR and read the numbers.
- `REPRODUCIBLE` — re-run the committed query/script against the public data.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | Seven companies file under 128 distinct spellings | B00/B01/B02 | REPRODUCIBLE | Verified by summing `figdata.spellings` filtered to universe v1: Databricks 51 + Space Exploration 28 + OpenAI 23 + Anduril 11 + Anthropic 10 + Cerebras 3 + Figure AI 2 = **128**. The injection script asserts both the count (7) and the total (128) and fails the build otherwise. |
| 2 | **The seven are universe v1, not the top seven by spelling count** | B02 | REPRODUCIBLE — **read this one** | The worklog records this exact defect in the source figure: it took the top seven by count, which silently swapped Cerebras and Figure AI out for **xAI and Perplexity — both watchlisted, marks not published**. The rebuild filters to an explicit universe list and asserts the result, so the same error cannot recur here. X.AI's 19 spellings are deliberately excluded. |
| 3 | A further 24 spellings belong to watchlisted companies | B02 (on-screen note) | REPRODUCIBLE | Sum of the non-universe rows: X.AI 19 + Perplexity 3 + Groq 2 = **24**, asserted in the injection. Matches the worklog's "watchlisted companies account for 24". |
| 4 | Databricks: 51 spellings; Space Exploration: 28; Anthropic: 10 | B02 | REPRODUCIBLE | `figdata.spellings` — exact values, injected as props, not transcribed. |
| 5 | Hiding inside 3.2 million distinct issuer names | B02 | REPRODUCIBLE | `figdata.corpus.distinct_names_private` = **3,204,853**. Spoken as "three point two million"; the exact figure is on screen. |
| 6 | The on-screen Databricks strings are real, as filed | B02 | REPRODUCIBLE | `figdata.databricks_sample` — nine real strings, rendered verbatim (`DATABRICKS SER H CVT PFD STOCK PP` etc.). Nothing invented. |
| 7 | Golden set: 322 labelled issuer names covering 7,276 holdings | B00/B03/B09 | REPRODUCIBLE | `README.md` "Numbers on screen" table; consistent with the worklog's "314 of the 322 labels remain unattested". Spoken as "seven thousand two hundred and seventy-six". |
| 8 | Two systems were scored against the same labels | B03 | REPRODUCIBLE | `figdata.scoreboard` carries both `A_like_patterns` and `B_matcher_v1` over one label set. |
| 9 | Simple name patterns: precision 0.9916, recall 0.9792 | B04 | REPRODUCIBLE | `figdata.scoreboard.A_like_patterns.macro`. Spoken as "ninety-eight percent recall" — 0.9792 rounds to 98%. |
| 10 | Deterministic matcher: precision 0.9959, recall 1.0000 | B04 | REPRODUCIBLE | `figdata.scoreboard.B_matcher_v1.macro`. |
| 11 | Precision "barely moves" | B04 | REPRODUCIBLE | 0.9916 → 0.9959 is +0.0043 on 241 macro cases — one fewer false positive. The beat states this as noise rather than a win. |
| 12 | **On the hardest cases the old patterns were cleaner** | B04 | REPRODUCIBLE — **read this one** | `figdata.hard`: patterns precision **1.0000**, matcher **0.9929**. The matcher wrongly claims a used-car marketplace. The script's own note forbids claiming a precision win, and both the narration and the on-screen strip carry the loss rather than burying it. |
| 13 | One missing dot hid 85 holdings | B04/B05/B09 | REPRODUCIBLE | `figdata.xai.missed_holdings` = **85**. |
| 14 | The fund filing it without the dot is the largest holder | B05 | REPRODUCIBLE | `figdata.xai.top_family` = **Fidelity Mt. Vernon Street Trust**, rendered verbatim on screen. Narration says "Fidelity, the largest holder of that company". |
| 15 | OpenAir.com: 5 holdings, BlackRock and New York Life, all at 687.6869 | B06 | EXTERNALLY VERIFIABLE | `figdata.openair` — five rows across two period ends (2026-03-31 ×3, 2026-04-30 ×2), five registrant entities that roll up to **two fund families**: BlackRock (3) and New York Life (2). Rendered at family level, consistent with the series' family-not-CIK discipline from week 2. |
| 16 | **The OpenAI Series C anchor is 8 holdings from 6 registrants — NOT "LEI-confirmed"** | B06 | REPRODUCIBLE — **read this one** | `figdata.openai_anchor`: holdings 8, registrants 6, `lei_confirmed` = **1**. The worklog records correcting exactly this: an earlier write-up said "eight LEI-confirmed holdings", but only **one** carries OpenAI's registered identifier; the other seven name OpenAI outright. The on-screen note is worded "that name OpenAI, **or** carry its registered identifier" to stay true to that correction. |
| 17 | The label was approved, then withdrawn | B06/B07 | AUTHOR-ASSERTED | Worklog, 2026-08-22 (later): the adjudication was reviewed, `OPENAIR.COM` had been labelled `NOT_IN_UNIVERSE` on a stated ground that "was false", and the approval was withdrawn. |
| 18 | The struck reason is quoted accurately | B07 | REPRODUCIBLE | Worklog: the label rested on the claim that its price coincided with an OpenAI anchor "in exactly one period". There are five holdings across **two** period ends, so the reason was factually wrong. |
| 19 | Four holdings tie at confidence 0.80 — one wrong, three right | B08 | REPRODUCIBLE | `figdata.tied_at_080`: OPEN BAY AUTOS AI INC. (`NOT_IN_UNIVERSE`, predicted OpenAI, wrong) plus three SpaceX vehicles (DXYZ SPACEX I LLC, MWAM VC SPACEX-II ×2), all correct, all at 0.80. |
| 20 | Only 8 of the 322 labels have been reviewed by a person | B09 | AUTHOR-ASSERTED | Worklog: "**314 of the 322 labels remain unattested** — nobody has reviewed them", and 8 of 10 adjudications were confirmed by Om Mali. The verdict card states the 8 explicitly rather than letting "golden set" imply the whole set is human-checked. |

## What this cut deliberately does NOT claim

- **No precision win.** Row 12. The script's note is explicit and the reel obeys it: the honest
  claim is recall, and the hardest-cases strip shows the matcher losing.
- **No validated matcher.** B07 says the 1.0000 was measured *after* fixing what the test caught,
  and calls that "not a validation".
- **No trustworthy ground truth by implication.** B09 names the 8-of-322 figure out loud.
- **No threshold.** B08 shows a cut-off failing rather than asserting that tuning would fix it.
- **No valuation claim** anywhere, consistent with weeks 1 and 2.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "Last month's simple name patterns" | "The patterns I started with" | DOUBLE-CHECK LAW: strip anything that dates the video. Weeks 1–2 shipped the same month, so "last month" is both datable and slightly wrong. Same referent (`A_like_patterns`), no date claim. |
| "covering seven thousand holdings" | "seven thousand two hundred and seventy-six" | The exact figure is short enough to speak, and it is the one on screen. |
| "a ground truth set — three hundred and twenty-two of these strings" | "each labelled with the company it actually means" | The script's phrasing risks implying the labels are hand-made. Only 8 of 322 are. The rebuilt line states what the labels ARE without implying who made them, and B09 names the 8. |

## Before publishing

Rows 2, 12 and 16 are the three a reviewer is most likely to challenge, and all three are places
where the honest number is the less flattering one. Everything else traces to a committed query
or a named accession. Publishing remains a separate, explicitly authorized step.
