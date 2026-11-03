# How Do You Know If You're Supervising Claude Enough?

Ask most people if they check Claude's work carefully enough and they'll answer
with a feeling — careful, or not careful enough. That's the wrong measurement.
Supervision should scale with how much decision-making you actually hand over
on a given task, not stay flat as a personal habit. The fix: log it. A small
tool logs each interaction, classifies how much you handed to Claude — a quick
edit, an assisted task, or a real decision made mostly by the model — and once
a week, audits for the gap: high-autonomy interactions that got almost no
verification time. Watch the anchor: twelve real interactions plotted on a
grid, usage against verification time. Nine land near the diagonal. Three sit
in a danger corner — heavy reliance, almost no checking. Two weeks later the
danger corner should empty out, and that's real progress — but a rising score
only proves you logged more checking time, not that the checking caught
anything, and an un-flagged interaction just means this pass didn't catch it.
Supervision isn't one habit you either have or don't. It's a gap between trust
and verification, invisible until you log it.

**Topic:** SUPERVISION CALIBRATION · WEEKLY AI AUDIT
**Playlist:** Behind the Model
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/behind-the-model--claude-liam-supervision-calibration-logger

---

## Chapters

0:00 Am I being careful enough with Claude?
0:12 One habit, or logged by task?
0:34 Log, classify, audit
0:55 The anchor — twelve interactions, one grid
1:11 From report to to-do list
1:28 Score rising — what does it prove?
1:46 Carry-out
1:56 Your turn
2:14 Outro

---

## YOUR TURN

"Log ten interactions I've had with Claude this week, one sentence each. For
each, note how much decision-making I handed over and how many minutes I
actually spent checking the result. Help me see whether my longest checks are
going to the highest-trust interactions — or somewhere else."

Why it's worth running: most people assume their checking effort already
tracks the stakes, and a ten-entry log is usually enough to show whether it
actually does.

---

## Deliberately not claimed

This reel redoes a published CLI-explainer reel
(`claude-liam-supervision-calibration-logger`) in the Plain register for a
general audience. The underlying facts are unchanged from the source: a
weekly supervision log records each AI interaction, classifies it by how much
decision-making was handed over, and audits for interactions where usage
outpaced verification time. The 12-interaction demo and its danger-corner
result are the source's own worked example, literalized as this reel's
anchor. The source's actual terminal commands, a Python code snippet, and a
named classifier model are dropped here — general audience, no invented or
stale product specifics.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics #AISupervision

---
