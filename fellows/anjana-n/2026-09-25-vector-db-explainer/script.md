# What Vector Databases Do That SQL Cannot

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source `beats.json` says `am_onyx`; overridden per
the series convention (Anjana narrates, no channel handle)
**Target length:** ~2:30 (16:9 master) / same cut in 9:16 (inside the 3:00
Shorts cap, so nothing is dropped)
**Register:** Teardown
**Standalone:** sibling to `embeddings-explainer`. That one is about what a
vector *is*; this one is about what you do with a few million of them. They
share a palette and a way of drawing vector space on purpose — the scatter in
B02 is meant to be recognised by anyone who watched the other video.

---

## Beat 0 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~12s

**Narration:**

Every database you have ever used answers the same kind of question: which rows
match. Vector databases answer a different one, and the difference is not a
feature — it is a different shape of question. I'm Anjana.

**Composer ask:**

> SQL is very good at "which rows match this condition". What does a vector
> database do that it structurally cannot, and how does it stay fast when the
> answer means comparing against everything?

**Output lines (resolved on screen):**
- no WHERE clause — a query is a point
- results ranked by distance, not filtered
- a graph index, so you skip most of the data

---

## Beat 1 — SQL Has No Operator for "Similar"

**Duration:** ~12s brief / ~17s actual

**Narration:**

Hello, Anjana here. A SQL database answers exact questions. Give me every row
where the status equals active. Give me every order above fifty dollars. But
what if the question is: find me something similar to this? SQL has no operator
for similar. That is where vector databases start.

**Visual direction:**

Two query blocks stack on the left. The first types itself out —
`SELECT * FROM products WHERE status = 'active'` — takes a green check, and
drops three matching rows beneath it. The second types out underneath and stops
dead where the operator should be: `WHERE ??? similar to this`, the `???`
pulsing red. No check. No rows. The right half of the frame stays empty except
for a dotted outline with a question mark in it — the answer hasn't arrived
yet.

---

## Beat 2 — Storing Embeddings

**Duration:** ~12s brief / ~21s actual

**Narration:**

A vector database does not store rows and columns. It stores embeddings. Each
record is converted into a high-dimensional vector, a list of hundreds of
numbers that encode its meaning. Text, images, audio, anything that can be
embedded becomes a point in space. Similar items land near each other.
Different items land far apart.

**Visual direction:**

The dotted box from B01 resolves into a vector space. Green dots arrive in the
upper right, each labelled with the sentence it came from — "quarterly revenue
rose", "sales beat expectations", "exceeded guidance". Red dots fill the lower
left — "missed earnings target", "lowered full-year outlook", "revenue
declined". One dot gets an annotation: each of these is 768 numbers. A dashed
line runs between the two clusters to say how far apart they are.

---

## Beat 3 — Querying by Distance

**Duration:** ~13s brief / ~23s actual

**Narration:**

When you query a vector database, you do not write a WHERE clause. You give it
a vector and ask: what is closest? The database computes the distance between
your query vector and every stored vector. Cosine similarity measures the angle
between them. Small angle, high similarity. The results come back ranked by
proximity, not filtered by a condition.

**Visual direction:**

Same space. A gold query dot drops in near the green cluster — "strong revenue
growth" — and rings ripple outward from it. As each ring passes a dot, that dot
lights and its entry writes itself into a ranked list on the right: 0.94, 0.89,
0.83. The red cluster sits inside the outermost ring and stays dim, which is
the point — nothing was excluded by a condition, it just ranked low. A small
inset shows the angle between two vectors, because that is what the number
actually measures.

---

## Beat 4 — Making It Fast

**Duration:** ~13s brief / ~27s actual

**Narration:**

Comparing your query against every stored vector works, but it is slow. A
million vectors means a million distance calculations per query. Vector
databases solve this with approximate nearest-neighbor indexes. One common
approach builds a graph where each vector connects to its nearby neighbors. To
search, you enter the graph at a random point, hop to the closest neighbor, and
repeat. In a few hops, you reach the neighborhood of the true nearest match
without scanning the full dataset.

**Visual direction:**

Split screen. On the left, brute force: a query dot with thin red lines firing
out to every single stored dot, a counter spinning up to 1,000,000, a clock
crawling, the word slow. On the right, the same dots but wired into a sparse
graph — each connected only to its near neighbours. The query enters at a
random node on the edge and a gold path hops: four hops, each landing closer,
the last one on the green target. Counter: 47. The word fast. Underneath both:
approximate nearest neighbor.

---

## Beat 5 — Close

**Duration:** ~10s brief / ~18s actual

**Narration:**

SQL answers what matches. Vector databases answer what is similar. Semantic
search, recommendation engines, retrieval-augmented generation, duplicate
detection. Anywhere the question is about meaning rather than exact values,
vectors are the right storage.

**Visual direction:**

Four panels in a row, each glowing gold in turn: semantic search (a query bar,
"meaning, not keywords"), recommendations (a grid with one item picked out,
"similar items"), retrieval-augmented generation (a chat bubble pulling a
document up beneath it, "retrieved context"), duplicate detection (two
overlapping documents with a similarity score between them, "near-duplicates").
They settle, and the title takes the bottom of the frame.

---

## Beat 6 — Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~22s

**Narration:**

Let's recap with Claude. A vector database stores meaning as position, so
"similar" becomes a distance you can actually compute. A query is not a filter,
it is a point — and what comes back is everything, ranked, rather than the
subset that passed a test. Doing that honestly against a million vectors would
be a million comparisons, so the index gives up exactness on purpose: it walks
a graph of near neighbours and gets close enough in a few dozen hops.

**Artifact lines:**
- Records are stored as embeddings — position in the space *is* the meaning.
- A query is a vector, not a condition; results come back ranked by distance.
- Cosine similarity scores the angle between two vectors, not their length.
- ANN indexes trade exactness for speed — a graph walk reaches the right
  neighbourhood without scanning everything.

---

## Beat 7 — Your Turn

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~30s

**Narration:**

Your turn. Look at something you currently search with exact matches — tags, a
category dropdown, a keyword field — and ask what people are actually trying to
find when they use it. Then ask whether ranking everything by similarity would
serve them better than filtering to whatever happened to match, and be honest
about where an approximate answer would not be good enough.

**Composer ask:**

> I have a search or lookup that works on exact matches — tags, categories,
> keyword fields. Can you help me: one, work out what people are actually
> trying to find when they use it, versus what the exact match returns; two,
> say whether ranking everything by similarity would genuinely serve them
> better than filtering, or whether I'd just be adding fuzziness to something
> that works; and three, tell me honestly where in my case an *approximate*
> nearest-neighbour answer would not be good enough, and what I'd have to do
> instead there?

---

## Beat 8 — Title outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~5s

**Narration:**

Anjana here, thanks for watching.

**Title:** What Vector Databases Do
**Subline:** similar is a distance · not a condition
**Handle:** (none)
