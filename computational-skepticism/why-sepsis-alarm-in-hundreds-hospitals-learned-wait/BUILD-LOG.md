# BUILD-LOG — Why a sepsis alarm in hundreds of hospitals learned to wait for the doctor

## Metadata
- **Candidate**: Candidate 24 — Why a sepsis alarm in hundreds of hospitals learned to wait for the doctor
- **Source**: `computational-skepticism-for-ai/chapters/12-the-three-categorical-limits.md`
- **Slug**: `why-sepsis-alarm-in-hundreds-hospitals-learned-wait`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the epistemic mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (12 scenes: clinical timeline, forecaster assumption, feature table, suspicion loop, data boundary, directional comparisons) + Remotion (4 scenes: BrutalistHesitantWriter cold open, WantQuote carry-out, ClaudeComposerAsk prompt, OutroCTA)
- **Visual Object**: The Suspicion Loop (`clinician suspicion → blood-culture order → model feature → alert → back to clinician`)
- **Manim Move**: `trace` (tracing the clinician order timestamp directly into the model risk jump)

## Six-Move Audit
1. **Cold Open**: B00 (`BrutalistHesitantWriter` typing animation questioning if high validation accuracy guarantees predicting sepsis before doctors notice, correcting to firing after doctors already suspect).
2. **Stakes First**: B01, B02 (Proprietary bedside sepsis early-warning AI deployed across hundreds of hospitals nationwide; Wong et al. 2021 external validation showing the model missed most sepsis cases and flooded wards with false alerts).
3. **Anchor Planted**: B03 (Clinical care timeline: observation → suspicion → diagnostic test order).
4. **Wrong Guess & Falsification**: B04, B05 (The intuitive assumption of an independent forecaster detecting raw physiology before humans; falsified by examining the model's feature set containing workflow orders alongside vital signs).
5. **Epistemic Mechanism**: B06, B07 (Clinician workflow at the bedside: deterioration triggers clinical suspicion, leading to a blood-culture order. Kinetic move `trace`: the timestamp of the doctor's test order traces directly to the spike in model alert risk).
6. **Anchor Payoff**: B08, B09 (The Suspicion Loop: circular signal where the model alert is downstream of the doctor's action. Internal metrics scored success because the model fired and the patient had sepsis, ignoring who acted first).
7. **One Flag**: B10 (The Data-World Boundary: the training data frame contains the order feature, but not the clinician's diagnostic intent. No algorithm can see beyond its own data frame to recognize its premise is circular).
8. **Both Directions**: B11 (Direction A: Predictive accuracy does not equal forecasting lead time), B12 (Direction B: The mathematics worked flawlessly as optimized; the failure was epistemic).
9. **Carry-Out**: BCRY (`WantQuote` card: *"An early-warning model cannot warn you about an event if its strongest feature is the trace of you already reacting to it."*)
10. **Your Turn**: BHTF (`ClaudeComposerAsk`: Audit production early-warning systems to check whether top predictive features are reflections of human response rather than independent precursors).
11. **Outro**: BOUT (`OutroCTA`: Title restatement + @HumanitariansAI skin).

## Exclusions Audit
- **No AUC / sensitivity deep-dive**: Verified — cited Wong et al. (2021) once in B02 and moved on.
- **No alert-fatigue subplot**: Verified — focused purely on the circular signal epistemic mechanism.
- **No EHR plumbing or HL7 integration mechanics**: Verified — kept focus on the epistemic boundary.
- **No vendor accountability or legal culpability thread**: Verified — framed as an epistemic limit of data frames, not malicious design.
- **No recap of the three categorical limits framework**: Verified — focused exclusively on Candidate 24.

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats checked against type specifications via `type_check.py` (0 FAILs).
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); all durations measured and synchronized in `beat_sheet.json` (176.3s total runtime).
- **Manim Render**: 12 custom scenes rendered at 24fps (B01–B12) implementing clinical timelines, feature comparisons, suspicion loop mechanics, and data-world boundaries.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to native 4K (`3840×2160`), 24 fps, 0 slates (16/16 filled). Total runtime 176.21s.
- **Gate Audio**: PASS — `mean_volume: -23.9 dB`, `max_volume: -3.0 dB` (audible threshold > -40 dB verified via `volumedetect`).
- **Gate V**: PASS — Visual inspection verified palette (`#FAF9F5`, `#3D3929`, `#D97757`), safe margins, legible typography, and valid contrast.
- **Delivery**: Ready for packaging and delivery via `deliver.py --push`.
