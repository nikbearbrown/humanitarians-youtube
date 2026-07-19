# FACTCHECK — vox-bcl-selectivity
## Why the Same Drug That Kills Cancer Cells Kills Platelets (and How to Fix It)

Source chapter: cancer-biology/chapters/14-apoptosis-in-cancer-evasion-and-restoration.md
Cross-reference: Letai (2016), PMC5133681

---

## CLAIMS TABLE

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | "A drug designed to release the death program that cancer cells have suppressed works beautifully — and then nearly kills the patient by destroying their blood platelets." | ✓ | Ch.14 verbatim description of navitoclax case. |
| B02 | Navitoclax entered clinical trials for leukemia and showed activity, then platelet counts fell severely | ✓ | Ch.14: "Navitoclax (ABT-263), went into clinical trials in CLL and small-cell lung cancer and showed activity. Then came the problem … severe dose-limiting thrombocytopenia." |
| B03 | Navitoclax inhibits BCL-2 and BCL-XL | ✓ | Ch.14: "Navitoclax inhibits BCL-XL as well as BCL-2." |
| B03 | The question on screen: "Why do platelets die from the same drug?" | ✓ | Verbatim from card's The Question field. |
| B04 | BCL-2 is overexpressed in leukemia | ✓ | Ch.14: "BCL-2 itself, discovered at the t(14;18) translocation of follicular lymphoma … The lymphoma cells are not proliferating unusually fast — they simply refuse to die." CLL also BCL-2-dependent per venetoclax discussion. |
| B05 | BCL-2 family proteins sequester pro-apoptotic proteins to suppress the death program | ✓ | Ch.14: "A BH3 mimetic … occupies the hydrophobic groove of an anti-apoptotic BCL-2 family member, displacing the pro-apoptotic proteins that were bound there, and freeing BAX and BAK to oligomerize and permeabilize the outer mitochondrial membrane." |
| B06 | BCL-2, BCL-XL, MCL-1 are three anti-apoptotic guardians; different cells depend on different ones | ✓ | Ch.14: "BCL-XL and MCL-1 overexpression are common across many solid and hematologic cancers." Dependency concept elaborated throughout. |
| B07 | Navitoclax blocks both BCL-2 and BCL-XL simultaneously | ✓ | Ch.14: "Navitoclax inhibits BCL-XL as well as BCL-2." |
| B07 | CLL cells die from BCL-2 inhibition (therapeutic); platelets die from BCL-XL inhibition (toxicity) | ✓ | Ch.14: "platelets require BCL-XL for survival. Inhibiting BCL-XL triggered platelet apoptosis … dose-limiting thrombocytopenia." |
| B08 | "On-target toxicity — not a side effect, not an accident" | ✓ | Ch.14: "the platelet toxicity was not an off-target side effect. It was on-target toxicity in a normal cell that happened to share the dependency." |
| B09 | Therapeutic window is set by whether normal cells share the same guardian dependency | ✓ | Ch.14: "The therapeutic window was too narrow … before the molecule is designed, ask which normal tissues express the targeted guardian at survival-relevant levels." |
| B10 | Venetoclax binds BCL-2 with Ki below 0.1 nM; affinity for BCL-XL is more than 500-fold weaker | ✓ | Ch.14: "The drug binds BCL-2 with a Ki below 0.1 nM; its affinity for BCL-XL is more than 500-fold weaker." |
| B10 | Venetoclax was designed by structure-guided medicinal chemistry | ✓ | Ch.14: "Venetoclax (ABT-199) was designed by structure-guided medicinal chemistry to retain high-affinity BCL-2 binding while avoiding the BCL-XL pocket." |
| B10 | Platelets survive at therapeutic venetoclax doses | ✓ | Ch.14: "Platelets survive at therapeutic doses." |
| B11 | CLL is BCL-2-dependent | ✓ | Ch.14: "CLL cells are among the most BCL-2-dependent of any cancer type." |
| B11 | Platelets are BCL-XL-dependent | ✓ | Ch.14: "platelets require BCL-XL for survival." |
| B11 | Neutrophil (framing: "depends on neither at survival-critical levels") | minor | The chapter does not explicitly state neutrophil guardian dependency. The claim is framed as "neither at survival-critical levels — it has other guardians in reserve," which is defensible: neutrophils have short lifespans and different apoptosis regulation; they are not known to be BCL-2 or BCL-XL dependent in the same way. This is an illustrative framing consistent with the card's example seed. Labeled ILLUSTRATIVE. |
| B12 | Same dose across three cell types: CLL dies, platelet dies, neutrophil survives — illustrative | illustrative | Card's Example seed, explicitly labeled illustrative in narration ("This is illustrative."). |
| B13 | With venetoclax: CLL dies, platelet survives, neutrophil survives — illustrative | illustrative | Same source; explicitly labeled illustrative in narration ("Illustrative."). |
| B14 | Recap: window set by which normal cell shares cancer's guardian dependency | ✓ | Core idea from Ch.14: "The decisive variable was not potency against the tumor. It was identifying which normal cell shared the dependency and engineering around it." |

---

## TERMS TABLE

| Term | Debuts | Prior beat that creates the need |
|------|--------|----------------------------------|
| BCL-2 / BCL-XL | B03 (named in question) | B01-B02 establish the drug story; B03 names what it targets |
| guardian | B05 | B04 establishes the naive model of cancer-specific targeting; B05 names the guardian role |
| BH3 mimetic | NOT used in narration | Excluded by card — navitoclax and venetoclax named directly |
| on-target toxicity | B08 | B07 shows the mechanism; B08 names the concept |
| therapeutic window | B09 | B07-B08 show the problem; B09 names the principle |
| apoptotic priming | NOT used in narration | Excluded (BH3 profiling excluded by card) |
| navitoclax | B02 (in narration as "navitoclax") | B01-B02 establish the drug story |
| venetoclax | B10 | B09 establishes the principle; B10 introduces the structural fix |
| selectivity | B10 (500x selectivity) | B09-B10 set up the dependency-gap concept |
| BCL-2-dependent | B11 | B06 establishes that different cells depend on different guardians |
| BCL-XL-dependent | B11 | B06 establishes the fan-out concept |

---

## EXCLUSION CONFIRMATIONS

- **No full intrinsic pathway mechanics:** Cytochrome c, caspases, MOMP not mentioned in narration. B05 alludes to "holes in the mitochondria" only as plain language for MOMP — acceptable at this level of abstraction. CONFIRMED ABSENT.
- **No MCL-1 inhibitors or cardiotoxicity:** MCL-1 appears once in B06 narration as a third guardian name (muted in graphic), with no inhibitor discussion. No cardiotoxicity mention anywhere. CONFIRMED ABSENT.
- **No IAP antagonists or TRAIL agonists:** Absent throughout. CONFIRMED.
- **No BH3 profiling assay detail:** Absent. CONFIRMED.
- **No trial data tables:** Absent. CONFIRMED.

---

## ILLUSTRATIVE NUMBER AUDIT

- B12 narration: "Three completely different fates from one drug. This is illustrative." — labeled.
- B13 narration: "Illustrative." — labeled.
- No other numeric claims in narration or graphics.

---

VERDICT: PASS
