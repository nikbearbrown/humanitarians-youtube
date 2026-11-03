# BUILD-LOG — claude-for-legal--claude-liam-investigation-query

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-investigation-query/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `investigation-query`. Built entirely fresh this
invocation: only `SUBJECT.json` existed in the target reel dir on pickup.

**Source-fidelity blocker, and how it was handled:** the source's
beat_sheet.json never received its skill-specific "Claude's job: ___" fill —
the literal placeholder `>` survives verbatim in two beats (B03, BHTF),
matching the identical unfilled-`>` bug already documented on the
`claude-for-legal--claude-liam-case-brief`, `-hiring-review`, `-internal-
investigation`, `-investigation-add`, and `-investigation-open` sibling
redos. The SKILL.md investigation-query was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/employment-legal/skills/investigation-query/SKILL.md`) does not exist
on this machine (confirmed: only `youtube/` exists locally under
`anthropics/claude-for-legal/`; no `employment-legal/` directory). Not a
build-halting blocker per the completion law: the source DOES establish
real, generic, true facts about how a Claude skill works, and one genuine
fact fragment survived intact in both B00 and BVDT — "Ask questions against
an open investigation log — what witnesses said,". This redo keeps that
fragment as the only investigation-query-specific claim and otherwise
treats the name as a generic anchor example. Full account in QUESTION.md
and SCRIPT.md.

**Beat-count note:** source is 7 beats; result here is B00 + 7 body beats
(B01-B07) + BCRY/BHTF/BOUT = 11 beats — the same proportionate expansion
pattern as the sibling redos, to satisfy hai-simple's mandatory six-move
spine (WRONG-GUESS / ANCHOR / BOTH-DIRECTIONS each need their own beat).

**B00 WRITER LAW / TIMING LAW:** narration is 30 words ("You'd guess Claude
works out what really happened once it picks up a skill called
investigation-query. It doesn't — it searches the investigation log. Let's
see what's inside that file."), measured 10.35s, plus `lead_silence_s: 0.8`.
Reused the exact `BrutalistHesitantWriter` prop values validated on the
`investigation-open` sibling's timing-bug fix (`mistakeRate:2,
hesitateWithin:1, hesitateBetween:6, charMs:34, jitter:20`) rather than the
component's higher-friction defaults, since those defaults were already
proven to overrun an 11-13s clip on that sibling. Rendered clip: 10.37s.
Verified via extracted frames: "investigates" types in accent (terracotta)
color and is visibly deleted/corrected to "queries" between t=1.3s and
t=2.5s; full 4-line corrected text — ending on "What is a skill?" — is on
screen and holding from roughly t=3s through the clip's end at t=10.37s.
Both the WRITER LAW correction and the "end ON the question" requirement
are met.

**Audio:** `generate_audio_kokoro.py` generated all 11 beats in one pass,
$0.00 cost, durations written back as ground truth.

**Graphics:** all 7 GRAPHIC beats (B01-B07) rendered via a per-reel
`scenes.py`/`render_scenes.py` pair adapted from the `investigation-open`
sibling's generic parametrized chip-row/chip-stack renderer — only the
`BEAT_CONTENT` dict content changed (investigation-query-specific labels:
"SOUNDS LIKE FACT-FINDING AUTHORITY", "investigation-query/" + "SKILL.md"
anchor chips, "FOUND IT IN THE LOG" / "CAME UP EMPTY" both-directions
pairs). All 7 rendered clean on first pass, no re-renders needed.

**Remotion beats:** B00, BCRY, BHTF, BOUT all rendered clean via
`remotion_scenes.py` in the foreground, one pass, no `--only`/`--force`
needed.

**Compile:** `compile.py` produced a clean 3840x2160 master directly (no
declared slates — all 11 beats real media):
`claude-for-legal--claude-liam-investigation-query.mp4`, 128.7s.
content-check, frame-check, and lane-check all PASS. One non-blocking
WARNING: GRAPHIC beats are 7/11 (63%), over the ~40% pantry-cap
motion-diversity guidance (MOTION.md) — noted, not a gate; this reel is
legitimately diagram-heavy (a skill's anatomy/mechanism/spec argument reads
naturally as labeled-chip diagrams) and every GRAPHIC beat is original,
locally-rendered Manim.

**GATE T:** ran `type_check.py` after compiling (render -> compile ->
type_check order, per `simple`'s documented Step 5). Result: **PASS, 0
FAILs** on first pass across all 11 beats — no exemption additions needed.

**Gate V (visual QC):** pulled one frame every 6s across the full 128.7s
master (21 frames) plus targeted frames for B00's typing/correction moment
and BOUT's final card, and read each by hand. B00's "investigates"->"queries"
correction and finished-question hold confirmed legible; B01/B02
(stakes, wrong-guess-broken) legible with correct accent/strike marks;
B03/B06 anchor pair visually identical (`investigation-query/` + `SKILL.md`
chips, only the accent differs); B04/B05 (mechanism, spec-not-judgment)
clean; B07 (both-directions, paired struck-through claims in vertical
stack) clean; BCRY carries the carry-out line alone on the Claude fidelity
card with the humanitarians terracotta asterisk sparkline; BHTF (Your Turn)
shows the full paste-ready prompt on the composer card, @HumanitariansAI
folder tag; BOUT carries the Humanitarians AI skin (title restate,
Subscribe CTA, @HumanitariansAI handle). No overlap, no off-canvas text, no
legibility issues found.

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **-24.0 dB**, max_volume -2.8 dB — comfortably clears the
-40 dB floor. (GATE AUDIO inside compile.py independently reported the
same -24.0 dB.)

**Master vs. beat_sheet.json:** master mtime (10:21:44) is newer than
beat_sheet.json's last content edit (10:19:15 — the audio-generation
write-back, made before the Remotion render and compile). beat_sheet.json
was not touched after this point, per the "never touch beat_sheet.json
after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field), which resolves
to **"Claude Basics."** Not the bare "Claude."

**Delivery:** `claude-for-legal--claude-liam-investigation-query-4k.mp4`
created — a copy of the compiled master, which was already genuine
3840x2160 (Remotion beats natively 4K; Manim beats upscaled into the 4K
canvas by compile.py itself). Ran `deliver.py --push`: staged
`DELIVERY/claude-for-legal--claude-liam-investigation-query/` (4K master +
description) for the Drive sync, and committed the text artifacts
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-investigation-query/`,
commit `fe924d49`, pushed.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Delivered to both targets.
Source-fidelity gap logged above and in QUESTION.md/SCRIPT.md/the
description's "Deliberately not claimed" section — nothing about the actual
employment-legal investigation-query procedure is asserted anywhere in this
reel.
