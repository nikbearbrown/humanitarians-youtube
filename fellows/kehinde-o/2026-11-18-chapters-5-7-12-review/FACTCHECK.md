# FACTCHECK — Fact-Checking Chapters 5, 7 and 12

Source of record: the Chapter 5, 7 and 12 Evidence Documents, REVIEWED workbooks and TextEdit
guides, and merged textbook PR #50. Counts computed from the workbooks.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | Ch5: 12 claims in scope, 10 revise, 2 approved | B02 | TRUE | Workbook (21 rows resolve to 12 IDs); Evidence Doc table |
| 2 | Ch5: 15 edits in 5 of 7 files | B02 | TRUE | Ch5 Evidence Doc table |
| 3 | Ch7: 32 claims, 25 revise, 5 approved, 2 pending | B02 | TRUE | Workbook and every per-claim section (see correction below) |
| 4 | Ch7: 24 edits in 7 of 9 files | B02 | TRUE | Ch7 Evidence Doc table |
| 5 | Ch12: 33 claims, 24 revise, 9 approved | B02 | TRUE | Workbook; Ch12 Evidence Doc "Where it landed" |
| 6 | Ch12: 19 edits in 5 of 8 files | B02 | TRUE | Ch12 Evidence Doc |
| 7 | Pre-check cited a paper "of 224 glioblastoma patients" that never mentions glioblastoma | B03 | TRUE | Ch5 ID 102, PMC9325965 (14,956 solid tumours) |
| 8 | Pre-check cited E2112's design paper, published before the result | B03 | TRUE | Ch7, PMID 29354686 (2018) vs result PMID 34357781 (2021) |
| 9 | Pre-check cited a two-case conference abstract for ovarian failure figures | B03 | TRUE | Ch12 IDs 310-311, PMC7715379 |
| 10 | RAS frequency stated as one in four, about 30% twice, about a third | B04 | TRUE | Ch5 sections 5.2, 5.4, 5.5, Figure 5.4.1 caption |
| 11 | Measured across databases: about 19 percent | B04 | TRUE | Prior et al. 2020, PMID 32209560 |
| 12 | Pre-check caught three; the caption was found on the sweep | B04 | TRUE | Ch5 Evidence Doc |
| 13 | Nine claimed approved; tucidinostat never FDA approved | B05 | TRUE | Ch7 Evidence Doc |
| 14 | Panobinostat withdrawn (Mar 2022); tazemetostat withdrawn (Mar 2026) | B05 | TRUE | Ch7 Evidence Doc |
| 15 | EPZ-6438 is tazemetostat's development code | B05 | TRUE | Ch7 Evidence Doc |
| 16 | Three approved IDH inhibitors missing | B05 | TRUE | Ch7: ivosidenib, enasidenib, vorasidenib |
| 17 | Meta-analysis credited with significant OS benefit, HR 0.84 | B06 | TRUE | Ch12 section 12.7.3 |
| 18 | Paper found no significant OS benefit: HR 0.89, P = 0.08; 0.84 is a PFS figure | B06 | TRUE | Chen et al. 2014 per Ch12 Evidence Doc |
| 19 | Ch12: seven of 19 edits from sweeping beyond the flags, including the two worst | B07 | TRUE | Ch12 Evidence Doc |
| 20 | Four flags did not hold up; three cleared by reading the chapter's source | B07 | TRUE | Ch12 Evidence Doc "Four flags I cleared" |
| 21 | All three chapters' corrections are merged | B08 | TRUE | PR #50 merged 13 Nov 2026 |

## Correction made to the review record (18 Nov 2026)
The Chapter 7 Evidence Document's summary table said 26 revise and 4 approved. The
workbook and every per-claim section say 25 and 5. The table was corrected in the .md and
.docx; originals kept in `Chapter 7/.backup-2026-11-18/`.

## Deliberately not claimed
- No clinical advice; not that any drug is ineffective.
- The three chapters are never summed.

## First-person claims added in the script revision (18 Nov 2026)

The narration was rewritten to describe what I did. Each new claim about my own work traces to the record:

| Claim | Source |
|---|---|
| I reviewed all three chapters on the same day | Evidence documents and first commits all dated 9 Nov 2026 |
| I confirmed the tazemetostat withdrawal separately because it was so recent | Ch7 Evidence Doc: 'I verified it independently' |
| Three wrong flags fell apart once I read the book the chapter was copied from | Ch12 Evidence Doc: three cleared by reading the source |
