"""diagnose.py — break exactly one stage, and see whether the symptom names it.

Cycle 2 of the CLI reel: the revision. Chapter 7's real payoff is not that the
pipeline works — it is that the pipeline is a DIAGNOSTIC MAP:

    "if the final answer cites the wrong number, the bug could be in retrieval
     (wrong chunk came back), in augmentation (the right chunk came back but was
     formatted or labeled poorly), or in generation (the right chunk came back
     and was assembled correctly, but the model still made something up) —
     three different problems with three different fixes"

That is a testable claim, so this script tests it. Each run injects ONE fault,
holds every other stage identical, and records three observable signals:

    answer      what came back
    cited       which chunk it claimed
    grounded    was the answer physically present in the prompt's context?

The claim survives only if the three faults produce three DIFFERENT signatures.
If two faults looked the same, the pipeline would not localise a bug and
Chapter 7's map would be decoration.

The deterministic reader (see pipeline.py) is what makes this measurable: it
cannot accidentally guess the right answer, so a wrong answer always has a
traceable upstream cause.
"""
from corpus import DOCUMENTS, GOLD_DOC, GOLD_FACT, QUESTION
from encoder import MiniLM
from pipeline import TOP_K, augment, embed, generate, ingest, retrieve


def retrieve_wrong(question, index, model, k=TOP_K):
    """FAULT (retrieve): a filter bug that skips the gold document entirely."""
    full = retrieve(question, index, model, k=len(index["chunks"]))
    return [h for h in full if h["doc"] != GOLD_DOC][:k]


def trace(label, index, model, *, broken_retrieve=False, labels=True, context=True):
    hits = (retrieve_wrong if broken_retrieve else retrieve)(QUESTION, index, model)
    prompt = augment(QUESTION, hits, label_chunks=labels)
    out = generate(prompt, use_context=context)
    return {
        "label": label,
        "answer": out["answer"],
        "cited": out["cited"],
        "grounded": out["grounded"],
        "has_fact": GOLD_FACT in out["answer"],
        "top": hits[0]["id"],
    }


if __name__ == "__main__":
    model = MiniLM()
    index = embed(ingest(DOCUMENTS), model)

    runs = [
        trace("none (healthy)", index, model),
        trace("retrieve", index, model, broken_retrieve=True),
        trace("augment", index, model, labels=False),
        trace("generate", index, model, context=False),
    ]

    print(f"one question, one fault at a time · gold = {GOLD_DOC} · fact = \"{GOLD_FACT} days\"\n")
    print(f"{'stage broken':<16} {'top chunk':<11} {'fact?':<6} {'cited':<11} {'grounded':<9}")
    for r in runs:
        print(f"{r['label']:<16} {r['top']:<11} "
              f"{('yes' if r['has_fact'] else 'NO'):<6} "
              f"{str(r['cited']):<11} {('yes' if r['grounded'] else 'NO'):<9}")

    print("\nwhat each fault actually returned:")
    for r in runs:
        print(f"  [{r['label']}] {r['answer']}")

    # The claim under test: do the three faults have three distinct signatures?
    sigs = {r["label"]: (r["has_fact"], r["cited"] is not None, r["grounded"])
            for r in runs if r["label"] != "none (healthy)"}
    distinct = len(set(sigs.values())) == len(sigs)
    print(f"\nsignatures: " + " · ".join(f"{k}={v}" for k, v in sigs.items()))
    print(f"all three distinguishable: {'YES' if distinct else 'NO'}")
