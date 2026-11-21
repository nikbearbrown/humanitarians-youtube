# FACTCHECK — multi-hop-search
| Beat | Claim | Verdict | Source |
|---|---|---|---|
| B02 | Iterative retrieval: each finding shapes the next search; latest fact wins | TRUE (mechanism; BABILong qa2 example lines) | evals/last_run.json |
| B03 | Self-Ask: model asks and answers its own follow-up questions; follow-ups can go to a search engine | TRUE | Press et al., arXiv 2210.03350 |
| B04 | IRCoT = Interleaving Retrieval with Chain-of-Thought; alternates reasoning and retrieval; authors report better retrieval and QA on multi-hop benchmarks (HotpotQA, 2WikiMultihopQA, MuSiQue, IIRC) | TRUE | Trivedi et al., ACL 2023 |
| B05 | GraphRAG builds an entity knowledge graph (+ community summaries) | TRUE (described as linking facts; not claimed as a multi-hop QA result) | Edge et al., arXiv 2404.16130 |
| B06 | Agent writes grep/read_lines searches; trail football→Daniel→kitchen; lines 3780/5091/5187/6021; 1 question, 1 run | TRUE | agentic_search_pi code + evals/last_run.json |
| B07 | Agent cited every line it used | TRUE | last_run.json final answer cites lines |
| B08 | Only search outputs (≤3,500 chars per step) go to the model API, not the whole document | TRUE (design); phrased "need to leave", not "nothing leaves" | repl/session.py max_output_chars |
| B10 | HotpotQA 2018, MuSiQue 2022, BABILong 2024 are multi-hop benchmarks | TRUE | Yang et al. EMNLP 2018; Trivedi et al. TACL 2022; Kuratov et al. NeurIPS 2024 |
