# PEDAGOGY AUDIT — vox-heavy-tail-yank

Gate P audit. Every item must pass before audio generation.

---

## Act structure audit

| Act | Required | Beats | Status |
|---|---|---|---|
| COLD OPEN | 1–3 beats: concrete situation and stakes, no thesis/verdict | B01 (title), B02 (settling trace), B03 (yank) | ✓ B02–B03 show the case concretely: a running average that looks stable, then lurches. No thesis stated yet. |
| THE QUESTION | 1 beat (mandatory): named on screen AND in narration | B04 | ✓ "When can one new observation undo everything a thousand already told you?" — on the question card AND in B04 narration. |
| THE PROBLEM | 2–5 beats: naive expectation + why a reasonable person holds it | B05 (CLT promise), B06 (the hidden condition), B07 (quote) | ✓ B05 gives the naive expectation ("more data, more confidence — CLT"), B06 reveals the condition, B07 names the failure mode. |
| THE MECHANISM | bulk beats: why reality diverges from naive expectation | B08 (Gaussian trace), B09 (heavy-tail trace), B10 (compare), B11 (extreme weight) | ✓ Four beats showing the mechanism: first the "good" case, then the "broken" case, then the contrast, then WHY. |
| THE IMPLICATION | 1–3 beats: where this bites in the real world | B12 (STILL·ai dashboard), B13 (bar chart), B14 (quote) | ✓ Three beats grounding the mechanism in AI deployment (average error cost metrics). |
| THE EXAMPLE | 1 beat right before RECAP: concrete illustrative instance | B15 (document-processing AI) | ✓ 10 normal docs (avg 0.3s) + 1 outlier (300s, full re-index) → running average yanked to 27s. Numbers illustrative, labeled in FACTCHECK. |
| RECAP | Endcard: question → answer in one line + topic label | B16 | ✓ "Averages converge when extremes are bounded. When they're not, the next observation can beat a thousand." No book title or chapter number on screen. topic: "COMPUTATIONAL SKEPTICISM" |

Act order correct: cold open → question → problem → mechanism → implication → example → recap ✓

---

## Key-case cold open check

B02–B03 show a concrete instance of the mystery:
- B02: a safety team tracks an AI system; after 300 cases, the running average LOOKS stable (concrete situation)
- B03: one extreme case arrives and the average lurches more than all 300 combined (the stakes)

The situation is SHOWN (running-average trace, then the yank) not summarized. No thesis or verdict before B04. ✓

---

## Gap formula on THE QUESTION beat (B04)

B04 narration: "When can one new observation undo everything a thousand already told you — and how do you know if you're in that world?"

Structure:
- X (what you expect): averaging many observations should stabilize the mean
- Y (what happens): one new observation undoes it all
- The mystery: "how would you know if you're in that world?" — the practical question

The question is named on screen (question card copy) AND spoken in narration. ✓

---

## Utility-framing lint

Scanning all narration beats for: "is critical for" / "important to understand" / "we'll cover" / "in this video"

| Beat | Narration excerpt | Verdict |
|---|---|---|
| B01 | "One data point can beat a thousand-point average. Here is why." | ✓ clean |
| B02 | "A safety team has been tracking an AI system's error costs..." | ✓ clean |
| B03 | "Then one case arrives. The average lurches..." | ✓ clean |
| B04 | "When can one new observation undo everything..." | ✓ clean |
| B05 | "Averaging feels like the safe move. More data, more confidence..." | ✓ clean — mystery framing |
| B06 | "The theorem has a condition buried in it..." | ✓ clean |
| B07 | Quote beat | ✓ clean |
| B08 | "Watch a running average from a well-behaved distribution..." | ✓ clean |
| B09 | "From a heavy-tailed distribution, it doesn't settle..." | ✓ clean |
| B10 | "Same observation count. Different distribution..." | ✓ clean |
| B11 | "In a Gaussian, extreme values grow increasingly improbable..." | ✓ clean |
| B12 | "When an AI system is evaluated on average error cost..." | ✓ clean |
| B13 | "Ninety-nine errors at thirty dollars. One error at three million..." | ✓ clean |
| B14 | Quote beat | ✓ clean |
| B15 | Endcard narration | ✓ clean |

No utility-framing violations. ✓

---

## Vocabulary law check

Every technical term is verified against FACTCHECK.md terms table:

| Term | Debuts at | Beat that created the need | Verdict |
|---|---|---|---|
| running average | B02 | B01 (cold open hook) | ✓ viewer watches a trace build before hearing the name |
| Central Limit Theorem | B05 | B04 (question: why did anyone trust the mean?) | ✓ CLT is the answer to B04's implicit "why do we trust averages?" |
| finite variance (condition) | B06 | B05 (CLT says mean settles — WHEN?) | ✓ named as the condition the CLT requires, after B05 established the promise |
| heavy-tailed distribution | B06 | B05/B06 contrast | ✓ named as what breaks the condition |
| convergence | B08 | B07 (quote: "no matter how many") | ✓ viewer needs a word for "it stops moving" |
| tail-aware metrics | B14 | B12–B13 (implication: averages fail) | ✓ named as the alternative after showing the failure |

No term debuts before its pedagogical need is created. ✓

---

## Equations check

No equations appear in narration, visuals, or card copy. The CLT condition is stated verbally ("extreme events must be rare enough...") without algebraic notation. The mechanism is carried entirely by the trace visuals. ✓

Card exclusions confirm: no CLT full statement, no confidence-interval formulas. ✓

---

## Recap endcard check (B16)

- Restates the question: ✓ "Averages converge when extremes are bounded. When they're not, the next observation can beat a thousand."
- No book title or chapter number on screen or in narration ✓
- card.topic: "COMPUTATIONAL SKEPTICISM" ✓

---

## Topic check
B01 scene: "COMPUTATIONAL SKEPTICISM" eyebrow (TEAL text, DISPLAY font) ✓
B16 endcard card.topic: "COMPUTATIONAL SKEPTICISM" — no book title, no chapter number on screen ✓
B16 narration: no book title or chapter number ✓

---

## THE EXAMPLE beat (B15)
B15 presents a document-processing AI: 10 normal files (avg 0.3s) + 1 outlier triggering full re-indexing (300s) → running average yanked to 27s (90× the prior average). All numbers illustrative and labeled in FACTCHECK.md. Shows the yank mechanism in a concrete deployment domain (document pipeline) distinct from the bar-chart domain (error cost) in B13. ✓

---

## Length law

Derived duration: ~157s ≈ 2:37 — well under the 5:00 hard cap. ✓

---

VERDICT: PASS
