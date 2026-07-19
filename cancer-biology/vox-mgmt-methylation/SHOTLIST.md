# SHOTLIST — vox-mgmt-methylation
*Why Silencing a Repair Gene Is Better for the Patient Than Expressing It*

---

## Top-half: audit histogram, rhythm, act map, color law, exclusion confirmation

### Shot histogram

| Beat | Type | Source | Motion |
|------|------|--------|--------|
| B01 | GRAPHIC | own | fade |
| B02 | STILL | ai | kenburns |
| B03 | GRAPHIC | own | drawon |
| B04 | CARD | own | hold |
| B05 | GRAPHIC | own | drawon |
| B06 | GRAPHIC | own | drawon |
| B07 | GRAPHIC | own | drawon |
| B08 | GRAPHIC | own | drawon |
| B09 | GRAPHIC | own | drawon |
| B10 | GRAPHIC | own | drawon |
| B11 | GRAPHIC | own | drawon |
| B12 | CARD | own | hold |

**Rhythm check:** No more than 2 consecutive same-type beats. B03-B06 are four consecutive GRAPHICs — acceptable because B04 is a CARD break. B07-B11 are five consecutive GRAPHICs — acceptable in THE MECHANISM/EXAMPLE acts where sustained visual explanatory motion is expected. B02 (STILL ai) provides early rhythm break.

### Act map

| Act | Beats | Duration est. |
|-----|-------|--------------|
| COLD OPEN | B01, B02, B03 | ~34s |
| THE QUESTION | B04 | ~12s |
| THE PROBLEM | B05, B06 | ~25s |
| THE MECHANISM | B07, B08, B09 | ~44s |
| THE IMPLICATION | B10 | ~14s |
| THE EXAMPLE | B11 | ~22s |
| RECAP | B12 | ~14s |
| **TOTAL** | 12 beats | **~165s (~2:45)** |

Within 2–3 min band. Hard cap 5:00 clear.

### Color law
- **TEAL (#1F6F5C)** = MGMT methylated / repair silenced / drug works / good patient outcome
- **CRIMSON (#BF3339)** = MGMT expressed / damage repaired / drug neutralized / bad outcome
- **GOLD (#F5D061)** = fill highlight only, once per graphic, editor's pen — never text
- **SLATE (#3E5559)** = structural scaffolding, entity cards
- Two data accents only. Never swap mid-film.

### Exclusion confirmations
- No full DNA methylation mechanism (no DNMT1, no maintenance methylation): CONFIRMED absent
- No histone code content: CONFIRMED absent
- No IDH mutation connection: CONFIRMED absent
- No azacitidine/decitabine mechanism: CONFIRMED absent
- No other epigenetic biomarkers: CONFIRMED absent

---

## Bottom-half: per-slot fill-in sections

### B02 — STILL · ai slot

**Beat B02 — Two Patients (COLD OPEN)**

Public-archive search:
- Wikimedia Commons: glioblastoma MRI scans (public domain medical images)
- https://commons.wikimedia.org/wiki/Category:Glioblastoma
- Note: medical charts are synthetic — no real patient data

**Paste-ready generative prompt:**

```
B02, two paper medical charts pinned side-by-side on aged newsprint, editorial collage, flat print reproduction, desaturated warm tones — both charts show the same header "Glioblastoma Multiforme, Grade IV" and same treatment protocol "Temozolomide + Radiation," charts labeled "Patient A" and "Patient B" in stamped black ink, slightly worn paper texture, no faces or identifying information, overhead flat lighting, no shadows, no digital effects, cream and charcoal palette
```

---

## Per-beat production notes (own-manim beats)

### B01 — Title graphic (COLD OPEN)
Title card: "Why Silencing a Repair Gene" / "Is Better for the Patient" — CRIMSON line on bottom text, TEAL eyebrow "CANCER BIOLOGY", GOLD underline. Fade in. ~11s.

### B03 — SameTreatment (COLD OPEN)
Show temozolomide action: guanine base with methyl group attaching at O6 position. Simple geometric representation — a G-base rectangle, then a methyl group dot with arrow landing at it. CRIMSON for the lesion mark. ~12s.

### B04 — TheQuestion CARD (THE QUESTION)
Question card: "DNA repair should protect a cell." / "A tumor that fixes its DNA efficiently should survive better." / "Here it doesn't — why?" Gap formula on screen. SLATE background card, INK text. ~12s.

### B05 — NaiveExpectation (THE PROBLEM)
Split panel: left = "DNA damage" (CRIMSON arrow hitting a cell), right = "Repair fixes it" (TEAL arrow removing damage), center label "cell survives." Naive intuition diagram. ~12s.

### B06 — WhyItFlips (THE PROBLEM)
Same split panel flips context: drug's intent arrow points toward tumor cell (TEAL = good for patient). MGMT repair arrow labeled "drug neutralized" (CRIMSON = bad for patient). The inversion made explicit. ~13s.

### B07 — DecisionTree (THE MECHANISM)
Two-branch decision tree — root: "MGMT Promoter Status." Left branch TEAL: "Methylated" → "No MGMT protein" → "Lesions accumulate" → "Tumor cells die" (TEAL terminal). Right branch CRIMSON: "Unmethylated" → "MGMT expressed" → "Damage repaired" → "Drug wasted" (CRIMSON terminal). Branches draw on sequentially. ~17s.

### B08 — SuicideMechanism (THE MECHANISM)
Show MGMT suicide: an MGMT protein icon, an O6-methylguanine lesion on DNA. Arrow shows methyl transfer from DNA to MGMT cysteine. Then MGMT icon crosses out (self-destructs). One repair per molecule. ~13s.

### B09 — MethylSilences (THE MECHANISM)
MGMT promoter region — CpG sites as dots, methylated dots shown as filled CRIMSON circles. Transcription machinery (RNA pol icon) blocked. Label: "MGMT gene silenced." TEAL = methylated promoter = good outcome. ~14s.

### B10 — Biomarker (THE IMPLICATION)
Two chips: TEAL chip "PREDICTIVE BIOMARKER" vs SLATE chip "PROGNOSTIC BIOMARKER." Serif labels distinguish: predictive = differential benefit from specific drug; prognostic = outcome regardless of treatment. ~14s.

### B11 — ExampleTrace (THE EXAMPLE)
Side-by-side trace, Patient A (TEAL) vs Patient B (CRIMSON). Each shows: lesion forms → repair step (absent in A, active in B) → cell fate. Numbers: "~2 minutes" for MGMT repair in Patient B (labeled illustrative). Sequential animation following one O6-methylguanine lesion in each patient. ~22s.

### B12 — Endcard CARD (RECAP)
Endcard: "CANCER BIOLOGY" eyebrow, serif quote: "Repair protects the wrong side." / "Silenced MGMT = the drug works." GOLD underline. ~14s.
