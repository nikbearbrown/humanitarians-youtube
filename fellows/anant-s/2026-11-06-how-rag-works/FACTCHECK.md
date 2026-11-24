# FACTCHECK — How RAG Works

Status: drafted and self-checked by Claude (planning session), 2026-11-22. Awaiting human sign-off at the narration gate (GATE P).

Verdicts: PASS · CORRECTED (wrong or loose in draft, fixed) · EXEMPT (greeting, framing, or an illustration labelled as such).
"Executed" means the number was produced by `demo/rag_demo.py`; the run is in `demo/RUN-LOG.txt`, the values in `demo/evidence.json`.
Script sha256 `ef0b6742…6be`; inputs sha256 `caf5a186…073`. The script asserts every ranking claim below and exits non-zero if one fails.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | "Hallo. This is Liam, in for Bear." | EXEMPT | Greeting and persona (IN-FOR-BEAR law); "Hallo" is on the SKILL's clean-greeting list | — |
| 2 | BIDEA | A chatbot has never read your own documents; RAG looks them up rather than memorizing them | PASS | A model's weights come from training data; private files are not in it unless trained on. RAG supplies retrieved passages at inference (Lewis et al. 2020, §1–2) | — |
| 3 | BDEFS | RAG = retrieval-augmented generation: look things up first, then write the answer | PASS | Lewis et al. 2020 §1: "which we refer to as retrieval-augmented generation (RAG)"; retriever then generator (§2) | — |
| 4 | BDEFS | Chunk, embedding, vector store definitions | PASS | Standard usage; the paper splits articles into "disjoint 100-word chunks" (§3) and searches dense vectors with a FAISS index (§3) | — |
| 5 | B00 | The model never saw these pages in training | EXEMPT | The handbook is constructed for the film (`demo/rag_demo.py` DOCS), so it is true by construction | — |
| 6 | B01 | Three documents: returns, shipping, warranty | PASS executed | `n_docs = 3` | — |
| 7 | B01 | RAG does not teach the model the pages; it supplies the right page at answer time | PASS | Lewis et al. 2020: the retriever's documents condition the generator at inference | — |
| 8 | B02 | Each document has two sentences, so each becomes two chunks; six in all | PASS executed | Chunker = one chunk per line; `n_chunks = 6` | — |
| 9 | B03 | Toy embedding counts words, one slot per word: 29 | CORRECTED | `dims = 29` executed. Draft said "twenty-nine different words in the handbook", but 29 is the count after dropping stop-words ("the", "and"…) and folding plurals and past tenses | Now "the handbook's twenty-nine key words"; screen says "29 numbers" |
| 10 | B03 | Real systems use a trained model, so chunks that mean the same thing land close together | PASS | Dense retrievers such as DPR (BERT-based bi-encoder) used in Lewis et al. 2020 §2.2 | — |
| 11 | B04 | Embeddings are filed once, ahead of time, before any question | PASS | Lewis et al. 2020 keep the document encoder and index fixed and build the index in advance (§2.2, §3); the demo builds the store before the query | — |
| 12 | B05 | The question passes through the same embedding, into the same space | PASS executed | `embed_query` uses the store's vocabulary and idf | — |
| 13 | B06 | The returns chunk scores 0.58 | PASS executed | Run A rank 1: `returns#1` 0.5774 | Shown and spoken to two decimals |
| 14 | B06 | The warranty chunk shares only the word "laptop" and scores 0.25 | PASS executed | Run A rank 2: `warranty#1` 0.2494; its tokens {every, laptop, one, year, warranty} ∩ question tokens {long, return, laptop} = {laptop} | — |
| 15 | B06 | The other four share no words and score zero | PASS executed | Run A ranks 3–6 are all 0.0000 | — |
| 16 | B07 | Paste the top two chunks into the prompt with an "answer only from these notes" instruction | PASS executed | `TOP_K = 2`; the prompt string is in RUN-LOG run A | — |
| 17 | B08 | The model answers "thirty days", from the returns chunk, and can point back to its source | EXEMPT | ILLUSTRATED: no language model is run. The demo's stand-in reader copies "30 days" from the rank-1 chunk and records `cites returns#1`. The screen carries an "illustrated" tag | Labelled as illustration on screen and in SHOTLIST |
| 18 | B09 | An added old FAQ page now scores 0.68; the right chunk drops to second at 0.38 | PASS executed | Run B: `faq-2019#1` 0.6833, `returns#1` 0.3846, `warranty#1` 0.1660. The tabs card shows all three | — |
| 19 | B09 | It repeats the question almost word for word | PASS | The chunk contains "How long do I have to return a laptop?" verbatim; it is the only chunk with "long" | — |
| 20 | B09 | Draft FAQ chunk began "Old FAQ:" | CORRECTED | A chunk that announces it is old is an easy case: a careful model might discount it. Real stale pages rarely label themselves | Chunk text is now "FAQ: …"; staleness lives only in the file name `faq-2019.txt` and the "2019 FAQ" screen label. Scores re-executed (0.6204 → 0.6833) |
| 21 | B10 | Draft: "the model answers fourteen days, with full confidence" | CORRECTED | Run B's prompt carries BOTH chunks (14 days first, 30 days second). A model may notice the conflict, so "answers" overstated it | Now "A model told to trust its notes CAN answer fourteen days, fluently and confidently"; answer card tagged "illustrated" |
| 22 | B10 | The mistake happened at retrieval, not in the writing | PASS executed | The stand-in reader's output changes only because the rank-1 chunk changed (run A vs run B) | — |
| 23 | B11 | Take the old page out and the returns chunk is back on top at 0.58; nothing retrained | PASS executed | Run C ranking is asserted identical to run A (0.5774); the demo has no trained parameters at all | — |
| 24 | B12 | The 2020 paper named RAG | PASS | Lewis et al. 2020 §1 introduces the name for its method ("which we refer to as retrieval-augmented generation (RAG)"). It does not claim to be the first retrieve-then-read system; the narration says "named", not "invented" | Wording kept to "named it" |
| 25 | B12 | Lewis and colleagues gave a model twenty-one million Wikipedia passages to search | PASS | Lewis et al. 2020 §3: December 2018 dump, "split into disjoint 100-word chunks, to make a total of 21M documents". On screen: "21M", "per Lewis et al. 2020" | Draft said "searched … this way"; "this way" dropped, since their retriever is dense (DPR), not word-count TF-IDF |
| 26 | B12 | They updated what the model knew by swapping in a newer copy of Wikipedia | PASS | Lewis et al. 2020 §4.5 "Index hot-swapping": December 2016 vs December 2018 indexes, 82 world leaders; 70% / 68% matched vs 12% / 4% mismatched. "We can update RAG's world knowledge by simply replacing its non-parametric memory." Same model throughout | — |
| 27 | BHTF | Your-turn prompt and two checks | EXEMPT | An instruction to the viewer, not a factual claim | — |
| 28 | BOUT | "How RAG Works. At Nik Bear Brown." | EXEMPT | Locked outro (OUTRO-LOCK.md) | — |

## Dating check (DOUBLE-CHECK law)
- No product names, prices, model names or "latest" claims in the narration. The one date (2020) is a citation date and will not go stale.
- The BHTF composer's `modelLabel: "Opus 5.5"` is house UI chrome copied from the reference sheets; review at render time.

## De-sensationalize
- "confidently" in B10 is hedged by "can"; no "always", "never", "solves hallucination".

## Format conversion, 2026-11-24 (appended; the rows above are unchanged)

The film was converted from show-tell to ai-explainer. BIDEA and BDEFS are retired (rows 1–4). The body was renumbered B00–B12 → B10–B22 with no content change; the rows above keep the old ids (B06 there = B16 now, and so on). A new BVDT recap was added. Narration approval: the original narration on 2026-11-22 ("approve all six"); the new B00, B01 and BVDT on 2026-11-24, by Anant.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 29 | B00 (spoken) | "Hello, this is Liam, in for Bear. The ask: how can a chatbot answer questions about my own documents, when it has never read them?" | EXEMPT | Greeting and the ask (a question). "Never read them" is true by construction (row 5). | — |
| 30 | B00 (on screen) | "the idea: look things up first, then write the answer" | ✓ | Row 3 | — |
| 31 | B00 (on screen) | "worked example: a shop handbook, a laptop return, 30 days" | ✓ executed | Rows 6, 13, 17. The retrieval is executed; the answer step is illustrated (row 17). | — |
| 32 | B00 (on screen) | "where it breaks: an old page in the store wins the search" | ✓ executed | Row 18: FAQ 0.6833 > returns 0.3846 | — |
| 33 | B01 | "With RAG, a chatbot answers from what it just looked up." | ✓ | Rows 2, 7 | — |
| 34 | B01 | "It searches your documents for the closest pieces, pastes them into the prompt, and writes from them." | ✓ executed | Rows 13–16 (TOP_K = 2) | — |
| 35 | B01 | "RAG stands for retrieval-augmented generation." | ✓ | Rows 3, 24 | — |
| 36 | BVDT | "Cut your documents into chunks, and turn each chunk into an embedding, a list of numbers." | ✓ executed | Rows 8–9 | — |
| 37 | BVDT | "File them in a vector store." | ✓ | Row 11 | — |
| 38 | BVDT | "When a question arrives, embed it too, and fetch the closest chunks." | ✓ executed | Rows 12–15 | — |
| 39 | BVDT | "Paste them into the prompt, and the model answers from them." | ✓ (minor) | Row 16. The answer step is illustrated, not run (row 17). | — |
| 40 | BVDT | "And if the store holds an old page, the answer goes old with it." | ✓ (minor) | Row 18: the stale chunk ranks first. Row 21 hedges that a model *can* then answer 14 days; this recap line is less hedged than row 21. | — |
| 41 | BVDT | "Fix the store, not the model." | ✓ executed | Row 23: removing the old page restores the ranking; nothing is retrained | — |
| 42 | BVDT (card line 6) | "The 2020 paper that named it searched 21 million Wikipedia passages." | ✓ | Rows 24–25: 21M 100-word passages. "This way" is not claimed (their retriever is dense). | — |
