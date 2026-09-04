# It Scores Before It Edits. — The Claude MD Improver Skill

CLAUDE.md files can live in five places — the project root, a gitignored
local override, a global user-wide file, package-specific files in a
monorepo, and any subdirectory. Claude discovers all of these automatically,
then scores each file against six criteria and hands back a letter grade,
A through F, before it changes anything. That's a hard rule in the skill:
the report comes first. Only after you approve does it propose updates, and
those updates arrive as a diff — which file, exactly what to add, and one
line on why — never a rewrite of what's already there. One practical limit:
discovery caps at fifty files, so a large monorepo past that count gets some
files silently unscored.

**Topic:** CLAUDE MD IMPROVER · CLAUDE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-claude-md-improver

---

## Chapters

0:00 The naive framing: "does it just rewrite the file?"
0:12 Five locations, one score
0:47 Report, then a diff
1:10 The fifty-file cap
1:24 Carry-out
1:34 Your turn
1:51 Outro

---

## YOUR TURN

Paste this into Claude: Check and improve my CLAUDE.md files. Watch for
three things. Does it output a quality report, with a grade, before
proposing any change? Are the proposed changes shown as a diff, each with a
one-line reason? And if your repo has more than fifty CLAUDE.md files, does
anything tell you some got skipped?

Run that today, on your own repository, not the video's example.

---

## Deliberately not claimed

No claim about how the six criteria are numerically weighted into the final
letter grade — the source skill states the criteria as High/Medium
importance labels, not a documented point formula, and this video doesn't
guess at arithmetic it can't verify. No claim that every CLAUDE.md
improvement tool works this way; the report-first gate, the diff-with-why
format, and the fifty-file discovery cap are properties of this specific
skill, not a claim about every possible implementation.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
