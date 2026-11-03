# BUILD-LOG — claude-for-legal--claude-liam-material-contract-schedule

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-material-contract-schedule/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
corporate-legal skill `material-contract-schedule`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in four beats (B00, B03, BVDT, BHTF), matching the
identical unfilled-`>` bug already documented on the
`claude-for-legal--claude-liam-case-brief` and `...-build-guide` sibling
redos. The SKILL.md material-contract-schedule was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/material-contract-schedule/SKILL.md`)
does not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`corporate-legal/` directory). Also checked this book's own
`youtube/video-ideas.md`: Candidate 11 (source `corporate-legal/README.md`)
covers a related mechanism (schema imposition / typed diligence columns)
but explicitly EXCLUDES "the disclosure schedule build" from its own
scope — i.e. it documents a sibling skill, not this one — so that material
was deliberately NOT borrowed here either. This is NOT a "genuine blocker
that halts the build" per the completion law, because the source DOES
establish real, generic, true facts about how a Claude skill works (a
folder Claude reads before it acts, one file — SKILL.md — read top to
bottom and executed step by step, and the specification semantics:
repeatable results in exchange for a hard limit at the file's edge) —
those facts are what carried over. What did NOT carry over, because it was
never actually present in the source: any specific claim about what
material-contract-schedule's particular corporate-legal procedure does.
This redo treats "material-contract-schedule" literally and generically —
the named example of a skill-shaped folder, using only the well-known,
generic shape of a material contracts disclosure schedule (a document,
produced during M&A diligence, listing contracts material to a deal) as
anchor flavor — and never asserts an invented procedure from the unread
SKILL.md. Logged in QUESTION.md and SCRIPT.md as well.

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
"a material-contract-schedule skill" sounds like a deal-review upgrade),
B02 (wrong guess broken with a falsifying case — delete the skill's
folder, no contract law is forgotten, because there was nothing to learn),
B06 (anchor payoff — restates the design tell against the named anchor),
B07 (both directions — a schedule with every row filled in proves nothing
about completeness; a schedule with gaps proves nothing about breakage).
B03/B04/B05 carry the source's anatomy/pipeline/design-tell facts forward,
with B03 now also serving as the anchor plant (material-contract-schedule's
single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion to satisfy hai-simple's mandatory six-move spine, identical in
shape to the `claude-for-legal--claude-liam-case-brief` and `...-build-
guide` sibling redos, which hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
material-contract-schedule skill" means the model itself learned contract
law. Typed text: "Claude learned contract law / from the material-
contract-schedule skill. / What is a skill?", trigger "learned" →
replacement "was given", ending on the real question. Audio 12.54s
(Remotion extended to 12.5s) — clears the ≥8s WRITER LAW floor with wide
margin; verified on a frame at t=9.5s that the correction resolves to "was
given" and the question is typing out cleanly toward "What is a skill?".

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern from the
`claude-for-legal--claude-liam-case-brief` sibling redo verbatim, adapted
in this reel's own `scenes.py` with material-contract-schedule-specific
chip labels and narration. Anchor pair: B03 plants `mcs/` + `SKILL.md` as
two plain chips (shortened folder label — the full
`material-contract-schedule/` string overflowed the chip renderer's fixed
3.4-unit width badly enough to risk a GATE T min-size false-fail on a long
mono-font run; `mcs/` is introduced by narration in the same beat, so the
abbreviation reads unambiguously); B06 returns the identical composition
with `SKILL.md` accented. Close: BCRY `WantQuote` (carry-out), BHTF
`ClaudeComposerAsk` (explicit `folderLabel: "@HumanitariansAI"` — the known
ClaudeComposerAsk-defaults-to-@NikBearBrown bug, worked around per
precedent — confirmed correct on the rendered frame), BOUT `OutroCTA`
(@HumanitariansAI). All four Remotion + WantQuote component prop schemas
verified renderable via `./art scenes --check` before authoring the sheet
(GATE L).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats (foreground,
`render_scenes.py`, exit 0) and 4 Remotion beats via `remotion_scenes.py`
(the call auto-backgrounded past the tool's 120s timeout; blocked on it
explicitly with TaskOutput rather than ending the turn, per the COMPLETION
LAW — exit 0, all 4 beats confirmed rendered before moving on).

**GATE T (type_check.py): PASS** — 0 FAILs, including the `mcs/` short
anchor label (verified no min-size or bbox-overlap failure on either
anchor beat).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-material-contract-schedule.mp4`, 126.0s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11
(63%), over the toolkit's ~40% "pantry cap" motion-diversity guidance
(MOTION.md) — noted, not treated as a gate; this reel is legitimately
diagram-heavy (a skill's anatomy/mechanism/spec argument reads naturally
as labeled-chip diagrams) and every GRAPHIC beat is original,
locally-rendered Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled 2fps frames across the full runtime and read
one representative frame per beat by hand — all legible, correct chip
content, safe insets, no overlapping text, the B03→B06 anchor pair
visually identical as intended, B07's vertical-stack layout reads cleanly.
B00's correction frame confirmed at t=9.5s (mid-beat, well after the "was
given" correction resolves, question typing toward completion). BHTF
confirmed `@HumanitariansAI` folder label renders correctly. BOUT confirmed
`OutroCTA` with `@HumanitariansAI` handle.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.0 dB**, max_volume −3.0 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime is newer than beat_sheet.json's
last content edit — beat_sheet.json was NOT touched after this point, per
the "never touch beat_sheet.json after compile" law; any further fix from
here would require a full recompile.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Delivery:** master was already genuine 3840×2160 4K (the Remotion beats
are natively 4K; the Manim beats are 1080p source upscaled into the 4K
canvas by the compile step itself) — copied as
`claude-for-legal--claude-liam-material-contract-schedule-4k.mp4`. Wrote
`claude-for-legal--claude-liam-material-contract-schedule.md` (YouTube
description, @HumanitariansAI, playlist "Claude Basics", direct code link,
AI disclosure). Ran `deliver.py --push` to stage
`DELIVERY/claude-for-legal--claude-liam-material-contract-schedule/` and
commit text artifacts to the humanitarians-youtube clone under
`claude-bear/claude-for-legal--claude-liam-material-contract-schedule/`.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity gap logged
above and in QUESTION.md/SCRIPT.md/the description's "Deliberately not
claimed" section — nothing about the actual corporate-legal
material-contract-schedule procedure is asserted anywhere in this reel.
