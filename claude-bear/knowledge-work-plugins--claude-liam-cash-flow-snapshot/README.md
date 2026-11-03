# Claude, Cash Flow Snapshot.

A named Claude skill like `cash-flow-snapshot` isn't code Claude wrote on
the fly — open the folder and there's no hidden script waiting to run the
real logic. Two items sit there: a `SKILL.md` file (about six kilobytes of
plain language) and a `reference/` folder. Claude reads that `SKILL.md`
itself and treats it as the program. The pipeline lives in the Steps
section, and Claude runs it top to bottom — linear, no branching unless a
step says so. Ask for a cash flow snapshot covering March, and it reads
the file, works through each step in order, and hands back a snapshot —
run the exact same request again and the answer comes back identical, not
because Claude re-examined anything with fresh judgment, but because the
same fixed steps ran a second time. That cuts both ways: identical output
on identical input doesn't prove understanding, and different output next
month doesn't mean the logic changed — same steps, new input either way.

**Topic:** CASH-FLOW-SNAPSHOT · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-cash-flow-snapshot

---

## Chapters

0:00 Claude built the cash-flow-snapshot skill. Right?
0:11 No hidden script — two items, that's all
0:30 Request in, steps in order, output out
0:51 Same steps, every time
1:20 Carry-out
1:33 Your turn
1:51 Outro

---

## YOUR TURN

"Open the cash-flow-snapshot skill folder. Before you run anything, read
me the SKILL.md and tell me, in your own words, what steps it says to
follow, in order."

Why it's worth running: it forces Claude to surface the actual instruction
set in its own words before acting on it — the same explain-first habit
that makes a deterministic skill auditable rather than a black box.

---

## Deliberately not claimed

Not what a cash flow snapshot specifically computes — the source sheet
this reel redoes lost the line naming the skill's exact job (a template
substitution defect, not a redaction), and no other copy of this skill's
`SKILL.md` exists to recover it. This reel states only the mechanism every
Agent Skill guarantees — a folder, a `SKILL.md`, an ordered Steps section,
same-input-same-output — and never invents the specific fields or formulas
a snapshot would contain. Not a verdict on whether the skill's design is
good — that's Teardown territory; this reel states the mechanism and
stops.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
