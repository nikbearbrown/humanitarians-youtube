# In-flight QC notes (collected during the render, resolved in the final pass)

| # | Cut | Beat | Observation | Severity | Disposition |
|---|---|---|---|---|---|
| 1 | 9:16 | B00 | Bottom ~25% empty. NOT a defect — it is the toolkit's documented 9:16 active band (230–1440), reserved for platform UI. The stock 916 scenes all leave it. | none | accepted |
| 2 | 9:16 | B01, B03, B05, B06 | Custom portrait scenes originally placed verdict/footnote at y≈1450–1620, inside the reserved band. | MAJOR | FIXED before render — all four pulled inside 230–1440. Verified on B01. |
| 3 | 9:16 | B01 | Verdict wraps to two lines with a one-word widow ("job"). Legible, but a typographic blemish on a poster line. | MINOR | Candidate fix: drop the portrait verdict from 46px to 42px so it sets on one line (needs ~915px vs the 928px maxWidth). Batch with any other re-render. |
| 4 | 16:9 | B02 | Killed mid-conform; left the raw 30s composition in the slot. | BLOCKER | FIXED — re-conformed to 10.41s with the pipeline's own ffmpeg step. |
| 5 | 16:9 | B03 | Killed between conform and move; correct clip was sitting in `_ext_B03.mp4`. | BLOCKER | FIXED — completed the move; verified 15.400s == beat. |

## Final dispositions (2026-08-31)

| # | Outcome |
|---|---|
| 1 | Accepted — the 9:16 bottom band is the documented platform-UI reserve. |
| 2 | Fixed and verified on the re-rendered B01/B03/B05/B06 in both aspects. |
| 3 | Superseded — the verdict widow disappeared when the portrait column was re-stacked to clear the header collision. |
| 4 | Fixed — B02 re-conformed to 10.41s. |
| 5 | Fixed — B03 completed from its `_ext_` temp file. |

Two further defects were found in the final pass and are recorded in
`REPORT-final.md`: the B03 portrait header collision (a real BLOCKER-class defect
the automated gate did not detect) and the `EtlSpark` title-safe breach.
