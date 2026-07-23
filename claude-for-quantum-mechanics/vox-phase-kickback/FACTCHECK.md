# FACTCHECK — vox-phase-kickback

Source: `quantum-mechanics-vol4/chapters/04-quantum-gates-and-circuits.md`

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | Deutsch problem: function is either constant or balanced, one bit input | ✓ | Ch4 Worked Example 2: "determine whether it is constant (f(0)=f(1)) or balanced (f(0)≠f(1)). Classical lower bound: 2 queries. Quantum: 1 query, zero error." |
| B03 | Classical solution requires 2 queries | ✓ | Ch4: "Classical lower bound: 2 queries." |
| B04 | Putting query in superposition and measuring still yields random result | ✓ | Ch4: "Quantum parallelism alone does not help: measuring after the oracle step gives one random value." |
| B06 | Ancilla set to |-> = (|0>-|1>)/sqrt(2) | ✓ | Ch4: "ancilla q_1 = |1>. The oracle U_f implements |x>|y> -> |x>|y xor f(x)>." After H: |-> = H|1> = (|0>-|1>)/sqrt(2) ✓ |
| B07 | Oracle on ancilla |-> returns (-1)^f(x)|x>|-> — the phase kickback | ✓ | Ch4: "U_f|x>|-> = (-1)^f(x)|x>|->. The function value f(x) has been kicked back as a phase on the query register. The ancilla is unchanged." |
| B08 | Constant case: both amplitudes same sign (|+> state) | ✓ | Ch4: "If f is constant: both terms acquire the same phase, so q_0 proportional to |0>+|1> = sqrt(2)|+>." |
| B08 | Balanced case: amplitudes have opposite signs (|-> state) | ✓ | Ch4: "If f is balanced: the phases are opposite, so q_0 proportional to |0>-|1> = sqrt(2)|->." |
| B10 | Hadamard on |+> gives outcome 0 (constant case) | ✓ | Ch4: "After H on q_0: H|+> = |0> (constant)." |
| B10 | Hadamard on |-> gives outcome 1 (balanced case) | ✓ | Ch4: "H|-> = |1> (balanced). Measure q_0: outcome 0 -> constant; outcome 1 -> balanced." |
| B13 | Every quantum speedup uses the pattern: superposition -> phase encoding -> interference | ✓ | Ch4: "This is the template for quantum algorithms: superposition evaluates a function on many inputs; interference filters the outputs so the answer has high amplitude and wrong answers cancel." |
| B14 | One query, zero chance of error | ✓ | Ch4: "Quantum: 1 query, zero error." |

## Exclusions confirmed

- NO Deutsch-Jozsa generalization to n bits (never mentioned) ✓
- NO quantum phase estimation (never mentioned) ✓
- NO Simon's or Grover's algorithm (Grover mentioned only at literacy level in ch4 but NOT in any beat) ✓
- NO gate-matrix algebra (no matrices shown or referenced) ✓

## Terms table

| Term | Prior beat creating need | Debut beat |
|------|--------------------------|------------|
| constant function | B02 (problem framing) | B02 |
| balanced function | B02 (problem framing) | B02 |
| ancilla qubit | B06 (two-wire circuit introduced) | B06 |
| |-> state | B06 (ancilla setup explained) | B06 |
| phase kickback | B07 (mechanism shown visually) | B07 |
| Hadamard gate | B10 (readout mechanism) | B10 |
| interference | B10 (Hadamard converts phase) | B10 |

## Illustrative numbers

- B14: The circuit outcome '0 = constant' is a correct result of the Deutsch algorithm, not illustrative — it is the mathematical answer. ✓
