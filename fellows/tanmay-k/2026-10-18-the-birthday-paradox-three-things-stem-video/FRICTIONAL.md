# Frictional Log: the-birthday-paradox-three-things (Week 27 topic video)

**Record provenance:** drafted 2026-10-17 with Claude from this folder's own records (`TOPIC-DECISION.md`, `DRAW.md`,
`CANDIDATES.md`, `ANGLE.md`, `FACTCHECK.md`, `BEATS-DRAFT.md`, `PEDAGOGY.md`, `STILLS-QC.md`, the `PROOF-REVIEW*.md` files)
and the working session, after the work was done rather than while it happened. **Awaiting Tanmay's review.** Every entry
points at the record it comes from.

## 2026-10-16 — A topic nobody had taken

- **Work and expectation:** draw the week's topic at random from the `claude-for-<topic>/<topic-name>` entries in
  `humanitarians-youtube`, make sure no fellow has used it, and use only commands that read.
- **Where it resisted:**
  - The repo holds 22 usable categories and 2,456 topic-name pairs, most of them variants of the same topic under different
    folder names (`nbb-`, `claude-liam-`, `vox-`, `hai-`).
  - Searching file contents branch by branch took about ten minutes per candidate, and the first shell loop silently searched
    nothing (an unquoted variable in zsh; a missing `mapfile` in macOS bash).
- **What was done:**
  - Switched to one pass over every unique text file reachable from all 65 refs (56,521 files), with a control search
    (`braess`, 41 hits) to prove the scan finds things.
  - Seed 20261016 drew `claude-for-cancer`; Tanmay asked for a different seed. Seed 27 drew `claude-for-video-production`.
  - Ten counterintuitive-statistics subjects were checked inside it; four were already taken (Simpson, survivorship, Braess,
    Berkson). Seed 2701 drew **birthday paradox** from the six free ones; 0 hits for the name or its ideas.
- **Decided by:** Tanmay set the rules and the redraw; the seeds decided the topic.
- **Record:** `DRAW.md`, `CANDIDATES.md`, `TOPIC-DECISION.md`.

## 2026-10-16 — Real people and sources that could hurt the channel

- **Work and expectation:** the angle was to test the model on real groups, so the first plan used presidents' birthdays and
  World Cup squads.
- **Where it resisted:** Tanmay ruled it out: strictly no political content, and only sources with no copyright risk to the
  channel.
- **What was done:** presidents and rosters dropped; the "real calendar" is US federal births-by-day counts (NCHS and SSA),
  plus our own simulations. The two CSVs were downloaded only after Tanmay approved them by name; they are not redistributed.
- **Decided by:** Tanmay.
- **Record:** `ANGLE.md`, `RESULTS.md`, `FACTCHECK.md` §2.

## 2026-10-16 — The result was flat, so the film changed shape

- **Work and expectation:** show that real, uneven birthdays change the 50.7% answer.
- **Where it resisted:** they barely do (50.8%, a tenth of a point). Clustering groups into a window of days changes it hugely,
  but seasonality inside the window adds almost nothing again.
- **What was done:** the film was rebuilt around that finding: three things you could change (people, evenness, days) and a
  square-root rule that the numbers already showed. The rule was then checked against the exact answer for every slot count
  from 2 to 2,000: exact for 1,161, one person off for 838, never more.
- **Decided by:** the numbers; Tanmay approved the angle.
- **Record:** `RESULTS.md`, `sqrt-rule.json`, `BEATS-DRAFT.md`.

## 2026-10-16 — A form that was already someone's thesis

- **Work and expectation:** the first draft was built on writing a prediction down before each result, and scored 10/12.
- **Where it resisted:** PROOF's form sweep found that `vox-prediction-lock` in the shared repo teaches exactly that
  ("a prediction you can edit is worth nothing"). The same review found a wrong word in B13 ("first test" for the second) and
  an unsupported claim ("within a few percent of average"; the lowest day is 0.567 of average).
- **What was done:** the prediction device was dropped and the film restructured; the unsupported claim became a measured one
  (96.4% of days within 10%); the wording error was fixed. Tanmay's Gate P sign-off was re-opened for the changed beats.
- **Decided by:** PROOF's review found the overlap; Tanmay asked for a 12/12 film, Claude chose the restructure, and Tanmay approved it by signing Gate P on draft 2.
- **Record:** `PROOF-REVIEW.md`, `ANGLE.md`, `PEDAGOGY.md`.

## 2026-10-16 — A maths renderer that was not installed

- **Work and expectation:** typeset the rule with a real radical and fraction, as the toolkit's maths rule requires.
- **Where it resisted:** the toolkit's `typeset_math.py` needs matplotlib, which is installed in none of the Pythons here.
- **What was done:** built the slates as a standalone Pillow drawer with a small structural layout for the equations (real
  radical, fraction bar, sized parentheses) instead of falling back to plain text; algebra checked separately.
- **Decided by:** Claude, reported to Tanmay in `STILLS-QC.md`; Tanmay approved the stills.
- **Record:** `STILLS-QC.md`, `build_slates.py`.

## 2026-10-16 — Stills, then motion, then the cut

- **Work and expectation:** review every beat as a picture, then build motion, audio and the master once.
- **Where it resisted:**
  - Looking at the stills found a dozen layout defects the number checks could not see (overlapping labels, a text overflow,
    missing check glyphs), and Tanmay asked for three more fixes.
  - PROOF on the stills found type that was too small for a phone (17–22 px), source lines too close to the bottom edge, and
    small accent text below contrast; all fixed and now enforced by `check_onscreen.py`.
  - PROOF on the compiled cut found two figures shown late: B13 spoke three head-counts over an empty slide, and B08's
    "96%" appeared three seconds after it was said.
- **What was done:** both timing issues fixed by reordering reveals, only B08 and B13 re-encoded, the master recompiled once.
  Measured on the master: 84 reveals on cue, the 8 s hold measures 8.69 s, no black frames, −14.9 LUFS / −1.9 dBTP.
- **Decided by:** Tanmay on the stills; PROOF's checks on the rest.
- **Record:** `PROOF-REVIEW-STILLS.md`, `PROOF-REVIEW-CUT.md`, `STILLS-QC.md`.

## 2026-10-17 — A Short that is one scene, not stitched beats

- **Work and expectation:** a 9:16 trailer for the long film, with its own script and one continuous arc (Tanmay's rule since
  Weeks 23 and 24), and a PROOF review with criteria specific to Shorts.
- **Where it resisted:**
  - The long film's habits did not carry over. PROOF's first Shorts pass scored the plan 10/12: the spoken hook began after a
    name introduction, and a Short cannot carry a link. Tanmay asked for 12/12; the bet now opens the Short and the name moves into
    the answer, and the closing text gives the long film's exact searchable title. Gate P was re-read for those two lines.
  - Kokoro voiced a three-word sentence on its own ("Add a half.") as "that'll have". Short sentences are now merged into their
    neighbour before synthesis.
  - The gate's own measurements were too coarse at first (a dot landing is invisible at 108×192), and the first compile trimmed four
    frames off the video. Both fixed, then re-measured.
  - The counter showed 57% and 50.8% while the calendar was still widening at the end; a static stretch of 3.07 s sat under
    "and it's ninety five percent". Both fixed: the widening now finishes as "twenty three" is said, and the number swells on its cue.
- **What was done:** a single scene rendered frame by frame from a function of time (1,633 frames at 2160×3840), every event timed to
  the Whisper word clock, compiled once. Measured on the master: all 11 production-gate items pass; no cut above 2.33 grey levels;
  longest static stretch 2.57 s; the last frame matches the opening state to 0.16 grey levels.
- **Decided by:** Tanmay set the rules, the 12/12 target and the Gate P sign-offs; PROOF's criteria and measurements found the rest.
- **Record:** `PROOF-REVIEW-SHORT.md`, `SHORT-SCRIPT.md`, `FACTCHECK-SHORT.md`, `GATE-P-SIGNOFF-SHORT.md`, `proof_short_output.txt`.

## 2026-10-17 — Watched and listened

- **What was done:** Tanmay watched the master and listened; no changes. The three words Whisper flagged (B09 "it", B13
  "and", B16 "a") and the names were part of that listen.
- **Record:** `PROOF-REVIEW-CUT.md`. He then watched and listened to the Short too, with no changes; the Short's by-ear items ("Add a half", "Squeeze it to one month", the pace, his name) were part of that.
