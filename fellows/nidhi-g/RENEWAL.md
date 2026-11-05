# Fellowship Renewal — Nidhi Grover

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment project)<br>
**Project Managers:** Dhruv Patel, Shilpa<br>
**Current agreement:** 2026-09-14 – 2026-10-31<br>
**Signed agreement received:** 2026-09-22<br>
**Reporting period:** 2026-09-23 – 2026-10-25<br>
**Requested renewal:** 2026-11-01 – 2026-12-31

After my initial project (Kaggle Gemma Hackathon) was dropped, I moved to agentic search and built and benchmarked a code-REPL search agent for multi-hop questions over very long documents. I then started Myelin, an LLM habit compiler, and completed its research and technical specification. Despite early Brutalist setup issues, I published five videos. I am requesting renewal to complete the multi-hop RAG project, build out the Myelin habit compiler, and take on the further projects my project managers assign.

## Completed
1. **Agentic search (multi-hop RAG)**: built a Pi-style agent that searches very long documents by writing and running Python in a REPL, benchmarked it on all ten BABILong task types across 20 books of 2,000+ pages each, and analyzed the failures with a proposed four-layer fix. [Benchmark testing and debugging](https://github.com/nidhi-humanitarians/agentic-repl#5-complete-empirical-benchmark-records-1m-context-tier--2500-pages) · [Repository](https://github.com/nidhi-humanitarians/agentic-repl)
2. **Myelin (LLM habit compiler)**: analyzed public tau-bench agent traces to find repeated decisions, wrote the technical specification for compiling them into deterministic code that answers "unsure" when it isn't sure, and scaffolded the Python package with example compiled habits and initial tests. [Technical specification](https://github.com/nidhi-humanitarians/myelin/blob/main/docs/DESIGN_SPECIFICATION.md) · [Repository](https://github.com/nidhi-humanitarians/myelin)
3. **Brutalist setup and five videos**: set up Brutalist on Windows after two failed attempts and produced five videos, each in 16:9 with a 9:16 Short: three progress updates and two STEM/AI videos on why plain RAG falls short and how multi-hop search connects the pieces. [STEM/AI playlist](https://www.youtube.com/playlist?list=PLBfwlskHBwRM) · [Progress playlist](https://www.youtube.com/playlist?list=PLMg75wq-4wVw)

Full version with more detail: [README: Completed Results](README.md#completed-results)

## Hours
20+ hours in Weeks 2–4. Below 20: Week 1 (5 h, onboarding). Week 5 is partial (to 2026-10-25). Full record: [HOURS.md](HOURS.md)

## Weekly Evidence

| Week | Hours | Videos | Logs |
|---|---|---|---|
| 0 · 09-14 – 09-22 | — | — | Signing period, no work |
| 1 · 09-23 – 09-29 | 5 | — | [Hours](HOURS.md#week-1-2026-09-23-to-2026-09-29) |
| 2 · 09-30 – 10-06 | 20 | — (setup failed) | [Hours](HOURS.md#week-2-2026-09-30-to-2026-10-06) · [Setup test 1](2026-10-02-binary-search-test/FRICTIONAL.md) · [Setup test 2](2026-10-02-claude-liam-ribosomes-read-mrna/FRICTIONAL.md) |
| 3 · 10-07 – 10-13 | 20.2 | [Progress](https://www.youtube.com/watch?v=t2tT4li77jM) · [STEM (late)](https://www.youtube.com/watch?v=bgagiyyImeI) | [Hours](HOURS.md#week-3-2026-10-07-to-2026-10-13) · [Progress log](2026-10-12-brutalist-installed/FRICTIONAL.md) · [STEM log](2026-10-22-stuff-or-search/FRICTIONAL.md) |
| 4 · 10-14 – 10-20 | 20 | [Progress](https://www.youtube.com/watch?v=q5kbQpRghHs) · [STEM (late)](https://www.youtube.com/watch?v=rZhI6hPbIOs) | [Hours](HOURS.md#week-4-2026-10-14-to-2026-10-20) · [Progress log](2026-10-20-search-dont-read/FRICTIONAL.md) · [STEM log](2026-10-22-multi-hop-search/FRICTIONAL.md) |
| 5 · 10-21 – 10-25 | 16 | [Progress](https://www.youtube.com/watch?v=uJVnuI_coE8) | [Hours](HOURS.md#week-5-2026-10-21-to-2026-10-27-in-progress) · [Progress log](2026-10-24-myelin-habits/FRICTIONAL.md) |

## Next Period
- **Multi-hop RAG: iterative benchmarking and debugging.** Run the agent against the complete BABILong benchmark (QA1–QA20; the repo currently covers QA1–QA10 at the 1M-token tier), including its extended longer-context versions, and add other long-document and multi-hop datasets. Work in rounds: run, diagnose the failures, apply fixes from the proposed four-layer harness design, rerun, and compare each round against the current 20-book baseline.
- **Multi-hop RAG: from prompt to fine-tuned model.** Experiment with moving the search behavior out of the prompt and into the model. Today a model plus a prompt makes an agent; the idea is to fine-tune a very small model so that the prompt's guidance becomes built-in priors, teaching it to search a very large data pool.
- **Myelin: implementation and initial testing.** Complete the habit compiler implementation and run initial testing on the tau-bench traces, using held-out later sessions and the planned baselines (semantic cache, small classifier, small local model).
- **Myelin: synthetic dataset (potential).** Generate a large synthetic question-and-answer dataset from a very large, well-established codebase such as scikit-learn or PostgreSQL, where functions represent concepts and models already know the material well. Use DeepSeek to generate the questions and answers and stronger models to judge them, then test how well Myelin learns habits on it.
- Further projects as assigned by the project managers
- Weekly videos, FRICTIONAL entries and daily hours, kept at the time of the work

## Outstanding Issues
See [README: Outstanding Issues](README.md#outstanding-issues)
