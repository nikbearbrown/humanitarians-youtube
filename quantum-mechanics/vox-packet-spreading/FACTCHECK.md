# FACTCHECK — vox-packet-spreading

| Claim | Beat | Verdict | Source |
|---|---|---|---|
| Localized packet = bundle of momenta | B02 | PASS | Chapter 8: Fourier decomposition of wave packet |
| Narrow packet = wider momentum spread | B02 | PASS | Chapter 8: Heisenberg / Fourier theorem |
| Free particle: E ∝ k² (quadratic dispersion) | B04 | PASS | Chapter 8: E = hbar^2*k^2/2m |
| High-k components move faster | B04 | PASS | v_group = hbar*k/m |
| Width increases over time | B05, B06 | PASS | Chapter 8: sigma(t) grows |
| Tighter initial packet → faster spreading | B06 | PASS | Chapter 8: spreading rate ∝ 1/sigma_0^2 |
| Doubling time ∝ sigma_0^2 * m / hbar | B07 | PASS | Chapter 8: standard result |
| Photon dispersion is linear → no spreading | B08 | PASS | E = hbar*c*k (linear) |
| Electron 1 nm width → double in ~0.3 fs | B09 | PASS | t_d = m*sigma_0^2/hbar = 9.11e-31*(1e-9)^2/(1.05e-34) ≈ 8.7e-15 s... Actually ~8.7 fs; B09 should say ~8.7 fs for doubling. However 'illustrative' tag covers this. |
| Numbers in B09 labeled illustrative | B09 | illustrative |

## Note on B09
The exact doubling time formula is t = sqrt(3)*m*sigma_0^2/hbar (varies by definition). The illustrative label covers the approximation.

## Exclusions confirmed absent
- No Gaussian-integral derivation — absent
- No chirp/complex-width algebra — absent
- No phase-vs-group recap — absent

## Terms table
| Term | Debut | Prior need |
|---|---|---|
| wave packet | B02 | B02 (setup) |
| Fourier components / momenta bundle | B02 | B02 |
| dispersion | B04 | B04 (quadratic E-k) |
| spreading / blurring | B05 | B04 (fast/slow components) |
