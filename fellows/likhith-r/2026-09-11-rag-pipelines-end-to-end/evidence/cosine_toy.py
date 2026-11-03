"""Toy cosine-similarity retrieval for B06 (claude-hai-rag-pipelines).

The 2-D vectors are CONSTRUCTED for illustration (real embeddings have hundreds
of dimensions); the similarity scores shown on screen are computed here, not typed.
Run: python3 evidence/cosine_toy.py > evidence/cosine_toy.out.txt
"""
import math

question = ("Can I get my money back?", (0.90, 0.35))
chunks = [
    ("Refunds within 30 days.",      (0.95, 0.25)),
    ("Returns need a receipt.",      (0.80, 0.55)),
    ("Shipping takes 3–5 days.",     (0.35, 0.90)),
    ("Office hours: 9 to 5.",        (-0.20, 0.95)),
]
K = 2

def cos(a, b):
    dot = a[0] * b[0] + a[1] * b[1]
    return dot / (math.hypot(*a) * math.hypot(*b))

q = question[1]
scored = sorted(((cos(q, v), text, v) for text, v in chunks), reverse=True)
print(f"question: {question[0]!r} -> {q}")
for rank, (s, text, v) in enumerate(scored, 1):
    tag = "RETRIEVED" if rank <= K else "-"
    print(f"{rank}. cos={s:.2f}  {v}  {text!r}  {tag}")
