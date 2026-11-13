"""bm25_search.py — sparse retrieval from scratch, run on both queries.

Cycle 1 of the CLI reel. BM25 exactly as Chapter 6 describes it: term frequency
weighted by inverse document frequency, with the two corrections that separate
BM25 from plain TF-IDF —

  * length normalisation (the `b` term), so a long passage does not win merely
    by containing more words, and
  * term-frequency saturation (the `k1` term), so a word appearing 50 times
    does not count 50 times as much as appearing once.

Tokenisation keeps hyphens inside a token, so "TR-114" survives as ONE term
rather than splitting into "tr" and "114". That matters: the whole reason sparse
retrieval wins query 1 is that "tr-114" occurs in exactly one passage, which
gives it the highest possible IDF in this collection.
"""
import math
import re

from corpus import GOLD, PASSAGES, QUERIES

K1 = 1.5
B = 0.75
TOKEN = re.compile(r"[a-z0-9][a-z0-9\-]*")


def tokenize(text: str):
    return TOKEN.findall(text.lower())


class BM25:
    def __init__(self, passages: dict):
        self.ids = list(passages)
        self.docs = [tokenize(passages[i]) for i in self.ids]
        self.lens = [len(d) for d in self.docs]
        self.avgdl = sum(self.lens) / len(self.lens)
        self.N = len(self.docs)
        self.tf = [{t: d.count(t) for t in set(d)} for d in self.docs]
        self.df = {}
        for d in self.docs:
            for t in set(d):
                self.df[t] = self.df.get(t, 0) + 1

    def idf(self, term: str) -> float:
        n = self.df.get(term, 0)
        # Robertson/Spärck Jones IDF: rare terms score far higher than common ones
        return math.log(1 + (self.N - n + 0.5) / (n + 0.5))

    def score(self, query: str, doc_i: int) -> float:
        s = 0.0
        norm = K1 * (1 - B + B * self.lens[doc_i] / self.avgdl)
        for t in tokenize(query):
            f = self.tf[doc_i].get(t, 0)
            if f:
                s += self.idf(t) * (f * (K1 + 1)) / (f + norm)
        return s

    def search(self, query: str, k: int = 3):
        scored = [(self.ids[i], self.score(query, i)) for i in range(self.N)]
        scored.sort(key=lambda r: -r[1])
        return scored[:k]


if __name__ == "__main__":
    bm25 = BM25(PASSAGES)
    print(f"BM25 sparse retrieval · {len(PASSAGES)} passages · k1={K1} b={B}")
    print(f"gold passage for both queries: {GOLD}\n")

    for kind, q in QUERIES:
        hits = bm25.search(q)
        top = hits[0][0]
        print(f"[{kind}] {q}")
        for rank, (pid, sc) in enumerate(hits, 1):
            mark = "  <- gold" if pid == GOLD else ""
            print(f"   {rank}. {pid}  {sc:6.3f}{mark}")
        print(f"   => {'HIT' if top == GOLD else 'MISS'} (top-1 = {top})\n")
