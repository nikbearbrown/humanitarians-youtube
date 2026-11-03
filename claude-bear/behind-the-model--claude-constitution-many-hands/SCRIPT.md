# One of the Many Hands — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-constitution-many-hands`
(Teardown, 16 beats, body beats seeded but never fleshed out) — question and
body facts kept from the source's written beats and `metadata.one_idea`, body
compressed to one idea per beat, cold open replaced, close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes Claude's safety is just about refusing obviously bad requests — bombs, malware, obvious harm. But the real danger is a request that looks completely legitimate. Isn't Claude's safety just about refusing those instead? | writer types "Isn't Claude's safety just about refusing obviously bad requests?", hesitates on "obviously bad requests", corrects to "requests that only look legitimate" |
| B01 | 1 stakes — **ANCHOR PLANTED** | Picture a coup. It needs soldiers willing to fight, officials willing to sign the orders, and clerks willing to process the paperwork. Historically, any one of them could refuse — and that possibility, spread across every hand involved, was the actual brake. Not the plan's difficulty. Their willingness. | THE ANCHOR — three hands (soldiers, officials, clerks), one lighting up in refusal |
| B02 | 2 wrong guess | So the obvious fix sounds easy: teach Claude to refuse the illegitimate stuff, the way a decent soldier or clerk already would. Add a rule against helping with a coup, and the many-hands problem is solved. | a single rule card, checked off, "problem solved?" |
| B03 | **2 break it** | But almost nothing arrives labeled "coup." A loyalty instruction gets folded into a routine system update. An order to delay an election gets framed as a security precaution, "just this once." Nothing in the wording trips an obviously-bad filter — because there isn't one to trip. | the same rule card, dimmed; ordinary-looking requests sliding straight through it |
| B04 | 3 mechanism | So Claude doesn't try to spot bad intentions from the wording. It tries to still be one of those hands — a place in the chain where refusal is still possible — and it asks the same three questions any one of those historical hands effectively asked: is this happening through a real, legitimate process? Is anyone accountable for it? Is it happening openly, or is it hidden? | Claude joins the row of hands; three gate cards appear — PROCESS, ACCOUNTABILITY, TRANSPARENCY |
| B05 | **4 anchor payoff — worked example** | Take the request to indefinitely postpone a mandated election, with a hidden loyalty instruction buried in the deployment. Process: illegitimate — it subverts the vote the law requires. Accountability: none — the instruction was hidden specifically so no one could be held to it. Transparency: zero — concealment was the point. It fails on all three, and Claude refuses. | the three gates, each stamped FAIL; REFUSED across the group |
| B06 | **5 both directions — ANCHOR RETURNS** | Compare a startup automating work that used to take a whole team, racing ahead of slower competitors. Same concentration — one system doing what many hands used to do. But the process is ordinary competition, someone is accountable for the product, and none of it is hidden. It passes on all three, and Claude helps. The test was never whether a lot of work is being replaced — it's whether the legitimacy triage holds. | the same three hands, now one automated system; the three gates, each stamped PASS; CLAUDE HELPS |
| **BCRY** | **6 carry-out** | A coup was never stopped by its difficulty — it was stopped by any one of the many hands involved refusing. Claude tries to still be that hand, checking whether a request is legitimate, accountable, and out in the open before it helps. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | One of the Many Hands. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read; B03 breaks it with the routine-update / "just this once" case — an obviously-bad filter never fires on wording that doesn't announce itself |
| One anchor, planted early, paid off late | B01 (the three hands, any one able to refuse) → B06 (the same hands, now one system, tested and passed) |
| Both failure directions | B05 (fails all three, refused) and B06 (passes all three, helped) |
| No design judgment | Beats describe why the triage exists and how it resolves; none rules on whether Anthropic was right to build it this way |

## Deliberately not claimed

- **Not "concentrating work is the problem."** B06 is the correction to that
  overreach — a startup automating a team's worth of work concentrates just as
  much as the election example, and passes clean. The disqualifier is the
  triage, not the concentration.
- **Not "Claude can read intent from wording."** B03 is exactly the case where
  it can't — the mechanism in B04 is structural (process, accountability,
  transparency), not a content filter looking for suspicious phrasing.
- **The source's second thread — epistemic autonomy / homogenized belief
  (acts A40–A51) — is not carried.** It's a real, related concern in
  Anthropic's material, but a different argument from the one this source's
  own `metadata.one_idea` names; folding it in would fracture the one-anchor
  law. See QUESTION.md.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to apply the many-hands test to a decision I'm about to hand to an
> AI system — one that used to need several people's separate sign-off. Ask
> me: what was the process that used to approve it, who's accountable if it
> goes wrong now, and would I be fine with everyone involved seeing it happen.
> If any answer is missing, tell me what that's a warning sign of."

Why it's worth running: the triage only feels real once it's pointed at
something with actual stakes. Naming one decision and running it through all
three questions takes a few minutes and turns an abstract safety category into
a checklist you can actually fail.

---
**GATE P — signed:** ______________________  (human)
