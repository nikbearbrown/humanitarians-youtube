# FACTCHECK — medhavy-who-was-max-planck

Checker: Claude Code
Date: 2026-07-16
Source: physics-modern-physics/youtube/who-was-max-planck/beat_sheet.json + standard physics references

## Claim-by-claim verification

| # | Claim | Beat | Verdict | Source / Notes |
|---|-------|------|---------|----------------|
| 1 | Classical physics prediction diverges to infinity at short wavelengths | B01 | PASS | The Rayleigh-Jeans law B(ν,T) = 2ν²kT/c² grows without bound as ν → ∞. Standard result. |
| 2 | Planck's fix: energy is discrete; E = hν | B02 | PASS | Planck 1900 ("Ueber das Gesetz der Energieverteilung im Normalspectrum"). Standard. |
| 3 | h = 6.626 × 10⁻³⁴ J·s | B02 | PASS | CODATA 2018 value: h = 6.62607015 × 10⁻³⁴ J·s. Rounded correctly. |
| 4 | Planck called the quantum "an act of desperation" | B02, B04 | PASS | Planck to R.W. Wood, 1931: "It was an act of desperation." Frequently cited, well-sourced. |
| 5 | Planck distribution matches all blackbody measurements | B03 | PASS | Standard result; Planck distribution is the correct blackbody spectral distribution. |
| 6 | Rayleigh-Jeans diverges at short wavelengths | B03 | PASS | See claim 1. |
| 7 | Planck tried to derive his formula without the quantum assumption and failed | B04 | PASS | Historically documented; see Kuhn, "Black-Body Theory and the Quantum Discontinuity." |
| 8 | Einstein used the quantum in 1905 to explain the photoelectric effect (photon) | B04 | PASS | Einstein 1905, "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." Nobel Prize 1921 for this. |
| 9 | 1905 Einstein photon; 1913 Bohr atom; 1925–27 Heisenberg/Schrödinger/Dirac QM | B05 | PASS | Standard physics history dates. All correct. |
| 10 | Transistor (Bell Labs, 1947); laser (Maiman, 1960); MRI (Lauterbur, 1973) | B05 | PASS | Bell Labs transistor: Bardeen/Brattain/Shockley, 1947. Maiman first working laser: 1960. Lauterbur MRI: 1973. All correct. |
| 11 | Planck born Kiel, 1858 | B06 | PASS | Born 23 April 1858, Kiel, Holstein. |
| 12 | Nobel Prize 1918 | B06 | PASS | Nobel Prize in Physics 1918, awarded 1919. |
| 13 | Lost one son in World War One | B06 | PASS | Karl Planck died in battle at Verdun, 1916. |
| 14 | Erwin executed by Nazis in 1945 | B06 | PASS | Erwin Planck executed 23 January 1945 for involvement in the July 20, 1944 plot against Hitler. |
| 15 | Planck argued for Jewish colleagues | B06 | PASS | Documented; Planck confronted Hitler directly about dismissal of Jewish scientists (1933). |
| 16 | Still working at eighty-eight (bombed out) | B06 | PASS | Planck was born 1858; 1946 = age 87-88. Evacuated due to bombing in later war years. Minor: "bombed out" is a slight simplification — evacuated from Rogätz after destruction. Acceptable editorial compression. |
| 17 | Died 1947 | B06 | PASS | Died 4 October 1947, Göttingen. |

## Numbers check

- h = 6.626 × 10⁻³⁴ J·s: CORRECT (CODATA 2018)
- E = hν: CORRECT (Planck relation)
- UV catastrophe at short wavelengths: CORRECT (Rayleigh-Jeans diverges as ν → ∞)
- 1905 Einstein, 1913 Bohr, 1918 Nobel, 1947 death: all CORRECT

## Editorial claims (labeled)

- "What follows from Planck's 1900 paper is almost hard to take in" — authorial observation, labeled as such implicitly by tone. Not a factual claim.
- "There is something that resists easy summary in a life like this" — authorial observation. Not a factual claim.

## Structure check (repair verification)

- Repaired from 8-beat MedhavyCard structure to 10-beat Claude-explainer. CONFIRMED.
- B00 = ClaudeComposerAsk (not MedhavyOpen). CONFIRMED.
- B02 = Manim B02.mp4 from canonical (not MedhavyConceptCard). CONFIRMED.
- B04 = Manim B04.mp4 from canonical (not MedhavyConceptCard). CONFIRMED.
- B06 = ClaudeWindow (not MedhavyConceptCard). CONFIRMED.
- B08 = ClaudeComposerAsk "Your turn." (new handoff beat). CONFIRMED.
- B09 = ClaudeTitleOutro (not MedhavyOutro). CONFIRMED.

## Verdict

All factual claims verified. Numbers correct. Dates correct. Historical attributions correct.
Beat structure repaired: correct 10-beat Claude-explainer, no wrong-pattern substitutions.

VERDICT: PASS
