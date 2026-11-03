# FACTCHECK — RAG Pipelines, End to End

Status: claims checked by Claude Code against the primary sources in SOURCES.md and local executable evidence. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Human sign-off: I, Likhith, reviewed both the 16:9 and 9:16 review cuts, including the final revisions (the "Hey, Likhith" greeting, the larger type and deeper accent colour, and the redesigned portrait scenes B04, B06, B07 and B08). Everything looks good: the claims above match the video, and I approve both the landscape and vertical cuts for their master builds. — Likhith

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | An LLM only knows its training data; private files aren't in it | PASS | Parametric knowledge is fixed at training (Lewis et al. 2020 §1) | Generic data categories on screen |
| 2 | B03 | Retraining is slow and expensive; retrieve at query time instead | PASS | Lewis et al.: the non-parametric index can be swapped/updated without retraining | Qualitative only, no figures |
| 3 | B04 | Documents are chunked; chunks become vectors capturing meaning, not just keywords | PASS | Dense retrieval (DPR encoder in Lewis et al.) matches semantics beyond lexical overlap | 2-D toy labelled |
| 4 | B05 | Vectors stored in a vector DB or in-database vector search for fast lookup | PASS | Standard practice (e.g. dedicated vector DBs; Postgres pgvector); Lewis et al. use a FAISS MIPS index | — |
| 5 | B06 | The question is embedded; cosine similarity finds the closest chunks | PASS | Same encoder embeds the query; cosine is the common metric (not the only one) | Scores computed by evidence/cosine_toy.py |
| 6 | B06 | cos θ = (q · c) / (‖q‖ ‖c‖); toy scores 0.99/0.97/0.68/0.16 | PASS | Algebra checked; numerical case: q=(0.90,0.35), c1=(0.95,0.25): 0.9425/(0.9657·0.9823)=0.9936 → 0.99 | — |
| 7 | B07 | Retrieved chunks inserted into the prompt as context beside the question | PASS | Standard prompt-assembly RAG (Lewis et al. concatenate passage + input) | Prompt labelled illustrative |
| 8 | B08 | Answer grounded in that context, not just training data; can cite sources | PASS | Generator conditions on retrieved passages + its parameters | "illustrative" answer |
| 9 | B09 | RAG answers about documents it never saw; only as good as its retrieval | CORRECTED | Brief said "answer accurately" — softened; retrieval failure → answer failure | Limit stated in narration + verdict |
