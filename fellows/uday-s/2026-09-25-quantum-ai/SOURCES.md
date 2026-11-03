# SOURCES — The Arrow Points The Other Way

A topic explainer on quantum AI. The field is unusually prone to headline
figures that are true in a narrow technical sense and misleading in plain
reading, so the standard here is: every number names a published result, and
the one famous benchmark that is routinely misread is shown with its caveat
attached rather than quoted bare.

| On screen | Beat | Source |
|---|---|---|
| AlphaQubit — neural decoder for quantum error correction | B03 | Google DeepMind / Google Quantum AI, *Learning high-accuracy error decoding for quantum processors*, **Nature, 2024** |
| 6% better than tensor network decoding | B03 | same |
| 30% better than correlated matching | B03 | same |
| held from 17 qubits (distance 3) to 241 | B03 | same |
| classical data must be encoded into a quantum state before a quantum algorithm runs | B04 | standard state-preparation / data-loading argument in the QML literature |
| Ewin Tang, 2018 — a classical algorithm matching quantum recommendation systems | B05 | Tang, 2018 |
| the advantage came from input assumptions, not quantum-ness | B05 | same |
| a wider class of QML algorithms dequantized | B05 | Tang et al., 2019 |
| topological data analysis resisted | B05 | same body of work |
| Willow — 105 qubits, first below-threshold error correction, 2024 | B07 | Google, *Quantum error correction below the surface code threshold* |
| 5 min vs 10²⁵ years **is random circuit sampling** | B07 | Google Willow benchmark; shown on screen with the caveat |
| IBM — 200 logical qubits 2029, 1,000 early 2030s | B07 | published IBM roadmap |
| Google — real-world problems need ~1M qubits | B07 | Google roadmap commentary |

## Reference links

- AlphaQubit, Nature — https://www.nature.com/articles/s41586-024-08148-8
- Below the surface code threshold, Nature — https://www.nature.com/articles/s41586-024-08449-y
- Dequantizing algorithms to understand quantum advantage in ML, Nature Reviews Physics — https://www.nature.com/articles/s42254-022-00511-w
- Ewin Tang, thesis and talks — https://ewintang.com/

## Precision notes

- **"Dequantized" is explained, never used as jargon.** The beat says what
  happened: someone wrote a classical algorithm that matched it.
- **The dequantization beat does not overclaim.** It states that one family —
  topological data analysis — resisted, because saying "all QML was
  dequantized" would be false.
- **Roadmap dates are attributed to the vendor publishing them**, not stated as
  industry consensus.
- **No qubit counts are compared across vendors.** Architectures differ enough
  that raw counts are not comparable, and the reel does not imply they are.

## Claims deliberately NOT made

- **No claim that chaotic systems become predictable with quantum hardware.**
  Chaos bounds prediction regardless of the computer; the commissioning brief
  implied otherwise and the reel does not repeat it.
- **No claim of quantum advantage on any machine-learning task with real
  data.** None has been demonstrated.
- **No commercial or product claim**, and no named drug, material or customer.
- **No position on whether quantum computing will succeed overall.** The reel
  is scoped to what a viewer should believe about *quantum plus AI*, today.
