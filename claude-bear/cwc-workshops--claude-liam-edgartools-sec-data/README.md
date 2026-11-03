# Claude's SEC Filings Skill: Reliable, Not All-Knowing

A newcomer's natural read: once Claude has a skill for SEC data, it must
now generally understand finance and filings — ask it anything, and it'll
know. It doesn't work that way. The skill file, edgartools-sec-data, spells
out exactly four things it covers: company lookups, filings, XBRL financial
statements, and sections like Item 1A risk factors. Ask for one of those and
you get the same reliable pull every time — Claude reads the file, works
through its steps in order, and hands back the result. Ask for something the
file never wrote down — an opinion on whether a filing looks risky — and
there's no step for it.

This works when your question matches the file — a lookup, a filing, a
statement. It flips the moment the question needs judgment the file doesn't
have.

**Topic:** CLAUDE BASICS · SEC FILINGS SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-edgartools-sec-data

---

## Chapters

0:00 The naive framing: "it just knows finance now?"
0:10 The wrong guess: general expertise
0:27 The anchor: the four-item spec list
0:37 Breaking the wrong guess: off the list, nothing happens
0:44 A skill is a folder
0:54 The pipeline: read, execute, return
1:02 Why it's repeatable
1:10 The anchor returns: on the list vs. off it
1:20 Both directions: dependable
1:27 Both directions: not written in
1:36 Carry-out
1:42 Your turn
1:57 Outro

---

## YOUR TURN

Paste this into Claude: "Read the edgartools-sec-data skill, and list, in
your own words, exactly which four things it lets you pull from SEC filings
— then tell me one thing about a company you might want to know that isn't
on that list."

---

## Deliberately not claimed

- **No inference flag.** Every claim here restates the source SKILL.md's
  own description of its scope, confirmed directly against the source
  reel's PEDAGOGY.md/AUDIT.md rather than inferred.
- **No design verdict.** The source's Teardown cut recapped and implicitly
  praised the spec-bounded design ("Repeatable. Spec-bounded."); this video
  states the fact — bounded, reliable within that bound — and stops.
- **No invented UI or tool names.** The `edgartools` Python package and SEC
  EDGAR are named because the source names them; nothing new is invented.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no
account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and
Remotion (motion graphics). No human-performed audio or video in this
production.*

#AI #ClaudeAI #AgenticAI #LLM #AIAgents #HumanitariansAI #ProfessorBear

---
