# When Is a Claude Legal Memo Actually Reliable? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a legal memo means a final legal opinion — Claude's confident answer on their case. Wrong word — a memo is a working draft analysis, not a verified opinion. Liam, take them through it." | BrutalistHesitantWriter — types "Can Claude give me a legal OPINION on my case?", corrects "OPINION" → "MEMO" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's tempting to think a confident, well-cited memo is ready to act on — every case named, every rule stated plainly. But say one of those citations names a real case, correctly, by name and by holding — except that case was overruled last year. A memo that reads confidently carries that dead case forward as if it still controlled the outcome, and it reads exactly like every correct citation around it. Real legal memos are a draft analysis of the law as it stands, not a verified answer, until every citation in them is checked. | a memo page dense with citations; one citation gets circled in accent, then struck, with a caption revealing why |
| B02 | 3 mechanism / **4 anchor planted** | A memo handoff that actually works has three parts: the legal question and facts in, a structured analysis out — issue, rule, application, conclusion — and a required verification step before anyone relies on it. Watch the anchor: that same memo comes back with one citation stamped in the margin. Not confirmed. Flagged to check. | three labeled parts lighting in turn (question / draft / verify); THE ANCHOR — a memo page with one citation stamped "FLAGGED — VERIFY" |
| B03 | **4 anchor payoff / 5 both directions** | That flagged citation gets checked against the law as it stands today, and only once every citation in the memo is confirmed does it move from draft analysis to something an attorney can actually rely on. But an unflagged citation isn't automatically confirmed — no flag doesn't mean checked, someone still has to look. And a memo that comes back heavily corrected at that verification step isn't a failure either — catching a wrong or outdated citation there is the verification step doing exactly its job. | THE ANCHOR RETURNS — the flagged citation gets checked and the memo is stamped "VERIFIED — RELIABLE"; then splits into "no flag ≠ confirmed" and "corrected ≠ failure" |
| **BCRY** | **6 carry-out** | A legal memo isn't reliable because it reads confidently — it's reliable once every citation in it has been checked. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Take a real legal question you're working on. Ask Claude to draft an issue-rule-application-conclusion memo answering it, with every case citation flagged to check. Then verify each citation against the law as it stands today before anyone treats the memo as reliable. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | When Is a Claude Legal Memo Actually Reliable? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the confident-memo-isn't-checked gap; the three-part mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (memo = final opinion); B01 falsifies it with a concrete case — an overruled citation that reads exactly like every correct one around it |
| Exactly one inference flag | none needed — the account describes the generic shape of a memo handoff (draft, flag, verify) and ordinary legal-practice convention (memos are predictive, internal analysis; citations get checked against current law), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the citation-stamped memo page becomes the verified page) |
| Both directions | B03 — no flag doesn't prove confirmation (someone still has to look); heavy correction doesn't prove failure (catching an error at verification is the step working) |
| No design judgment | B01–B03 state what a memo handoff needs and why, never a verdict on whether any specific skill or tool was well designed |

## Deliberately not claimed

- **Not that Claude made an error.** B01's case is about a citation that reads
  correctly and confidently — the failure mode is trusting confidence without
  checking, not a mistake Claude specifically made.
- **Not a specific Claude product feature.** Because the source sheet's actual facts
  were never written (see QUESTION.md), this script describes the generic mechanics of
  a legal-memo drafting handoff (question in, flagged draft out, citation verification)
  rather than citing any particular skill's steps, tool, or output format.
- **No accusation that anyone was negligent.** The overruled citation in B01 is
  presented as an ordinary risk of legal research — law changes — not a failure by a
  named person or team.

## Handoff prompt (BHTF, read aloud)

> "Take a real legal question you're working on. Ask Claude to draft an
> issue-rule-application-conclusion memo answering it, with every case citation
> flagged to check. Then verify each citation against the law as it stands today
> before anyone treats the memo as reliable."

Why it's worth running: it forces the draft to separate what it's confident about
(the structure of the analysis) from what still needs a human check (whether the law
it cites is actually still good law) — which is exactly the boundary the reel is
built around.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
