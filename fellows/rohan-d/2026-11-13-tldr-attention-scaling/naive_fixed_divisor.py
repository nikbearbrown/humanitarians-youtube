"""NAIVE beat: 'just divide by a fixed number (10)'. Same seed/setup as experiment.py."""
import numpy as np
rng = np.random.default_rng(7)
def softmax(x):
    e = np.exp(x - x.max(-1, keepdims=True)); return e / e.sum(-1, keepdims=True)
print("fixed divisor 10 | sqrt(d_k) divisor   (mean largest softmax weight over 20000 trials, 6 keys)")
for d in (4, 16, 64, 512, 2048):
    q = rng.standard_normal((20000, 1, d)); k = rng.standard_normal((20000, 6, d))
    s = (q * k).sum(-1)
    print(f"d_k={d:>5}: std/10={s.std()/10:6.2f} maxw={softmax(s/10).max(-1).mean():.3f} | std/sqrt(d)={s.std()/np.sqrt(d):5.2f} maxw={softmax(s/np.sqrt(d)).max(-1).mean():.3f}")
print("uniform over 6 keys would be maxw=0.167")
