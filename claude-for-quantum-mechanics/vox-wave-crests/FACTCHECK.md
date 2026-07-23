# FACTCHECK — vox-wave-crests

Source: `quantum-mechanics-vol1/chapters/08-the-free-particle-and-wave-packets.md`

## Claims audit

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | Ripples inside a quantum wave packet race forward — born at back, dying at front | ✓ | Ch.8 p.83: "Individual crests keep entering the packet from behind and emerging at the front." | — |
| B02 | A classical pulse on a guitar string moves as one unit — wiggles travel with the blob | ✓ | Standard wave mechanics; the distinction between classical non-dispersive and quantum dispersive media is the chapter's whole point | — |
| B03 | Crests are two times faster than the blob | ✓ | Ch.8 p.81: "v_g / v_ph = 2" explicitly derived | — |
| B04 | Wave packet = superposition of plane waves with nearby momenta | ✓ | Ch.8 p.21: "We build... a wave packet, formed by superposing plane waves with nearby momenta" | — |
| B05 | Shorter wavelength = higher momentum; higher momentum = faster in QM | ✓ | p = hbar·k; omega = hbar·k²/2m; d·omega/dk = hbar·k/m; so v_g ∝ k ∝ p | — |
| B06 | Phase velocity = p/2m for a free quantum particle | ✓ | Ch.8 p.60: "v_ph = hbar·k/2m = p/2m" | — |
| B07 | Group velocity = p/m = classical velocity; group velocity is twice phase velocity | ✓ | Ch.8 p.75: "v_g = hbar·k_0/m = p_0/m" and p.81: "v_g/v_ph = 2" | — |
| B08 | New crests born at trailing edge, vanish at leading edge | ✓ | Ch.8 p.83 verbatim | — |
| B09 | No detector records where a crest is — only where the blob is | ✓ | Born rule: |\Psi|^2 = probability density; crest position (phase) not observable | — |
| B10 | Ocean swell crests race through the wave group; group carries energy to shore | ✓ | Standard dispersive wave physics; textbook analogy widely used | — |
| B11 | Phase carries no energy, carries no particle | ✓ | The phase velocity is a property of the wave structure; the energy flux follows the group velocity in dispersive media | — |
| B12 | EXAMPLE: p=1 (dimensionless), v_g=1, v_ph=0.5; after t=1, blob at x=1, crests at x=0.5 | ILLUSTRATIVE | Dimensionless illustrative values consistent with v_g=2·v_ph ratio | Label "illustrative" confirmed in narration |
| B13 | Crests run at half-speed; packet runs at full speed | ✓ | Summary of verified claims above | — |

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| wave packet | B01 (shown) / B04 (named) | B01 shows the mystery; viewer wants a name for the blob |
| crests | B01 (shown) | B01 shows them racing ahead |
| phase velocity | B06 | B03 asks "why twice as fast?" → viewer needs a name for crest speed |
| group velocity | B07 | B06 introduces phase velocity → viewer needs the contrasting term |
| superposition | B04 | B03 sets up the question; B04 explains packet structure |
| envelope | B07 | B04–B05 establish the superposition structure; B07 names the blob |

## Illustrative numbers confirmed
- B12: dimensionless p=1 unit, v_g=1, v_ph=0.5, t=1s → blob at 1, crests at 0.5. Labeled illustrative. Consistent with the v_g=2·v_ph ratio throughout.

## Exclusions confirmed
- No Taylor expansion of omega(k): absent
- No Fourier-integral derivation: absent  
- No dispersion-spreading math: absent
- No equations on screen: absent (relationships stated verbally)
