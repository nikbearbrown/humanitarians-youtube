# BUILD-LOG — gemma4-unified

Started 2026-08-02. Brief: *"a short video on Gemma 4, the open-source any-to-any
model, and how the model does what it does. Misconception is you assume generator
and discriminator models need different arch but the arch seems to be
converging."*

**Status: DELIVERED (revision 5).** Reviewed against `PROOF.md` — see
`PROOF-REVIEW.md`. Teaching **10/12 → 12/12**; production gate **FAIL → PASS**.

## Revision 5 (2026-08-05) — full regression verification

Every fix made across revisions 1–4 was re-verified against the **current**
compiled master, not against the changelog, because these scenes were edited
repeatedly and a later edit could have silently reverted an earlier fix.

Automated: 3840×2160 h264 + AAC, 181.80s · 12/12 beats all `VIDEO`, no slates ·
all 12 clip durations match measured audio (0 mismatches) · stale-string scan for
`NikBearBrown` / `Sawubona, Liam` / `next beat` / `Say it out loud` returns 0 ·
GATE V 24 frames, 0 BLOCKER / 0 MAJOR.

Visual: read a settled frame from all 12 beats in the compiled master and
confirmed each earlier fix holds — name/size collision, the TEXT-lane dash, the
decoder subtext, strike-through scoping, the `was 550M` carry-forward, footer
safe-area clearance, the sliced parameter chips at B07, WER label crowding, the
predict question clearing the rule, the reworded commit line, verdict card fill
and its source line, the B09 footer and its three citations, and the handle on
B00/B10/B11.

**Placeholder question resolved:** the `B00 GRAPHIC VIDEO 0.0s +10.8s` plate the
user saw exists only in `gemma4-unified-slate.mp4`. Swept 39 timestamps across the
whole runtime of both files: the master has the plate on **0/39** frames, the
slate on **39/39**. The master was never affected.

**One real inconsistency found and fixed:** B00 still greeted `Sawubona, Liam`
while B01 introduces the presenter as Ritik and the channel is `@HumanitariansAI`
— a leftover of the nbb persona. Now `Sawubona, Ritik`. Visual only (the greeting
is not spoken), so no new audio; runtime unchanged at 181.80s.

## Revision 4 (2026-08-05) — PROOF review + source fixes

Self-assessed against the PROOF protocol by sampling frames at each claim moment.
The gate **failed** on sources-on-screen: B01–B04 asserted every parameter figure
and B09 asserted the Platonic Representation Hypothesis (and that it is contested)
with no citation visible at the moment of assertion. For a reel whose own rule is
"no source, no verdict," that is self-refuting and vetoes public on its own.

Fixed, all cheap edits to the existing cut:

1. `GemmaEncoderStack` + `GemmaExecSummary` gained a `sourceNote` prop —
   `arXiv:2607.02770 · Gemma 4 Technical Report`, on the header line of B02–B04
   and beneath B01's cards, live for the whole beat.
2. `GemmaConvergenceThread`: `arXiv:2405.07987` beside the hypothesis and
   `arXiv:2604.18572` beside "and contested" — each citation on the same line as
   the claim it backs, not in a footer. Model chips labelled `pointers only`.
3. B01's roadmap relabelled from an agenda to three reusable **questions**
   (WHAT WAS REMOVED? / WHAT DO THE NUMBERS SAY? / WAS THE TEST CONTROLLED?).
   This is what moved *Explicit framework* and *Reusable rubric* from 1 to 2 —
   the film now hands over axes instead of only demonstrating them. No narration
   change, so no new audio.
4. B10 gained an answer key so a viewer can tell whether they ran the task right.

**Still open, and named rather than hidden:** every figure is redrawn rather than
shown from the source page (the one real [RESHOOT]), and the narration never tells
the viewer the three questions are reusable — that lives only in on-screen text.

**Root pattern worth fixing at the toolkit level:** sourcing was strong exactly
where a source was *built into* the scene (B06/B07 header, B08 card) and absent
everywhere it wasn't. It was a per-scene afterthought, not a contract. A shared
source lower-third that every claim beat takes as a required prop would make an
unsourced beat impossible to ship.

**Status (revision 3).** GATE P signed by the user 2026-08-03.
Master is `gemma4-unified.mp4` — **181.80s (3m02s)**, 3840×2160 @ 24fps, AAC
mono 24kHz, **12/12 beats**, **GATE V clean (24 frames, 0 BLOCKER / 0 MAJOR)**,
$0.00. Never published, per law.

## Revision 3 (2026-08-03) — channel handle

Handle changed from `@NikBearBrown` to `@HumanitariansAI` everywhere it appears:

- **B00 and B10** composer footer chip. `ClaudeComposerAsk` *defaults*
  `folderLabel` to `@NikBearBrown`, so both beats were inheriting it silently.
  Set explicitly in this reel's props rather than editing the shared scene, which
  other reels depend on.
- **B11** outro `handle` prop.
- **B11 narration — this one is spoken**, so it needed new audio, not just a
  re-render: "Gemma four, unified. Nik Bear Brown." → "…Humanitarians A I."
  (3.43s, up from 2.99s; runtime 181.36 → 181.80s).
- `metadata.voice` → `HumanitariansAI`; the `Nik Bear Brown` tag → `Humanitarians AI`.
- `metadata.voice_env` (`ELEVENLABS_VOICE_NIKBEARBROWN`) **removed** — it named a
  paid engine this toolkit forbids, and nothing under `runtime/` reads it, so it
  was dead config still carrying the old name.

Note `metadata.channel_title` is a *different* mechanism (compile.py burns it in
at the bottom of the first beat only) and is unused here — the handles the viewer
sees are the in-scene props above.

**Left unchanged, deliberately — flag for the user:**
- B00's greeting still reads `Sawubona, Liam`. "Liam" is the nbb persona name, and
  B01 introduces the presenter as Ritik, so the identity is now mixed. Renaming a
  presenter was outside the request.
- Voice is still Kokoro `am_onyx` (Onyx). The toolkit's convention pairs the
  `@HumanitariansAI` channel with the `hai` persona and `af_bella` (Bella).
  Switching would mean re-recording all 12 beats.

Correction to an earlier claim in this file: the **first** cut (11 beats,
161.93s) did **not** pass GATE V — it reported `frames=22 BLOCKER=0 MAJOR=4`,
four underfill defects across B04 and B07. That cut was pushed to the repo
before the failure was addressed. Revision 2 fixes those defects and adds the
executive summary; see below.

## Revision 2 (2026-08-03, after review of the first cut)

1. **Added B01, an executive summary** ("Hi, I'm Ritik, and this video is
   about…"), at the user's request. New scene `GemmaExecSummary.tsx`: presenter
   line, the thesis in one sentence, and a three-card roadmap of what the reel
   does — an advance organizer. Beats after it renumbered B02–B11; existing
   media and mp3 files were **renamed rather than re-rendered**, so only the new
   beat needed generating.
2. **Reworded the 1:07 line.** It was not a placeholder — it is the PREDICT beat
   asking the viewer to commit before the reveal — but it said "before the next
   beat", and "beat" is production jargon a viewer has no reason to know. Now
   "Pick an answer before you watch the scores."
3. **Fixed the two GATE V underfills.**
   - **B05 (PREDICT)** was genuinely broken, not merely sparse: at 62px inside
     1000px stage units the question ran to three lines and collided with the
     terracotta rule fixed at stage y=450. Shortened the question to two lines
     and added `eyebrow` + `options` to `PredictCardBeat` — WORSE / NOT WORSE
     chips. A prediction beat needs something to commit *to*, so this fills the
     dead lower third with the thing that was missing rather than with padding.
   - **B08 (VERDICT)** had ~250px of empty card below line 3 from a forced
     `minHeight`. Added an optional `sourceNote` prop and put the citation on the
     card's face — "no source, no verdict" made literal — plus larger type
     (heading 54→60, lines 32→36) and `minHeight` 620→700.

Worth recording: the white card (`#FFFFFF`) on the cream stage (`#F2F0E9`) is
only 22 per-channel apart, under the `INK_DELTA = 28` that
`runtime/qc/final_frame_check.py` counts as content — so a card-based scene's
measured fill is driven by its *type*, not by its card. Filling such a beat
means adding real content, not enlarging the container.

## Two premise corrections (see FACTCHECK.md #23–#27)

The brief contained two claims the sources do not support. Both are logged as
REJECTED in FACTCHECK rather than quietly dropped:

1. **Gemma 4 is not any-to-any.** It takes text, image, video and audio *in* and
   emits **text only** — no image head, no audio head. The phrase almost
   certainly comes from HuggingFace's `any-to-any` **pipeline name**, which
   describes arbitrary input modalities, not output.
2. **Gemma 4 is not an instance of generator/discriminator convergence.** It has
   no generative visual head and no discriminator. That literature exists
   (Chameleon, Emu3, Show-o, Transfusion, Janus, BAGEL) but Gemma 4 is not in it.

**Reframe kept instead:** Gemma 4 12B is evidence for a *different* convergence —
**encoder convergence.** Modality-specific perception front-ends are being
deleted and absorbed into the general decoder. That is countable, visual, and
what the technical report is actually about. The brief's original question is
still answered on screen, at B08, as an explicit correction plus a reading list.

## What the research turned up that changed the shape of the reel

- The 12B unified model **did not ship with the family.** Gemma 4 launched
  2026-04-02 with four encoder-based models; the encoder-free 12B arrived
  **2026-06-03**, two months later. So this is not a same-day side-by-side — it
  is Google going back and redoing the front end. Better story, and it is the
  reel's spine (B02: "two months later, Google shipped a fifth model").
- **The report never runs the controlled experiment.** MMMU-Pro has the
  encoder-free 12B at 69.1 against 76.9 for the 31B, and FLEURS ASR has it at
  0.067 WER against 0.075 for E4B. Both comparisons change parameter count *and*
  architecture at once, and Table 5 benchmarks the 12B against Gemma 3, not
  against its own siblings. That absence is the twist (B06) and the reason the
  verdict is "direction of travel, not result."

## Toolkit work this reel required

New Remotion scenes in `runtime/remotion/src/scenes/`, registered in `Root.tsx`:

- `GemmaEncoderStack.tsx` — the exhibit. Three input lanes into a decoder slab,
  three focus states (`specialists` / `vision` / `audio`). Deletions accumulate
  across beats rather than resetting, so B03 still shows the vision lane cut.
- `GemmaScoreboard.tsx` — MMMU-Pro and FLEURS side by side, `split` and
  `confound` states. The confound state is what reveals the parameter counts.
- `GemmaConvergenceThread.tsx` — the two-column reframe beat.

## Fixes applied

1. `GemmaConvergenceThread` — columns shortened 560→540px and the footer pulled
   up 34px. The last footer line sat at a 1024 baseline; title-safe bottom is
   y=1026 with a 7px margin (`runtime/qc/final_frame_check.py`), so descenders
   were on the edge and would have tripped an edge-bleed BLOCKER.
2. `GemmaEncoderStack` — footer moved up 14px for the same reason.
3. `GemmaEncoderStack`, after reading the rendered B03 frame:
   - the strike-through now only draws on the lane cut in *this* beat, and fades
     as the replacement label arrives. Previously a lane cut in an earlier beat
     kept a terracotta line running into its `35M` chip, which read as "the 35M
     matmul is deleted too"; and on the audio beat the line struck through the
     words "no encoder", which reads as the opposite of what it means.
   - a lane cut earlier now carries a `was 550M` ghost label for context.
   - the TEXT lane's size dropped its `—` placeholder (read as a minus sign).
   - decoder subtext `5:1 local·global attn` → `text · image · audio`. The
     attention ratio is verified (FACTCHECK #5) but PEDAGOGY.md explicitly cuts
     attention interleaving as extraneous load; leaving it on screen contradicted
     the reel's own pedagogy doc.
4. `GemmaEncoderStack` **text collision**, caught by reading the B01 frame: at
   36px the module name and at 58px the parameter count overlapped — "Vision
   Transformer" ran straight into "550M". Name 36→34px, size 58→52px, and the
   size now right-aligns inside a reserved zone so the two can't meet. Also
   shortened the TEXT lane note to fit the box.

Lesson repeated from `claude-debunked`: the mp4 probe said all three of these
renders succeeded. Only looking at the frames found the defects.

## Known toolkit flakiness hit again

`remotion_scenes.py` intermittently fails with **"Could not find composition with
ID X. Available compositions: CodexComposerAsk"** — `Root.tsx` partially
evaluates and only the first composition registers. Retrying the same beat
succeeds. This is the same failure the version pinning was supposed to fix on
`claude-debunked` (all three remotion packages are on exact 4.0.490), so pinning
was necessary but not sufficient. Worked around with a retry loop (up to 5 tries).

**Hypothesis tested and rejected:** that Remotion's 30s `delayRender` ceiling was
being exceeded while evaluating a 600-composition Root. Added `--timeout=180000`
to `remotion_scenes.py`; beats still failed and then succeeded on retry with the
flag in place. The flag is kept (harmless, arguably correct for this Root size)
but its comment now says plainly that it does not fix the flake.

**Better correlation, still unproven:** failures cluster on the first renders
*after* any edit to `Root.tsx` or a scene file — i.e. exactly when Remotion has
to re-bundle cold. Once a pass gets going, later beats mostly succeed on try 1.
This predicts the flake is a race on the cold-bundle path rather than anything
about composition count per se, and it explains why retrying works: by the second
attempt the bundle is cached. Worth testing by warming the bundle with one
throwaway render after any source edit.

## Post-audio work

**I clobbered the measured durations myself.** Audio was generated while a render
pass was still in flight. `remotion_scenes.py` does an unlocked read-modify-write
of `beat_sheet.json` per beat, so an invocation that had loaded the sheet before
the audio write saved its stale copy back over `actual_duration_s`. Caught it
because a clip reported "extended to 14.2s" when B00's audio is 10.84s.
`mp3/timings.json` still held the ground truth, so the durations were restored
from there rather than re-synthesised. **Never run the audio step concurrently
with renders.**

**Registered scene durations had to be reset against measured audio.** The three
custom scenes drive everything off `useP()` (`frame/durationInFrames`), so the
registered duration *is* the animation length — and `extend_clip_to_duration`
truncates a clip to its beat. Registered at 21s/24s/26s against beats of
15.17–25.02s, the animations would have been cut off at ~72% and never resolved.
Reset to at-or-under the shortest beat using each scene: 450f / 590f / 740f.
Verified the stock scenes were safe rather than assuming: `ClaudeComposerAsk`
types at a fixed rate (done by frame 63 ≈ 2.1s) and `ClaudeTitleOutro` only does
a 14-frame fade — neither scales with the registered duration.

Also: every measured beat came in shorter than its estimate, and compile.py
**center-cuts** clips longer than their beat (`LADDER_RETIME` ±5%, then cut). On
staged reveals that removes the setup and the payoff, so all 11 clips were
re-rendered against measured durations to leave compile with zero delta.

## GATE V: 4 MAJOR → 0

First compile failed with 4 underfill MAJORs, all in the two stock scenes. Both
were real defects, not metric artifacts — confirmed by reading the frames:

- **B04 `PredictCard`** — the question overflowed. The card's question sits at
  stage y=250 at 62px/1.2 inside 1000px and the terracotta rule is *fixed* at
  y=450, so anything past two lines collides with it. "Delete the vision and
  audio encoders. Does perception get worse?" ran to three lines and struck
  through the rule. Shortened to 44 chars, and added `eyebrow` + `options` to
  `PredictCardBeat` (both defaulting to empty, so other reels are untouched):
  WORSE / NO WORSE chips give the viewer something to actually commit *to* and
  fill the dead lower third. Chips were then moved from p=0.62 to p=0.26 — a
  mid-beat frame had no chips yet and still read 53%, and showing the options
  while the question is being asked is better sequencing anyway.
- **B07 `ClaudeVerdictArtifact`** — `minHeight: 620` forced dead space under
  three short lines. Note the card is `#FFFFFF` on the `#F2F0E9` stage: only 22
  per-channel, *under* the `INK_DELTA=28` in `runtime/qc/final_frame_check.py`, so
  the card body does not count as content and the bbox comes from the type and the
  shadow edge. Fixed by filling it rather than padding it: heading 54→60, lines
  32→36, minHeight 620→700, plus a new optional `sourceNote` prop that pins the
  evidence to the card — "no source, no verdict" made literal on the verdict beat.

## Advisory warning left standing (deliberate)

- `illustrate` carries 7/11 beats (63%) vs the ~40% MOTION.md cap. The reel's
  argument *is* a sequence of concept exhibits (encoder stack ×3, scoreboard ×2,
  reframe) and the ILLUSTRATE LAW forbids putting the Claude UI on those beats.
  Converting any of them to a UI or terminal language would break the stronger law.

## Cost

$0.00. Kokoro TTS, local Remotion renders, no API keys.
