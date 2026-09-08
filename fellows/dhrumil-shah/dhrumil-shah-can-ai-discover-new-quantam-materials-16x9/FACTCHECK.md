# FACTCHECK — Can AI Discover New Quantum Materials?

Checker: Claude Code, operating under the PROOF protocol
Date: 2026-09-01
Method: every factual, numerical, and historical claim in `beat_sheet.json`
was extracted and checked against the strongest available primary source.
Nothing was silently repaired; every issue is listed for human review.

Verdicts: **SUPPORTED** · **QUALIFY** (true but needs the stated caveat) ·
**VERIFY** (believed correct; the exact figure must be checked against the
primary paper before public release) · **UNSUPPORTED** · **NOT USED**.

---

## Claim-by-claim

| # | Beat | Claim | Verdict | Evidence / required action |
|---|---|---|---|---|
| 1 | B01 | Superconductivity is a quantum effect; below Tc electrons bind into pairs and resistance is exactly zero | SUPPORTED | BCS 1957. "Exactly zero" is correct for DC resistance in the superconducting state. |
| 2 | B01 | The problem dates from 1911 | SUPPORTED | Kamerlingh Onnes, mercury, ~4.2 K, Leiden 1911. |
| 3 | B01 (chart) | Tc values plotted for Hg, Pb, NbN, Nb₃Sn, Nb₃Ge, LaBaCuO, YBCO, BSCCO, HgBaCaCuO, MgB₂, LaFeAsO, H₃S, LaH₁₀ | SUPPORTED / VERIFY | Cuprate, MgB₂, pnictide and hydride values are HIGH confidence (see SOURCES #7–14). NbN 1941, Nb₃Sn 1954 and BSCCO 1988 are marked VERIFY in SOURCES — they are conventional textbook values but the exact first-report figures should be confirmed. They are unlabelled points on the chart, so an error would not be legible to a viewer. |
| 4 | B01 (chart) | H₃S and LaH₁₀ are shown in accent and their **pressures are stated on screen** | SUPPORTED | 155 GPa and ~170 GPa respectively. Displaying the pressure is required: without it the chart would imply an ambient-pressure record that does not exist. |
| 5 | B02 | CLAIM is the presenter's review framework | SUPPORTED (by construction) | Labelled `PRESENTER FRAMEWORK · CLAIM` on screen in Scenes 02, 09 and 10. It is not attributed to any dataset, model, or paper. |
| 6 | B03 | 21,263 superconductors in the standard public table | SUPPORTED | Hamidieh 2018 / UCI "Superconductivty Data". |
| 7 | B03 | 81 features, one measured Tc target | SUPPORTED | Same source. The UCI set ships 81 predictors plus `critical_temp`. |
| 8 | B03 | Underlying measurements are from NIMS SuperCon | SUPPORTED | Hamidieh 2018 states the SuperCon provenance. |
| 9 | B04 | Features are composition-derived only — no crystal structure, phonon spectrum, band structure, or synthesis route | SUPPORTED | Hamidieh 2018 §2. This is the film's key technical point and it is correct. |
| 10 | B05 | **±9.5 K out-of-sample RMSE, gradient-boosted trees, held-out split** | **VERIFY** | Reported in Hamidieh 2018 §4. This is the single largest number on screen (190 px). **Action: confirm the exact figure and the split definition against the published table before making the film public.** If it differs, the value is a one-line edit in `src/CanAIDiscoverQuantumMaterials.tsx` (`MethodScene`). |
| 11 | B06 | "It learned to interpolate a table of things we already found" | QUALIFY | This is presenter interpretation, not a quoted finding. It is a fair characterisation of a supervised regression objective, and the source tag frames it as interpretation. |
| 12 | B07 | The screening funnel: score → rank → stability filter → synthesizability filter → shortlist | QUALIFY | This is a faithful description of the standard high-throughput screening pattern, but the specific proportions shown are **illustrative**. Labelled `ILLUSTRATIVE SCREENING SCHEMATIC` in the source tag and again in an accent card at B08. |
| 13 | B08 | "No discovery campaign was run for this film, and no new superconductor is claimed" | SUPPORTED | True statement of what this project did. Required by the brief and stated on screen. |
| 14 | B08b | The cuprates (1986) and iron pnictides (2008) arrived from outside the then-known distribution | SUPPORTED (fact) / QUALIFY (framing) | Both discoveries are correctly dated and attributed. The "outside the distribution" framing is the presenter's analogy between historical surprise and statistical extrapolation; the source tag says so. |
| 15 | B08b | A model trained on known chemistry is structurally weakest at out-of-distribution candidates | QUALIFY | A standard, uncontroversial property of supervised learning. Stated as interpretation, not as a cited result. |
| 16 | B09 | Confirmation chain: stability estimate → synthesis → four-probe R = 0 → Meissner | SUPPORTED | Standard experimental practice. Meissner & Ochsenfeld 1933 for field expulsion. |
| 17 | B09/B10 | Zero resistance alone is insufficient; field expulsion is also required | SUPPORTED | This is the correct and important distinction, and it is what the LK-99 case turns on. |
| 18 | B10 | One of five stages is computational; four are laboratory work | SUPPORTED (by the film's own chain) | Describes the chain the film just showed. Not a claim about the wider field. |
| 19 | B11 | July 2023 preprint claimed LK-99, a copper-doped lead apatite, superconducted at room temperature and ambient pressure | SUPPORTED | arXiv:2307.12008 and arXiv:2307.12037. |
| 20 | B12 | Independent groups failed to reproduce it | SUPPORTED | Broad replication record, Aug–Sep 2023. |
| 21 | B12 | The resistivity drop was attributed to a Cu₂S impurity phase transition | SUPPORTED | Replication analyses, August 2023. |
| 22 | B12 | Levitation was attributed to ferromagnetic impurity, not flux pinning | SUPPORTED | Replication analyses, August 2023. |
| 23 | B12 | No Meissner effect was confirmed | SUPPORTED | Replication record. This is the decisive point and it is correctly stated. |
| 24 | B12b | LK-99 scored on CLAIM: C present, L n/a, A unknown, I failed, M failed | SUPPORTED (by construction) | This is the presenter's framework applied to the record above. Each row's justification is on screen. |
| 25 | B12b | "I and M are exactly the two axes no model can supply" | QUALIFY | True as stated — independent replication and physical measurement are not model outputs. Presenter conclusion, framed as such. |
| 26 | B13 | "It can shrink a search space before anyone enters a laboratory" | QUALIFY | A deliberately bounded claim. The film does not quantify the acceleration, because no verifiable figure was available (see below). |

---

## Open action before public release

**One item.** Claim #10 — the ±9.5 K RMSE — is marked VERIFY. It is displayed
larger than anything else in the film. Confirm it against Hamidieh 2018 §4.

Everything else is either SUPPORTED, or QUALIFY with the qualification visible
on screen.

---

## Claims supplied in the brief but NOT used

Two 2026 results were supplied in the project brief without citations:

| Supplied claim | Status | Prepared slot |
|---|---|---|
| ORNL (June 2026): autonomous thin-film discovery loop combining LLM hypothesis generation, automated synthesis and AI analysis; reported 10–100× acceleration | **NOT USED — UNVERIFIED** | Scene 05, after the funnel. Needs: lab, paper title, venue, date, DOI, and the exact system the acceleration was measured on. |
| 2026 peer-reviewed system screening >1.3 million candidate structures, with experimental confirmation of superconductivity in two previously unreported compounds | **NOT USED — UNVERIFIED** | Scene 05, as the funnel's real-world instance. Needs: paper, venue, DOI, the two compound formulas, their measured Tc, and the pressure. |

Neither claim could be verified at build time and no source was supplied for
either. Under the film's own standard — no source, no verdict — an unverifiable
claim does not go on screen, however plausible it is.

This is not a rejection of the results. Both would materially strengthen
Scene 05, which currently carries an illustrative schematic where it could
carry a real campaign. **If you supply the two papers, adding them is a
contained edit to `FunnelScene` plus two rows in `SOURCES.md`.**

---

## What the film deliberately does not claim

- It does not claim a new superconductor.
- It does not claim to have run a screening campaign.
- It does not claim a specific acceleration factor for AI-assisted search.
- It does not show a predicted-Tc plot for any candidate, because no such run
  was performed. The funnel is a labelled schematic, not a result.
- It does not present the CLAIM framework as anything other than the
  presenter's own review structure.
