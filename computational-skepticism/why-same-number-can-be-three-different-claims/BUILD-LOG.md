# Build Log — Why the Same Number Can Be Three Different Claims

- **Reel Slug**: `why-same-number-can-be-three-different-claims`
- **Course**: *Computational Skepticism for AI* by Professor Nik Bear Brown
- **Source**: Chapter 11 (*Communicating Uncertainty: Calibrating Claims to Evidence*)
- **Candidate Card**: Candidate 22 (*Why the Same Number Can Be Three Different Claims*)
- **Score**: 8/10
- **Narrator**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Chassis**: `course-skepticism` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757` single accent, EB Garamond + UI sans)
- **Visual Object**: One sentence on screen whose verb slot climbs an 8-rung ladder (`hypothesize` → `suggest` → `observe` → `find` → `show` → `demonstrate` → `conclude` → `prove`) as evidence cards stack beneath it.
- **Manim Move**: `accumulate`

---

## 1. Candidate Spec & Binding Exclusions Audit

| Candidate Item | Spec Requirement | Implementation & Verification | Status |
|---|---|---|---|
| **Hook** | Model scores 87% once; 3 engineers write "observe", "find", "conclude"; only one tells truth | B00 hesitancy open and B01–B02 establish 87% score with 3 engineer claim verbs | **PASS** |
| **Core Idea** | Every claim-verb has an evidence price; frozen 8-rung ladder upgrades only as evidence stacks | B06–B07 introduce evidence pricing and 8-rung ladder structure | **PASS** |
| **Visual Object** | Sentence on screen whose verb slot climbs 8-rung ladder as evidence stacks | B03 plants sentence anchor; B08–B09 animate evidence stack paying for verb upgrades | **PASS** |
| **Manim Move** | `accumulate` kinetic progression | B08–B09 stack replication, subgroup tests, and stress tests beneath verb slot | **PASS** |
| **Prerequisites** | Held-out test set, rough idea of confidence interval | Plain setup accessible to anyone reading benchmark scorecards | **PASS** |
| **Exclusion 1** | No IPCC calibrated-language history | Zero IPCC history mentioned | **PASS** |
| **Exclusion 2** | No two-axis caution/strength digression | Excluded completely; focused solely on evidence-to-verb price | **PASS** |
| **Exclusion 3** | No calibration metrics (ECE/Brier) | Excluded completely | **PASS** |
| **Exclusion 4** | No peer-critique protocol | Excluded completely | **PASS** |
| **Exclusion 5** | Ladder strictly frozen: `hypothesize → suggest → observe → find → show → demonstrate → conclude → prove` | Ladder order strictly preserved across all beats and visuals | **PASS** |

---

## 2. Six-Move Pedagogical Audit (Plain Register)

1. **Move 1 — Stakes First (B00–B02)**:
   - Cold open with `BrutalistHesitantWriter` types naive draft (*"If three engineers see the exact same 87% benchmark score..."*), deletes and corrects to *"Why the Same Number Can Be Three Different Claims"*.
   - B01 presents the evaluation run: Model scores 87.4% on held-out test split.
   - B02 introduces the 3 engineers reporting the exact same 87% number with three verbs: "observe", "find", "conclude". Only Engineer A is telling the truth.
2. **Move 2 — Wrong Guess & Falsifying Case (B04–B05)**:
   - B04 articulates the Number Equivalence Reflex: *"Eighty-seven percent is eighty-seven percent. The number is the claim."*
   - B05 delivers the falsifying audit: The number is merely an output measurement; the verb dictates what epistemic commitment is being made. Engineer A paid the evidence price for a single run; Engineers B and C wrote checks their evaluation never cashed.
3. **Move 3 — Epistemic Mechanism (B06, B07, B10)**:
   - B06 defines the Evidentiary Price concept: verbs are not stylistic synonyms; each verb requires specific validation receipts.
   - B07 displays the frozen 8-rung ladder: `hypothesize → suggest → observe → find → show → demonstrate → conclude → prove`.
   - B10 (One Flag) delivers the critical boundary: You cannot buy higher verbs by adding more descriptive adjectives ("clearly", "robustly") or adjusting font sizes; only concrete validation receipts upgrade a claim.
4. **Move 4 — Anchor Planted & Paid Off (B03, B08, B09)**:
   - B03 plants the core visual sentence: `We [VERB] that the model achieves 87% accuracy.`
   - B08 applies the `accumulate` move: evidence blocks stack beneath the sentence (single run pays for *observe*; multi-seed replication pays for *find*; subgroup & shift testing pays for *show*).
   - B09 pays off the anchor: stress tests, confounder elimination, and adversarial validation accumulate to unlock *conclude*.
5. **Move 5 — Both Directions (B11–B12)**:
   - Direction A (B11): Over-claiming — spending *conclude* or *prove* on single-split evidence creates brittle epistemic debt that collapses in production.
   - Direction B (B12): Under-claiming — hedging down to *suggest* when rigorous multi-condition validation was performed obscures genuine empirical progress.
6. **Move 6 — Carry-Out Sentence (BCRY)**:
   - *"Every claim-verb has an evidence price — you can only spend the verb your validation actually paid for."*
   - Delivered in Remotion `WantQuote` serif typography with terracotta quotation marks.

---

## 3. Production Gates Verification

- **Audio Generation**: Kokoro `am_onyx` synthesized per-beat narration across 16 beats (195.1 s total duration).
- **Gate Audio**: PASS — `mean_volume: -23.9 dB`, `max_volume: -2.9 dB` (threshold: > −40 dB).
- **Gate T (Typography)**: PASS — line budgets, word ceilings, and bookend exemptions verified with `type_check.py` (0 FAILs).
- **Gate V (Visual QC)**: PASS — verified safe margins, contrast ratios, single terracotta accent per beat, crisp serif/sans typography, and kinetic `accumulate` evidence stacking animations.
- **Composition & Assembly**: `compile.py` generated `why-same-number-can-be-three-different-claims.mp4` (4K 3840×2160, 24fps) with all 16 slots filled (0 slates).
- **4K Master**: `why-same-number-can-be-three-different-claims-4k.mp4` verified at 3840×2160 resolution.

---

## 4. Delivery Status

- **Outbox**: `DELIVERY-course/why-same-number-can-be-three-different-claims/` staged with 4K master (`why-same-number-can-be-three-different-claims-4k.mp4`) and YouTube description (`why-same-number-can-be-three-different-claims-description.md`).
- **Repository**: `humanitarians-youtube/computational-skepticism/why-same-number-can-be-three-different-claims/` staged with text artifacts (`README.md`, `beat_sheet.json`, `SCRIPT.md`, `SUBJECT.json`, `BUILD-LOG.md`, `CARRY-OUT.md`, `QUESTION.md`, `TYPECHECK.md`).
- **YouTube Metadata**: `why-same-number-can-be-three-different-claims.md` targeted to Playlist: *Computational Skepticism — Communicating Uncertainty*.
