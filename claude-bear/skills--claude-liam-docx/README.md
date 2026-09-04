# DOCX

Ask Claude to build a Word document, and the natural guess is that touching
a .docx file — to create it or to edit one you already have — always takes
a code library. It doesn't. A docx file is a ZIP archive holding XML, so the
edit path is just unpack, edit the text, repack — no library at all. The
create path is different: it does take a library, docx-js, and its
defaults fail silently rather than throwing errors. The page size defaults
to A4, not U.S. Letter. Tables need matching DXA widths on the table and
every cell, or the percentage option quietly breaks the table in Google
Docs. Watch one concrete ask — a one-page memo, U.S. Letter, with a
two-column table and page numbers — go in, get corrected against those
rules, and come back out right. And both directions matter: the five
documented rules catch exactly the failures they were built for, but
nothing forces a check for one that isn't on the list.

**Topic:** DOCX · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-docx

---

## Chapters

0:00 The naive framing: "do you need to install something to edit a docx?"
0:09 Two paths, one file format
0:24 The ask, planted: a one-page memo
0:36 Same library either way? — the wrong guess
0:43 It's a ZIP of XML — the case that breaks it
0:54 A4 is the default, not Letter
1:04 Paragraphs and bullets, not characters
1:14 Tables need dual widths
1:25 Unpack, edit, repack — in order
1:38 The anchor returns: the same memo, now correct
1:51 What the rules catch
2:02 What's outside the list — one flag
2:12 Carry-out
2:25 Your turn
2:42 Outro

---

## YOUR TURN

I want a one-page technical memo as a Word document, U.S. Letter, with a
header, heading styles, a two-column table, and a footer with page numbers.
Use the docx skill.

Then watch what Claude does before the file is done — does it set the page
size explicitly, and does it use DXA widths on the table instead of
percentage? Run it today, on your own memo, not the video's example.

---

## Deliberately not claimed

The source skill file this reel is based on could no longer be located at
its original path by the time of this build — the skills tree has been
reorganized since. Facts are carried over unchanged from the locked source
script (the two paths, the five docx-js rules, the three-step edit
workflow, the tracked-changes and element-order pitfalls) rather than
re-verified against a live file, per this series' redo contract.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #LLM #HumanitariansAI #ProfessorBear
