# SCRIPT — "Stuff It or Search It?"

Skill: ai-explainer · Channel: claude-hai (@HumanitariansAI) · Voice: Kokoro `af_bella`
Formats: 16:9 + native 9:16 (built together) · Target ~2:00 (verified after audio; trimmed if over)
Status: **DRAFT v1 — awaiting narration approval (GATE P). No audio generated.**
Covers points 1–9 of the agreed list (10–11 are covered in the Multi-Hop Search video).

---

## B00 — Opening (ClaudeComposerAsk) · ~10 s
**Show:** composer, `Hi, Nidhi`. Ask: *"Why can't I just give an AI my whole document?"* Results: `it may accept it` · `it won't reliably reason over it` · `and retrieval misses connections`.
> Hi, I am Nidhi, and this video is about why the easy fixes for searching long documents fall short. The voice is Bella, an AI narrator.

## B01 — Overview (BrutalistHesitantWriter) · ~10 s
**Show:** writer types *"Give the AI the whole document. It reads all of it."* — strikes "reads all of it", types "won't use all of it".
> The easy answer is to give the AI the whole document. It will accept it. But accepting a document isn't the same as reasoning over it.

## B02 — NIAH: the easy case · ~12 s
**Show:** a page stack; one highlighted sentence (the "needle") lights up; label *Needle in a Haystack (Kamradt, 2023)*; tag *"one fact, found"*.
> The classic test is the needle in a haystack: hide one sentence in a long text, ask the model to find it. Most frontier models now pass, but that's the easy case.

## B03 — Shortcut 1: stuff it (points 1, 5) · ~13 s
**Show:** a whole document pours into a prompt box; the few relevant lines shrink into the pile; a meter labelled *cost & time per question* fills on every question.
> Shortcut one: stuff the whole document into the prompt. The few lines that matter get buried, and every question pays again for every page, in cost and in time.

## B04 — Accepted isn't used (points 2, 3) · ~15 s
**Show:** bar *advertised context* vs shorter bar *effective context* (label *RULER, Hsieh et al. 2024*); then a U-shaped curve: accuracy high at *start* and *end*, dipping in the *middle* (label *Lost in the Middle, Liu et al.*).
> Accepting a long context isn't using it. The RULER benchmark found most models fall short of their advertised length. And models use the start and end of their input best, losing what's in the middle.

## B05 — Distractors (point 4) · ~8 s
**Show:** the real fact among look-alike sentences; an arrow is tugged toward a look-alike.
> And similar-looking but irrelevant text can pull the model toward the wrong answer.

## B06 — Shortcut 2: RAG, and chunking (point 6) · ~14 s
**Show:** pipeline *split into chunks → find the most similar chunks → send to the model*; then two related facts land in different chunks, separated by a cut line.
> Shortcut two: retrieval, or RAG. Split the document into chunks, find the chunks most like your question, and pass only those on. But chunking can split facts that belong together.

## B07 — The second hop, and order (points 7, 8) · ~15 s
**Show:** question *"Where is the football?"*; similarity scores: *"Daniel took the football"* ranks high, *"Daniel went to the kitchen"* ranks low; then a timeline *took → dropped → grabbed → went to the kitchen*, last step highlighted.
> Ask, where is the football? Retrieval finds Daniel taking it. But the deciding fact, Daniel went to the kitchen, never mentions the football, so it ranks low. And order matters: the latest fact wins.

## B08 — References inside documents (point 9) · ~8 s
**Show:** a clause *"…as defined in section 4.2"* with an arrow jumping to section 4.2 elsewhere in the document.
> Documents also point to themselves, like "see section four point two". Those references need following, not matching.

## B09 — Takeaway (verdict card) · ~8 s
**Show:** two columns *Stuffing* / *Basic RAG*, both with ✓ *finds pieces* and ✗ *connects them*; footer *Next: multi-hop search*.
> Both shortcuts find pieces. Neither connects them. That's the job of multi-hop search, coming in the next video.

## B10 — Your Turn (ClaudeComposerAsk, "Your turn.") · ~11 s
**Prompt on screen:** *"Answer using only this document, and list every passage you combined to reach the answer."*
> Your turn. Give Claude a long document and ask: "Answer using only this document, and list every passage you combined to reach the answer." Then check: did it find them all?

## B11 — Outro · ~3 s
**Show:** `Stuff It or Search It?` · HAI wordmark · `@HumanitariansAI`.
> Stuff It or Search It? At Humanitarians AI.

---
Sources: Kamradt (NIAH, Nov 2023); Hsieh et al., "RULER", COLM 2024 (arXiv 2404.06654); Liu et al., "Lost in the Middle", TACL 2024 (arXiv 2307.03172). Football example: BABILong qa2 (Kuratov et al., NeurIPS 2024), my recorded run.
