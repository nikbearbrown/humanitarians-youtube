# BUILD-LOG — financial-services--claude-liam-idea-generation

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-idea-generation/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
Anthropic partner-built skill `idea-generation`. Built as the direct sibling
of `financial-services--claude-liam-gl-recon` (same day, same pattern) — same
chip-row/chip-stack Manim renderer, same 11-beat expansion shape.

**Source-fidelity check:** the source's job line survives verbatim across
its B00 beat (B03/BVDT in the source truncate the same line mid-word to
"…thematic res." / "…quantitative s." — a template-truncation bug in the
source script, not reproduced here): "Systematic stock screening and
investment idea sourcing. Combines quantitative screens, thematic research,
and pattern recognition to surface new long and short ideas. Use when
looking for new ideas, running screens, or conducting thematic sweeps.
Triggers on 'idea generation', 'stock screen', 'find ideas', 'what looks
interesting', 'screen for', 'new ideas', or 'pitch me something'." The
source's anatomy beat (B01) lists exactly one real file: `SKILL.md` (3k,
accented) — no second file is ever named, so none is invented here. The
skill's own source file
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-
services/plugins/agent-plugins/market-researcher/skills/idea-generation/
SKILL.md`) is not reachable from this machine (confirmed via `find` — no
match anywhere under the local `financial-services` book) — same class of
gap as the `gl-recon` sibling redo — but nothing here depends on reading it:
every fact used traces to the source's own filled-in beats. Logged in
QUESTION.md and SCRIPT.md as well.

**Facts kept unchanged (from the source):** a skill is a folder Claude reads
before it acts; idea-generation's folder holds one file that matters,
SKILL.md; Claude reads it and executes steps in a fixed linear order (read
→ execute → return output); the job is systematic stock screening and
investment idea sourcing, combining quantitative screens, thematic
research, and pattern recognition to surface new long and short candidates;
it is a specification, not a capability — repeatable results are the
payoff, anything outside the spec is the limit.

**New content added to meet hai-simple's spine (not in the source, but not
invented financial fact either):** the source has no explicit wrong-guess,
anchor, or both-directions beat. Added: B01 (stakes — "an idea-generation
skill" sounds like Claude is creatively brainstorming, free-associating the
way an analyst might in a pitch meeting), B02 (wrong guess broken with a
falsifying case — run the same screen twice on the same data and the same
candidates come back both times, not two different creative pitches), B06
(anchor payoff — restates the design tell against the named anchor). B03/
B04/B05 carry the source's anatomy/pipeline/design-tell facts forward, with
B03 also serving as the anchor plant: an illustrative screen (rising free
cash flow plus recent insider buying) surfacing 3 candidates, tagged
"pattern match" — built to visualize the source's own literal three
mechanisms (quantitative screens, thematic research, pattern recognition),
not a claim about any real screen or ticker the skill has processed. B07
(both directions) is new: a candidate surfacing proves nothing about trade
quality; a candidate never surfacing proves nothing about badness.

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — the identical
proportionate expansion used on the `financial-services--claude-liam-
gl-recon` sibling redo.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has an
idea-generation skill" means Claude itself is creatively brainstorming new
stock ideas, free-associating the way an analyst might in a pitch meeting.
Typed text: "Claude brainstorms / new stock ideas with / idea-generation. /
What does it actually do?", trigger "brainstorms" → replacement "screens
for", ending on the real question. Audio 11.07s — clears the ≥8s WRITER LAW
floor comfortably; verified on frame pulls at t=5.5s (correction already
resolved: "Claude screens for new stock|") and t=9.8s ("Claude screens for
new stock ideas with idea-generation. Wh|" — mid-typing the final question)
that the correction lands well before the beat ends (11.07s total).

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer verbatim from the `financial-services--
claude-liam-gl-recon` sibling redo, adapted in this reel's own `scenes.py`
with idea-generation-specific chip labels and narration. Anchor pair: B03
plants "FCF UP + INSIDER BUYING" → "PATTERN MATCH" → "3 CANDIDATES SURFACE"
as three arrow-connected chips; B06 returns the identical composition with
the candidate-count chip accented.

**GATE T iteration:** first `type_check.py` run (after render + compile)
came back GATE T FAIL with one finding: **B06 bbox-overlap §8.6b** — frame
pull at t=5.3s (mid-beat, raw `manim/B06.mp4`) confirmed the reported
blob@(729,437)-(1190,588) enclosing blob@(822,495)-(876,529) is the
"PATTERN MATCH" chip's own INK border ring enclosing its own interior
label — no second element, no genuine text-on-text collision. Same
documented border-ring-encloses-label false-positive class already exempted
for `BGB01/02/03/04/05/07Scene` (gl-recon and other siblings sharing this
renderer). Added `BGB06Scene` to `BBOX_OVERLAP_EXEMPT_PATTERNS` in the
shared `runtime/scripts/type_check.py`, with a frame-pull-verified comment.

Second `type_check.py` run came back **GATE T: PASS** (0 FAILs across all
11 beats) — no beat content or scenes.py layout was changed, only the one
new exemption entry in the shared `runtime/scripts/type_check.py`.

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`financial-services--claude-liam-idea-generation.mp4`, 129.6s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance
(MOTION.md) — noted, not treated as a gate; this reel is legitimately
diagram-heavy (a skill's anatomy/mechanism/spec argument reads naturally as
labeled-chip diagrams) and every GRAPHIC beat is original, locally-rendered
Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled frames from the compiled master at t=5.5,
9.8 (B00 late-frame correction check), 16.6, 27, 38, 50.5, 62, 73, 86, 99,
115, 128 and read each by hand — all legible, correct chip content, safe
insets, no overlapping text, the B03→B06 anchor pair visually identical as
intended (candidate-count chip accented on return), B07's paired-stack
layout reads cleanly, B00's correction confirmed resolved to "screens for"
well before the beat ends, BCRY/BHTF/BOUT carry the Humanitarians AI skin
correctly (@HumanitariansAI handle, humanitarians palette, Fable 5
composer, subscribe CTA).

**Audio presence:** `compile.py`'s own GATE AUDIO check: mean_volume
**−24.1 dB** — comfortably clears the −40 dB floor.

**Master vs. beat_sheet.json:** master mtime (1788316091) is newer than
beat_sheet.json's last content edit (1788315938) — the sheet was NOT
touched after the final compile; the GATE T fix was applied entirely in the
shared `type_check.py` exemption list, never in this reel's beat_sheet.json
or scenes.py content, per the "never touch beat_sheet.json after compile"
law.

**Playlist resolution:** `SUBJECT.json`'s family `"financial-services"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field), which resolves
to **"Claude Basics."** Not the bare "Claude," per the PLAYLIST LAW.

**Status: REVIEW CUT DONE.** `financial-services--claude-liam-idea-
generation.mp4` (129.6s, 3840×2160, mean_volume -24.1 dB) is newer than
beat_sheet.json's last content edit; beat_sheet.json was never touched
after the final compile. Passes content-check, frame-check, lane-check,
GATE AUDIO, GATE T, and Gate V by eye.
