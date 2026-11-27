"""A bigram model learns which word follows which -- not which statements are true."""
from collections import Counter, defaultdict
text = ("paris is the capital of france . "
        "berlin is the capital of germany . "
        "rome is the capital of italy .")
w = text.split()
nxt = defaultdict(Counter)
for a, b in zip(w, w[1:]):
    nxt[a][b] += 1
total = sum(nxt["of"].values())
for word, c in nxt["of"].most_common():
    print(f"P({word} | 'of') = {c/total:.2f}")
