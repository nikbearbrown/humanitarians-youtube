# BUILD-LOG — claude-for-legal--claude-liam-matter-briefing

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-matter-briefing/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-ops skill `matter-briefing`.

**Source-fidelity note (better than the `case-brief`/`gaps` siblings, still
logged):** the source SKILL.md
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/matter-briefing/SKILL.md`)
does not exist on this machine — confirmed via `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`litigation-legal/` directory). Unlike `case-brief`, this source's own
beat_sheet.json narration was NOT left with an unfilled `>` placeholder — B00
speaks the skill's job in full: "Deep briefing on one matter — current
posture, what's changed, next deadline, open questions, and a risk
re-assessment check, ready before a GC update or outside counsel call. Use
when the user says 'brief me on [matter]', 'where are we on [matter]', or
needs a read on a specific matter." Every specific claim in this redo about
what matter-briefing produces traces to that sentence (same
source-narration-is-sufficient precedent used on the `gaps` sibling redo).
Nothing about the unread SKILL.md's actual internal steps is invented.
Logged in QUESTION.md and SCRIPT.md as well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
an ongoing capability — its payoff is a repeatable five-part read (current
posture, what's changed, next deadline, open questions, a risk
re-assessment check), its limit is anything the file/record doesn't cover.

**New content added to meet hai-simple's spine (not in the source, but not
invented legal-specific fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes — "a
matter-briefing skill" sounds like it's been keeping tabs on the case),
B02 (wrong guess broken with a falsifying case — delete the skill's folder,
no update on the matter is forgotten, because nothing was being tracked),
B06 (anchor payoff — restates the design tell against the named anchor), B07
(both directions — a sharp briefing proves nothing about completeness; a
briefing with a gap proves nothing about the skill being broken). B03/B04/B05
carry the source's anatomy/pipeline/design-tell facts forward, with B03 also
serving as the anchor plant (matter-briefing's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 + 7
body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — the identical-shape
expansion used on the `case-brief` and `gaps` sibling redos, which hit the
same compact-source-format situation.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
matter-briefing skill" means it's been quietly tracking the legal matter
over time, building a running memory of it. Typed text: "Claude has been
tracking / this legal matter. / What is a skill?", trigger "tracking" →
replacement "handed a file on", ending on the real question. Audio 10.1s
(Remotion extended to 10.1s) — clears the ≥8s WRITER LAW floor with margin;
verified on a late frame (t=9.5s) that the correction resolves to "handed a
file on" and the full question types out to "What is a skill?" before the
beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer verbatim from the `case-brief` sibling
redo, adapted in this reel's own `scenes.py` with matter-briefing-specific
chip labels and narration. Anchor pair: B03 plants `matter-briefing/` +
`SKILL.md` as two plain chips; B06 returns the identical composition with
`SKILL.md` accented.

**GATE T fix pass required (2 iterations):** first run failed B01 — a
bbox-overlap false positive from an isolated single-letter word "A" sitting
directly before "MATTER" in "CLAUDE HAS A MATTER SKILL" (the exact defect
class already documented on the `gaps` sibling's chip-row renderer for
isolated single-letter words). Reworded to "CLAUDE HAS MATTER-BRIEFING" —
still FAILed, same location, this time from the isolated hyphen glyph in
"MATTER-BRIEFING" forming its own tiny disconnected ink blob nested inside
the chip's bbox. Reworded again to "CLAUDE PICKED UP THIS SKILL" (no
hyphens, no single-letter words) — GATE T PASS 0 FAILs after. Both fixes
applied to `scenes.py` BEAT_CONTENT and mirrored into beat_sheet.json's
`graphic.production_viz.chips` before recompiling.

Close: BCRY `WantQuote` (carry-out), BHTF `ClaudeComposerAsk` (explicit
`folderLabel: "@HumanitariansAI"`), BOUT `OutroCTA` (@HumanitariansAI). All
four Remotion + WantQuote component prop schemas verified renderable via
`./art scenes --check` before authoring the sheet (GATE L).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats (foreground,
`render_scenes.py`, exit 0, one re-render after the GATE T fix) and 4
Remotion beats via `remotion_scenes.py` (foreground, exit 0, all 4 beats
confirmed rendered before moving on — no backgrounding, per the COMPLETION
LAW).

**GATE T (type_check.py):** FAIL → FAIL → **PASS** (0 FAILs across all 11
beats after the second B01 rewording).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-matter-briefing.mp4`, 122.3s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md) —
noted, not treated as a gate; this reel is legitimately diagram-heavy (a
skill's anatomy/mechanism/spec argument reads naturally as labeled-chip
diagrams) and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled one representative frame per beat (timestamps
at each beat's midpoint) from the compiled 4K master and read each by hand —
all legible, correct chip content, safe insets, no overlapping text, the
B03→B06 anchor pair visually identical as intended, B07's vertical-stack
layout reads cleanly, BHTF's `folderLabel` correctly shows
`@HumanitariansAI`, BOUT carries the HAI subscribe skin. B00's correction
frame confirmed at t=9.5s (mid-beat, well after the "handed a file on"
correction resolves and the full question has typed out).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −3.0 dB — comfortably clears the
−40 dB floor. Confirmed via `ffprobe` the master carries both a video stream
(3840×2160) and an audio stream.

**Master vs. beat_sheet.json:** master mtime (16:15) is newer than
beat_sheet.json's last content edit (16:12, the GATE T fix); beat_sheet.json
was NOT touched after this point, per the "never touch beat_sheet.json after
compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity note logged
above and in QUESTION.md/SCRIPT.md/the description's "Deliberately not
claimed" section — nothing about matter-briefing's actual internal SKILL.md
steps is asserted anywhere in this reel.
