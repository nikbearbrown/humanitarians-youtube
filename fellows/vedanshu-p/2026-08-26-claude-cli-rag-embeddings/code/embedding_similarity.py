"""Cycle 2: retrieve the same FAQ passage using real sentence embeddings.

Same query, same six passages, same top-1 task as naive_similarity.py.
The only change is *how* similarity is measured: instead of counting
shared words, each passage and the query are encoded with a real,
free, locally-run Sentence-BERT model (Reimers & Gurevych, 2019) —
no API key, no paid service.

    pip install sentence-transformers

downloads the small "all-MiniLM-L6-v2" model (~90MB) once from
Hugging Face's public model hub and caches it locally.
"""

from sentence_transformers import SentenceTransformer
import numpy as np

from naive_similarity import PASSAGES, QUERY, word_overlap

MODEL_NAME = "all-MiniLM-L6-v2"


def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def main():
    model = SentenceTransformer(MODEL_NAME)

    print(f"query: {QUERY!r}\n")

    texts = [text for _, text in PASSAGES]
    passage_embeddings = model.encode(texts)
    query_embedding = model.encode(QUERY)

    ranked = sorted(
        (
            (cosine(query_embedding, emb), pid)
            for (pid, _), emb in zip(PASSAGES, passage_embeddings)
        ),
        reverse=True,
    )

    print(f"ranked by cosine similarity ({MODEL_NAME} embeddings):")
    for score, pid in ranked:
        print(f"  {score:.3f}  {pid}")
    top_score, top_id = ranked[0]
    print(f"\ntop match: {top_id} (score {top_score:.3f})")

    naive_score = word_overlap(QUERY, dict(PASSAGES)["IT-01"])
    print(f"\nfor comparison - cycle 1's word-overlap score was highest for "
          f"IT-01 ({naive_score:.3f}), because the query and IT-01 both "
          f"contain the literal phrase \"how do i request\". Embeddings "
          f"aren't fooled by the shared phrase; they rank by meaning.")


if __name__ == "__main__":
    main()
