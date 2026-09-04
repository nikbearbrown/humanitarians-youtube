# Claude, Tested by a Stranger — What the Doc Co-Authoring Skill Actually Does

A draft can read as finished and still be wrong — finished to the one person
who already knows every unstated fact in it. The doc-coauthoring skill
treats that as the actual failure mode: Stage 1 closes the knowledge gap
before a word gets drafted (five meta-questions, then a full context dump).
Stage 2 builds section by section in a repeating clarify/brainstorm/curate
loop, with a quality gate that fires after three rounds of no real change
and a final pass to cut generic filler. Stage 3 is the mechanism that
matters most: the finished draft goes to a fresh Claude with none of this
conversation's context, and it reads cold, asking what a real reader would
ask. Watch the anchor return: a payments-API spec that reads perfectly to
its author stalls a fresh reader on one undefined term — the exact blind
spot no amount of "more detail" from the author could have caught. That
test is a real structural signal, not a guess — but it isn't unlimited: it's
built for documents that get reviewed at scale, and it only holds if edits
keep going through the loop instead of bypassing it silently.

**Topic:** CLAUDE · DOC CO-AUTHORING SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-doc-coauthoring

---

## Chapters

0:00 The naive framing: "Can Claude write my doc for me?"
0:10 The spec reads great — to you (the anchor)
0:23 More detail, same blind spot — the wrong guess
0:34 Stage 1 — close the gap
0:52 Stage 2 — the per-section loop
1:05 The quality gate
1:19 Stage 3 — a reader who wasn't there
1:37 The reader stops here — the anchor returns
1:49 What the test proves
2:04 What it doesn't fix
2:21 Carry-out
2:31 Your turn
2:49 Outro

---

## YOUR TURN

I need to write a decision doc about migrating our auth service to OAuth
2.0. Walk me through the doc-coauthoring workflow. Before you write
anything, ask me the five context questions and wait for my full context
dump.

Then watch what happens before Claude writes a single word — does it ask
first? Does it wait for your dump before drafting? That's the whole gate.

---

## Deliberately not claimed

No named tool beyond the generic "auth service" / "payments API" — the
mechanism (context first, reader-tested last) holds regardless of the
document. No claim about how long the workflow takes beyond "long, built
for documents reviewed at scale" — not a timed guarantee. No claim that
Stage 3 catches every possible gap — only the structural kind: missing
context a familiar author cannot see in themselves.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
