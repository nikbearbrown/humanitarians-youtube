# Claude, Asana API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude opens the Asana app and clicks around to manage tasks. It doesn't — it calls the Asana API directly, sending and reading back JSON. So what does that API actually look like?" | BrutalistHesitantWriter — types "Claude must open the Asana app and click around to manage my tasks. Is that it?", corrects "app" → "API" |
| B01 | 1 stakes / 2 wrong guess, falsified | Ask Claude to list your incomplete tasks and the answer doesn't come back as a bare list. Every response the Asana API sends — a read or a write — arrives wrapped under a top-level `data` key, and every object inside it is addressed by a `gid`, a string ID, never a name. | the data envelope opened; a bare-array guess struck through, `data` revealed inside |
| B02 | 3 mechanism / **4 anchor planted** | The objects nest the same way every time: workspace holds projects, a project holds sections and tasks, a task carries comments and subtasks. Ask for every incomplete task assigned to you in one project, and Claude resolves your name to a gid, then lists tasks under that project's gid — unwrapping `data` at each step. | THE ANCHOR — workspace → project → task hierarchy; the "list my incomplete tasks" request traced through gid resolution and the data envelope |
| B03 | **4 anchor payoff / 5 both directions** | Get both habits right and that same request returns every task, page after page, because the bundled script keeps requesting until the pages run out. Skip either one — assume a name works where a gid is required, or assume the first page is the whole list — and the request can look successful while it quietly hands back the wrong task, or only the first batch. One more thing to watch for: workspace search is capped at 100 results and doesn't paginate at all — it's the one operation that doesn't follow the other nine. | THE ANCHOR RETURNS — the full paginated list landing correctly, then the same request silently truncated when a habit is skipped; search flagged as the exception |
| **BCRY** | **6 carry-out** | Every Asana call Claude makes turns on two habits — a gid instead of a name, and a response unwrapped from data — get those right and the ten operations take care of themselves. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. List all incomplete tasks assigned to me across all my Asana workspaces, and tell me which ones are due this week. Watch three things: does it resolve who you are before it lists anything, does it unwrap `data` from every response instead of assuming a bare array, and does it use the bundled script instead of a single unpaginated request. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Asana API. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the data-envelope fact; the full hierarchy mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude operates the app); B01 falsifies it with a case — the response isn't a bare array, it's wrapped in `data`, which only makes sense if Claude is reading raw API output, not clicking a UI |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documented facts about the Asana API skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the "list my incomplete tasks" request, traced through gid resolution and the data envelope, then paginated to completion) |
| Both directions | B03 — get gid + data envelope right and the list comes back complete (holds); skip either and the request looks successful while returning the wrong task or a truncated page (flips); search is called out as the one operation that never fully resolves either way (capped, no real pagination) |
| No design judgment | B03 states the search cap as a documented fact to watch for, never a verdict on whether capping search at 100 results was the right call |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the same facts
  as "what it gets right" / "where it bites" — Teardown language. Plain
  keeps the facts (the two-habit rule, the search cap) but states them as
  mechanism and a documented boundary, never a judgment on the skill's
  design quality.
- **Not that gid and the data envelope are the only rules.** `opt_fields`,
  rate limits, and error-code mapping are real parts of the skill; the
  reel picks the two habits that govern every single call as the
  carry-out, not a full reference of every rule.
- **Not that every Asana operation needs the bundled script.** Only that a
  hand-rolled request still owes the same gid + data-envelope habits, and
  that pagination — which the script handles — is where a hand-rolled loop
  most often goes quietly wrong.

## Handoff prompt (BHTF, read aloud)

> "List all incomplete tasks assigned to me across all my Asana workspaces,
> and tell me which ones are due this week."

Why it's worth running: it forces three checks in one shot — does Claude
resolve `/users/me` before listing, does it project `.data` from every
response instead of assuming a bare array, and does it reach for
`asana_tasks.sh`'s pagination instead of a single unpaginated request that
quietly misses tasks past the first page.

---
**GATE P — signed:** ______________________  (human)
