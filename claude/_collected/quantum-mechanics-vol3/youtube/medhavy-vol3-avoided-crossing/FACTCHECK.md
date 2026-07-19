# FACTCHECK — medhavy-vol3-avoided-crossing

All physics facts verified against:
- Griffiths, *Introduction to Quantum Mechanics*, 3rd ed., Ch. 8 (Perturbation Theory)
- Sakurai & Napolitano, *Modern Quantum Mechanics*, 3rd ed., §5.1 (Two-State Mixing)
- Landau & Lifshitz, *Quantum Mechanics*, §79 (Level Repulsion)

## Claims verified

| Claim | Source | Status |
|---|---|---|
| Two-level Hamiltonian: H = diag(E₁, E₂) + [[0,V],[V,0]] | Standard QM | PASS |
| Eigenvalues: E± = (E₁+E₂)/2 ± √((ΔE/2)²+V²) | 2×2 eigenvalue problem | PASS |
| Minimum gap = 2\|V\| at degeneracy point (E₁=E₂) | ΔE=0 → gap=2\|V\| | PASS |
| Concrete: E₁=0, E₂=1 eV, V=0.1 eV → gap = 0.2 eV | arithmetic | PASS |
| When V=0, levels cross freely | Eigenvalues become E₁, E₂ unchanged | PASS |
| When V≠0, levels always avoid crossing | gap = 2\|V\| > 0 always | PASS |
| "Avoided crossing" is the avoided-crossing theorem / von Neumann-Wigner theorem | Landau §79 | PASS |
| Energy levels repel: 2nd-order E correction pushes levels apart | Griffiths Eq. 7.15 | PASS |

## Verdict: APPROVED
