# SOURCES.md — claude-liam-algorithmic-art

## Verbatim Quotes

| Figure | Quote | Source |
|--------|-------|--------|
| B03 / Figure 2 | "Organic Turbulence," "Quantum Harmonics," "Recursive Whispers," "Field Dynamics," "Stochastic Crystallization" | algorithmic-art SKILL.md — movement name examples |
| B04 / Figure 4 | "Think like a jazz musician quoting another song through algorithmic harmony - only those who know will catch it, but everyone appreciates the generative beauty." | algorithmic-art SKILL.md — conceptual seed section |
| B06 / Figure 5 | "a series of prints from the same plate" | algorithmic-art SKILL.md — Art Blocks reproducibility section |
| B08 / Figure 7 | "meticulously crafted algorithm" | algorithmic-art SKILL.md — quality standards (repeated ×6) |
| B08 / Figure 7 | "the product of deep computational expertise" | algorithmic-art SKILL.md — quality standards (repeated ×4) |
| B08 / Figure 7 | "painstaking optimization" | algorithmic-art SKILL.md — quality standards (repeated ×3) |
| B08 / Figure 7 | "master-level implementation" | algorithmic-art SKILL.md — quality standards (repeated ×5) |

All verbatim quotes used by permission as descriptive/educational excerpts from Anthropic's
algorithmic-art SKILL.md instruction folder.

## Seed Values

| Figure | Component | Seed | Beat | Notes |
|--------|-----------|------|------|-------|
| Figure 1 — Organic Turbulence | AlgArtOrganicTurbulence | 42 | B02 | Primary showpiece seed |
| Figure 2 — Quantum Harmonics | AlgArtMovementGallery (section 0) | 7 | B03 | Gallery vignette seed |
| Figure 2 — Recursive Whispers | AlgArtMovementGallery (section 1) | 13 | B03 | Gallery vignette seed |
| Figure 2 — Field Dynamics | AlgArtMovementGallery (section 2) | 99 | B03 | Gallery vignette seed |
| Figure 2 — Stochastic Crystallization | AlgArtMovementGallery (section 3) | 137 | B03 | Gallery vignette seed |
| Figure 4 — Hidden Seed | AlgArtHiddenSeed | 256 | B04 | Hidden reference: φ = 1.618033… |
| Figure 5 — Seed Grid tile 0 | AlgArtSeedGrid | 1 | B06 | Grid seed 1 of 9 |
| Figure 5 — Seed Grid tile 1 | AlgArtSeedGrid | 7 | B06 | Grid seed 2 of 9 |
| Figure 5 — Seed Grid tile 2 | AlgArtSeedGrid | 13 | B06 | Grid seed 3 of 9 |
| Figure 5 — Seed Grid tile 3 (highlighted) | AlgArtSeedGrid | 42 | B06 | Grid seed 4 of 9 — terracotta ring |
| Figure 5 — Seed Grid tile 4 | AlgArtSeedGrid | 99 | B06 | Grid seed 5 of 9 |
| Figure 5 — Seed Grid tile 5 | AlgArtSeedGrid | 137 | B06 | Grid seed 6 of 9 |
| Figure 5 — Seed Grid tile 6 | AlgArtSeedGrid | 256 | B06 | Grid seed 7 of 9 |
| Figure 5 — Seed Grid tile 7 | AlgArtSeedGrid | 314 | B06 | Grid seed 8 of 9 |
| Figure 5 — Seed Grid tile 8 | AlgArtSeedGrid | 512 | B06 | Grid seed 9 of 9 |
| Figure 6 — Fixed/Variable System A | AlgArtFixedVariable (SystemA) | 42 | B07 | Organic Turbulence style |
| Figure 6 — Fixed/Variable System B | AlgArtFixedVariable (SystemB) | 7 | B07 | Quantum Harmonics style |

## Hidden Reference (Figure 4)

The hidden reference embedded in AlgArtHiddenSeed is **φ (phi) = 1.618033988749895**
(the golden ratio). It appears as the multiplier in the flow angle calculation:

```
flowAngle = (n1 * PHI + n2 * 0.618) * Math.PI * 2.618
```

This is visible to anyone reading the source code but invisible on the canvas —
exactly as the skill describes: "only those who know will catch it."

## Noise Function

All flow fields use a deterministic value-noise implementation with a seeded
hash function (sin-based gradient approximation). The PRNG uses the mulberry32
algorithm. Both are deterministic: same frame number → same pixel values, always.
