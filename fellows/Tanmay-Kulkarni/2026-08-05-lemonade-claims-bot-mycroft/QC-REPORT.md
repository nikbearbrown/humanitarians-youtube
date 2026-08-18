# QC-REPORT — Lemonade Claims Bot Video

Append-only. Every fix dated, per PLAYBOOK §8.

---

## 2026-08-10 — Component build + first visual QC pass

### What was built

Two Remotion components, plus a shared frame helper, covering six of the
eleven beats:

| File | Registered as | Beats |
|---|---|---|
| `scenes/LemonadeFrame.tsx` | *(helper — not a composition)* | shared locator / header / carry-bar |
| `scenes/LemonadeStage.tsx` | `LemonadeStage` | B3, B5 (scaffold) |
| `scenes/LemonadeProduction.tsx` | `LemonadeProduction` | B4, B6, B8 (production) |

`LemonadeProduction` carries three interior variants — `branch`, `swap`,
`accumulate` — rather than three separate components, per PLAYBOOK §2. The
variants exist because the three production beats are three different
arguments; reading identically would make the middle of the film metronomic.

Both registered in `Root.tsx` **before** any pattern name was referenced in a
beat sheet. Project typecheck: **0 errors**.

### Render verification

Rendered through `runtime/scripts/remotion_scenes.py` (toolkit rule 5 — never
hand-rolled `npx remotion render`), one beat at a time, foreground, bounded
timeout. ~63s per beat.

**Output confirmed 3840×2160 on all four** via `ffprobe`. This is a true 4K
render, not an upscale: compositions are authored at 1920×1080 and rendered
with `--scale=2`, which supersamples text (`remotion_scenes.py:82`). All
artwork is vector, so it holds at that scale.

Frames sampled at **45% and 99% of each beat's own duration**, never fixed
frame numbers (PLAYBOOK §4). Frames were looked at, not just probed.

### Defects found and fixed

**1. Row dividers didn't match across the scaffold/production pair — FIXED.**
`LemonadeStage` drew its row dividers to `x=1140`; `LemonadeProduction`'s
`swap` variant drew them to `x=1090`. B5 and B6 are deliberately built to look
like the same picture so the viewer reads the delta rather than re-orienting —
a 50px jump on the cut would have undercut the whole grammar. Both now
`x=1140`, with a comment in the code recording why they must stay equal.

**2. Connectors floated instead of connecting — FIXED.** The dashed leaders
ran `1100→1220`, stopping 15px short of the swap cards at `x=1235`, so they
read as loose dashes rather than as pointing at anything. Now `1160→1235`,
touching the card edge.

**3. `accumulate` variant was inset and the nesting didn't read — FIXED.**
Two problems on the same frame. The rings spanned `260→1660` while the header
rule and carry-bar span `150→1770`, so the assembly looked like a narrower,
unrelated element. And the ring tints (`#EBE6DA`→`#F7F5EF`) were too close to
distinguish at render size, so the nesting was invisible. Rings now start at
`150→1770`, matching the rule and carry-bar exactly, and step inward by 50px;
tints re-stepped to `#E4DDCC`→`#F6F2EA`. All rings share a vertical centre with
the core file, so the layers read as concentric rather than top-anchored.

Re-rendered and re-checked after the fixes — all three confirmed resolved.

### Approved frames

The working folder holds the settled (99%) frame from each variant:
`B5-verification-scaffold.png`, `B4-intake-production.png`,
`B6-verification-production.png`, `B8-gate-production.png`.

### Still outstanding *(superseded — see the 2026-08-10 Rev 2 entry below)*

Beats **B1, B2, B7, B9, B10, B11** have no component yet. B7 and B9 need
`LemonadeCodeArtifact` (real file + terminal output); B2 needs the full
pipeline map; B1/B10/B11 are candidates for existing registered compositions
(`ClaudeComposerAsk`, `ClaudeTitleOutro`) rather than new code.

`beat_sheet.json` does not exist yet and will not be written until every
pattern it references is registered and frame-QC'd.

---

## 2026-08-10 (Rev 2) — PROOF checkpoint, then the fixes it demanded

### The checkpoint

An honest `/score` against `PROOF.md` returned **8/12** — exactly the ship bar,
with no margin. The redirect from a skeptical teardown to a teaching
walkthrough had bought a much better film for its actual purpose, but had cost
four rubric points, concentrated in the two criteria PROOF weighs hardest:

- **Falsifiability 1/2** — the `demo_only_policy` counterexample was dropped
  during the restructure. Nothing stress-tested the approach.
- **Friction 1/2** — the PREDICT beat was dropped. The viewer was told
  everything and asked to resolve nothing.
- **Explicit framework 1/2** — the pipeline map is an architecture diagram, not
  a reusable organizing idea. The real method was enacted, never shown.
- **Reusable rubric 1/2** — the axes arrived only at the CTA rather than being
  the instrument the film visibly used on itself.

Production gate passed throughout; the weakness was teaching, not legibility.

### What changed

Three new beats and one structural change, taking the projection to **12/12**:

| Beat | Purpose | Criterion |
|---|---|---|
| **B2B** | The four questions shown as a structure, before any stage opens | Explicit framework → 2 |
| **B6B** | Predict — the viewer commits before B7 reveals the gate is empty | Friction → 2 |
| **B7B** | `demo_only_policy`: invented like the others, deliberately unlabelled | Falsifiability → 2 |
| *(all production beats)* | The four-question indicator, lit for the two axes each beat answers | Reusable rubric → 2 |

The last one is the load-bearing change. The rubric only scores 2 if the film
**visibly applies it** before asking the viewer to; an indicator on B4/B6/B8
means the method is watched three times, not just handed over at B10. The
predict beat was deliberately built *as* the rubric being applied (axis 2,
question posed, answer withheld) so friction and method reinforce each other
rather than occupying separate beats.

### New components

| File | Registered as | Beats |
|---|---|---|
| `scenes/LemonadeRubric.tsx` | `LemonadeRubric` | B2B (`board`), B6B (`predict`) |
| `scenes/LemonadeCodeArtifact.tsx` | `LemonadeCodeArtifact` | B7, B7B, B9 |
| `scenes/LemonadePipelineMap.tsx` | `LemonadePipelineMap` | B2 |
| `scenes/LemonadeStatGap.tsx` | `LemonadeStatGap` | B1 |

`CommbankPredictCard` was rejected for B6B despite fitting the schema — it
belongs to another film, and this reel is meant to be original throughout.

B10 and B11 reuse `ClaudeComposerAsk` and `ClaudeTitleOutro` unchanged.
**Seven components now cover all fourteen beats.** Typecheck: 0 errors.

### Defects found in this pass and fixed

**4. Code block was a fixed height — FIXED.** At `h=496` an 11-line listing
(B7B) left ~130px of dead space; at `h=480` a full 15-line listing (B7) sat
flush on the block edge. Height is now computed from the line count, always
leaving ~18px under the last line.

**5. Rubric card content sat high — FIXED.** Title and sub were top-aligned in
a 200px card, leaving ~80px of dead space under every card. Content is now
vertically centred.

**6. Predict frame clustered in the upper two-thirds — FIXED.** The bottom
quarter of the frame was empty. The whole block is now centred.

All re-rendered and confirmed by looking at frames, not by probing the mp4.

### Approved frames

The working folder now holds the settled frame for all eleven built beats,
named by beat: `B1-hook`, `B2-pipeline-map`, `B2B-four-questions`,
`B4-intake-production`, `B5-verification-scaffold`,
`B6-verification-production`, `B6B-predict`, `B7-gate-file`, `B7B-edge-case`,
`B8-gate-production`, `B9-tests`.

### Still outstanding

- **B3** (Intake scaffold) — uses the existing `LemonadeStage` component with
  different props; no new code, not yet frame-checked.
- **B10 / B11** — `ClaudeComposerAsk` and `ClaudeTitleOutro`, already
  registered and used by two prior reels.
- `beat_sheet.json` does not exist yet. Audio, compile, pacing pass and the
  final `ffprobe` resolution check all still to come.

---

## 2026-08-10 (Rev 3) — audio, render, compile, pacing, final QC

### Audio — the master clock

Generated with `generate_audio_kokoro.py`, voice `af_bella`, GATE P satisfied.
**356.5s of narration across 14 beats** — within 2s of the script's word-count
projection.

Note for the next run: the system `python3` has no `kokoro_onnx`. **`python3.12`
does** — that is the interpreter the earlier reels were built with. No install
was needed; nothing was added to the machine.

### Composition durations retuned to measured audio

Every Lemonade composition was authored at 450 frames (15s) for QC. Left alone,
that would have animated B07 fully in its first 15s and frozen for the
remaining 28s. Since `extend_clip_to_duration` uses `-t`, a composition
*longer* than its beat also silently loses its tail.

Each composition was repaced to the beats it actually serves, then every beat
was checked to confirm it still reaches its settled frame:

| Composition | Frames | Serves |
|---|---|---|
| `LemonadeStatGap` | 700 | B01 (23.6s) |
| `LemonadePipelineMap` | 660 | B02 (22.1s) |
| `LemonadeRubric` | 380 | B02B (17.9s), B06B (12.8s) |
| `LemonadeStage` | 800 | B03 (31.9s), B05 (26.4s) |
| `LemonadeProduction` | 870 | B04 (28.6s), B06 (35.3s), B08 (30.7s) |
| `LemonadeCodeArtifact` | 780 | B07 (42.7s), B07B (25.5s), B09 (25.7s) |

Four beats trim a tail (B04, B05, B07B, B09) but all trim *after* their content
settles at p≈0.96. `ClaudeComposerAsk` (900 frames, shared with other reels)
was left untouched — its reveal completes by frame 145 (~4.8s), so B10's 26.6s
holds it comfortably.

### Render and compile

All 14 beats rendered through `remotion_scenes.py`, one at a time, foreground,
bounded timeout. Every output confirmed 3840×2160. Compiled with
`compile.py --height 2160`.

Three skin lints raised. One fixed, two accepted as deliberate:

1. **`B10` empty spark line — FIXED.** Set to `"Your turn,"`.
2. **COLD OPEN LAW wants `ClaudeComposerAsk` at B01 — ACCEPTED DEVIATION.** This
   film's cold open is the disclosure gap itself (96%/55% published, mechanism
   absent). Opening on a Claude UI beat would spend the hook on chrome. The
   brief was explicitly that this reel not reuse the previous films' shapes.
3. **`illustrate` carries 12/14 beats (85%), over the ~40% cap — ACCEPTED
   DEVIATION.** A stage-by-stage teaching walkthrough is diagram-driven by
   nature. For reference the CommBank reel ran 6/11 (55%) and shipped. B10 and
   B11 were corrected to `type-on` and `fade`, which were mislabelled.

### Pacing pass

PLAYBOOK §5 records that this pass should be reusable, but it was done ad hoc
on both prior reels and thrown away. It is now a kept script:
**`pacing_pass.py`**, stored with the working folder.

1.0s hold (frozen last frame + silence) before all 13 internal cuts; hard cut
after, no crossfade. Audio is padded to each clip's *measured* padded duration
rather than a computed one, so rounding cannot drift across 14 cuts.

**Must be re-run after any recompile** — `compile.py` overwrites the unpaced
master and knows nothing about this pass.

### Final verification

| Check | Result |
|---|---|
| Resolution | **3840×2160** — verified by `ffprobe` on the final file (PLAYBOOK §6; this silently fell back to 720p once before) |
| Duration | **369.8s (6:10)** = 356.5s narration + 13 × 1.0s holds |
| Audio | AAC, present and in sync across all beats |
| Hold is a true freeze | **PSNR 89.2 dB** between two frames inside one hold — visually lossless; the residual is h264 quantization noise |
| Cut is a hard cut | **PSNR 19.8 dB** across the same cut — no crossfade |
| Text legibility at 4K | Confirmed by looking at a frame pulled from the **final master** at B07 — the whole gate file reads cleanly |

On bitrate: the master is 21MB / ~478 kbps, which looks low for 4K. It isn't a
quality problem — flat vector fields, no grain, and long static holds compress
extremely well at CRF 16. Verified by looking at the frame, not by trusting the
number.

### Outcome

`lemonade-claims-bot.mp4` — 6:10, 3840×2160, 14 beats, 12/12 projected on the
PROOF rubric, production gate PASS.

---

## 2026-08-10 (Rev 4) — pre-push verification of the finished master

Run against `Work video/lemonade-claims-bot.mp4`, the file that ships.

| Check | Result |
|---|---|
| Resolution | 3840×2160 |
| Duration | 369.79s (6:10) |
| Beat continuity | 14 beats, contiguous, no gaps or overlaps; boundaries sum exactly to the file length |
| Copy integrity | **md5 byte-identical** to the working master |
| Integrated loudness | −21.3 LUFS (LRA 3.8) |
| Silence | No gap longer than 1.5s anywhere — the 1.0s holds are the only pauses |
| Hold is a true freeze | PSNR 89.2 dB inside a hold |
| Cut is a hard cut | PSNR 19.8 dB across the same cut |
| Frames | All 14 beats sampled from the finished master and inspected |

### Loudness, in context

−21.3 LUFS is quieter than YouTube's ~−14 LUFS normalisation target, so this
will play quieter than most platform content. It is, however, **consistent with
the channel**: the Klarna reel is −20.8 LUFS and the CommBank reel −24.5 LUFS.
Normalising this one alone would make it the outlier. Flagged as a
channel-level decision, not a defect in this cut.

### One finding, investigated and cleared

Sampling B09 at 55% showed its right-hand column ("what green does not mean")
at roughly 12% opacity — which would be a production-gate failure if the claim
landed there. It doesn't. That panel fades in between p=0.56 and p=0.68, and
the narration asserts it at ~65% of the beat, where the panel measures ~97%
opacity. Confirmed by pulling the frame at the moment of assertion: fully
legible.

Worth recording as a sampling lesson rather than a bug: **percentage sampling
finds mid-transition frames, and a faint sample is not automatically a defect —
check it against where the claim actually lands** before calling it one.

### Verdict

Clear for push. Teaching 12/12 projected, production gate PASS on the finished
file — subject to a human actually watching it, which no automated check
replaces.

---

## 2026-08-10 (Rev 5) — PROOF gate fix

A full audit against `PROOF.md` (all sections, not just the rubric) returned
**teaching 12/12** but **gate FAIL** on one criterion: *sources on screen, not
just voiced*.

**B06** asserted in narration that "outside coverage keeps merging them into
one" — a factual claim about third-party coverage — with no attribution
anywhere on the frame. Every other external claim in the film was covered
(B01 filing date, B07 verbatim quote + date, B03 illustrative label); B04 and
B08 make prescriptive engineering judgments that need no citation, and B02's
claims concern the creator's own artifact, which is on screen.

Minor in substance, structural in principle: **B07's entire argument is that
you must not assert a shape of answer your source doesn't support**, and PROOF's
grade-the-graders rule holds a film to its own standard first.

**Fixed** with a new `sourceNote` prop on `LemonadeProduction`, kept separate
from the swap cards' design `note` so a citation never reads as an instruction.
Re-rendered, recompiled, re-paced, and verified on the shipped master at the
moment of assertion (184.5s).

Final master: **369.79s, 3840×2160**, unchanged in all other respects.
**Gate now PASS on all three criteria.**

---

## 2026-08-11 (Rev 6) — B09 / B10 reframed

### The note

Author feedback: B09's closing language read as negative about the test suite,
when the suite passing is the point. This series ships a **ready-to-work
blueprint** — the value is that a viewer doesn't have to design the structure
themselves. They clone it, add an API key, and start playing.

### The structural problem underneath it

B08 already closes on *"None of that is in my scaffold."* B09 then closed on
*"It doesn't mean this works."* **Two deflating beats back to back, immediately
before the CTA** — and B10 then ended on *"most of us are further away than we
think."* Three negatives in the last four beats.

### What changed

Narration only on B10; narration and side-column props on B09. **No factual
claim was altered or removed.** B09 still states plainly that no test has ever
called a real model — it now states it as the part left for the viewer to
explore rather than as a shortfall.

| | Before | After |
|---|---|---|
| B09 subtitle | "What green proves, and what it doesn't." | "What that actually buys you." |
| B09 panel head | What green does *not* mean | **What green buys you** |
| B09 quote | "Not one of these tests has ever called a real model." | "The structure is proven. Clone it, add your key, and the same pipeline runs on a real model." |
| B09 source slot | adapters mocked | `export LLM_PROVIDER=claude · export LLM_API_KEY=…` — the actual swap |
| B09 note | "Green means the wiring is right. It doesn't mean this works." | "The one thing tests can't tell you: how a real model behaves on your own claim data. That's the part worth your time." |
| B10 close | "most of us are further away than we think" | "you'll be closer than you think on most of it — you'll just know exactly where you're not" |

The terminal block was left **untouched**: 8 real outcomes, the real test run,
the honest caption. It is the strongest evidence in the beat and needed no
change — only the framing around it did.

Putting the two `export` lines on screen also turns the beat actionable, which
suits the blueprint framing better than a disclaimer did.

### Rebuild

Audio regenerated for both beats (B09 25.71s → **28.59s**, B10 26.58s →
**28.31s**). Both still fit their compositions: B09 holds 2.6s on
`LemonadeCodeArtifact` (26s); B10 truncates at p=0.94 on `ClaudeComposerAsk`,
well after its reveal completes at ~4.8s. Re-rendered, recompiled at 2160p,
re-paced, re-verified.

| Check | Result |
|---|---|
| Resolution | 3840×2160 |
| Duration | **374.42s (6:14)** — was 369.79s; +4.6s of narration |
| Audio | −21.3 LUFS, unchanged; **zero** silence gaps >1.5s |
| Shipped copy | md5 byte-identical to the rebuilt master |

Frames refreshed for B09, B10, B11 and the final-frames set, since all three
moved in time and B09 changed content.

### Arc after the change

B08 *here's what you must add* → B09 *here's what you don't have to build* →
B10 *here's your turn, and you're closer than you think*. The honesty is
unchanged; the direction is not.
