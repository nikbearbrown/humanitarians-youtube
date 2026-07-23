# FACTCHECK — vox-fluency-seam
*The Seam Where Fluency Sneaks Back In*
Source chapter: the-reallocation-engine/chapters/03-the-verified-data-contract.md

---

## Claims inventory

| Beat | Claim | Verdict | Source / Fix |
|------|-------|---------|-------------|
| B01 | "Fifteen filings, 85% approval rate — sourced to government records" | illustrative | Chapter ch03 uses "fifteen LCAs" and "85% H-1B approval rate" as a worked example (Exercise 5). Labeled illustrative. |
| B01 | "The number came back real" (verified script produces real numbers) | PASS | Core premise of ch03's verified-data contract — verified throughout chapter |
| B02 | Model output: "strong sponsorship signal" | PASS | Direct from ch03 Exercise 5 pre-generated artifact paragraph |
| B02 | Model output: "very likely to sponsor your visa" | PASS | Direct from ch03 Exercise 5 |
| B02 | Model output: "probably expanding" | PASS | Direct from ch03 Exercise 5 |
| B02 | Model output: "great culture fit" | PASS | Direct from ch03 Exercise 5 |
| B04 | Department of Labor publishes LCA data | PASS | ch03 p.2: "The Department of Labor publishes every Labor Condition Application a U.S. employer files before hiring a foreign worker." |
| B04 | USCIS publishes H-1B approval/denial counts | PASS | ch03 p.2: "The USCIS publishes H-1B approval and denial counts by employer." |
| B04 | A language model "produces the most coherent sentence it can" (not counting) | PASS | ch03 p.1: "the most coherent-sounding sentence the model could assemble from patterns in its training data — which is a completely different operation from looking at a record." |
| B06 | One-question test: "Could this sentence have been produced by counting records?" | PASS | ch03, section "The seam where fluency sneaks back in": "For any sentence in a system output, one question settles it: could this sentence have been produced by counting records?" |
| B06 | YES branch: must trace to script output or audit | PASS | ch03: "If yes, it must trace to a script output or an audit report." |
| B06 | NO branch: model judgment, allowed but must be labeled | PASS | ch03: "If no — if it is a reading, a framing, a suggestion — it is model judgment, and it is allowed, but it must be visible as such." |
| B07 | "Verification stops at the data layer" | PASS | ch03, section heading and content: verified-data contract operates at the data layer |
| B07 | "At the reading layer, a language model interprets and completes" | PASS | ch03: "You run the script... Now you hand that number to a language model and ask it to interpret the finding. The model says: 'fifteen filings over three years is strong for a company of this size in this sector.' Did the model count anything? No. It estimated." |
| B08 | "Acme Bio filed 15 LCAs" (B08 color-coded example) | illustrative | Exercise 5 pre-generated artifact. Illustrative. |
| B08 | "85% approval rate (source: DOL/USCIS)" | illustrative | Exercise 5. Illustrative. |
| B08 | "strong signal for a company of this size" = model judgment | PASS | ch03 Exercise 5 validation: "which sentences are counted facts and which are estimates?" |
| B08 | "very likely to sponsor" = unsourced present-tense claim | PASS | ch03 Exercise 5 |
| B08 | "great culture fit" = fabricated | PASS | ch03 Exercise 5: "a culture-fit and expansion claim nothing measured" |
| B08 | "One sentence passes the test. Four do not." | PASS | ch03 Exercise 5 validation checklist: two data claims traceable to DOL/USCIS; three judgments unlabeled |
| B09 | "The seam where a true number launches an unsourced judgment is invisible" | PASS | ch03: "The seam where interpretation re-enters is invisible: a true number launches an unsourced judgment, and nothing in the output marks the transition." |

## Illustrative numbers (labeled)
- "15 LCAs" / "85% H-1B approval rate" / "Acme Bio" — all from ch03 Exercise 5 pre-generated artifact. Not real company data. Labeled illustrative throughout.

## Exclusion confirmations
- Full verified-data pipeline architecture (three-pipeline detail): does NOT appear in any beat narration or visual
- Caching mechanism: does NOT appear
- Only the seam at the reading layer: CONFIRMED

## Terms table

| Term | Debut beat | Prior beat that creates need |
|------|-----------|------------------------------|
| verified script | B01 | — (establishing premise) |
| data layer | B04 | B01 (running the script) |
| reading layer | B04 | B04 (data layer contrasted) |
| model judgment | B05 | B04 (model estimates vs counts) |
| one-question test | B06 | B05 (the invisible seam established) |
| data claim | B06 | B05 (seam introduced, need a name for each side) |
| authority borrowing | B07 | B06 (one-question test defined, now: why it matters) |

All terms debut AFTER the beat that creates the need for them. PASS.

## Verdict
All claims: PASS or illustrative-labeled. No invented counts. Exclusions honored.
