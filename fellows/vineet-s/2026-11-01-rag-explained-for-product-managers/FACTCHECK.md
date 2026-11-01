# FACTCHECK — RAG Explained for Product Managers

Scope: a general explainer. No source document, no statistics, no product or model names, no version numbers, no dated claims.
Method: author self-check of each claim against widely taught concepts. No external sources were consulted for this pass.

| Beat | Claim | Status |
|---|---|---|
| B00-B01 | RAG retrieves documents and gives them to the model with the question; the model is not retrained | Standard definition of retrieval-augmented generation. VERIFIED (general knowledge) |
| B02 | Company knowledge in policies, wikis, tickets is retrieved and used to ground answers | Typical enterprise RAG setup; sources vary by company. OK |
| B03 | Chunk and index (often embeddings), retrieve, augment the prompt, generate with citations | Standard pipeline; embeddings described as numbers capturing meaning. VERIFIED (general knowledge) |
| B04 | Fresh info, private data, fewer hallucinations (not zero), citations, usually cheaper than retraining, access control | Common reasons; hedged with 'usually' and 'reduces'. OK |
| B05 | PM decisions: data, chunking, number of passages, no-result behavior | Author's framing of real design levers. OK |
| B06 | Failure modes: wrong retrieval, stale docs, ignored passage, conflicting sources, unneeded retrieval | Widely observed failure modes. VERIFIED (general knowledge) |
| B07 | RAG for facts, fine-tuning for style or skill; many teams start with RAG | General guidance; 'many teams' is a soft generalization, not a statistic. OK |
| B08-B09 | Recap and viewer prompt | Restates the above. OK |

Corrections applied: none needed. Soft wording kept soft on purpose.
Limit: this is a self-check, not an independent review. A subject-matter reviewer has not signed it.
