# Claude, Writing Hookify Rules — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:45.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "You might think you type a skill's exact name to switch it on. You don't — you describe the task, and Claude checks that against the file. So: how do you describe the skill you want?" | BrutalistHesitantWriter — types "How do I name the skill I want to use?", corrects "name" → "describe" |
| B01 | 1 stakes / 2 wrong guess, falsified | A Claude skill is a folder with one file, SKILL.md — and near the top sits a plain paragraph saying exactly when to use it. Nobody has to name the skill to switch it on. Say "help me write a rule for hookify," never naming any skill, and it still fires — the paragraph is doing the matching, not you. | a folder opening to one file card; a paragraph card growing beneath it; a "NAME" tag fading out; a request bubble arrowing into the paragraph, landing with a checkmark |
| B02 | 3 mechanism / **4 anchor planted** | Claude reads your request against that paragraph, word for word — no menu, no button, no name required. This skill's paragraph says it fires for "create a hookify rule," "write a hook rule," "configure hookify," or "add a hookify rule." Watch the anchor: type a request that lands inside that wording, and the match fires the skill — Claude opens the file and follows it, step by step. | THE ANCHOR — four phrase chips lighting in turn; a request "add a rule to hookify that blocks rm -rf" arrowing in; one chip recoloring; MATCH → SKILL FIRES; a short step list ticking down |
| B03 | **4 anchor payoff / 5 both directions** | Ask again to add a rule to hookify blocking a dangerous command, and the same match fires every time — same wording in, same skill out. Ask something unrelated instead — say, "explain YAML in general" — and none of that wording is in the paragraph. The skill stays off. Claude still answers, just without this file's playbook. | THE ANCHOR RETURNS — the same four chips firing three times in a row; then a different request arrowing in with no chip lighting, NO MATCH, SKILL STAYS OFF, a small "Claude still answers" note |
| **BCRY** | **6 carry-out** | A skill fires when your words match its description — not when you name it. From there, Claude follows exactly what the file says, and nothing more. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: "I want to add a hookify rule that blocks rm -rf commands. Read the writing-hookify-rules skill first, and walk me through what you'll do before you do it." That last clause matters — asking Claude to explain first is what shows whether the match actually landed on the right skill. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Writing Hookify Rules. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder/description fact; the word-for-word matching mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (name the skill); B01 falsifies it with a case — say "help me write a rule for hookify," never naming a skill, and it still fires |
| Exactly one inference flag | none needed — every claim is read directly off the source's own quoted description field, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the four real trigger phrases; the request that matches them) |
| Both directions | B03 — wording that lands inside the description fires reliably every time (holds); wording that doesn't simply doesn't fire, and Claude still helps another way (flips, not a failure) |
| No design judgment | B01–B03 describe how matching works, never whether the skill's documentation should have explained it better |

## Deliberately not claimed

- **Not that missing the description means Claude is stuck.** B03 is explicit
  that a non-match just means this particular file doesn't fire — Claude
  still answers from general knowledge. The source doesn't claim otherwise
  either.
- **Not a verdict on the skill's design.** The source's B03 framed the
  description text as "the interesting constraint" and its BVDT verdict
  named a "limit" — descriptive language about what the file specifies, not
  a critique of whether it should specify more. Plain keeps the fact, drops
  any judgment.
- **No claim about internal matching mechanics beyond what the source shows.**
  The reel states that wording is compared to the description, because that
  is literally what the source's B00/B03 demonstrate (the description text
  is quoted verbatim as the trigger). It does not speculate about scoring,
  thresholds, or ranking.

## Handoff prompt (BHTF, read aloud)

> "I want to add a hookify rule that blocks rm -rf commands. Read the
> writing-hookify-rules skill first, and walk me through what you'll do
> before you do it."

Why it's worth running: asking Claude to explain itself before acting
surfaces whether the match actually landed on the `writing-hookify-rules`
skill — you never say the skill's name in the prompt, only the task, which
is the whole point this reel makes. This is the source's own worked handoff
idea, cleaned up from the source's garbled phrasing into a real, pasteable
prompt.

---
**GATE P — signed:** ______________________  (human)
