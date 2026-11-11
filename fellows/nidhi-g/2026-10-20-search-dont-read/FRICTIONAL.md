# Frictional Log — Search, Don't Read.

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment)<br>
**Folder:** `2026-10-20-search-dont-read`<br>
**Week:** Week 4 (2026-10-14 – 2026-10-20)<br>
**Type:** Progress video<br>
**Project repository:** [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)

---

## 2026-10-06 — Project change
*(Written late on 2026-10-24; describes work from 2026-09-23 to 2026-10-06.)*

- **What I was working on:** The Kaggle Gemma Hackathon, assigned in Week 1: post-training Google's Gemma to act as a developer agent. Research only: RLVR methods and GPU acceleration (Week 1), then post-training, QLoRA and GPU-based acceleration (Week 2), plus datasets and benchmarks such as PostTrainBench and HumanEval.
- **Where it resisted / what I did next:** The project was dropped on 2026-10-06 because of differing competency expectations from the project managers. I was reassigned to agentic search: run Earendil's Pi agent with a Python REPL and fine-tune it to search 2,000+ page books.

## 2026-10-11 — First agentic-search test
*(Written late on 2026-10-24; describes work from Week 3, mainly 2026-10-11.)*

- **What I was working on:** Set up the initial repository for the multi-hop RAG problem ([agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)): a Pi-style agent loop (for testing) with one tool, a Python REPL with `grep`, `read_lines` and `file_info`; output capped at 3,500 characters; up to 12 turns. Also researched which evaluation metrics and benchmarks to use.
- **Where it resisted / what I did next:** Debugged evident issues locally. Tested on BABILong qa2 at 128k tokens (6,429 lines, ~275 pages). First run: correct answer ("kitchen"), 11 code runs, citing lines 3780 / 5091 / 5187 / 6021. One question, one run, so very early.
- **Understand now / still don't:** One run isn't evidence yet. Still open: stricter scoring, sandboxing the code, connecting the real Pi agent.
- **Evidence:** [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl) · `evals/last_run.json`

## Week 4 — Trying the real Pi agent
*(Written late on 2026-10-24; describes work from Week 4, 2026-10-14 – 2026-10-20.)*

- **What I was working on:** Continued testing and debugging the multi-hop RAG problem.
- **Where it resisted / what I did next:** After discovering an error, I tried connecting to the Pi agent directly, then decided to keep the setup local for testing.
- **Claude / others:** Attended a group meeting this week.
- **Evidence:** [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)

## 2026-10-20 — Making the progress video
*(Written late on 2026-10-24; describes work from 2026-10-20.)*

- **Tried / expected:** A progress video under 2:30, 16:9 and 9:16 built together: the project change, then the work so far.
- **Where it resisted / what I did next:** I corrected Claude's first understanding: it was a literature review when I was reassigned, not active work. I told it not to show any tokens or credentials (the problem statement I pasted contained one). Script edits I made: call it "Pi-style for testing" with Earendil's Pi agent as a next step; present it as very early work; drop B09 (that feature isn't available for testing); write "2,000+ page texts" instead of naming the quantum textbook; frame B07 clearly as a test question. Approved the script the same day; both masters were ready that evening.
- **Claude / others:** I provided the backstory, the problem statement and the repository. Claude translated them into a script and scenes, which I corrected (above) and approved. I also approved the final video.
- **Evidence:** [SCRIPT.md](SCRIPT.md) · [FACTCHECK.md](FACTCHECK.md) · [final/search-dont-read.verified.json](final/search-dont-read.verified.json) · [video](https://www.youtube.com/watch?v=q5kbQpRghHs)
