# PEDAGOGY — medhavy-vol2-orbital-energies

## What the learner already knows
Hydrogen energy levels, angular momentum quantum number l, effective nuclear charge concept, multi-electron atoms.

## What this reel teaches
The workflow: how to prompt Claude Code to build an orbital energy level diagram
comparing hydrogen (degenerate) vs sodium (l-split), read the code and verify
the n-dependent vs (n,l)-dependent energy formulas, run and check two predictions
(H n=3 all degenerate, Na 3s below 3p by ≈2.1 eV), then iterate to shade the
degeneracy-lifted gap.

## Loop structure
PROMPT → SCRIPT → RUN → CHANGE

## Physics gate numbers
- H E_n = -13.6/n² eV → E(n=3) = -1.511 eV for 3s=3p=3d ✓ FACTCHECK
- Na 3s ≈ -5.1 eV, Na 3p ≈ -3.0 eV, gap ≈ 2.1 eV ✓
- P1: H n=3 all three at -1.51 eV (degenerate)
- P2: Na 3s is 2.1 eV below Na 3p

## Medhavy register compliance
- FIRST beat: MedhavyOpen ✓
- LAST beat: MedhavyOutro ✓
- tts: "med dahvy" in narration, "Medhavy" on screen ✓
- No "important to understand" framing ✓
- All Text() in INK ✓

VERDICT: PASS
