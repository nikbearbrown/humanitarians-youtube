# Claude, Session Report.

When Claude hands you a session report — exact token counts, cache hits,
subagent calls, the priciest prompts — is Claude the one doing that
counting? No. A bundled script (`analyze-sessions.mjs`) reads your raw
session data and writes one already-computed answer,
`/tmp/session-report.json`, before Claude ever opens a report. Delete
that script and the report doesn't get a little worse — it can't run at
all, because there was no other way inside this skill to get those
numbers. Claude's real job starts after that file exists: read it, skim
the totals, and decide what's worth explaining — the report's
interactive parts (sorting, expanding a row, drawing a bar) already live
in a template file Claude copies in, not code Claude writes. A report
that looks right doesn't prove Claude read every log line itself, and a
report that's wrong doesn't prove Claude reasoned badly — either way, the
script counts and Claude explains what the count means.

**Topic:** CLAUDE · SKILLS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-session-report

---

## Chapters

0:00 The naive framing: "Claude counts every token itself"
0:11 Sounds like Claude did the counting
0:21 Broken, with a case — delete the script, the report is gone
0:33 The anchor: the middleman file — the script's already-computed answer
0:46 Read it, then skim it
0:57 The template already moves — Claude's job is words, not markup
1:09 The anchor returns — same file, unchanged
1:20 Both directions — neither one is proof
1:34 Carry-out
1:41 Your turn
1:53 Outro

---

## YOUR TURN

Run the session-report skill on your Claude Code sessions — tokens,
cache, subagents, skills, the priciest prompts. Read the skill first, and
walk Claude through exactly what it will do before it does it.

Run that today, against your own `~/.claude/projects` history.

---

## Deliberately not claimed

This reel does not describe the session-report skill's own `SKILL.md`
word for word — that file lives in a plugin collection not reachable
from this build, and the source script this reel redoes truncates its
own quoted description of the analyzer's default window and the
pipeline's later steps mid-sentence. Rather than invent past that
truncation, this reel keeps only the facts the source's narration
establishes whole: a 3-file skill (`analyze-sessions.mjs`,
`SKILL.md`, `template.html`), a script that computes the numbers, a
`/tmp/session-report.json` handoff file, a bundled template that already
carries the interactive parts, and same-input-same-output behavior. See
BUILD-LOG.md for the full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no
account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and
Remotion (motion graphics). No human-performed audio or video in this
production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
