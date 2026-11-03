# XLSX

Ask Claude to build you a spreadsheet with a computed total, and the
natural guess is that once the number's known, typing it straight into the
cell is just as good as writing the formula that produced it. It isn't.
The xlsx skill's one absolute rule is: never calculate a value in Python
and hardcode it — write the actual Excel formula, so the sheet stays
dynamic when inputs change. The workflow is six steps, and one is
mandatory the moment a formula gets written: scripts/recalc.py opens the
file in LibreOffice, recalculates every formula, and scans for four Excel
error types, returning JSON with the exact cell address for each one. The
financial-model color code marks every cell by what it actually is — blue
for a hardcoded input, black for a formula, green for a cross-sheet link,
red for an external one, yellow for a key assumption. Watch one concrete
ask — a three-year revenue model with a growth-rate assumption — go in,
get corrected against the formula mandate, and come back out right. And
both directions matter: recalc.py catches exactly the four error types
it's built for, but a formula pointed at the wrong cell can pass clean and
never throw an error at all.

**Topic:** XLSX · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-xlsx

---

## Chapters

0:00 The naive framing: "does Claude just type the number in?"
0:10 Two tools, one decision
0:27 The ask, planted: a three-year revenue model
0:38 Just type the number in? — the wrong guess
0:50 The formula mandate — the case that breaks it
1:03 Six steps, one mandatory
1:17 Recalc.py, under the hood
1:34 Blue, black, green
1:48 Red, yellow, and the numbers
2:02 The anchor returns: the same model, now correct
2:19 What recalc.py catches
2:31 What it can't catch — one flag
2:48 Carry-out
3:01 Your turn
3:27 Outro

---

## YOUR TURN

Build a three-year SaaS revenue model with a growth-rate assumption and a
computed revenue total each year — deliver it as an xlsx file, using the
xlsx skill.

Then watch two things: does it write an actual formula for the total,
instead of a hardcoded number? And does it run scripts/recalc.py
afterward, and read the JSON result before calling it done? Run it today,
on your own model, not the video's example.

---

## Deliberately not claimed

The source skill file this reel is based on could no longer be located at
its original path by the time of this build — the skills tree has been
reorganized since. Facts are carried over unchanged from the locked source
script (the two tools, the six-step workflow, the mandatory recalc.py
step and its four error types, the financial-model color code and number
formats, the formula mandate, the row-offset trap) rather than
re-verified against a live file, per this series' redo contract.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #LLM #HumanitariansAI #ProfessorBear
