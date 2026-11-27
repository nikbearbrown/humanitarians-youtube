"""Softmax with temperature over four candidate next words for 'The cat sat on the ...'."""
import math
logits = {"mat": 3.0, "sofa": 2.0, "roof": 1.2, "moon": 0.2}
for T in (0.5, 1.0, 2.0):
    exps = {w: math.exp(z / T) for w, z in logits.items()}
    total = sum(exps.values())
    print(f"T={T}: " + "  ".join(f"{w}={exps[w]/total:.2f}" for w in logits))
