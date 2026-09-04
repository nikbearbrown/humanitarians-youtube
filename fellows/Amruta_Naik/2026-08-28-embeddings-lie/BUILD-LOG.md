# BUILD-LOG — embeddings-lie

Built with `ai-explainer` from `stem_beat_sheet_embeddings-lie.json` (Downloads).
Free path only: Kokoro `am_onyx` (local), Remotion, ffmpeg. No paid API call, no
Higgsfield beat, no key required. Cost: $0.00.

## Decisions and corrections applied to the incoming beat sheet

1. **`estimated_duration_s` was a blank string `" "` on B03 and BVDT.**
   `remotion_scenes.py` calls `float(estimated_duration_s)` when no measured audio
   duration exists yet, so a blank string would raise `ValueError` and drop both
   beats to slates. Set to word-count estimates: B03 → 24s, BVDT → 21s. These are
   estimates only — the Kokoro MP3 durations written back as `actual_duration_s`
   are the master clock, per audio-first doctrine.

2. **B03 `ClaudeCodeBeat` had no `sparkLine`.** It would have rendered the
   component default `The code speaks.` — generic, and not this beat's idea. Set to
   `Words, not logic.` (SPARK-LINE LAW: one short serif line, <=4 words, the
   narration's key line compressed).

3. **Fixed templates used for the verdict and the outro**, as requested:
   `ClaudeVerdictArtifact` (BVDT) and `ClaudeTitleOutro` (BOUT), both taken as
   shipped from `runtime/remotion/src/scenes/`. No retint, no prop schema
   extension, no local scene override. This is what makes the reel gate-clean
   without a custom `scenes.py`.

Nothing else in the authored sheet was changed. Narration text, greeting
(`Hello Amruta`), topic strings, output lines, and the title are as authored.

## Violations carried, not silently passed

### 1. FALSIFIABILITY beat missing (teaching-arc item, ✗)

The arc checklist wants a beat that stress-tests the thesis. This sheet has none —
it moves B04 (consequence) straight to BVDT (verdict). The sibling reel
`rag-silent-failure` has one (`BEDGE`, "does more compute fix this? No").

**Why it was carried rather than fixed:** adding a falsifiability beat means
authoring new narration and a new visual, which changes the video the author
wrote. That is the author's call, not the builder's. The reel is complete and
watchable without it; the arc item stays marked ✗ in CHECKS-REPORT.md until the
author decides.

**If it should be fixed,** the natural beat sits between B04 and BVDT: *when is
similarity enough?* — it genuinely is, for fuzzy dedup, clustering, and
first-pass recall where a human or a reranker checks after. Naming where the tool
works is what makes the "it lies" claim falsifiable rather than a slogan.

### 2. ILLUSTRATE LAW smell — composer-heavy beat mix

Five of eight beats render `ClaudeComposerAsk`: B00, B01, B02, B04, BHTF. The law
reserves the Claude UI for beats where the UI is the subject — the cold open, ask
micro-beats, the verdict, the handoff, the outro — and asks every other inner beat
to ILLUSTRATE its concept. B01, B02, and B04 are inner concept beats wearing UI
clothes, and B01→B02 are consecutive beats sharing one scheme, which the law names
as "the smell".

**Why it was carried rather than fixed:** rebuilding three beats as concept
illustrations means writing new Remotion scene source, which is a re-authoring of
the reel's visual design, not a render fix.

**If it should be fixed,** B02 is the strongest candidate and the cheapest: the
cat/mat contrast is a textbook *divergence* — two things that look identical
splitting apart — which the rhetorical-pattern library already covers. B04's
retrieve-then-answer chain maps onto `SourceFlow` from
`runtime/remotion/src/illustrations/`. Both are prop changes to existing
components rather than new motion math.

## Machine gates

Gate results for this build are recorded in `_qc/REPORT.md` (GATE V) and the
`./art run` console output. GATE F (paperwork) does not arm: the reel has no Manim
beats, so nothing was pending render. GATE L (beat-mix lint) and GATE SHAPE run
regardless.

## Never published

Output stays in this folder. No upload machinery was invoked.
