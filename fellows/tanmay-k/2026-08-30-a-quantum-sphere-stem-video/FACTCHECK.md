# FACTCHECK — *Four, Then Two, Never One*

Every factual, numerical, and attributional claim the script makes, with its verdict and
evidence. Per the source README's fact-check protocol: nothing is silently repaired, and
gaps are marked `[VERIFY: …]` rather than filled by guessing.

Primary evidence is [`experiment/RESULTS.md`](experiment/RESULTS.md), reproducible with
`python3 experiment/hard_sphere.py --all` on a stock python3.

| ID | Beat | Claim | Verdict | Evidence |
|---|---|---|---|---|
| C1 | B01 | Classically, a hard sphere of radius a has σ = πa², at every energy | **SUPPORTED** | Definitional — geometric shadow area. Standard result. |
| C2 | B05 | Low-energy quantum limit is σ → 4πa², i.e. 4× classical | **SUPPORTED** | Computed: 3.999999987 at ka = 10⁻⁴ (R1). Standard textbook result (s-wave, δ₀ = −ka). |
| C3 | B06 | High-energy limit is σ → 2πa², i.e. 2× classical | **SUPPORTED** | Computed: 2.0125 at ka = 2000, still falling (R1). Known as the *extinction paradox*. |
| C4 | B08 | The quantum answer never equals the classical one at any energy | **SUPPORTED (scoped)** | Minimum 2.1988 on 0 < ka ≤ 30, attained at the ka = 30 endpoint since the curve is monotone decreasing; scanned at Δka = 0.02; all sampled ka up to 10⁴ exceed 2 (R1, R4). Scope stated on screen: verified numerically, not proved for all ka. |
| C5 | B03B | The number of partial waves that matter is ≈ ka | **SUPPORTED** | ka = 100 → 102 waves; ka = 2000 → 2002, for 99.9% of the sum (R2). Semiclassical impact-parameter argument. |
| C6 | B09 | The approach to 2 goes as (ka)^(−2/3) | **SUPPORTED, numerically** | Local exponent climbs 0.6307 → 0.6659 monotonically over three decades toward 2/3 = 0.6667 (R3). Stated on screen as *measured*, not derived. |
| C6b | B09 | The exponent is 2/3, and nothing else nearby | **SUPPORTED, numerically — analytic derivation still `[VERIFY]`** | Falsification test (R3a): assuming p = 2/3, the coefficient C(ka) flattens to 0.996 (drift 1.016 over ka = 100 → 30 000); assuming 0.65 it falls (0.924) and 0.70 it rises (1.229), bracketing the true value. Only 2/3 holds still. **This rules out the neighbours; it does not derive 2/3.** The canonical reference for the analytic expansion is Nussenzveig, *Ann. Phys.* **34** (1965) 23–95, which we identified but could not access — so no coefficient is quoted from it. Script says "consistent with two thirds, and nothing else nearby… measured, not proved", which is now exactly what the evidence supports. |
| C7 | B09B | At ka = 100 the true value is 2.091, still 4.5% above the limit; 1% needs ka ≈ 1000 | **SUPPORTED** | Computed (R3). |
| C8 | B10 | A hard sphere shows no resonances; an attractive well does | **SUPPORTED** | 0 turning points for the sphere vs 10 peaks for a well at 2mV₀a²/ħ² = 900, same code, same grid (R4). |
| C9 | B10 | The reason is that an impenetrable sphere has no interior to hold a quasi-bound state | **SUPPORTED as interpretation** | The control (C8) is consistent with it and could have falsified it. Labelled on screen as the *explanation the control tests*, not as an independent measurement. |
| C10 | B04 | The source video's simulation is numerically correct: σ/πa² = 2.328 at ka = 13.6, l_max = 16 | **SUPPORTED** | Independent recomputation: 2.328297 (Δ = 2.97 × 10⁻⁴); 16 waves capture 99.99% (R5). |
| C11 | B04 | The source frame's label "σ/a²" should read "σ/πa²" | **SUPPORTED** | 2.328 is the ratio to πa². Arithmetic, visible in frame `qc-sheet.png` cell B06. |
| C12 | B11 | The standard shortcut for computing these waves falls apart past l ≈ ka — wrong by thirteen orders of magnitude, with no error raised | **SUPPORTED** | Measured on our own code: j_l by upward vs downward recurrence at ka = 13.6 gives relative error 3.3 × 10¹³ by l = 40, failing upward toward a large value where the truth is ~10⁻¹⁶ (R6). |
| C12b | — | The source video's simulation used an unstable recurrence | **NOT CLAIMED** | Its HTML is not in the repo and cannot be audited. The script says only that its *output* was checked and is right (C10). C12 is a hazard of the method, demonstrated on our own code, and B11 states it as such. |
| C13 | B11 | Thermal neutron/nucleus ka ≈ 1.8 × 10⁻⁴; red light off a 10 µm-radius droplet ka ≈ 99 | **SUPPORTED as illustrative** | λ = 1.8 Å, a = 5 fm → 1.75 × 10⁻⁴; λ = 633 nm, a = 10 µm → 99.3. Order-of-magnitude framework examples, **labelled "illustrative" on screen**; the video computes neither cross section. Moved from B03B to B11, where the viewer works them out before the answers are revealed. |
| C14 | B07 | The mechanism for the factor 2 is that forming a sharp shadow requires diffraction, which is itself scattering, contributing a further πa² | **SUPPORTED, attributed** | Standard resolution of the extinction paradox, due to van de Hulst (diffraction + geometrical optics); the quantitative link is the optical theorem, σ_tot = (4π/k)·Im f(0). Named on screen. |
| C15 | — | The source video attributes the high-energy limit to "Babinet's principle" | **QUALIFY** | Loose. Babinet's principle concerns complementary diffracting screens and *motivates* the diffraction half of van de Hulst's argument, but the result is standardly called the extinction paradox and follows from the optical theorem. **This version does not repeat the attribution**; it names the extinction paradox and the optical theorem instead. |
| C16 | B01, B03 | "Hard sphere" means an impenetrable potential, V = ∞ for r < a, so ψ(a) = 0 | **SUPPORTED** | Definitional; it is what makes tan δ_l = j_l(ka)/n_l(ka) exact rather than approximate. |

## Claims deliberately NOT made

- Nothing about *why* the source video's narration omitted the result. `SOURCE-ANALYSIS.md`
  records what the artifact does and does not contain; motive is not evidence.
- No claim that AI-generated physics code is unreliable. The one generated artifact examined
  here was correct (C10). R6 is a hazard of the *method*, demonstrated on our own code.
- No experimental cross-section measurements are cited. Every number in this video is
  computed from the partial-wave sum in this folder; the video says so on screen.

## Keeping this table honest

The Beat column is generated from `beat_sheet.json`, not maintained by hand — it drifted
through three restructures before this was noticed, at one point pointing eight of sixteen
claims at the wrong beat. `build_beat_sheet.py` now re-checks it on every build and fails
if a claim's beat here disagrees with the sheet.

## Open items before Gate P

- [x] **C6b** — *resolved 2026-08-27, without a citation.* Rather than assert 2/3 on a
      source we could not read, the claim is now carried by a falsification test that rules
      out the neighbouring exponents (R3a). The narration needed no change: "consistent with
      two thirds, and nothing else nearby" was already the exact claim, and the evidence has
      caught up to it.
- [ ] *(optional, non-blocking)* Read Nussenzveig, *Ann. Phys.* **34** (1965) 23–95 if a
      copy becomes available, and compare its coefficient against our measured C ≈ 0.996.
      This would upgrade C6b from "neighbours ruled out" to "matches the derivation".
- [ ] Confirm on-screen source lines render legibly at 1080p for C10 (source-video credit)
      and C14 (van de Hulst / optical theorem).

## Sources consulted

- [Extinction paradox — Wikipedia](https://en.wikipedia.org/wiki/Extinction_paradox) — the
  2πa² result, the van de Hulst and Brillouin explanations, and the optical-theorem link.
- [Hard Sphere Scattering — Fitzpatrick, UT Austin](https://farside.ph.utexas.edu/teaching/qmech/Quantum/node136.html)
  — partial-wave treatment, low- and high-energy limits, l_max ≈ ka.
- [14.6: Hard-Sphere Scattering — Physics LibreTexts](https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/14:_Scattering_Theory/14.06:_Hard-Sphere_Scattering)
  — same treatment, openly licensed.
- Primary numerical evidence: [`experiment/hard_sphere.py`](experiment/hard_sphere.py) and
  [`experiment/RUN-LOG.txt`](experiment/RUN-LOG.txt), this folder.
