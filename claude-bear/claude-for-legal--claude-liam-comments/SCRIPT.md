# Claude, Comments. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet — see
QUESTION.md; source facts are real, unlike the placeholder-shell siblings
in this family). Register: **Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude knows which comment deadlines are coming due on its own. It doesn't — it only tracks what a skill tells it to track. The real question: how does Claude track a filing deadline?" | BrutalistHesitantWriter — types "Does Claude know\nwhich comments\nare due?", corrects "know" → "track" |
| B01 | 1 stakes / 2 wrong guess, falsified | A federal agency proposes a rule, and opens a public comment period — often just sixty days before it can finalize. Miss that window, and your objection never reaches the record. The easy assumption is that Claude is already watching that window, the way a person might watch a calendar. But Claude has no built-in connection to any docket. What it has is a skill — a folder of instructions called comments. | an "assumption" card ("CLAUDE IS WATCHING the docket, on its own") rings out and dims; two dim fact-chips ("comment period", "filing deadline") slide past it, never touching |
| B02 | 3 mechanism / **4 anchor planted** | The SKILL.md inside that folder says three things: review open comment periods, log decisions, track deadlines. Claude reads that file fresh each time — it keeps no memory of a docket from any other session. Watch one rule: a proposal opens its comment window on March second, sixty days to respond. The skill logs that date the moment it's told, and starts the clock. | SKILL.md card unfurls into three stacked instructions; THE ANCHOR — a "RULE OPENS · MAR 2" card beside a countdown ring filling toward 60 days |
| B03 | **4 anchor payoff / 5 both directions** | When day sixty arrives, the skill doesn't file anything itself — a person still decides, and records that call with one flag: filed, not filed, or waived. For March second's rule, the log shows filed, on day fifty-nine. But a decision logged on time doesn't mean the comment itself was any good — the skill only kept the date. And a rule with no logged decision isn't necessarily missed — it might be tracked somewhere the skill never saw. | THE ANCHOR RETURNS — the countdown ring fills to day 59, a FILED stamp locks in; then splits into "logged ≠ good" and "not logged ≠ missed" |
| **BCRY** | **6 carry-out** | A skill like this doesn't know the law, and it doesn't decide anything — it only remembers the date you gave it. Filed, waived, or missed, that call is still yours to make. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Paste in a proposed rule with its comment deadline. Then ask: log this with the deadline, and ask me before the deadline which way I want it recorded — filed, not filed, or waived. Don't decide for me. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Comments. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the comment-window/filing-deadline fact; the SKILL.md mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude already knows/watches the docket); the B02→B03 anchor falsifies it directly — the clock only starts once the rule's opening is logged, and the log on day 59 shows only what it was told |
| Exactly one inference flag | none needed — every claim (NPRM comment windows, SKILL.md as the instruction set, the file/not-file/waived decision states, the `--decide CMT-ID` flag) is lifted directly from the source sheet's own real facts; see QUESTION.md |
| One anchor, planted early, paid off late | B02 → B03 (a proposed rule opening its comment window March 2nd, a sixty-day clock, resolved to filed on day 59) |
| Both directions | B03 — a decision logged on time doesn't prove the comment was any good; a rule with no logged decision doesn't prove it was missed |
| No design judgment | B01–B03 state what the skill does and why watching-the-docket is the wrong model, never a verdict on the skill's own design (the source's Teardown "what it gets right / what it bites" framing is dropped) |

## Deliberately not claimed

- **Not that Claude ever decides whether to file.** The source's own facts
  are explicit that the decision (`--decide CMT-ID`) is a human call the
  skill records, never one it makes — B03 states this directly.
- **Not a live connection to any government system.** The skill logs what
  it is told; it does not claim to poll the Federal Register or any
  external docket on its own.
- **No accusation that the skill's design is flawed.** The source's
  Teardown verdict ("what it gets right… what it bites") is dropped in
  favor of stating the mechanism and its two failure directions as
  properties of any deadline-tracking skill, not a judgment on this one.

## Handoff prompt (BHTF, read aloud)

> "Paste in a proposed rule with its comment deadline. Log this with the
> deadline, and ask me before the deadline which way I want it recorded —
> filed, not filed, or waived. Don't decide for me."

Why it's worth running: it surfaces the same distinction the reel is built
around — the skill's job is to hold the date and force the decision back
to you, not to make it.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off
exists for this redo's script (source facts are real; framing and
carry-out are newly composed for the Plain register).
