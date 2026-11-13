# Frictional log — Context Window Limits: The Budget That Doesn't Grow

*Written contemporaneously, as the build happens — not reconstructed after the fact.*

## 2026-11-12/13 — Start

Read both reference STEM reels in full as the structural template —
`2026-11-04-goodharts-law-proxy-metrics/` (closest structural match: `README.md`,
`BEAT-SHEET.md`, `BUILD-LOG.md`, `FRICTIONAL.md`, `FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`,
`PROMPTS.md`, `scenes.py` + `vertical/scenes.py`, `beat_sheet.json` + `vertical/beat_sheet.json`)
and `2026-10-28-in-context-learning-limits/` (second reference, same format, and the video this
one is most easily confused with) — plus the toolkit's `CLAUDE.md`, `art`, `runtime/scripts/
run.sh`, `runtime/scripts/compile.py`, `runtime/scripts/shorts.py`,
`runtime/scripts/generate_audio_kokoro.py`, `runtime/qc/final_frame_check.py`,
`runtime/qc/manim_layout_audit.py`, `runtime/scripts/build_safety.py`, and
`docs/FELLOWS-SUBMISSION.md` directly (not just the sibling reels' secondhand description of them)
to confirm exactly how `./art run` / `./art final` / `./art vertical` actually work end to end.
Confirmed directly in source: `compile.py`'s embedded GATE V call (`final_preflight` ->
`require_paperwork` -> the Gate V subprocess call at the end of `compile_reel`) genuinely has no
`--lenient` flag anywhere in its own argparse and never reads `ART_STRICT`, so `./art final` is
always Gate-V-strict; `require_paperwork` hard-requires `FACTCHECK.md`/`SHOTLIST.md`/`PROMPTS.md`
non-empty with no bypass. Confirmed `run.sh`'s Manim render step hardcodes `-r 3840,2160` (or
`2160,3840` when the beat sheet declares `aspect_ratio: "9:16"`) regardless of the `--height` flag
passed to `run.sh`/`art run` itself — that flag only controls the later `compile.py` review-cut
encode resolution, not the Manim source resolution. Confirmed `T()`/`PALETTE` are NOT centrally
defined anywhere in the toolkit (grepped the whole repo) — they're a per-project convention this
fellow's sibling reels established and that this project copies forward verbatim.

Topic: context window limits (the capacity ceiling itself — token budget, overflow behavior —
distinct from the already-covered in-context-learning-limits video, which is about ICL as a
*mechanism*). Read `2026-10-28-in-context-learning-limits/README.md`, `BEAT-SHEET.md`,
`FACTCHECK.md`, `SOURCES.md` specifically to confirm no overlap: that video's rubric is "Spot the
Mapping / Shuffle the Set / Push Past the Window," its worked example is a toy Caesar-shift cipher
taught via 4 example pairs, and its only mention of "context window" is one structural,
one-sentence boundary condition on ICL's own rubric ("in-context learning is bounded by the
model's context window — information that doesn't fit cannot be used, no matter how many examples
are added"). None of that rubric name, cipher example, or tag ("LOCATED, NOT LEARNED" /
"MISMATCH") is reused here. Devised this video's own rubric instead, mirroring the series' prior
falsifiable-rubric pattern (Goodhart's "Name the Target / Find the Lever / Watch the Coupling,"
ICL's "Spot the Mapping / Shuffle the Set / Push Past the Window") without reusing any of their
wording: **"Count the Tokens / Share the Pool / Watch the Edge."** Worked example: a fully
invented, illustrative 1,000-token budget shared by fixed instructions, a pasted-in document, and
a growing conversation history, with the oldest turns silently dropped once the budget is
exceeded — no real model/vendor named, no real context-window size cited as a universal fact (per
the house rule — context windows vary enormously across systems and change over time).
Falsifiability case: per the build brief's explicit requirement that this show a case where going
over budget does NOT cause a silent problem, made it structurally identical to B04 (same budget,
same numbers, same overflow condition), changing only whether the system checks the total before
answering — the single variable the rubric's own test (#3, Watch the Edge) actually names.

Confirmed via direct read of `build_safety.py`'s `is_fellows()` that this project's planned
`voice_policy` string ("Bella (af_bella) — persistent voice for this fellow's whole series.
Unchanged for this episode.") does NOT equal the exact trigger string `"persistent-fellow-
selected"`, matching both reference projects' beat sheets exactly — so no `metadata.approvals`
block is required for `compile.py --review`/`--final` to proceed, confirmed by reading
`build_safety.py` directly rather than assuming it from the reference beat sheets' absence of an
`approvals` key.

Planned the build order per both references' documented lesson set: beat sheet → Kokoro audio
(measure real durations) → `scenes.py` tuned to those exact durations → render/QC landscape →
`./art vertical` scaffold → hand-author `vertical/scenes.py` → render/QC vertical → final-master
build for both aspects via `./art final --out deliverables/<aspect>`, with the documented manual
`ffmpeg -f concat` + standalone `final_frame_check.py --lenient` workaround held in reserve only if
the embedded GATE V step crashes or refuses unexpectedly → GATE V direct verification on the true
final candidates, plus real-frame extraction (not just the automated gates) before calling
anything done. Pre-applied several already-documented fixes from the start rather than
re-discovering them: `T()` safe-text helper for every on-screen string, `metric_panel()`'s return
contract indexed directly as `content[1]` (no extra index — the exact bug the Goodhart's reel's
`BUILD-LOG.md` documents in its own `metric_panel()`), front-loaded B02 pre-transition waits (the
exact empty-frame GATE V bug prior reels hit), and 0.5-unit edge buffs on all structure-beat
framing rules (the exact edge-bleed GATE V bug prior reels' vertical builds hit).

Wrote `BEAT-SHEET.md`, `FACTCHECK.md`, `SOURCES.md`, `PROMPTS.md`, and a draft `SHOTLIST.md`
(durations left as TBD pending measured audio, per the audio-first rule — never guessed) and
`beat_sheet.json` (9 beats, same act structure as both references:
TITLE/EXEC-SUMMARY/HOOK/FRAMEWORK/WORKED-EXAMPLE/FALSIFIABILITY/SCAFFOLDED-TASK/TAKEAWAY/SIGN-OFF).
Next: generate the real silent B00 track and run Kokoro for the 8 spoken beats, measure every
duration via `ffprobe`, and only then write `scenes.py`'s per-beat timing.

## 2026-11-13 — Audio, scenes.py, first GATE B failures (both self-caused, both real)

Built the real silent B00 mp3 by hand (`ffmpeg -f lavfi -i anullsrc=r=48000:cl=stereo -t 4.1`),
measured via `ffprobe` at 4.128s (matches the Goodhart's reel's B00 exactly — same mp3
frame-boundary rounding behavior, not a coincidence of content). Ran
`generate_audio_kokoro.py --only B01 B02 B03 B04 B05 B06 B07 B08` (`af_bella`) in one pass, no
retries needed: B01=16.49 B02=22.61 B03=34.10 B04=31.75 B05=24.79 B06=28.13 B07=14.16 B08=1.51.
`generate_audio_kokoro.py` skips B00 entirely as "intentional silence" and does NOT write its
`actual_duration_s`/`audio_file` back (unlike the 8 spoken beats) — hand-set both fields on B00
afterward using the real measured 4.128s, matching the audio-first rule: measure, don't assume,
and don't rely on a tool to do it for a beat it explicitly skips. Total measured runtime:
4.128+16.49+22.61+34.10+31.75+24.79+28.13+14.16+1.51 = 177.668s.

Wrote `scenes.py` with the established `T()`/`PALETTE`/`fit()`/`panel()`/`box_around()`/
`stat_row()`/`metric_panel()` helpers copied verbatim from the Goodhart's reel, hand-summed every
beat's `self.play`/`self.wait` durations to match each measured `actual_duration_s` exactly up
front (reusing the Goodhart's reel's exact per-beat play-time allocations where the beat's
narrative shape was similar enough, and only changing the final `self.wait()` remainder).

First `./art run --height 480` pass: GATE A and GATE W clean on all 9 beats first attempt. GATE B
(pixel-true layout audit) caught a REAL bug on B02 — not a false positive: `correct_tag` ("NOT
WORDS EITHER"), positioned via `next_to(trend_block, RIGHT, buff=2.9)`, landed partly outside the
safe area (box x up to 7.04 against a ±6.3 safe half-width). This is a genuinely different root
cause from the sibling reels' documented B05 overlap bug (element-on-element overlap, invisible to
bbox checks) — this one WAS a plain off-safe-area bbox violation, exactly the class GATE B is
built to catch, and it caught it correctly on the first try.

First fix attempt was wrong and made it WORSE: tried chaining `looks_good` and `correct_tag`
further RIGHT off each other with smaller buffs (0.45, 0.4) instead of fixing the real problem
(an off-center multi-element row with nothing to re-center it) — re-ran GATE B and the SAME tag
now came back as a hard ERROR (off-FRAME, not just off-safe-area: box x up to 7.54 against the
hard frame edge at 7.11 for a 14.222-wide 16:9 frame), because chaining three short, independently
left-aligned-by-`next_to` text pieces rightward off an already-centered anchor accumulates
rightward drift with nothing pulling the row back toward center — the width of each new tag adds
to the drift instead of being absorbed into a centered group. Lesson logged: `next_to(X, RIGHT,
buff=N)` chained across 3+ short text mobjects is NOT self-centering, even when the first anchor
(`trend_block`) was itself centered at x=0 — only grouping all pieces into one `VGroup` *before*
positioning, or stacking `DOWN` instead of chaining `RIGHT`, keeps every piece centered.

Real fix: restructured the two trailing tags to stack `DOWN` off `trend_block` (each
`next_to(..., DOWN, buff=...)` individually, so each one centers independently at x=0, matching
the pattern `box_around`/structure-card beats already use elsewhere in this file) instead of
chaining sideways. Re-ran `./art run --height 480`: GATE A/W clean, GATE B clean, B02 rendered and
slotted. No stale-cache issue hit this time (each re-render used a genuinely different scene
source hash, so Manim's own cache correctly treated it as a new render rather than reusing a
partial-movie-file fragment from the broken version).

Remaining 7 beats (B03-B08) rendered clean on the first attempt — GATE A/B/W clean on all, no
further fixes needed. Confirmed via `ffprobe` that every `manim/B0N.mp4` was already true native
3840x2160 despite the `--height 480` flag, matching both sibling reels' documented finding. The
review slate's GATE V came back at exactly **18 BLOCKER / 0 MAJOR** — the documented burn-in
false-positive pattern (2 per beat x 9 beats) from the review cut's own global-timecode overlay,
not a real defect. Per the documented workaround, this was NOT trusted at face value; proceeded to
build and independently verify the TRUE final candidate before accepting anything as clean (see
below).

## 2026-11-13 — Landscape final master, verified independently and by real frame extraction

Built the TRUE final landscape master directly (`./art final <reel> --out deliverables/landscape`,
no `--review`): succeeded on the first attempt with no BuildError, meaning `compile.py`'s own
embedded GATE V step (no `--lenient`) found nothing blocking. Re-ran `final_frame_check.py
--lenient` directly against the written candidate as an independent confirmation (never trusting
the embedded step's silent success alone): **0 BLOCKER, 0 MAJOR**. `ffprobe`: 3840x2160, 24fps,
h264/aac, 177.625s. Renamed `<slug>.mp4`/`.verified.json` to `ContextWindowLimits_SaiPranaviJ.mp4`/
`.verified.json` per `FELLOWS-SUBMISSION.md`'s manual naming convention — confirmed `compile.py`
itself only ever writes the slug-named file; the `ProjectName_VolunteerName.mp4` rename is always
a manual step after the fact, exactly as both reference reels' actual `deliverables/` contents
show (no slug-named file survives in either reference project's `deliverables/` folders either).

Extracted and personally inspected real frames (not just the automated gate) at B02 (both the
panel-content phase at t=25.5s and the overlay phase at t=30.5s/40.5s), B03 (t=55s), B04 (t=87.25s
and t=97.25s), B05 (t=119s and t=127s, two separate timestamps to confirm steady-state stability),
and B06 (t=150s, caught mid-animation on the third checkbox by chance — a reminder that an
arbitrarily-chosen extraction timestamp can land mid-transition; not treated as a defect since
GATE V's own beat-aware steady-state sampling, not an arbitrary manual timestamp, is the real
measure, and that sampling already came back clean). All content frames: budget panels fully
legible, TRUNCATED/CAUGHT tags sit clear of their panels with no overlap (the B05-style tag-overlap
bug both sibling reels hit never reproduced here, since this file placed tags below their panels
from the start, matching the already-fixed pattern), no off-frame/off-safe-area content, no Pango
small-font-size word-gap artifacts anywhere.

## 2026-11-13 — Vertical scaffold and hand-authored portrait scenes

Ran `./art vertical <reel> --no-endcard --handle "@HumanitariansAI"`: confirmed it copies the
parent's 9 mp3s and beat-sheet metadata (`aspect_ratio: "9:16"`, `kind: "vertical"`,
`fit: "pad"`) into `vertical/`, correctly reports every beat as `GENERATED -- no cut; needs a
portrait scene` (the documented contract for Manim/non-Remotion beats — it never silently
center-crops a generated graphic), and correctly did NOT add a silent endcard (confirmed by the
explicit `--no-endcard` flag; `shorts.py`'s default behavior adds one even under `--vertical`,
and its default `--handle` is `@nikbearbrown`, so both flags were passed explicitly from the
start rather than discovered as a bug after the fact). `vertical/FACTCHECK.md`/`SHOTLIST.md`/
`PROMPTS.md` were copied automatically, satisfying GATE F for the vertical sub-reel without any
manual copying.

Hand-authored `vertical/scenes.py`: same `T()`/`PALETTE`/`fit()`/`panel()`/`box_around()` helpers
copied verbatim, `stat_row()`/`metric_panel()` redesigned to stack label-over-value instead of
label-beside-value (the narrow ~4.5-unit portrait frame can't fit a long label and a value on one
line), and every structure beat's trailing tags (B02's "NOT CHARACTERS"/"NOT WORDS EITHER", B04/
B05's TRUNCATED/CAUGHT tags) built stacked DOWN from the start -- the exact safer pattern the
landscape file's B02 only reached after a real bug (see above), applied here preemptively rather
than re-discovered. Every `self.play`/`self.wait` duration hand-matched to `../scenes.py` beat-for-
beat by construction (not verified via a separate regex cross-check script this time, since every
beat's timing comments were copied and re-summed by hand directly from the landscape file while
authoring, beat by beat, rather than written independently and reconciled after).

First vertical QC pass (`./art run vertical --height 480`) hit the exact documented GATE A false
positive on the first pending beat it reached: B04 failed static pre-flight with "1 explicit
coord(s) outside the frame, e.g. (0.0,-4.4) in move_to." Grepped `vertical/scenes.py` for any
literal `move_to([...])` call and found none anywhere in the file -- every `move_to()` call in
this file takes a dynamic `.get_center()` or `ORIGIN`, confirming this is the exact documented
stub-vs-real-Manim divergence class of false positive (the static checker's render-free stub
doesn't correctly apply this file's portrait `config.frame_height`/`frame_width` patch, so it
mis-evaluates where a dynamic `.get_center()` call actually lands). Independently verified via the
real pixel-true `manim_layout_audit.py --portrait` run directly against a fresh scratch copy of
the file (copied to `/tmp/cwl_vertical_scratch/`, never the reel's own `vertical/media/videos/`
tree, per the documented stale-cache-contamination lesson) for EVERY one of the 9 beats, not just
B04: B04 came back CLEAN, but this full sweep caught two REAL warnings neither reference reel's
BUILD-LOG specifically flagged for this project's own content -- B04's title ("A budget, under")
and closing line ("Nobody saw what left.") both measured 0.1 unit outside the portrait safe area
(`±3.4` y half-extent) at `to_edge(UP/DOWN, buff=0.5)`, because this portrait frame's safe
half-height (3.4) is tighter than the landscape frame's (3.6) that the `buff=0.5` convention was
originally tuned against -- copying a landscape buff value verbatim into a portrait file is NOT
automatically safe, even though both files share the same `frame_height=8`. Fixed by raising every
`to_edge(UP/DOWN, buff=0.5)` text-block margin to `0.7` (and the paired rule-line margins from
0.35 to 0.55) across all 6 beats that used this pattern (B02-B06, plus B00's handle line), computed
from the portrait auditor's own reported safe half-height (4.0 - 0.7 = 3.3, inside the 3.4 safe
bound) rather than guessed. Re-ran the real portrait auditor against all 9 beats again: all 9
CLEAN, 0 errors, 0 warnings.

Proceeded past GATE A for the vertical render using the documented `ART_QC=0` escape hatch, with
every one of the 9 beats already independently re-verified via the real portrait auditor BEFORE
rendering (not just trusted from the escape hatch after the fact) -- an improvement on the
sequencing both reference reels describe (auditor-after-escape-hatch), since the two real edge-
overflow warnings were caught and fixed before spending a render cycle on them.

## 2026-11-13 — A real GATE V underfill/edge-bleed cycle on the vertical candidate, and a
## self-caused false signal from checking the wrong resolution

`./art final <reel>/vertical --height 3840 --out deliverables/vertical` REFUSED on the first
attempt with a genuine (not false-positive) GATE V failure: 0 BLOCKER, 6 MAJOR, all `underfill` --
B02 (44% of the safe area, min 55%), B03 (54%), B06 (47%), B08 (34%, the worst). Confirmed via
direct re-run of `final_frame_check.py` against a manually-reconstructed candidate
(`ffmpeg -f concat` on `clips/concat.txt` + `clips/_work/master.wav`) that this was real, not a
burn-in artifact (no `--review` label on this path). Root cause: this portrait file's B02/B03/B06/
B08 content was sized too close to the landscape file's own proportions, leaving real, visible
negative space in the much taller 9:16 frame -- a genuinely different failure mode from the two
GATE B edge-overflow warnings already caught and fixed during authoring (those were about content
going OUTSIDE the safe bounds; this is about content not filling ENOUGH of them). Fixed each beat
with genuine added content mass -- larger real text, wider real rule lines, and more real spacing
between real elements -- never a padding rectangle, per the house rule.

The B08 fix round-tripped twice: the first attempt (bigger fonts, a wider accent rule, a larger
frame cap) fixed the 34% underfill but introduced a NEW real defect -- 2 BLOCKER `edge-bleed` (the
enlarged frame's own half-width, 2.05, exceeded the portrait safe half-width, 1.95, by 0.1) plus
the underfill only partially recovering (51%, still under the 55% floor). Re-extracted a real
frame and confirmed visually: the `@HumanitariansAI` handle and its bordering frame both ran right
up to the card edge. Second fix: capped the frame width more conservatively (half-width 1.85, a
real 0.1 inside margin) and recovered the fill ratio by stacking the two-line captions (
"explained with" / "Claude Code", "in for" / "Sai Pranavi J.") instead of fitting them on one
line each -- genuine added vertical content mass within a width that stays safely inside the
frame, rather than trying to win back area by going wider.

**A self-caused false signal, caught before it was wrongly blamed on real content:** after fixing
B08 a second time, re-ran the manual `ffmpeg -f concat` + `final_frame_check.py` workaround again
and got a NEW, different-looking failure: 0 BLOCKER, 6 MAJOR `low-contrast` on B01, B04, AND B08 --
beats B01 and B04 whose scene code was never touched in this entire session. Re-ran the identical
check against the identical manually-built candidate twice in a row and got the identical result
both times (ruling out nondeterministic video encoding as the cause), then re-ran the EXACT SAME
check against the very FIRST manual candidate built earlier in this session and got back that
original candidate's ORIGINAL report (6 MAJOR underfill, no contrast findings at all) --
confirming the checker itself is deterministic per file, so the underlying frames really had
changed. Diffed actual extracted PNGs at B01's and B04's sample timestamps between the two
manual-candidate builds with `PIL.ImageChops.difference()`: genuinely different pixels, and both
were a suspiciously small 270x480 -- not the expected 2160x3840. Root cause: `clips/manifest.json`
confirmed every clip was cached at `270x480@24`, the review-pass resolution from an EARLIER
`ART_QC=0 ./art run <reel>/vertical --height 480` call made solely to re-render the single changed
B08 Manim scene -- that call's own internal `compile.py --review --height 480` step recompiles
EVERY beat's clip at that review height as a side effect, silently downgrading all 9 clips
(including B01/B04, never touched) back to low-resolution preview quality in the shared `clips/`
cache. My own manual `ffmpeg -f concat` workaround then unknowingly reconstructed a candidate from
those stale low-res clips instead of true 4K ones -- and at 270x480, several beats' anti-aliased
text blends measurably closer to the background color than at true resolution, producing a
genuinely different (and spurious) contrast reading, not a real defect in the content. Lesson
logged: **the manual `ffmpeg -f concat` GATE V workaround is only trustworthy immediately after a
`./art final --height <true>` pass actually recompiles `clips/` at true resolution** -- any
subsequent `./art run --height <preview>` call (even one scoped to re-rendering a single Manim
beat) silently reverts the ENTIRE shared `clips/` cache to preview resolution as a side effect, and
a manual reconstruction built after that point is checking the wrong material, even though the
underlying `manim/B0N.mp4` source files it's downstream of remain true 4K throughout. Resolution:
stopped hand-reconstructing from `clips/concat.txt` and instead re-ran the real `./art final`
command directly, letting it recompile `clips/` at the correct height itself before its own
embedded (always-strict) GATE V check runs against genuinely true-resolution material.

## 2026-11-13 — Both masters done, both independently verified by gate and by eye

The clean re-run of `./art final <reel>/vertical --height 3840 --out deliverables/vertical`
succeeded on the first attempt with no `BuildError` — meaning the embedded, always-strict GATE V
step found nothing blocking against genuinely true-4K-resolution clips this time. Independently
re-ran `final_frame_check.py --lenient` directly against the written deliverable (never trusting
the embedded step's silent success alone): **0 BLOCKER, 0 MAJOR.** `ffprobe`: 2160x3840, 24fps,
h264/aac, 177.625s — identical to the millisecond to the landscape master's duration. Renamed
`<slug>-vertical.mp4`/`.verified.json` to `ContextWindowLimits_SaiPranaviJ.mp4`/`.verified.json`.

Extracted and personally inspected real frames from the TRUE vertical deliverable (not the manual
reconstruction used mid-build for diagnosis) at B02's overlay phase, B04, B05 (at a genuine
steady-state timestamp, after first grabbing an early transition frame by mistake and correctly
not treating a 0.5s-into-the-beat title-write frame as a steady-state defect), B03, B06, and B08.
All clean: budget panels fully legible, no overlap, no off-frame/off-safe-area content, every
underfill-fixed beat now visibly filling the tall portrait frame rather than leaving it sparse,
mechanism legible in both B04 (TRUNCATED — SILENTLY) and B05 (CAUGHT IMMEDIATELY), and the fixed
B08 sign-off card now actually fills its card rather than floating in a mostly-empty frame.

Both final deliverables confirmed: `deliverables/landscape/ContextWindowLimits_SaiPranaviJ.mp4`
(3840x2160, 24fps, h264/aac, 177.625s, GATE V 0/0) and
`deliverables/vertical/ContextWindowLimits_SaiPranaviJ.mp4` (2160x3840, 24fps, h264/aac, 177.625s,
GATE V 0/0) — durations identical to the millisecond, both independently re-verified against the
TRUE final candidates (never the review slate), both with real extracted frames personally
inspected rather than trusted from the automated gates alone. Nothing inside `brutalist/` was
modified; publishing not authorized, per `FELLOWS-SUBMISSION.md`.

Overall lesson for this build, worth carrying into the next one: this reel's two genuinely novel
bug classes (the chained-RIGHT text-drift off-frame bug in landscape B02, and the shared `clips/`
cache silently reverting to preview resolution after an unrelated beat's re-render in vertical)
were NOT pre-documented by either sibling reel's BUILD-LOG/FRICTIONAL.md — both were found the
same way the brief insisted on: by not trusting an automated result that looked plausible (a
GATE B pass, a GATE V contrast failure) without tracing it back to a concrete, reproducible cause.

## 2026-11-13 — A third self-caused bug found only while writing this log, after the build:
## B00's documented 4.128s silent duration was never actually used by the pipeline

While reconfirming `beat_sheet.json` for this log's final numbers, `grep` showed B00's
`actual_duration_s` as `4.0`, not the `4.128` this project's `BEAT-SHEET.md`/`BUILD-LOG.md` had
been claiming since early in the build. Root cause, reconstructed from the actual edit order:
`generate_audio_kokoro.py --only B01...B08` was run BEFORE the B00 silent-duration edit, and that
tool — even though it prints "B00 SKIPPED" — still writes `actual_duration_s: 4` (the
`estimated_duration_s` fallback) back into B00's own beat object as a matter of course, so every
downstream consumer always has a number. The subsequent `Edit` call that was meant to set B00's
REAL measured value (4.128, from `ffprobe` on the real silent mp3) anchored its insertion point
right after the beat's `shot` block — the exact same location Kokoro's own writer had already used
for its `actual_duration_s: 4` — so the edit inserted a SECOND `"actual_duration_s"` key into the
same JSON object rather than replacing the first. Valid JSON parsers (including Python's) resolve
duplicate object keys by keeping the LAST one — and the Kokoro-written `4` sat textually AFTER my
inserted `4.128`, so it silently won every single time the file was loaded and re-saved by any
later tool in this build (`compile.py`'s own stamp-back included), with no parser error and no
warning at any point, including repeated manual inspections of SPECIFIC KEYS via `python3 -c
"json.load(...).get('actual_duration_s')"` — which is exactly why this escaped notice until now:
checking a parsed VALUE can't reveal that its SOURCE file held two conflicting raw key occurrences.

Checked what this actually did to the delivered masters: `manim/B00.mp4` genuinely renders
4.128s (scenes.py's own play/wait sum), and every build log line
(`"[art] B00: clip 4.2s center-cut to 4.0s (skip 0.1s head/tail)"`) shows `compile.py` center-
cutting that real 4.128s render down to the pipeline's `render_duration_s` of exactly `4.0s` — a
real, if practically harmless, 0.128s trim off a SILENT title card whose on-screen content
(title + handle) finishes animating and holds static well inside the first 1.6s of play time, so
no visible content was cut, only 0.128s trimmed from an already-long static hold. This happened
consistently on every single build in this session (the very first `./art run`, before any of the
later content bugs, already shows this same center-cut line), so it did not cause any of the
other defects found and fixed above — it is a separate, narrower, purely-bookkeeping-plus-0.128s-
of-silent-hold issue, not a visible defect, and both final deliverables' GATE V results (0
BLOCKER/0 MAJOR, confirmed by direct re-check) are unaffected by it. Corrected `BEAT-SHEET.md`'s
claimed raw runtime (4.128+...=177.668s) to the figure the pipeline actually used throughout
(4.0+...=177.54s) rather than silently leaving the inaccurate number standing. Lesson logged for
future builds: when hand-editing a beat's duration field after an engine has already written its
own default for that same beat, use `Edit`'s exact-match requirement against the CURRENT
post-generation file content (re-`Read` first), not against a draft anchor written before the
generation step ran — and a parsed-value spot-check is not sufficient to catch a duplicate-key
JSON bug; only a raw-text `grep` for the key would have caught it earlier.
