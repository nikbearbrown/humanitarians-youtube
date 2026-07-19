# Chapter 7 — From Chapter to Lecture

## Overview

The reels side of the book turns a story into a film. This chapter turns a *chapter* into a lecture — a narrated, captioned video where one slide is one narrated beat, and where the voice teaching you is the author's own. It is the highest-value use of the whole system for anyone who writes to teach, because it takes the artifact you already have — a Markdown chapter — and walks it, without ever re-explaining itself, to a finished `lecture.mp4`.

The engine is three skills run in order, and the order is again the lesson. **`lecture-assets` builds a pool of candidate visuals. `slide-deck` selects from that pool into a deck. `deck-lecture` turns the deck into narrated video.** Each stage writes files to disk that the next stage reads. Nothing is re-derived between them, because they all speak the same two schemas you have already met: `assets.json` for the visual inventory and `beat_sheet.json` for the timed narration.

Notice the shape. The first stage over-generates on purpose and forces nothing. The second stage is where a human commits to a structure and, crucially, to the speaker-notes. The third stage never estimates timing — it measures narrated audio and lets that be the master clock, exactly as the reels pipeline locks audio in Chapter 3. The same laws govern both halves of Unreal Reels; only the surface differs.

There is a single human gate that matters more than all the others, and it lives early, in stage two. Everything downstream — the narration, the captions, the render — grows from the speaker-notes you approve there. Fix the lecture in the plan, not in the video. This chapter shows you all three stages, then walks the real fairness-metrics lecture that was built, rendered, and published through them.

## Stage 1 — `lecture-assets`: build the pool

The first stage reads `chapter.md` and produces a deliberately over-generated pool of candidate visuals under `lectures/<chapter>/assets/`. The rule is one sentence long: **breadth now, selection later.** Every asset enters the manifest tagged `candidate`. You never bend a chapter to use an asset, and you never require an asset to appear. An unused figure is inventory, not waste — it is still yours for an article, a Substack post, a slide somewhere else.

Four kinds of thing land in the pool, and they arrive in a sensible order. First, the book's own figures are imported (`import_book_figures.py`) — pre-vetted, on-brand, and free. Then cajal scans the chapter and writes a figure-intelligence report, from which the strong diagrams — Venns, partitions, timelines — are rendered as colorblind-safe SVGs under `svg/`. ✅ Then, for every quantitative claim, a live D3 chart is authored as a *drawer* under `charts/` via `new_chart.py`: a self-contained function that draws into a mount, plus a standalone HTML page derived from it. One chart, two artifacts, always in step. ✅ Finally scout mines the chapter for doodle-worthy moments and records each as a candidate note — a concept and a one-line sketch — for stage three to animate later, not now.

The reason the drawer format is worth the discipline is that stage two folds each drawer straight into the deck as live D3, with no nested iframes. So the pool authors charts in exactly the shape the deck can absorb. Everything is written to `assets.json` through `add_asset.py`, and every asset must pass the honesty gate before it joins: colorblind-safe, zero-baseline, one accent color, one idea per figure. This stage's only job is to fill the pool. It does not decide the lecture.

## Stage 2 — `slide-deck`: select into a deck

The middle stage is where the lecture actually gets its spine. It reads `chapter.md` plus the stage-one pool and emits a single brutalist `.dc.html` deck — the exact dialect stage three will parse. It runs in four phases with exactly one human gate.

**Phase 0, plan.** `build_plan.py` slices the chapter into an ordered `deck_plan.json` and seeds each slide's speaker-notes from the prose. This is where you stop. A regex can cut a chapter into slides; it cannot summarize or motivate. **You review and rewrite the plan — above all, the speaker-notes.** This is the gate that governs everything, because those approved notes become the seed the entire narration expands from in stage three. Emitting nine hundred lines of HTML afterward is mechanical; deciding the structure and the notes is the work. It is the cheapest place in the whole pipeline to fix anything, so fix it here.

**Phase 1, bind.** `bind_assets.py` matches chart and figure slides to pool assets and prints a gap report — what bound, what is missing, what candidates went unused. It is advisory and never stops; a gap simply routes back to stage one instead of getting faked.

**Phase 2, emit.** `emit_deck.py` renders the plan through the **nine archetypes** — `title · section · statement · concept · equation · example · chart · figure · close` — copies the runtime and design system, and folds each chart's drawer into the deck's script registry as live D3.

**Phase 3, verify.** `verify_deck.py` audits statically: every slide parses, every slide has non-empty speaker-notes, no blue anywhere, every equation is valid KaTeX, every `data-chart` resolves to a registered drawer. It fails loudly. Two attributes are load-bearing and never placeholders — `data-label` (the beat's identity) and `data-speaker-notes` (the narration seed). A blank note is a silent slide.

## Stage 3 — `deck-lecture`: narrate the deck

The last stage turns the deck into video, and it is governed by the same clock as everything in this book: **audio is the master clock.** Narration is generated and measured first; each slide's screen time is its real spoken duration plus a breath. Timing is never estimated from word count.

But the rule that makes a lecture worth watching is the second one: **discuss, don't read.** The narration is not the slide's text spoken aloud. Each beat's script *expands* the slide's speaker-notes into natural spoken teaching voice — it motivates and connects what the slide shows, while the slide carries the formal statement and the voice carries the understanding. This is enforced, not merely hoped: a discuss-don't-read guard computes the token overlap (Jaccard over content words) between the narration and the on-slide text, and flags any beat above roughly 0.6 as "probably reading the slide." Rewrite those.

The phases follow the clock. **Extract** parses the deck into `beat_sheet.json`, one beat per slide. **Script** fills each `narration_text` by expanding the notes — and here is the second gate: **approve the scripts before spending any audio.** A short TTS clarity pass respells rare names into a TTS-facing field only, so captions keep the correct spelling. **Audio** generates one voice-clone MP3 per beat via ElevenLabs and writes back the measured duration (✅ swap in a local TTS if you want zero cost; only the durations must be real). **Captions** use faster-whisper forced alignment — the words are already known, so it supplies only *when* each is spoken. ✅ **Visuals** ensure you never stare at static text for thirty seconds: each talky slide gets a doodle drawn on one line at a time, or hand-written summary bullets; chart slides stay live; equations earn a short tangent. Then **scaffold** the Remotion project, open Studio — and **stop.** The human scrubs every beat, confirms the audio lands and the captions track, and only then renders it themselves. Rendering is the most expensive step, so like every gate before it, it is never automatic.

## Worked example — the fairness-metrics lecture

Chapter 7 of a companion book, "Fairness Metrics," was walked through all three stages end to end. Stage one read the chapter and filled the pool: cajal drew the partition and Venn diagrams as SVGs, two quantitative claims became live D3 chart drawers, and scout logged doodle candidates like "demographic parity" for later. Stage two sliced the chapter into a plan of forty-seven slides across the nine archetypes; the author sat at the Phase-0 gate and rewrote the speaker-notes until each one motivated its slide rather than labeling it, then emitted and verified the `.dc.html` deck. Stage three extracted forty-seven beats, expanded each note into spoken teaching voice, passed the discuss-don't-read guard, cloned the author's voice for one MP3 per beat, force-aligned the captions, drew the doodles and bullets, and scaffolded Remotion. The author previewed every beat in Studio, then rendered it — about ten minutes of narrated, captioned lecture. It is published: youtu.be/5RZKbSXa-E8. One Markdown chapter went in; a lecture you can watch came out, and the voice teaching it is the author's own.

## Exercises

**Exercise 7.1 — Fill a pool without forcing it.** Run stage one over one chapter of your own. Report how many candidates landed in each bucket — book figures, SVGs, chart drawers, doodles — and name one candidate you expect the deck will *not* use, plus where else it could live. (Artifact: your `assets.json` counts + the one "inventory" asset and its second home.)

**Exercise 7.2 — Rewrite one speaker-note at the gate.** Take a single slide from a generated `deck_plan.json` and rewrite its `data-speaker-notes` from the regex-seeded starter into a note that *motivates* the slide. Explain in one line why fixing it here is cheaper than fixing it in the rendered video. (Artifact: before/after note + your one-line reason — it should name the narration seed.)

**Exercise 7.3 — Catch a slide being read.** Here is a beat: on-slide text "Demographic parity: P(Ŷ=1|A=0) = P(Ŷ=1|A=1)"; narration "Demographic parity means the probability of Y-hat equals one given A equals zero equals the probability of Y-hat equals one given A equals one." Score it against the discuss-don't-read guard and rewrite the narration to *discuss* the equation instead of reciting it. (Artifact: your judgment on the overlap + the rewritten narration.)
