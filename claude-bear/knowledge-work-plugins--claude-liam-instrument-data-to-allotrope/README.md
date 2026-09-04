# Your Lab Data Gets Converted, Not Read

Someone hears "instrument data to Allotrope" and assumes Claude reads the lab
results — understands them, judges them, the way a scientist would. It
doesn't. It detects which instrument produced the file and converts it — PDF,
CSV, Excel, or plain text in; Allotrope JSON or a flattened CSV out — the same
exact way every run. The instructions live in one file Claude reads before it
works; ask it to interpret a result or flag something scientifically odd, and
there's no step written for that.

**Topic:** INSTRUMENT DATA TO ALLOTROPE · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-instrument-data-to-allotrope

---

## Chapters

0:00 Can Claude read my instrument files for me?
0:10 A skill is a folder
0:28 How it runs
0:37 One job, two shapes
0:56 Carry-out
1:04 Your turn
1:23 Outro

---

## YOUR TURN

"I have a plain CSV export from a lab instrument, with columns like sample ID,
measurement, units, and timestamp. Convert each row into one clean JSON
record with consistent field names and ISO-format timestamps, and tell me the
schema you used."

That's the whole idea: detect the shape of what you've got, convert it into
one exact standard format — never a read on what the numbers mean.

---

## Deliberately not claimed

This reel never claims the skill performs scientific judgment — it doesn't
flag anomalies, validate results, or assess data quality. It's also not a
claim that auto-detection is perfect: that capability is stated as the source
describes it, with no accuracy figure invented for effect.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AIagents #AgenticAI #LabAutomation #HumanitariansAI #ProfessorBear #ClaudeBasics

---
