# Claude, Deal Tracker. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude's deal tracker is a smart assistant that already knows their pipeline. It isn't — it's a scripted set of steps. So what does the deal-tracker skill actually do?" | BrutalistHesitantWriter — types "Claude, Deal Tracker. It's a SMART assistant that tracks my deals — so what does it actually do?", corrects "smart" → "scripted" |
| B01 | 1 stakes / 2 wrong guess, falsified | A skill is a folder Claude reads before it acts. Deal-tracker's SKILL.md says exactly what to do: track live deals — milestones, deadlines, action items, status — and surface what's overdue. Plain instructions. No hidden reasoning. | a folder icon labelled "deal-tracker/" with a SKILL.md card inside it; the job description typing out beside it: milestones, deadlines, action items, status |
| B02 | 3 mechanism / **4 anchor planted** | The steps run in order, one deal at a time. Take Acme — a live deal moving through the pipeline. When a milestone's deadline passes, deal-tracker flags it overdue. Exactly what step three says to do. | THE ANCHOR — a deal card labelled "ACME · Series C" moving through numbered steps; on step three, its milestone deadline passes and an OVERDUE flag lights up in terracotta |
| B03 | **4 anchor payoff / 5 both directions** | Now ask Acme's tracker something the spec never lists — draft the counterparty's redline. Nothing happens. No fallback, no guess. Same input, same reliable output for what's written; anything outside those six trigger phrases, it simply doesn't reach. | THE ANCHOR RETURNS — the same "ACME · Series C" card; a new request bubble reads "draft the counterparty's redline"; no step lights up, the card stays dim, no flag appears |
| **BCRY** | **6 carry-out** | Deal-tracker gives the same reliable output for exactly what's written in its steps — and nothing at all for what isn't. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Read the deal-tracker skill, then track three deals: Acme, a Series C with a milestone due Friday; Beta Corp, an add-on due next Tuesday; Gamma LLC, a refi with no deadline set. Ask for the pipeline view and anything overdue. Then ask something the skill never lists — like negotiating strategy — and watch: does it say that's outside the skill, or does it guess? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Deal Tracker. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the job (milestones, deadlines, action items, status) before B02's step-by-step mechanism |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (a smart assistant that already knows the pipeline); B01–B03 falsify it directly — it's a written spec, and the Acme case shows exactly where it stops |
| Exactly one inference flag | none needed — every claim is read directly off the source's own statement of the skill's job, triggers, and step structure, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the "ACME · Series C" deal card) |
| Both directions | B03 — the same input gives the same reliable output when the request is written into a step (holds); the same mechanism reaches nothing when the request falls outside the six trigger phrases (flips) |
| No design judgment | B03 states the boundary as a mechanism fact — what's in the spec runs, what isn't doesn't — never a verdict on whether the skill should have been written wider |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03/BVDT framed the spec as
  "what it gets right: repeatable results" against "what it bites: anything
  outside the spec" — Teardown language. Plain keeps the same underlying
  fact (reliable inside the spec, unhandled outside it) but states it as a
  mechanism boundary, not a critique of the skill file.
- **Not that deal-tracker is unintelligent or broken.** The reel never
  claims the skill fails at its stated job — only that its stated job is
  the whole job.
- **Not every source beat gets separate airtime.** The source's B01
  (anatomy) and part of B03 (the job description) are compressed into this
  reel's B01; the source's BVDT verdict recap becomes this reel's BCRY
  carry-out — compression for a 7-beat Plain cut, not a factual change.

## Handoff prompt (BHTF, read aloud)

> "Read the deal-tracker skill, then track three deals: Acme, a Series C
> with a milestone due Friday; Beta Corp, an add-on due next Tuesday; Gamma
> LLC, a refi with no deadline set. Ask for the pipeline view and anything
> overdue. Then ask something the skill never lists — like negotiating
> strategy."

Why it's worth running: watching whether Claude reports only milestones,
deadlines, action items, and status — nothing invented — and then watching
what happens when you step outside those six trigger phrases, surfaces
whether the spec-bounded behavior from B01–B03 actually holds.

---
**GATE P — signed:** ______________________  (human)
