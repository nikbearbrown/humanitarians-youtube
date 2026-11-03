# Claude, Crm Cleanup. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-crm-cleanup`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone typed 'fix' — Claude doesn't fix your CRM alone. A skill called crm-cleanup scans for stale deals, duplicate contacts, and missing fields, then fixes what you approve. Does Claude scan my CRM by itself?" | writer types "Does Claude\nFIX my CRM\nby itself?", hesitates on FIX, corrects to "scan" — lands "Does Claude scan my CRM by itself?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is crm-cleanup. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: SKILL.md only |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → APPROVED FIXES |
| B03 | 3 mechanism | The scope is specific. crm-cleanup scans HubSpot for three things: stale deals, duplicate contacts, and missing fields. It fixes only what the owner approves, and you can narrow it further with a scope argument — deals, contacts, or all. Stay inside that request, and the same input produces the same result every time; ask for anything the file doesn't cover, and the skill has nothing to say about it. | heading card: "The interesting constraint." + scope statement |
| **BCRY** | **6 carry-out** | Claude doesn't clean up your CRM however it wants. It scans for exactly what the file specifies, and fixes only what you approve. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Read the crm-cleanup skill in this folder. Before you fix anything, tell me exactly which stale deals, duplicate contacts, and missing fields you'd flag in HubSpot, and wait for my approval on each one. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Crm Cleanup. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the scope (scans for three named things, fixes only what's approved, nothing outside the request) and stops; the source's "Teardown moment," "what it gets right / what it bites," and "Verdict" framing are all dropped |
| Stakes → mechanism | B00 states the misconception (crm-cleanup = Claude decides on its own how to tidy up the CRM); B01–B02 explain the file and pipeline before B03's scope statement |
| Carry-out | BCRY compresses the distinction (bounded scan, approval-gated fix — not free-form autonomous cleanup) rather than summarizing the topic |
| Host handoff | B00 hands narration to Liam implicitly; no puppet host in hai-simple |
| Hedge words | none used — every claim is a confirmed, present-tense description of how crm-cleanup and Claude Skills generally work |

## Deliberately not claimed

- **Not "Claude fixes the CRM on its own."** The naive framing in B00 ("Does Claude
  FIX my CRM by itself?") is stated and corrected within the same beat — the skill
  scans automatically, but every fix waits on the owner's approval.
- **Not a claim about specific "stale" or "duplicate" thresholds.** The source names
  three categories (stale deals, duplicate contacts, missing fields) and the
  approval gate without defining exact thresholds; this reel states only what the
  source's readable text supports.
- **Recovered, not invented, the skill description.** The source truncates its own
  description sentence in B03/BVDT/BHTF ("...then fixes what the owner app.",
  "...then fixe.", "...missing fields,."); the complete sentence survives intact in
  the source's own B00 and is used here instead of guessing at the cut-off text
  (see QUESTION.md).
- **No verdict on the skill's design.** The source's Teardown register judged the
  skill ("what it gets right," "what it bites," "know the limit"); this Plain redo
  describes the same scope without ruling on whether it was well designed.

## Handoff prompt (BHTF, read aloud)

> "Read the crm-cleanup skill in this folder. Before you fix anything, tell me
> exactly which stale deals, duplicate contacts, and missing fields you'd flag
> in HubSpot, and wait for my approval on each one."

Why it's worth running: it forces Claude to state its own scope before acting —
the same "explain first" clause the source reel's own handoff used to surface a
skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
