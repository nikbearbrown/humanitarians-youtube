# BUILD-LOG — claude-for-legal--claude-liam-expansion-kickoff

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-expansion-kickoff/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-team skill `expansion-kickoff`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in four beats (B00, B03, BVDT, BHTF), matching the
identical unfilled-`>` bug already documented on the
`claude-for-legal--claude-liam-case-brief` sibling redo (and, per its log,
also on `claude-for-legal--claude-liam-build-guide`) — this looks like a
batch-wide defect across the whole `claude-for-legal/youtube/` skill-
teardown set, not a one-off. The SKILL.md expansion-kickoff was meant to
describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/expansion-kickoff/SKILL.md`)
does not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`employment-legal/` directory). This is NOT a "genuine blocker that halts
the build" per the completion law, because the source DOES establish real,
generic, true facts about how a Claude skill works (a folder Claude reads
before it acts, one file — SKILL.md — read top to bottom and executed step
by step, and the specification semantics: repeatable results in exchange
for a hard limit at the file's edge) — those facts are what carried over.
What did NOT carry over, because it was never actually present in the
source: any specific claim about what expansion-kickoff's particular
legal-team procedure does. This redo treats "expansion-kickoff" literally
and generically — the named example of a skill-shaped folder, using only
the generic, well-known idea of a "starting checklist" as anchor flavor —
and never asserts an invented procedure from the unread SKILL.md. Logged
in QUESTION.md and SCRIPT.md as well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
a capability — its payoff is repeatable results, its limit is anything the
file never covers.

**New content added to meet hai-simple's spine (not in the source, but not
invented legal-specific fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes — "an
expansion-kickoff skill" sounds like a strategy upgrade), B02 (wrong guess
broken with a falsifying case — delete the skill's folder, no expansion
planning is forgotten, because there was nothing to learn), B06 (anchor
payoff — restates the design tell against the named anchor), B07 (both
directions — a tidy plan proves nothing about understanding; a rough one
proves nothing about breakage). B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts forward, with B03 now also serving as the anchor
plant (expansion-kickoff's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion to satisfy hai-simple's mandatory six-move spine, identical in
shape to the `claude-for-legal--claude-liam-case-brief` sibling redo, which
hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has an
expansion-kickoff skill" means the model itself learned expansion planning.
Typed text: "Claude learned expansion / planning from that skill. / What is
a skill?", trigger "learned" → replacement "was given", ending on the real
question. First attempt used a longer text ("Claude learned expansion
planning\nfrom the expansion-kickoff skill.\nWhat is a skill?") whose
natural typing performance ran 20.24s against an 11.84s narration — far
past the ~15% LADDER_RETIME window, which would have made compile.py
CENTER-CUT the clip (skip ~4.2s off both ends), risking a truncated open
that never shows the correction. Shortened the on-screen text to match the
case-brief precedent's proportions and re-rendered: natural duration came
in under the audio and got padding-extended to 11.8s instead, matching the
"extended to Xs" pattern seen on every other beat. Verified on frames at
t=6.0s and t=10.5s: the correction has already resolved to "was given" by
mid-beat, well before the beat ends — clears the WRITER LAW requirement
with margin.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer verbatim from the
`claude-for-legal--claude-liam-case-brief` sibling redo's `scenes.py`,
adapted in this reel's own copy with expansion-kickoff-specific chip labels
and narration. Anchor pair: B03 plants `expansion-kickoff/` + `SKILL.md` as
two plain chips; B06 returns the identical composition with `SKILL.md`
accented. Close: BCRY `WantQuote` (carry-out), BHTF `ClaudeComposerAsk`
(explicit `folderLabel: "@HumanitariansAI"` — the known
ClaudeComposerAsk-defaults-to-@NikBearBrown bug, worked around per
precedent — confirmed correct on the rendered frame), BOUT `OutroCTA`
(@HumanitariansAI). All four Remotion + WantQuote component prop schemas
verified renderable via `./art scenes --check` before authoring the sheet
(GATE L).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats (foreground,
`render_scenes.py`, exit 0). Rendered 4 Remotion beats via
`remotion_scenes.py`: the first attempt (all 4 beats in one call) hit the
tool's 2-minute foreground timeout partway through (exit 143) — B00 had
already written media/B00.mp4 but the process was killed before stamping
provenance or reaching BCRY/BHTF/BOUT. Confirmed no orphaned render process
was left running (`ps aux` showed no live remotion/manim child from this
invocation), then re-ran each remaining beat individually in the foreground
(`--only BCRY`, `--only BHTF`, `--only BOUT`, then `--only B00 --force`
after the text fix) — all four completed well inside the tool's timeout
this way, each confirmed exit 0 before moving on, per the COMPLETION LAW.

**GATE T (type_check.py):** PASS on both the pre-render structural pass
(`--skip-pixels`, 0 FAILs) and the post-render full pass (0 FAILs across
all 11 beats) — the chip-row/chip-stack renderer's known kerning/bbox-
overlap fixes (upright serif captions, MUTE-not-strikethrough for rejected
chips, one-phrase-per-row layout for B07) were reused directly from the
case-brief sibling, so no new type-check defect surfaced.

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-expansion-kickoff.mp4`, 120.9s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md)
— noted, not treated as a gate; this reel is legitimately diagram-heavy (a
skill's anatomy/mechanism/spec argument reads naturally as labeled-chip
diagrams) and every GRAPHIC beat is original, locally-rendered Manim, not
pantry/stock footage.

**Gate V (visual QC):** pulled frames at 1-per-6s across the full runtime
and read a representative frame from every beat by hand — all legible,
correct chip content, safe insets, no overlapping text, the B03→B06 anchor
pair visually identical as intended, B07's vertical-stack layout reads
cleanly, B00's correction confirmed resolved well before the beat ends, the
first-beat `@HumanitariansAI` caption overlay present and correctly
positioned, BHTF's composer card carries `@HumanitariansAI` (not the
library default), and the OutroCTA closes with the restated title and
handle.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −3.0 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime (02:43) is newer than
beat_sheet.json's last content edit (02:41) — beat_sheet.json was NOT
touched after this point, per the "never touch beat_sheet.json after
compile" law; any further fix from here would require a full recompile.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Status: DONE (review cut).** Review cut passes every gate
(content-check, frame-check, lane-check, GATE AUDIO, GATE T, Gate V by
eye). Source-fidelity gap logged above and in QUESTION.md/SCRIPT.md/the
description's "Deliberately not claimed" section — nothing about the
actual legal-team expansion-kickoff procedure is asserted anywhere in this
reel. Wrote `claude-for-legal--claude-liam-expansion-kickoff.md` (YouTube
description, @HumanitariansAI, playlist "Claude Basics", direct code link,
AI disclosure, chapter timestamps computed from measured beat durations).

**Not yet done (Phase 4 — deliver):** 4K master already exists as the
compiled cut itself (3840×2160 natively); still need to produce the
`-4k.mp4` copy and run `deliver.py --push` to stage `DELIVERY/<slug>/` and
commit text artifacts to the humanitarians-youtube clone. Proceeding to
that now in this same invocation.
