# PEDAGOGY — hai-vox-photoelectric-effect
Variant: HAI (Pragmatist register)
Date: 2026-07-16

## Pedagogical sequence audit

### Act structure

| Act | Beats | Job |
|-----|-------|-----|
| INTRO | B00 | What it is, what it produces — lead with method |
| Setup | B01–B02 | Historical context, title card |
| Failures | B03–B06 | Three measurable failures of wave model |
| Diagnosis | B07 | Why wave model fails — root cause |
| Method | B08–B11 | Photon hypothesis, mechanism, equation resolution |
| Confirmation | B12–B14 | Millikan validation, Nobels |
| Limits | B15 | When to use / when NOT to use |
| CLI Exercise | B_CLI | Runnable BUILD simulation (second-to-last) |
| Outro | B_OUTRO | Humanitarians AI CTA (last) |

### Pragmatist register compliance

- [x] Opens with method: "what it is, what it produces" — no hook, no narrative warmup
- [x] States when to use it (B15): threshold calculations, UV sensors, classical EM limits
- [x] States when NOT to use it (B15): coherent light, multiphoton effects, nonlinear regimes — the AI main event is not skipped or softened
- [x] Equation variables fully defined with units (T02)
- [x] No personality tax, no academic hedging
- [x] Irreducibly-Human tangent: not inserted — photoelectric effect does not create a clear AI-vs-human decision boundary for social-impact practitioners
- [x] CLI exercise present as B_CLI (second-to-last)
- [x] Outro is last (B_OUTRO)

### Voice compliance

- [x] All voiced beats: af_kore (Kokoro)
- [x] B00 cold-open uses voice af_kore
- [x] B_CLI uses af_kore
- [x] B_OUTRO uses af_kore

### CLI exercise compliance (B_CLI)

- Lane: BUILD (quantitative, computable simulation)
- ASK: paste-ready `claude "..."` command for frequency sweep
- OUTPUT: two-metal table with clear threshold marking
- CHANGE: add third metal (gold)
- OUTPUT 2: extended table showing gold requires deep UV
- NEXT STEP: "Run it with your own metal — look up its work function on NIST"
- Genuinely runnable: the Python simulation is straightforward and produces real output

### Narration compliance — human-provided beats

For beats with human-provided media (B01, B03, B04, B06, B08, B12, B15):

| Beat | Source narration | Variant narration | Change type |
|------|-----------------|-------------------|-------------|
| B01 | "In 1887, Heinrich Hertz proved light is a wave — the crowning triumph of classical physics. The same year, he noticed something that would destroy it." | "In 1887, Heinrich Hertz confirmed light is a wave — the dominant model of classical physics. That same year, he observed an anomaly that would eventually require abandoning it." | Register — "proved" → "confirmed", "noticed something that would destroy it" → "observed an anomaly that would eventually require abandoning it"; same facts, same referents |
| B03 | "By 1902, Philipp Lenard had shown the sparks were electrons. By 1914, Robert Millikan had measured every feature of them. The data said three impossible things." | "By 1902, Philipp Lenard had identified the ejected particles as electrons. By 1914, Robert Millikan had precisely measured all three anomalous behaviors. The data was unambiguous." | Register — "sparks" → "ejected particles", "impossible things" → "anomalous behaviors"; same facts, dates, people |
| B04 | "One: below a threshold frequency, nothing. A blinding red arc lamp frees no electrons from sodium. A dim ultraviolet lamp frees them instantly." | "Failure one: threshold frequency. Below a material-specific cutoff, no electrons are ejected — regardless of light intensity. A blinding red lamp: nothing. A dim UV lamp: immediate ejection." | Register prefix change; same referents (red lamp/UV lamp/sodium); slightly restructured for Pragmatist clarity |
| B06 | "Three: no delay. Emission begins within nanoseconds, at any brightness above threshold. Even the dimmest lamp never needs time to charge up an electron." | "Failure three: instantaneous emission. Electrons are ejected within nanoseconds at any intensity above threshold. The wave model requires time to accumulate enough energy. That delay is never observed." | Register prefix + clarifying diagnostic sentence; same numerical claim (nanoseconds); same threshold reference |
| B08 | "Enter a twenty-six-year-old patent clerk in Bern, in his miracle year: Albert Einstein, taking the step Planck himself refused." | "In 1905, Albert Einstein proposed the solution. Working as a patent clerk in Bern, he applied Planck's energy quantization — which Planck had limited to emission — to light itself." | Pragmatist restructuring (state method first); same person, same place, same year, same fact about Planck |
| B12 | "Robert Millikan thought photons were absurd. He spent two years trying to prove Einstein wrong — freshly scraped metal surfaces, vacuum, exquisite care." | "Millikan attempted to disprove Einstein's photon hypothesis — two years of precise measurements on freshly prepared metal surfaces in vacuum." | Condensed; preserves "two years", same method details |
| B15 | "Who was this patent clerk? A story of its own. What he did to light — wave AND particle at once — has no classical answer." | "When to use this model: threshold calculations for photoemission, UV sensor design, understanding classical EM limits. When NOT to: coherent light sources, multiphoton ionization, near-threshold nonlinear regimes..." | Full replacement for B15 in HAI: the source beat's bio-kicker narration is replaced with the Pragmatist's use/don't-use diagnosis. The supplied video (Einstein portrait) remains unchanged; the narration is now the "when not to use" beat, which is the HAI main event. This is a generated-visual-equivalent editorial decision: the beat's job in HAI is the limits diagnostic, not the bio kicker. |

Note on B15: the human-provided video (AI-generated Einstein portrait) is preserved unchanged. The narration change is substantial because B15 in the HAI register serves a different pedagogical job (use/don't-use) than in the source (bio kicker). The media is ambiguous — it works equally well under either narration. Per the instructions, this is treated as a generated-visual editorial decision for the HAI brand's required diagnostic beat.

### Ending order

```
B00 (intro) → B01–B02 (setup) → B03–B06 (failures) → B07 (diagnosis) →
B08–B10 (photon hypothesis) → T01–T03 (equation) → B11 (resolved) →
B12–B14 (Millikan/Nobel) → B15 (use/don't-use) → B_CLI (exercise) → B_OUTRO (outro)
```

Confirmed: CLI exercise is second-to-last. Outro is last.

## VERDICT: PASS
