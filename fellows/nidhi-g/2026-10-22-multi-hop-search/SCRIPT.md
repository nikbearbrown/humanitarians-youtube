# SCRIPT — "Multi-Hop Search: Connecting the Pieces"

Skill: ai-explainer · Channel: claude-hai (@HumanitariansAI) · Voice: Kokoro `af_bella`
Formats: 16:9 + native 9:16 (built together) · Target ~2:00 (verified after audio; trimmed if over)
Status: **DRAFT v2 — awaiting narration approval (GATE P). No audio generated.**
Covers the fixes for points 6–9 plus points 10 (citations) and 11 (privacy).

---

## B00 — Opening (ClaudeComposerAsk) · ~10 s
**Show:** composer, `Hi, Nidhi`. Ask: *"How do I answer a question whose facts are scattered across a document?"* Results: `retrieve, read, retrieve again` · `follow the chain` · `cite every line`.
> Hi, I am Nidhi, and this video follows up on why the easy fixes fall short, with ways to connect the pieces. The voice is Bella, an AI narrator.

## B01 — Overview (BrutalistHesitantWriter) · ~9 s
**Show:** writer types *"Retrieve once. Then answer."* — strikes "once. Then answer", types "read, retrieve again".
> Multi-hop search doesn't retrieve once and answer. It retrieves, reads what it found, and lets that decide where to search next, step by step.

## B02 — Iterative retrieval (fixes 7, 8) · ~13 s
**Show:** a chain builds left to right: search *football* → *"Daniel took it"* → search *Daniel* → *dropped* → *grabbed* → *went to the kitchen*; the last link highlighted.
> Take the football question. Search the football: Daniel took it. Now search Daniel: dropped it, grabbed it, went to the kitchen. Each finding shapes the next search, and the latest fact wins.

## B03 — Decomposition: Self-Ask · ~11 s
**Show:** the question splits into sub-questions *"Who had the football?"* → *"Where did they go last?"*; label *Self-Ask (Press et al.)*.
> One method breaks the question into smaller ones. Self-Ask has the model pose and answer its own follow-up questions, which can each go to a search engine.

## B04 — Interleaving: IRCoT · ~12 s
**Show:** title *IRCoT = Interleaving Retrieval with Chain-of-Thought* (Trivedi et al., ACL 2023); alternating row *reason → search → reason → search*; note *reported gains on HotpotQA, MuSiQue and more*.
> Another, IRCoT, short for Interleaving Retrieval with Chain-of-Thought, does what its name says: one reasoning step, then a new search guided by it. Its authors report better retrieval and answers on multi-hop benchmarks.

## B05 — Linking facts: GraphRAG (fix 6) · ~11 s
**Show:** chunks with the same names (*Daniel*, *football*, *kitchen*) light up and connect into a small graph across chunk boundaries; label *GraphRAG (Microsoft, 2024)*.
> Graph-based methods like Microsoft's GraphRAG build a map of the people and things a document mentions, so related facts stay linked, even across chunks.

## B06 — Agentic search with code (my project; fix 9) · ~16 s
**Show:** code lines `grep("football")` → `grep("Daniel")` → `read_lines(…)`; the trail football → Daniel → kitchen with line numbers 3780 · 5091 · 5187 · 6021; tag *very early work · 1 question · 1 run*.
> My project tries an agent that writes its own searches in code, like grep and read lines, and follows the trail: in my first test, from the football, to Daniel, to the kitchen. That's very early work: one question, one run.

## B07 — Citations (point 10) · ~12 s
**Show:** answer *kitchen* alone, greyed with a "?" — then its receipt appears: the four cited line numbers, each ✓ checkable, and the answer turns solid; chips *insurance* · *healthcare* · *law* with *must be checkable*.
> Whatever the method, answers need receipts. Without the exact lines behind an answer, nobody can check it, and in insurance, healthcare or law, an answer you can't check is an answer you can't trust. My agent cited every line it used.

## B08 — Privacy (point 11) · ~7 s
**Show:** a document stays inside a "your machine" box; only a few highlighted lines pass out to the model.
> And searching locally means only the relevant lines need to leave your machine, not the whole sensitive document.

## B09 — The trade-offs · ~7 s
**Show:** a hop counter rising with a *time & cost* meter; one wrong link turns the rest of the chain grey.
> The catch: more hops cost more time and money, and one wrong step can derail the rest.

## B10 — How it's measured · ~8 s
**Show:** three benchmark cards: *HotpotQA (2018)* · *MuSiQue (2022)* · *BABILong (2024)*, each tagged *answer needs several facts*.
> That's why they're tested on multi-hop benchmarks like HotpotQA, MuSiQue and BABILong.

## B11 — Your Turn (ClaudeComposerAsk, "Your turn.") · ~12 s
**Prompt on screen:** *"Before answering, break my question into steps, search the document for each one, and cite the lines you used."*
> Your turn. Give Claude a long document and ask: "Before answering, break my question into steps, search the document for each one, and cite the lines you used." Then check each step.

## B12 — Outro · ~4 s
**Show:** `Multi-Hop Search` / `Connecting the Pieces` · HAI wordmark · `@HumanitariansAI`.
> Multi-Hop Search: Connecting the Pieces. At Humanitarians AI.

---
Sources: Press et al., Self-Ask, arXiv 2210.03350; Trivedi et al., IRCoT, ACL 2023; Edge et al., GraphRAG, arXiv 2404.16130; Yang et al., HotpotQA, EMNLP 2018; Trivedi et al., MuSiQue, TACL 2022; Kuratov et al., BABILong, NeurIPS 2024. Football run: agentic_search_pi evals/last_run.json.
