# FACTCHECK — vox-ultraviolet-catastrophe

Pass date: 2026-07-04 · sources: `books/quantum-mechanics-vol1/chapters/01`
(the book chapter, primary source of record), independent recomputation of
every number (constants: h = 4.1357×10⁻¹⁵ eV·s, kB = 8.6173×10⁻⁵ eV/K),
period facts against standard history of physics. Regenerate this file
whenever narration or viz data changes (Gate F).

| beat | claim | verdict | basis |
|---|---|---|---|
| B01 | glow color depends only on temperature, not material | ✓ | blackbody universality (Kirchhoff); chapter opening |
| B02 | measured to ~1% by 1900 | ✓ | Lummer–Pringsheim precision, chapter |
| B02 | classical prediction literally infinite | ✓ | ∫RJ dν diverges; chapter |
| B03 | Lummer & Pringsheim, Berlin, precise spectra | ✓ | PTR Berlin; chapter |
| B04 | hotter → taller hump, peak toward blue | ✓ | Wien: ν_max = 2.821 kBT/h ∝ T (scene fixed to match — was backwards, caught in review) |
| B05 | mode count is undisputed geometry | ✓ | 8πν²/c³; chapter |
| B06 | equipartition: kBT per EM mode | ✓ | 2 quadratic terms/mode; chapter |
| B06 | "ran the steam age flawlessly" | RHETORIC | kinetic theory lineage; labeled flourish, not a claim |
| B07 | RJ = modes × kT; fits at long wavelength, then grows without bound | ✓ | chapter |
| B08 | hot poker should flood the room with UV | ✓ | chapter's own reductio |
| B09 | counting ✓, equipartition ✓ (gases), continuity is the broken assumption | ✓ | chapter (chapter itself caveats low-T heat capacities) |
| B10 | Planck was curve-fitting, working backward from data | ✓ | chapter; standard history |
| B11 | oscillators (cavity walls) restricted to 0, hν, 2hν… | ✓ | chapter — walls, NOT the field (Einstein's step comes next film) |
| T01 | E = hν; in-between energies banned (for the oscillators) | ✓ | chunk law; physical-commitment phrasing per EQUATIONS.md zone 5 merge |
| T02 | h = 6.626×10⁻³⁴ J·s | ✓ | CODATA |
| T03 | budget kBT@3000K = 0.26 eV | ✓ | computed 0.2585 eV |
| T03 | UV chunk 12.4 eV; ≈48× budget ("fifty times" spoken) | ✓ | computed 12.41 eV, x = 47.99 |
| T03 | "red chunks cost almost nothing" (1.8 eV ≈ 689 nm) | SIMPLIFICATION | red = 7× budget (occupancy ~e⁻⁷) — small only relative to UV's e⁻⁴⁸. Comparative point stands; card shows the true numbers |
| B12 | Planck matches RJ at low ν, dies exponentially at high ν | ✓ | expansion → kBT; e^(−hν/kBT) tail; chapter |
| B13 | classical error ≈ twenty orders of magnitude | ✓ | computed ratio 6.9×10⁻²⁰ |
| B14 | read to the Physical Society, 14 December 1900 | ✓ | Verhandlungen DDPG 2, 237 (1900) — the scan on screen IS the document |
| B14 | "his constant within one percent of today's value" | MINOR | computed 1.15% (6.55 vs 6.626). The book itself says "within one percent" — narration follows the book. Candidate book erratum: "within about one percent" |
| B15 | Planck spent years trying to un-quantize his formula; cannot be done | ✓ | chapter |
| B16 | photoelectric effect is the next chapter section | ✓ | chapter §"A Completely Different Crisis" |

## Verdict

No blocking errors. One MINOR (B14's "within one percent" is strictly 1.15% —
follows the book; fix in the book or accept), one labeled SIMPLIFICATION
(T03 red-chunk cost — defensible, numbers on screen are exact), one labeled
RHETORIC (B06 steam age). Physics error in B04's original render (hotter
peaked red-ward) was caught in review and fixed at the scene level before
this pass was formalized.
