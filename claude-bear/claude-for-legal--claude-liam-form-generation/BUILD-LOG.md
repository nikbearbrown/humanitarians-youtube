# BUILD-LOG — claude-for-legal--claude-liam-form-generation

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-form-generation/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `form-generation`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in four beats (B00, B03, BVDT, BHTF), identical to the
already-documented gap on the `claude-for-legal--claude-liam-case-brief`
sibling redo. The SKILL.md form-generation was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/form-generation/SKILL.md`)
does not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`legal-clinic/` directory). This is NOT a "genuine blocker that halts the
build" per the completion law, because the source DOES establish real,
generic, true facts about how a Claude skill works (a folder Claude reads
before it acts, one file — SKILL.md — read top to bottom and executed step
by step, and the specification semantics: repeatable results in exchange
for a hard limit at the file's edge) — those facts are what carried over.
What did NOT carry over, because it was never actually present in the
source: any specific claim about which fields form-generation's particular
legal-clinic procedure actually fills or how. This redo treats
"form-generation" literally and generically — the named example of a
skill-shaped folder, using only the well-known, generic shape of a
fillable legal form (a fixed set of fields — parties, dates, signatures —
filled from case facts) as anchor flavor — and never asserts an invented
procedure from the unread SKILL.md. Logged in QUESTION.md and SCRIPT.md as
well.

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
"a form-generation skill" sounds like a drafting upgrade), B02 (wrong guess
broken with a falsifying case — delete the skill's folder, Claude can still
write a sentence, because there was no drafting talent stored there), B06
(anchor payoff — restates the design tell against the named anchor), B07
(both directions — a clean form proves nothing about understanding; a
wrong field proves nothing about breakage). B03/B04/B05 carry the source's
anatomy/pipeline/design-tell facts forward, with B03 now also serving as
the anchor plant (form-generation's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion, identical in shape to the `claude-for-legal--claude-liam-case-brief`
sibling redo, which hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
form-generation skill" means it can compose or design a legal form's
structure from a blank page. Typed text: "Claude designs the legal form /
from the form-generation skill. / What is a skill?", trigger "designs" →
replacement "was given", ending on the real question. Audio 12.1s (Remotion
extended to 12.1s) — clears the ≥8s WRITER LAW floor with margin; verified
on a late frame (t=9.5s) that the correction resolves to "was given" before
the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern from the
`claude-for-legal--claude-liam-case-brief` sibling redo verbatim, adapted
in this reel's own `scenes.py` with form-generation-specific chip labels and
narration. Anchor pair: B03 plants `form-generation/` + `SKILL.md` as two
plain chips; B06 returns the identical composition with `SKILL.md`
accented — confirmed visually identical on pulled frames. Close: BCRY
`WantQuote` (carry-out), BHTF `ClaudeComposerAsk` (explicit
`folderLabel: "@HumanitariansAI"` — the known ClaudeComposerAsk-defaults-to-
@NikBearBrown bug, worked around per precedent — confirmed correct on the
rendered frame), BOUT `OutroCTA` (@HumanitariansAI). All four Remotion +
WantQuote component prop schemas verified renderable via `./art scenes
--check` before authoring the sheet (GATE L).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats (foreground,
`render_scenes.py`, exit 0) and 4 Remotion beats via `remotion_scenes.py`
(the call auto-backgrounded past the tool's 120s timeout; blocked on it
explicitly with TaskOutput rather than ending the turn, per the COMPLETION
LAW — exit 0, all 4 beats confirmed rendered before moving on).

**GATE T (type_check.py): PASS** — 0 FAILs across all 11 beats. The
chip-row/chip-stack renderer's known kerning/bbox-overlap fixes (upright
serif captions, MUTE-not-strikethrough for rejected chips,
`render_chip_stack`'s one-phrase-per-row layout for B07) were reused
directly from the case-brief sibling, so no new type-check defect surfaced.

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-form-generation.mp4`, 118.8s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance
(MOTION.md) — noted, not treated as a gate; this reel is legitimately
diagram-heavy (a skill's anatomy/mechanism/spec argument reads naturally as
labeled-chip diagrams) and every GRAPHIC beat is original, locally-rendered
Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled frames every 6s across the full runtime and
read each by hand — all legible, correct chip content, safe insets, no
overlapping text, the B03→B06 anchor pair visually identical as intended,
B07's vertical-stack layout reads cleanly. B00's correction frame confirmed
at t=9.5s (mid-beat, well after the "was given" correction resolves).
BHTF and BOUT both confirmed carrying the @HumanitariansAI handle/folder
label, not the claude-liam default.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.0 dB**, max_volume −3.0 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime (04:34:20) is newer than
beat_sheet.json's last content edit (04:31:33) — beat_sheet.json was NOT
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
actual legal-clinic form-generation procedure is asserted anywhere in this
reel. Wrote `claude-for-legal--claude-liam-form-generation.md` (YouTube
description, @HumanitariansAI, playlist "Claude Basics", direct code link,
AI disclosure). Proceeding to Phase 4 delivery (4K render + deliver.py).
