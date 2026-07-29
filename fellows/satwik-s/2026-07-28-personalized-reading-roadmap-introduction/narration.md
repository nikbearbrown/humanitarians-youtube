# Narration — Personalized, Project-Driven Reading Roadmaps for CaNCURE Trainees

- **Channel / persona:** `claude-hai` — Humanitarians AI · narrator **Satwik** (first author)
- **Voice:** Kokoro `af_bella` ("Bella") — free, local. No ElevenLabs, no keys.
- **Register:** Pragmatist (method → decision trigger → when NOT to use it / where it fails).
- **Source:** `sources/manuscript.pdf` — the paper **draft only**.
- **Spoken lines below are the ground truth for GATE P and for the audio step.** Word counts are planning aids; the generated MP3 durations are the master clock.

---

**B00 — cold open / ASK** *(≈54 words · est. 19s · Claude skin)*
> Hello. Here's a problem worth solving. Every trainee in our cancer-nanomedicine program gets the same thirty-eight-chapter textbook, organized by topic — but each one works a different lab project. So the book already holds everything they need, just in the wrong order. Claude, can you turn one fixed textbook into a personalized, project-driven reading roadmap?

**B01 — the problem** *(≈46 words · est. 16s)*
> Start with the failure mode: the textbook doesn't get read. Not because trainees won't — because the book is ordered by scientific topic, chapter after chapter, while the student's actual problem runs in a different sequence. One book, handed out identically to everyone. Every lab project, different.

**B02 — the reframe (ordering, not content; reorder, not retrieve)** *(≈62 words · est. 21s)*
> Here's the reframe. This isn't a content problem — the textbook has all of it. It's an ordering problem. Which makes this a reordering method — not search, not retrieval, not summarization. A similarity ranker returns the sections most like your project, but it can't say read this one first. So the system uses similarity only to select — then it sequences by learning dependency.

**B03 — the method (four-stage pipeline)** *(≈53 words · est. 18s)*
> The pipeline has four stages. One — extract every textbook section with a stable identifier. Two — tag each section with structured metadata: concepts, mechanisms, techniques. Three — build a dependency graph. Four — sequence a roadmap for the student's project. Every stage writes an inspectable, editable file. That's what keeps it reviewable, not a black box.

**B04 — the dependency graph + faculty (irreducibly-human)** *(≈57 words · est. 20s)*
> Stage three is the crux. Sections become nodes; learning dependencies become typed edges. Faculty-specified prerequisites are authoritative — read A before B. The model proposes additional edges, and faculty review them — not every relationship is approved yet. Proposing edges, the AI does well. Deciding which prerequisites are authoritative is the faculty's judgment. That part can't be handed off.

**B05 — the output (weekly project-aligned roadmap)** *(≈61 words · est. 21s)*
> Stage four turns the student's own project description into a weekly reading sequence. Every item says four things — what to read, why it matters, which lab task it supports, and what to read first. Once faculty-approved prerequisites are available, required background sections can be pulled earlier automatically. And two different projects produce two visibly different roadmaps — that's the personalization, on screen.

**B06 — when NOT to trust it + the future adaptive layer** *(≈72 words · est. 25s)*
> Now — when not to trust it. It runs on a single textbook, tuned for one program. The weekly timing is an advisor's heuristic, not a learned model. The current tagging pass is rule-based and deterministic. Uncertain metadata and any future model-assisted suggestions remain subject to faculty review. And it makes no claim about better learning — there's no outcome data yet. Later, faculty assessment and student progress could update the roadmap. Not today.

**B07 — verdict** *(≈67 words · est. 23s · Claude skin)*
> So — the method in one page. The textbook already holds the knowledge; the problem is order, not content. Treat it as reordering, not retrieval. Four inspectable stages: extract, tag, graph, sequence. Faculty approve the authoritative prerequisites — review is ongoing. And the output tells a trainee what to read, why, for which task, and in what order. Whether it improves learning is the next study — not this one.

**B08 — your turn / handoff** *(≈45 words · est. 16s · Claude skin)*
> Your turn. Give the system a course table of contents and a student project, then ask it to draft a dependency-ordered reading roadmap and flag every prerequisite that needs human approval. The goal is not to hide judgment — it is to make that judgment visible.

**B09 — outro / title restate** *(≈10 words · est. 7s · Claude skin)*
> Personalized, Project-Driven Reading Roadmaps. This is Satwik for Humanitarians AI.

---

**Estimated total:** ≈ 186 s (≈ 3:06) at ~2.9 words/sec. Bella typically runs a touch faster, so the audio-derived runtime should land near **2:48–3:02** — inside/at the top of the 2–3 minute target. If the measured cut overshoots 3:00, trim B06 then B07 first (the two longest body beats); never hand-edit timing — regenerate audio and recompile.
