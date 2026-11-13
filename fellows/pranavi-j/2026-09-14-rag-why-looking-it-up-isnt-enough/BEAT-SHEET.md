# Beat Sheet (APPROVED — Gate P, 2026-09-17): "RAG: Why 'Looking It Up' Doesn't Guarantee It's True"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly work report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as the prior 3 STEM
videos in this series)
**Phase:** 2 — approved for narration lock / audio generation. FACTCHECK item resolved 2026-09-17:
citation skipped, kept as general/uncited framing. See `FACTCHECK.md`.
**Format note:** first STEM video built under the toolkit's new submission spec — see the
sibling weekly-work video's beat sheet for the same note.

---

## Premise

**What this covers:** a reusable 3-question rubric — "Is the source actually relevant? / Is the
source actually current? / Is the model reading the source, or just remembering it?" — for
deciding whether a Retrieval-Augmented Generation (RAG) system's answer is actually grounded in
what it retrieved, or just sounds like it is. Teaches the framework before any example, walks it
through a worked example (a support-bot RAG system that retrieves an outdated policy document and
answers confidently from it anyway), stress-tests it against a case where retrieval genuinely does
fix the problem, and closes on a concrete audit task.

**Why this topic:** RAG is widely treated as "the fix" for LLM hallucination — bolt on a search
step and the model can't make things up anymore. That's only half true. Retrieval only helps if
the retrieved document is actually relevant, actually current, and the model actually uses it
instead of falling back on what it already "knew." This video teaches the difference between
"has access to a source" and "is actually grounded in that source."

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not name or benchmark any specific real RAG product, vendor, or vector database. The worked
example is a generic, illustrative support-bot scenario.

**Source status:** general AI/STEM topic explainer. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated |
| B03 Framework | All 3 questions shown together as a rubric, before any example | Framework-first |
| B04 Worked example | The retrieved (outdated) document AND the model's confident answer shown together | Not narration-only — the mismatch between source and answer must be visible |
| B05 Falsifiability | A case where retrieval genuinely resolves an otherwise-unanswerable question, legible, visibly different resolution from B04 | Side-by-side or sequential-but-both-legible comparison to B04 |
| B06 Task | The 3 questions restated as an audit checklist | Actionable, distinct from B03's framework card |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "RAG: Why 'Looking It Up' Doesn't Guarantee It's True" + @HumanitariansAI.
No narration.

**B01. Exec summary (~0:04–0:20)**
VO: "Hi, I'm Sai Pranavi J.. This video is about Retrieval-Augmented Generation — giving an
AI model a search step so it can look things up instead of guessing — and three questions that
catch the difference between an answer that's actually grounded in what it found, and one that
just sounds like it is."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:20–0:35)**
VO: "Picture a support assistant that searches your company's policy documents before answering.
It finds a real document. It quotes a real policy number. And the answer is still wrong — because
the document it found was replaced eight months ago, and nobody told the search index."
Visual: a chat-style Q&A, a retrieved document card stamped with an old date, a confident answer
bubble.

**B03. Framework (~0:35–0:58)**
VO: "Here's the check, before any example: three questions, every time a retrieval-based answer
shows up. One — Relevant: does the retrieved document actually address this question, or just
share some keywords with it? Two — Current: is this the newest version, or a stale copy the index
never updated? Three — Grounded: is the answer actually built from what was retrieved, or did the
model fall back on what it already 'knew' and just cite the document anyway?"
Visual: rubric card, all 3 questions shown together (Relevant / Current / Grounded).

**B04. Worked example (~0:58–1:25)**
VO: "Back to that support bot. Relevant — yes, it's the right policy document. Current — no, it's
eight months stale. Grounded — doesn't matter, because the document itself is wrong, so a
technically-grounded answer is still a wrong answer. Retrieval didn't fail here. Freshness did."
Visual: the retrieved document (dated, visibly stale) shown side by side with the model's answer,
both the document's date and the current date visible together.

**B05. Falsifiability case (~1:25–1:48)**
VO: "Now the case where retrieval is exactly the fix. Ask a model about an internal product that
launched last week — with no retrieval, it has never seen that word and will either say so, or
invent something plausible-sounding and wrong. Give it the actual internal launch doc, and now
there's real, current, relevant text to ground the answer in. Same mechanism. Completely different
outcome, because this time the source is actually right."
Visual: a "no retrieval" attempt (invented, wrong answer) next to a "with retrieval" attempt
(correct, grounded in a current real document), both visibly labeled.
*[Stress-tests the rubric — retrieval alone isn't the fix; a genuinely relevant, current source is.]*

**B06. Scaffolded task (~1:48–2:08)**
VO: "Here's something to check today. Take one answer your RAG system gave recently. Ask the three
questions: was the source actually relevant, was it actually current, and can you point to the
exact sentence the answer came from. If you can't point to that sentence, you don't know if it's
grounded — you're just hoping."
Visual: the 3 questions restated as a checklist card.

**B07. Takeaway (~2:08–2:22)**
VO: "Giving a model a search step doesn't make it honest. It makes it capable of being honest —
only if what it finds is actually right, and it actually uses it."
Visual: statement card.

**B08. Sign-off (~2:22–2:27)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] Framework (B03) shown fully, before any example
- [ ] B04's stale document and the answer are shown together, not narration-only
- [ ] Falsifiability case (B05) uses a genuinely fair comparison (same mechanism, different
      source quality), not a strawman
- [ ] Scaffolded task (B06) is a concrete action, not a restatement of B03
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] Worked examples clearly generic/illustrative — no real product/vendor named — see FACTCHECK.md

**Estimated runtime:** ~2:27 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-09-17. FACTCHECK open item resolved
(see `FACTCHECK.md`). Cleared to generate Kokoro audio and proceed to previz.
