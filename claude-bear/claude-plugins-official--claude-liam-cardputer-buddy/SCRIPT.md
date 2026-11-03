# SCRIPT.md — Push The One File. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-cardputer-buddy` (Teardown, walks the Anthropic
`cardputer-buddy` Claude Code plugin skill — the iterate-after-provisioning
dev loop for the M5Stack Cardputer) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed a one-file change meant reinstalling everything on the
device. It doesn't — there's a script built for exactly that. So: I changed
one file on my Cardputer — do I reinstall it?

*(Text typed on screen: "I changed / one file on / my Cardputer — / do I
reinstall it?" — trigger word "reinstall" corrects to "push", landing on:
"I changed one file on my Cardputer — do I push it?")*

## Body — device layout, the four scripts, the overlap that bites

**NB01 — /flash/, the launcher, the template** (source B01, anatomy)
The Cardputer runs MicroPython on a /flash/ filesystem. main.py is the
launcher — it scans /flash/apps/ at boot and lists every .py file it finds
as a menu entry, automatically. Drop a new file into that folder, push it
to the device, and it shows up on the next boot — no registration code
needed anywhere. The payload has three zones: the launcher itself, a
shared library of BLE, UI, state, and protocol code, and the apps folder
holding whatever's installed. When you're writing a new app, you start
from hello_cardputer.py — the smallest working example, covering keyboard
polling, font rendering, and the convention for exiting back to the
launcher.

**NB02 — four scripts, one job each** (source B02, design)
Four scripts drive everyday changes. install_apps.py pushes the entire
apps folder over USB-serial — reach for it when you've added or renamed
files and need the whole directory back in sync. push.py pushes just the
files you name — reach for it when you've edited one existing file and
want the fast loop. tail_serial.py streams the device's serial logs — run
it in a second terminal while you test. repl_run.py runs a single Python
expression over the REPL — handy for a quick filesystem check without
pushing anything. All four need PORT, and that's whatever the
provisioning step detected earlier — something like /dev/cu.usbmodem on a
Mac, /dev/ttyACM on Linux, or COM on Windows.

**NB03 — the overlap that bites** (source B05, teardown analysis —
re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Here's the actual overlap: install_apps.py and push.py can both push your
one changed file. install_apps.py syncs the complete apps folder every
time, which takes longer than it needs to for a single edit. push.py,
given just that one filename, does the same job in a fraction of the
time. Nothing in either script's name tells you which is faster for the
change in front of you — that's a distinction you have to remember, the
tools don't remind you of it.

## Close

**BCRY — carry-out**
When you've changed one file, push.py sends just that file —
install_apps.py resyncs everything, whether it changed or not. Match the
script to the size of the change, not habit.

**BHTF — your turn**
Your turn. Paste this into Claude: Add a timer app to the Cardputer that
counts down from 60 seconds and returns to the launcher when done. Watch
four things. Does it create the new file in buddy/device/apps/, following
the hello_cardputer.py structure? Does it use push.py for the single new
file rather than install_apps.py for the full directory? Does it follow
the exit convention — polling the keyboard for a key back to the launcher
— instead of hard-looping with no way out? And after pushing, does it
suggest tail_serial.py to watch the output, instead of asking you to
re-flash?

**BOUT — outro**
Push The One File. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a workflow question — does one changed file mean a full reinstall, or is there a lighter tool for that? |
| Wrong guess | B00 (WRITER LAW) | "reinstall" corrected to "push" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the /flash/ layout and launcher auto-discovery, then the four dev-loop scripts and which job each is built for |
| Anchor | the Cardputer dev loop itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one plugin skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the concrete cost the overlap creates (install_apps.py works but is slower than it needs to be for one file); BCRY states the matching rule and its converse together (push.py for one file, install_apps.py for a full resync) — together they cover which tool a given change actually calls for, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the cardputer-buddy Skill's SKILL.md specifies (the /flash/ layout, the
launcher's boot-time auto-scan, the hello_cardputer.py template's coverage,
each script's scope, and the overlap between install_apps.py and push.py)
— not an inference about hidden device or model internals. Per simple's
ONE-FLAG LAW, when the source genuinely supports everything as stated, no
flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat
each; B05's four-item "gets it right / where it bites" list (trigger
distinction, /flash/ layout, launcher auto-discovery, the four scripts —
versus PORT rediscovery, install_apps/push ambiguity, undocumented BLE
protocol, undocumented hello_cardputer.py signatures) is compressed into
NB03, keeping only the single fact a general audience needs and can act on
— the concrete install_apps.py/push.py overlap — and dropping the gaps
that assume a technical audience simple/hai-simple doesn't target (BLE
protocol internals, exact function signatures, PORT rediscovery when
detect.py hasn't been re-run); Teardown framing ("gets it right," "where
it bites") is stripped to a plain mechanism-and-consequence description,
per the NO JUDGMENT register check; BVDT's verdict facts (the four
scripts' scopes and the install_apps/push overlap) are merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW; BHTF kept as the your-turn handoff, with
the source's prompt ("Add a timer app to the Cardputer that counts down
from 60 seconds and returns to the launcher when done") and its four watch
points carried over unchanged — it was already a concrete, paste-ready
prompt needing no extra setup, so it's actually runnable by any viewer
today; BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 +
NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`CardputerBuddyLayout` / `CardputerBuddyScripts` / `CardputerBuddyTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
