# BUILD-LOG — claude-for-legal--claude-liam-investigation-open

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-investigation-open/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `investigation-open`. This invocation resumed a
partially-built reel: SCRIPT.md, QUESTION.md, CARRY-OUT.md, beat_sheet.json,
Kokoro audio (11/11 beats), and Manim renders (B01-B07) already existed on
disk from a prior pass; only B00's Remotion timing and the remaining
Remotion beats needed finishing.

**Source-fidelity blocker, and how it was handled:** the source's
beat_sheet.json never received its skill-specific "Claude's job: ___" fill —
the literal placeholder `>` survives verbatim in three beats (B00, B03,
BVDT), matching the identical unfilled-`>` bug already documented on the
`claude-for-legal--claude-liam-case-brief`, `-hiring-review`,
`-internal-investigation`, and `-investigation-add` sibling redos. The
SKILL.md investigation-open was meant to describe does not exist on this
machine (confirmed: only `youtube/` exists locally under
`anthropics/claude-for-legal/`; no `employment-legal/` directory). Not a
build-halting blocker per the completion law: the source DOES establish
real, generic, true facts about how a Claude skill works, and one genuine
fact fragment survived intact in both B00 and BVDT — "Open a new internal
investigation matter — runs intake,". This redo keeps that fragment as the
only investigation-open-specific claim and otherwise treats the name as a
generic anchor example. Full account in QUESTION.md and SCRIPT.md.

**Beat-count note:** source is 7 beats; result here is B00 + 7 body beats
(B01-B07) + BCRY/BHTF/BOUT = 11 beats — the same proportionate expansion
pattern as the sibling redos, to satisfy hai-simple's mandatory six-move
spine (WRONG-GUESS / ANCHOR / BOTH-DIRECTIONS each need their own beat).

**B00 WRITER LAW / TIMING LAW — bug found and fixed this session:** the
existing B00 render (from the prior pass) had narration at 11.31s (clears
the ≥8s floor) but the `BrutalistHesitantWriter` props inherited the
component's higher-friction defaults (`mistakeRate:5, hesitateWithin:2,
hesitateBetween:12, charMs:46, jitter:26`). Simulating the component's exact
seeded timeline (reimplemented `buildTimeline`/`buildActs` in Node against
the installed `remotion` package's `random()`, at the composition's real
fps=30 — confirmed via `Root.tsx`, not assumed) showed the full typing
performance needed **13.73s**, 2.4s longer than the 11.31s clip. The
rendered clip was being cut off mid-third-line ("...investigation-open.")
and never reached the final line, "What is a skill?" — silently violating
"end ON the question." This is exactly the render-duration-caps-at-
actual_duration_s trap the pilot lesson warns about, just manifesting via
component-internal pacing instead of a too-short narration.

Fix: retuned B00's props to `mistakeRate:2, hesitateWithin:1,
hesitateBetween:6, charMs:34, jitter:20` (same `triggerWords:"launches" ->
"opens"` correction, same seed). Re-simulated: full performance now
completes in **8.93s** at fps=30, leaving a ~2.4s hold on the finished
question before the 11.31s clip ends. Re-rendered via `remotion_scenes.py
--only B00 --force`. Verified on pulled frames: "launches" types fully in
accent color by t=2s, corrects to "opens" by t=2.5s (the WRITER LAW
correction is visible), and the full text — ending on "What is a skill?" —
is on screen and holding by t=9.5s through t=11s (the TIMING LAW "end ON
the question" requirement, now actually met). Audio track confirmed present
on the re-rendered clip via ffprobe.

**Remaining Remotion beats:** BHTF and BOUT had already been rendered in a
prior (apparently backgrounded) pass. Rendered BCRY (`WantQuote`, the
carry-out card) this session via `remotion_scenes.py` with no `--only` flag
— it picked up the one unfilled slot and left the others alone.

**Compile:** `compile.py` produced a clean 3840x2160 master directly (no
declared slates — all 11 beats real media):
`claude-for-legal--claude-liam-investigation-open.mp4`, 130.44s.
content-check, frame-check, and lane-check all PASS. One non-blocking
WARNING: GRAPHIC beats are 7/11 (63%), over the ~40% pantry-cap
motion-diversity guidance (MOTION.md) — noted, not a gate; this reel is
legitimately diagram-heavy (a skill's anatomy/mechanism/spec argument reads
naturally as labeled-chip diagrams) and every GRAPHIC beat is original,
locally-rendered Manim.

**GATE T:** ran `type_check.py` after compiling (render -> compile ->
type_check order, per `simple`'s documented Step 5). Result: **PASS, 0
FAILs** across all 11 beats on every check (min-size, overflow, contrast,
contrast-local, bbox-overlap, card-clip, kerning) — no exemption additions
needed this time.

**Gate V (visual QC):** pulled frames every 6s across the full 130s master
and read each by hand — B00's correction and finished-question hold
confirmed; B01/B02 (stakes, wrong-guess-broken) legible with correct
accent/strike marks; B03/B06 anchor pair visually identical
(`investigation-open/` + `SKILL.md` chips, only the accent differs); B04/B05
(mechanism, spec-not-judgment) clean; B07 (both-directions, paired
struck-through claims) clean; BCRY carries the carry-out line alone on the
Claude fidelity card with the humanitarians terracotta asterisk; BHTF (Your
Turn) shows the full paste-ready prompt on the composer card,
@HumanitariansAI folder tag; BOUT carries the Humanitarians AI skin (title
restate, Subscribe CTA, @HumanitariansAI handle). No overlap, no
off-canvas text, no legibility issues found.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **-24.1 dB**, max_volume -2.8 dB — comfortably clears the
-40 dB floor.

**Master vs. beat_sheet.json:** master mtime (10:00:55) is newer than
beat_sheet.json's last content edit (09:58:43 — the B00 prop retune, made
BEFORE the B00 re-render and recompile). beat_sheet.json was not touched
after this point, per the "never touch beat_sheet.json after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field), which resolves to
**"Claude Basics."** Not the bare "Claude."

**Status: DONE (review cut).** `claude-for-legal--claude-liam-investigation-open.mp4`
passes every gate (content-check, frame-check, lane-check, GATE AUDIO,
GATE T, Gate V by eye). Wrote
`claude-for-legal--claude-liam-investigation-open.md` (YouTube description,
@HumanitariansAI, playlist "Claude Basics", direct code link, AI
disclosure). Source-fidelity gap logged above and in
QUESTION.md/SCRIPT.md/the description's "Deliberately not claimed" section.
Proceeding to Phase 4 (4K render + deliver.py).
