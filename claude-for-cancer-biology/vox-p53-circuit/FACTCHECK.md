# FACTCHECK — vox-p53-circuit
## Why Cancer Cannot Read Its Own Death Instructions

Source chapter: `cancer-biology/chapters/13-apoptosis-in-cancer-the-death-programs.md`

---

## Claims audit

| # | Claim | Beat | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | A cell absorbs 500 UV-induced thymine dimers | B01, B13, B14 | ✓ illustrative | Chapter 13: "the dose is 500 dimers" — verbatim from the chapter's second scenario | Labeled "illustrative" in narration (×2) |
| 2 | Thymine dimers are bulky distortions that block polymerases | B01 | ✓ | Chapter 13 intro: "fuses adjacent thymine bases into covalent dimers — bulky distortions that, if left in place, will be miscopied" | — |
| 3 | In healthy skin, a cell with heavy UV damage would be gone within the hour | B02 | ✓ | Chapter 13: "The cell dismantles itself in about an hour" (p53 WT / 500-dimer scenario) | — |
| 4 | Cell dismantles itself quietly, without leaking, without inflammation | B02 | ✓ | Chapter 13: "apoptosis…leaves no mess…the plasma membrane never ruptures…no inflammation" | — |
| 5 | Apoptosis exists to prevent passing corrupted instructions to daughters | B04 | ✓ | Chapter 13 intro and "Running the scenario twice" section | — |
| 6 | ATR and ATM detect thymine dimers and activate | B05 | ✓ | Chapter 13: "ATR and ATM activate, phosphorylate p53" | Card exclusions: no ATR/ATM biochemistry beyond naming |
| 7 | p53 normally degrades within minutes | B06 | ✓ | Standard cell biology: p53 half-life ~20-30 min under normal conditions; chapter 13 states p53 is "stabilized" by phosphorylation | Simplified to "minutes" — acceptable |
| 8 | ATR and ATM phosphorylate p53, stabilizing it | B06 | ✓ | Chapter 13: "ATR and ATM activate, phosphorylate p53, which stabilizes" | — |
| 9 | p53 is a transcription factor | B07 | ✓ | Chapter 13: "p53…acts as a transcription factor" | — |
| 10 | p53 transcribes PUMA and NOXA (BH3-only sensors) | B07 | ✓ | Chapter 13: "p53…turns on pro-apoptotic genes: PUMA and NOXA (encoding BH3-only sensors)" | — |
| 11 | p53 transcribes BAX (an effector) | B07 | ✓ | Chapter 13: "BAX (encoding an effector directly)" | — |
| 12 | PUMA and NOXA neutralize BCL-2 guardians | B07 | ✓ | Chapter 13: "PUMA and NOXA neutralize the BCL-2 guardians" | — |
| 13 | BAX oligomerizes and inserts into the outer mitochondrial membrane | B08 | ✓ | Chapter 13: "BAX oligomerizes, inserts into the outer mitochondrial membrane, MOMP occurs" | — |
| 14 | Cytochrome c assembles the apoptosome | B08 | ✓ | Chapter 13: "cytochrome c…drives its assembly into…the apoptosome" | — |
| 15 | Caspase-9 activates executioner caspases from the apoptosome | B08 | ✓ | Chapter 13: "apoptosome recruits and activates caspase-9, which activates the executioner caspases" | Caspase-9 not named in narration — correct, stays at mechanism level |
| 16 | p53 is the hinge between damage detected and death executed | B09, B15 | ✓ | Chapter 13: "p53 is the hinge. Remove it and damage accumulates without consequence" | — |
| 17 | Without p53, PUMA and NOXA are not transcribed, BAX is not induced | B10 | ✓ | Chapter 13: "no PUMA, no NOXA, no BAX induction" (p53-mutant scenario) | — |
| 18 | BCL-2 guardians hold if BH3-only proteins don't accumulate | B10 | ✓ | Chapter 13: "The BCL-2 balance…guardians predominate and the effectors are held in check" | — |
| 19 | TP53 is the most frequently mutated gene in human cancer | B11 | ✓ | Chapter 13: "TP53 is the most frequently mutated gene in human cancer" | — |
| 20 | TP53 is lost in roughly half of all cancers | B11 | ✓ | Chapter 13: "as it is in roughly half of all human cancers" | — |
| 21 | p53 WT: UV → p53 rises → PUMA/NOXA → BCL-2 tips → cytochrome c → caspases → cell gone in ~60 min | B13 | ✓ illustrative | Chapter 13 "Running the scenario twice" section: 500-dimer scenario traces exactly this sequence; timing "about an hour" from chapter | Labeled "illustrative" in narration for the 60-min figure and the 500-dimer count |
| 22 | p53 mutant: UV → p53 does not rise → PUMA/NOXA absent → BCL-2 holds → S phase with 500 dimers → two daughters | B14 | ✓ illustrative | Chapter 13 "Running the scenario twice" section; daughter-cell count (2) is the natural consequence of one division — accurate but labeled illustrative | Labeled "illustrative" in narration for 500-dimer figure; daughter count is plain arithmetic |
| 23 | The cell dismantles itself in about an hour (60 min figure) | B13 | ✓ illustrative | Chapter 13: "The cell dismantles itself in about an hour" | Labeled "illustrative" in narration |

---

## Illustrative numbers audit
All figures labeled "illustrative" in narration at point of use:
- 500 dimers: spoken as "five hundred UV-induced thymine dimers — illustrative" at B01, referenced again as "five hundred dimers — illustrative" at B13
- ~60 minutes: spoken as "roughly sixty minutes — illustrative" at B13
- Two daughter cells: natural arithmetic consequence of one division; labeled "illustrative" at B14

---

## Exclusion confirmation (card requirement)
All confirmed absent from narration, viz, card copy:
- [x] p53 arrest vs. senescence vs. apoptosis choice mechanism — absent
- [x] Extrinsic pathway (FAS, TRAIL, DR4, DR5, FADD, caspase-8) — absent
- [x] Necroptosis / ferroptosis / pyroptosis — absent
- [x] Venetoclax, navitoclax, BH3 mimetics — absent
- [x] p53 tetramer / dominant-negative detail — absent

---

## Terms table (vocabulary law audit)
Each technical term debuts at or after the beat that creates the need for it:

| Term | Debuts at | Created need at |
|---|---|---|
| thymine dimers | B01 (cold open: concrete damage) | B01 (debut in same beat — viewer sees the damage before the name) |
| apoptosis | B02 narration | B02 (the behavior — cell dismantles quietly — shown before the word) |
| ATR, ATM | B05 (sensors named when the mystery is "sensors fire but…") | B05 (break in the circuit creates need for sensor names) |
| p53 | B06 (hub named when the missing link is identified) | B05 (broken link beat creates the need for a name) |
| PUMA, NOXA, BAX | B07 (named when p53's action is shown) | B06 (p53 hub established; viewer now wants to know what it does) |
| BCL-2 (guardians) | B07 (named in context of what PUMA/NOXA neutralize) | B07 (debut in same beat — the balance is the point) |
| MOMP | B08 (via description, not isolated acronym) | B08 (BAX pores and cytochrome c release is described first) |
| apoptosome | B08 (named when cytochrome c assembles it) | B08 (cytochrome c behavior shown; need for assembly name follows) |
| caspases | B08 (named as the execution endpoint) | B08 (apoptosome recruits them — sequence is natural) |
| TP53 | B11 (gene notation used when prevalence is the point) | B10 (p53 loss established; B11 names the gene for the prevalence claim) |

No term debuts before its beat creates the need for it. Vocabulary law: PASS.

---

## VERDICT: PASS

All claims verified against chapter 13. Illustrative numbers labeled. Exclusions honored. Vocabulary law satisfied. No WRONG verdicts. Minor simplifications (p53 half-life described as "minutes"; BCL-2 family referred to as "guardians" without MCL-1/BCL-XL specifics) are appropriate for the reel's pedagogical level and exclusions.
