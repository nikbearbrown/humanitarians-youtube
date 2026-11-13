"""rag_demo.py — the real retrieval step shown in beat B05 of "What Is RAG?".

Splits the example syllabus into one chunk per section, scores every chunk
against the question with TF-IDF cosine similarity (pure standard library, no
model, no key), and prints the top three. The output is saved to
retrieval_output.json and its numbers go into the beat sheet as props.

Run:  python3 rag_demo.py
"""
import json
import math
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
QUESTION = "Can I submit Lab 3 late?"
STOP = set("a an and are be can for from i if in is it may of on or the to you your with after each".split())


def tokens(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    # crude plural folding so "labs" matches "lab"
    return [w[:-1] if len(w) > 3 and w.endswith("s") else w for w in words if w not in STOP]


def chunks(md):
    out = []
    for block in re.split(r"\n(?=## )", md):
        m = re.match(r"## (\d+)\. (.+)\n(.+)", block.strip(), re.S)
        if m:
            out.append({"section": f"§{m.group(1)} {m.group(2)}", "text": m.group(3).strip()})
    return out


def tfidf(docs):
    n = len(docs)
    df = Counter(t for d in docs for t in set(d))
    idf = {t: math.log((1 + n) / (1 + c)) + 1 for t, c in df.items()}
    return idf, [{t: c * idf[t] for t, c in Counter(d).items()} for d in docs]


def cosine(a, b):
    dot = sum(v * b.get(t, 0.0) for t, v in a.items())
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def main():
    cs = chunks((HERE / "syllabus.md").read_text())
    idf, vecs = tfidf([tokens(c["text"]) for c in cs])
    q = {t: c * idf.get(t, 0.0) for t, c in Counter(tokens(QUESTION)).items()}
    ranked = sorted(
        ({**c, "score": round(cosine(q, v), 3)} for c, v in zip(cs, vecs)),
        key=lambda r: r["score"], reverse=True)
    top = ranked[:3]
    result = {"question": QUESTION, "method": "TF-IDF cosine (keyword search)",
              "chunks_searched": len(cs), "top3": top}
    (HERE / "retrieval_output.json").write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f'Question: {QUESTION}   ({len(cs)} chunks searched)')
    for i, r in enumerate(top, 1):
        print(f'{i}. {r["score"]:.3f}  {r["section"]}: {r["text"]}')


if __name__ == "__main__":
    main()
