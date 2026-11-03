# Sources & Fact-Check — correlation-is-not-causation

**Checked:** 2026-10-14, against the primary texts themselves — the scanned journal pages, saved in
`sources/` — not against secondary summaries or memory.

## Citations (verified)

| | Citation | How verified |
|---|---|---|
| **[1]** | Charig CR, Webb DR, Payne SR, Wickham JE. Comparison of treatment of renal calculi by open surgery, percutaneous nephrolithotomy, and extracorporeal shockwave lithotripsy. *Br Med J (Clin Res Ed)* 1986 Mar 29;**292**(6524):**879–882**. doi:[10.1136/bmj.292.6524.879](https://doi.org/10.1136/bmj.292.6524.879) · PMID 3083922 · [PMC1339981](https://pmc.ncbi.nlm.nih.gov/articles/PMC1339981/) | PubMed record (NCBI E-utilities esummary) **and** the scanned pages: header "BRITISH MEDICAL JOURNAL VOLUME 292 29 MARCH 1986", article opens p. 879, references end p. 882 (`sources/bmjcred00227-0031…0034.png`) |
| **[2]** | Julious SA, Mullee MA. Confounding and Simpson's paradox. *BMJ* 1994 Dec 3;**309**(6967):**1480–1481**. doi:[10.1136/bmj.309.6967.1480](https://doi.org/10.1136/bmj.309.6967.1480) · PMID 7804052 · [PMC2541623](https://pmc.ncbi.nlm.nih.gov/articles/PMC2541623/) | PubMed record **and** the scanned pages: printed citation line "BMJ 1994;309:1480-1"; article runs p. 1480 to p. 1481 (`sources/bmj00468-0032…0033.png`) |

**Correction logged:** my earlier note cited [2] as "309:1480"; the article spans **1480–1481**.
In 1986 the journal's indexed title was *Br Med J (Clin Res Ed)*; the page header reads "British
Medical Journal". Both corrected in `beat_sheet.json` metadata.

**LibKey:** the organization's LibKey connector is not signed in to this session, so access links
have not been resolved through it. Run `/mcp` → "Scholarly Full Text Article Access with LibKey"
and I'll resolve both DOIs and add the links here. The bibliographic facts above don't depend
on it.

## The data, traced to [1] Table II (p. 880)

| Row in `sql/kidney_stones.sql` | [1] Table II | [1] Table I |
|---|---|---|
| open surgery · small · 87 patients · 81 successes | "All open procedures" group 1: **81 (93)** | 13 + 31 + 43 = **87** |
| open surgery · large · 263 · 192 | group 2: **192 (73)** | 218 + 45 = **263** |
| keyhole (PCNL) · small · 270 · 234 | "Percutaneous nephrolithotomy" group 1: **234 (87)** | **270 (77)** |
| keyhole (PCNL) · large · 80 · 55 | group 2: **55 (69)** | **80 (23)** |
| totals | open **273 (78)** of 350; PCNL **289 (83)** of 350 | — |

[1] p. 880 defines the groups: "group 1 were those with stones of a mean diameter of less than 2 cm
and group 2 those with stones of a mean diameter of 2 cm or more **or with multiple stones**."
Success: "free of stones at three months or… fragmented into particles of less than 2 mm."

**Misprint in [2]:** it prints small-stone PCNL as "83% (234/270)". 234/270 = 86.7%; [1] Table II
prints 87. The reel uses the counts, so it shows 86.7 / "eighty-seven". [2] is cited for the framing,
not this number.

## Claim-by-claim trace

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | real hospital data can point you to "the worse treatment" | [1] Table II | **RESOLVED (Flag A)**: now "the wrong answer". The old wording was true for success rate within each size group, but [1] also weighs cost and morbidity, and favors the less invasive methods. See flags |
| 2 | B01 | "Doctors treated kidney stones two ways" | [1] abstract: 350 open, 350 PCNL, **328 ESWL**, 24 PCNL + ESWL | **RESOLVED (Flag B)**: now "A study compared two ways…". The study compared three methods (four groups). The reel deliberately covers two |
| 3 | B01 | 350 patients each | [1] abstract | CONFIRMED |
| 4 | B01 | a British Medical Journal study, 1986 | [1] page header | CONFIRMED |
| 5 | B01 | "Say you run the hospital. You have to pick one." | [1] p. 879: open surgery **1972–1980**, PCNL **1980–1985**, consecutive, same surgical team | **NOTED (Flag C, no change)**: a hypothetical framing. The two treatments were used in different eras, not side by side |
| 6 | B02 | success = stones gone or nearly gone at three months | [1] p. 880 definition | CONFIRMED (paraphrase of "<2 mm") |
| 7 | B04 | keyhole 82.6%, open 78.0%, almost five points | `sql/q1_by_treatment.out`; [1] 289/350, 273/350 | CONFIRMED (gap 4.6) |
| 8 | B05 | large stones are harder to clear | [1] p. 881: "Stones greater than 2 cm lead to a high failure rate with all forms of treatment"; Table II, every method lower in group 2 | CONFIRMED |
| 9 | B07 | small: 93 vs 87; large: 73 vs 69; open surgery wins both | `sql/q2_by_size.out`; [1] Table II | CONFIRMED (68.75 → "sixty-nine"; on-screen 68.8) |
| 10 | B07/B08 | "large stones" | [1] group 2 = ≥2 cm **or multiple stones** | CONFIRMED as a simplification. On-screen labels and the SQL comment now say "≥2 cm or multiple" |
| 11 | B08 | 263 of surgery's 350 had large stones; keyhole had 270 small | [1] Table I | CONFIRMED |
| 12 | B08 | "the hard cases went to surgery" | [1] p. 880: "Most open procedures were for stones greater than 2 cm in diameter, whereas most of the closed procedures were performed for smaller stones"; [2] "the probability of having open surgery or [PCNL] varied according to the diameter of the stones" | CONFIRMED. Describes who got what, not anyone's intent |
| 13 | B09 | even the split is observational; only randomizing rules out unmeasured causes | [2]: "In observational (non-randomised) studies… Randomised trials are therefore necessary to demonstrate any treatment effect"; [1] is "a historical comparison" ([2]) | CONFIRMED |
| 14 | B10 | handoff prompt | — | Instruction, not a factual claim |

## Flags (decided by Supriya 2026-10-15: A and B applied, C no change)

**A — B00 "the worse treatment."** The data supports "less successful", but the paper's verdict is
broader: PCNL cost £1861 vs £3500 for open surgery, and the paper favors less invasive methods.
"Worse" implies a clinical verdict the reel doesn't argue. *Suggested:* "…and how real hospital
data can point you to the wrong answer." (same length)

**B — B01 "two ways."** The study had a third method (ESWL, shockwave), which beat both. *Suggested:*
"Here's the problem. A study compared two ways of treating kidney stones: open surgery, and a
keyhole procedure." Accurate, and it doesn't claim these were the only two.

**C — the eras (no change suggested).** Open surgery came from 1972–80 and PCNL from 1980–85, so
time is a second possible confounder. The B09 caveat ("only randomizing rules out the causes nobody
measured") already covers this honestly. B01's "Say you run the hospital" reads as a hypothetical. I'd
leave the narration alone and keep this note as the record.

## Dating check (DOUBLE-CHECK LAW)

No model names or version numbers anywhere. The composer's model chip reads plain "Claude". The
1986 date is the study's, not the video's.

## No paid services

SQLite, Kokoro (`af_bella`, local), Manim, Remotion. No keys anywhere.

## 9:16-only presentation changes (no new claims)

- B00 result lines shortened for portrait ("by size — surgery wins both", "why — who got which
  treatment"). Same meaning.
- B04/B07 use horizontal bars; B07 adds a pale "overall" strip showing B04's own figures (82.6%,
  78.0%). Every number still parsed from `sql/*.out`.
- Endcard: "Supriya", "Correlation is not causation. / Check who got what.", "Built with Claude."
  These restate the reel; no new claim.
