"""Toy, deterministic comparison behind claude-hai-rag-vs-okf (B03, B06).

RAG half: a raw pile of documents is split into sentence chunks, each chunk becomes a
bag-of-words vector (a stand-in for a learned embedding; no model, no network), and at
query time the chunks are ranked by cosine similarity to the question; top-k return.

OKF half: the agent opens okf_bundle/index.md and follows Markdown links into the
concept files it needs, reading each file whole. No vectors are built.
"""
import math, re, sys, hashlib
from collections import Counter
from pathlib import Path

PILE = {
    "meeting-notes.txt": "Q3 sync. Revenue was up again. Finance says revenue only counts paid orders. Refunds went down.",
    "support-faq.txt": "Customers can get a refund within 30 days. Refunded orders keep their row.",
    "slack-export.txt": "Is revenue gross or net? I think we subtract refunds. Ask finance.",
    "onboarding.txt": "Orders live in the orders table. Each order has an amount and a status.",
}
QUERY = "How is revenue calculated?"
K = 3
STOP = {"is", "how", "the", "a", "an", "we", "i", "and", "or", "in", "of", "their", "each", "has", "only", "was", "up", "can", "get", "within", "ask", "think", "says", "live", "keep"}

def tokens(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP]

def stem(w):
    return w[:-1] if w.endswith("s") and len(w) > 3 else w

def vec(s):
    return Counter(stem(w) for w in tokens(s))

def cos(a, b):
    dot = sum(a[k] * b[k] for k in a)
    na = math.sqrt(sum(v * v for v in a.values())); nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0

out = []
chunks = [(doc, c.strip()) for doc, text in PILE.items() for c in re.split(r"(?<=[.?!])\s+", text) if c.strip()]
out.append(f"RAG: {len(PILE)} raw docs -> {len(chunks)} chunks -> {len(chunks)} vectors")
q = vec(QUERY)
ranked = sorted(((cos(q, vec(c)), d, c) for d, c in chunks), key=lambda r: (-r[0], r[1], r[2]))
out.append(f"query: {QUERY!r}  top-{K} by cosine:")
for s, d, c in ranked[:K]:
    out.append(f"  {s:.2f}  {d}: {c}")

bundle = Path(__file__).parent / "okf_bundle"
link = re.compile(r"\]\(([^)]+\.md)\)")
path = ["index.md", "metrics/revenue.md"]
seen = list(path)
for l in link.findall((bundle / "metrics/revenue.md").read_text()):
    p = (bundle / "metrics" / l).resolve().relative_to(bundle.resolve()).as_posix()
    if p not in seen: seen.append(p)
total = len(list(bundle.rglob("*.md")))
out.append(f"OKF: {total} files, 0 vectors; agent walk for the same question:")
for p in seen:
    fm = (bundle / p).read_text().split("---")[1] if p != "index.md" else ""
    t = re.search(r"type: (.+)", fm)
    out.append(f"  open {p}" + (f"  (type: {t.group(1)})" if t else ""))
out.append(f"  read {len(seen)} of {total} files, whole; 0 embeddings")
text = "\n".join(out)
print(text)
print("sha256", hashlib.sha256(text.encode()).hexdigest()[:16])
