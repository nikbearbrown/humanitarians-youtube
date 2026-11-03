# Claude, Deal Sourcing. — Narration Script (redo of claude-liam-deal-sourcing)

*Skill: `hai-simple`. Register: **Plain**. 11 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** BrutalistHesitantWriter (Remotion, machine-rendered). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "You'd guess Claude decides which companies to invest in once it picks up deal-sourcing. It doesn't — it just finds candidates. Let's see what's actually inside that file." | writer types "Claude decides which companies to invest in with the deal-sourcing skill. What is a skill?", hesitates on "decides", corrects to "finds" |
| B01 | 1 stakes | Hear "Claude has a deal-sourcing skill" and it sounds like Claude itself can judge which companies are worth investing in. | chips: CLAUDE HAS A DEAL-SOURCING SKILL → JUDGES WHICH DEALS ARE GOOD? |
| B02 | 2 wrong guess, broken | But nothing in the model changes. Delete the skill's folder and Claude doesn't lose any investment judgment — there was none to begin with. It just stops running that three-step checklist. | chips: DELETE THE FOLDER → LOSES JUDGMENT? (struck) → NOTHING TO LOSE (accent) |
| B03 | **4 anchor planted** | Here's what a skill actually is: one file. Deal-sourcing, for instance, is a folder holding a single SKILL.md — three steps, in order: search a sector for target companies, check the CRM for existing relationships, draft a personalized outreach email to the founder. | THE ANCHOR — deal-sourcing/, SKILL.md |
| B04 | 3 mechanism | Claude reads that file top to bottom and works through it step by step: search the sector, check the CRM, draft the email — no branching, unless the file itself says branch. | chips: READ THE FILE → SEARCH SECTOR → CHECK CRM → DRAFT EMAIL |
| B05 | 3 mechanism | That makes a skill a specification, not new judgment. The payoff: the same three steps, every sector, every time. The limit: ranking those candidates by how good an investment they are — that's not on the page. | chips: SAME THREE STEPS EVERY TIME (accent) / OFF THE MAP |
| B06 | **4 anchor payoff** | So deal-sourcing never gave Claude judgment about which deals are good. It just guarantees that every time it runs, Claude reads that same file and works through the same three steps — that's the whole trick. | THE ANCHOR RETURNS — deal-sourcing/, SKILL.md (accent) |
| B07 | 5 both directions | Watching Claude surface twenty candidate companies proves the search step ran — it proves nothing about whether any of them are a good investment. And watching it draft a clean, personalized outreach email proves nothing about whether the founder ever replies. | pairs: SURFACED 20 CANDIDATES → PROVES A GOOD INVESTMENT? (struck) / DRAFTED A CLEAN EMAIL → PROVES THE FOUNDER REPLIES? (struck) |
| **BCRY** | **6 carry-out** | A skill named deal-sourcing doesn't hand Claude investment judgment — it finds candidate companies and drafts the outreach; whether any of it's a good deal is still on you. | the sentence, alone, serif, large |
| BHTF | your turn handoff | Your turn. Paste this into Claude: pick one repeatable search-and-outreach routine you run over and over — sourcing candidates for anything, not just deals. Write me a SKILL.md for it: the steps in order, plain language. Then read it back to me and walk me through exactly what you'll do, before you do it. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Deal Sourcing. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B01 states the read; B02 breaks it — delete the folder, Claude loses no investment judgment, because there was none to begin with |
| One anchor, planted early, paid off late | B03 → B06 (deal-sourcing's single SKILL.md, the three-step checklist) |
| Both failure directions | B07 — surfacing candidates proves nothing about deal quality; a clean email proves nothing about the founder replying |
| No design judgment | B02/B05 describe why the skill is a checklist, not a verdict on whether the checklist is well designed |

## Deliberately not claimed

- **Not the specific PE process beyond the source's own three steps.** The
  underlying private-equity `deal-sourcing` SKILL.md is not reachable on
  this machine. Every claim about the mechanism (search a sector, check the
  CRM, draft a founder email) is carried over verbatim from the source
  reel's own narration text, never invented beyond it.
- **No accusation that a diligent search is a substitute for investment
  judgment, or vice versa.** B07's both-directions beat states plainly that
  neither surfacing candidates nor a clean draft proves anything about deal
  quality or founder response — that's the whole point of the beat.

## Handoff prompt (BHTF, read aloud then discussed)

> "Pick one repeatable search-and-outreach routine you run over and over —
> sourcing candidates for anything, not just deals. Write me a SKILL.md for
> it: the steps in order, plain language. Then read it back to me and walk
> me through exactly what you'll do, before you do it."

Why it's worth running: naming the steps out loud is what separates a
checklist Claude can repeat from a vague habit only you remember.
