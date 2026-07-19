# FACTCHECK — vox-context-priority-weight

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Six unlabeled documents → output reflects longest/most formal | ✓ | Chapter 2: "Claude may weight documents in ways you did not intend — often by structural prominence rather than recency or reliability." |
| B02 | Keiko: 15-page brand guide, 6-page competitor analysis, 1-page brief with "nothing blue" constraint | ✓ | Card key case verbatim |
| B03 | Output follows brand guide, predominantly blue — constraint in brief ignored | ✓ | Card key case verbatim |
| B04 | Without labels, Claude treats all documents as single undifferentiated block | ✓ | Chapter 2: "When multiple documents are pasted together without labels or hierarchy, Claude cannot determine which source is authoritative or current." |
| B05 | Claude weights by length, formality, structural completeness | ✓ | Chapter 2: "It will weight documents in ways you did not intend — often by structural prominence rather than recency or reliability." |
| B06 | Brief gets proportional weight (~1/15 of brand guide) | illustrative | Proportional weight claim is a reasonable inference. The chapter says length matters but doesn't give a 1/15 number. Labeled illustrative. |
| B07 | More unlabeled documents = more dilution | ✓ | Chapter 2: "Irrelevant context does not just fail to help — it can actively distort output." |
| B08 | Fix: label + prune. Three categories: primary, background, override | ✓ | Chapter 2: "Label each source before it appears. Tell Claude what each source is, how authoritative it is, and how to treat it." |
| B09 | Labeled brief = hard constraint honored | ✓ | Chapter 2: the whole point of Practice 1 (label your sources) |
| B10 | Policy doc vs email override: label "email overrides policy on timeline" | ✓ | Chapter 2: "The final email in this thread corrects the figures in Section 4 of the report. Treat the email as authoritative for those figures." |
| B11 | School admin scenario: handbook, memo, 2-sentence override email | illustrative | Invented. Plausible application. Labeled illustrative. |
| B12 | Two labels reverse priority order | illustrative | Illustrative extension. |
| B13 | Three label categories: primary, background, override | ✓ | Chapter 2 Practice 1 + exclusions practice (adapted) |
| B14 | Unlabeled context creates false priority orders; labels assign weight | ✓ | Chapter 2 thesis |

## Terms table
| Term | Debuts | Prior need |
|------|--------|-----------|
| unlabeled context | B04 | B01–B03: saw the false-weighting problem |
| priority order | B06 | B04–B05: length/formality weighting established |
| label / source label | B08 | B06–B07: problem fully stated; ready for solution |

## Exclusions
- No RAG: CONFIRMED absent
- No token limits: CONFIRMED absent
- No chunking: CONFIRMED absent
- No context-window utilization literature: CONFIRMED absent
