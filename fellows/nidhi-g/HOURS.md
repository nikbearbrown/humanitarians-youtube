# Hours Log — Nidhi Grover

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment project)<br>
**Agreement:** 2026-09-14 – 2026-10-31<br>
**Project managers:** Dhruv Patel, Shilpa

Weekly record of hours and tasks. Hours are split into **Video** (making STEM/AI and progress videos with Brutalist, including Brutalist setup) and **Research** (research and project work, including meetings).

**Projects:**
- Multi-hop RAG / agentic search: [nidhi-humanitarians/agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)
- Myelin (LLM habit compiler): [nidhi-humanitarians/myelin](https://github.com/nidhi-humanitarians/myelin)

---

## Summary

| Week | Dates | Hours | Video | Research | Status |
|---|---|---|---|---|---|
| 0 | 2026-09-14 – 09-22 | — | — | — | Agreement signing period; no work |
| 1 | 2026-09-23 – 09-29 | 5 | 0 | 5 | Below 20 h |
| 2 | 2026-09-30 – 10-06 | 20 | 14 | 6 | |
| 3 | 2026-10-07 – 10-13 | 20.2 | 10.2 | 10 | |
| 4 | 2026-10-14 – 10-20 | 20 | 10 | 10 | |
| 5 | 2026-10-21 – 10-27 | 16 (so far) | 10 | 6 | In progress (as of 2026-10-25) |
| **Total** | | **81.2** | **44.2** | **37** | |

---

## Week 0: 2026-09-14 to 2026-09-22

**Hours:** — (no work)

- Initial 8-day period for signing the agreement.
- Fully signed agreement received on 2026-09-22 at 21:15. No work was done before the signed agreement was in hand.

## Week 1: 2026-09-23 to 2026-09-29

**Hours:** 5 · Video 0 · Research 5

- Introduced myself on the Humanitarians AI Discord.
- Assigned to the initial project: the Kaggle Gemma Hackathon (post-training Gemma as a developer agent).
- Preliminary research on RLVR (reinforcement learning with verifiable rewards) and GPU acceleration.

**Note:** Below 20 hours. This was the first week after the agreement was signed, spent on onboarding and project assignment.

## Week 2: 2026-09-30 to 2026-10-06

**Hours:** 20 · Video 14 · Research 6

- Two failed Brutalist setup attempts, about 7 hours each. Evidence: test reels that failed at the review stage on 2026-10-02: [binary-search-test](2026-10-02-binary-search-test/) · [ribosomes-read-mrna](2026-10-02-claude-liam-ribosomes-read-mrna/)
- Further research on post-training, QLoRA, and GPU-based acceleration for the Gemma Hackathon project.

**Note:** The Gemma Hackathon project was dropped on 2026-10-06 because of differing competency expectations from the project managers.

## Week 3: 2026-10-07 to 2026-10-13

**Hours:** 20.2 · Video 10.2 · Research 10

- Watched the detailed Brutalist setup guide; completed a working Brutalist install.
- Created my first successful Brutalist video: [Brutalist, Installed.](2026-10-12-brutalist-installed/) (progress video)
- Set up the initial Git repository for the multi-hop RAG problem ([agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)) and debugged evident issues locally.
- Researched evaluation metrics and benchmarks to use.

## Week 4: 2026-10-14 to 2026-10-20

**Hours:** 20 · Video 10 · Research 10

- Created and reviewed 2 Brutalist videos with iterative changes: [Search, Don't Read.](2026-10-20-search-dont-read/) (progress video) and the first version of [Multi-Hop Search](2026-10-22-multi-hop-search/) (STEM/AI video, completed in Week 5).
- Attended a group meeting.
- Continued testing and debugging the multi-hop RAG agent ([agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)) on BABILong multi-hop questions over long documents. Tried connecting to the Pi agent directly after discovering an error, then decided to keep it local for testing.
- Received a new problem assignment: Myelin, an LLM habit compiler ([myelin](https://github.com/nidhi-humanitarians/myelin)). Conducted preliminary research, including RLCD (reinforcement learning for calibrated decisions) for calibrating when a compiled habit should answer "unsure".

## Week 5: 2026-10-21 to 2026-10-27 (in progress)

**Hours so far (as of 2026-10-25):** 16 · Video 10 · Research 6

- Created the backdated Week 3 STEM/AI video: [Stuff It or Search It?](2026-10-22-stuff-or-search/)
- Created the Week 5 progress video: [Myelin: Teaching Agents Habits](2026-10-24-myelin-habits/)
- Decided on and explored the tau-bench dataset for Myelin: agent traces from GPT-4o and Claude 3.5 Sonnet in the airline and retail domains, analyzed for frequently repeated decisions.
- Completed the initial research and [technical specification](https://github.com/nidhi-humanitarians/myelin/blob/main/docs/DESIGN_SPECIFICATION.md) for Myelin, and scaffolded the repository ([myelin](https://github.com/nidhi-humanitarians/myelin)).
- Wrote initial unit tests: trace mining and clustering on the tau-bench airline traces (including the chronological train/test split), the code-safety validator that blocks banned modules, and two example compiled habits (correct extraction, and "unsure" on ambiguous input).
- Attended a group meeting.
