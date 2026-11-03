# SCRIPT — Claude, Is This A Problem.

*Reel: claude-for-legal--claude-liam-is-this-a-problem*
*Register: Plain — explain, then stop.*
*Voice: Liam (Kokoro am_onyx), in for Bear.*
*Redo of a Teardown "skill-teardown" reel — see BUILD-LOG.md for the
placeholder-reconstruction note.*

---

## B00 — HESITANT WRITER (Remotion)

*(Writer types the naive question, hesitates on "decide", replaces with
"check", then lands the real question. Liam reads the naive framing, the
correction, and the final question over the typing.)*

**Liam:** "Someone assumes Claude judges 'is this a problem' by feel. It
doesn't decide — it checks. A written skill spells out exactly what counts
as a problem. Liam walks you through it."

---

## B01 — Stakes / Anatomy

A skill is a folder Claude reads before it acts. This one is called
is-this-a-problem. Its SKILL.md holds the whole instruction set, in plain
language — no hidden logic, nothing left to guess. Claude reads the file,
then follows it. The file is the program.

---

## B02 — Mechanism / ANCHOR PLANTED

Inside, a Steps section lays out the pipeline: read the situation, check
it against a list of defined conditions, then answer. Watch that middle
step — the checklist. It isn't Claude weighing the situation on its own;
it's Claude matching it against conditions someone already wrote down.

*(THE ANCHOR: the checklist step, matching a situation against written
conditions. Returns at B03.)*

---

## B03 — ANCHOR PAYOFF / Both Directions

Back to that checklist: feed it a situation the list anticipated, and it
answers the same way every time — reliable, on repeat. But feed it
something the list never named, and it has nothing to fall back on. Not
wrong, exactly — just outside what the spec covers. That's the trade a
written checklist makes: consistency where it applies, silence everywhere
else.

*(THE CHECKLIST FROM B02 RETURNS, now tested against a covered case and an
uncovered case.)*

---

## BCRY — Carry-Out (Remotion)

Is this a problem, from Claude, means is this a problem according to the
checklist it was given — same input, same output, every run, and only for
what that checklist thought to name.

---

## BHTF — Your Turn (Remotion)

Your turn. Here's the prompt — read it with me. Pick one decision you
currently make by gut feel — is this urgent, is this worth escalating, is
this a problem. Ask Claude to help you write out the actual criteria
you're using as a short checklist, then run your next three real cases
through it and flag anything that doesn't fit. Liam, in for Bear.

---

## BOUT — Outro CTA (Remotion)

Claude, Is This A Problem. Liam, in for Bear.

---

## Redo mapping (source → this reel)

| Source beat | Source content | This reel |
|---|---|---|
| B00 (`ClaudeComposerAsk`, Teardown cold open) | Claude UI opening the skill | B00 (`BrutalistHesitantWriter`) — WRITER LAW swap |
| B01 (anatomy) | skill = folder + SKILL.md, generic, already true | B01 — kept, register unchanged (was never judgmental) |
| B02 (pipeline) | Steps section, linear execution | B02 — kept, anchor added (checklist step) |
| B03 (design tell, `>` placeholder) | unfilled — "Claude's job: >" | B03 — reconstructed generically: reliable on covered cases, silent on uncovered ones (see QUESTION.md) |
| BVDT (verdict) | unfilled `>` recap | folded into BCRY per CARRY-OUT LAW |
| BHTF (handoff, `>` placeholder) | unfilled — "I want to >" | BHTF — rewritten as a runnable, generic checklist exercise |
| BOUT (outro) | ClaudeTitleOutro, @NikBearBrown | BOUT — OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism (the checklist) waits until B02 |
| Wrong guess surfaced and corrected | B00 (WRITER LAW: "decide" → "check") |
| One anchor, planted early, paid off late | B02 → B03 (the checklist step) |
| Both failure directions | B03 — covered case (reliable) vs. uncovered case (silent, not wrong) |
| No design judgment | B03 states the mechanism and its limit; it never rules on whether the skill was built well |
| No invented facts | B01/B02 kept verbatim from source; B00/B03/BCRY/BHTF reconstruct only the generic triage-skill mechanism already implied by the skill's name and B01–B02 — no invented legal criteria |
