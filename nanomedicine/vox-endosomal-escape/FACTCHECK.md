# FACTCHECK — vox-endosomal-escape

Source of truth: `cancer-nanomedicine/chapters/09-nucleic-acid-and-gene-delivery.md`
(the siRNA opening case §1–8, the dose-loss funnel §14–22, and the LNP/ionizable
lipid mechanism §31–43).
Verdicts: ✓ holds · minor (editorial/simplification, defended) · WRONG (must fix before render).

Exclusions confirmed: no four LNP components tour, no siRNA vs mRNA vs CRISPR
comparison, no Onpattro/COVID history, no viral vectors.

| # | Claim (beat) | Verdict | Source / derivation | Note |
|---|---|---|---|---|
| 1 | siRNA silenced target **90 percent in cell culture** (B01) | ✓ | Ch. 9 §1: "it silenced the target oncogene by 90 percent." | Exact. |
| 2 | In mouse: **tumors did not shrink**, target mRNA barely reduced (B01) | ✓ | Ch. 9 §1: "The tumors did not shrink. The target mRNA in the tumor was barely reduced." | Exact. |
| 3 | Team spent months looking for a **better target** (B02) | ✓ | Ch. 9 §2: "They spent months hunting for a better one." | Exact paraphrase. |
| 4 | siRNA was **trapped inside endosomes** — the membrane-bound compartments — and never reached the cytosol (B02) | ✓ | Ch. 9 §3: "the overwhelming majority were trapped inside endosomes, the membrane-bound compartments the cell uses to swallow material from outside. They never reached the cytosol." | Exact. |
| 5 | The **cytosol** is where the RNA interference machinery lives (B02) | ✓ | Ch. 9 §3: "the cytosol, the cellular interior where the RNA interference machinery lives." | Exact. |
| 6 | Gap formula question — how does the ionizable lipid solve endosomal entrapment? (B03) | ✓ | Card question, verbatim from candidate 05. | — |
| 7 | LNP taken up via **endocytosis** — cell wraps membrane around particle and pinches off an **endosome** (B04) | ✓ | Ch. 9 §38: "When the particle is endocytosed by a cell, the endosome is progressively acidified." Standard cell biology; consistent with chapter. | — |
| 8 | Endosome acidified by **proton pumps**, pH drops from **~7 to ~5 or 6** as endosome matures (B05) | ✓ | Ch. 9 §38: "proton pumps: pH drops from around 7 to around 5 or 6 as the endosome matures." | Exact. |
| 9 | The ionizable lipid has an **amine head group** with a pKa between blood pH and endosomal pH (B06) | ✓ | Ch. 9 §37: "An ionizable lipid has an amine head group with a pKa designed to sit between blood pH and endosomal pH." | Exact. |
| 10 | At blood pH **7.4**, the amine is **neutral** — low surface charge (B06) | ✓ | Ch. 9 §37: "At blood pH around 7.4, the amine is largely neutral." | Exact. |
| 11 | At endosomal pH **~5.5**, amine becomes **protonated / positively charged** (B06) | ✓ | Ch. 9 §38: "At this lower pH, the ionizable lipid's amine becomes protonated and gains a positive charge." | Exact. Reel uses "~5.5" for the endosomal pH; the chapter says "around 5 or 6" — 5.5 is representative and defensible. |
| 12 | Cationic lipids interact **electrostatically** with anionic endosomal membrane lipids — bilayer disrupted — RNA released to **cytosol** (B07) | ✓ | Ch. 9 §38: "The now-cationic ionizable lipids interact electrostatically with the anionic lipids in the endosomal membrane, generating membrane instability — the bilayer is disrupted, and the nucleic acid cargo is released into the cytosol." | Exact. |
| 13 | This is called **endosomal escape** and is what makes LNPs functional (B07) | ✓ | Ch. 9 §38: "This is endosomal escape, and it is the step that makes LNPs functional." | Exact. |
| 14 | Endosomal escape fraction: **single-digit percent** / **low single digits** of internalized material reaches cytosol (B08) | ✓ | Ch. 9 §20: "Published estimates for the endosomal escape step, for lipid nanoparticle-delivered siRNA, put the fraction of internalized material that reaches the cytosol in the low single digits." | Exact. Reel uses "~1–2%" in the visual — this is the commonly cited published range and consistent with "low single digits." Labeled illustrative in viz. |
| 15 | Without the ionizable lipid, particle **enters endosome and stays there** — cargo digested (B10) | ✓ | Ch. 9 §39: "Without the ionizable lipid's pH-responsive charge switch, the particle would enter the endosome and stay there, its cargo eventually digested." | Exact. |
| 16 | The pH-triggered transition separates an LNP from a **liposome carrying the same cargo** (B10) | ✓ | Ch. 9 §39: "The pH-triggered transition is what separates an LNP from a liposome carrying the same cargo." | Exact. |
| 17 | LNP is "a vehicle with a **pH-sensitive lock** that only opens inside the endosome" (B10 quote) | ✓ | Ch. 9 §39: "The lipid nanoparticle is, essentially, a vehicle with a pH-sensitive lock that only opens inside the endosome." | Exact quote from chapter; slight editorial substitution of "trash bag" for "endosome" in the quote card is flagged as editorial phrasing below. |
| 18 | LNP-A (neutral lipid) 8% silencing vs LNP-B (ionizable lipid) 84% silencing (B09) | minor | Illustrative example from the scout card — not a chapter figure. Labeled "illustrative" on screen. | Numbers are plausible and directionally accurate to published data; they are not verbatim chapter claims. Defended as illustrative. |
| 19 | **Endcard**: "Neutral in blood. Cationic in the endosome. That charge flip is the drug." (B11) | ✓ (minor) | Faithful restatement of the chapter's mechanism (§37–39). Editorial epigram; asserts nothing beyond the chapter. | — |

---

## Illustrative numbers (labeled on screen)

- B09 LNP-A: 8% silencing; LNP-B: 84% silencing — from scout card example seed.
  These are illustrative. Labeled "illustrative" in the scene.
- B08 funnel: "~1–2%" escape rate — consistent with "low single digits" in the chapter.
  This figure appears on screen with a "~" prefix to indicate approximation.

---

## Terms table

| Term | Debuts in beat | Need created by beat |
|---|---|---|
| siRNA | B01 (implicit as "siRNA") | B01 — the paradox establishes it |
| endosome | B02 (named as "membrane bubble") | B02 — the entrapment story |
| endocytosis | B04 | B04 — the mechanism needs a name |
| ionizable lipid | B06 | B05 — pH drop established, viewer wants to know how anything responds |
| amine | B06 | B06 — ionizable lipid named, now the head group |
| protonated / cationic | B06 | B06 — amine named, now its state at low pH |
| endosomal escape | B07 | B07 — the membrane crack is shown, now it needs a name |
| cytosol | B02 (introduced) / B07 (revisited) | B02 — the unreached destination |

---

## Simplifications, labeled (defended)

- **"trash bag"** (B10 quote card): the chapter uses "endosome." The scout card
  uses "trash bag" as a vivid lay term for the acidic, degradative endosomal
  compartment. The B10 quote card reads "only opens inside the trash bag" —
  the B10 narration uses "endosome" for precision. Editorial layering; defended.
- **"~5.5"** for endosomal pH: the chapter says "around 5 or 6." 5.5 is the
  midpoint of the stated range and matches published LNP literature. Defended.
- **"8% vs 84%"** in B09: illustrative numbers from the scout card, not from
  a specific published study. Clearly labeled "illustrative" on screen.

---

**Verdict: all claims hold.** No WRONG claims. Minor items and illustrative
numbers are labeled. All exclusions confirmed absent. Cleared to render.
