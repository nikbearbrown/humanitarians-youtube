# Bio-Art Figure Audit — Molecule / Drug Category

**Scope:** All 49 figures in `index.json` tagged `category: "molecule"` or `category: "drug"` (the batch-figure entries, not the 11 hand-authored chapter illustrations). This is every drawn figure in the repo touching a molecular/pharmacological concept — a complete set, not a sample.

**Method:** For each figure, read the generation prompt from `annotations/*.json` ("Expected"), viewed the actual PNG in `figures/batch-NNN/` ("AI Result"), and judged it against the prompt. Categorized as **Useful / Partially useful / Not useful / Incorrect result**, per your document's rubric.

**Data caveat:** This repo has a single generative pipeline (Illustrae "rough" sketches) — there is no separate search-vs-generate distinction and no per-item AI report file. Every row below is an "AI Result" against its own text prompt (used as "Expected" and as the source-of-truth "manifest").

---

## Headline finding: template duplication, not just molecular detail loss

Before getting to small molecules specifically: **the dominant failure mode across this entire category is that the generator collapses dozens of distinct, detailed prompts into a handful of recycled generic templates.** Of the 49 figures:

| Template | Composition | # figures reusing it verbatim |
|---|---|---|
| **B** | wavy strand pair → X-in-circle → diamond/circled-X → X | **16** |
| **C** | 2 small circles → arrows into a big circle/oval-squiggle → small circle → "cloud" shape with 5 dots | **15** |
| **A** | concentric circle with a dot grid vs. a circle-in-circle with a few dots | 5 |
| **D** | wavy strand pair → circle → fork with one solid + one dashed arrow | 5 |
| **E** | X-circle → cluster-of-circles-in-circle → plain circle → larger circle, with a timeline arrow | 2 |
| Unique composition | — | 6 |

**31 of 49 figures (63%)** are one of five recycled templates, each reused across concepts that have nothing to do with each other. For example, Template B is the delivered image for: base excision repair, nucleotide excision repair, mismatch repair, double-strand break repair, p53–p21 activation, p53–MDM2 degradation, two separate "mutant p53" figures, a hand-drawn-napkin-style p53/MDM2 clamp figure, a napkin-style timeline, and four more p53-pathway figures — twelve distinct named mechanisms, one image. Template C does the same for base/nucleotide excision panels' apoptosis cousins, three different nucleosome/chromatin figures, SWI/SNF remodeling, DNA hierarchical structure, and four separate p53-apoptosis panel variants, plus a mitochondrion figure.

This means the "rough" pipeline is not really drawing the requested mechanism at all in most cases — it's selecting from a tiny shape library that ignores almost all of the (often very detailed, multi-step, explicitly labeled) prompt content, including requested style (e.g. two "hand-drawn napkin ballpoint" prompts came back in the same clean vector template as everything else).

## Small molecules specifically

**Zero of these 49 figures — and zero of all 245 figures in the repo — attempt an actual chemical/skeletal structure.** Confirmed by grep across `annotations/*.json` for "skeletal formula," "chemical structure," "molecular structure," "bond angle," "functional group": no matches. The `object-inventory.json` lists 56 named molecule/drug objects with real chemical identities (doxorubicin, olaparib, pembrolizumab, ATP, etc.), but none has been drawn as its actual structure — the "object" tag is used as a loose keyword match, not a request to render the molecule itself.

So your document's original conclusion holds, but for a reason one step removed from what actually happens here: this pipeline never gets far enough to draw a wrong bond, because it never attempts the structure at all. If it ever is asked to, the same template-collapse behavior seen everywhere else in this audit is exactly why an exact structural tool (RDKit, PubChem export, ChemDraw) should be used instead of the generative illustrator — a system that already can't reliably distinguish DNA mismatch repair from double-strand break repair has no chance of getting a bond graph right.

---

## Full table (all 49 figures)

| # | Figure ID | Expected (prompt summary) | AI Result | Useful? | Problem | Suggested Fix |
|---|---|---|---|---|---|---|
| 1 | in-situ-hybridization | 2-panel ISH technique for oncogene detection | Template A: concentric circle+dots vs. circle-in-circle+dots | Partially useful | Plausible probe/signal metaphor, but generic and unlabeled | Add labels |
| 2 | dna-packaging | 3-part DNA→chromatin packaging levels | Unique: coil→beads-on-string→supercoil twist | Partially useful | Correct topology/sequence, zero labels | Add labels; keep composition |
| 3 | dna-replication-fork | Y-shaped fork, leading/lagging strands, enzymes | Template D: wavy pair→circle→fork (solid/dashed arrows) | Partially useful | Plausible fork+directionality, no enzymes/labels | Add enzyme icons+labels |
| 4 | inrg-risk-stratification | Neuroblastoma risk-staging infographic | Unique: 4-tier bar pyramid + stray arrows/circles | **Incorrect result** | Tagged `object:"dna"` — wrong concept match; image unreadable without labels | Fix tagging; add labels |
| 5 | oncogenes-383428 | 3-part proto-oncogene→oncogene explainer | Template A (duplicate) | Not useful | Generic, no oncogene-specific content survived | Don't use generator for stepwise mechanism |
| 6 | replication-stress-356226 | 3-stage replication stress→DNA damage→instability | Template A-variant (duplicate) | Not useful | Same generic shapes as unrelated concepts | Same |
| 7 | oncogene-activation-385861 | 3-step oncogene activation→cancer cell | Template E: X→circle-cluster→circle→bigger circle, timeline | Not useful | No oncogene/gene content, purely generic growth metaphor | Same |
| 8 | proto-oncogenes-386660 | 2-panel normal vs. oncogene cell comparison | Template A (duplicate of #1, #5) | Not useful | Identical to unrelated ISH and oncogene figures | Same |
| 9 | kras-386687 | KRAS hub-and-spoke driver across cancers | Unique: hub-and-spoke circles/arrows | Partially useful | Plausible layout, but no KRAS/gene-specific content or labels | Add labels |
| 10 | glycolysis-452683 | 2-panel glycolysis pathway, labeled intermediates | Unique: hexagonal ring of circles+arrows+X | **Not useful** | No correspondence to glucose/pyruvate/any real intermediate | Generator unsuitable for biochemical pathways; use a diagram template tool |
| 11 | tp53-432934 | TP53 function vs. loss, 2 pathways | Template B (duplicate) | Not useful | Zero p53-specific content; identical to DNA-repair figures below | Don't reuse for distinct mechanisms |
| 12 | four-panel-dna-repair-432945 | 4 DNA repair pathways (BER/NER/MMR/DSB) | Template B (duplicate) | Not useful | Same image as individual BER/NER/MMR/DSB figures below | Same |
| 13 | cpg-445876 | CpG hypermethylation, normal vs. cancer | Template A (duplicate) | Not useful | Identical to unrelated oncogene/ISH figures | Same |
| 14 | base-excision-repair-445972 | 4-step BER mechanism | Template B (duplicate) | Not useful | Identical to NER, MMR, DSB, and 8 p53 figures | Same |
| 15 | nucleotide-excision-repair-445981 | 4-step NER mechanism | Template B (duplicate, pixel-identical to #14) | Not useful | Indistinguishable from BER | Same |
| 16 | apoptotic-465013 | Intrinsic apoptosis: BH3→Bax/Bak→MOMP | Template C (duplicate) | Not useful | No mitochondria/Bax/Bak content; generic cell+dots | Same |
| 17 | apoptotic-468442 | Intrinsic apoptosis, 3-stage textbook version | Template C (duplicate, pixel-identical to #16) | Not useful | Indistinguishable from #16 despite different prompt | Same |
| 18 | apoptotic-470271 | Intrinsic apoptosis, single-panel cell cross-section | Template C (duplicate) | Not useful | Same as #16/#17 | Same |
| 19 | draw-sequence-618794 | DNA ladder + downstream sequence | Template C (duplicate) | Not useful | Bears no resemblance to "DNA ladder" | Same |
| 20 | two-panels-nucleus-601030 | Nucleus, transcriptional regulator bound to DNA | Template C (duplicate) | Not useful | No nucleus/DNA-binding content | Same |
| 21 | mismatch-repair-445988 | 4-step MMR mechanism | Template B (duplicate) | Not useful | Identical to BER/NER/DSB | Same |
| 22 | double-strand-break-445993 | 3-part DSB repair mechanism | Template B (duplicate) | Not useful | Identical to BER/NER/MMR | Same |
| 23 | napkin-cell-533506 | **Hand-drawn napkin style**, cell+nucleus+3 labeled proteins | Template B-like generic shapes | **Incorrect result** | Requested art style (ballpoint/napkin) entirely ignored; no cell/protein content | Style + content both need fixing; consider a different pipeline for style-specific requests |
| 24 | napkin-p53mdm2-533511 | Napkin style, p53/MDM2 "clamp" metaphor | Template B (duplicate) | Not useful | Napkin style ignored again; identical to non-napkin figures | Same |
| 25 | napkin-p53-533513 | Napkin style, normal vs. bound p53 | Template B (duplicate) | Not useful | Same | Same |
| 26 | napkin-timeline-533514 | Napkin style, **timeline** of cell/DNA damage events | Template B (duplicate) | **Incorrect result** | Requested a timeline; got the same non-timeline 2-row diagram as everything else | Same |
| 27 | p53mdm2-535127 | p53 bound by MDM2 → degradation | Template B (duplicate) | Not useful | Identical to unrelated repair-pathway figures | Same |
| 28 | atmatr-540789 | DNA break → ATM/ATR → downstream | Template D (duplicate) | Partially useful | Fork/branch plausible for "two outcomes," no ATM/ATR labels | Add labels |
| 29 | atmatr-540793 | Same concept, alternate prompt wording | Template D (duplicate, near-identical to #28) | Not useful | Two differently-worded prompts → same image | Same |
| 30 | p53-p21-540808 | p53→p21→cell-cycle arrest | Template B (duplicate) | Not useful | No p21/cell-cycle-ring content despite explicit request | Same |
| 31 | p53mdm2-degradation-540884 | p53/MDM2 binding → degradation | Template B (duplicate) | Not useful | Identical to repair-pathway figures | Same |
| 32 | mutant-p53-541155 | Mutant p53, blocked p21 activation | Template B (duplicate) | Not useful | Same | Same |
| 33 | cell-division-541163 | Broken-DNA cell dividing into daughter cells | Template E (duplicate of #7) | Not useful | Identical to unrelated oncogene-activation figure | Same |
| 34 | mutant-p53-541171 | Mutant p53, structural disruption | Template B (duplicate) | Not useful | Same | Same |
| 35 | nucleosome-452818 | 2-panel nucleosome + histone tail modifications | Template C (duplicate) | Not useful | No DNA-wrap/histone-tail content | Same |
| 36 | dna-methyltransferase-452824 | 3-panel DNMTi mechanism | Template C (duplicate) | Not useful | Same | Same |
| 37 | swi-snf-551520 | SWI/SNF chromatin remodeling explainer | Template C (duplicate) | Not useful | Same | Same |
| 38 | hierarchical-dna-525806 | Multi-level DNA structure, cell→nucleotide | Template C (duplicate) | Not useful | Same | Same |
| 39 | nucleosome-525827 | Single-panel nucleosome, DNA wrap detail | Template C (duplicate) | Not useful | Same | Same |
| 40 | chromatin-remodeling-574608 | 3-panel chromatin remodeling in cancer | Template B (duplicate) | Not useful | Same as DNA-repair figures | Same |
| 41 | histone-octamer-549837 | DNA wrap around histone octamer, labeled tails | Unique: circle-cluster in oval | Partially useful | Octamer clustering roughly right; no DNA wrap/tails (the actual point) | Regenerate emphasizing wrap; add labels |
| 42 | four-callout-549846 | 2×2 grid, 4 epigenetic silencing mechanisms | Template C (duplicate) | Not useful | No grid, no 4 distinct mechanisms shown | Same |
| 43 | p53-apoptosis-616816 | p53-mediated apoptosis, single panel | Template D (duplicate) | Not useful | Same | Same |
| 44 | lipid-bilayer-634115 | Lipid bilayer + receptor cluster panel | Unique-ish (Template C family): wavy lines+dots / circle-cluster-in-oval | Partially useful | Reasonable bilayer/vesicle metaphor, but tagged `object:"dna"` | Fix tagging |
| 45 | dna-helix-715168 | Horizontal DNA helix across frame | Template D (duplicate) | Not useful | Same | Same |
| 46 | p53-apoptosis-662095 | p53 apoptosis, wild-type vs. loss (2-panel) | Template C (duplicate) | Not useful | Same | Same |
| 47 | p53-apoptosis-662103 | Same concept, alternate layout prompt | Template C (duplicate, identical to #46) | Not useful | Same | Same |
| 48 | p53-apoptosis-662106 | Same concept, solid-white-canvas variant | Template C (duplicate, identical to #46/#47) | Not useful | Three different layout prompts → one image | Same |
| 49 | mitochondrion-693715 | Mitochondrion outer-membrane event sequence | Template C (duplicate) | Not useful | No mitochondrion-specific content | Same |

---

## Tally

| Verdict | Count |
|---|---|
| Useful | 0 |
| Partially useful | 8 |
| Not useful | 38 |
| Incorrect result | 3 |

## Recommendations

1. **Fix the template-collapse bug first** — it's the single biggest driver of "Not useful" here (38/49). Before touching small molecules, figure out why ~16 distinct DNA-repair/p53-pathway prompts and ~15 distinct chromatin/apoptosis prompts are producing pixel-identical output. This looks like a pipeline defect (e.g. a prompt-truncation or template-fallback bug), not an inherent generative-illustrator limitation.
2. **Fix `object` tagging** for at least 2 confirmed mismatches (`inrg-risk-stratification`, `lipid-bilayer-634115` both tagged `"dna"` when unrelated).
3. **Small molecules**: continue to avoid the generative illustrator entirely for chemical structures. Use RDKit / PubChem structure export / ChemDraw. This is doubly justified now — not only would bonds be unreliable in principle, the pipeline as currently built can't even reliably distinguish coarse-grained mechanisms from each other.
4. **Style requests are not honored** — both "hand-drawn napkin ballpoint" prompts (#23, #24, #25, #26) came back in the same clean vector template as everything else. If style control matters, that's a separate defect worth flagging to whoever maintains the Illustrae pipeline.
