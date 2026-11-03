"""rerank.py — retrieve broadly with a bi-encoder, then re-score the shortlist.

WHAT IS REAL HERE, AND WHAT IS NOT. Read this before trusting a number.

REAL:
  * Stage 1 is a genuine bi-encoder pass — all-MiniLM-L6-v2 weights, the real
    6-layer forward pass in numpy (encoder.py), mean-pooled and L2-normalised.
  * Stage 2 is a genuine JOINT scorer: it keeps the per-token vectors for the
    query and for each candidate and scores them against each other with MaxSim
    (for every query token, the best-matching document token; summed). The query
    and the document really do look at each other, token by token.
  * Every timing is measured on this machine with perf_counter.
  * The structural claim in `prove_query_independence` is checked, not asserted.

NOT A CROSS-ENCODER. Chapter 9's re-ranking section is specifically about
cross-encoders — a model that encodes the query and one document TOGETHER
through a network trained to emit a relevance score. No such checkpoint exists
in this machine's model cache, `transformers` is not installed, and there is no
network access, so this reel cannot run one. Rather than fake it, stage 2 uses
late interaction (MaxSim), which is a different and weaker thing:

  * a cross-encoder runs full attention ACROSS the pair, in a network fine-tuned
    on relevance labels;
  * MaxSim compares two independently-encoded token sequences afterwards.

MaxSim is the scoring function from ColBERT (Khattab & Zaharia, 2020), but this
is NOT ColBERT either: ColBERT TRAINS a model to produce token vectors suited to
that comparison. Here the function is applied off-label to a model trained for
mean-pooled sentence similarity. It is a legitimate, real, joint interaction —
and it is a weaker stand-in for the mechanism the chapter describes.

The 27% improvement the chapter cites is Nogueira & Cho's measurement of a
BERT cross-encoder on MS MARCO. It is NOT this reel's number and is never
presented as one.
"""
import time

import numpy as np

from corpus import GOLD_DOC, GOLD_PARA, QUESTION, QUESTIONS, chunks
from encoder import MiniLM

TOP_K = 5
GOLD = f"{GOLD_DOC}#{GOLD_PARA}"


def build_index(cs, model):
    """Stage-1 cost is paid ONCE for the whole corpus, before any query exists."""
    t0 = time.perf_counter()
    vecs = model.encode([c["text"] for c in cs])
    return {"chunks": cs, "vecs": vecs}, time.perf_counter() - t0


def retrieve(query, index, model, k=TOP_K):
    """Stage 1 — one query pass, then a dot product against every chunk."""
    t0 = time.perf_counter()
    q = model.encode([query])[0]
    scores = index["vecs"] @ q
    order = np.argsort(-scores)[:k]
    hits = [{"id": index["chunks"][i]["id"],
             "text": index["chunks"][i]["text"],
             "score": float(scores[i])} for i in order]
    return hits, time.perf_counter() - t0


def maxsim(q_tokens, d_tokens):
    """Late interaction: for each query token, its best match in the document.

    Both sides are L2-normalised, so the matrix product is cosine similarity.
    Summing the per-query-token maxima is ColBERT's MaxSim. Unlike a pooled dot
    product this score DEPENDS ON THE PAIR — a document has no single score until
    a query is supplied.
    """
    return float((q_tokens @ d_tokens.T).max(axis=1).sum())


def rerank(query, hits, model):
    """Stage 2 — re-score ONLY the shortlist, jointly."""
    t0 = time.perf_counter()
    qt = model.encode_tokens([query])[0]
    dts = model.encode_tokens([h["text"] for h in hits])
    out = []
    for h, dt in zip(hits, dts):
        out.append({**h, "rerank": maxsim(qt, dt) / max(1, qt.shape[0])})
    out.sort(key=lambda h: -h["rerank"])
    return out, time.perf_counter() - t0


def prove_query_independence(model, cs):
    """A bi-encoder's document vector cannot depend on the query. Check it.

    This is the structural reason re-ranking exists, and it is verifiable rather
    than rhetorical: encode the same document twice, in two different batches
    alongside two different queries, and compare the bytes.
    """
    doc = cs[0]["text"]
    a = model.encode([QUESTION, doc])[1]
    b = model.encode(["what is the parking policy", doc])[1]
    return float(np.abs(a - b).max())          # measured: 0.0


def rank_of(hits, gold_doc):
    """Document-level rank: the position of the first chunk from the right doc."""
    for i, h in enumerate(hits, 1):
        if h["id"].split("#")[0] == gold_doc:
            return i
    return None


def show(title, hits, key):
    print(f"  {title}")
    for i, h in enumerate(hits, 1):
        mark = "  <-- the answer" if h["id"] == GOLD else ""
        print(f"    {i}. {h['id']:10} {h[key]:6.3f}{mark}")


if __name__ == "__main__":
    model = MiniLM()
    cs = chunks()

    print("corpus")
    print(f"  {len(cs)} chunks, gold = {GOLD}")
    print()

    index, t_index = build_index(cs, model)
    print("stage 1 — bi-encoder, the whole corpus embedded once")
    print(f"  index built: {len(cs)} chunks in {t_index*1000:.0f} ms")
    print(f"  per chunk:   {t_index/len(cs)*1000:.1f} ms")
    print()

    drift = prove_query_independence(model, cs)
    print("the structural limit, checked (not asserted)")
    print("  same document, encoded beside two different queries")
    print(f"  max elementwise difference: {drift:.2e}")
    print("  the document vector does not know the query. that is the whole")
    print("  speed trick, and the whole blind spot.")
    print()

    # ── the sweep: every question, before and after ──────────────────────────
    print(f"re-ranking the top-{TOP_K}, on every question")
    print()
    print(f"  {'question':50} {'before':>6} {'after':>6}  effect")
    rows, t_pairs, n_pairs = [], 0.0, 0
    for q, gold_doc in QUESTIONS:
        hits, _ = retrieve(q, index, model)
        reranked, t_rr = rerank(q, hits, model)
        t_pairs += t_rr
        n_pairs += len(hits)
        b, a = rank_of(hits, gold_doc), rank_of(reranked, gold_doc)
        eff = ("promoted" if (a or 99) < (b or 99) else
               "demoted" if (a or 99) > (b or 99) else "unchanged")
        rows.append({"q": q, "gold": gold_doc, "before": b, "after": a, "eff": eff})
        short = q if len(q) <= 48 else q[:47] + "…"
        print(f"  {short:50} {str(b):>6} {str(a):>6}  {eff}")

    promoted = sum(1 for r in rows if r["eff"] == "promoted")
    demoted = sum(1 for r in rows if r["eff"] == "demoted")
    top1_before = sum(1 for r in rows if r["before"] == 1)
    top1_after = sum(1 for r in rows if r["after"] == 1)
    print()
    print("  totals")
    print(f"    answer already first before re-ranking: {top1_before}/{len(rows)}")
    print(f"    answer first after re-ranking:          {top1_after}/{len(rows)}")
    print(f"    promoted {promoted}   demoted {demoted}   "
          f"unchanged {len(rows)-promoted-demoted}")
    print()

    # ── the cost argument, on measured numbers only ──────────────────────────
    per_pair = t_pairs / max(1, n_pairs)
    print("why stage 2 only ever sees the shortlist")
    print(f"  measured joint pass: {per_pair*1000:.0f} ms per query-document pair")
    print(f"  on a {TOP_K}-chunk shortlist:   {per_pair*TOP_K*1000:.0f} ms")
    print(f"  on all {len(cs)} chunks:        {per_pair*len(cs)*1000:.0f} ms")
    print(f"  on 1,000,000 chunks:     {per_pair*1_000_000/3600:.1f} hours per query")
    print()
    print(f"  stage 1 embeds the corpus ONCE: {t_index*1000:.0f} ms total, and every")
    print(f"  later query costs one pass plus {len(cs)} dot products.")
