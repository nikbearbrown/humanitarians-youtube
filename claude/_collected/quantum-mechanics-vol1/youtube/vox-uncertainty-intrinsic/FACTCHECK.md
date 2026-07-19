# FACTCHECK — vox-uncertainty-intrinsic

Source: quantum-mechanics-vol1/chapters/09-operators-and-uncertainty.md

## Claims checked

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Uncertainty limit is in the state before measurement | PASS | Ch.9: "The limitation lives in the state itself, before any apparatus touches it" |
| B02 | sigma_x * sigma_p >= hbar/2 even with no particle measured twice | PASS | Ch.9: "No single copy of the electron is ever measured twice. No measurement disturbs any other measurement." |
| B03 | Uncertainty is an algebraic theorem, not a disturbance story | PASS | Ch.9: "No experiment appears in the proof. The bound is fixed by how the state is prepared, not by any measurement." |
| B04 | [x̂, p̂] = i*hbar (canonical commutation relation) | PASS | Ch.9 eq. boxed: "[x̂,p̂] = iℏ" |
| B05 | Definite position state = spike in x = flat in p (plane wave) | PASS | Ch.9: "Any state with definite position (a Dirac delta in x) is infinitely spread in momentum" |
| B06 | Gaussian saturates the Kennard bound exactly | PASS | Ch.9: "For the Gaussian, the anticommutator term happens to vanish, so both bounds agree" |
| B07 | Robertson inequality: sigma_A * sigma_B >= (1/2)|<[A,B]>| | PASS | Ch.9 eq.: Robertson inequality 1929 |
| B07 | Proof uses Cauchy-Schwarz | PASS | Ch.9: "Move 1 (Cauchy-Schwarz)" |
| B08 | Commuting operators share a common eigenbasis | PASS | Ch.9: "If it is zero, the operators commute and share a common eigenbasis" |
| B09 | Electron in atom of width ~1 angstrom has minimum p spread ~ hbar/angstrom | PASS | Direct from Kennard bound sigma_p >= hbar/(2*sigma_x) |

## Exclusions honored
- No Robertson inequality proof steps (Cauchy-Schwarz moves omitted from narration)
- No Schrodinger tighter bound algebra
- No Hermite polynomial wave functions

## Verdict: PASS
