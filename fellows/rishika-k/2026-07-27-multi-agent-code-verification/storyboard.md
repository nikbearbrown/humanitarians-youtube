# STORYBOARD — "The Grader Who Can't Grade Their Own Exam" (urso)
### Why separated verification catches errors a self-checking AI misses

**Format:** CapCut explainer video · 3:30 runtime · 5 scenes
**Modifier:** `urso` — appended verbatim to every image prompt below.
**Audience:** Program reviewers, PM, technical portfolio viewers. Technical literacy, no prior project exposure.
**Target behavior:** After watching, a viewer can explain to a third party why separated verification catches errors a single self-checking AI would miss.
**Arc:** Intuition (grade-your-own-exam) → Mechanism (separation + human oracle written first) → Payoff (the tested counterfactual).

**The sentence the viewer should be able to repeat afterward:**
*"You can't trust anyone to grade their own exam. So the writer and the checkers are separate, and the human answer key comes first — and that caught the AI inventing a rule nobody wrote."*

**Honest scope, held throughout:** The AI self-check is not useless — it catches many errors. It was structurally blind to *this* error: the assumption it invented and then validated against itself. No scene claims self-checking "always" misses.

---

## SCENE 1 — THE HOOK + STAKES (0:00–0:45)
**One idea:** An AI that checks its own work is grading its own exam — and here it decides real loans.

**On screen:** A single figure at a desk marks their own paper test with a red pen, writes "A+". The image resolves into a loan document with the same red pen resting on it.

**Narration (spoken):**
"Would you trust a student to grade their own final exam? Of course not — the same blind spot that caused the mistake will hide it during grading. Now: our system turns plain-English loan rules into working code. And when we ask one AI to write that code and check it too — that's a student grading their own exam. Except here, the exam decides real loans."

**Image prompt:**
Show a single student at a wooden desk marking their own paper test with a red pen and writing a large "A+", the desk surface transitioning to a loan document with the same red pen resting on it, warm overhead light, muted background, white margins. --urso

**Text overlay:** `one AI writing and checking = grading its own exam`

**CapCut note:** The desk-to-loan-document morph carries the stakes in one move. Hold the "A+" for 1 second of silence before narration.

---

## SCENE 2 — THE INTUITION + MECHANISM (0:45–1:40)
**One idea:** The fix is separation — writer, human answer key written first, independent checkers, human approval — nobody grades their own work.

**On screen:** The lone figure splits into a writer at one desk and two checkers at separate desks, with a boxed "answer key" between them and a visible gap and no lines connecting writer to checkers.

**Narration (spoken):**
"So how do you catch a mistake the maker can't see? You separate the roles. One AI writes the code. But first — before any code exists — a human writes the answer key. We call it the oracle, and its timing is the whole trick: written first, it can't be contaminated by the code's assumptions. Then two independent checkers compare the code against that human answer key. They don't confer, so they don't share a blind spot. And a human gives final approval. Nobody grades their own work."

**Image prompt:**
Show three distinct figures at separate desks: one writing code on the left, two checkers on the right comparing papers against a boxed "answer key" placed between them, a clear gap and no connecting lines between the writer and the checkers, limited palette, white background. --urso

**Text overlay:** `human answer key first. then the code. Nobody grades their own work.`

**CapCut note:** Load-bearing scene for the outcome. Stage the answer key snapping into place BEFORE the writer starts — the eye should feel the order. Give "Nobody grades their own work" a 1-second title-card hold.

---

## SCENE 3 — SETUP FOR THE CATCH (1:40–2:25)
**One idea:** A real rule was ambiguous, and the AI silently filled the gap with an invented number.

**On screen:** A printed rule: "deny if the applicant has a recent missed payment." The word "recent" glows. A thought-bubble from a small robot fills in "= under 90 days."

**Narration (spoken):**
"Here's what actually happened. The rule said: deny if the applicant has a recent missed payment. But it never defined 'recent.' The code-writing AI had to pick something — so it quietly decided 'recent' meant 'under 90 days.' Nobody asked it to. Nobody wrote that number down. It invented a rule to fill a gap the human left open — silently, with total confidence."

**Image prompt:**
Show the printed rule "deny if the applicant has a recent missed payment" with the word "recent" glowing in one warm highlight color, and a thought bubble rising from a small robot figure containing handwritten "= under 90 days" with a question mark beside it, white background. --urso

**Text overlay:** `nobody wrote "90 days." the AI did.`

**CapCut note:** This is the turn — the "recent" plant becomes active. Slow the pace slightly. Let "It invented a rule" sit before Scene 4.

---

## SCENE 4 — THE PAYOFF (2:25–3:05)
**One idea:** We ran both approaches on the same ambiguous rule — the AI self-check approved the error because it graded against its own assumption; the human answer key caught the mismatch.

**On screen:** A split screen. LEFT panel labeled "AI checks its own work": one robot writes both the code ("recent = under 90 days") and its own test cases (also "= under 90 days"), a green check stamps "PASS." RIGHT panel labeled "Independent human answer key": an "Answer Key" card reading "recent = (undefined)" faces the same code card, a red mismatch line, two checkers raise red flags, a human reaches in to halt the pipeline.

**Narration (spoken):**
"So we tested it — the same ambiguous rule, two ways. First, we let one AI write the code and its own test cases. It passed itself: green check, all clear. But look at why — it graded its homework against its own answer key, using the same invented 'ninety days' in both the code and the test. The boundary case sailed through as correct. Then we ran it against the human answer key, which never said ninety days. That version caught the mismatch. To be clear: self-checking isn't useless — it catches plenty of errors. But it was blind to this one, because it was checking its own assumption. The independent key wasn't."

**Image prompt:**
Show a split-screen diagram on a white background. Left half labeled "AI checks its own work": a single robot figure connected to both a code card reading "recent = under 90 days" and a test-case card also reading "= under 90 days," a large green checkmark stamping "PASS" below them. Right half labeled "Independent human answer key": an "Answer Key" card reading "recent = (undefined)" beside the same code card reading "recent = under 90 days," a red mismatch line between them, two checker figures raising red flags, a human figure reaching in to halt the pipeline, thin black lines, green accent only on the left, red accent only on the right, clean sans-serif labels. --urso

**Text overlay:** `self-check: PASS (graded against its own assumption). human key: CAUGHT IT.`

**CapCut note:** Reveal the LEFT panel (green PASS) first and let it land as if it's the happy ending — hold ~1 second on the green check. Then bring in the RIGHT panel on "Then we ran it against the human answer key," so the red flags feel like a correction to the false all-clear. The green-then-red order is the whole point; don't show both panels at once. Hold the final two-panel frame for a full second.

---

## SCENE 5 — THE TAKEAWAY (3:05–3:30)
**One idea:** Hand the viewer the exact sentence to repeat.

**On screen:** The Scene 2 separation image returns at low opacity behind a clean title card.

**Narration (spoken):**
"So in one line: you can't trust anyone to grade their own exam — so the writer and the checkers are kept separate, the human answer key comes first, and that caught the AI inventing a rule nobody wrote. Self-checking can miss the errors it invented. Separation catches them."

**Image prompt:**
Show a clean closing title card on a white background with the separated-roles illustration faded behind it at low opacity, the sentence "Self-checking can miss what it invented. Separation catches it." in bold sans-serif centered, generous white margins, minimal style. --urso

**Text overlay:** `Self-checking can miss what it invented. Separation catches it.`

**CapCut note:** End on silence and the title card. No music sting over the last line — the sentence is the last thing they hear and read.

---

## PRODUCTION NOTES

**Pacing:** Scene 1 hooks and sets stakes in one move. Scene 2 installs the analogy and the mechanism together (separation + oracle-first). Scenes 3–4 are the plant-and-payoff, paced slightly slower. Scene 5 hands over the sentence. Total 3:30.

**Recurring visual motifs — keep consistent:**
- **Red** = the error/flag, and nothing else — except the single green PASS in Scene 4's left panel, which is quarantined to mark the "false all-clear."
- **Glowing "recent"** planted in Scene 1's loan document, activated in Scene 3, resolved in Scene 4. Same warm highlight each time.
- **The gap between writer and checkers** (Scene 2) is what makes Scene 4 legible. Never connect them.
- **Oracle-first ordering** — in Scene 2, the answer key lands before the writer moves. That timing is the mechanism, so stage it, don't just draw it.

**Modifier:** `--urso` is appended verbatim to all five image prompts. One modifier, applied consistently — do not mix with another style string or the palette and figures will drift across scenes.

**Handoff:** CapCut-ready. For a live-talk slide version, run `deck` on this content — the arc is validated, intake will be fast.
