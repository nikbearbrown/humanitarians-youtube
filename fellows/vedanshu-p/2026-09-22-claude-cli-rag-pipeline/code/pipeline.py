"""pipeline.py — the five stages, end to end, traced on one question.

Cycle 1 of the CLI reel. Chapter 7's breakdown is ingest -> embed -> retrieve ->
augment -> generate, and the chapter's claim is that each stage is "a distinct
place where something concrete happens, and therefore a distinct place where
something can go wrong."

So each stage is ONE function with ONE return value, and the trace prints what
each one handed to the next: documents -> chunks -> vectors -> retrieved chunks
-> prompt -> answer. If the stages were tangled, the trace could not be printed
this way, and Chapter 7's diagnostic argument would not hold.

ABOUT THE GENERATE STAGE — READ THIS BEFORE BELIEVING THE OUTPUT.
There is no language model here. `generate` is a deterministic EXTRACTIVE
reader: it can only quote a sentence that is physically present in the prompt's
CONTEXT block, and it cites the chunk it took the sentence from. That is a
stand-in for an LLM, and the reel says so out loud.

It is also the right stand-in for this particular chapter. A real LLM is
stochastic and can mask a retrieval fault by guessing correctly from prior
knowledge; this reader cannot guess at all. That makes it a CONTROL: when the
answer is wrong here, the fault is provably upstream, which is exactly the
property Chapter 7's diagnostic map depends on. Chapter 8 is where prompt
construction and a real generator get their due.
"""
import re

import numpy as np

from corpus import DOCUMENTS, GOLD_DOC, QUESTION
from encoder import MiniLM

TOP_K = 3
STOP = {"how", "many", "do", "i", "get", "in", "my", "a", "the", "of", "is", "are",
        "what", "for", "to", "and", "on", "at", "per", "you", "your"}


# ── stage 1 · INGEST ────────────────────────────────────────────────────────
def ingest(documents: dict) -> list:
    """Documents -> addressable chunks. Split on paragraph breaks (Chapter 4)."""
    chunks = []
    for doc_id, text in documents.items():
        for i, para in enumerate(p.strip() for p in text.split("\n\n")):
            if para:
                chunks.append({"id": f"{doc_id}#{i}", "doc": doc_id, "para": i,
                               "text": para})
    return chunks


# ── stage 2 · EMBED ─────────────────────────────────────────────────────────
def embed(chunks: list, model: MiniLM) -> dict:
    """Chunks -> a searchable index. Vectors are L2-normalised."""
    return {"chunks": chunks, "vectors": model.encode([c["text"] for c in chunks])}


# ── stage 3 · RETRIEVE ──────────────────────────────────────────────────────
def retrieve(question: str, index: dict, model: MiniLM, k: int = TOP_K) -> list:
    """Question -> a short list of chunks. Embedded by the SAME model (Ch. 3)."""
    q = model.encode([question])[0]
    sims = index["vectors"] @ q
    order = np.argsort(-sims)[:k]
    return [dict(index["chunks"][i], score=float(sims[i])) for i in order]


# ── stage 4 · AUGMENT ───────────────────────────────────────────────────────
def augment(question: str, hits: list, label_chunks: bool = True) -> str:
    """Question + chunks + instruction -> ONE prompt string."""
    lines = ["Answer using ONLY the context below. Cite the chunk id you used.",
             "", "CONTEXT:"]
    for h in hits:
        lines.append(f"[{h['id']}] {h['text']}" if label_chunks else h["text"])
    lines += ["", f"QUESTION: {question}", "ANSWER:"]
    return "\n".join(lines)


# ── stage 5 · GENERATE ──────────────────────────────────────────────────────
def generate(prompt: str, use_context: bool = True) -> dict:
    """Prompt -> answer. Deterministic extractive reader — NOT a language model.

    Scores every context sentence by overlap with the question's content words
    and returns the best one verbatim, with the chunk id it came from. It cannot
    produce a sentence that is not in the prompt.
    """
    if not use_context:
        # The 'hallucinating generator' fault: answer from a prior, ignore context.
        return {"answer": "You get 20 vacation days in your first year.",
                "cited": None, "grounded": False}

    body = prompt.split("CONTEXT:", 1)[1].split("QUESTION:", 1)[0]
    question = prompt.split("QUESTION:", 1)[1].split("ANSWER:", 1)[0].strip()
    keys = {w for w in re.findall(r"[a-z]+", question.lower()) if w not in STOP}

    best, best_score, best_id = None, -1.0, None
    for block in [b for b in body.strip().split("\n") if b.strip()]:
        m = re.match(r"\[([^\]]+)\]\s*(.*)", block)
        cid, text = (m.group(1), m.group(2)) if m else (None, block)
        for sent in re.split(r"(?<=\.)\s+", text):
            words = set(re.findall(r"[a-z]+", sent.lower()))
            score = len(keys & words) + (0.5 if re.search(r"\d", sent) else 0)
            if score > best_score:
                best, best_score, best_id = sent.strip(), score, cid

    return {"answer": best or "Not found in the provided context.",
            "cited": best_id, "grounded": True}


def run(question: str, model: MiniLM, documents: dict = DOCUMENTS):
    chunks = ingest(documents)
    index = embed(chunks, model)
    hits = retrieve(question, index, model)
    prompt = augment(question, hits)
    result = generate(prompt)
    return chunks, index, hits, prompt, result


if __name__ == "__main__":
    model = MiniLM()
    chunks, index, hits, prompt, result = run(QUESTION, model)

    n_vecs, dim = index["vectors"].shape
    rows = [
        ("ingest",   f"{len(chunks)} chunks",        f"{len(DOCUMENTS)} documents -> paragraph chunks"),
        ("embed",    f"{n_vecs}x{dim} index",        "chunks -> vectors (all-MiniLM-L6-v2)"),
        ("retrieve", f"top-{TOP_K} chunks",          "query vector -> nearest chunks"),
        ("augment",  f"{len(prompt)}-char prompt",   "question + chunks + instruction -> prompt"),
        ("generate", "1 answer",                     "prompt -> answer (extractive reader)"),
    ]

    print(f"QUESTION: {QUESTION}\n")
    print(f"{'stage':<10} {'out':<20} {'what moved':<44}")
    for stage, out, moved in rows:
        print(f"{stage:<10} {out:<20} {moved:<44}")
        if stage == "retrieve":
            for h in hits:
                print(f"{'':<10}   {h['id']:<10} {h['score']:.3f}")
    print()
    print(f"ANSWER: {result['answer']}")
    print(f"CITED : {result['cited']}   (gold document: {GOLD_DOC})")
