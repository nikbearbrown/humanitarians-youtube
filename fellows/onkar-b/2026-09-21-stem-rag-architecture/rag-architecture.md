**Series:** STEM & AI Architecture
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

**SCENE 1 — HOOK**
**VISUAL** — Ground fill. A prompt block snaps in.
`USER: What is our company's Q3 internal revenue?`
`AI: I don't have access to your private data.`
**ON SCREEN:** `THE KNOWLEDGE CUTOFF`
**VO:**
Hi, I am Onkar Bhujbal, and this video is about Retrieval-Augmented Generation, or RAG. Large language models are frozen in time the day they finish training, and they have zero access to your private data. So how do we make an AI answer questions about a confidential document? We use a RAG architecture.

**SCENE 2 — THE FRAMEWORK**
**VISUAL** — A Brutalist triangle diagram snaps in. 
`01 USER QUERY` | `02 VECTOR RETRIEVAL` | `03 CONTEXTUAL GENERATION`
**VO:**
We solve the knowledge gap using the RAG Triangle. Step one: intercept the user query. Step two: run a vector search against a private database to retrieve the relevant document. Step three: bundle that document and the original query together, and force the AI to generate its answer strictly from the provided context.

**SCENE 3 — WORKED EXAMPLE**
**VISUAL** — Side-by-side comparison. 
**LEFT:** `PROMPT: What is Q3 Revenue? (Fails)`
**RIGHT:** `PROMPT: Use this text: [Q3 Revenue was $4M]. What is Q3 Revenue? (Passes)` 
**VO:**
When you ask a raw AI for Q3 revenue, it fails. But with RAG, the system searches your vector ledger, finds the exact row saying Q3 revenue was four million dollars, and transparently injects that into the prompt behind the scenes. The AI isn't memorizing your data; it's just reading the text you handed it.

**SCENE 4 — FALSIFIABILITY**
**VISUAL** — The Triangle returns. Retrieval step flashes red.
**ON SCREEN:** `CONTEXT POISONING`
**VO:**
Where does RAG break? Context poisoning. If your retrieval system accidentally pulls an outdated document from Q2 instead of Q3, the AI will confidently generate a perfectly written, completely false answer. In a RAG system, the AI surrenders entirely to the retrieved text. If your search is flawed, your generation is doomed.

**SCENE 5 — SCAFFOLDED TASK & CLOSE**
**VISUAL** — Hard cut to mono text.
`SYSTEM: Answer strictly using context.`
`CONTEXT: The sky is neon green.`
**VO:**
Test this architecture manually. Paste a paragraph of made-up facts into an AI chat, and tell it to answer a question based only on your text. You will immediately see how context overrides training data. 
Liam, for Onkar Bhujbal and Humanitarians AI.