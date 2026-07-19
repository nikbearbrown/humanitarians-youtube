# FACTCHECK — vox-soc-mismatch

Source chapter: the-reallocation-engine/chapters/09-is-the-role-any-good-bls-onet-role-quality.md

---

## Terms table

| Term | Beat debut | Earlier beat that creates the need |
|---|---|---|
| SOC code / Standard Occupational Classification | B05 | B04 (title ambiguity → need a code beneath the title) |
| Alternate-title list | B06 | B05 (SOC is the pivot → need to confirm the mapping) |
| O*NET | B07 | B06 (alternate-title list introduced → need to name its source) |
| BLS OEWS / national median | B09 | B05 (SOC attaches wages → need to name where wages come from) |
| Confirmed / rejected match | B07 | B06 (alternate-title check shown → need confirm/reject vocabulary) |

---

## Claim-by-claim audit

### B01 — Title card narration
> "A candidate gets role quality data: stable field, well-paid, growing. The data is describing a different job."

Verdict: ✓ — Direct paraphrase of chapter Exercise 5 scenario: "The compact row shows stable national employment and a median wage of $68,230 — a solid, stable occupation. Verdict: acceptable role quality, proceed." That verdict was wrong because the SOC was wrong.

---

### B02 — STILL narration
> "A posting lands. Title: Growth Analyst. The system assigns a code. Numbers flow: median salary, employment trend, occupation profile. Everything looks real."

Verdict: ✓ — Chapter para: "A wrong SOC match is silent. It doesn't error out. It just quietly attaches the wrong wages, the wrong employment trend…"

---

### B03 — THE QUESTION
> "Mapping a title should attach the right wages. Here is the case where the mapping is wrong and the wages are wrong — and nothing in the output says so. Why?"

Verdict: ✓ — Chapter: "A wrong SOC match is silent. It doesn't error out."

---

### B04 — TitleAmbiguity
> "Job titles are marketing artifacts. One company's Growth Analyst builds dashboards. Another's deploys machine learning models on product data. Same title, opposite work."

Verdict: ✓ — Chapter para 2: "A title is a marketing artifact, written by whoever drafted the posting, calibrated to attract applicants rather than to describe the work."
The dashboard/ML split is illustrative — labeled as such.

---

### B05 — SOCIsPivot
> "The SOC code is the pivot. Get it right, and occupation wages and employment trends follow correctly. Get it wrong — silently — and the numbers are real but describe the wrong occupation."

Verdict: ✓ — Chapter: "The SOC code is the hinge. Get it right, and everything useful follows from it." / "A wrong SOC match is silent."

---

### B06 — TheMapping
> "A model proposes a plausible code. Growth Analyst looks like Market Research Analyst. The proposed SOC: 13-1161. Alternate-title list: Market Research Analyst, Consumer Insights Analyst, Survey Researcher. No modeling. No ML anywhere."

Verdict: ✓ — Chapter Exercise 5: "Mapped to SOC 13-1161 (Market Research Analysts)… alternate-title list on file: 'Market Research Analyst,' 'Market Researcher,' 'Consumer Insights Analyst,' 'Survey Researcher.' The posting describes building and deploying predictive models."
SOC 13-1161 is the BLS code for Market Research Analysts — verified against chapter text.

---

### B07 — TheCheck
> "The alternate-title list is the only check. If the posting's title or described work does not appear there, the match is unconfirmed — regardless of how plausible the proposed code seemed."

Verdict: ✓ — Chapter: "The verification step is mandatory: take the model's proposed SOC, look at the alternate-title list in the compact row, and check whether your posting's title or description actually appears there. If it does, the match is confirmed. If it doesn't, you re-classify before you trust any number downstream."

---

### B08 — RejectAndRetry
> "Rejected. Try 15-2051: Data Scientists. Alternate titles include Machine Learning Engineer, Predictive Analytics Engineer. The posting's work is there. Confirmed."

Verdict: ✓ — Chapter card content: "Try 15-2051 (Data Scientists): alternate-title list includes 'Machine Learning Engineer,' 'Predictive Analytics Engineer.' Confirmed."
SOC 15-2051 is the BLS code for Data Scientists — consistent with chapter.

---

### B09 — TheGap
> "National median: Market Research Analyst, sixty-eight thousand. Data Scientist, one hundred eight thousand. Forty thousand dollars."

Verdict: ✓ — Chapter card content: "national median Data Scientist $108K vs Market Research Analyst $68K." These are illustrative figures consistent with BLS OEWS order-of-magnitude. **ILLUSTRATIVE** — not a quoted BLS survey year; labeled national, lagging in the pedagogy.

---

### B10 — WalkThrough (THE EXAMPLE)
> Full walk-through of Growth Analyst case: 13-1161 rejected, 15-2051 confirmed, $68K vs $108K gap.

Verdict: ✓ — ILLUSTRATIVE (narration says so). All numbers match chapter card content exactly. The mechanism is real; the numbers are the chapter's own illustrative seed, not invented independently.

---

### B11 — Endcard
> "The numbers were real. They described the wrong occupation. The only check is the alternate-title list. If the work is not there, the match is unconfirmed."

Verdict: ✓ — Direct synthesis of chapter's core mechanism. No invented claims.

---

## Exclusion audit
- OEWS survey methodology: absent ✓
- Job zone detail: absent ✓
- BLS pipeline build instructions: absent ✓
- SOC taxonomy history: absent ✓
- BLS data collection mechanics: absent ✓
