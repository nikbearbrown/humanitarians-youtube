# BUILD-LOG — claude-for-legal--claude-liam-log-leave

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-log-leave/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `log-leave`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in four beats (B00, B03, BVDT, BHTF), matching the
identical unfilled-`>` bug already documented on the `claude-for-legal--
claude-liam-case-brief`, `-hiring-review`, `-investigation-add`,
`-investigation-query`, and `-internal-investigation` sibling redos. The
SKILL.md log-leave was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/employment-legal/skills/log-leave/SKILL.md`) does not exist on this
machine — confirmed by `find` across the whole `anthropics/claude-for-
legal/` tree (only `youtube/` exists locally; no `employment-legal/`
directory). This is NOT a "genuine blocker that halts the build" per the
completion law, because the source DOES establish real, generic, true facts
about how a Claude skill works (a folder Claude reads before it acts, one
file — SKILL.md — read top to bottom and executed step by step, and the
specification semantics: repeatable results in exchange for a hard limit at
the file's edge) — those facts are what carried over. What did NOT carry
over, because it was never actually present in the source: any specific
claim about what log-leave's particular employment-legal leave procedure
does. This redo treats "log-leave" literally and generically — the named
example of a skill-shaped folder for logging an employee's leave record —
and never asserts an invented procedure from the unread SKILL.md. Logged in
QUESTION.md and SCRIPT.md as well.

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
"a log-leave skill" sounds like Claude gained approval authority over
leave), B02 (wrong guess broken with a falsifying case — delete the skill's
folder, no approval authority is lost, because there was none to begin
with), B06 (anchor payoff — restates the design tell against the named
anchor), B07 (both directions — logging a leave request cleanly proves
nothing about judging the situation correctly; flagging something as
incomplete proves nothing's wrong). B03/B04/B05 carry the source's
anatomy/pipeline/design-tell facts forward, with B03 now also serving as
the anchor plant (log-leave's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion, identical in shape to the sibling `claude-for-legal` redos,
which hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
log-leave skill" means Claude itself can decide whether to approve an
employee's leave request. Typed text: "Claude approves / an employee's
leave request / with log-leave. / What is a skill?", trigger "approves" →
replacement "logs", ending on the real question. Audio 9.6s (clears the
≥8s WRITER LAW floor); verified on a frame at t=9.0s that the correction
resolves to "logs" and the question types out to "What is a skill" (caret
mid-word before the final "?") well before the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern from the sibling redos verbatim,
adapted in this reel's own `scenes.py` with log-leave-specific chip labels
and narration. Anchor pair: B03 plants `log-leave/` + `SKILL.md` as two
plain chips; B06 returns the identical composition with `SKILL.md`
accented.

**GATE T:** first `type_check.py` run (post-compile) came back GATE T:
PASS (0 FAILs across all 11 beats) — no exemptions or fixes needed.

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-log-leave.mp4`, 123.1s. One non-blocking
WARNING carried through compile: GRAPHIC beats are 7/11 (63%), over the
toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md) — noted,
not treated as a gate; this reel is legitimately diagram-heavy (a skill's
anatomy/mechanism/spec argument reads naturally as labeled-chip diagrams)
and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled one frame per beat from the compiled master
(B00 t=9.0s … BOUT t=121s) and read each by hand — all legible, correct
chip content, safe insets, no overlapping text, the B03→B06 anchor pair
visually identical as intended (SKILL.md accent moves from B03's plain
state to B06's terracotta fill), B07's vertical-stack layout reads cleanly,
B00's correction confirmed resolved to "logs" well before the beat ends,
BCRY/BHTF/BOUT carry the Humanitarians AI skin correctly (@HumanitariansAI
handle/folderLabel, humanitarians palette, subscribe CTA).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −3.0 dB — comfortably clears the
−40 dB floor.

**Resolution confirmed:** `ffprobe` on the compiled master: 3840×2160
(native 4K; compile.py's 4K LAW forced this directly, no upscale pass
needed as a separate step for delivery).

**Master vs. beat_sheet.json:** beat_sheet.json was not touched after the
final compile, per the "never touch beat_sheet.json after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery:** `claude-for-legal--claude-liam-log-leave-4k.mp4` created — a
copy of the compiled master, which was already genuine 3840x2160 (the
Remotion beats are natively 4K; the Manim beats are 1080p source upscaled
into the 4K canvas by the compile step itself, same as every other GRAPHIC
beat in this pipeline). Wrote `claude-for-legal--claude-liam-log-leave.md`
(YouTube description, @HumanitariansAI, playlist "Claude Basics", direct
code link, AI disclosure). Ran `deliver.py --push`: staged
`DELIVERY/claude-for-legal--claude-liam-log-leave/` (4K master +
description) and committed the text artifacts to the humanitarians-youtube
clone under `claude-bear/claude-for-legal--claude-liam-log-leave/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md).

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Delivery staged to both
targets. Source-fidelity gap logged above and in QUESTION.md/SCRIPT.md/the
description's "Deliberately not claimed" section — nothing about the
actual employment-legal log-leave procedure is asserted anywhere in this
reel.
