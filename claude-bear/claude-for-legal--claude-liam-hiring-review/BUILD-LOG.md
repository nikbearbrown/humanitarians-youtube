# BUILD-LOG — claude-for-legal--claude-liam-hiring-review

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-hiring-review/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `hiring-review`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in three beats (B00, B03, BVDT), matching the identical
unfilled-`>` bug already documented on the `claude-for-legal--claude-liam-
case-brief` and `claude-for-legal--claude-liam-build-guide` sibling redos.
The SKILL.md hiring-review was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/employment-legal/skills/hiring-review/SKILL.md`) does not exist on
this machine — confirmed by `find` across the whole `anthropics/claude-for-
legal/` tree (only `youtube/` exists locally; no `employment-legal/`
directory). This is NOT a "genuine blocker that halts the build" per the
completion law, because the source DOES establish real, generic, true facts
about how a Claude skill works (a folder Claude reads before it acts, one
file — SKILL.md — read top to bottom and executed step by step, and the
specification semantics: repeatable results in exchange for a hard limit at
the file's edge) — those facts are what carried over. What did NOT carry
over, because it was never actually present in the source: any specific
claim about what hiring-review's particular employment-legal checklist
actually contains. This redo treats "hiring-review" literally and
generically — the named example of a skill-shaped folder that walks through
a hiring decision — and never asserts an invented procedure from the unread
SKILL.md. Logged in QUESTION.md and SCRIPT.md as well.

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
"a hiring-review skill" sounds like Claude got hiring authority), B02 (wrong
guess broken with a falsifying case — delete the skill's folder, Claude
loses no hiring judgment, because there was none to begin with), B06
(anchor payoff — restates the design tell against the named anchor), B07
(both directions — flagging every risk proves nothing about understanding;
flagging nothing proves nothing about a clean hire). B03/B04/B05 carry the
source's anatomy/pipeline/design-tell facts forward, with B03 now also
serving as the anchor plant (hiring-review's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion to satisfy hai-simple's mandatory six-move spine, identical in
shape to the `claude-for-legal--claude-liam-case-brief` sibling redo, which
hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
hiring-review skill" means Claude itself gained the authority to decide who
gets hired. Typed text: "Claude decides who / gets hired with the /
hiring-review skill. / What is a skill?", trigger "decides" → replacement
"checks", ending on the real question. Audio 9.47s (Remotion extended to
9.5s) — clears the ≥8s WRITER LAW floor; verified on a late frame (t=8.5s)
that the correction resolves to "checks" and the sentence reads "Claude
checks who gets hired with the hiring-review..." before the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern from the `claude-for-legal--
claude-liam-case-brief` sibling redo verbatim, adapted in this reel's own
`scenes.py` with hiring-review-specific chip labels and narration. Anchor
pair: B03 plants `hiring-review/` + `SKILL.md` as two plain chips; B06
returns the identical composition with `SKILL.md` accented.

**GATE T iteration (read before assuming a first-pass pattern name is
correct):** the first `type_check.py` run — executed BEFORE `compile.py` —
came back GATE T FAIL, flagging §8.6b bbox-overlap on B02 and B07 (chip
border-ring blob mistaken for a text run, the same documented false-positive
class already exempted in `BBOX_OVERLAP_EXEMPT_PATTERNS` for sibling scenes
`BGB01Scene`/`BGB04Scene`/`BGB07Scene`). Root cause: `type_check.py`
resolves the exemption lookup key (`beat_pattern`) from `beat.build.status`
— for GRAPHIC/Manim beats that field is only stamped by `compile.py`, not by
`render_scenes.py`, so running type_check before compiling leaves
`beat_pattern` empty and no exemption can match. **Correct order is render →
compile → type_check (GATE T)**, matching `simple`'s own documented Step 5.
After compiling: `BGB07Scene` was already covered by the deposition-prep
sibling's pre-existing exemption entry (scene names are shared across reels
via the generic chip renderer); `BGB02Scene` was not yet listed, so it was
added to `BBOX_OVERLAP_EXEMPT_PATTERNS` in `runtime/scripts/type_check.py`
with a comment, verified first by cropping the exact flagged frame region
(confirmed: the "LOSES JUDGMENT?" chip's own INK border ring encloses its
own label, no second element, no genuine text-on-text collision). Separately,
GATE T also flagged a genuine §8.1 min-size defect on B02: the original
chip label "CLAUDE LOSES JUDGMENT?" (22 chars) exceeded its chip's width cap
and autoscaled below the 20px floor — fixed by shortening the label to
"LOSES JUDGMENT?" (15 chars, matching the case-brief sibling's label-length
budget) and shortening the caption from "there was no judgment to begin
with" to "no judgment to begin with". B02 was re-rendered and the reel
recompiled twice; the second post-compile `type_check.py` run came back
GATE T: PASS (0 FAILs across all 11 beats).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-hiring-review.mp4`, 119.25s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md)
— noted, not treated as a gate; this reel is legitimately diagram-heavy (a
skill's anatomy/mechanism/spec argument reads naturally as labeled-chip
diagrams) and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled frames from the compiled master at one
representative timestamp per beat (B00 t=5s … BOUT t=117s) and read each by
hand — all legible, correct chip content, safe insets, no overlapping text,
the B03→B06 anchor pair visually identical as intended, B07's vertical-stack
layout reads cleanly, B00's correction confirmed resolved to "checks" well
before the beat ends, BCRY/BHTF/BOUT carry the Humanitarians AI skin
correctly (@HumanitariansAI handle, humanitarians palette, subscribe CTA).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.0 dB**, max_volume −2.9 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime (06:40:59) is newer than
beat_sheet.json's last content edit (06:39:34) — beat_sheet.json was NOT
touched after this point, per the "never touch beat_sheet.json after
compile" law; any further fix from here would require a full recompile.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery:** `claude-for-legal--claude-liam-hiring-review-4k.mp4` created —
a copy of the compiled master, which was already genuine 3840×2160 (the
Remotion beats are natively 4K; the Manim beats are 1080p source upscaled
into the 4K canvas by the compile step itself, same as every other GRAPHIC
beat in this pipeline). Wrote
`claude-for-legal--claude-liam-hiring-review.md` (YouTube description,
@HumanitariansAI, playlist "Claude Basics", direct code link, AI
disclosure). Ran `deliver.py --push` to stage
`DELIVERY/claude-for-legal--claude-liam-hiring-review/` and commit text
artifacts to the humanitarians-youtube clone under
`claude-bear/claude-for-legal--claude-liam-hiring-review/`.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity gap logged
above and in QUESTION.md/SCRIPT.md/the description's "Deliberately not
claimed" section — nothing about the actual employment-legal hiring-review
procedure is asserted anywhere in this reel.
