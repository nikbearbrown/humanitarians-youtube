# Beat Sheet (APPROVED — Gate P, 2026-10-02): "Hallucination: Why Sounding Sure Isn't the Same as Being Right"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly work report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as this fellow's
prior STEM videos — facial recognition, AI-code trust, prompt injection, embeddings, RAG)
**Phase:** 2 — approved for narration lock / audio generation. B04's fabricated citation kept
fully generic. See `FACTCHECK.md`.

---

## Premise

**What this covers:** a reusable 3-question rubric — "Checkable? / Would it hedge? / Does
confidence track difficulty?" — for telling a model's genuine certainty apart from fluent-sounding
phrasing that merely resembles certainty. Teaches the framework before any example, walks it
through a worked example (a fabricated citation delivered in the same confident tone as a real
one), stress-tests it against a case where fluent, confident phrasing is actually warranted (a
well-established fact answered correctly), and closes on a concrete task the viewer can run today.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not name or benchmark any specific real model, vendor, or product. The worked example is
generic and hypothetical, matching the pattern used in this fellow's prior STEM videos.

**Source status:** general AI/STEM topic explainer. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Framework | All 3 questions shown together as a rubric, before any example | Framework-first, per the pattern that scored well on prior STEM videos |
| B04 Worked example | The fabricated citation and the real one shown side by side, same confident tone | Both must look equally fluent — the whole point is they're visually indistinguishable by tone alone |
| B05 Falsifiability | The case where confident phrasing is correct, legible, visibly different resolution from B04 | Side-by-side or sequential-but-both-legible comparison to B04 |
| B06 Task | The 3 questions restated as a checklist | Actionable, not just a restatement of the framework |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "Hallucination: Why Sounding Sure Isn't the Same as Being Right" +
@HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:20)**
VO: "Hi, I'm Sai Pranavi J.. This video is about why a confident-sounding answer from an AI
model isn't the same thing as a correct one, and three questions that catch the difference before
you act on it."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:20–0:34)**
VO: "Ask an AI model a question it knows the answer to, and a question it's making up. It will
answer both in exactly the same confident tone. Nothing in how it sounds tells you which one you
just got."
Visual: two answer bubbles, identical confident styling, one labeled (after a beat) "real" and one
"fabricated" — the point is they look the same until labeled.

**B03. Framework (~0:34–0:58)**
VO: "Here's the check, before any example: three questions. One — checkable: is there something
specific here you could actually verify, like a name, a date, a citation? Two — would it hedge: if
you asked it to rate its own confidence, would it admit uncertainty, or just restate the answer
more firmly? Three — does confidence track difficulty: is it exactly as sure about the hard,
obscure part as the easy, well-known part? That last one is the tell."
Visual: rubric card, all 3 questions shown together (Checkable / Would It Hedge / Confidence Tracks
Difficulty).

**B04. Worked example (~0:58–1:26)**
VO: "Here's a fabricated citation — a real-sounding paper title, a real-sounding journal, a
specific year. It reads exactly as confidently as a real citation would. Checkable? Yes — and that
check is where it falls apart, because the paper doesn't exist. Would it hedge? Not unless asked
directly. Does confidence track difficulty? No — it's just as sure about this invented detail as it
would be about something true and easy."
Visual: two citations side by side, identical fluent styling — one real, one fabricated — with a
"checkable" callout on the fabricated one showing it doesn't resolve to a real source.

**B05. Falsifiability case (~1:26–1:48)**
VO: "Now the case that would break this rubric if it were sloppy. Ask the same model something
simple and true — say, the boiling point of water at sea level. It answers just as confidently.
Run the same three questions: checkable, yes, and it checks out. Would it hedge? No reason to.
Does confidence track difficulty? Yes — this is genuinely easy, and the confidence matches that.
Same fluent tone as B04. Completely different, and correct, answer."
Visual: a simple, verifiably-true answer shown with the same confident styling as B04, its 3
rubric answers resolved differently — all green/confirmed instead of red/failed.
*[Stress-tests the rubric against a naive "confident tone = hallucination" over-trigger.]*

**B06. Scaffolded task (~1:48–2:08)**
VO: "Here's something to check today. Next time an AI model gives you a specific fact, a citation,
a name, a number, ask the three questions. Is it checkable, and did you actually check it? Would it
hedge if pushed? And does its confidence change with how hard or obscure the question actually
is? If the confidence never wavers no matter what you ask, that's not certainty. That's just tone."
Visual: the 3 questions restated as a checklist card.

**B07. Takeaway (~2:08–2:22)**
VO: "A model's tone is generated the same way whether it's right or wrong. The only way to tell the
difference is to ask the question tone can't answer: can this actually be checked?"
Visual: statement card.

**B08. Sign-off (~2:22–2:27)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] Framework (B03) shown fully, before any example
- [ ] B04's fabricated and real citations shown in visually identical confident styling
- [ ] Falsifiability case (B05) uses genuinely similar fluent tone, not a strawman, and shows a
      visibly different resolution from B04
- [ ] Scaffolded task (B06) is a concrete action, not a restatement of B03
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] Worked example is clearly generic/illustrative, not naming a real model or vendor

**Estimated runtime:** ~2:27 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-02. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
