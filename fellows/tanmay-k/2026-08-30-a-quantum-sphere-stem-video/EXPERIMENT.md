# EXPERIMENT — the hard-sphere cross section, computed rather than quoted

The primary source for **"A Quantum Sphere Is Never the Size It Looks."** Every number the
film puts on screen traces to `experiment/hard_sphere.py`, and every claim beat carries on
frame the flag that produced it.

**Headline: σ/πa² → 4 as ka → 0, → 2 as ka → ∞, and never equals 1 anywhere on 0 < ka ≤ 30.**
The classical answer is wrong at every energy tested — not only near resonances.

---

## 1. The question

A hard sphere of radius `a` blocks its own shadow, so classically σ = πa² and σ/πa² = 1 at
every energy. Quantum mechanically it is not 1 anywhere. The film's job is to make that
checkable rather than asserted, so the cross section is computed from the partial-wave sum
here and read off a curve the viewer watches being drawn.

## 2. Method

For a hard sphere the phase shifts are exact:

```
tan δ_l = j_l(ka) / n_l(ka)
σ = (4π/k²) Σ (2l+1) sin²δ_l
```

Implemented in **~200 lines of standard-library Python** — no scipy, no install, no network.
The dependency-free constraint is deliberate: a viewer must be able to run this without
setting anything up, or the evidence is not really available to them.

**Spherical Bessel functions use Miller's downward recurrence.** Upward recurrence is the
obvious implementation, and past l ≈ ka it drifts by roughly thirteen orders of magnitude while
**raising no error at all** — the curve simply develops bumps that look like physics. Knowing
that in advance is why the validation below runs first, and why it is worth showing.

## 3. Validation, before any result was used

```bash
python3 hard_sphere.py --validate
```

| Check | Result |
|---|---|
| `j_l`, `n_l` against closed forms, l = 0…3 | worst error **5.3e-15** |
| Wronskian identity `j_l n_l' − j_l' n_l = 1/x²` | holds to machine precision |
| Truncation: σ stable as `lmax` grows past ka | converged |

Nothing downstream was trusted until these passed. The film shows this step rather than
skipping to the answer, because the whole argument depends on the sum being right.

## 4. Results

```bash
python3 hard_sphere.py --all
```

| Flag | What it establishes | Value on screen |
|---|---|---|
| `--limits` | low- and high-energy limits | 4 and 2 |
| `--curve` | σ/πa² across the dial | minimum **2.1988**, never 1 |
| `--check-source` | the inherited simulation, recomputed | **2.328297** vs its displayed 2.328 |
| `--exponent` | approach to the high-energy limit | **0.6659** by ka = 10⁴ |
| `--exponent-test` | falsification of neighbouring exponents | 2/3 flat, 0.65 falls, 0.70 rises |
| `--contrast` | the control | 0 spikes vs ~10 for a square well |

## 5. What the numbers do *not* establish

- **"Never 1" is verified over 0 < ka ≤ 30, not proved for all ka.** The film states that
  scope on the frame that makes the claim, rather than in a footnote.
- **The 2/3 exponent is measured, not derived.** `--exponent-test` rules out the neighbours by
  falsification — assuming 2/3 the coefficient flattens to 0.996 while 0.65 falls and 0.70
  rises — but that is evidence, not a derivation. The frame carries `measured — not derived`.
  The canonical analytic treatment is Nussenzveig, *Annals of Physics* 34 (1965) 23–95, which
  was identified but not accessible, so no coefficient is quoted from it.
- **The square-well control is a control, not a survey.** It shows the framework distinguishes
  a resonant potential from a non-resonant one; it does not characterise square wells.

## 6. The control, and why it is in the film

`--contrast` plots the hard sphere against an attractive square well of depth
2mV₀a²/ħ² = 900 on the same axes. The sphere falls smoothly with **0** spikes; the well
produces about **10**, the first near ka = 2.88.

This is the beat that could have falsified the whole framework. If "count the partial waves"
were a story that happens to fit one example, the control is where it would break — so it runs
on the same code, and the result is reported either way.

## 7. Reproduce

```bash
cd experiment
python3 hard_sphere.py --validate     # do this first
python3 hard_sphere.py --all
```

No arguments, no data files, no network. If the sphere curve wobbles, that is not physics —
the sum is truncating too early, or the Bessel functions are going up instead of down.
