# SCRIPT — RAG Pipelines, End to End

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about RAG pipelines.

**B01 · BLUF** — Here's the idea. You don't retrain the model on your documents. When a question arrives, you look up the right pieces of them, and hand those to the model along with the question.

**B02 · HOOK** — An LLM only knows its training data. So how can it answer about your private files?

**B03 · PROBLEM** — Retraining is slow and expensive. So we retrieve at query time instead.

**B04 · FRAMEWORK** — Step one, embed. Chunks become vectors that capture meaning, not just keywords.

**B05 · MECHANISM** — Step two, store them in a vector database, or your database's own vector search.

**B06 · WORKED EXAMPLE** — Step three, retrieve. Embed the question, and cosine similarity finds the closest chunks.

**B07 · MECHANISM** — Step four, augment. Those chunks go into the prompt, beside the original question.

**B08 · FALSIFIABILITY** — Step five, generate. The answer is grounded in that context, not just training data.

**B09 · VERDICT** — That's how RAG answers about documents it never saw. It's only as good as its retrieval.

**B10 · YOUR_TURN** — Your turn. Ask Claude: show which chunks a RAG pipeline should retrieve for one question about my documents. Then check they hold the answer.

**B11 · OUTRO** — RAG pipelines, end to end. At Humanitarians A I.
