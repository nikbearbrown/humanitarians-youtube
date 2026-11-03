# BUILD-LOG — financial-services--claude-liam-nav-tieout

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-nav-tieout/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
Anthropic partner-built skill `nav-tieout`. Built from a bare `SUBJECT.json`
(no prior scaffolding existed in the target reel dir) end-to-end to a
verified review cut in this invocation, following the `financial-services--
claude-liam-gl-recon` sibling redo's proven pattern exactly (same family,
same reconciliation/tie-out shape, same generic chip-row Manim renderer).

**Source-fidelity check:** the source's job line survives verbatim across
its B00/B03/BVDT beats: "Tie an LP statement to the fund's NAV pack —
recompute the LP's capital account from the NAV components and flag any
line that doesn't agree. Use before LP statements are distributed." The
source's anatomy beat (B01) describes a skill as a folder holding one file,
SKILL.md — "plain language, no hidden logic... the file is the program" —
read then executed in a fixed linear pipeline (B02: read → execute each step
in order → return output). The design-tell/verdict beats (B03/BVDT) state
the specification semantics: repeatable results are the payoff, anything
outside the spec is the limit. The skill's own source file
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-
services/plugins/agent-plugins/statement-auditor/skills/nav-tieout/
SKILL.md`) is not reachable from this machine (confirmed via `find`) — the
same class of gap documented on other `financial-services` sibling redos —
but nothing here depends on reading it: every fact used traces to the
source's own filled-in beats. Logged in QUESTION.md and SCRIPT.md as well.

**Facts kept unchanged (from the source):** a skill is a folder Claude reads
before it acts, holding one file that matters, SKILL.md, in plain language
with no hidden logic; Claude reads it and executes steps in a fixed linear
order; nav-tieout's job is to recompute an LP's capital account from the
fund's NAV pack components and flag any line in the LP statement that
disagrees; it is a specification, not independent judgment — repeatable
results are the payoff, anything outside the spec is the limit.

**New content added to meet hai-simple's spine (not in the source, but not
invented financial fact either):** the source has no explicit wrong-guess,
anchor, or both-directions beat. Added: B01 (stakes — "a nav-tieout skill"
sounds like Claude is independently confirming the fund's NAV is accurate),
B02 (wrong guess broken with a falsifying case — run nav-tieout on a period
with a known LP-statement error, and the NAV pack's own components don't
move; only a flagged mismatch appears on the LP side, because the skill
never touches the NAV pack), B06 (anchor payoff — restates the design tell
against the named anchor), B07 (both directions — a flagged mismatch proves
nothing about which side actually has the error; a clean tie-out proves
nothing about whether the NAV itself was calculated correctly). B03/B04/B05
carry the source's anatomy/pipeline/design-tell facts forward, with B03 also
serving as the anchor plant: an illustrative $404,000 NAV-pack vs. $400,000
LP-statement gap, flagged at $4,000 — built to visualize the source's own
literal job line (recompute from the NAV components, flag disagreement), not
a claim about any real fund, LP, or account the skill has processed.

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 + 7
body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — the identical
proportionate expansion used on the `financial-services--claude-liam-gl-
recon` sibling redo.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
nav-tieout skill" means Claude itself is confirming the fund's NAV is
accurate. Typed text: "Claude proves the / fund's NAV is / correct with
nav-tieout. / What does it actually do?", trigger "proves" → replacement
"assumes", ending on the real question. Audio 11.14s — clears the ≥9s
TIMING LAW floor comfortably (34-word narration + `lead_silence_s` 0.8);
verified on a late frame (t=9.5s) that the correction reads "Claude assumes
the fund's NAV is correct with nav-tieout. What does..." well before the
beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer verbatim from the `financial-services--
claude-liam-gl-recon` sibling redo, adapted in this reel's own `scenes.py`
with nav-tieout-specific chip labels and narration. Anchor pair: B03 plants
"NAV PACK $404,000" → "LP STMT $400,000" → "FLAGGED $4,000 GAP" as three
arrow-connected chips; B06 returns the identical composition with the
flagged chip accented.

**GATE T iteration:** first `type_check.py` run (after render + compile) came
back GATE T FAIL with the same false-positive class already documented on
the `gl-recon` sibling — chip RoundedRectangle border rings enclosing their
own interior labels:
1. **B02 bbox-overlap §8.6b + kerning §8.4** — reported blob@(189,437)-
   (650,588) enclosing blob@(422,502)-(464,523); kerning gap 441px vs.
   176px threshold. Verified false positive by frame pull at t=6s: the
   3-chip arrow row ("RUN ON A KNOWN LP ERROR" → "CHANGES THE NAV PACK?" →
   "NAV PACK UNCHANGED") reads cleanly, no text-on-text overlap — the
   box-to-box arrow-shaft gaps between chips at the same y-band are being
   read as one oversized inter-glyph gap, same mechanism as `BGB02Scene`.
2. **B03/B06 bbox-overlap §8.6b** — reported blob@(189,437)-(650,588)
   enclosing blob@(450,494)-(530,530). Verified false positive by frame
   pull at t=6s into each beat: "NAV PACK $404,000" sits cleanly inside its
   own bordered box with visible margin — the reported enclosing blob is
   the chip's own INK border ring, not a second element. Same pattern as
   `BGB03Scene`.

Added `BNB02Scene`, `BNB03Scene`, `BNB06Scene` to `BBOX_OVERLAP_EXEMPT_
PATTERNS` and `BNB02Scene` to `KERNING_EXEMPT_PATTERNS` in the shared
`runtime/scripts/type_check.py`, each with a frame-pull-verified comment.
Second `type_check.py` run came back **GATE T: PASS** (0 FAILs across all 11
beats) — no beat content or scenes.py layout was changed, only the four new
exemption entries in the shared `type_check.py`.

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`financial-services--claude-liam-nav-tieout.mp4`, 133.2s. One non-blocking
WARNING carried through compile: GRAPHIC beats are 7/11 (63%), over the
toolkit's ~40% "pantry cap" motion-diversity guidance (MOTION.md) — noted,
not treated as a gate, per the NO-GENAI/NO-PANTRY LAW (every beat is
GRAPHIC or REMOTION, never pantry/stock).

**Gate V (visual QC):** pulled frames from the compiled master at 13
timestamps spanning the full 133s runtime (t=3, 12, 20, 28, 40, 52, 65, 78,
90, 100, 112, 122, 130), plus a targeted B00 late-frame check (t=9.5s of
`media/B00.mp4`), and read each by hand — all legible, correct chip content,
safe insets, no overlapping text, the B03→B06 anchor pair visually identical
as intended (flagged-gap chip accented on return), B07's vertical-stack
layout reads cleanly, B00's correction confirmed resolved to "assumes" well
before the beat ends, BCRY/BHTF/BOUT carry the Humanitarians AI skin
correctly (@HumanitariansAI handle, humanitarians palette, Fable 5 composer,
subscribe CTA). t=20 landed mid-transition (a normal fade in-between frame,
not a defect).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −2.9 dB — comfortably clears the
−40 dB floor.

**Master vs. beat_sheet.json:** master mtime (1788333675) is newer than
beat_sheet.json's mtime (1788333520) — beat_sheet.json was never touched
after the final compile; the GATE T fix was applied entirely in the shared
`type_check.py` exemption lists.

**Playlist resolution:** `SUBJECT.json`'s family `"financial-services"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field), which resolves to
**"Claude Basics."** Not the bare "Claude," per the PLAYLIST LAW — same
resolution as the `gl-recon` sibling.

**Status: REVIEW CUT DONE.** Review cut passes every gate (content-check,
frame-check, lane-check, GATE AUDIO, GATE T, Gate V by eye). Final master
`financial-services--claude-liam-nav-tieout.mp4` (133.2s, 3840×2160,
mean_volume -24.1 dB) is newer than beat_sheet.json; beat_sheet.json was
never touched after the final compile. Proceeding to Phase 4 (4K + delivery).
