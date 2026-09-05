# Material Plan Change: Stop Before the Scope Shifts — Narration Script (redo, GATE P)

*Skill: `hai-simple`. Register: **Plain**. 10 beats ≈ 2:15.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*
*Redo of `behind-the-model/claude-liam-material-plan-change` — question,
facts, and beat count preserved; register re-registered Teardown → Plain;
cold open replaced with `BrutalistHesitantWriter`; outro re-skinned Humanitarians AI.*

**Cold open:** `BrutalistHesitantWriter` (Remotion, machine-rendered — no puppet, no human step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes the fix is telling you after the agent changes its plan. But by then the change already happened. The real question: should it stop and tell you before it changes something?" | Writer types "My agent keeps adapting\nthe plan on its own.\nWhen should it tell me\nafter it changes something?" — hesitates on "after", corrects to "before" |
| B01 | 1 stakes — **ANCHOR PLANTED** | Say you approve a five-step plan: pull last quarter's invoices, merge them into one report, and save it to the shared drive. Step three hits an invoice in a format the merge tool can't read. Adapting to that is normal — tool failures and missing formats are ordinary parts of how these agents work. The only question is whether the adaptation stays inside what you approved. | THE ANCHOR — a five-step plan card, step three flagged with a format mismatch |
| B02 | 2 wrong guess | The natural guess sounds reasonable: let the agent keep going, and it can tell you afterward what it had to change to finish. | A "TASK DONE" gate, a completion report unrolling after it |
| B03 | **2 break it** + 3 mechanism | But by the time you read that report, the library is already installed and the shared folder has already been read — changes you never named in the plan. The same three signs mark a change worth stopping for: a tool you didn't approve, data you didn't name, or a risk level higher than you agreed to. | The plan card gains two unnamed line items before the report appears; three trigger labels beside it |
| B04 | 3 mechanism, continued | Any one of those firing means stop before the next step, not after. A report written after the fact is an audit log. A question asked before the step is supervision — and only the question can still change what happens. | A timeline with two gate positions, BEFORE and AFTER; only BEFORE has a working stop |
| B05 | **5 direction A** | Stopping for everything would be its own problem. An agent that pauses on every small, in-scope adaptation — retrying a failed call, reading the one file it was told to read — is one nobody keeps approving. | A string of small in-scope adaptations, each interrupted by a stop sign, an approver waving them through unread |
| B06 | **5 direction B** + **4 ANCHOR PAYOFF** | Back to the invoice job: installing that library and reading that folder both clear the bar — a new tool, new data. The agent that stops there and asks returns control while the plan can still change. The agent that finishes and reports has already made the call for you. | THE ANCHOR RETURNS — the plan card splits into a before-path that pauses and an after-path that only reports |
| **BCRY** | **6 carry-out** | A change reported after it happens is an audit log. A change confirmed before it happens is supervision — and only supervision can still change what happens. | The sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads the paste-ready prompt] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Material Plan Change: Stop Before the Scope Shifts. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the anchor plan and the adapt-is-normal fact before B03/B04's mechanism claims |
| Wrong guess surfaced *and falsified by a case* | B02 states the report-afterward shortcut; B03 falsifies it with the anchor's own case — the library and folder are already touched by the time the report exists |
| One anchor, planted early, paid off late | B01 → B06 (the five-step plan card; the before-path pauses and asks, the after-path only reports) |
| Both failure directions | B05 (stopping for every small in-scope adaptation defeats itself) and B06 (a report after isn't worthless, it just can't undo what already happened) |
| No design judgment | B03–B04 describe why placement changes what a check can do mechanically; no beat rules on whether the source's original task-brief wording was well designed |

## Deliberately not claimed

- **Not "every adaptation needs a gate."** B01 and B05 state the opposite —
  routine, in-scope adaptations (a retried call, reading the one named file)
  keep going without a pause; only the three named triggers stop it.
- **Not "a before-gate guarantees safety."** B05 states the failure mode: a
  gate the approver waves through unread stopped nothing.
- **No accusation of anyone building unsupervised agents on purpose.**
  Treating a completion report as sufficient supervision is an ordinary,
  reasonable-sounding assumption, and the reel treats it as one.

## Handoff prompt (BHTF, read aloud)

> "I want to build a material-plan-change detector into an agent workflow: a
> check that fires when the agent's actual plan diverges materially from
> what was authorized. Help me define what counts as a material change in
> scope or method, what signal should trigger the check, and how to route
> the agent back to human approval rather than letting it proceed with an
> unauthorized approach."

(Near-verbatim from the source reel's `YOURTURN` ask — the prompt itself
needed no register change.)

---
**GATE P — signed:** ______________________  (human)
