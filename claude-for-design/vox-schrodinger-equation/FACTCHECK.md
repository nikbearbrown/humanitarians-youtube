# FACTCHECK — vox-schrodinger-equation

Pass date: 2026-07-05 · sources: `books/quantum-mechanics-vol1/chapters/04`
(source of record), independent recomputation (h = 6.626×10⁻³⁴ J·s,
e = 1.602×10⁻¹⁹ C), standard history. Regenerate on narration/viz change
(Gate F).

| beat | claim | verdict | basis |
|---|---|---|---|
| B01 | first six months of 1926; Austrian physicist; four papers; one equation at the center of all four | ✓ | chapter ("Within six months he submitted four foundational papers to Annalen der Physik"); the four "Quantisierung als Eigenwertproblem" papers I–IV, Ann. Phys. 79, 80, 81 (1926) — standard record; Schrödinger Austrian ✓ |
| B02 | film four callback (psi² gives the odds); this equation moves psi; "law of motion for the quantum world" | ✓ | series continuity; "law of motion" is fair register for the TDSE |
| T01 | LHS = rate of change of Ψ; RHS = energy operator acting on the state; "energy drives all change" | ✓ | chapter (TDSE structure); the claim is the standard reading — stationary states don't change observably precisely because energy is definite |
| T02 | i ⇒ rotation not decay; ℏ sets the clock speed; Ĥ decides how fast each piece spins | ✓ | chapter (phase e^(−iEt/ℏ) rotates; each eigenstate at its own E/ℏ); "rotation not decay" = the i is what makes the evolution unitary rather than diffusive — standard, consistent with ch 3's real-LHS contradiction |
| T03 | separation ⇒ every energy state gets phase e^(−iEt/ℏ); 1 eV → "two hundred forty trillion turns a second" | ✓ | chapter eq (4.1); COMPUTED: 1 eV/h = 2.418×10¹⁴ Hz = 242 trillion turns/s — "two hundred forty trillion" ✓ (TURNS = Hz, deliberately not rad/s; rad/s would be 1.5×10¹⁵) |
| B04 | one guess (product ansatz); equation splits: trivial time clock + eigenvalue problem in space | ✓ | chapter (calls (4.1) "trivial"; (4.2) the TISE eigenvalue problem; same constant E on both sides) |
| B05 | clock and shadow: Re/Im spin together 90° apart; \|Ψ\|² frozen | ✓ | chapter, near-verbatim ("The wave function is a clock; the probability density is the clock's shadow... The shadow does not move, but the clock is spinning"); Re ∝ cos, Im ∝ −sin ✓ |
| B06 | every laser: two mirrors, only waves that fit survive, the rest self-destroy | ✓ | chapter (laser-cavity section, faithful compression) |
| B07 | confinement + wave equation = a menu of shapes, each with its own energy; that menu is quantization | ✓ | chapter ("The cavity selects... the discrete set that satisfies its boundary conditions"; modes ↔ energies) |
| B08 | mix two states: density sloshes at the beat (E₂−E₁)/ℏ; total energy constant | ✓ | chapter: cross term 2Re[c₁*c₂ψ₁*ψ₂e^(−i(E₂−E₁)t/ℏ)]; ⟨H⟩ = Σ\|cₙ\|²Eₙ exactly time-independent ("perfectly still" = the expectation value, which is what the narration says: "the total energy") |
| B09 | mathematics a century old; Fourier proved the building blocks complete in 1822, for heat | ✓ | chapter ("Fourier proved (for the heat equation) in 1822... a century older than quantum mechanics"); Théorie analytique de la chaleur, Paris, 1822 — standard record; completeness claim scoped to the well's sine basis by the chapter, narration's "these building blocks" inherits that scope |
| B10 | equation in six months; decades uneasy about its meaning; "his doubt became physics' most famous cat" | ✓ w/ label | six months per chapter; the unease is EDITORIAL-DEFENSIBLE (Schrödinger's lifelong dissent from the probabilistic/Copenhagen reading — Born–Einstein-era correspondence and the 1935 paper itself, which frames the cat as a critique); cat: "Die gegenwärtige Situation in der Quantenmechanik," Naturwissenschaften 23 (1935) ✓ |
| B11 | next: particle in a box, "the notes it's allowed to play" | ✓ | book structure (05-the-infinite-square-well.md); "notes" = the standing-mode menu, set up by B07 |
| kicker/SHOTLIST | ages/dates: Schrödinger b. 12 Aug 1887 → 38 in Jan–Jun 1926; 1887–1961 | ✓ | COMPUTED; d. 4 Jan 1961 |

## Verdict

No blocking errors. Two labels:

1. **B10 "decades uneasy... most famous cat"** — editorial compression,
   defensible: the 1935 cat paper is itself a critique of the standard
   interpretation, and Schrödinger's dissent is documented into the 1950s.
   Labeled here; kicker line in annotations.json ("His doubt became the
   cat.") matches.
2. **T03 "turns" not radians** — deliberate: 1 eV/h = 2.42×10¹⁴ full turns
   per second. Anyone recomputing with ℏ gets 1.5×10¹⁵ rad/s; the narration
   says TURNS. Noted so a future factcheck doesn't "correct" it wrongly.

Scope note: separation ALGEBRA, hydrogen, and the well's eigenfunctions are
deliberately absent — ch 5's film (B11 tease). Not errors.
