"""Tiny retrieval step of RAG: score each passage against the question with TF-IDF cosine similarity."""
import math, re
from collections import Counter
docs = {
    "ch3 projectile": "a projectile follows a parabola its range depends on launch angle and speed",
    "ch5 circular": "circular motion needs a centripetal acceleration toward the center",
    "ch1 units": "physics uses si units such as metres seconds and kilograms",
    "ch7 energy": "kinetic energy grows with the square of speed"
}
query = ("what launch angle gives a projectile "
         "the longest range")
tok = lambda s: re.findall(r"[a-z]+", s.lower())
N = len(docs)
df = Counter(t for d in docs.values() for t in set(tok(d)))
idf = {t: math.log((N + 1) / (df[t] + 1)) + 1
       for t in df}
def vec(s):
    tf = Counter(t for t in tok(s) if t in idf)
    return {t: c * idf[t] for t, c in tf.items()}
def cos(a, b):
    dot = sum(a[t] * b.get(t, 0) for t in a)
    # ... divided by both vector lengths ...
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0
q = vec(query)
for name, text in sorted(docs.items(), key=lambda kv: -cos(q, vec(kv[1]))):
    print(f"{name}: {cos(q, vec(text)):.2f}")
