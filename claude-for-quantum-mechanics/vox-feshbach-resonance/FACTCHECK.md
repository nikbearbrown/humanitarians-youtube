# FACTCHECK — vox-feshbach-resonance

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | Ultracold cesium Feshbach resonance — cross-section spikes by factor of 10,000 | ✓ | Ch07: "scattering cross-section spikes by a factor of ten thousand in a few milligauss" |
| B02 | At one field value new two-body bound state appears at zero binding energy | ✓ | Ch07: "a new two-body bound state flicks into existence at zero binding energy" |
| B04 | Low-energy cross-section depends on scattering length | ✓ | Ch07: sigma_tot → 4*pi*a_s^2 as k→0 |
| B05 | sigma = 4*pi*a^2 | ✓ | Ch07: exact formula for low-energy s-wave scattering |
| B06 | Bound state at exactly zero energy: wave function barely decays outside well | ✓ | Ch07: "a bound state at exactly zero energy means the wave function barely decays outside the well" |
| B07 | As binding energy → 0, wave function extends further | ✓ | Ch07: scattering length → +infinity as bound state approaches threshold |
| B08 | At exactly zero binding energy, wave function extends to infinity | ✓ | Ch07: scattering length diverges at threshold |
| B09 | Scattering length passes through +/- infinity at each new bound state threshold | ✓ | Ch07: Levinson theorem context; "passing through ±∞ each time a new bound state is born" |
| B11 | Feshbach resonance uses magnetic field to tune bound-state energy across threshold | ✓ | Ch07: "Feshbach resonances allow the scattering length to be tuned from −∞ to +∞ by adjusting a magnetic field" |
| B13 | V0=0.3 eV, no bound state, sigma=0.08 nm^2 | ILLUSTRATIVE | From card example seed |
| B13 | V0=0.38 eV, first bound state at threshold, a→1000 nm, sigma=4*pi*(1000)^2≈10^7 nm^2 | ILLUSTRATIVE | From card example seed; 4*pi*(1000)^2 ≈ 12.6×10^6 nm^2 ≈ 10^7 nm^2 ✓ |
| B13 | V0=0.42 eV, bound state 0.01 eV below threshold, a=12 nm, sigma=1800 nm^2 | ILLUSTRATIVE | From card example seed; 4*pi*(12)^2 ≈ 1810 nm^2 ≈ 1800 nm^2 ✓ |

## Terms table

| Term | Debuts at | Prior beat creates need |
|------|-----------|------------------------|
| cross-section | B01 | B01 (concrete spike observed) |
| scattering length | B04 | B04 (introduced when explaining what determines cross-section) |
| bound state | B02 | B02 (shown as appearing at specific field) |
| threshold | B06 | B06 (need arises when discussing zero binding energy) |
| Feshbach resonance | B11 | B11 (named when explaining how field tunes bound state) |

## Illustrative numbers
- B13: all numbers from card example seed, labeled illustrative in narration.
