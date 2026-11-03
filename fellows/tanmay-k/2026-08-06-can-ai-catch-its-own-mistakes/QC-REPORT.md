# QC-REPORT — Can AI Catch Its Own Mistakes? I Ran the Experiment

Append-only. Every fix dated, per PLAYBOOK §8. PROOF checked at every phase per
PLAYBOOK §1b.

---

## 2026-08-12 — components, beat sheet, audio, render, compile, pacing

### Components

Four generic, props-driven components carry all 13 beats (PLAYBOOK §2), plus a
shared `SkepticFrame` helper. Deliberately plain: one accent colour, a single
fade per element, no decorative motion, type-led.

| File | Registered as | Beats |
|---|---|---|
| `scenes/SkepticFrame.tsx` | *(helper)* | shared constants, easing, margins |
| `scenes/SkepticStatement.tsx` | `SkepticStatement` | B1, B2, B11, B13 |
| `scenes/SkepticList.tsx` | `SkepticList` | B3, B12 |
| `scenes/SkepticSplit.tsx` | `SkepticSplit` | B4, B5, B7, B10 |
| `scenes/SkepticNumber.tsx` | `SkepticNumber` | B6, B8, B9 |

All registered in `Root.tsx` **before** any pattern name entered a beat sheet.
Project typecheck: **0 errors** at every step.

Two constraints enforced in code rather than left to discipline:

- **`figure` and `bound` are fields on the same component.** The count (`0`) and
  its ceiling (`8.7%`) cannot drift into independently-editable beats — PROOF's
  gate requires them in frame together.
- **B3 and B12 use the same component.** The four questions the film teaches and
  the four it hands over are one object and cannot diverge.

### Defects found by looking at frames

1. **`0 / 33` read backwards — FIXED.** It parses as a score ("caught 0 of 33"),
   the exact opposite of the finding. Now `0` with caption *"missed — out of 33
   wrong expressions"*, matching the narration's "Zero. Not low. Zero."
   Genuinely misleading had it shipped.
2. **Newlines collapsed in split panels — FIXED.** Prompts rendered as one
   run-on line. Needed `white-space: pre-line`.
3. **Quote rule over-ran the text by ~100px — FIXED.** Replaced the hardcoded
   box with a CSS `border-left` on the text itself, so it auto-sizes.

### PROOF checkpoint before the beat sheet — two gate violations

Run at the Phase 2 → Phase 3 boundary. Both are Behavioral Rule 3 (*never let a
claim ship without a visible source at the moment of assertion*):

- **B4 [EDIT]** — narration quotes the draft verbatim (*"same weights, same
  activations, same direction of error"*) with no quote and no source on screen.
- **B7 [EDIT]** — narration claims *"what the published work actually does"*
  with no citation on screen. This is the film's **only** appearance of the paper
  it is testing, and the only place the preprint / peer-reviewed distinction is
  visible.

**Fix:** added a `source` prop to `SkepticSplit` that fades in by **~14%** of the
beat, not the footer's 80%. The timing is the point — a footer *is* an artifact,
but one arriving after the claim has been spoken does not satisfy "legible at the
moment of assertion." Presence is necessary, not sufficient.

Both verified on the **shipped master**, sampled at the moment each claim lands:
B4 at 28% into the beat, B7 at 32%.

### Deviation logged: framework at 0:45, not the first ~20s

PROOF's Phase 2 gate suggests the framework graphic in the first ~20s. It lands
at **0:45** and completes at **1:15**. The binding constraint — *framework before
examples* — is met with zero overlap (B3 ends 1:15, B4 starts 1:15).

B1 is the claim under test and B2 is the admission of prior expectation that
makes B8's reversal land; cutting either would flatten the arc PLAYBOOK §1a
exists to protect. Logged as a deviation, not argued as a pass.

### Audio — the master clock

`generate_audio_kokoro.py`, voice **`am_onyx`**, GATE P signed in `PEDAGOGY.md`
and `SCRIPT.md` first. **295.1s across 13 beats.**

Onyx runs at ~223 wpm against the ~180 wpm assumed when drafting, so the film
came in at 5:07 rather than the projected 6:22. Worth carrying forward: **the
two voices are not interchangeable for runtime estimates.**

Voice and register are a **documented deviation**: the toolkit pairs Onyx with
the Teardown register, and this film keeps a warm first-person register instead.
Rewriting B6's wince or B8's disbelief into Teardown clip would destroy the arc.
Recorded in `SCRIPT.md` so it reads as a choice.

### Composition durations retuned to measured audio

Every component was registered at 600 frames (20s) for QC. Left alone, **B13
(8.7s) would have been truncated at 43%** — losing the sign-off line entirely,
because the conform step uses `-t`.

Rule applied: **composition duration ≤ the shortest beat it serves**, and long
enough for its own animation to settle.

| Component | Frames | Shortest beat served | Settles by |
|---|---:|---:|---:|
| `SkepticStatement` | 240 (8.0s) | B13 — 8.70s | ~5.7s |
| `SkepticList` | 540 (18.0s) | B3 — 22.24s | ~16.8s |
| `SkepticSplit` | 600 (20.0s) | B5 — 21.46s | ~16.0s |
| `SkepticNumber` | 540 (18.0s) | B8 — 19.11s | ~15.5s |

B13's settled frame was checked directly afterwards — the sign-off is present.

### Render and compile

All 13 beats rendered through `remotion_scenes.py`, one at a time, foreground,
bounded timeout. **Every output confirmed 3840×2160.** Compiled with
`compile.py --height 2160`.

Three lints. One fixed, two accepted:

1. **Motion metadata missing — FIXED.** The beat sheet used a non-standard
   `shot.scene_type`; the convention is `shot.type` / `shot.source` /
   `shot.motion`, and the histogram read `?` for all 13. Set to `fade` (4) and
   `illustrate` (9). No re-compile needed — every slot filled as `VIDEO`, and
   motion only governs still-image animation.
2. **COLD OPEN LAW wants `ClaudeComposerAsk` at B1 — ACCEPTED.** This film opens
   on the claim under test. Spending the hook on UI chrome would waste it.
3. **OUTRO LAW wants `ClaudeTitleOutro` at B13 — ACCEPTED.** The brief was
   deliberately plain visuals; a branded outro component fights it.

### Pacing

`pacing_pass.py` (kept from the Lemonade reel, PLAYBOOK §5): 1.0s hold — frozen
last frame plus silence — before all 12 internal cuts, hard cut after, no
crossfade. **Must be re-run after any recompile.**

### Final verification

| Check | Result |
|---|---|
| Resolution | **3840×2160** by `ffprobe` on the final file (PLAYBOOK §6) |
| Duration | **307.5s (5:07)** = 295.1s narration + 12 × 1.0s holds |
| Hold is a true freeze | **PSNR 92.4 dB** between two frames inside one hold |
| Cut is a hard cut | **PSNR 19.4 dB** across the same cut |
| Gate: source at moment of assertion | Verified on the shipped master — B4 @28%, B7 @32% |
| Gate: count and bound together | Verified — B9 holds `8.7%` and `0 missed / 33 tested` in frame |
| Text legibility at 4K | Confirmed by looking at frames from the final master |

Master is 13MB / ~357 kbps. Low for 4K, and not a quality problem: flat vector
fields, no grain, long static holds. Verified by looking, not by trusting the
number.

### Outcome — first cut

`can-ai-catch-its-own-mistakes.mp4` — 5:07, 3840×2160, 13 beats.
Teaching **12/12** projected. Production gate **PASS** after the two B4/B7 fixes.

---

## 2026-08-12 (later) — author review of the finished cut: two defects, both fixed

The film was watched end to end by the author. Two findings, one of them
structural. Both are recorded here in full because both were invisible to every
automated check that had already passed.

### 1. An audible pause mid-sentence at ~1:00 — FIXED

Reported as *"the word 'Let's' is cut, there's an abrupt pause."* The word
"Let's" is at **15.9s**, not 1:00, so that attribution was off — **but the defect
was real and exactly where it was reported.** Silence detection on the shipped
master found four gaps that were not the intentional 1.0s inter-beat holds:

| Time | Gap | Beat |
|---|---|---|
| 45.61s | 0.75s | B3 |
| **60.50s** | **0.84s** | **B3** — the one heard |
| 228.94s | 0.62s | B10 |
| 287.57s | 0.62s | B12 |

**Cause: punctuation, not the renderer.** B3 numbered its four questions as
one-word sentences — *"One. What's the claimed cause? Two. …"* — and Kokoro
treats a full stop after a single word as a hard stop. Nothing was truncated;
the silence was synthesised exactly as written.

**Fix:** ordinals with colons (*"First: what's the claimed cause?"*), and the
three closing fragments joined into one sentence. Re-measured after
regeneration: **no silence over 0.55s anywhere in B2 or B3**, and a sweep of all
thirteen beats at the same threshold now returns nothing. The 0.62s pairs in B10
and B12 did not reproduce at −40 dB / 0.55s on the rebuilt master.

**Carry forward: punctuation is a timing instruction to the TTS engine, not a
typographic choice.** A one-word sentence buys a full stop's worth of silence.

### 2. The central idea did not land — FIXED, and the more serious of the two

Reported as: *"it is able to show what happened but I did not get much clarity
of what this whole video is about."*

Correct, and diagnosable. Here is what a viewer actually had after one minute:

| Time | What they had been given |
|---|---|
| 0:00–0:18 | A quoted sentence with jargon in it, and that it carries no number |
| 0:18–0:39 | That the author expected to confirm something, and it is "about one question you can put to any claim" |
| 0:39–1:02 | Four abstract meta-questions about causal claims |

**A full minute in, the film had never said the words "catch its own mistake."**
It stated the *meta*-lesson (how to test a causal claim) without ever stating the
*subject* (whether a model can check its own work). Every event was legible and
the spine was not.

This is a miss against our own standard, not a matter of taste. **PLAYBOOK §1
mandates an intro-summary beat** — *"Hi, I'm [name], this video covers X."* B2
delivered the greeting and skipped the *covers X*.

**Fix — B2 rewritten** to lead with the question in ordinary language ("does it
catch the mistake, or does it just agree with itself?"), keep the admission of
prior expectation that makes B8's reversal land, state the scale of the test,
and say what the viewer walks away with. The on-screen statement changed from
*"I picked this topic expecting to confirm it"* to the question itself.

**PROOF check on the rewrite.** B2 now voices *"thirty-three wrong answers"* as
a forward reference — a number, and therefore Behavioral Rule 3 territory. A
source line was added to the beat (`33 wrong expressions · 99 verdicts · our own
run, results-20260812T014950Z.json`). It fades in at 34% of the composition
(~2.7s) and the number is spoken at ~68% of the beat, so the evidence is on
screen well before the claim. Checked on the frame, not assumed.

### Title changed

**"The Control You Didn't Run" → "Can AI Catch Its Own Mistakes? I Ran the
Experiment."** The old title named the *method* and told a viewer nothing about
the *subject*; paired with an abstract opening it left no anchor anywhere. The
old phrase is kept in metadata as `working_title`.

**The build directory keeps the old slug** (`youtube/the-control-you-didnt-run/`).
It is a working path, not a deliverable, and its concat manifests carry absolute
paths that a rename would silently break. The shipped file is
`can-ai-catch-its-own-mistakes.mp4`.

### Rebuild and re-verification

Audio regenerated for B2 and B3 only; both beats re-rendered; full recompile;
`pacing_pass.py` re-run (mandatory after any recompile).

| Check | Result |
|---|---|
| Resolution | **3840×2160** by `ffprobe` on the final file |
| Duration | **322.3s (5:22)** = 310.0s narration + 12 × 1.0s holds |
| B2 audio | 20.42s → **33.11s** |
| B3 audio | 22.24s → **24.43s** |
| Rogue silences > 0.55s | **none** — every gap over threshold is an intentional hold |
| Hold is a true freeze | **PSNR 92.4 dB** within the B1→B2 hold |
| Cut is a hard cut | **PSNR 19.4 dB** across the same cut |
| B2 / B3 frames | Inspected directly at settled points; both legible at 4K |
| Gate: source at moment of assertion | B2's results-file line verified on the frame |
| Composition durations | Unchanged and still valid: `SkepticStatement` 240f serves B13 (8.71s); `SkepticList` 540f serves B3 (24.43s) |

Compile lints unchanged from the first build: COLD OPEN LAW, OUTRO LAW and the
`illustrate` motion cap, all three previously accepted and re-accepted here.

### What this pass says about the process

Both defects survived a clean PROOF audit, a full claims audit, a frame-by-frame
QC sweep and a production-gate verification. Neither is a claim error — they are
a **comprehension** error and a **delivery** error, and no rubric in use here
scores either one. The check that caught them was a person watching the film.

Worth stating plainly: **PLAYBOOK §1's intro-summary beat was already the rule,
and the first cut did not follow it.** The gap was not a missing standard. It
was a standard that nothing in the pipeline tests for. A "does B2 name the
subject in plain words?" line item belongs in the phase-2 check.

### Outcome

`can-ai-catch-its-own-mistakes.mp4` — **5:22, 3840×2160, 13 beats.**
Teaching **12/12** projected. Production gate **PASS**.
