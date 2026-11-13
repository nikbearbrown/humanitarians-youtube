# Beat Sheet (APPROVED — Gate P, 2026-10-06): "The Classifier That Learned When Not to Guess"

**Creator:** Sai Pranavi J. | Weekly work video
**Format:** `work-report`, same register as this fellow's prior Project 29 reports
**Phase:** 2 — approved for narration lock / audio generation.

---

## Premise

**What this covers:** a real continuation of the B2 source-classification fix (first closed
2026-08-30, narrowed further 2026-09-07). 21 items were falling through the keyword/pattern
classifier to "Unknown Source." Prior fixes brought that down to 13 already resolved as of today
— verified live by re-running the real `identifySource()` function against the actual 21 DB rows
— leaving a genuine residual of 8 generic headlines no fixed keyword list can resolve without
false-positiving on unrelated content. This video covers adding a local-LLM (Ollama) fallback
classification step for just that residual, and the honestly modest result: it resolved 1 of 8,
correctly declining to guess on the rest rather than force a label onto genuinely ambiguous
content.

**Why this is worth a video:** the engineering message is "the model declining to answer was the
correct outcome, not a shortfall" — a useful real example of what principled, honest LLM-assisted
classification looks like, rather than reporting a bigger number by loosening the bar.

**Source status:** real Project 29 (`mycroft`) fix, fully verified against live DB data —
see `FACTCHECK.md`/`SOURCES.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Setup | The 21→13 resolved / 8 residual breakdown, with 2-3 real example headlines | Real titles, not paraphrased |
| B04 Discovery/Fix | The new node's position in the pipeline + its 3 design rules (only-Unknown, validate-category, fail-open) | Diagram, not just narration |
| B05 Proof | The live verification numbers: 0 mutated / 1 resolved / 7 declined / 0 errors | All 4 numbers on screen together |
| B06 Honest limits | The 1-of-8 framed explicitly as a correct, not partial, result | No softening — matches house style |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Classifier That Learned When Not to Guess" + @HumanitariansAI. No
narration.

**B01. Exec summary (~0:04–0:22)**
VO: "Hi, I'm Sai Pranavi J.. This video is about a small fix to our regulatory
intelligence pipeline — teaching it to ask a local AI model for help on headlines it couldn't
classify, and why the honest result was a model that correctly said 'I don't know' most of the
time."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:22–0:38)**
VO: "Twenty-one real headlines were falling through our classifier to 'Unknown Source.' Over the
last few weeks, keyword fixes brought that down to eight. This week: what happens when you hand
those eight to an AI model instead of another keyword rule."
Visual: a counter ticking 21 → 13 resolved → 8 remaining, landing on "8."

**B03. Setup (~0:38–1:04)**
VO: "Before touching any code, I re-ran the actual classifier — the real function, not a copy —
against all 21 database rows. Thirteen are already resolved by fixes already shipped. The
remaining eight are headlines like 'Understanding the Regulations of 24-Hour Trading' or 'Know
Your Client: Key Requirements for Financial Services.' Generic enough that no fixed keyword list
can catch them without also catching things that have nothing to do with financial regulation."
Visual: 2-3 real example headlines shown directly, with a caption "no keyword list resolves these
safely."

**B04. Discovery / The fix (~1:04–1:34)**
VO: "So instead of one more brittle keyword rule, I added a new step: for exactly the items still
marked Unknown Source, and only those, ask a local AI model to pick the best-fitting category
from the four we already track — or say none of them fit. Every other item is never touched. If
the model's answer isn't one of the four real categories, or the call fails for any reason, the
item keeps its original label. Nothing gets silently mislabeled."
Visual: pipeline diagram — the new node inserted between the existing classifier and the next
step, with a highlighted "only acts on Unknown Source" condition.

**B05. Proof (~1:34–2:04)**
VO: "I tested this against the real eight headlines, running the exact code that would ship, not
a simulation. Zero of the thirteen already-resolved items were touched. Of the eight, the model
correctly classified one — an enforcement-actions piece that does belong to one of our tracked
categories. It declined to guess on the other seven. I also killed the connection to the AI model
entirely and reran it: every item kept its original label, nothing broke."
Visual: the 4 real numbers on screen together — 0 mutated, 1 resolved, 7 declined, 0 errors — plus
the one resolved headline and its new label.

**B06. Honest limits (~2:04–2:28)**
VO: "One out of eight is not a big number, and I'm not going to pretend it is. But it's the
correct number. Those seven declined headlines are genuinely generic — a KYC explainer, a
24-hour-trading explainer, law-firm monthly digests. They don't actually belong to any of the
four categories this pipeline tracks. A model that forced a label onto all eight would have
looked more impressive and been more wrong."
Visual: statement card, "1 of 8 — and that's the correct number," with the 7 declined headlines
dimmed below it.

**B07. Takeaway (~2:28–2:46)**
VO: "When you add an AI model to a pipeline, the win isn't always a bigger number. Sometimes the
win is a system that knows the difference between 'I can classify this' and 'I shouldn't guess' —
and does the second one on purpose."
Visual: statement card.

**B08. Sign-off (~2:46–2:51)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B03's 8 example headlines are real, verbatim DB titles, not paraphrased
- [ ] B04 diagram clearly shows the new node only acts on Unknown Source items
- [ ] B05's 4 numbers (0 mutated / 1 resolved / 7 declined / 0 errors) all visible together
- [ ] B06 explicitly frames 1-of-8 as correct, not as an apology or a shortfall
- [ ] Silent title card present; brand/fellow sign-off card present

**Estimated runtime:** ~2:51 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-06. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
