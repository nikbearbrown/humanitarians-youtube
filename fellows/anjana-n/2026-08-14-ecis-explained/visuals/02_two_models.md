# Beat 2 — Two Models

**Visual type:** Remotion
**Duration:** ~15 seconds

## What the viewer sees

Starting from the zoomed-out view at the end of Beat 1. The LLM reader node is now in focus.

**Split animation (0-4s):** The single LLM node divides cleanly down the middle into two parallel nodes. Left node: "Llama 3.1 8B" in purple. Right node: "Mistral 7B" in teal. Both sit at the same level, both connect to the same input (chunks from above) and the same output (triangulator below).

**Agreement example (4-8s):** A chunk card slides in from the left. It flows to both models simultaneously. Both process it (a brief loading pulse). Llama outputs "raised 0.85." Mistral outputs "raised 0.82." A green line connects them labeled "AGREE." The triangulator below absorbs both signals and outputs a single verdict: "raised 0.88" — confidence boosted.

**Disagreement example (8-13s):** A second chunk flows in. Llama outputs "maintained 0.71." Mistral outputs "raised 0.68." A red line connects them labeled "DISAGREE." The triangulator pulses differently — more deliberate — and outputs "raised 0.54" with a lower confidence and an amber indicator.

**Payoff (13-15s):** Both nodes settle side by side, pulsing steadily. A label appears below: "Two architectures. One triangulator."

## Technical notes

- The split animation is the signature moment of this episode — make it clean and satisfying
- Purple for Llama, teal for Mistral — keep these consistent throughout all beats
- The agreement/disagreement examples should feel fast and systematic, not dramatic
- Confidence numbers should be readable but not dominant — the flow is the point
- Reuse the triangulator node style from Episode 1
