# FACTCHECK — vox-name-match-gap

**Source chapter:** the-reallocation-engine/chapters/07-who-sponsors-the-80-days-sponsorship-scorer.md

---

## Claims Table

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | The engine assigns "Unknown" tier to companies with no matched sponsorship history | ✓ | Ch7: "Unknown means the record is silent." |
| B02 | A company can have sponsorship filings yet score Unknown | ✓ | Ch7: "A failed name match is a data problem you fix by resolving the entity and re-running." |
| B03 | THE QUESTION: engine should distinguish "doesn't sponsor" from "can't find" | ✓ | Ch7: "Those two causes of Unknown require opposite responses." |
| B04 | Unknown has two causes: true absence of filings, or name-match failure | ✓ | Ch7: "A company is Unknown for one of two reasons: either there is genuinely no filing history…or the name did not match." |
| B05 | Filings can exist but "never joined" due to name mismatch | ✓ | Ch7: table row: "The history may exist under a different legal name." |
| B06 | DOL has LCA filings; USCIS has H-1B approvals; joined on company name | ✓ | Ch7: "The record lives in three datasets…The second is the DOL LCA disclosure data…The third is the USCIS H-1B Employer Data Hub…joined by the 80 Days pipeline on resolved company names." |
| B07 | "BioTechCo LLC" vs "BIOTECHCO LLC" — join normalizes case but not punctuation | ✓ | Ch7 (key case on card): "The join script normalizes case but not punctuation. Two rows fall into a separate bucket and never match." |
| B07 | Three name variants used: BioTechCo LLC, BIOTECHCO LLC, BioTechCo Inc. | ILLUSTRATIVE | The card shows "BioTechCo LLC" and "BIOTECHCO LLC"; "BioTechCo Inc." added as third variant for visual clarity. Labeled illustrative. |
| B08 | Fragmented buckets look thin individually; consolidated they represent one legal filer | ✓ | Ch7 visual object description: "Three employer-name buckets…each with a small count, enclosed by a dotted boundary labeled 'same legal filer,' with an arrow to the consolidated true count." |
| B09 | Coverage number = fraction of shortlist that matched across both datasets | ✓ | Ch7: "The output is a number: how many companies on your shortlist matched, how many failed to match." |
| B09 | 64% matched → ~36% did not match | ILLUSTRATIVE | From card example seed: "Join coverage: 64% of shortlist matched. That means ~36% of Unknowns could be artifacts." Labeled illustrative. |
| B10 | Two causes, opposite fixes: direct signals (true absence) vs resolve entity (artifact) | ✓ | Ch7: "Those two causes of Unknown require opposite responses. A true absence…is a prompt to look for direct sponsorship signals…A failed name match is a data problem you fix by resolving the entity and re-running." |
| B10 | Coverage audit is what tells the two causes apart | ✓ | Ch7: "You tell by reading the join-coverage audit." |
| B11 | NovaGen: Series B, 3 years old, 60 employees, scores Unknown | ILLUSTRATIVE | From card example seed. Labeled illustrative. |
| B11 | Coverage audit: 64% matched, so ~36% of Unknowns may be artifacts | ILLUSTRATIVE | Same source. Labeled illustrative. |
| B12 | DOL records "NovaGen Bio LLC"; USCIS records "NOVAGEN BIO" | ILLUSTRATIVE | From card example seed. Labeled illustrative. |
| B12 | Strip punctuation and normalize case → match → 8 filings surface → tier jumps to Likely | ILLUSTRATIVE | From card example seed. Labeled illustrative. |
| B13 | RECAP: Unknown has two causes; coverage audit tells which; fix join or find signal | ✓ | Ch7 throughout. |

---

## Terms Table

| Term | Beat it debuts | Earlier beat that creates the need |
|------|----------------|-----------------------------------|
| Unknown tier | B01 | — (established cold open) |
| Sponsorship history / LCA filings | B02 | B01 (engine references missing history) |
| Name-match gap | B03 (THE QUESTION) | B01–B02 set up the contradiction |
| True absence (of filings) | B04 | B03 (question names two possible causes) |
| Name-match failure / artifact | B05 | B04 (first cause named, second follows) |
| Data join (joining on company name) | B06 | B05 (filings "never joined" — viewer wants to know how) |
| Fragmentation / buckets | B07 | B06 (join on name → separate buckets when name differs) |
| Coverage number | B09 | B08 (consolidated vs fragmented count raises the diagnostic question) |
| Coverage audit | B10 | B09 (coverage number introduced, audit is how you read it) |
| Entity resolution / resolve the entity | B10 | B09–B10 (fix named after problem established) |
| Likely tier | B12 | B04 (tier spectrum introduced; Likely named when NovaGen flips) |

---

## Exclusion Audit

- Levenshtein / fuzzy matching algorithms: ABSENT from all narration and visuals ✓
- Full entity-resolution system design: ABSENT ✓
- Legal definition of "legal entity": ABSENT ✓
- Bayes / base-rate material: ABSENT ✓
- Verb taxonomy (Ch5 topic): ABSENT ✓

---

## Illustrative Numbers Summary

All numbers labeled illustrative in this file and in the beat sheet note:
- 64% join coverage / 36% unmatched
- NovaGen: Series B, 3 years old, 60 employees
- "NovaGen Bio LLC" (DOL) vs "NOVAGEN BIO" (USCIS) — 8 filings surfaced
- Three name-bucket counts (illustrative visual)

These are drawn verbatim from the card's example seed, which is labeled "illustrative" in the source scout card.
