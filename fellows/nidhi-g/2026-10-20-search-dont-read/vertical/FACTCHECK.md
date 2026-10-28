# FACTCHECK — search-dont-read

Format: claim | verdict | source. No dates/times beyond the paper's venue year. No credentials anywhere.

| Beat | Claim | Verdict | Source |
|---|---|---|---|
| B02 | Started on a Kaggle competition: post-training Gemma as a developer agent; literature review (RLVR, PostTrainBench, HumanEval) | TRUE (owner's account) | Owner |
| B02 | Gemma is Google's model | TRUE | Google |
| B03 | Project scoped beyond the fellowship; reassigned | TRUE (owner's account, owner-approved wording) | Owner |
| B04 | Problem: 2,000+ page texts, reasoning scattered; payoff for insurance/healthcare | TRUE (paraphrase of assigned problem statement) | Owner's problem statement |
| B05 | Pi-style loop (for testing), one tool python_repl, helpers grep/read_lines/file_info, up to 12 turns, output capped at 3,500 chars | TRUE | agentic_search_pi/agent/pi_loop.py, tools_schema.py, run_search.py (--max_turns 12) |
| B06 | BABILong, NeurIPS 2024 Datasets & Benchmarks Track; hides facts in long books; multi-hop | TRUE | Kuratov et al., arXiv 2406.10149 |
| B06 | qa2 · 128k tokens · 6,429 lines · ~275 pages | TRUE | corpus/babilong_qa2_128k_meta.json |
| B07 | Lines 3780/5091/5187/6021 verbatim; answer kitchen matched target; 11 code runs; 1 question, 1 run | TRUE | evals/last_run.json |
| B08 | Next steps incl. connecting Earendil's Pi agent, fine-tuning | PLAN (owner-approved) | Owner |
