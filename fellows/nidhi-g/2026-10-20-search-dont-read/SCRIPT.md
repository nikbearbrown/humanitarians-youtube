# SCRIPT — "Search, Don't Read."

Skill: ai-explainer · Channel: claude-hai (@HumanitariansAI) · Voice: Kokoro `af_bella`
Formats: 16:9 + native 9:16 (designed together) · Target ≤ 2:30 (estimate ~2:20, verified after audio)
Status: **DRAFT v2 — awaiting narration approval (GATE P). No audio generated.**

**Credentials rule:** no API key, curl command, `settings.py`, or problem-statement snippet
containing a token appears on screen or in narration. The problem statement is paraphrased.
Evidence shown is from `agentic_search_pi/` (code, corpus meta, `evals/last_run.json`) only.

---

## B00 — Opening (ClaudeComposerAsk) · ~12 s
**Show:** composer, greeting `Hi, Nidhi`. Ask: *"Can an agent find one fact in a 275-page document by writing code?"* Result lines: `built: a Pi-style loop + Python REPL` · `tested on: BABILong, 128k tokens` · `first run: correct, 11 code runs`.
> Hi, I am Nidhi, and this video is about my first steps in research on agentic search. The voice you're hearing is Bella, an AI narrator, telling my story.

## B01 — Overview (BrutalistHesitantWriter) · ~11 s
**Show:** writer types *"Agents read long documents."* — strikes "read", types "search"; then *"They do it by writing code."*
> Agents don't read long documents the way we do. They search them, by writing code. My project asks how well that works, on documents far too long to read.

## B02 — Where I started · ~15 s
**Show:** a Kaggle card *"Post-train Gemma → developer agent"*; three literature-review cards arrive: **RLVR** · **PostTrainBench** · **HumanEval**.
> I started on a different project: a Kaggle competition on post-training Google's Gemma model to act as a developer agent. I was in the literature review, reading about reinforcement learning with verifiable rewards, and benchmarks like PostTrainBench and HumanEval.

## B03 — Reassigned · ~8 s
**Show:** the Kaggle card dims; an arrow to a new card *"Agentic search"*.
> Then the project was scoped beyond what the fellowship could take on, so I was reassigned to a new research question.

## B04 — The new problem · ~15 s
**Show:** a towering page stack labelled *2,000+ pages*; three highlighted fragments far apart on different pages, connected by a thin line to one answer; a person searching (slow) vs. an agent writing `grep(...)` (fast); chips: *insurance* · *healthcare*.
> Picture a text of two thousand pages or more, where the reasoning behind one answer is scattered across it. People are bad at searching like that. Agents search by writing code, but how well does that work? Solving it would help insurance, healthcare and any field buried in documents.

## B05 — The setup · ~16 s
**Show:** loop diagram: model → `python_repl` (helpers `grep`, `read_lines`, `file_info`) → output, capped at 3,500 characters → model · *up to 12 turns*. Label: *Pi-style loop (for testing)*.
> So I built a small repository. A Pi-style agent loop, for testing, gives a model one tool: a Python REPL with search helpers like grep and read lines. The model writes code, sees the output, and repeats, for up to twelve turns, until it can answer.

## B06 — The benchmark: BABILong · ~17 s
**Show:** BABILong card: *NeurIPS 2024 · Datasets & Benchmarks* · *facts hidden inside long books* · *multi-hop: chain scattered facts*. Then my test: `qa2 · 128k tokens · 6,429 lines · ~275 pages`.
> To test it, I used BABILong, a benchmark published at NeurIPS twenty twenty-four. It hides simple facts inside long books, so answering means finding scattered facts and chaining them together. My first test: one hundred twenty-eight thousand tokens, about two hundred seventy-five pages.

## B07 — First test question · ~16 s
**Show:** label *BABILong test question*: *"Where is the football?"* · the supporting facts appear in document order, far apart: line 3780 took · 5091 dropped · 5187 grabbed · 6021 went to the kitchen → agent answer **kitchen** · benchmark answer **kitchen** ✓ · tag *very early work: 1 question · 1 run*.
> For a first test, I gave it one BABILong question: where is the football? The facts that answer it are scattered across the document. The agent traced Daniel taking the ball, dropping it, picking it up, then walking to the kitchen. Its answer, kitchen, matched the benchmark. One question, one run: very early work.

## B08 — What's next · ~12 s
**Show:** checklist builds: *connect Earendil's Pi agent* · *longer documents, more BABILong tasks* · *stricter scoring* · *sandbox the code* · *fine-tune toward 2,000-page books*.
> Next: connect the real Pi agent from Earendil, test longer documents and more BABILong tasks, score more strictly, sandbox the code, and then fine-tune toward two-thousand-page books.

## B09 — Your Turn (ClaudeComposerAsk, "Your turn.") · ~13 s
**Prompt on screen:** *"Here's a long document. Before answering my question, write code to search it, and show me every line you used."*
**Look-for lines:** *real line citations, not guesses* · *the search code it wrote* · *every fact in the chain*.
> Your turn. Give Claude a long document and paste this: "Here's a long document. Before answering my question, write code to search it, and show me every line you used." Then check: did it cite real lines, or guess?

## B10 — Outro (title restate) · ~4 s
**Show:** `Search, Don't Read.` serif, terracotta period · HAI wordmark · `@HumanitariansAI`.
> Search, Don't Read. At Humanitarians AI.

---
Sources for BABILong facts: Kuratov et al., arXiv 2406.10149 (NeurIPS 2024 Datasets & Benchmarks Track).
