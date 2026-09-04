# FACTCHECK — "Claude, Nearest."

| Claim (beat) | Verdict | Source / derivation |
|---|---|---|
| Embedding models map text to vectors so similar meaning yields nearby vectors (B01/B02) | ✓ | Standard description of learned text embeddings (word2vec, sentence-transformers); trained via contrastive-style objectives |
| Nearest-neighbor search finds semantically related items regardless of surface word overlap (B03) | ✓ | Direct consequence of the embedding property above |
| Brute-force search is O(N) per query (B04) | ✓ | Definitional — exact search without an index requires a full scan |
| Graph-based ANN (e.g. HNSW) visits a small fraction of nodes via greedy graph traversal (B04) | ✓ | Malkov & Yashunin, "Efficient and robust ANN search using Hierarchical Navigable Small World graphs" (2018) |
| ANN trades recall for speed; can return a non-nearest neighbor (B05) | ✓ | Documented, expected behavior of every approximate index — recall < 100% is the defining trade-off (tunable via e.g. HNSW's `ef`/`M`) |

## Corrections applied

None needed.

## Numbers on screen

None invented. The 2D toy map is explicitly a simplification, not a claim
about any specific model's real embedding layout.
