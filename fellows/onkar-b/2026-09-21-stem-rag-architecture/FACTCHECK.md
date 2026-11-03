# FACTCHECK.md — hai-liam-rag-triangle ("Claude, Retrieved.")

DOUBLE-CHECK LAW: every claim the narration makes, checked before the render.
Anything that would date the video is stripped; anything illustrative is
labelled illustrative ON SCREEN, not just here.

| # | Claim (as narrated) | Verdict | Basis | Fix applied |
|---|---|---|---|---|
| 1 | "Large language models are frozen in time the day they finish training" | TRUE, with care | A trained model's weights are fixed after training; its parametric knowledge ends at its training cutoff. | Kept. No model name, no cutoff date on screen or in the voice — a dated number is exactly what ages a video. |
| 2 | "They have zero access to your private data" | TRUE as scoped | A base model with no connected tool/retrieval path cannot read private files. | Scoped in the visual: B00's output lines say "no connected source, no private index" — the claim is about the un-augmented path, not about products with connectors. |
| 3 | RAG = retrieve relevant text, then generate an answer conditioned on it | TRUE | This is the defining structure of retrieval-augmented generation: a retrieval step supplies context to a generation step at inference time. | Kept as the reel's spine (the RAG Triangle). |
| 4 | "No retraining anywhere in this loop" | TRUE | Retrieval augmentation happens at inference time; model weights are untouched. This is the load-bearing distinction of the episode, and the misconception B01 corrects. | Kept and stamped on screen in B02. |
| 5 | Vector search retrieves passages by similarity, not by keyword match | TRUE | Embedding-based retrieval ranks by vector similarity in an embedding space. | Simplified on screen to "search the private database" — the reel does not claim a specific similarity metric. |
| 6 | "Q3 revenue was $4M" / ChromaDB ledger | ILLUSTRATIVE — not a real company figure | Invented demonstration data. ChromaDB is a real open-source vector database; the ledger row is not real. | **On-screen note added** in B04: "Illustrative figures — a demonstration ledger, not a real company's numbers." Narration says "a ChromaDB ledger", never "our ledger" or a named company. |
| 7 | Context poisoning: wrong retrieved document → confident wrong answer | TRUE | A generator constrained to supplied context will faithfully render whatever that context says; retrieval error propagates into a fluent, wrong answer. This is the documented central failure mode of RAG systems. | Kept as the falsifiability beat. |
| 8 | B05's false figures ("$2.1M — a 12% decline") | ILLUSTRATIVE by construction | The beat's whole point is that these numbers are false. | Stamped on screen: "FLUENT. CONFIDENT. FALSE." No viewer can mistake it for data. |
| 9 | "The AI completely surrenders to the retrieved text" | TRUE as a claim about the designed behaviour | When the system prompt constrains generation to provided context, the context governs the answer. | Kept — it is the episode's takeaway, and B07 makes the viewer verify it by hand rather than take it on trust. |
| 10 | The B07 task will make a model answer "neon green" | VERIFIABLE BY THE VIEWER | This is the point of the scaffolded task: it is falsifiable in 30 seconds, by the viewer, at no cost. | Kept. Narration frames it as something to watch happen, not a guarantee. |

## Stripped to keep the video from dating

- No model version numbers or vendor comparisons in narration or on screen.
- No benchmark percentages, no "studies show", no retrieval-accuracy statistics.
- No claim about which vector database is best; ChromaDB appears once, as the
  example the script named, not as a recommendation.

## Register check (DOUBLE-CHECK LAW)

The source is the author's own script. It was not parroted: B00 was rewritten so
the narrator does not claim to be the author (see BUILD-LOG.md, deviation 1),
every body beat was rewritten to react to what is on screen rather than to
describe it, and the judgment lines ("the failure is upstream of the model,
which is exactly where nobody is looking") are additions in register, not
restatements of the source.
