# Chapter 6 — Explainer

## Overview

An explainer is the strangest and most disciplined member of the Unreal Reels family. There is no cast to keep consistent, no cinematic frame to art-direct, no found-footage grit. There is a white page, a line being drawn, and a voice explaining one idea slowly enough that you can actually follow it. This is the MinutePhysics move: as the narrator says a thing, the thing appears — a curve, an arrow, a label — one new mark for one new sentence. The video is not illustrated *after* the explanation is written; the drawing *is* the explanation, unfolding in time.

That single constraint — **one narration line, one new drawn element** — is what makes the form teach. It is called progressive disclosure, and it is the whole trick. When everything appears at once, the viewer's eye scatters and the words wash over a static picture. When the picture accumulates in lockstep with the words, attention has exactly one place to go: the mark being made right now. You are not decorating a lecture. You are pacing a reader's attention with a pen.

The reason to build explainers this way, rather than reaching for stock footage or a generated montage, is that most concepts do not need to look impressive — they need to be *seen correctly*. A wavefunction that curves the wrong way teaches the wrong physics. A metaphor drawn loosely and honestly ("two electrons refusing to share a seat") teaches an intuition a photoreal render never could. And the whole thing can be made for free: clean SVG or code-drawn diagrams for the figures, a local text-to-speech voice for the clock. No vendor required.

This chapter uses two skills from the pipeline: **scout**, which mines a book for concepts worth animating and hands you review cards, and **bears-doodles**, which turns one approved card into the finished sketch video. You will scout a book, pick a candidate, and produce the beat sheet and audio for your own explainer. The image-prompt rule from Chapter 3 still holds, sharpened: labels and equations are overlays, never baked into art.

## Progressive disclosure: draw ON as you narrate

The governing rule of bears-doodles is one sentence equals one new visual element, no exceptions. A beat sheet enforces it by carrying, per beat, the *accumulated* scene state — everything on screen so far — plus the single new mark this beat adds. Nothing is redrawn; the page only grows. When a scene reaches five or six simultaneous elements, you cut to a fresh page (marked `[CUT]` in the script) so the viewer is never staring at clutter.

Two consequences follow. First, your script's sentences must be short and atomic — six to twenty words, each introducing exactly one idea. If a sentence smuggles in two new things, the beat cannot draw them both without breaking the rule; you split the sentence. Second, the *order* of drawing is the order of understanding. Hook first, then the mechanism in steps, then the synthesis — one idea per beat, building in a direction that matters. You are choreographing comprehension, not filling a timeline.

## The bears-doodles look

The style is deliberately plain: line art on a white background, tightly synced to a narrated voice. This is not a limitation to apologize for; it is the reason the form reads on mute and reads clearly. There are two visual registers. **Manim** renders anything where being *exactly right* is the teaching — curves, axes, boundary conditions, energy levels, equations as labels. It is code-drawn, pixel-precise, and free to render. **Doodle** renders the loose, napkin-art metaphors — a balance scale for a trade-off, a sun drawing itself in — where the shape is a vibe, not a measurement.

The honest deliverable is Manim plus voiceover, and that alone is a complete video. Hand-drawn doodles and SVG icons are optional overlays added on top *only when they help* — never baked into the master render, never blocking it. This matters for the free path: a video with zero generated art, all code-drawn figures and a local TTS voice, is still a finished explainer. The rule of thumb: if a wrong curve would teach wrong physics, it is Manim; if the shape is just a feeling, it is a doodle.

## Scouting a book with FIELD

You do not start an explainer by staring at a blank page hoping for a concept. You **scout**. The scout skill scans a book's chapters and writes candidate cards — one clean tension, one clean resolution each — into a `vids/` directory, scored and ranked. It produces the shortlist; the human picks. Its value is selectivity, not coverage: most chapter material does not belong in a short explainer, and the scout's job is to say so.

A good candidate answers five questions. I call them **FIELD**:

- **Focus** — the concept stated in one sentence. If you cannot, it is two videos.
- **Image** — the single central visual metaphor the whole video orbits. One drawable object that moves.
- **Exclusions** — what it will *not* cover: the derivation, the second example, the historical aside. Naming the rabbit holes is what keeps the video tight — as long as the concept needs and no longer.
- **Load** — the prerequisites. Keep it to two or three the viewer plausibly already has. More than that and the concept is too big to stand alone.
- **Drive** — the hook: the misconception it corrects, the "wait, what?" surprise, the violated intuition. This is the first beat and the reason anyone keeps watching.

A candidate that scores well on all five — a genuine surprise, an obvious visual, few prerequisites, a real payoff — is one you build soon. One that fails Focus (two ideas tangled together) or Exclusions (no clean edge) you either narrow to its one surprising slice or shelve. The scout writes the cards; you read the slate and choose.

## Manim versus Remotion-native doodles

A note on the seam, because it recurs. The figures — the taught content — are drawn in Manim, in code, for free and pixel-precise. Remotion's job is the *overlay*: titles, captions, and any label, arrow, or equation the viewer reads as text. This is the same division from Chapter 3, and the same reason: text belongs in a crisp vector overlay laid on top, never inside a generated or rendered image. Diffusion models render text as gibberish, and even a clean Manim figure is better labeled by a Remotion overlay you can restyle without re-rendering the scene. Keep the drawn mechanism and the read-it-as-words layer separate, and each stays editable on its own.

## Worked example

Start from the demo input at `examples/explainer-demo/`. Segment it into beats and set the clock:

```
python scripts/segment_story.py examples/explainer-demo/source.txt \
  --slug photosynthesis --title "Photosynthesis" \
  -o reels/photosynthesis/beat_sheet.json
```

This returns a beat sheet — one narrated unit per beat, ordered hook → mechanism in steps → synthesis, each with a `narration_text` and, initially, an empty duration. Read it against the one-sentence rule: any beat that introduces two new elements gets split. Then generate the audio (✅ with a local TTS), which narrates each beat and writes its real measured duration back into the sheet. Now every beat has a true length and the total is your runtime — before a single figure is drawn. From here, the Manim figures and the Remotion labels are both trimmed to that clock. You have done the segment-and-audio gates; the concept is set, the timing is honest, and the drawing can begin.

## Exercises

**Exercise 6.1 — Scout and pick.** Run the scout skill over a book or chapter you know. Read the candidate cards it produces and choose one to build. Write two sentences: why this candidate over the others, and which one FIELD element (Focus, Image, Exclusions, Load, Drive) is strongest. (Artifact: your chosen candidate card + your two-sentence pick rationale.)

**Exercise 6.2 — Segment and time a beat sheet.** Take your chosen concept, segment it into a beat sheet (hook → mechanism in steps → synthesis), and generate the audio to measure durations. Confirm every beat introduces exactly one new element; split any that break the rule. Report the beat count and total runtime. (Artifact: a `beat_sheet.json` with measured durations and one line per beat naming its single new element.)

**Exercise 6.3 — Sort the layers.** For three beats of your explainer, list what is *drawn* (the Manim/doodle figure) versus what is *overlaid as text* (label, arrow, or equation in Remotion). Catch any case where you were tempted to bake a word into the figure, and move it to the overlay. (Artifact: a three-row table — beat / drawn element / overlaid text — plus one line on what you moved.)
