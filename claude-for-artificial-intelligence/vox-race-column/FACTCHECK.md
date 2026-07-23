# FACTCHECK — vox-race-column

Source: `computational-skepticism-for-ai/chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Fairness through unawareness (FTU) | Dropping sensitive attributes from the model — blocks direct use but not indirect reconstruction through proxies | Lines 209, 211 |
| Proxy reconstruction | Correlated features (zip code, surname, occupation) jointly reconstruct the deleted sensitive attribute | Line 209 |
| Fairness through awareness (FTA) | Explicitly naming and reasoning about the sensitive attribute in the similarity metric | Line 207 |
| Indirect discrimination | Model uses correlated features to recover the signal of a deleted attribute | Line 209 |
| Direct vs indirect path | Direct = model sees the sensitive attribute column; indirect = model recovers from correlated proxies | Lines 209, 211 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | Loan model deletes race column; zip code, surname, occupation reconstruct it; discrimination continues through invisible path | Line 209 | PASS |
| B04 | Correlated columns encode the sensitive attribute; removing the column leaves the correlated structure | Line 209: "zip code, surname, occupation — that correlate with group membership" | PASS |
| B05 | FTU blocks direct use; does nothing about indirect discrimination through correlated features | Line 209: exact | PASS |
| B07 | Reconstruction happens inside model's learned associations; direct path deleted, indirect paths open | Line 209 | PASS |
| B08 | Quote verbatim | Line 211: "FTU is not a fairness guarantee. It is a documentation choice that looks like one." | PASS |
| B09 | Fix: audit proxy features for correlation with deleted attribute | Line 209, 211 | PASS |
| B10 | Quote verbatim | Line 209: exact | PASS |
| B11 | Deleting column is documentation; audit outcomes by group | Lines 209, 211 | PASS |

| B12 | Hiring model removes names; university (ρ=0.19), ZIP code, prior employer remain as proxies; hiring rates for Black candidates unchanged after 6 months | Illustrative — numbers are made-up to demonstrate mechanism | ILLUSTRATIVE |

## VERDICT: PASS
