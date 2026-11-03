# BUILD-LOG — claude-for-legal--claude-liam-gaps

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-gaps/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
regulatory/legal skill `gaps`.

**Source-fidelity note (better than the `claude-for-legal--claude-liam-
case-brief` sibling redo's gap):** the source `claude-liam-gaps` beat sheet's
narration already carries the skill's real, specific description verbatim,
in four beats (B00, B03, BVDT, BHTF): "Open gaps tracker — what's flagged
and not yet closed. Use when the user asks 'what gaps are open', 'gap
tracker', 'remediation status', or wants to close (--close GAP-ID) or
risk-accept (--accept GAP-ID) a tracked gap." Unlike case-brief's source
(which never filled in its skill-specific line — literal `>` placeholder),
gaps's source narration is real, usable content, and this redo uses it as
the anchor fact as-is. What is NOT reachable from this machine is the
underlying SKILL.md file itself
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/regulatory-legal/skills/gaps/SKILL.md`
— confirmed via `find` across the local `anthropics/claude-for-legal/` tree:
only `youtube/` exists locally; no `regulatory-legal/` directory). Nothing
beyond the source's own stated spec (open tracker, report flagged/unclosed
items, close or risk-accept an item) is asserted anywhere in this redo.

**Facts kept unchanged (from the source):** a skill is a folder Claude
reads before it acts; the whole routine lives in one file (SKILL.md);
Claude reads it and executes the file's steps in order, with no branching
unless the file itself branches; a skill is a specification, not a
capability — its payoff is repeatable results, its limit is anything the
file never covers; gaps specifically opens a tracker, reports what's
flagged and not yet closed, and lets you close or risk-accept a tracked
item.

**New content added to meet hai-simple's spine (not in the source, but not
invented domain fact either):** the source has no explicit wrong-guess,
anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes —
"a gaps skill" sounds like Claude can now weigh regulations and decide what
counts as a gap), B02 (wrong guess broken with a falsifying case — delete
the skill's folder, no compliance judgment is lost, because there was none
to lose), B06 (anchor payoff — restates the design tell against the named
anchor), B07 (both directions — a clean close proves nothing about
understanding; a mishandled update proves nothing about breakage). B03/B04/
B05 carry the source's anatomy/pipeline/design-tell facts forward, with B03
now also serving as the anchor plant (gaps's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion, identical in shape to the `claude-for-legal--claude-liam-
case-brief` sibling redo (same source shape, same expansion pattern).

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a gaps
skill" means the model itself can now judge compliance risk. Typed text:
"Claude learned to judge / compliance risk from / the gaps skill. / What is
a skill?", trigger "learned" → replacement "was given", ending on the real
question. Audio 10.56s (Remotion extended to 10.6s) — clears the ≥8s WRITER
LAW floor with margin; verified on frames at t=9.5s and t=10.3s that the
correction resolves to "was given" and the full question types out to
"What is a skill?" before the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer verbatim from the case-brief sibling
redo's `scenes.py`, adapted with gaps-specific chip labels and narration.
Anchor pair: B03 plants `gaps/` + `SKILL.md` as two plain chips; B06 returns
the identical composition with `SKILL.md` accented.

**GATE T (type_check.py) — two rounds of fixes before PASS:** first run
failed 2 beats. B02 failed min-size (19px < 20px floor) because its middle
chip label "CLAUDE LOSES JUDGMENT?" (22 chars, a wide word "JUDGMENT")
forced a width-driven downscale below the floor — shortened to "LOSES ITS
JUDGMENT?" (19 chars, drops the redundant "CLAUDE"). B01 failed
bbox-overlap (a small isolated-glyph blob nested inside the first chip's
declared bbox, at the "...DE HAS A..." span — a false-positive class the
case-brief scenes.py already documents for other glyph shapes) — traced to
the standalone word "A" sitting directly before "GAPS" in "CLAUDE HAS A
GAPS SKILL"; reworded to "CLAUDE PICKED UP GAPS" (removes the isolated
single-letter word entirely) and the second chip's apostrophe
("DECIDES WHAT'S A GAP?") was also dropped in favor of "DECIDES WHAT
COUNTS?" as a precaution. Second run: GATE T PASS, 0 FAILs across all 11
beats. beat_sheet.json's `graphic.production_viz.chips` fields were kept in
sync with the final scenes.py labels.

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats (foreground,
`render_scenes.py`, exit 0, one re-render pass after the GATE T fixes) and
4 Remotion beats via `remotion_scenes.py` (the call auto-backgrounded past
the tool's 120s timeout; blocked on it explicitly with TaskOutput rather
than ending the turn, per the COMPLETION LAW — exit 0, all 4 beats
confirmed rendered before moving on).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-gaps.mp4`, 114.6s. One non-blocking WARNING
carried through compile: GRAPHIC beats are 7/11 (63%), over the toolkit's
~40% "pantry cap" motion-diversity guidance (MOTION.md) — noted, not
treated as a gate; this reel is legitimately diagram-heavy (a skill's
anatomy/mechanism/spec argument reads naturally as labeled-chip diagrams)
and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled frames across the full runtime (one per
beat, plus two extra frames inside B00 to confirm the writer correction)
and read each by hand — all legible, correct chip content, safe insets, no
overlapping text, the B03→B06 anchor pair visually identical as intended,
B07's vertical-stack layout reads cleanly. B00 confirmed: at t=9.5s the
correction has already resolved to "was given"; by t=10.3s the full
question "What is a skill?" has typed out completely, well before the
10.56s beat ends.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −2.9 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime is newer than beat_sheet.json's
last content edit — beat_sheet.json was NOT touched after this point, per
the "never touch beat_sheet.json after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery (Phase 4):** the compiled master was already native 3840×2160
(compile.py's 4K LAW), so `claude-for-legal--claude-liam-gaps-4k.mp4` is a
direct copy — no upscale needed. Wrote
`claude-for-legal--claude-liam-gaps.md` (YouTube description,
@HumanitariansAI, playlist "Claude Basics", direct code link, AI
disclosure). Ran `deliver.py --push`: staged
`DELIVERY/claude-for-legal--claude-liam-gaps/` (4K master + description) and
committed + pushed the text artifacts (README.md, beat_sheet.json,
SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md, QUESTION.md) to the
humanitarians-youtube clone under
`claude-bear/claude-for-legal--claude-liam-gaps/`.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye) and both delivery targets
(Drive outbox + humanitarians-youtube) are staged/pushed. Source-fidelity
note logged above and in QUESTION.md/SCRIPT.md/the description's
"Deliberately not claimed" section — nothing about how gaps's unread
SKILL.md internally decides what counts as a "gap" is asserted anywhere in
this reel.
