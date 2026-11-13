# What Is RAG? (script draft for approval, v2)

**Fellow:** Tanishaa · **Channel:** @HumanitariansAI · **Narrator:** Bella (Kokoro `af_bella`, an AI voice; disclosed on screen and aloud)
**Target length:** ~2½ minutes (about 420 spoken words), inside the 2–3 minute range · **Exports:** 16:9 at 3840×2160, plus a native 9:16 at 2160×3840
**Audience:** students who are new to AI. The channel's recurring question is when to use AI and when not to.

Each beat lists what's **on screen** first, then what Bella **says**.

---

### B00 · Cold open: the ask (~15 s)
**On screen:** The Claude app opens with the greeting "Hi, Tanishaa". The composer types: *"What is RAG, and when should I actually use it?"* The send button lights up and the first lines of the answer appear. A small label reads "AI narration: Bella".
**Says:** "Hi, I am Tanishaa, and this video is about RAG, retrieval-augmented generation, and when it actually helps. The voice you're hearing is Bella, an AI narrator reading a script I wrote."

### B01 · The one-line summary (~11 s)
**On screen:** A writer types *"RAG makes the AI smarter."*, hesitates, deletes **"makes the AI smarter"** and retypes it as **"lets the AI look things up before it answers."** A second line follows: *"It hands the model the right pages."*
**Says:** "RAG lets an AI look things up before it answers. It doesn't make the model any smarter. It hands the model the right pages, so the answer can point back to a source."

### B02 · The problem: answering from memory (~19 s)
**On screen:** Two answers side by side to the question *"Can I submit Lab 3 late?"* On the left, **From memory**: a confident, invented answer stamped "no source". The right side stays empty for now.
**Says:** "Start with the problem. A language model answers from patterns it absorbed during training. It has never seen your syllabus, your company handbook, or a policy that changed last month. Ask anyway, and it may still answer, fluently and wrong. Fluent isn't the same as correct."

### B03 · How it works: Retrieve, Augment, Generate (~18 s)
**On screen:** A three-stage flow lights up as each word is spoken. **Retrieve**: a stack of document chunks, with the three best matches pulled out. **Augment**: those chunks slide into the prompt. **Generate**: the answer writes itself with numbered citations.
**Says:** "RAG adds a step before the answer. Retrieve: search your documents for the few passages that best match the question. Augment: paste those passages into the prompt. Generate: the model writes from that text, and it can say where each part came from."

### B04 · How the search finds the right passage (~22 s) *(new)*
**On screen:** The syllabus is cut into short chunks. Each chunk becomes a dot on a map. The question becomes a dot too, and the three nearest dots light up. One of them is the passage about an **"extension"**, even though the question said **"late"**.
**Says:** "How does the search know which passages match? First, the documents are cut into short chunks. Each chunk is turned into a list of numbers, called an embedding, that captures what it means. The question gets one too. Chunks with similar meaning land close together, so a question about 'late' work can find a passage about an 'extension'."

### B05 · Worked example, run for real (~20 s)
**On screen:** Real Python retrieval output over a short **example syllabus written for this demo** (labeled as made up). Three passages appear, ranked by match score. The top one, *"Labs may be submitted up to 48 hours late with a 10% penalty"*, is highlighted. The empty right side from B02 fills in as **With retrieval**: the answer quotes it and cites the section.
**Says:** "Here it is on that same question. The search pulls three passages from the syllabus. The top one says labs can be submitted up to forty-eight hours late, with a ten percent penalty. Now the answer quotes it and names the section it came from, so you can check it yourself."

### B06 · When to use it, and when not to (~25 s)
**On screen:** Two columns sort themselves as each item is spoken.
**Use it when:** the answer lives in documents you have · the facts change · you need to cite.
**Skip it when:** the document is short enough to paste in · the task is reasoning or writing, not looking something up.
At the end, a third card drops in: **"Wrong passage → wrong answer that looks sourced."**
**Says:** "So when should you use it? When the answer lives in documents you can point to, like a syllabus, a manual or last week's meeting notes, especially when those facts change. When shouldn't you? If the document is short, just paste it in. If you need reasoning or writing, not lookup, retrieval won't help much. And watch the search: if it grabs the wrong passage, you get a wrong answer that looks sourced."

### B07 · Verdict (~11 s)
**On screen:** A Claude artifact page titled "What Is RAG?" with three key findings:
1. RAG looks things up; it doesn't learn.
2. A citation is something to check, not a guarantee.
3. The answer is only as good as the retrieval.
**Says:** "Three things to keep. RAG looks things up; it doesn't learn. A citation is something to check, not a guarantee. And the answer is only as good as what was retrieved."

### B08 · Your turn (~24 s)
**On screen:** The Claude composer, greeting "Your turn.", with this prompt typed in:
> *"Here's a document I use for school or work. Split it into short passages, show me the three you'd retrieve for this question: [my question]. Then answer using only those passages, quote them, and tell me what the document doesn't say."*

**Says:** "Your turn. Paste in a document you actually use and try this prompt: split it into short passages, show me the three you'd retrieve for my question, answer using only those passages, quote them, and tell me what the document doesn't say. That last part is the real test. A good answer admits what isn't there."

### B09 · Outro (~5 s)
**On screen:** The title "What Is RAG." in serif with a terracotta period, and @HumanitariansAI below it.
**Says:** "What is RAG? At Humanitarians AI."

---

**Fact check:** "Retrieval-augmented generation" comes from Lewis et al., 2020 (Facebook AI Research, NeurIPS 2020). Embedding-based search (dense retrieval) is the common approach, but keyword search is also used, and the script says "search" so it stays true for both. The script avoids model names and version numbers so it won't date. The syllabus in B05 is a made-up example and is labeled that way on screen.
**Timing:** Bella's real audio sets the final length. If it comes out under 2:00 or over 3:00, I'll adjust the narration and regenerate before rendering.
**Next, after your approval:** I'll build the beat sheet, generate Bella's audio, render a preview cut, and check its frames before showing it to you.
