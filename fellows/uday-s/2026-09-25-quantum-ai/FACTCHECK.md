# FACTCHECK — The Arrow Points The Other Way

Status: **GATE F SIGNED — 2026-09-25. 12 rows PASS.**
**Two claims in the commissioning brief did not survive checking and were
rewritten. One survived and is used.** Detail below.

## The brief, checked claim by claim

The reel was commissioned with a concept summary. Treating it as a claim set
rather than a script:

| Brief said | Verdict | What the reel says instead |
|---|---|---|
| "Traditional computers struggle to model chaotic real-world systems like weather and financial markets" | ⚠️ **MISLEADING AS A QUANTUM ARGUMENT** | Chaos is a property of the system, not a hardware limitation. Sensitive dependence on initial conditions bounds prediction regardless of the computer. A quantum computer does not repeal it. The reel does not claim quantum fixes chaotic forecasting |
| "Quantum AI uses qubits to recognize hidden patterns in massive data sets much faster than standard electronics" | ❌ **NOT SUPPORTED** | This is the least supported claim in the field. Two independent problems: classical data must be encoded into a quantum state, and that loading can cost what the algorithm saves (B04); and several headline QML speedups were **dequantized** — matched classically once someone wrote the classical algorithm (B05) |
| "Recent studies show combining quantum processing with AI dramatically improves prediction of complex events" | ⚠️ **DIRECTION REVERSED** | The strongest published result runs the other way: AlphaQubit, an AI decoder, improving a **quantum** processor's error correction. The reel reports that result with its measured numbers (B03) |
| "Could transform drug discovery and material science" | ✅ **SURVIVES** | And the reel says *why* it survives: simulating a quantum system with a quantum computer is the one case never dequantized, because the simulated thing is itself quantum. This is Feynman's original argument (B06) |
| "…and global supply-chain forecasting" | ❌ **DOES NOT SURVIVE** | Classical data, so it runs straight into question 2 (B06) |

Rather than drop the brief, the reel **keeps its subject and its two surviving
industries, and makes the correction the story.** That is a stronger video than
the original framing and an honest one.

## Verified figures used on screen

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B03 | AlphaQubit is a neural decoder for quantum error correction, published in Nature 2024 | ✓ PASS | Google DeepMind / Google Quantum AI, *Learning high-accuracy error decoding for quantum processors*, Nature |
| 2 | B03 | 6% better than tensor network decoding | ✓ PASS | Same |
| 3 | B03 | 30% better than correlated matching | ✓ PASS | Same |
| 4 | B03 | Held from 17 qubits (distance 3) to 241 | ✓ PASS | Same |
| 5 | B05 | In 2018 Ewin Tang produced a classical algorithm matching the quantum recommendation-systems algorithm | ✓ PASS | Tang, 2018 |
| 6 | B05 | The advantage came from assumptions on the input, not from quantum-ness | ✓ PASS | Same |
| 7 | B05 | She and co-authors dequantized a wider class of QML algorithms | ✓ PASS | 2019 follow-up work |
| 8 | B05 | Topological data analysis resisted dequantization | ✓ PASS | Same body of work — included so the beat does not overclaim |
| 9 | B07 | Willow, 105 qubits, first below-threshold error correction, 2024 | ✓ PASS | Google, 2024 |
| 10 | B07 | The 5-minutes-vs-10²⁵-years figure is random circuit sampling | ✓ PASS | The benchmark is chosen for classical hardness, not utility. Stated on screen as a caveat |
| 11 | B07 | IBM roadmap — 200 logical qubits 2029, 1,000 early 2030s | ✓ PASS | Published IBM roadmap |
| 12 | B07 | Google states real-world problems need on the order of a million qubits | ✓ PASS | Google roadmap commentary |

## Why the most quotable number carries a caveat

The 10²⁵-years comparison is the single most repeated figure in quantum
computing and the most misread. It describes random circuit sampling — a task
selected *because* classical machines find it hard, not because the output is
wanted. Quoting it bare would be technically true and practically deceptive, so
it appears on screen inside a caveat card rather than as a headline.

## Claims deliberately NOT made

- **No claim that quantum computing is overhyped or will fail.** The reel's
  verdict is "be excited about the right thing".
- **No timeline for practical advantage beyond published roadmaps.**
- **No claim about any specific drug, material or commercial result.**
- **No qubit-count comparison between vendors** — different architectures make
  raw counts non-comparable.
- **No claim that dequantization killed QML.** It constrained it, and one
  family resisted; the reel says both.
