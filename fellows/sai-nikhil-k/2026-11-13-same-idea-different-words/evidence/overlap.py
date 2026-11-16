#!/usr/bin/env python3
"""overlap.py — do Portals' three "cyclone" worlds share any words?

Ethan Mollick (One Useful Thing, 9 Nov 2026, "Fable 5.2 and Jagged AGI") says
three separate teams of agents built a cyclone of circling animals: reindeer,
manta rays, storks. Those three worlds are real (src/worlds/index.js). This asks
what a word-matching check would make of them.

Text: design/descriptions.json "texts" — the one-to-three-sentence description
of every world, as built (472 entries; 471 are in src/worlds/index.js and are
used here). Measure: TF-IDF vectors (scikit-learn, English stop words) and the
cosine of every pair:
    cos(a, b) = a . b / (|a| |b|)      — 0 when two texts share no content word.

usage: python3 -I overlap.py <path to a clone of emollick/ai-portals>
"""
import json
import re
import subprocess
import sys

import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

repo = sys.argv[1]
head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
src = open(f"{repo}/src/worlds/index.js").read()
ents = re.findall(r'\{ id: "([^"]+)", name: "([^"]+)", category: "([^"]+)".*?line: "([^"]*)"', src)
texts = json.load(open(f"{repo}/design/descriptions.json"))["texts"]
ids = [e[0] for e in ents]
assert all(i in texts for i in ids)
print(f"ai-portals @ {head}  ·  scikit-learn {sklearn.__version__}  ·  numpy {np.__version__}")
print(f"worlds in src/worlds/index.js: {len(ids)}  ·  descriptions: {len(texts)}")

THREE = ["reindeer-cyclone", "manta-cyclone", "stork-kettle-riso"]
names = {e[0]: (e[1], e[2], e[3]) for e in ents}
for k in THREE:
    print(f"  {k:18} {names[k][0]!r} ({names[k][1]})")
    print(f"      {texts[k]}")

vec = TfidfVectorizer(stop_words="english")
X = vec.fit_transform([texts[i] for i in ids])
S = cosine_similarity(X)
iu = np.triu_indices(len(ids), 1)
pairs = S[iu]
idx = {k: n for n, k in enumerate(ids)}
vocab = vec.get_feature_names_out()
print(f"pairs of worlds: {len(pairs)}")
print(f"pairs sharing at least one content word: {(pairs > 0).sum()} = {100 * (pairs > 0).mean():.1f}%")
print(f"mean pair cosine: {pairs.mean():.4f}")
for a, b in [(THREE[0], THREE[1]), (THREE[0], THREE[2]), (THREE[1], THREE[2])]:
    shared = sorted(set(X[idx[a]].indices) & set(X[idx[b]].indices))
    print(f"cyclone pair {a} ~ {b}: cosine {S[idx[a], idx[b]]:.3f}, shared words {[vocab[j] for j in shared]}")
    # the dot product by hand, term by term, so the zero is not just a library's say-so
    va, vb = X[idx[a]].toarray().ravel(), X[idx[b]].toarray().ravel()
    print(f"    a.b = {float(va @ vb):.6f}  |a| = {np.linalg.norm(va):.4f}  |b| = {np.linalg.norm(vb):.4f}")
cyc = [S[idx[a], idx[b]] for a, b in [(THREE[0], THREE[1]), (THREE[0], THREE[2]), (THREE[1], THREE[2])]]
print(f"cyclone pairs sharing a word: {sum(c > 0 for c in cyc)} of 3")

# the short captions (index.js `line`) for comparison: there the word "cyclone" is shared
capX = TfidfVectorizer(stop_words="english").fit_transform([names[i][2] for i in ids])
capS = cosine_similarity(capX)
print("captions instead of descriptions: reindeer~manta cosine "
      f"{capS[idx[THREE[0]], idx[THREE[1]]]:.3f} (both captions say 'cyclone'); "
      f"pairs sharing a word {100 * (capS[iu] > 0).mean():.1f}%")
