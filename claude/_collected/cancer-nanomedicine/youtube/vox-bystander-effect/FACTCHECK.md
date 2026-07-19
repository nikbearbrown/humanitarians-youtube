# FACTCHECK — vox-bystander-effect

Source: cancer-nanomedicine/chapters/05-antibody-drug-conjugates-as-nanoscale-medicines.md

---

## Terms Table

| Term | Debut beat | Preceding beat that created need |
|------|-----------|----------------------------------|
| HER2-low | B01 | — (first concrete instance, establishes context) |
| T-DM1 | B02 | B01 established that two drugs exist with the same antibody |
| T-DXd | B02 | B01 established the same |
| antibody | B03 | B01–B02 used the concept, B03 names the gap formula |
| HER2-positive / HER2-negative | B04 | B03 asks why same antibody differs; B04 explains the target distribution |
| membrane-permeable / membrane-impermeable | B06–B08 | B04–B05 established antibody limitation; B06 introduces the linker payload distinction as the answer |
| non-cleavable linker | B06 | B05 established that the naive view (antibody = whole story) is wrong |
| cleavable linker | B08 | B06 named non-cleavable; B08 introduces the contrast |
| bystander effect | B08 | B06–B07 showed confined killing; B08 names the opposite phenomenon |

---

## Claim-by-Claim Verification

| Beat | Claim | Source line | PASS/FAIL |
|------|-------|------------|-----------|
| B01 | "HER2-low" is a distinct breast cancer category | Ch5 p.3: "HER2-low breast cancer" used as treatable category | PASS |
| B01 | Both drugs carry the exact same HER2-targeting antibody | Ch5 p.3: "The antibodies are identical." | PASS |
| B02 | T-DM1 and T-DXd both carry the trastuzumab antibody | Ch5 p.3: "T-DXd is also built on the trastuzumab antibody" | PASS |
| B02 | One opens a new disease category (T-DXd in HER2-low) | Ch5 p.3: "T-DXd, not T-DM1, opened HER2-low breast cancer as a treatable disease category" | PASS |
| B04 | Antibody controls exactly one step: which cell gets bound | Ch5 p.1: "This is the only step the antibody controls — which cell gets bound. Everything after binding depends on the other two components." | PASS |
| B04 | In HER2-low, only a few cells carry the antigen | Ch5 p.3: "In tumors that are HER2-low — expressing HER2 at low, heterogeneous levels — many cancer cells would never bind or internalize the ADC" | PASS |
| B05 | Naive expectation: both drugs should underperform equally in HER2-low | Ch5 p.4: "The first instinct is that both should underperform equally in a HER2-low tumor — antigen is scarce, so little ADC binds, so little drug is delivered." | PASS |
| B06 | T-DM1 uses a non-cleavable linker | Ch5 p.3: "Trastuzumab emtansine (T-DM1) is an anti-HER2 ADC with a non-cleavable linker" | PASS |
| B06 | T-DM1 freed payload carries a charged fragment and cannot cross membranes | Ch5 p.3: "The freed payload bears a charged linker fragment and cannot cross membranes [verify]" and Ch5 p.2: "The released drug-linker fragment is typically charged and hydrophilic, which means it cannot cross cell membranes." | PASS |
| B07 | T-DM1 kills only the cell it directly enters; HER2-negative cells survive | Ch5 p.3: "T-DM1 kills cells it directly enters." and "T-DM1 leaves them untouched." | PASS |
| B08 | T-DXd uses a cleavable linker with membrane-permeable payload | Ch5 p.3: "Trastuzumab deruxtecan (T-DXd) is also built on the trastuzumab antibody but carries a topoisomerase-I-inhibitor payload at high DAR (~8) on a cleavable linker, and the freed payload is membrane-permeable [verify]" | PASS |
| B08 | T-DXd payload diffuses across membrane into neighbors | Ch5 p.3: "When T-DXd binds one of the few HER2-expressing cells in a HER2-low tumor, the released drug diffuses into neighbors — HER2-negative, HER2-low, and HER2-positive alike." | PASS |
| B09 | "The antibody finds the cell. Everything else decides whether the drug kills it." | Ch5 final line: "The antibody finds the cell. Everything else decides whether the drug kills it." | PASS |
| B10 | 5 HER2-positive entry points → 5 kills for T-DM1 | Illustrative number — see B10 EXAMPLE section below | LABELED ILLUSTRATIVE |
| B10 | 5 entry points → ~40 kills for T-DXd | Illustrative number — see B10 EXAMPLE section below | LABELED ILLUSTRATIVE |
| B10 | "Same antibody. Eight times more kills." | Illustrative ratio derived from 5 vs ~40 (8x) — labeled illustrative | LABELED ILLUSTRATIVE |
| B11 | T-DXd, not T-DM1, treats HER2-low breast cancer | Ch5 p.4: "T-DXd is the correct choice for HER2-low disease" | PASS |
| B11 | Difference is payload membrane permeability | Ch5 p.4: "the decisive variable is the linker-payload combination enabling the bystander effect" | PASS |

---

## B10 EXAMPLE Section

All numbers in B10 are **illustrative** — invented for pedagogical clarity, not drawn from clinical trial data.

- "5 HER2-positive entry points" — illustrative
- "5 cells killed" (T-DM1) — illustrative, consistent with mechanism (T-DM1 kills only cells it directly enters)
- "~40 cells killed" (T-DXd) — illustrative, consistent with mechanism (bystander spread from 5 entry points)
- "Eight times more kills" — illustrative ratio (40/5 = 8x)
- "HER2-low tumor, 100 cells modeled" — illustrative scenario label

The illustrative nature is confirmed in the card's Example seed: "All numbers illustrative."  
These numbers appear nowhere in the source chapter. The mechanism they illustrate — bystander spread from HER2-positive entry points to HER2-negative neighbors — is sourced directly from Ch5 p.3.

---

## Exclusions Audit

| Excluded element | Appears in reel? |
|-----------------|-----------------|
| DAR (drug-to-antibody ratio) | NO |
| Five-step dose-loss funnel | NO |
| Linker cleavable/non-cleavable chemistry details (acid, cathepsins, glutathione) | NO |
| Pneumonitis toxicity | NO |
| Opening-case DAR-8 failure | NO |

All exclusions honored.

---

VERDICT: PASS
