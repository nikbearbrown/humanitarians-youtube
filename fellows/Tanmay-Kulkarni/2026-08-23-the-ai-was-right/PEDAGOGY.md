# PEDAGOGY — The AI Was Right. That Was the Problem.

Week 19 · Humanitarians AI · presented by **Tanmay Kulkarni**, voice `af_bella`, Pragmatist register
Rebuilt from `claude-for-music/indie-on-the-pitch`. Append-only log (PLAYBOOK §8).

---

## 2026-08-23 — Authoring audit

### Laws check

- **Intro-summary beat present and it names the subject** (PLAYBOOK §1, §1c) ✓ — B02 says
  "getting your song into film and TV" in plain words before the term "sync licensing", and
  states the takeaway up front.
- **Framework shown before examples** (PROOF Phase 2) ✓ — `SyncClaimLayers` at ~0:18, inside
  the first 20s. First example is B04 at ~1:25.
- **Tone is an arc, not a setting** (PLAYBOOK §1a) ✓ — mapped before writing: blunt → warm →
  clear → conspiratorial → diagnostic → **peak (B05)** → pullback (B06) → sober → practical →
  warm. Peak-then-discipline shape.
- **Punctuation as TTS timing** (PLAYBOOK §1d) ✓ at authoring — ordinals with colons in B08,
  not "One. Two. Three." Deliberate short landings in B01/B04/B05 are intentional pauses.
  **Still to do:** `silencedetect` sweep over `mp3/` after generation, before compiling.
- **No fabrication** (PROOF §CORE) ✓ — every load-bearing claim traces to a primary read
  directly. Nothing inherited from the source folder, whose `RECEIPTS.md` does not exist.
- **Claims calibrated to evidence** (PROOF rule 5) ✓ — B06 states n=10 / one model / one run
  on screen and in narration. No percentage is ever shown; the count is shown instead.
- **Illustrate law — no two adjacent beats share a scheme** ✓ — the two `WantQuote` beats
  (B05, B07) are separated by B06; the two `SyncClaimLayers` beats (B02, B05) are far apart
  and the second deliberately fills the first's empty structure with a real claim.
- **Structure is unique to this film** ✓ — see the v2 entry below.

### Corrections made to the inherited material

The source was a **Musinique** episode (6/7, `@Musinique`, `am_puck`, Baldwin register) that
had been mechanically rebranded to HAI. Three artifacts described three different videos;
the rebrand had deleted the original cold open and injected two boilerplate beats. Full
diagnosis in `SOURCE-ANALYSIS.md`. Everything except the subject, the machine/human thesis
and the render patterns was rebuilt.

Two claims from the source were **dropped as unsupported**:

- "No legitimate sync company ever charges artists." The GMS Code of Conduct was read
  directly and contains no such rule; no FTC music-specific alert exists. Replaced with the
  honest and stronger version — *nobody is checking this for you*.
- All episode-2/3/4/5 cross-references. The film is standalone.

### Components

Three authored for this film — `SyncClaimLayers`, `SyncRecordStrata`, `SyncCheckResult` —
each portrait-portable by construction, so each `916` is a 10-line alias rather than a port.
Typecheck clean; all six compositions register; QC stills for both aspects in
`components-qc/`. Rationale in `PATTERN-STRATEGY.md`.

### Presenter and voice

Spoken as **Tanmay Kulkarni**, in for Humanitarians AI, at both the open (B02) and the close
(B09) — matching Week 18, whose B00 is "Hi, this is Tanmay Kulkarni from Humanitarians AI."

Voice is `af_bella`, not `af_kore`. `generate_audio_kokoro.py` allows only `am_onyx` and `af_bella`;
`af_kore` exists in the voice pack but is not permitted, and Weeks 17 and 18 both shipped on
`af_bella`. No toolkit patch.

### PROOF gate

- **Phase 1 — PREMISE: CLEARED.** Framework has a mechanism (record tiers), a rubric
  (attribution / placement / detail), a worked example (C10), a real falsifiability case
  (C05/C06 — true and still wrong to say).
- **Phase 2 — BUILD: teaching 12/12**, ship bar 8.
- **Production gate: PROVISIONAL.** Legibility at the moment of assertion cannot be scored
  from a script. Re-run on rendered frames before this is called a pass.

**AUTHORING VERDICT: PASS** — render QC and the production gate happen at build.

---

## 2026-08-23 — Script v2: structure changed from a SPLIT to a CROSS-SECTION

Per reviewer feedback, 2026-08-23. Two changes.

**1. Presenter named.** "I'm Bella" → "I'm Tanmay Kulkarni, in for Humanitarians AI", at the
open and the close.

**2. The framework was rebuilt.** v1 was a machine-half / human-half split rendered as two
columns (`SyncSplitFrame`, `SyncRecordTiers`). Withdrawn for two reasons:

- **It was inherited, not derived.** The split came from the Musinique source's thesis. The
  research replaced that thesis. What the experiment found is not that the job has two
  halves — it is that *a claim passes every layer you check, and there is a layer beneath
  the ones you check*. Attribution → placement → detail is sequential depth, and the twist
  is a fourth layer below. That is a cross-section, and the split was actively misdescribing
  the finding.
- **It duplicated Week 18.** *Their Numbers, My Arrows* is built entirely on two columns —
  its own B02 says "it's the only method in this video. Two columns." Reusing it would make
  the device a house signature rather than this film's structure.

A third argument arrived for free: **two side-by-side panels are the worst possible layout
in 9:16**, and a downward stack is the best. The structure that is truer to the finding is
also the one that survives the Shorts cut.

New components: `SyncClaimLayers` (claim cut open, layers peeling down, a final terracotta
layer with no tick) and `SyncRecordStrata` (the public record as a core sample — bedrock
ownership data at the bottom, the fact you actually need loose on the surface).
`SyncCheckResult` kept unchanged; it is a tally list, a distinct device.

`SyncSplitFrame` / `SyncRecordTiers` and their `916` aliases deleted from
`runtime/remotion/src/scenes/` and unregistered from `Root.tsx`.

Runtime moved 2:37 → ~2:46. Still under the 3:00 cap.

---

## 2026-08-23 — v2.1: B05 split, beat sheet authored

Building `beat_sheet.json` surfaced a structural problem: **one beat carries one shot**, and
B05 needed two — the `SyncClaimLayers` callback *and* the sourced Golubić quote. Forcing
both into one beat would have put a verbatim quote on screen without its source (a PROOF
production-gate failure) or dropped the callback. Split into **B05 (the layers walk)** and
**B06 (the wince + quote)**; everything after renumbered. 10 beats total.

Beat sheet validated: no duplicate `beat_id` (the source folder's bug — it used `B00`
twice, which made the second unaddressable by `timings.json`), and no two adjacent beats
share a pattern.

**Runtime budget corrected.** The ceiling is **173.5s**, not 180 — `plan_drops` in
`shorts.py` computes `180 cap − 2 headroom − 4.5 silent endcard`. Estimate is 169.0s, so the
margin is **4.5s**, thinner than the "14s" quoted earlier against the raw cap. If measured
audio runs ~3% long the Short will start dropping beats; trim B09 or B03 first.

The 9:16 cut therefore runs ~4.5s longer than the 16:9 master — same beats, same audio,
plus the silent branded endcard.

---

## 2026-08-23 — v2.2: two fixes from the end-to-end read

Reading the narration as continuous prose — rather than beat by beat — surfaced two things
that per-beat frame QC and the PROOF gate had both passed.

**1. Two depth metaphors, unreconciled.** B02 teaches layers of a *claim*; B03 teaches layers
of the *record*. Both vertical, both "underneath", 25s apart, never related. Worse, B03 set up
"placement facts live in a soft record" while the payoff (B05) is a failure of *inference* —
Baby Blue is well documented. Setup and payoff were about different problems. Fixed with a
two-sentence bridge closing B03: "So the three layers you can check rest on soft ground. The
fourth isn't in any record at all." B03 audio regenerated, 21.61s → 24.36s.

**2. The viewer task depended on an artifact never shown.** B09 told the viewer to read the
"Music Supervisor Verified" / "Questions" label — introduced in the CTA, never on screen. A
scaffold that needs a UI element the viewer has never seen is not usable, and it is a factual
claim about a real product interface with no artifact at the moment of assertion. New
component `SyncSendChecklist` (+ `916` alias) renders the three label states with a source
line. Replaces `ClaudeVerdictArtifact` at B09.

Neither was caught by frame sampling, because every individual frame was legible. They were
only visible when the film was read as one continuous argument.

Runtime: 16:9 2:48.4 → **2:51.1**; 9:16 2:52.9 → **2:55.6**. Still under the 180s Shorts cap,
with 2.4s against the headroom-adjusted 178s — tighter than before and worth watching if any
beat grows again.

---

## 2026-08-24 — v2.3: pacing pass

Reviewer note: beats cut into each other too fast to absorb. Per PLAYBOOK §5 the fix is a
**hold** — frozen last frame plus silence, then a clean hard cut — not a crossfade, which
softens the cut without buying reading time. `compile.py` has no transition mechanism, so
this is a post-compile pass using `pacing_pass.py`, reused from Week 17.

| Cut | Hold | Before | After |
|---|---|---|---|
| 16:9 | 0.60s × 9 | 171.12s | **176.78s (2:56.8)** |
| 9:16 | 0.35s × 10 | 175.62s | **177.88s (2:57.9)** |

**Different holds per aspect, deliberately.** 0.60s × 10 on the vertical would have produced
181.6s and broken YouTube's 180s cap. A Short is also a swipe-away format where six seconds
of dead air is a retention cost the long cut does not pay. The Short's endcard was trimmed
4.5s → 3.0s to buy the remaining headroom.

Two defects surfaced during this pass and are recorded in `QC-REPORT.md` v2.3: the endcard's
silence was generated at 44.1 kHz against Kokoro's 24 kHz, and because `pacing_pass.py`
concatenates with stream copy, that single mismatched segment made the whole track report
326.8s instead of 177.8s. `compile.py` had been hiding it by re-encoding.

**Re-run `pacing_pass.py` after any future recompile** — `compile.py` overwrites the unpaced
master and knows nothing about this pass.

---

## GATE P — narration sign-off

Read-aloud pack: `GATE-P-READ-ALOUD.md`. A human must read every line aloud and record the
verdict here. **No audio is generated before this line reads PASS.** Audio is free in this
toolkit — this is a quality gate, not a cost gate.

```
VERDICT: PASS
Signed by: Tanmay Kulkarni (Humanitarians AI)
Date:      2026-08-23
Basis:     Script v2.1 reviewed and approved in session, after two rounds of
           revision (presenter naming; structure changed from split to
           cross-section). Not hand-timed.
Timing:    Estimated 169.0s against a 173.5s budget. Measured Kokoro audio is
           the clock — durations are checked against the budget immediately
           after generation, before any rendering, and a beat is trimmed if the
           read comes in long.
```

**Audio generation is authorised.**

---

## 2026-08-23 — Audio generated

Engine: Kokoro (`kokoro-onnx`, toolkit `.venv`), voice `af_bella`, 10 beats, cost $0.00.

### Per-beat pacing, not one setting

Kokoro takes no emotion or style parameter — the only prosody lever it exposes is `speed`,
and `--speed` is global. So each beat was generated in its own invocation with `--only` and
its own speed, chosen from the tone already mapped in the beat sheet:

| Beat | Speed | Measured | wpm | Intent |
|---|---:|---:|---:|---|
| B01 | 1.04 | 11.80s | 224 | blunt, brisk hook |
| B02 | 0.97 | 23.27s | 181 | warm welcome, slow down |
| B03 | 1.00 | 21.61s | 189 | curious, digging |
| B04 | 1.04 | 21.03s | 191 | diagnostic, moving |
| B05 | 0.96 | 17.94s | 187 | the peak — let it land |
| B06 | 0.95 | 10.99s | 147 | wry wince |
| B07 | 0.93 | 13.21s | 164 | careful pullback — slowest, deliberate contrast to B05 |
| B08 | 0.98 | 17.75s | 149 | sober, plain |
| B09 | 1.02 | 21.85s | 179 | practical, clear |
| B10 | 0.96 | 7.13s | 160 | warm close |

Delivered spread: **147–224 wpm, a 76 wpm range.** The `speed` flag accounts for only ~11%
of that; the rest comes from the writing — sentence length, the short landings ("It knew.",
"True. He did."), and punctuation as timing. That was the point of mapping the arc before
writing a line (PLAYBOOK §1a): the engine will not act, so the words have to.

### Measurements

- **Total 166.58s (2:46.6)** against a 173.5s Shorts budget → **6.9s margin**, better than
  the 169.0s estimate. The 9:16 cut lands at ~171.1s with the silent endcard.
- Largest estimate misses: B01 −3.20s (hook is tighter than it read) and B08 +2.75s.
- **`silencedetect` sweep at `-40dB:d=0.55` over all ten files: clean.** No TTS gaps, so the
  ordinals-with-colons treatment in B09 did its job (PLAYBOOK §1d).

Measured durations are now `actual_duration_s` in the beat sheet and `mp3/timings.json` —
these are the clock from here.

### Note

`generate_audio_kokoro.py` requires the toolkit venv (`.venv/bin/python`); the system Python
lacks `kokoro-onnx` and the script exits with an install hint rather than an error.
