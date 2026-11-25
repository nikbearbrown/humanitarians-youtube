# Storyboard — RAG, Explained

_Fellow: Asavari (Ash) Shejwal · AI / STEM · 2026-08-14 · 16:9 + 9:16 · 4K (3840×2160)_

Official Brutalist beat-sheet format (renders via brutalist.art / kokoro voice `af_kore`).
Beat two is the executive summary ("why this matters"), per review.

## Beat 1 — GREETING

**On screen:** This is Humanitarians.

**Narration:** This is Humanitarians.

## Beat 2 — OPEN

**On screen:** How does an AI answer from documents it was never trained on?

**Narration:** How can an AI answer questions about documents it was never trained on? The pattern is called RAG. The model doesn't memorize your files, it looks them up when you ask.

## Beat 3 — Why This Matters

**On screen:** What is this video about, and why should I watch it?

**Narration:** Hi, I'm Asavari, a fellow at Humanitarians AI. This video explains RAG, retrieval-augmented generation, the pattern that lets an AI answer questions about documents it was never trained on. You'll learn how it works and, more importantly, where it quietly goes wrong. If you're building anything with an LLM over your own data, start here.

## Beat 4 — THE PROBLEM

**On screen:** no source -> confident invention

**Narration:** A model only knows what it saw during training. Ask about your internal document, last week's filing, anything private, and it either admits it doesn't know or, far more often, invents something that sounds right. That confident invention is the hallucination. The model isn't lying, it just has no source.

## Beat 5 — THE MECHANISM

**On screen:** Question -> search -> passages -> answer

**Narration:** Your documents are split into chunks and indexed so they can be searched by meaning. When a question comes in, the system finds the passages most relevant to it, hands them to the model, and says, answer using this. So the answer is grounded in retrieved text, with citations you can check.

## Beat 6 — THE LIMIT

**On screen:** retrieval is the whole game

**Narration:** The catch people skip. RAG doesn't fix hallucination, it moves the risk. If retrieval pulls the wrong passages, the model writes a fluent, confident answer on the wrong evidence, and it looks just as trustworthy. So the hard problem is retrieval, chunking, search quality, and knowing when nothing relevant was found.

## Beat 7 — The verdict

**On screen:** Citations you can open beat prose you can't

**Narration:** Judge a RAG system not by how good the answer sounds. Ask whether it cites the passages it used, and whether you can open them. Ask what it does when nothing relevant exists. And ask whether anyone measures retrieval quality. An answer you can trace beats a polished one you can't. No source, no verdict.

## Beat 8 — OUTRO

**On screen:** RAG, Explained — outro card

**Narration:** RAG, Explained. From Humanitarians AI.
