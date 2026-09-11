# FACTCHECK.md — rag-from-first-principles

Source: `VIDEO_SCRIPT.md` Appendix B (claims ledger) in this repo, each number tied
to a generating script. **Verification status is stated honestly** (deep-explainer
rule 5): numbers are author-asserted and reproducible from the cited scripts;
internal consistency was checked this session; scripts were **not re-run** here.

| Beat | Claim | Value | Source script | Status |
|------|-------|-------|---------------|--------|
| B01/B02 | corpus | 600 docs → 1,500 chunks → 25 eval Qs | generate_corpus_big.py, build_index_big.py | source-asserted |
| B03/B04 | step = chunk_size − overlap (real code) | — | chunking.py | code verified (reads correctly) |
| B05 | fixed vs recursive chunk count | 8 vs 10 | build_index.py vs build_index_v2.py | source-asserted |
| B05 | chunk-length spread | 67–388, mean 202, median 104 | index_big.pkl | source-asserted |
| B05 | histogram buckets | 564/336/96/504 | index_big.pkl | source-asserted |
| B06 | token counts | 6 vs 13 tokens (20 chars each) | token_demo.py | source-asserted |
| B06 | chars/token range | 1.67–8.00 | token_demo.py | source-asserted |
| B07 | shape collapse | (7,)→(7,384)→(384,) | mechanism (mean pooling) | verified (standard) |
| B08 | isolated matmul speedup | 12.6× (14.924→1.181 ms), identical 75,497,472 ops | numpy benchmark | source-asserted; FLOP-identity verified (standard) |
| B09 | real batch throughput | 9.9 / 14.2 / 13.7 / 11.0 chunks/s | build_index_big.py | source-asserted |
| B09 | mask vs no-mask pooling delta | 2.9044 | pad_demo.py | source-asserted |
| B10 | embeddings shape/size | (1500, 768), 4.4 MB | build_index_big.py | verified (1500·768·4 B ≈ 4.4 MB) |
| B11 | cosine = normalized dot product | — | retrieval.py | code + math verified |
| B12 | argpartition top-k bug + fix | ascending → sorted | retrieval.py | code verified (argpartition semantics) |
| B13 | dilution | 0.7254 → 0.4681 (−35.5%) at 1365 chars | dilution_demo.py | source-asserted |
| B15 | chunking MRR | fixed 0.833 vs recursive 1.000 (both hit@3 100%) | run_eval.py | source-asserted |
| B16 | model comparison | mpnet 76%/0.655, MiniLM 76%/0.637, bge 88%/0.683 | compare_embeddings.py | source-asserted |
| B17 | hybrid equal-weight | dense 76%/0.655, BM25 84%/0.750, hybrid 80%/0.733 | weight_sweep.py | source-asserted |
| B18 | weight sweep peak | MRR 0.810 at 0.2–0.3 dense; hit flat 84% | weight_sweep.py | source-asserted |
| B19 | per-stage latency | embed 40.9 / retrieve 4.0 / rerank 301.5 / generate 1287.9 ms | benchmark.py | source-asserted; 0.2% and 320× checked |
| B20 | cache hit | 0.002 ms (~800,000× vs 1634 ms) | benchmark.py | source-asserted; ratio checked |
| B21 | storage | chunks × dims × 4 bytes | mechanism | verified (standard) |

## Notes
- "Source-asserted" = taken from the repo's own claims ledger, which states every
  figure is reproducible from the named script. Consistency (e.g. 0.2% latency, 320×,
  4.4 MB, FLOP identity, −35.5%) was arithmetic-checked and holds.
- The honest caveat from the script (Segment 9) is preserved in narration where it
  matters: the corpus is name-driven, BM25's best case — so the transferable lesson
  is "sweep the weight on your own eval set," not "use 0.3."
- No datable vendor version strings on screen.
