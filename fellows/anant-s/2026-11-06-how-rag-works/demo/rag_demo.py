#!/usr/bin/env python3
"""rag_demo.py — the executable evidence for show-tell-how-rag-works.

A tiny, deterministic retrieval-augmented-generation pipeline on a toy shop handbook:

    documents -> chunks -> embeddings -> vector store -> question embedded
    -> nearest chunks retrieved -> chunks placed into the prompt -> answer

Everything is local and exact: no model downloads, no APIs, no randomness.

  * Chunking   : one chunk per line of each document.
  * Embedding  : TF-IDF over the store's own vocabulary (lower-case words, a small stop-word
                 list, a crude plural/past-tense stemmer), L2-normalised. A toy stand-in for a
                 learned embedding model; it matches WORDS, not meaning.
  * Store      : a numpy matrix, one row per chunk. Search = cosine similarity (a dot product,
                 since rows are unit length), ranked high to low, ties broken by chunk order.
  * Prompt     : the top-2 chunks pasted above the question with a grounding instruction.
  * Answer     : a STAND-IN READER, not a language model: it copies the "<n> days" figure out of
                 the top-ranked chunk. It exists to show that the answer follows whatever was
                 retrieved. No LLM is run; the film labels the answer step as illustrated.

Three runs:
  A  the six-chunk handbook             -> the right chunk ranks first  -> "30 days"
  B  plus one outdated FAQ page         -> the stale chunk ranks first  -> "14 days" (wrong)
  C  the outdated page removed (the fix) -> identical to run A

Writes evidence.json and RUN-LOG.txt beside this file. Every number shown in the film comes
from evidence.json.
"""
import hashlib
import json
import platform
import re
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent

# ── the toy corpus (constructed for the film; one sentence per line) ─────────────────────
DOCS = {
    "returns.txt": [
        "Laptops can be returned within 30 days of purchase.",
        "Bring the receipt and the charger to the service desk.",
    ],
    "shipping.txt": [
        "Orders ship within two business days.",
        "Tracking numbers arrive by email.",
    ],
    "warranty.txt": [
        "Every laptop has a one year warranty.",
        "The warranty covers parts and repairs, but not water damage.",
    ],
}
STALE = {"faq-2019.txt": ["FAQ: How long do I have to return a laptop? 14 days."]}
QUESTION = "How long do I have to return a laptop?"
TOP_K = 2

STOP = set("""a an and are be but by can do does for from has have how i in is it its of on or
the this to was what when where which who why will with you your""".split())


# ── pipeline ───────────────────────────────────────────────────────────────────────────
def stem(w):
    """Crude, deterministic: returned->return, laptops->laptop, days->day. Leaves 'business'."""
    if len(w) > 4 and w.endswith("ed"):
        return w[:-2]
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def tokens(text):
    return [stem(w) for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP]


def chunk(docs):
    """One chunk per line, keeping its source document."""
    return [{"id": f"{name.split('.')[0]}#{i + 1}", "doc": name, "text": line}
            for name, lines in docs.items() for i, line in enumerate(lines)]


def build_store(chunks):
    """TF-IDF embeddings (smoothed idf, as in scikit-learn's default), L2-normalised rows."""
    toks = [tokens(c["text"]) for c in chunks]
    vocab = sorted({t for ts in toks for t in ts})
    index = {t: j for j, t in enumerate(vocab)}
    n = len(chunks)
    df = np.zeros(len(vocab))
    for ts in toks:
        for t in set(ts):
            df[index[t]] += 1
    idf = np.log((1 + n) / (1 + df)) + 1.0
    M = np.zeros((n, len(vocab)))
    for i, ts in enumerate(toks):
        for t in ts:
            M[i, index[t]] += 1
    M *= idf
    M /= np.linalg.norm(M, axis=1, keepdims=True)
    return {"vocab": vocab, "index": index, "idf": idf, "M": M}


def embed_query(store, text):
    v = np.zeros(len(store["vocab"]))
    unknown = []
    for t in tokens(text):
        if t in store["index"]:
            v[store["index"][t]] += 1
        else:
            unknown.append(t)          # a word the store has never seen gets no slot
    v *= store["idf"]
    nrm = np.linalg.norm(v)
    return (v / nrm if nrm else v), unknown


def search(store, chunks, qv):
    scores = store["M"] @ qv
    order = sorted(range(len(chunks)), key=lambda i: (-round(float(scores[i]), 12), i))
    return [{"rank": r + 1, "id": chunks[i]["id"], "doc": chunks[i]["doc"], "text": chunks[i]["text"],
             "score": round(float(scores[i]), 4)} for r, i in enumerate(order)]


def build_prompt(hits, question):
    notes = "\n".join(f"[{k + 1}] {h['text']} ({h['doc']})" for k, h in enumerate(hits))
    return ("Answer using only the notes below. If they don't say, say you don't know.\n\n"
            f"Notes:\n{notes}\n\nQuestion: {question}")


def stand_in_reader(hits):
    """NOT a language model. Copies the '<n> days' figure from the top-ranked chunk."""
    m = re.search(r"\b(\d+) days\b", hits[0]["text"])
    return {"answer": f"{m.group(1)} days" if m else "I don't know.",
            "cites": hits[0]["id"], "method": "stand-in reader: regex copy from the rank-1 chunk (no LLM)"}


def run(label, docs):
    chunks = chunk(docs)
    store = build_store(chunks)
    qv, unknown = embed_query(store, QUESTION)
    ranking = search(store, chunks, qv)
    top = ranking[:TOP_K]
    return {"label": label, "n_docs": len(docs), "n_chunks": len(chunks), "dims": len(store["vocab"]),
            "vocab": store["vocab"], "question_tokens": tokens(QUESTION), "question_unknown": unknown,
            "question_nonzero": int(np.count_nonzero(qv)),
            "ranking": ranking, "top_k": TOP_K, "prompt": build_prompt(top, QUESTION),
            "answer": stand_in_reader(top), "chunks": chunks}


def sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def main():
    A = run("A_handbook", DOCS)
    B = run("B_plus_stale_faq", {**DOCS, **STALE})
    C = run("C_stale_removed", DOCS)

    # ── self-checks: the claims the film makes from these runs ──
    assert A["n_docs"] == 3 and A["n_chunks"] == 6, "three documents, six chunks"
    assert A["ranking"][0]["id"] == "returns#1", "run A: the current returns chunk ranks first"
    assert A["answer"]["answer"] == "30 days"
    assert B["ranking"][0]["id"] == "faq-2019#1", "run B: the stale FAQ chunk ranks first"
    assert B["answer"]["answer"] == "14 days"
    assert B["ranking"][1]["id"] == "returns#1", "run B: the right chunk is pushed to second"
    assert C["ranking"] == A["ranking"] and C["answer"] == A["answer"], "run C restores run A"
    assert all(abs(np.linalg.norm(build_store(chunk(DOCS))["M"][i]) - 1) < 1e-12 for i in range(6))
    # determinism: a second build gives identical scores
    assert run("A2", DOCS)["ranking"] == A["ranking"]

    a_top, a_2nd = A["ranking"][0], A["ranking"][1]
    b_top, b_2nd = B["ranking"][0], B["ranking"][1]
    film = {
        "question": QUESTION,
        "n_docs": A["n_docs"], "n_chunks": A["n_chunks"], "dims": A["dims"],
        "A_top": {"id": a_top["id"], "score": a_top["score"], "text": a_top["text"]},
        "A_second": {"id": a_2nd["id"], "score": a_2nd["score"], "text": a_2nd["text"]},
        "A_answer": A["answer"]["answer"],
        "B_top": {"id": b_top["id"], "score": b_top["score"], "text": b_top["text"]},
        "B_second": {"id": b_2nd["id"], "score": b_2nd["score"], "text": b_2nd["text"]},
        "B_answer": B["answer"]["answer"],
        "A_right_score": a_top["score"], "B_right_score": b_2nd["score"], "B_stale_score": b_top["score"],
    }
    script = Path(__file__).read_bytes()
    ev = {
        "python": platform.python_version(), "numpy": np.__version__, "platform": platform.platform(),
        "script_sha256": hashlib.sha256(script).hexdigest(),
        "inputs_sha256": sha({"docs": DOCS, "stale": STALE, "question": QUESTION, "stop": sorted(STOP), "top_k": TOP_K}),
        "seed": None, "randomness": "none (fully deterministic)",
        "method": {"chunking": "one chunk per line", "embedding": "TF-IDF, idf = ln((1+N)/(1+df)) + 1, L2-normalised",
                   "similarity": "cosine (dot product of unit vectors)", "top_k": TOP_K,
                   "answer": "stand-in reader, regex copy from rank-1 chunk; no LLM"},
        "docs": DOCS, "stale": STALE, "film": film, "runs": {"A": A, "B": B, "C": C},
    }
    (HERE / "evidence.json").write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    L = [f"python {ev['python']} numpy {ev['numpy']} on {ev['platform']}",
         f"script sha256 {ev['script_sha256']}", f"inputs sha256 {ev['inputs_sha256']}", "",
         f"question: {QUESTION!r}"]
    for R in (A, B, C):
        L += ["", f"== run {R['label']}: {R['n_docs']} docs -> {R['n_chunks']} chunks -> {R['dims']}-number embeddings",
              f"   question tokens {R['question_tokens']}  (unknown to the store: {R['question_unknown'] or 'none'})"]
        for h in R["ranking"]:
            L.append(f"   #{h['rank']}  {h['score']:.4f}  {h['id']:<12} {h['text']}")
        L.append("   prompt:")
        L += ["     | " + ln for ln in R["prompt"].split("\n")]
        L.append(f"   answer ({R['answer']['method']}): {R['answer']['answer']}  [cites {R['answer']['cites']}]")
    L += ["", "all self-checks passed"]
    (HERE / "RUN-LOG.txt").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    sys.exit(main())
