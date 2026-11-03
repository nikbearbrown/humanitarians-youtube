# BUILD-LOG — claude-for-legal--claude-liam-internal-investigation

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-internal-investigation/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `internal-investigation`. Picked up with only
SUBJECT.json present; built entirely fresh this invocation.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in three beats (B00, B03, BVDT), and its "Reference:"
line ("shared framework for managing internal investigations from.") is
itself cut off mid-sentence — matching the identical unfilled-`>` bug
already documented on the `claude-for-legal--claude-liam-hiring-review` and
`claude-for-legal--claude-liam-case-brief` sibling redos. The SKILL.md
internal-investigation was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/employment-legal/skills/internal-investigation/SKILL.md`) does not
exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`employment-legal/` directory). This is NOT a "genuine blocker that halts
the build" per the completion law, because the source DOES establish real,
generic, true facts about how a Claude skill works (a folder Claude reads
before it acts, one file — SKILL.md — read top to bottom and executed step
by step, and the specification semantics: repeatable results in exchange
for a hard limit at the file's edge) — those facts are what carried over.
What did NOT carry over, because it was never actually present in the
source: any specific claim about what internal-investigation's particular
employment-law procedure actually contains. This redo treats
"internal-investigation" literally and generically — the named example of
a skill-shaped folder that walks through organizing an investigation — and
never asserts an invented procedure from the unread SKILL.md. Logged in
QUESTION.md and SCRIPT.md as well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
a capability — its payoff is repeatable results, its limit is anything the
file never covers.

**New content added to meet hai-simple's spine (not in the source, but not
invented employment-law fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes — "an
internal-investigation skill" sounds like Claude got investigative
authority), B02 (wrong guess broken with a falsifying case — delete the
skill's folder, Claude loses no investigative judgment, because there was
none to begin with), B06 (anchor payoff — restates the design tell against
the named anchor), B07 (both directions — flagging every irregularity
proves nothing about understanding; flagging nothing proves nothing about
no wrongdoing). B03/B04/B05 carry the source's anatomy/pipeline/design-tell
facts forward, with B03 now also serving as the anchor plant
(internal-investigation's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion, identical in shape to the `claude-for-legal--claude-liam-
hiring-review` sibling redo, which hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has an
internal-investigation skill" means Claude itself can run an investigation
and decide who's at fault. Typed text: "Claude decides who's / at fault
using the / internal-investigation / skill. What is a skill?", trigger
"decides" → replacement "documents", ending on the real question. Audio
12.57s (Remotion extended to 12.6s) — clears the ≥8s WRITER LAW floor by a
wide margin; verified on a frame at t=10.5s that the correction resolves to
"documents" and the sentence reads "Claude documents who's at fault using
the internal-investigation skill..." well before the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern verbatim from the `claude-for-
legal--claude-liam-hiring-review` sibling redo, adapted in this reel's own
`scenes.py` with internal-investigation-specific chip labels and narration.
Anchor pair: B03 plants `internal-investigation/` + `SKILL.md` as two plain
chips; B06 returns the identical composition with `SKILL.md` accented.

**GATE T iteration (read before assuming a first-pass label length is safe):**
the first `type_check.py` run — executed AFTER `compile.py`, per the
documented render → compile → type_check order — came back GATE T FAIL,
flagging a genuine §8.1 min-size defect on B01: the chip label "CLAUDE HAS
AN INVESTIGATION SKILL" (33 chars, longer than the analogous 25-char label
that passed on the hiring-review sibling) got squeezed via `set_width` below
the 20px floor once autoscaled into its 3.4-unit-wide chip. Fixed by
shortening the label to "AN INVESTIGATION SKILL" (22 chars, matching the
case-brief/hiring-review sibling label-length budget and landing in the
renderer's larger 22px font tier instead of the 17px tier). B01 was
re-rendered and the reel recompiled once; the second post-compile
`type_check.py` run came back GATE T: PASS (0 FAILs across all 11 beats).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-internal-investigation.mp4`, 125.83s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md)
— noted, not treated as a gate; this reel is legitimately diagram-heavy (a
skill's anatomy/mechanism/spec argument reads naturally as labeled-chip
diagrams) and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled frames from the compiled master at one
representative timestamp per beat (t=6s B00 … t=123s BOUT) and read each by
hand — all legible, correct chip content, safe insets, no overlapping text,
the B03→B06 anchor pair visually identical as intended (same two-chip
layout, accent moved from none to SKILL.md), B07's vertical-stack layout
reads cleanly, B00's correction confirmed resolved to "documents" well
before the beat ends, BCRY/BHTF/BOUT carry the Humanitarians AI skin
correctly (@HumanitariansAI handle, humanitarians palette, subscribe CTA,
Fable 5 High composer chrome).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.0 dB**, max_volume −2.8 dB — comfortably clears the
−40 dB floor. (Also confirmed inline by compile.py's own GATE AUDIO: PASS.)

**Master vs. beat_sheet.json:** master mtime (07:58:13) is newer than
beat_sheet.json's last content edit (07:57:07) — beat_sheet.json was NOT
touched after this point, per the "never touch beat_sheet.json after
compile" law; any further fix from here would require a full recompile.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery:** wrote
`claude-for-legal--claude-liam-internal-investigation.md` (YouTube
description, @HumanitariansAI, playlist "Claude Basics", direct code link,
AI disclosure). 4K render and `deliver.py --push` to follow in this same
invocation (see the delivery block appended below once run).

**Status: DONE (review cut).** Review cut passes every gate (content-check,
frame-check, lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity
gap logged above and in QUESTION.md/SCRIPT.md/the description's
"Deliberately not claimed" section — nothing about the actual
employment-law internal-investigation procedure is asserted anywhere in
this reel.
