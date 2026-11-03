# BUILD-LOG — claude-for-legal--claude-liam-investigation-add

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-investigation-add/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `investigation-add`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in three beats (B00, B03, BVDT), matching the identical
unfilled-`>` bug already documented on the `claude-for-legal--claude-liam-
case-brief` and `claude-for-legal--claude-liam-hiring-review` sibling redos.
The SKILL.md investigation-add was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/employment-legal/skills/investigation-add/SKILL.md`) does not exist on
this machine — confirmed by `find` across the whole `anthropics/claude-for-
legal/` tree (only `youtube/` exists locally; no `employment-legal/`
directory). This is NOT a "genuine blocker that halts the build" per the
completion law, because the source DOES establish real, generic, true facts
about how a Claude skill works (a folder Claude reads before it acts, one
file — SKILL.md — read top to bottom and executed step by step, and the
specification semantics: repeatable results in exchange for a hard limit at
the file's edge) — those facts are what carried over. What did NOT carry
over, because it was never actually present in the source: any specific
claim about what investigation-add's particular employment-legal intake
procedure does. This redo treats "investigation-add" literally and
generically — the named example of a skill-shaped folder for logging a new
workplace investigation — and never asserts an invented procedure from the
unread SKILL.md. Logged in QUESTION.md and SCRIPT.md as well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
a capability — its payoff is repeatable results, its limit is anything the
file never covers.

**New content added to meet hai-simple's spine (not in the source, but not
invented legal-specific fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes —
"an investigation-add skill" sounds like Claude gained investigative
authority), B02 (wrong guess broken with a falsifying case — delete the
skill's folder, no investigative authority is lost, because there was none
to begin with), B06 (anchor payoff — restates the design tell against the
named anchor), B07 (both directions — filling every field of an
investigation record proves nothing about judging the situation correctly;
leaving one blank proves nothing's wrong). B03/B04/B05 carry the source's
anatomy/pipeline/design-tell facts forward, with B03 now also serving as
the anchor plant (investigation-add's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion, identical in shape to the `claude-for-legal--claude-liam-case-
brief` and `claude-for-legal--claude-liam-hiring-review` sibling redos,
which hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has an
investigation-add skill" means Claude itself can open a workplace
investigation on its own authority. Typed text: "Claude opens a new /
workplace investigation / with investigation-add. / What is a skill?",
trigger "opens" → replacement "logs", ending on the real question. Audio
10.71s (media/B00.mp4 source render 20.2s, center-cut to 10.7s in compile)
— clears the ≥8s WRITER LAW floor with margin; verified on a frame at
t=9.5s that the correction resolves to "logs" and the full question types
out to "What is a skill?" before the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern from the `claude-for-legal--
claude-liam-hiring-review` sibling redo verbatim, adapted in this reel's
own `scenes.py` with investigation-add-specific chip labels and narration.
Anchor pair: B03 plants `investigation-add/` + `SKILL.md` as two plain
chips; B06 returns the identical composition with `SKILL.md` accented.

**GATE T iteration:** the first `type_check.py` run (post-compile) came
back GATE T FAIL on B01 — §8.1 min-size, smallest text run 15px < the 20px
floor. Root cause: the original chip label "CLAUDE HAS AN INVESTIGATION
SKILL" (34 chars) exceeded the chip-row renderer's autoscale budget for a
2-chip row and got squeezed below the floor — the identical failure class
the `hiring-review` sibling hit and fixed by shortening a label. Fixed by
shortening the label to "PICKED UP A SKILL" (17 chars, matching the
sibling's label-length budget), updated in both `scenes.py`'s
`BEAT_CONTENT["B01"]` and beat_sheet.json's descriptive `chips` field. B01
was re-rendered and the reel recompiled once (only B01's manim/B01.mp4
changed; the other 10 beats' encoded media were untouched by the second
compile pass). The second post-compile `type_check.py` run came back
GATE T: PASS (0 FAILs across all 11 beats).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-investigation-add.mp4`, 126.3s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md)
— noted, not treated as a gate; this reel is legitimately diagram-heavy (a
skill's anatomy/mechanism/spec argument reads naturally as labeled-chip
diagrams) and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled frames from the compiled master at one
representative timestamp per beat (B00 t=9.5s … BOUT t=124s) and read each
by hand — all legible, correct chip content, safe insets, no overlapping
text, the B03→B06 anchor pair visually identical as intended (SKILL.md
accent moves from B03's plain state to B06's terracotta fill), B07's
vertical-stack layout reads cleanly, B00's correction confirmed resolved to
"logs" well before the beat ends, BCRY/BHTF/BOUT carry the Humanitarians AI
skin correctly (@HumanitariansAI handle/folderLabel, humanitarians palette,
subscribe CTA).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −3.0 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime (09:09:28) is newer than
beat_sheet.json's last content edit (09:08:26, the B01 label fix prior to
the second compile) — beat_sheet.json was NOT touched after the final
compile, per the "never touch beat_sheet.json after compile" law; any
further fix from here would require a full recompile.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery:** `claude-for-legal--claude-liam-investigation-add-4k.mp4`
created — a copy of the compiled master, which was already genuine
3840x2160 (the Remotion beats are natively 4K; the Manim beats are 1080p
source upscaled into the 4K canvas by the compile step itself, same as
every other GRAPHIC beat in this pipeline). Wrote
`claude-for-legal--claude-liam-investigation-add.md` (YouTube description,
@HumanitariansAI, playlist "Claude Basics", direct code link, AI
disclosure). Ran `deliver.py --push`: staged
`DELIVERY/claude-for-legal--claude-liam-investigation-add/` (4K master +
description) and committed the text artifacts to the humanitarians-youtube
clone under `claude-bear/claude-for-legal--claude-liam-investigation-add/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md) - commit + push confirmed.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Delivery staged to both
targets. Source-fidelity gap logged above and in QUESTION.md/SCRIPT.md/the
description's "Deliberately not claimed" section - nothing about the
actual employment-legal investigation-add procedure is asserted anywhere in
this reel.
