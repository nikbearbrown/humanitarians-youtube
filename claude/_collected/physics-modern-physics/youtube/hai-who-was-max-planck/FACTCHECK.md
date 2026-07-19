# FACTCHECK — hai-who-was-max-planck

Checker: Claude Code
Date: 2026-07-16
Source: physics-modern-physics/youtube/who-was-max-planck/beat_sheet.json + standard physics references

## Claim-by-claim verification

| # | Claim | Beat | Verdict | Source / Notes |
|---|-------|------|---------|----------------|
| 1 | Classical physics predicted infinite energy from a warm oven (UV catastrophe) | B00, B01 | PASS | Rayleigh-Jeans divergence at high frequencies. Standard result. |
| 2 | Rayleigh-Jeans derived from Maxwell's equations and classical statistical mechanics | B01 | PASS | Correct provenance: Maxwell electrodynamics + equipartition theorem. |
| 3 | RJ matches data at long wavelengths, diverges at short | B01 | PASS | Standard result. RJ is the long-wavelength (classical) limit of Planck. |
| 4 | E = nhν where n = 1, 2, 3, … | B02 | PASS | Correct Planck quantization condition. n is a positive integer. |
| 5 | h = 6.626 × 10⁻³⁴ J·s | B02 | PASS | CODATA 2018: h = 6.62607015 × 10⁻³⁴ J·s. Rounded correctly. |
| 6 | Rayleigh-Jeans valid when hν ≪ kT | B03 | PASS | In the limit hν/kT → 0, Planck distribution reduces to Rayleigh-Jeans. Correct. |
| 7 | Planck's original derivation treated quantization as mathematical convenience | B04 | PASS | Historically documented. Planck did not initially accept physical reality of quanta. |
| 8 | Position/momentum quantization requires Schrödinger equation | B04 | PASS | Correct: Planck's quantization applies to energy of oscillators interacting with radiation field. Wave mechanics (Schrödinger 1926) extends quantization to spatial wavefunctions. |
| 9 | Einstein used same idea in 1905 — photoelectric effect | B05 | PASS | Einstein 1905. Nobel Prize 1921 for this work. |
| 10 | Bohr atomic model: 1913 | B05 | PASS | Bohr model published 1913. |
| 11 | Heisenberg/Schrödinger/Dirac: 1925–27 | B05 | PASS | Matrix mechanics (Heisenberg 1925), wave mechanics (Schrödinger 1926), Dirac equation (1928 — slight mismatch with "1927" but "1925–27" is standard for quantum mechanics formalization period). Minor acceptable compression. |
| 12 | Transistor 1947 (solid-state quantum effects) | B05 | PASS | Bardeen/Brattain/Shockley, Bell Labs, December 1947. |
| 13 | Laser 1960 | B05 | PASS | Theodore Maiman, first working laser, May 1960. |
| 14 | MRI 1973 (Lauterbur) | B05 | PASS | Paul Lauterbur, NMR zeugmatography (MRI) paper, Nature, 1973. |
| 15 | Nobel Prize 1918 | B05, B06 | PASS | Nobel Prize in Physics 1918 (awarded 1919). |
| 16 | Planck born Kiel 1858 | B06 | PASS | Born 23 April 1858, Kiel, Holstein. |
| 17 | One son lost in World War One | B06 | PASS | Karl Planck, died at Verdun, 1916. |
| 18 | Erwin executed for involvement in July 20 plot against Hitler | B06 | PASS | Erwin Planck executed 23 January 1945, convicted of involvement in the 20 July 1944 assassination plot. |
| 19 | Planck remained in Germany advocating for colleagues | B06 | PASS | Documented. Planck met Hitler in 1933 to argue against dismissal of Jewish scientists. |
| 20 | B08 handoff prompt: "Explain the ultraviolet catastrophe and how Planck's quantum hypothesis solved it" | B08 | PASS | Accurate description of the topic. Paste-ready in Claude. |

## Numbers check

- h = 6.626 × 10⁻³⁴ J·s: CORRECT
- hν ≪ kT for Rayleigh-Jeans validity: CORRECT (stated in B04)
- 1858 born, 1918 Nobel, 1945 Erwin executed, 1947 death: all CORRECT

## Structure check (repair verification)

- Repaired from 9-beat MedhavyCard/OutroCTA structure to 10-beat Claude-explainer. CONFIRMED.
- B00 = ClaudeComposerAsk (not MedhavyConceptCard). CONFIRMED.
- B02 = Manim B02.mp4 from canonical (not MedhavyConceptCard). CONFIRMED.
- B04 = Manim B04.mp4 from canonical (not MedhavyConceptCard). CONFIRMED.
- B06 = ClaudeWindow (not MedhavyConceptCard). CONFIRMED.
- B08 = ClaudeComposerAsk "Your turn." (not B_CLI terminal exercise). CONFIRMED.
- B09 = ClaudeTitleOutro (not OutroCTA). CONFIRMED.

## Verdict

All factual claims verified. Numbers correct. Dates correct. Historical attributions correct.
Beat structure repaired: correct 10-beat Claude-explainer, no wrong-pattern substitutions.

VERDICT: PASS
