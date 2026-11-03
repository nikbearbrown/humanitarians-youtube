# Claude, Demand Intake. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a filled Teardown skill-teardown sheet — source
narration already carried real facts, see QUESTION.md). Register: **Plain**.
7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks whether Claude can just write their demand letter. It can't yet — first it needs the case: the parties, the facts, the leverage. So the real question: can Claude prep for the demand letter?" | BrutalistHesitantWriter — types "Can Claude\njust write\nmy demand letter?", hesitates on "write", corrects to "prep for" |
| B01 | 1 stakes / 2 wrong guess, falsified | A skill is a folder Claude reads before it acts. Demand-intake is a checklist, spelled out in one file, for everything a demand letter needs before any drafting starts. Skip straight to "write the letter," and there's no case in it yet — no parties, no facts, no dollar figure. Claude can only guess. | a "DEMAND LETTER" card with blank fields — PARTIES, FACTS, AMOUNT — each a dim question mark |
| B02 | 3 mechanism / **4 anchor planted** | The skill walks through six things, in order: the parties, the facts, the legal basis, the leverage, the fallback if talks fail, and anything privileged that should stay out of it. Take one case: an unpaid invoice for forty thousand dollars, now sixty days late. Intake doesn't start with the letter — it starts with those six answers. | THE ANCHOR — the six-item checklist appears one at a time; an invoice stamp card ("$40,000 · 60 DAYS LATE") lands beside it |
| B03 | **4 anchor payoff / 5 both directions** | Fill in those six for the invoice — the vendor, the due date, the late clause, the interest owed, the fallback of small claims — and the letter has ground to stand on. Same six questions, every time. But only those six: a fact nobody mentions never makes it in, and this step never writes the letter itself. It hands a finished file to a separate step that drafts. | THE ANCHOR RETURNS — the invoice card locks in as "GROUND TO STAND ON," then splits into "a fact nobody mentions → never makes it in" and "this step never drafts → hands a file to the step that does" |
| **BCRY** | **6 carry-out** | Claude doesn't draft a demand letter until it has a case: demand-intake gathers the parties, the facts, and the leverage into one file first — the draft step only ever writes what's already there. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I have an unpaid invoice. Before you draft a demand letter, ask me for the parties, the facts, the legal basis, my leverage, my fallback if they don't pay, and anything privileged that should stay out of it. Then tell me what's still missing. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Demand Intake. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the empty-letter fact; the six-question mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (just ask Claude to write the letter); B01's blank-fields card and the B02→B03 anchor falsify it — an unpaid $40,000 invoice, 60 days late, produces no usable letter until the six intake answers exist |
| Exactly one inference flag | none needed — the account describes the generic shape of a pre-drafting intake step (gather structured facts before drafting), which is exactly what the source's own filled narration already states; no invented UI or unverifiable claim |
| One anchor, planted early, paid off late | B02 → B03 (the unpaid $40,000 invoice, 60 days late) |
| Both directions | B03 — a fact nobody mentions never makes it into intake; and intake never drafts the letter itself, only hands a finished file to a separate drafting step |
| No design judgment | B01–B03 state what the intake step does and why the letter can't start without it, never a verdict on the skill's design (the source's Teardown "what it gets right / where it bites" framing is dropped) |

## Deliberately not claimed

- **Not a specific product feature demo.** The source's own `source_skill`
  file path does not exist on this machine, so this script draws only on the
  facts already written into the source's narration (parties, facts, basis,
  leverage, BATNA, privilege filters; output to a structured file a separate
  drafting step reads) — nothing about UI, file format, or command syntax is
  invented.
- **Not that intake alone produces a demand letter.** B03 states plainly that
  this step hands a finished file to "a separate step that drafts" — intake
  and drafting are kept distinct, matching the source's own two-skill split
  (`demand-intake` → `demand-draft`).
- **No accusation that a shortcut is careless.** Asking Claude to "just write
  the letter" is presented as an ordinary, understandable first guess, not a
  mistake by any named person.

## Handoff prompt (BHTF, read aloud)

> "I have an unpaid invoice. Before you draft a demand letter, ask me for the
> parties, the facts, the legal basis, my leverage, my fallback if they
> don't pay, and anything privileged that should stay out of it. Then tell
> me what's still missing."

Why it's worth running: it forces the six-question intake pass before any
letter gets written, and surfaces exactly which of the six you haven't
actually answered yet.

---
**GATE P — signed:** n/a — hai-simple redo; source narration supplied the
facts directly, no separate human sign-off gate applies.
