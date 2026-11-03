# BUILD-LOG — claude-for-legal--claude-liam-investigation-memo

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-investigation-memo/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `investigation-memo`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific fill. A literal `>` placeholder survives verbatim in two
beats (B03's `body`, BHTF's `command`), and a related, separate defect sits
in B00's `output` line and BVDT's `artifactLines`: the sentence "Draft or
update the privileged investigation memo from the." is truncated
mid-clause and never completed. This matches the identical unfilled-source
bug already documented on the `claude-for-legal--claude-liam-hiring-
review`, `claude-for-legal--claude-liam-case-brief`, and `claude-for-
legal--claude-liam-build-guide` sibling redos. The SKILL.md investigation-
memo was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/employment-legal/skills/investigation-memo/SKILL.md`) does not exist
on this machine — confirmed by `find` across the whole `anthropics/claude-
for-legal/` tree (only `youtube/` exists locally; no `employment-legal/`
directory). This is NOT a "genuine blocker that halts the build" per the
completion law, because the source DOES establish real, generic, true facts
about how a Claude skill works (a folder Claude reads before it acts, one
file — SKILL.md — read top to bottom and executed step by step, and the
specification semantics: repeatable results in exchange for a hard limit at
the file's edge) — those facts are what carried over. What did NOT carry
over, because it was never actually present in the source: any specific
claim about what investigation-memo's particular employment-legal procedure
or memo template actually contains. This redo treats "investigation-memo"
literally and generically — the named example of a skill-shaped folder that
writes up an investigation in a fixed structure — and never asserts an
invented procedure from the unread SKILL.md. Logged in QUESTION.md and
SCRIPT.md as well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
a capability — its payoff is repeatable results, its limit is anything the
file never covers.

**New content added to meet hai-simple's spine (not in the source, but not
invented employment-law fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes —
"an investigation-memo skill" sounds like Claude got investigative
authority), B02 (wrong guess broken with a falsifying case — delete the
skill's folder, Claude loses no investigative judgment, because there was
none to begin with), B06 (anchor payoff — restates the design tell against
the named anchor), B07 (both directions — a thorough memo proves nothing
about understanding; a thin memo proves nothing about a clean case). B03/
B04/B05 carry the source's anatomy/pipeline/design-tell facts forward, with
B03 now also serving as the anchor plant (investigation-memo's single
SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion, identical in shape to the `claude-for-legal--claude-liam-
hiring-review` sibling redo, which hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has an
investigation-memo skill" means Claude itself gained the authority to
determine what happened. Typed text: "Claude decides what / really happened
using / investigation-memo. / What is a skill?", trigger "decides" →
replacement "documents", ending on the real question. Audio 10.2s clears
the ≥8s WRITER LAW floor.

**B00 render note:** the first `remotion_scenes.py` invocation timed out at
the harness's 2-minute default before finishing all four Remotion beats;
B00's underlying `npx remotion render` subprocess had already produced a
raw clip by then, but the process was killed before `extend_clip_to_
duration` ran, leaving a stale, un-trimmed 20.2s file on disk (the
component's natural full-performance length for this text, not the 10.2s
beat length). Caught by an independent ffprobe check before compiling —
duration mismatched the 10.2s audio. Fixed by re-running with a longer
timeout and `--only B00 --force`, which produced a correctly-trimmed
10.2s clip; verified on a frame at t=9.3s that the correction resolves to
"documents" well before the beat ends (see the review's saved frame).
Lesson for future invocations of this skill: always run
`remotion_scenes.py` with a timeout generous enough to cover all Remotion
beats in one pass (600s here), and independently verify each Remotion
output's duration against the beat's `actual_duration_s` before trusting a
"filled already (skip)" log line — a skip only means the file exists, not
that it was ever correctly conformed to length.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern from the `claude-for-legal--
claude-liam-hiring-review` sibling redo verbatim, adapted in this reel's own
`scenes.py` with investigation-memo-specific chip labels and narration.
Anchor pair: B03 plants `investigation-memo/` + `SKILL.md` as two plain
chips; B06 returns the identical composition with `SKILL.md` accented.

**GATE T iteration:** first `type_check.py` run (after compile) came back
GATE T FAIL — §8.1 min-size on B01: the chip label "CLAUDE HAS AN
INVESTIGATION SKILL" (34 chars) autoscaled to a 15px text run, below the
20px floor. Fixed by shortening the label to "INVESTIGATION SKILL" (20
chars, matching the hiring-review sibling's label-length budget), then
re-rendering B01's Manim scene and recompiling. Second `type_check.py` run:
GATE T PASS (0 FAILs across all 11 beats).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-investigation-memo.mp4`, 123.9s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (64%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md)
— noted, not treated as a gate; this reel is legitimately diagram-heavy (a
skill's anatomy/mechanism/spec argument reads naturally as labeled-chip
diagrams) and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled frames from the compiled master at one
representative timestamp per beat (t=5s … t=121s) and read each by hand —
all legible, correct chip content, safe insets, no overlapping text, the
B03→B06 anchor pair visually identical as intended, B07's vertical-stack
layout reads cleanly, B00's correction confirmed resolved to "documents"
well before the beat ends, BCRY/BHTF/BOUT carry the Humanitarians AI skin
correctly (@HumanitariansAI handle, humanitarians palette, subscribe CTA).

**Audio presence:** independent `ffmpeg -af volumedetect` on the compiled
master: mean_volume **−24.1 dB**, max_volume −2.8 dB — comfortably clears
the −40 dB floor.

**Master vs. beat_sheet.json:** master mtime is newer than beat_sheet.json's
last content edit (the B01 chip-label fix, applied before the final
compile) — beat_sheet.json was NOT touched after this point, per the
"never touch beat_sheet.json after compile" law; any further fix from here
would require a full recompile.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery:** `claude-for-legal--claude-liam-investigation-memo-4k.mp4`
created — a copy of the compiled master, which was already genuine
3840×2160 (the Remotion beats are natively 4K; the Manim beats are 1080p
source upscaled into the 4K canvas by the compile step itself, same as
every other GRAPHIC beat in this pipeline). Wrote
`claude-for-legal--claude-liam-investigation-memo.md` (YouTube description,
@HumanitariansAI, playlist "Claude Basics", direct code link, AI
disclosure). Ran `deliver.py --push`, which staged
`DELIVERY/claude-for-legal--claude-liam-investigation-memo/` (4K master +
description) and committed the text artifacts (README.md, beat_sheet.json,
SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md, QUESTION.md) to the
humanitarians-youtube clone under
`claude-bear/claude-for-legal--claude-liam-investigation-memo/` — reported
"repo: committed + pushed".

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity gap logged
above and in QUESTION.md/SCRIPT.md/the description's "Deliberately not
claimed" section — nothing about the actual employment-legal investigation-
memo procedure is asserted anywhere in this reel.
