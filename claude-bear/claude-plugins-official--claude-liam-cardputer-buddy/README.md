# Push The One File. — Cardputer Buddy (Claude Code Plugin, Dev-Loop Scripts)

The Cardputer runs MicroPython on a /flash/ filesystem. main.py is the
launcher — it scans /flash/apps/ at boot and lists every .py file it finds
as a menu entry, automatically. Four scripts drive everyday changes:
install_apps.py pushes the entire apps folder over USB-serial, push.py
pushes just the files you name, tail_serial.py streams the device's serial
logs, and repl_run.py runs a single Python expression over the REPL. Here's
the catch: install_apps.py and push.py can both push your one changed
file — install_apps.py syncs the complete folder every time, which takes
longer than it needs to for a single edit; push.py, given just that one
filename, does the same job in a fraction of the time. Nothing in either
script's name tells you which is faster for the change in front of you.

**Topic:** CARDPUTER BUDDY · CLAUDE CODE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-cardputer-buddy

---

## Chapters

0:00 The naive framing: "do I reinstall it?"
0:11 /flash/, launcher, template
0:46 Four scripts, one job each
1:26 The overlap that bites
1:49 Carry-out
1:59 Your turn
2:30 Outro

---

## YOUR TURN

Paste this into Claude: Add a timer app to the Cardputer that counts down
from 60 seconds and returns to the launcher when done. Watch four things.
Does it create the new file in buddy/device/apps/, following the
hello_cardputer.py structure? Does it use push.py for the single new file
rather than install_apps.py for the full directory? Does it follow the exit
convention — polling the keyboard for a key back to the launcher — instead
of hard-looping with no way out? And after pushing, does it suggest
tail_serial.py to watch the output, instead of asking you to re-flash?

Run that today, on your own Cardputer, not just in your head.

---

## Deliberately not claimed

No claim about the BLE protocol in claude_buddy.py (how Claude Desktop
sends commands, what event triggers are available) — the source Skill
doesn't spell it out inline, and this video doesn't guess. No claim about
exact PORT rediscovery steps if detect.py hasn't been re-run in a new
session, or about hello_cardputer.py's precise function signatures — both
are real gaps in the source material, but they assume a technical audience
this video isn't aimed at. The claim that install_apps.py "takes longer
than it needs to" for a single file is a direct consequence of syncing a
whole folder versus one named file, not a measured benchmark.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
