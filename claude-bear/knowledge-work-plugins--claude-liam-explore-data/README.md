# Claude Doesn't Write a Report. It Profiles the Data. — The Explore-Data Skill

A skill is a folder Claude reads before it works — this one is
`explore-data`, and its SKILL.md is the whole instruction set, in plain
language, no hidden logic. The instructions run in order: read the file,
then run each step. The actual job isn't writing a narrative report — it's
producing a structured profile: shape, quality, and patterns. Check null
rates and column distributions, spot issues like duplicates or suspicious
values, and decide which dimensions and metrics are worth analyzing next.
Ask it to explore your data, and explore-data hands back a profile — the
same checklist every time, not a freeform report.

**Topic:** EXPLORE-DATA · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-explore-data

---

## Chapters

0:00 The naive framing: "does Claude write a report?"
0:11 A skill is a folder
0:24 Steps, in order
0:32 Profile the dataset
0:46 Carry-out
0:57 Your turn
1:16 Outro

---

## YOUR TURN

Paste this into Claude: I have a CSV of customer orders. Profile it for
me — how many rows and columns, which columns have missing values and how
often, whether any rows look like duplicates, and which two or three
columns are most worth digging into next. Walk me through your plan before
you start.

That clause matters — explaining first surfaces the real constraint logic
before any profiling gets done.

---

## Deliberately not claimed

No claim about what conclusions the skill draws from a profile — this
video describes what explore-data is built to check (shape, null rates,
duplicates, suspicious values, which dimensions/metrics look worth
analyzing), not a guarantee about any specific dataset's findings. Every
fact here is read directly off the source skill's own description; nothing
is inferred.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #DataAnalysis #LLM #HumanitariansAI #ProfessorBear

---
