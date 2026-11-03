# BUILD-LOG — claude-for-legal--claude-liam-exam-forecast

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-exam-forecast/beat_sheet.json`
— a Teardown skill-teardown sheet for the Anthropic `exam-forecast` skill.
Same defect class as most `claude-for-legal` siblings, but worse here: the
source's `narration_text` and `props` fields carry **literal unresolved
`>` placeholder characters** at every skill-specific fact (B00's greeting/
command, B03's "Claude's job: >", BVDT's artifact lines, BHTF's handoff
clause all contain a bare `>` where content belongs), and its
`metadata.source_skill` path (`/Users/bear/.../law-student/skills/
exam-forecast/SKILL.md`) is a different machine's home directory —
confirmed absent both there and anywhere else in this repository. No
`SCRIPT.md` existed on the source either. This is the most incomplete
source encountered in this family so far: even the general anatomy beats
had real narration, but every topic-specific line was never written.

**Judgment call, logged per the honesty rule:** rather than block on an
unrecoverable source, reconstructed the exam-forecast-specific facts
generically from the skill's name and its family's sibling law-student
skills (`bar-prep-questions`, `flashcards`, `irac-practice`,
`cold-start-interview`) — a skill that reads a course's syllabus and past
exams and ranks likely topics by how often they've previously been
tested. This is explicitly not presented as an official Anthropic
capability; it's a custom teaching skill's generic behavior, consistent
with "when in doubt, describe behavior generically." Full reasoning in
QUESTION.md and SCRIPT.md's "Deliberately not claimed" section. The
source's true, generic facts were kept verbatim: a skill is a folder
Claude reads before it works; `SKILL.md` lists steps; Claude executes
them in order; reliability comes from staying inside what the file says.

**Beat count:** source is a spare 7 beats (B00 + B01/B02/B03 anatomy-
pipeline-mechanism + BVDT verdict + BHTF handoff + BOUT outro, total
measured runtime only ~63s). hai-simple's mandatory six-move spine
(stakes, wrong guess *and* a falsifying case, mechanism, one flag, one
anchor planted-and-paid-off, both directions, carry-out) does not fit in
7 beats at 2-3 minutes of narration, so expanded to 13: B00 writer + 9
GRAPHIC body beats (B01-B09) + BCRY/BHTF/BOUT REMOTION close. The source's
general SKILL.md anatomy (B01/B02 in the source) survives as B05 here;
its "design tell"/BVDT verdict framing was dropped (Teardown judgment,
not Plain) and replaced by the six-move structure — stakes (B01), anchor
planted (B02), wrong guess (B03), broken by a case (B04), mechanism
(B05), one flag (B06), anchor payoff (B07), both directions (B08/B09).

**B00 WRITER LAW:** naive assumption that "exam forecast" means Claude
reads the textbook and tells you *exactly* what's on the exam, corrected
to "roughly" — the wrong guess this reel exists to defeat (certainty vs.
probability), broken concretely at B04 (this year's exam file is locked;
the skill reads public material instead). Typed text: "Claude reads my
textbook and tells me EXACTLY what's on the exam. What does it really
promise?" trigger "exactly" → "roughly". Narration 35 words +
`lead_silence_s: 0.8` → measured 11.16s (>= 8s TIMING LAW floor).
Verified by frame pull: correction resolves by t≈6s, full final question
("What does it really promise?") completes by t≈10.9s of the 11.17s clip.

**Body beats:** all 9 built as Manim GRAPHIC scenes via one shared
generic "chip row" renderer in `scenes.py` (title + up to 4 labeled
chips, optional arrows, optional terracotta accent/mute-strike, caption)
driven per-beat by a content dict — copied verbatim from the
`books--claude-liam-building-plugins` sibling's proven renderer, not
hand-tuned per beat. Anchor pair: B02 plants three blank ranked slots
("TOPIC 1?" / "TOPIC 2?" / "TOPIC 3?"), B07 returns the identical
three-slot composition filled in and topic-1 accented — same object,
same layout, same order, per ANCHOR LAW. One flag: B06 (the forecast only
holds where a testing record already exists; a brand-new course or a
professor who changes format yields nothing to count). Both directions:
B08 (ranked first isn't guaranteed) / B09 (ranked last isn't safe to
skip). Close: BCRY `WantQuote` (carry-out), BHTF `ClaudeComposerAsk`
(explicit `folderLabel: "@HumanitariansAI"` per the known
ClaudeComposerAsk-defaults-to-@NikBearBrown bug documented on prior
sibling builds), BOUT `OutroCTA` (@HumanitariansAI).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (13 beats), `scenes.py` (generic chip-row Manim generator
+ 9-beat content table), `render_scenes.py`. Ran `generate_audio_kokoro.py`
(13/13 beats, am_onyx, $0.00) — measured durations became the clock.
Rendered 9 Manim beats (foreground) and 4 Remotion beats via
`remotion_scenes.py` — the Remotion step exceeded the shell's 120s
default and was auto-moved to background by the harness mid-render;
rather than end the turn (one-shot invocation — no later turn exists to
receive that notification), blocked in-turn polling the actual OS
process (ffmpeg encoder, then the `remotion_scenes.py` PID directly)
until it exited 0, then verified all four `media/*.mp4` files existed
before proceeding. No orphaned renders.

**GATE T (type_check.py) first pass: 4 FAILs.**

1. **2 confirmed real min-size defects** (B03, B04): chip labels
   "HAS SEEN THE REAL EXAM?" (23 chars) and "THIS YEAR'S LOCKED EXAM"
   (23 chars) crossed the shared `_chip()` renderer's `>22 chars -> 
   font_size 18` tier, which measured out to 19px < the 20px/1.9% floor
   on the rendered frame — same class as the `books--claude-liam-
   building-plugins` precedent's "GENERATE QUESTIONNAIRE" defect.
   **Fixed at the root**: shortened the labels ("HAS SEEN THE REAL
   EXAM?" → "SEEN THE REAL EXAM?", "THIS YEAR'S LOCKED EXAM" → "THIS
   YEAR'S EXAM", and its sibling chip "THE PUBLIC SYLLABUS AND PAST
   EXAMS" → "SYLLABUS, PAST EXAMS") to land inside the `<=22 chars ->
   font_size 22` tier with margin; updated beat_sheet.json's
   `production_viz.chips` to match, re-rendered both scenes.
2. **2 confirmed false positives** (B05, B06 — and B03/B04 recurred at
   the same location after the font fix): `check_bbox_overlap` flags the
   chip's INK-bordered box (a closed ring, itself detected as a "text
   run" at its full box-height bbox) as numerically containing its own
   centered label's bbox. Verified false by cropping the exact reported
   coordinates from a mid-clip frame of all four beats' raw
   `manim/B0{3,4,5,6}.mp4`: every label sits cleanly centered inside its
   chip border with visible margin, no real text-on-text overlap. This
   is the documented `BBOX_OVERLAP_EXEMPT_PATTERNS` class already
   carrying ~15 prior entries in `type_check.py` (`B01Scene`,
   `BPB10Scene`, `MIVB01Scene`, etc.) — added `EFB03Scene`, `EFB04Scene`,
   `EFB05Scene`, `EFB06Scene` with the verification recorded inline,
   matching the exact precedent those entries were added under. Content
   defects were fixed first; this exemption covers only what was
   independently re-verified clean.

**GATE T (type_check.py) final pass: PASS, 0 FAILs.**

Compiled with `compile.py . --force` (re-compile after the B03/B04 fix):
13/13 beats real (no slate), master born natively 4K (3840×2160,
`compile.py`'s 4K LAW), 120.4s. `content-check`/`frame-check`/
`lane-check` all PASS. Non-blocking warning: motion histogram
`graphic:9 remotion:4` (69%, over the ~40% pantry cap) — logged as
structural, not a defect: hai-simple's mandated shape fixes B00/BCRY/
BHTF/BOUT as REMOTION against 9 Manim body beats for a 13-beat reel,
same disposition as every sibling in this family.

**Gate V:** pulled 20 frames at 6s spacing across the full 120.4s
runtime; read every one directly. B00's correction and full question
land inside the beat with margin. The B02→B07 anchor pair reads as the
same three-slot composition returning, topic 1 singled out at the
payoff. BCRY/BHTF/BOUT are centered, legible, safe-inset, and BHTF
correctly shows `@HumanitariansAI` (not the `ClaudeComposerAsk` Root.tsx
default `@NikBearBrown`). No remaining blockers.

**Audio:** ffprobe confirms an AAC stream present, master mtime
(02:16:45) newer than beat_sheet.json (02:14:06); `ffmpeg -af
volumedetect`: mean_volume **-23.9 dB**, max -2.9 dB — comfortably above
the -40 dB floor.

Metadata file written: `claude-for-legal--claude-liam-exam-forecast.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Playlist note:
`SUBJECT.json`'s `family` is `"claude-for-legal"`, which has no entry in
`skills/make/hai-simple/loop/playlists.json`'s map — fell through to the
`hai-simple` skill-key fallback ("Claude Basics"), consistent with every
other delivered sibling in this family (the content here is general
Claude-skill mechanics for a newcomer audience, not law-specific). Per
the DELIVERY CONTRACT format, the description also carries the direct
code link.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
