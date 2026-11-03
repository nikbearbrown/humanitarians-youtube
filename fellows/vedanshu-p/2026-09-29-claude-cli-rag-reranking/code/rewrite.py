"""rewrite.py — the other refinement: fix the query, not the ranking.

THE RESULT THAT MOTIVATES THIS FILE. `rerank.py` measured a joint re-scorer over
the top-5 on six questions and it moved nothing: 0 promoted, 0 demoted. On one
question it could not have helped even in principle, because the answering
document was not in the top-5 at all.

That is the structural ceiling of re-ranking, and it is worth stating plainly:

    a re-ranker REORDERS a shortlist. It cannot RETRIEVE.
    whatever stage 1 missed, stage 2 never sees.

Which points at a different fix. If the shortlist is wrong, the thing to change
is what was searched for — the query — not the order of what came back.

WHAT IS REAL HERE: the retrieval, the ranks, the timings. Same encoder, same
index, same corpus; only the query text differs.

WHAT IS NOT: the rewrites are HAND-WRITTEN (see corpus.REWRITES). Chapter 9's
two named methods — HyDE and Rewrite-Retrieve-Read — both require a language
model, and this machine has none. This file measures what a better query buys.
It does not demonstrate a model producing one.
"""
import numpy as np

from corpus import QUESTIONS, REWRITES, chunks
from encoder import MiniLM
from rerank import TOP_K, build_index, rank_of, retrieve


def sweep(index, model):
    rows = []
    for q, gold_doc in QUESTIONS:
        rw = REWRITES[q]
        hits_a, _ = retrieve(q, index, model)
        hits_b, _ = retrieve(rw, index, model)
        rows.append({
            "q": q, "rw": rw, "gold": gold_doc,
            "before": rank_of(hits_a, gold_doc),
            "after": rank_of(hits_b, gold_doc),
            "top_before": hits_a[0]["id"],
            "top_after": hits_b[0]["id"],
        })
    return rows


if __name__ == "__main__":
    model = MiniLM()
    cs = chunks()
    index, _ = build_index(cs, model)

    print(f"corpus: {len(cs)} chunks   ·   top-{TOP_K}   ·   ranks are "
          f"document-level")
    print()
    print("the literal question, then the rewritten one")
    print()
    rows = sweep(index, model)
    for r in rows:
        print(f"  gold {r['gold']}")
        print(f"    literal : {r['q']}")
        print(f"              rank {r['before']}   top hit {r['top_before']}")
        print(f"    rewrite : {r['rw']}")
        print(f"              rank {r['after']}   top hit {r['top_after']}")
        if r["before"] is None and r["after"] is not None:
            print(f"              -> PULLED INTO THE SHORTLIST "
                  f"(re-ranking could never have done this)")
        elif (r["after"] or 99) < (r["before"] or 99):
            print(f"              -> promoted {r['before']} -> {r['after']}")
        elif (r["after"] or 99) > (r["before"] or 99):
            print(f"              -> DEMOTED {r['before']} -> {r['after']}")
        else:
            print(f"              -> unchanged")
        print()

    found_before = sum(1 for r in rows if r["before"] is not None)
    found_after = sum(1 for r in rows if r["after"] is not None)
    top1_before = sum(1 for r in rows if r["before"] == 1)
    top1_after = sum(1 for r in rows if r["after"] == 1)
    rescued = sum(1 for r in rows if r["before"] is None and r["after"] is not None)
    lost = sum(1 for r in rows if r["before"] is not None and r["after"] is None)

    print("totals")
    print(f"  answer present in the top-{TOP_K}:  {found_before}/{len(rows)}"
          f"  ->  {found_after}/{len(rows)}")
    print(f"  answer ranked first:         {top1_before}/{len(rows)}"
          f"  ->  {top1_after}/{len(rows)}")
    print(f"  rescued by the rewrite: {rescued}   lost by the rewrite: {lost}")
    print()
    print("the honest comparison, on this corpus")
    print("  re-ranking  : 0 promoted, 0 demoted, 0 rescued")
    print(f"  rewriting   : {rescued} rescued, "
          f"{top1_after - top1_before:+d} to first place")
    print()
    print("  a re-ranker reorders what it was handed.")
    print("  a rewrite changes what gets handed over.")
