# What Happens Inside a Financial Chatbot

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source files say `am_onyx`; overridden per the
convention used across this series (Anjana narrates, no channel handle)
**Target length:** ~4:10 (16:9 master) / ~2:45 (9:16 short)
**Register:** Teardown
**Topic:** Retrieval Augmented Generation, explained as the four steps between
a typed question and a cited answer.

---

## Beat 0 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~12s

**Narration:**

A financial chatbot answers in two seconds and cites three real filings. That
looks like the model knowing things. It isn't. I'm Anjana — here are the four
steps hiding behind that answer.

**Composer ask:**

> When I ask a financial chatbot whether a company raised guidance, it comes
> back in seconds with an answer and three citations. What is actually
> happening between my question and that answer?

**Output lines (resolved on screen):**
- the question becomes a vector
- meaning search, not keyword search
- the model reads your documents, not its memory

---

## Beat 1 — The Hook

**Duration:** ~8s brief / ~20s actual

**Narration:**

You type a question into a financial chatbot. "Did Company A raise revenue
guidance last quarter?" Two seconds later, an answer appears with three
citations from real filings. It looks like magic. It is not. There are four
steps between your question and that answer. Here is what happened.

**Visual direction:**

A clean, generic chat interface on a dark ground. The question types itself
character by character. Three loading dots pulse, then the answer streams in —
"Yes, Company A raised full-year revenue guidance from $12B to $12.5B during Q3
prepared remarks." — with three citation badges glowing beneath it. On "Here is
what happened" the whole interface shrinks to the top-left corner and stays
there as an anchor, opening the frame below for the pipeline to build into.

---

## Beat 2 — Embed the Question

**Duration:** ~12s brief / ~33s actual

**Narration:**

Step one. Your question is not sent to the language model yet. First it is
converted into a vector, a list of numbers that captures its meaning. The
embedding model reads "Did Company A raise revenue guidance" and produces a
three hundred eighty four dimensional vector. This vector is a coordinate in
meaning space. Questions about revenue guidance land near other revenue
guidance text. Questions about margin pressure land somewhere else entirely.
The vector is a search key, not for words, but for meaning.

**Visual direction:**

The question floats center screen and flows into a small box labelled
"Embedding Model" — deliberately a black box; its internals are not this
video's subject. Out the other side comes a horizontal strip of colored cells,
a barcode of meaning, labelled "384 dimensions." The strip lifts into a 2D
scatter plot of embedding space with four labelled neighbourhoods — revenue
guidance, margin commentary, capex outlook, earnings estimates. The question's
vector lands as a bright pulsing dot inside the revenue-guidance cluster,
because of what it means, not which words it used.

**Label:** Not searching for words. Searching for meaning.

---

## Beat 3 — Retrieve

**Duration:** ~15s brief / ~38s actual

**Narration:**

Step two. The vector searches a database of every earnings call transcript the
system has ever processed. Not keyword search. Vector search. It compares the
question's vector against thousands of stored chunk vectors and finds the
closest matches by meaning. "Revenue guidance" in the question matches
"top-line outlook" in a filing even though they share no words. The system
pulls the top three to five most relevant chunks, ranked by similarity. Each
chunk carries its metadata: company name, transcript date, section, speaker.
These chunks become the context the language model will read.

**Visual direction:**

The question's vector enters from the left; a cylindrical vector store pulses
on the right, filled with thousands of faint stored-chunk dots. The question
sends out a sonar ripple — dots near it in meaning space light up, distant ones
stay dim, and three glow brightest, connected by similarity scores of 0.94,
0.91, and 0.87. Three chunk cards slide out ranked by score, each carrying real
transcript language and its metadata tags: company, quarter, section, speaker.
The cards stack into a bundle and hand off to a waiting, not-yet-active LLM
node.

**Label:** Context assembled. Three chunks. Ready for the model.

---

## Beat 4 — Generate

**Duration:** ~15s brief / ~55s actual — the longest beat in the reel

**Narration:**

Step three. Now the language model gets involved. It receives a prompt with
three parts. First, a system instruction: you are a financial analyst, answer
only from the provided context, cite your sources. Second, the retrieved
chunks, the actual transcript text the vector search found. Third, the original
question. The model reads all of it together. It does not guess. It does not
use its training data. It answers from the context it was given, and it tags
every claim with a citation pointing back to the specific chunk it came from.
Step four. The answer streams back to you with source references attached. That
is RAG. Retrieval augmented generation. The model's knowledge comes from your
documents, not its memory.

**Visual direction:**

A prompt window assembles vertically in three color-coded sections — a grey
system instruction, a blue context block holding the three numbered chunks, and
a white question line — which lock together into one package and fire into the
LLM node. The node glows and the answer streams out character by character. As
each citation tag lands, a faint line draws back to the chunk it came from: the
citations are traceable, and that traceability is the payoff. The answer then
flows up into the chat interface still sitting in the corner from Beat 1, which
grows back to full size with its three badges lit. The pipeline fades. The
viewer is back where they started, knowing what happened underneath.

**Label:** RAG. The model reads your documents. Not its memory.

---

## Beat 5 — The Close

**Duration:** ~7s brief / ~19s actual

**Narration:**

Four steps. Embed the question. Search by meaning. Read the context. Generate
with citations. No hallucination, because the model never had to guess. Every
answer is grounded in a real document. That is what happens inside a financial
chatbot.

**Visual direction:**

A clean horizontal four-step pipeline — Embed, Retrieve, Read, Generate — each
step a compact icon that lights as the narration names it. On "grounded in a
real document," the citation badges glow and faint lines trace all the way back
through the pipeline to the chunks in the database, showing the whole chain at
once. The title lands: What Happens Inside a Financial Chatbot / Retrieval
Augmented Generation.

---

## Beat 6 — The Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~22s

**Narration:**

Let's recap with Claude. The question becomes a vector before the model ever
sees it. That vector searches by meaning, so a question about revenue guidance
finds a filing that says top-line outlook. The retrieved chunks are pasted into
the prompt as context, with an instruction to answer only from them. And every
claim in the answer points back to the chunk it came from. The model isn't
remembering. It's reading.

---

## Beat 7 — Your Turn (handoff)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~45s

**Narration:**

Your turn. "I have a pile of documents I keep having to search — reports,
notes, transcripts, policies — and right now I find things in them by
remembering roughly what I wrote and hunting for keywords. Can you help me: one,
work out whether keyword search is actually failing me, by naming things I'd
look for where the words I'd type wouldn't match the words on the page; two,
sketch what a retrieval system over my own documents would need to do to catch
those cases; and three, tell me honestly whether my collection is big enough
that this would be worth building, or small enough that I should just read it?"
Paste that into Claude and find out whether your own filing system has a
meaning problem.

**Why this prompt:** it turns the episode's mechanism on the viewer's own
material, and its third clause is the honest one — most people's document piles
are too small to need a vector store, and the prompt asks Claude to say so.

---

## Beat 8 — Outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~6s

**Narration:**

Embed, retrieve, read, generate. That's Anjana.

---

## Production Notes

**Total estimated duration:** ~4:10 (16:9). Beat 4 is the outlier — its source
narration covers both step three and step four, so it runs roughly 55 seconds
against a 15-second brief. Its component is built to fill that whole span
rather than finishing early and freeze-holding on a stale frame.

**Voice:** `af_bella` (Anjana). The source `beats.json` and `README.md` say
`am_onyx`; overridden per the series convention.

**Continuity device:** the chat interface introduced in Beat 1 persists as a
small thumbnail in the corner of Beats 2 and 3, then returns to full size in
Beat 4 — the loop the briefs ask for, honored across independently-rendered
beats.

**Delivery:** rendered at 4K in both 16:9 (3840×2160) and 9:16 (2160×3840). The
9:16 short is a derivative cut via `runtime/scripts/shorts.py`.

**No real company names or tickers anywhere in this reel** — the running
example is "Company A" throughout, and the $12B → $12.5B figures are
illustrative of that placeholder company, not a real filing. See `PEDAGOGY.md`.
