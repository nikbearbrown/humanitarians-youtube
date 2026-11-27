"""Byte-pair encoding on a toy corpus: count adjacent pairs, merge the most frequent, repeat."""
from collections import Counter
corpus = {"low": 5, "lower": 2,
          "newest": 6, "widest": 3}
words = {tuple(w) + ("</w>",): n for w, n in corpus.items()}
for step in range(1, 5):
    pairs = Counter()
    for sym, n in words.items():
        for a, b in zip(sym, sym[1:]):
            pairs[(a, b)] += n
    (a, b), count = pairs.most_common(1)[0]
    # ... merge every (a, b) into one symbol ...
    merged = {}
    for sym, n in words.items():
        out, i = [], 0
        while i < len(sym):
            if i < len(sym) - 1 and sym[i] == a and sym[i + 1] == b:
                out.append(a + b); i += 2
            else:
                out.append(sym[i]); i += 1
        merged[tuple(out)] = n
    words = merged
    print(f"merge {step}: {a}+{b} -> {a+b}  ({count}x)")
print("newest ->", " ".join(next(s for s in words if "".join(s).startswith("newest"))))
