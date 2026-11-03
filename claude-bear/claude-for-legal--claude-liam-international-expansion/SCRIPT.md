# What Comes First When You Hire Abroad? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone on a legal team wants to hire their first person in Germany. Wrong first move: draft a contract. What they actually need first is the worker's classification. Liam, take them through it." | BrutalistHesitantWriter — types "What contract do we need to hire someone in Germany?", corrects "contract" → "classification" |
| B01 | 1 stakes / 2 wrong guess, falsified | You could draft an employment contract today, calling the role whatever you like. But a contract's label doesn't decide the classification — the country's labor law does. Call someone a contractor while you set their hours, hand them your equipment, and take them as their only client, and a local court will call them an employee anyway, no matter what the page says. | a "CONTRACT" card with an editable "CONTRACTOR" label; clock/toolbox/single-client icons all light up employee-shaped anyway; a stamp comes down reading EMPLOYEE |
| B02 | 3 mechanism / **4 anchor planted** | A real hiring plan runs three checks before any contract gets written: how the role is classified, who will be the legal employer on paper — your own entity, or an Employer of Record standing in for one — and which local rules are mandatory no matter what the contract says, like notice periods and statutory benefits. Watch the anchor: a developer in Berlin, forty hours a week, one client, using your laptop and your tools. | three check chips (classification / legal employer / mandatory terms); THE ANCHOR — a dim, icon-only developer card off to the side |
| B03 | **4 anchor payoff / 5 both directions** | Run the Berlin developer through the checks: full control over their hours, one client, your equipment — that's employee-shaped, no matter what the contract calls them. Passing as contractor-shaped today doesn't mean it stays that way; change how the work actually runs and the classification can flip later, same contract. And landing on employee doesn't mean you need your own German entity tomorrow — an Employer of Record can be the legal employer on paper while you sort that out. | THE ANCHOR RETURNS — the dim card fills in and joins the list; splits into "classification can still flip" and "doesn't require your own entity" |
| **BCRY** | **6 carry-out** | The contract can't fix a bad classification. Work out how the role is classified and who the legal employer will be before you draft anything — the country's labor law decides that, not the label on the page. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I'm planning to hire our first employee in a new country. Before drafting anything, walk me through how the role would likely be classified there under local labor law, the difference between opening our own entity there versus using an Employer of Record, and which statutory terms — notice period, benefits, termination rules — would apply once it's classified. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | What Comes First When You Hire Abroad? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the contract-doesn't-decide fact; the three-check mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (draft a contract); B01 falsifies it directly — a court reclassifies based on the actual working relationship, not the contract's label |
| Exactly one inference flag | none needed — the account describes the generic shape of an international-hiring implementation plan (classify / choose legal employer / attach mandatory terms), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the Berlin developer) |
| Both directions | B03 — passing as contractor-shaped today doesn't mean the classification is locked in; landing on employee-shaped doesn't mean you need your own entity |
| No design judgment | B01–B03 state what the classification and legal-employer decisions are and why a contract alone can't settle them, never a verdict on whether any specific skill or tool was well designed |

## Deliberately not claimed

- **Not legal advice for any specific country.** The reel names Germany once,
  as a concrete anchor, but never states German law's actual test or
  thresholds — those vary and would be false precision from a reconstructed
  script. It states the *shape* of the decision (classification, legal
  employer, mandatory terms), not a jurisdiction's specific rule.
- **Not that a contract is useless.** The reel never says skip the contract —
  only that it has to follow the classification and legal-employer decision,
  not precede it, or it's written for the wrong relationship.
- **Not a specific Claude product feature.** Because the source sheet's
  actual facts were never written (see QUESTION.md), this script describes
  the generic mechanics of an international-hiring implementation plan
  rather than citing any particular tool's UI or output format.
- **No accusation that anyone was negligent.** Drafting a contract before
  classifying the role is presented as an ordinary, common first instinct,
  not a failure by any named person or team.

## Handoff prompt (BHTF, read aloud)

> "I'm planning to hire our first employee in a new country. Before drafting
> anything, walk me through how the role would likely be classified there
> under local labor law, the difference between opening our own entity there
> versus using an Employer of Record, and which statutory terms — notice
> period, benefits, termination rules — would apply once it's classified."

Why it's worth running: it forces the classification and legal-employer
questions to the front, before a single clause gets drafted — the exact
order the reel argues for.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
