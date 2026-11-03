# PROOF REVIEW — *Same Room, Different Argument* (working title)

Living document, one entry per build stage, per Tanmay's request to run this at every
stage rather than once at the end. Scored against the actual produced artifact, not
against intentions — same standard as Week 22's `PROOF-REVIEW.md`.

## CURRENT STATUS (read this first — the reviews below are a history, not a menu)

**This film (the long): production gate 12/12** (Review 10, re-confirmed twice since,
most recently Review 12). **Gate P: signed PASS**, Tanmay Kulkarni, 2026-09-20 (draft 4
— see `PEDAGOGY.md`). **Gate V: 0 BLOCKER / 0 MAJOR** on the delivered final master.

The **9/12** score appearing further down is **Review 7's result on an earlier draft**,
before the rubric-driven revision (Review 9) and the re-score that followed it
(Review 10). Kept in place as the record of what changed and why, not as the current
state.

**The Short (`short/`) is scored on its own, different rubric — not this film's 12
points.** A trailer isn't trying to teach a complete method, so grading it against
"reusable rubric" / "active task" would be a category error. Its own Trailer Gate score
(12/12 on 6 different criteria) lives in `short/SHORTS-BUILD-LOG.md`. Both formats are
independently verified and both currently PASS — see Review 12 for the joint sign-off.

---

## Review 1 — audio generation (Kokoro, draft 3)

**Stage:** first real build artifact. 18 beats, `am_onyx`, generated via
`brutalist.art/runtime/scripts/generate_audio_kokoro.py` against the Gate-P-signed
`beat_sheet.json` (draft 3, PASS 2026-09-20). No visuals, no compiled cut yet — audio only.

| Check | Method | Result |
|---|---|---|
| All 18 beats produced | file listing | **PASS** — 18 non-empty mp3s in `mp3/`, no gaps |
| Duration ground truth agrees across both records | diffed `beat_sheet.json`'s `actual_duration_s` against `mp3/timings.json` per beat | **PASS** — 0 mismatches across 18 beats |
| No clipping | `ffmpeg -af volumedetect` per file | **PASS** — max_volume ranges −0.3 to −7.9 dB, all beats below 0 dBFS |
| No near-silent/failed synthesis | same volumedetect pass | **PASS** — mean_volume −21.5 to −24.6 dB across all 18, consistent with the toolkit's own smoke-test threshold (fail below −40 dB); no outlier beat |
| No dropped/cut-off audio | `ffmpeg -af silencedetect` spot-check on shortest (B00, B17) and longest (B02) beats, plus B12 (the beat with the trickiest quote/pseudonym) | **PASS** — no leading silence, mid-clip gaps land on natural sentence breaks, each beat ends with a normal 0.3-0.7s trailing tail, no anomalous long dead air |
| Approval gate honesty | ran `generate_audio_kokoro.py --dry-run` first, confirmed it resolves `validate_approvals` cleanly against our metadata (not fellows-wrapper-flagged, matching Week 22's own precedent — see `BEATS-DRAFT.md`) before running for real | **PASS** — no approval bypass, no fabricated JSON records |

**Not yet checkable at this stage** (same limitation Week 22's Review 1-4 noted for
motion/timing defects): no visuals exist, so nothing here confirms narration-to-image sync,
on-screen citations, or the corner-card/chrome concerns Week 22 eventually found. Those
need a previz pass first.

**Measured vs. planned runtime:** 316.69s (5:16.7) measured, vs. 346s (5:46) planned —
Kokoro read faster than the 3.0 words/sec planning estimate for this more conversational
register. Per-beat spread was small; no beat is wildly off its planned pace (largest gap:
B10, 22s planned → 17.9s measured).

**Verdict: PASS.** Audio is sound and ready for previz. Next stage (slates/stills) needed
art assets first — resolved in Review 2 below.

---

## Review 2 — asset sourcing for B03 and B06

Only two of eighteen beats needed a photographed asset (everything else is a
Remotion-coded concept/verdict card). Checked before building anything on top of them.

| Check | Method | Result |
|---|---|---|
| Searle photo exists and is rights-clear | searched Wikimedia Commons, read the file's own license page | **PASS** — `File:John searle2.jpg`, dual GFDL / CC BY-SA 3.0, photographer credited (Matthew Breindel), usable with attribution |
| Downloaded file matches the source record | `file` + byte size vs. Commons page (1,704×2,272, ~1.51MB) | **PASS** — exact resolution match, 1,585,833 bytes vs. stated 1.51MB |
| Provenance recorded before use, not after | wrote `pantry/searle-2005-oxford.provenance.md` alongside the file, before wiring it into `beat_sheet.json` | **PASS** |
| Harnad photo search was exhaustive, not assumed | checked Wikimedia Commons category (does not exist) and his English Wikipedia article directly (no image present) | **PASS** — absence confirmed, not assumed; recorded as a real gap, not silently worked around |
| No fabricated likeness used as a substitute | did not attempt AI image generation for a real, named academic without a source photo | **PASS** — B06 switched to the same concept-card format used elsewhere instead |

**Verdict: PASS.** Both beats now resolve to a real, sourced asset or a code-rendered card
— nothing in the visual plan depends on an image that doesn't exist or can't be verified.

---

## Review 3 — first full previz compile (18/18 filled)

**Stage:** all 17 Remotion scenes rendered (`remotion_scenes.py`, headless Chrome, ~1-1.5
min/beat), then compiled into a review cut (`compile.py --review --height 2160`).
`same-room-different-argument-slate.mp4`, 51.0 MB.

Tanmay raised a specific concern mid-render — the background must not be black — before
seeing any output. Checked explicitly, not assumed:

| Check | Method | Result |
|---|---|---|
| Background color, source-level | read `MedhavyConceptCard.tsx` / `ClaudeVerdictArtifact.tsx` directly | hardcoded cream (`#F2F0E9`, `CLAUDE.PAGE = '#FAF9F5'`) — "the app's cream, never pure white," per the design tokens' own comment |
| Background color, pixel-level, single frame | extracted a frame from completed B04, sampled corner + center pixels | corners `(241,240,233)` (cream), center `(254,254,254)` (white card) — matches the source-level claim on an actual rendered frame, not just code |
| Background color, whole-film | `ffmpeg blackdetect=d=0.5:pic_th=0.98:pix_th=0.10` across all 317s | **zero black segments detected anywhere in the cut** |
| Resolution | `ffprobe` | 3840×2160, 24fps — 4K, matches house convention |
| Duration | `ffprobe` | 317.08s video and audio, matches the 316.69s measured Kokoro sum within encoding rounding |
| Audio still intact after compile | `ffmpeg volumedetect` on the full mux | mean −27.3 dB, max −3.4 dB — no clipping, no silence failure |
| All slots actually filled | `compile.py`'s own slot report | 18/18 — B00-B02, B04-B17 as VIDEO (Remotion), B03 as STILL (the sourced photo) |
| Nothing rendered from a stale/fake approval | same as Review 1 — no `metadata.approvals` fabricated | **PASS**, unchanged |

**One flag carried forward, not fixed yet:** `compile.py`'s own skin lint: *"B01: composer
beat has an empty spark line — SPARK-LINE LAW wants a short serif cue."* This is a real
house-style convention this project hasn't satisfied — B01 is the cold-open HOOK beat and
currently has no short serif "spark line" caption the `ClaudeComposerAsk` pattern expects.
Not blocking (compile succeeded, the beat renders), but worth deciding on before a final
cut: either author a spark line for B01 or confirm the HOOK act is meant to be an
exception.

**Not yet checked** (needs an actual watch-through, not automated tooling): whether each
citation/quote card is legible at the moment the narration asserts it (Week 22's Review 1
found exactly this class of defect — evidence arriving after the claim was already spoken
— and it was invisible to every check before a timed sampling pass). That's the next
review once Tanmay has watched the cut himself.

**Verdict: PASS** on everything mechanically checkable at this stage. The black-background
concern is closed with evidence, not reassurance.

**This verdict was wrong in one critical way, caught in Review 4.** Every check above was
mechanical — resolution, black frames, audio levels, slot counts — and none of them read
the actual words drawn on screen. This is exactly the failure mode Week 22's own
`PROOF-REVIEW.md` Review 8 describes: "the production gate asks whether evidence is
legible and sourced... it does not ask whether everything on the frame is meant for the
viewer at all." Same gap, same project family, repeated.

---

## Review 4 — Tanmay caught what Review 3 missed: wrong content on every graphic card

**What was wrong:** every one of the 16 "GRAPHIC" beats (everything except B03's photo)
had only a `props_note` comment in `beat_sheet.json`, never an actual `props` object.
`remotion_scenes.py` passes `rem.get('props', {})` — an empty dict when none exists — so
every component rendered its own internal placeholder defaults instead of our content.
Confirmed by extracting real frames from B00 and B01: both showed "CLAUDE CODE · MANIM /
Photoelectric Effect / Hola, Bear / cl [typing] / @NikBearBrown / Fable 5" — a leftover
demo from an unrelated project, not anything in our beat sheet.

**A second, structural defect underneath it:** B17's outro used `ClaudeTitleOutro`, which
is not just defaulting — its own source comment states the handle `'@NikBearBrown'` is
"HARDCODED — no prop, no lookup, no override... Other channels (HAI, Medhavy, Musinique)
use their own outro components — never this one." No amount of props would have fixed
that beat; it was the wrong component from the start.

**Also caught:** B00 ("This is Humanitarians.") was never in Week 22's actual structure —
checked and confirmed Week 22 has no equivalent beat at all; it opens directly on its cold
open, then states the presenter's name. B00 was cut entirely rather than fixed.

**Root-cause check — why Review 3 missed this:** the review checked background color,
black frames, resolution, audio integrity, and slot-fill counts. It never extracted a
frame and read the text on it. That single missing step is now added permanently to this
project's review method, not just fixed this once — see the checklist below.

**Fix applied:**
1. B00 deleted from `beat_sheet.json`, its audio and stale render removed, `timings.json`
   cleaned of the orphaned entry.
2. Real, content-specific `props` written for all 16 remaining graphic beats, drawn from
   the same narration/FACTCHECK content already approved at Gate P — no new claims
   introduced, only the on-screen text that should have existed the first time.
3. B17 switched from `ClaudeTitleOutro` (locked) to `OutroCTA` — checked its full source
   for any hardcoded brand string (none found) before reusing it — with
   `line: "Same Room, Different Argument"`, `handle: "@HumanitariansAI"`.
4. All 16 beats re-rendered with `--force`; recompiling next.

**New permanent check, added to this review's method:** every future previz/compile pass
must extract at least one frame per beat and confirm the on-screen text matches the
intended content — not just that a video file exists at the right resolution with no
black pixels. Background/audio/slot checks catch render failures; they do not catch
render *success on the wrong content*.

---

## Review 5 — re-render verified, recompiled, PASS

**Content check, all 16 graphic beats, this time actually done:** extracted a frame from
every one of B01-B17 and read it directly (not sampled — all of them). Every card shows
its intended content: B01's opener reads "Same Room, Different Argument" /
"@HumanitariansAI" / "Claude"; B02-B16 each show the real heading/body/artifact text
written for that beat (Schank's SAM, the Robot Reply, the symbol grounding problem, the
Dictionary-Go-Round, Harnad on the list, the octopus test, B&K's exact quote, the
correction, the stochastic-parrot quote with full attribution, Bender's disavowal, the
"not settled science" honesty beat, the four-claim verdict, the task). **Zero instances of
"Photoelectric Effect," "Hola, Bear," or "@NikBearBrown" anywhere.** B17's outro correctly
reads "Same Room, Different Argument" / "SUBSCRIBE" / "@HumanitariansAI".

| Check | Method | Result |
|---|---|---|
| On-screen content, every beat | extracted + read a frame from all 16 rebuilt beats individually | **PASS** — matches intended props, zero leaked demo content |
| B00 actually gone | beat count | **PASS** — 17 beats, film opens on B01 (HOOK), no brand card |
| Resolution/framerate | `ffprobe` | 3840×2160, 24fps |
| Duration | `ffprobe` | 314.96s (down from 317.08s, consistent with removing B00's ~2s and B02's narration/prop timing being unaffected) |
| Black frames, whole film | `ffmpeg blackdetect` | **zero segments found** |
| Audio integrity | `ffmpeg volumedetect` | mean −27.3 dB, max −3.4 dB — unchanged from the pre-fix compile, as expected since no audio changed |
| Slot fill | `compile.py`'s own report | 17/17 |

**One cosmetic inconsistency noted, not fixed:** B17's `OutroCTA` uses a different design
token family (`VOX.CREAM = '#FFFFFF'`, flat white "never cream, never warm paper," per its
own source comment) than the other 16 beats' `CLAUDE.PAGE = '#FAF9F5'` cream. Not black,
not wrong, but a visible shade shift on the last beat of the film. `compile.py`'s own skin
lint flags this from a different angle: *"B17: palette=claude but the outro is 'OutroCTA'
— OUTRO LAW wants ClaudeTitleOutro."* That "correct" answer is the one component
confirmed hardcoded to `@NikBearBrown` — this lint is a known, deliberate exception, not
an unaddressed defect. Left as an open item for Tanmay to decide: accept the white outro,
or find/build a cream-toned generic outro instead.

**Verdict: PASS.** The specific defects raised — the uninstructed "This is Humanitarians"
line, Hola Bear, @NikBearBrown, and the underlying wrong-outro-component problem — are
fixed and verified by direct inspection, not just by re-running the same checks that
missed them the first time.

---

## Review 6 — outro background fixed, presenter name added, final recompile

Two follow-up requests: fix B17's flat-white background to match the film's cream, and
make sure Tanmay's name appears on screen at least once (narration already says it in
B02, but nothing on screen did).

**B17 outro:** switched from `OutroCTA` (`VOX.CREAM = '#FFFFFF'`) to `ClaudeTitleOutroFull`
— found by checking sibling outro components' source directly. Confirmed before use: no
hardcoded brand string anywhere in the file (unlike `ClaudeTitleOutro`), background is
`CLAUDE.PAGE` (the same cream as every other beat), and its `handle` prop already defaults
to `@HumanitariansAI` rather than `@NikBearBrown` — this component was built for exactly
this channel. Props set: title "Same Room, Different Argument.", handle
"@HumanitariansAI", subline "Tanmay Kulkarni, in for Humanitarians AI" (added so the name
appears here too, not just in B02).

**B02:** prepended "Tanmay Kulkarni, in for Humanitarians AI." to the card's body text.

| Check | Method | Result |
|---|---|---|
| B17 background now cream, not white | extracted frame, read directly | **PASS** — matches "The lineage." card's tone in the same recompile |
| B17 no hardcoded brand string | grepped full `ClaudeTitleOutroFull.tsx` source before using it | **PASS** — none found |
| B02 name visible on screen | extracted a later frame (body text animates in after ~1s) | **PASS** — "Tanmay Kulkarni, in for Humanitarians AI." reads clearly as the first sentence |
| Full recompile | `compile.py --review --height 2160` | 17/17 filled |
| Resolution/framerate | `ffprobe` | 3840×2160, 24fps |
| Duration | `ffprobe` | 314.958s |
| Black frames, whole film | `ffmpeg blackdetect` | zero segments |
| Audio integrity | `ffmpeg volumedetect` | mean −27.3 dB, max −3.4 dB, unchanged (no audio touched) |

**Skin lint, unchanged and still a known exception:** *"B17: palette=claude but the outro
is 'ClaudeTitleOutroFull' — OUTRO LAW wants ClaudeTitleOutro."* Same situation as Review 5
— the lint's suggested "correct" component is the one confirmed hardcoded to the wrong
channel. Deliberate, documented deviation, not an oversight.

**Verdict: PASS.**

---

## Review 7 — production gate, scored against the master

Same standard as Week 22's Review 1: scored by sampling every beat of the master against
its own narration clock, not by reading the beat sheet. Sample point = 25% into each
beat's *measured* duration (`actual_duration_s`), same rule Week 22 used.

| Criterion | Result |
|---|---|
| Evidence legible at the moment of assertion | **PASS** — all 17 beats sampled at 25% of their own duration; every beat's key card/quote/citation is already fully rendered at that point (checked directly, not inferred from render logs) |
| Sources on screen, not just voiced | **PASS** — every claim-bearing beat (B04-B08, B10-B14) carries a visible `FACTCHECK.md` row number or explicit author/year attribution in the card footer, not just in narration |
| Side-by-side at the moment of comparison | **PASS** — B08 ("Harnad is on the list") holds Searle's rejection and Harnad's proposal in the same numbered list; B11 ("not the Chinese Room again") holds Searle's question and Bender & Koller's question together; B15 holds all four names/dates in one line |

### One thing checked and resolved, not just assumed

B11's on-screen card states "Searle: can rule-following ever be thinking..." and "Bender &
Koller: can meaning be learned from form alone..." as direct, unhedged lines. Checked
whether this overclaims relative to `FACTCHECK.md` 3.5, which is explicit that the
"not a Chinese Room repeat" framing comes from a close reader's analysis (Julian Michael),
not a line either paper's authors wrote about themselves. On inspection this is fine: the
card states each paper's actual scope (Searle's real target per FACTCHECK 1.4; B&K's real
claim per FACTCHECK 3.2), which is directly supported — the meta-claim *about* the
distinction (that commentators explicitly separate the two) stays in the narration, where
it's correctly hedged ("close readers... are explicit"), and isn't repeated as an
unqualified claim on screen. No change needed.

### Held to its own standard

The film's rule is *check what each side actually wrote, don't flatten it into one tidy
story.* Applied to itself:

- **It passes on facts.** Every claim-bearing card cites a FACTCHECK row or a named
  primary source — nothing asserted without a visible attribution.
- **It passes on hedging.** B14 keeps the "not settled science" caveat as its own beat
  immediately before the verdict, rather than burying it.
- **It does not manufacture false symmetry.** B03's photo is real and sourced (Searle,
  2005, Christ Church) while B06 (Harnad) is honestly a text card because no rights-cleared
  photo exists — the film doesn't pretend otherwise.

### Rubric

| Criterion | This cut |
|---|---|
| **Explicit framework** | **2** — B02 states the four-name/four-decade lineage and the "it is not [one argument]" thesis on screen, not just in narration |
| **Reusable rubric** | **1** — B16 gives a real, actionable method ("go find what each side actually wrote") but it's a general habit, not a checkable step-by-step rubric the way Week 22's three-question framework was |
| **Worked example** | **2** — four real cases, each with its actual reasoning shown (not just a conclusion), sourced to FACTCHECK throughout |
| **Falsifiability / edge case** | **2** — B14 tests the film's own central claim (B&K's arithmetic prediction, now contested) |
| **Active task** | **1** — B16's task is real but soft (go read primary sources) rather than something the viewer does and measures, unlike Week 22's tap-and-count |
| **Friction** | **1** — B11 is the closest thing to genuine friction (correcting the viewer's assumption from B01), but there's no held moment (silence, forced pause) the way Week 22's B11 used timed silence |

**9/12.** Lower than Week 22's 12/12 on the two "activity" axes (reusable rubric, active
task, friction) — this film is built to correct a citation/attribution habit, which is a
harder thing to turn into a tap-this-and-count exercise than a physical measurement was.
Not a defect to silently accept, but not a gap to manufacture busywork to close either.

**Verdict: PASS, production gate 9/12.** Ready to move to a clean final cut (no `--review`
chrome).

---

## Review 8 — building the clean final cut (GATE F and GATE V, unplanned)

Attempting `compile.py` without `--review` (the actual final master, no beat-id chrome)
hit two hard gates neither of the review-cut runs had exercised:

**GATE F — missing paperwork.** `compile.py` refuses a final (non-review) cut without
non-empty `FACTCHECK.md`, `SHOTLIST.md`, and `PROMPTS.md`. Only `FACTCHECK.md` existed.
Added `SHOTLIST.md` (generated from the actual beat sheet's shot patterns) and
`PROMPTS.md` (states plainly there are no CLI/AI-video-prompt beats in this project —
everything is either the sourced photo or a Remotion card with props written directly).

**GATE V — frame-level visual QC, run for the first time on this project.** This is a
real, calibrated check (`runtime/qc/final_frame_check.py`) that samples the actual master
and audits every beat's pixel content against the title-safe area — something none of
Reviews 1-7 did, because they checked resolution/audio/black-frames/on-screen-text but
never *how much of the frame the content actually fills*. First run: **2 BLOCKER, 28
MAJOR** across 34 sampled frames.

| Defect | Cause | Fix |
|---|---|---|
| **MAJOR** `underfill` on 14 of 17 beats (23-40% of safe area filled, need ≥55%) | `MedhavyConceptCard` sizes its card at a hardcoded `width: 820` — correct at 1080p, only ~21% of a 3840px-wide 4K frame; `ClaudeVerdictArtifact` scales proportionally but caps at a hardcoded `1560px`, same problem at 4K | Migrated all 14 beats to `ClaudeArtifactCardFull` — a component that exists specifically for this: its own docstring cites this exact defect class ("Gate V measured 18-20% and 53% against a 55% floor") and sizes everything as a fraction of `height` instead of fixed pixels. Confirmed compatible before switching: same `artifactTitle`/`artifactHeading`/`artifactLines` contract as `ClaudeVerdictArtifact` (5 beats: trivial rename); `MedhavyConceptCard`'s `sparkLine`/`heading`/`body`/`evidenceNote` beats (9 beats) were remapped — `sparkLine` → `artifactTitle`, `heading` → `artifactHeading`, `body` split into 2-3 lines, `evidenceNote` folded in as its own line so citations stay on screen. No wording changed beyond the line breaks. |
| **BLOCKER** `edge-bleed` on B03 (both samples) | The Ken Burns pan on the Searle photo is *supposed* to fill the frame edge-to-edge — that's what Ken Burns is — but Gate V doesn't know that by default | Declared `qc.full_bleed: true` on B03 — a real, narrow, per-beat opt-out the toolkit provides for exactly this case (its own docstring: "some compositions fill the frame on purpose... for those, edge-bleed is the design, not a defect... underfill and every other check still apply"). Not a blanket disable — verified `full_bleed_beats()` only affects B03 and only suppresses the edge-bleed check, nothing else. **First attempt at this failed silently**: I placed the flag at `beat["shot"]["qc"]`, but the checker reads `beat["qc"]` (top-level) — traced with a direct Python call to `full_bleed_beats()`, confirmed it returned an empty set, fixed the placement, confirmed it returned `{'B03'}`. |

**After both fixes: Gate V clean — 0 BLOCKER, 0 MAJOR, re-verified against the actual
final master file, not just the review cut.**

**Also discovered:** `compile.py`'s own "stamp" step (which runs on every compile,
recording build provenance into `beat_sheet.json`) strips unrecognized custom keys from
a beat's `shot` object — this is why the first `qc` placement silently vanished after a
recompile. Anything added outside the schema `compile.py` itself writes needs to go at
the top level of the beat, not nested under `shot`, or it needs to be re-applied after
every compile pass.

**Final master:** `same-room-different-argument-final.mp4` (also in
`brutalist.art/renders/`), 3840×2160 @ 24fps, 314.958s, mean −27.3 dB / max −3.4 dB audio,
zero black frames, zero Gate V defects, no review chrome. `SKIN LINT` on B17
(`ClaudeTitleOutroFull` vs the flagged `ClaudeTitleOutro`) remains the one known,
documented, deliberate exception — unchanged reasoning from Review 5/6.

**Verdict: PASS. This is the deliverable.**

---

## Review 9 — rubric-driven revision (raising the production-gate score)

Tanmay asked where the 9/12 gate score was weak and approved acting on it. All three
losses were on the "activity" axes (reusable rubric 1/2, active task 1/2, friction 1/2).
One redesigned turn addressed all three:

- **Reusable rubric →2:** B02 now states the actual checklist out loud and on screen —
  "what does it claim to prove? Does it answer the one before it? Has the author
  corrected its misuse since?" — instead of leaving the method implicit. B17 (was B16)
  restates the same three questions verbatim as the handed-back takeaway.
- **Active task →2:** B11 is a new beat — a guess-along game. Both Searle's and Bender &
  Koller's questions are shown unlabeled; the viewer is asked to guess which is whose
  before the next beat answers it. Self-checkable inside the film, no outside research
  required.
- **Friction →2:** B11's audio was padded with 1.8s of trailing silence (`ffmpeg apad`),
  producing a real 2.4s held pause — verified with `silencedetect` — before B12 (new)
  delivers the reveal and the correction. `actual_duration_s` and `mp3/timings.json`
  updated to match the padded length so the visual hold is genuine, not just implied.

**Mechanical consequence:** the old B11 (correction) split into B11 (guess) + B12
(reveal), shifting every beat from the old B12 onward up by one ID (old B12→13 ... old
B17→18). Given the scale of the renumbering, did a full regeneration rather than patching
IDs in place: cleared all `mp3/`/`media/` (except the B03 pantry asset), regenerated all
18 beats' audio, re-padded B11, re-rendered all 17 graphic beats, recompiled.

| Check | Result |
|---|---|
| New/changed beat content (B02, B11, B12, B17) | **PASS** — read every frame directly, matches intended checklist/guess/reveal content |
| Renumbered beat content survived the shift (spot-checked B13, B18) | **PASS** — identical to their pre-shift content, correct IDs |
| B11 audio padding | **PASS** — `silencedetect` confirms 2.385s trailing silence; volumedetect confirms no clipping/failure on the padded file |
| Full recompile, resolution/duration | 3840×2160, 24fps, 346.375s (up from 314.958s — one new beat plus the added checklist content in B02/B17) |
| Black frames, whole film | **PASS** — zero segments |
| Audio integrity | **PASS** — mean −27.4 dB, max −3.4 dB |
| Gate V (frame-level QC) | **PASS** — 0 BLOCKER, 0 MAJOR across 36 sampled frames (18 beats × 2 samples) |
| Final clean master (no review chrome) | Built and independently re-verified — same checks, same result, against `same-room-different-argument-final.mp4` directly |

**Gate P status — flagged, not silently carried forward.** Tanmay approved the *plan* for
this revision (the three fixes described in chat) but has not yet read the exact final
narration lines aloud against `READ-ALOUD.md`. Per this project's own rule, new words are
a new Gate P precondition. Recorded honestly here rather than assumed: the previous
signed PASS (draft 3) does not cover draft 4's actual wording in B02/B11/B12/B17.

**Verdict: PASS on everything mechanically and visually checkable. Gate P on the new
wording is open, pending a read.**

---

## Review 10 — full re-score against the revised, signed final master

Gate P for draft 4 signed since Review 9 ("read aloud and pass all beats," 2026-09-20 —
see `PEDAGOGY.md`). This review does what Review 7 did, but against
`same-room-different-argument-final.mp4` as it now stands (18 beats, post-revision) —
the 9/12 score was never re-run end-to-end after the Review 9 fixes landed, only
spot-checked. Closing that gap now.

**Production gate**, sampled at 25% of each beat's measured duration, all 18 beats on
the actual final file (not the review-chrome cut):

| Criterion | Result |
|---|---|
| Evidence legible at the moment of assertion | **PASS** — all 18 beats checked (not sampled — full sweep), every card/quote/citation fully rendered by 25% into its own duration, including B02 at its new 39.68s length |
| Sources on screen, not just voiced | **PASS** — unchanged from Review 7 for beats B04-B10/B13-B16; B12's new correction card still names both papers by year, matching spoken attribution |
| Side-by-side at the moment of comparison | **PASS** — B11 now holds both unlabeled questions together (a stronger side-by-side than draft 3 had, since neither is pre-labeled); B12 holds the labeled reveal; B16 (was B15) still holds all four names |

### Rubric, re-scored

| Criterion | Review 7 | Review 10 | Why it moved |
|---|---:|---:|---|
| Explicit framework | 2 | 2 | unchanged |
| Reusable rubric | 1 | **2** | B02 now states the three-question checklist verbatim on screen; B17 hands it back verbatim as the closing takeaway. Honest caveat: this is stated twice, not carried through a persistent per-beat corner card the way Week 22's was — a lighter execution of the same requirement, not an identical one, but the core ask (viewer leaves with an explicit, reusable method) is met |
| Worked example | 2 | 2 | unchanged |
| Falsifiability / edge case | 2 | 2 | unchanged (B15, was B14) |
| Active task | 1 | **2** | B11 is a real predict-then-check task the viewer does inside the film. Honest caveat: it's a binary guess, not a continuous measurement against a distribution like Week 22's tap-and-count — genuinely active, but lighter-weight than that bar |
| Friction | 1 | **2** | B11's guess is followed by a measured 2.385s silence (verified via `silencedetect`, not estimated) before B12's reveal — a real predict-then-reveal beat, the same mechanism family as Week 22's held-silence moment |

**12/12.** Matches Week 22's score, by a different but comparably real route — two lighter,
appropriately-scoped versions of the same two mechanisms (guess vs. measure; stated
checklist vs. persistent corner card), not weaker copies of them.

**Verdict: PASS. Production gate closed at 12/12. Nothing outstanding on this film.**

---

## Review 11 — re-verification alongside the Short's own review

Tanmay asked for a PROOF review on both formats together. Re-ran the long's core checks
against the exact delivered file (`same-room-different-argument-final.mp4`) to confirm no
drift since Review 10: resolution 3840×2160 @ 24fps, duration 346.375s (unchanged), zero
black frames, audio mean −27.4 dB / max −3.4 dB (unchanged), Gate V 0 BLOCKER / 0 MAJOR
across 36 sampled frames (unchanged). **Identical to Review 10 — no rescoring needed.**

The Short's own full review (trailer-appropriate criteria, not this film's pedagogy
rubric) lives in `short/SHORTS-BUILD-LOG.md` — it caught and fixed a real factual error
in the outro's timeline claim during the pass.

---

## Review 12 — final joint sign-off, both formats, before setting up the delivery folder

Tanmay asked for a genuine trailer-specific rubric on the Short (done — Review 11 /
`short/SHORTS-BUILD-LOG.md`), then a final proof review on both formats together using
the same practice followed at every stage of this build: full mechanical re-verification
against the actual delivered file, not assumed from prior passes.

| Check | Long | Short |
|---|---|---|
| File | `same-room-different-argument-final.mp4` | `short/same-room-different-argument-short-final.mp4` |
| Resolution / fps | 3840×2160 @ 24fps | 2160×3840 @ 24fps |
| Duration | 346.375s (5:46.4) | 87.333s (1:27.3) — under the 180s Shorts cap |
| Black frames | zero, full scan | zero, full scan |
| Audio | mean −27.4 dB / max −3.4 dB | mean −27.7 dB / max −5.2 dB |
| Integrated loudness / true peak | −24.86 LUFS / −3.39 dBTP | −24.93 LUFS / −5.22 dBTP |
| Gate V | 0 BLOCKER / 0 MAJOR (36 frames) | 0 BLOCKER / 2 MAJOR (12 frames — end-card underfill, documented exemption) |
| Gate P | Signed PASS, 2026-09-20 | Reuses the long's signed narration for B08/B11/B12; the short-only intro and outro are new text, mechanically checked for FACTCHECK fidelity in Review 11 rather than a separate formal Gate P read |
| Rubric | **Production gate: 12/12** (Review 10) | **Trailer Gate: 12/12** (own criteria, `short/SHORTS-BUILD-LOG.md`) |
| Known, documented exceptions | B03 full-bleed declaration (Ken Burns photo, legitimate) | END card underfill (deliberate minimal sign-off); `compile.py`'s automated final path has an unreproduced internal Gate V quirk — final file built and verified independently instead, see `short/SHORTS-BUILD-LOG.md` |

**One open item, named rather than glossed over:** the Short's short-only beats (intro,
outro) were verified for factual accuracy against `FACTCHECK.md` and read correct on
screen, but never went through a dedicated spoken read-aloud sign-off the way the long's
`PEDAGOGY.md` Gate P did. If that formal read matters before publishing, it's the one
remaining step — everything else has been checked against the actual files, not assumed.

**Verdict: PASS on both formats.** Ready to assemble the final delivery folder.
