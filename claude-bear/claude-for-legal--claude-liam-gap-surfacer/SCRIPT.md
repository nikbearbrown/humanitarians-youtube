# What Is a Gap-Surfacer Actually Looking For? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone on a legal team asks if a contract review tool catches bad clauses in what's already there. Wrong word. What it actually catches is missing ones. Liam, take them through it." | BrutalistHesitantWriter — types "Does this contract have any bad clauses?", corrects "bad" → "missing" |
| B01 | 1 stakes / 2 wrong guess, falsified | You'd guess a tool like this reads the contract and flags whatever clauses are badly written — a quality check. It isn't one. Its checklist has a line item, say governing law, and it isn't judging whether that clause is any good. It's only asking one thing: does matching text show up anywhere in this document at all. | a "QUALITY CHECK" magnifying-glass card struck through; a checklist chip + scan sweep ending on a lit MATCH |
| B02 | 3 mechanism / **4 anchor planted** | Here's how the check actually runs: it walks a checklist one line at a time — governing law, indemnification, assignment — and for each one, scans the whole document for matching text. Watch the anchor: the assignment line comes back with no match anywhere. Flagged, not yet resolved — that's as far as the scan alone can tell you. | THE ANCHOR — three checklist chips scanned; two light green MATCH, the third (assignment) ends dim, red-outlined, NO MATCH |
| B03 | **4 anchor payoff / 5 both directions** | Turns out the protection was there the whole time — just filed under Transfer of Rights instead of Assignment, so the checklist's exact wording missed it. A match doesn't prove a clause is good enough, and a no-match doesn't prove it's actually gone — both times, a person still has to open the page and read it. | THE ANCHOR RETURNS — the dim NO MATCH card connects to a highlighted "Transfer of Rights" clause and lights up; splits into "match ≠ good enough" and "no-match ≠ gone" |
| **BCRY** | **6 carry-out** | A gap-surfacer doesn't tell you a clause is missing — it tells you where to look. No match found is a lead, not a verdict; the read is still yours. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Take a document you're responsible for and a short checklist of things it should contain. Ask Claude to scan for matches and flag every item with none — then, for each flag, ask it to also check whether the same coverage might be sitting under different wording before calling it missing. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | What Is a Gap-Surfacer Actually Looking For? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the absence-not-quality fact; the checklist-walk mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (catches bad clauses); B01 falsifies it directly — the checklist only asks whether matching text exists, never whether it's well written |
| Exactly one inference flag | none needed — the account describes the generic shape of a checklist-vs-document gap check (walk a list, scan for matches, flag absences), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the assignment-clause checklist item) |
| Both directions | B03 — a match doesn't prove the clause is adequate (match ≠ good enough); a no-match doesn't prove the protection is gone (no-match ≠ gone, it can be under different wording) |
| No design judgment | B01–B03 state what the check does and why a checklist match can't settle the question either way, never a verdict on whether any specific skill or tool was well designed |

## Deliberately not claimed

- **Not that the check is useless.** The reel never says a no-match flag is
  worthless — only that it's a pointer to check, not a finished finding.
- **Not a specific Claude product feature.** Because the source sheet's
  actual facts were never written (see QUESTION.md), this script describes
  the generic mechanics of a checklist-vs-document gap check rather than
  citing this particular skill's exact steps, output format, or trigger
  phrases.
- **No accusation that anyone drafted badly.** The assignment clause turning
  up under different wording is presented as an ordinary labeling mismatch,
  not a failure by any named person or team.

## Handoff prompt (BHTF, read aloud)

> "I have a document and a short checklist of things it's supposed to
> include. Scan the document, flag every checklist item with no matching
> text anywhere in it, and for each flag, tell me whether equivalent
> coverage might exist under different wording before calling it missing."

Why it's worth running: the exercise surfaces the same distinction the reel
is built around — a flagged item isn't a finished verdict, it's the list of
places a person still needs to actually read.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
