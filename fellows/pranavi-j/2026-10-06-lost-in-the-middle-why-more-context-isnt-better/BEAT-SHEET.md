# Beat Sheet (APPROVED — Gate P, 2026-10-06): "Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly work report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as this fellow's
prior STEM videos)
**Phase:** 2 — approved for narration lock / audio generation. Fully generic worked example, no
real model/vendor benchmarked — see `FACTCHECK.md`.

---

## Premise

**What this covers:** the well-documented "lost in the middle" effect — language models given a
long context (a long document, a long conversation, many retrieved chunks) are reliably better at
using information placed near the *start* or *end* of that context than information buried in the
*middle*, even when every fact is equally present and equally relevant. Teaches a 3-question
rubric — "How long is the context? Where does the key fact sit? Would moving it change the
answer?" — before any example, walks through a worked example (the same fact, same question,
different position in the context), stress-tests it with a falsifiability case (a short context,
where position stops mattering), and closes on a concrete task the viewer can run today.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not name or benchmark any specific real model's long-context behavior (the exact shape and
severity of this effect varies by model and has shifted over time as providers address it). The
worked example is a fully generic, illustrative long-document scenario.

**Source status:** general AI/STEM topic explainer, describing a widely-documented class of
behavior in long-context language models, not a specific benchmark claim. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Mechanism | A long document with a single key fact shown at 3 candidate positions (start/middle/end) | Must visually show "middle" as genuinely buried, not just labeled |
| B04 Worked example | The same fact, same question, planted in the middle — model's answer shown as unreliable/missed | Position is the only variable that changes |
| B05 Falsifiability | The same fact moved to the start or end — same model, same question, now reliably found | Visibly different resolution from B04 |
| B06 Task | The 3 questions restated as a checklist | Actionable, not just a restatement of the framework |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer" +
@HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:20)**
VO: "Hi, I'm Sai Pranavi J.. This video is about a strange, well-documented habit of AI
models reading long documents — they're much better at using facts at the start or end than
facts buried in the middle, even when nothing else about those facts is different."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:20–0:36)**
VO: "Give a model a short paragraph with one key fact, and it finds it every time. Give it a
hundred-page document with that exact same fact buried on page fifty, and it can miss it
completely — not because the fact is hard to understand, but because of where it happens to
sit."
Visual: two document icons side by side — a short one with a highlighted fact, and a long one
with the same fact buried deep inside, both labeled with the same question.

**B03. Mechanism (~0:36–1:02)**
VO: "Here's the pattern researchers have repeatedly found. Picture a long context as a line —
start, middle, end. Models are reliably better at using information near the two ends than
information in the middle. It's not that the model can't technically see that part of the text.
It's that attention across a long input isn't evenly distributed — the beginning and end get
disproportionately more of it."
Visual: a long horizontal bar representing the context, with an attention-strength curve drawn
over it — high at both ends, dipping in the middle.

**B04. Worked example (~1:02–1:30)**
VO: "Say you hand a model a long onboarding document and ask one specific question, and the
answer is stated once, buried in the middle section. Ask the model, and it might miss it
entirely, or guess at an answer that isn't actually in the text. The fact was right there. It
just wasn't in a part of the document the model was reliably attending to."
Visual: a long document with the key fact highlighted in the middle section, the model's answer
shown as wrong or "not found," with a red marker on the middle of the attention curve.

**B05. Falsifiability (~1:30–1:54)**
VO: "Now move that exact same fact, same document, same question — just place it in the first
paragraph or the last paragraph instead. Ask again, and the model gets it right. Nothing about
the fact changed. Only where it sat in the document did."
Visual: the same document, same fact, now shown at the start (or end), the model's answer now
correct, a green marker on the end of the attention curve.

**B06. Scaffolded task (~1:54–2:14)**
VO: "Here's something to check today. Next time you're stuffing a long document or a long chat
history into an AI model and asking it to use one specific detail, ask yourself: how long is the
context? Where does the key fact actually sit? And would moving it toward the start or end change
whether the model finds it? If the answer is yes, you've just found a real blind spot — not a
reason to distrust the model entirely, a reason to put the important part where it'll actually be
seen."
Visual: the 3 questions as a checklist card.

**B07. Takeaway (~2:14–2:28)**
VO: "A model that misses a fact buried in page fifty isn't failing to understand it. It's
reading unevenly — and knowing that changes where you put the thing you actually need it to
find."
Visual: statement card.

**B08. Sign-off (~2:28–2:33)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] Mechanism (B03) shown as a real attention-curve diagram, not just asserted in narration
- [ ] B04's "buried in the middle" position is visually obvious, not just labeled
- [ ] Falsifiability case (B05) changes only position — same fact, same document, same question
- [ ] Scaffolded task (B06) is a concrete action, not a restatement of B03
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] No specific real model/vendor named or benchmarked; no fabricated percentage/statistic

**Estimated runtime:** ~2:33 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-06. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
