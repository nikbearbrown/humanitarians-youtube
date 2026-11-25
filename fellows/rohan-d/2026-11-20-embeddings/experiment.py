"""Every number the embeddings film shows (pure numpy; deterministic)."""
import numpy as np
V = {"cat": np.array([4.0, 1.0]), "dog": np.array([3.0, 2.0]), "car": np.array([1.0, 4.0])}
V["cat x3"] = 3 * V["cat"]
def dist(a, b): return float(np.linalg.norm(a - b))
def cos(a, b): return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
def ang(a): return float(np.degrees(np.arctan2(a[1], a[0])))
for k, v in V.items(): print(k, v.tolist(), "length", round(float(np.linalg.norm(v)), 3), "angle", round(ang(v), 2))
c = V["cat"]
for k in ("dog", "car", "cat x3"):
    print(f"cat vs {k}: distance {dist(c, V[k]):.3f}  cosine {cos(c, V[k]):.4f}  angle {abs(ang(c) - ang(V[k])):.2f}")
print("dog vs car: cosine", round(cos(V["dog"], V["car"]), 4), "angle", round(abs(ang(V['dog']) - ang(V['car'])), 2))
print("cat . dog =", float(c @ V["dog"]), " |cat| |dog| =", round(float(np.linalg.norm(c) * np.linalg.norm(V["dog"])), 3))
print("cat . car =", float(c @ V["car"]))
with np.errstate(all="ignore"):
    z = np.zeros(2)
    print("zero vector cosine:", cos(c, z))
