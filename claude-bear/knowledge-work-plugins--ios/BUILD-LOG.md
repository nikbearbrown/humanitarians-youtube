# BUILD-LOG — knowledge-work-plugins--ios

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-contact-center/ios/beat_sheet.json`
(a Teardown skill-teardown of the Anthropic `contact-center/ios` Skill, built in a
2026-07-25 batch — `PEDAGOGY.md`: "Batch build — skill teardown format", verdict
PASS). This invocation started from a bare `SUBJECT.json` and built the full reel
from scratch: `QUESTION.md`, `CARRY-OUT.md`, `SCRIPT.md`, `beat_sheet.json` (8
beats), GATE T (`type_check.py`, PASS, 0 FAILs), 8 Kokoro `am_onyx` mp3s with
measured `actual_duration_s` written back, all 8 Remotion beats rendered via
`remotion_scenes.py` (the first invocation hit the 10-minute Bash timeout mid-run
at 6/8 beats — B00, B01, B02, B03, BCRY, BHTF already cached to disk — and a
second invocation picked up exactly where it stopped, rendering the remaining
BOUT/BCTA and skipping the six already-filled beats), then compiled.

**Redo contract check:** question, facts, and body argument carried over from the
source unchanged — a skill is a folder Claude reads before it works; SKILL.md is
the full instruction set in plain language ("the file is the program"); the
pipeline runs linearly (read → execute → return); scope is the Zoom Contact
Center SDK for native iOS (chat, video, the virtual agent, scheduled callback
integrations, app lifecycle bridging, rejoin flow, and callback handling); same
request produces the same integration code every time, and the guarantee holds
only for what the file specifies. Register re-registered Teardown → Plain: the
source's judgment framing ("Teardown moment," "what it gets right / what it
bites," "Verdict") is dropped; B03 states the scope and stops. Voice re-set to
Liam `am_onyx` regardless of source (the source was already `am_onyx`, so no
change in practice). Close carries the Humanitarians AI skin
(`OutroSeries`/`OutroCTA`, `@HumanitariansAI`). No source beat was
ai-video-prompt, pantry, or a human-drop slot — the source's 7 beats were all
already REMOTION, so NO-GENAI/NO-PANTRY LAW required no substitution beyond the
mandated B00 cold-open swap to `BrutalistHesitantWriter`. No fabricated
trigger-phrase quote — the source never gives one for this skill, and
SCRIPT.md/`.md`'s "Deliberately not claimed" sections say so explicitly. Beat
count kept at the source's 7 pedagogical beats (this redo's 8 = the 7 plus the
split BCTA outro-CTA beat that's standard to every hai-simple close — matches
the `knowledge-work-plugins--android` sibling redo of the same source family).

**WRITER LAW check:** B00 (`BrutalistHesitantWriter`) measured 11.86s — clears
the ≥8s window. Narration is 35 words + `lead_silence_s: 0.8`. Pulled a frame at
~6s into the beat (screenshot: "Does Claude / RUN" with RUN in terracotta and
caret) and a second frame later in the beat (screenshot: "Does Claude / build
my / contact center / app?" fully corrected) — the correction from "RUN" to
"build" lands on screen before the beat ends, as required.

**Gate V finding, assessed and not treated as blocking:** the BHTF
(`ClaudeComposerAsk`) command reads "Read the contact-center/ios skill in this
folder. Before you run it, tell me exactly which Zoom Contact Center SDK
features it covers and which iOS lifecycle pieces it handles. Then help me wire
up one feature in my app." — 235 characters as one un-broken line, and the
component's input area clips it after "...Then help" at 3 visible lines,
identical in shape to the clipping already logged (and accepted) on the
`knowledge-work-plugins--android` sibling redo, which found this to be the
established, accepted behavior of this shared component across dozens of
already-shipped `hai-simple` siblings. Narration (Liam) still reads the full
prompt aloud, and the full paste-ready text is carried verbatim in
`knowledge-work-plugins--ios.md`'s "YOUR TURN" section for anyone who wants to
copy it. Left as-is rather than diverging from sibling convention on a single
reel.

**Gates passed:** GATE T PASS (8 beats checked, 0 FAILs). `compile.py`:
content-check PASS (8/8 beats), frame-check PASS (4K canvas, 8/8 beats),
lane-check PASS, GATE AUDIO PASS (mean_volume -23.9 dB, max -3.0 dB — well
above the -40 dB floor), compile PASS. Master
`knowledge-work-plugins--ios.mp4` — 84.6s, 3840×2160 (compile.py's 4K LAW
forces the clean master to 2160p by default), newer than `beat_sheet.json`
(compiled 03:54:13 vs. sheet 03:52:57). Read frames across all 8 beats at
1/6 fps plus a targeted frame in the final 3s: legible, safe-inset, no
overlapping text/cards except the BHTF clipping noted above. `MOTION.md`
advisory: 8/8 beats render as `remotion` (100%, over the ~40% pantry-language
cap) — expected for this skill (WRITER LAW + all-GRAPHIC/REMOTION body per
NO-GENAI/NO-PANTRY LAW leaves no other motion language available), not a
defect.

**Delivery:** since the review-cut master already compiles at 3840×2160
(compile.py 4K LAW), the Fellows-facing 4K deliverable is a copy of the same
master under the `-4k.mp4` filename (`deliver.py`'s `newest_master()` prefers
`<slug>-4k.mp4` first, falling back to the plain master, which is already 4K
here). `deliver.py --push` staged `DELIVERY/knowledge-work-plugins--ios/` (4K
mp4 + `-description.md`) and copied text artifacts to
`humanitarians-youtube/claude-bear/knowledge-work-plugins--ios/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4), committed, and pushed.

**Status: DONE.** `knowledge-work-plugins--ios.mp4` (and its `-4k.mp4` copy)
exist, are newer than `beat_sheet.json`, and carry audible audio (-23.9 dB). No
further edits to `beat_sheet.json` after this compile.
