# Nidhi Grover — Humanitarians AI Fellow

**Project:** Iacon Autonomics (RL Environment project)<br>
**Project Managers:** Dhruv Patel, Shilpa<br>
**Current agreement:** 2026-09-14 – 2026-10-31<br>
**GitHub:** [@nidhi-humanitarians](https://github.com/nidhi-humanitarians)<br>
**LinkedIn:** [nidhirg57](https://www.linkedin.com/in/nidhirg57/)

## About
I graduated from North Carolina State University (NCSU) with a B.S. in Computer Science, concentrating in Artificial Intelligence, with a minor in Statistics. At Humanitarians AI I work on the Iacon Autonomics (RL Environment) project. I started with a multi-hop retrieval-augmented generation (RAG) subproject, which I'm now wrapping up. I'm also building a habit compiler (Myelin) to make LLM pipeline tasks faster and cheaper to run.

## Projects

| Project | What it is | Repository | Status |
|---|---|---|---|
| **Multi-hop RAG / agentic search** | Can an agent answer questions over documents far too long to read by writing code to search them? A Pi-style agent loop with a Python REPL, tested on the BABILong multi-hop benchmark. | [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl) | Testing, debugging and write-up |
| **Myelin (LLM habit compiler)** | Spots repetitive decisions in agent traces and compiles them into fast, deterministic code that abstains when unsure, so the LLM is called only when needed. | [myelin](https://github.com/nidhi-humanitarians/myelin) | Initial research, technical specification and scaffolding done |

## Research / Project Plan

| Project | Deliverable | Target date | Status | Repository |
|---|---|---|---|---|
| Multi-hop RAG / agentic search | Finish testing and debugging the code-REPL search agent on the BABILong benchmark, then write up the results, failure modes and proposed fixes | — | In progress | [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl) |
| Myelin (LLM habit compiler) | First working version of the habit compiler: detect repeated decisions in agent traces and compile them into deterministic code that abstains when unsure | 2026-10-27 | In progress | [myelin](https://github.com/nidhi-humanitarians/myelin) |

## Weekly Evidence Index

Each **Hours** figure links to that week in [HOURS.md](HOURS.md). **Process logs** are the FRICTIONAL.md files in each video folder.

| Week | Start | End | Hours | STEM/AI video | Progress video | Process logs | Other Evidence/Notes |
|---|---|---|---|---|---|---|---|
| 0 | 2026-09-14 | 2026-09-22 | — | — | — | — | Agreement signing period; signed agreement received 2026-09-22 |
| 1 | 2026-09-23 | 2026-09-29 | [5](HOURS.md#week-1-2026-09-23-to-2026-09-29) | — | — | — | Initial project assignment (Kaggle Gemma Hackathon) received 2026-09-28 |
| 2 | 2026-09-30 | 2026-10-06 | [20](HOURS.md#week-2-2026-09-30-to-2026-10-06) | — (setup failed) | — (setup failed) | [Setup test 1](2026-10-02-binary-search-test/FRICTIONAL.md)<br>[Setup test 2](2026-10-02-claude-liam-ribosomes-read-mrna/FRICTIONAL.md) | Kaggle Gemma Hackathon dropped 2026-10-06 (differing competency expectations from the project managers) |
| 3 | 2026-10-07 | 2026-10-13 | [20.2](HOURS.md#week-3-2026-10-07-to-2026-10-13) | [Why RAG fails for complex texts](https://www.youtube.com/watch?v=bgagiyyImeI) | [Brutalist Installation](https://www.youtube.com/watch?v=t2tT4li77jM) | [STEM](2026-10-22-stuff-or-search/FRICTIONAL.md)<br>[Progress](2026-10-12-brutalist-installed/FRICTIONAL.md) | [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl) |
| 4 | 2026-10-14 | 2026-10-20 | [20](HOURS.md#week-4-2026-10-14-to-2026-10-20) | [Multi Hop Search](https://www.youtube.com/watch?v=rZhI6hPbIOs) | [Multi Hop Reasoning Project Update](https://www.youtube.com/watch?v=q5kbQpRghHs) | [STEM](2026-10-22-multi-hop-search/FRICTIONAL.md)<br>[Progress](2026-10-20-search-dont-read/FRICTIONAL.md) | [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl) |
| 5 | 2026-10-21 | 2026-10-27 | [16 (so far)](HOURS.md#week-5-2026-10-21-to-2026-10-27-in-progress) | — | [Myelin Project Update](https://www.youtube.com/watch?v=uJVnuI_coE8) | [Progress](2026-10-24-myelin-habits/FRICTIONAL.md) | [myelin](https://github.com/nidhi-humanitarians/myelin) |

## Completed Results

1. **Brutalist videos**
   - Set up Brutalist on Windows (after two failed attempts) and produced every video in 16:9 with a matching 9:16 Short.
   - STEM/AI: *Why RAG fails for complex texts* · *Multi Hop Search*. Progress updates: *Brutalist Installation* · *Multi Hop Reasoning Project Update* · *Myelin Project Update*.
   - [STEM/AI playlist](https://www.youtube.com/playlist?list=PLBfwlskHBwRM) · [Progress playlist](https://www.youtube.com/playlist?list=PLMg75wq-4wVw) · [Drive renders](https://drive.google.com/drive/folders/1urwoGwLCSoS4XG3U7dz-HtGePkXyDaGY)

2. **Multi-hop RAG / agentic search** ([agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl))
   - Built a Pi-style agent harness that searches very long documents by writing and running Python in a REPL.
   - Benchmarked it on all ten BABILong task types across 20 books of 2,000+ pages each.
   - Analyzed the failures into four failure modes and proposed a four-layer harness design to fix them.

3. **Myelin: LLM habit compiler** ([myelin](https://github.com/nidhi-humanitarians/myelin))
   - Analyzed public agent traces (tau-bench airline and retail) to find decisions agents repeat often enough to compile.
   - Wrote the [technical design specification](https://github.com/nidhi-humanitarians/myelin/blob/main/docs/DESIGN_SPECIFICATION.md): mining, clustering, code synthesis, sandboxed verification with an abstention rule, baselines and deliverables.
   - Scaffolded the Python package (mining, clustering, synthesis, sandbox, runtime, baseline and dashboard modules) with two example compiled habits and initial tests.

## Renewal
Renewal report: [RENEWAL.md](RENEWAL.md)

## Outstanding Issues
- **Agreement:** The agreement period is listed as 2026-09-14 – 2026-10-31, but the completed, signed contract was received on 2026-09-22. Per program guidance, no work was performed before the signed agreement was in hand, so this record covers 2026-09-23 onward.
- **Week 1 below 20 hours:** 5 hours, the first week after signing, spent on onboarding and project assignment.
- **Brutalist setup:** I had a considerable number of issues setting up Brutalist (two failed attempts in Week 2, about 7 hours each) and discussed them with my project managers. These issues affected my ability to produce the weekly videos: there are no weekly videos for Weeks 1–2, and the Week 3 STEM/AI video was made late.
- **Late videos:** The Week 3 STEM/AI video (*Stuff It or Search It?*) was made on 2026-10-22. The Week 4 STEM/AI video (*Multi-Hop Search*) was reworked and completed on 2026-10-22. Each video's README has a late note.
