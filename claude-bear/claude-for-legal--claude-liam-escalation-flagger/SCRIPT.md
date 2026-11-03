# Claude, Escalation Flagger. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes escalation-flagger decides what's risky using its own judgment. It doesn't. It matches input against criteria written in SKILL.md. So — is it flagging by judgment, or by match?" | BrutalistHesitantWriter — types "Claude's escalation flagger — is it flagging things it thinks are risky?", corrects "thinks" → "matches" |
| B01 | 1 stakes / **4 anchor planted** | A Claude Skill is just a folder Claude reads before it works. This one is named escalation-flagger, and everything it knows lives in one file: SKILL.md — plain sentences, not code. Open it, and you'd see something like a numbered list of criteria, checked one after another. Claude reads that file, then follows it. The file decides what gets flagged, not Claude. | THE ANCHOR — a SKILL.md card opening, a numbered checklist of criteria typing in top to bottom, one lighting up with a checkmark |
| B02 | 2 wrong guess, falsified / 3 mechanism | It can look like Claude is sensing which things feel risky — that's the guess most people make. It isn't. Claude checks each item on the list, one criterion after another, and flags only where one actually matches. Remove a criterion from that file, and inputs that used to trigger it stop being flagged. Nothing hidden fills the gap. | a linear checklist, an input checked against each item in turn; one criterion struck out; the same input passes through afterward with no flag |
| B03 | **4 anchor payoff** / 5 both directions | Go back to that same SKILL.md and its list of criteria. Run the same input through escalation-flagger twice, and you get the same match and the same flag both times — for as long as the input matches something written there. Send through a case the list never anticipated, and nothing gets flagged — not because Claude judged it safe, but because nothing in the file matched it. | THE ANCHOR RETURNS — the same SKILL.md card, run twice side by side, the same criterion lit both times; then a new input shape with no matching criterion, passing through unflagged |
| **BCRY** | **6 carry-out** | A flag isn't Claude's judgment call — it's a match against criteria written in a file. Same match, same flag, every time; no match, no flag, however it looks to a person. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: write me a SKILL.md with three short numbered criteria for flagging something you deal with often. Then hand it inputs on both sides — one that matches, one that doesn't — and watch whether the flag follows the file, not a feeling. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Escalation Flagger. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder/file split and the checklist shape; the step-by-step matching mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude judges what's risky); B02 falsifies it with a case — remove a criterion from the file, and inputs that used to trigger it stop being flagged, nothing hidden notices instead |
| Exactly one inference flag | none needed — every claim describes the general, publicly documented mechanism of a Claude Skill (a folder, a `SKILL.md`, criteria checked in order); no claim is made about what `escalation-flagger` specifically checks for or where it escalates to, since the source never says and the real file is unreachable (see QUESTION.md) |
| One anchor, planted early, paid off late | B01 → B03 (the SKILL.md card with its numbered checklist of criteria) |
| Both directions | B03 — repeatable match and flag when the input stays inside what the file describes (holds); nothing gets flagged, not from judgment but from no match, when the input falls outside it (flips) |
| No design judgment | B02/B03 state the matching mechanism and its edge as facts about how a Skill runs, never a verdict on whether `escalation-flagger`'s SKILL.md was written well |

## Deliberately not claimed

- **Not what `escalation-flagger` specifically checks for, or who/what it
  escalates to.** The source's own narration never says — four of its
  seven beats carry a literal unfilled `>` template placeholder exactly
  where that content should be (see QUESTION.md). This reel states only
  what's generically true of any Claude Skill's matching mechanism, with
  `escalation-flagger` as the example's name and its plain-language
  category of behavior (checks input, flags matches for a human), never as
  a source of invented criteria.
- **Not a verdict on the design.** The source's B03 called this "the
  Teardown moment" — Teardown language. Plain keeps the same underlying
  mechanism (repeatable inside the spec, silent outside it) but states it
  as a boundary, not a critique of the file.
- **No claim that Claude never reasons.** B02 states plainly that *this*
  mechanism — a Skill's written criteria, checked step by step — decides
  the flag, not that Claude never reasons about anything anywhere.

## Handoff prompt (BHTF, read aloud)

> "Write me a SKILL.md with three short numbered criteria for flagging
> something I deal with often. Then hand it inputs on both sides — one
> that matches, one that doesn't — and watch whether the flag follows the
> file, not a feeling."

Why it's worth running: watching whether the flag fires exactly where a
criterion matches and stays silent everywhere else surfaces whether the
match-not-judgment claim from B01–B03 actually holds for a Skill written
by hand.

---
**GATE P — signed:** ______________________  (human)
