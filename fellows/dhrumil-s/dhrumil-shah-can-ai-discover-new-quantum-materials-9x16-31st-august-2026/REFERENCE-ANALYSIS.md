# REFERENCE ANALYSIS — 9:16 vertical cut

Three references informed this cut. None was copied.

## 1. The approved 16:9 master (`../Can-AI-discover-new-quantum-materials-16x9`)

This is the source of truth. Everything about the film's *content* comes from
it unchanged: narration, measured timing, scene order, on-screen copy, every
cited figure, the CLAIM framework, and both honesty disclosures.

What this cut inherits structurally:

- 24 fps, exactly 4320 frames, exactly 03:00.
- Ten numbered scenes with a persistent `NN / 10` marker.
- A persistent `SOURCE` plate on every scene.
- Audio-first construction — measured durations are the master clock.
- The presenter-labelled CLAIM framework, shown before any example.
- The same Claude palette and type stack.
- The same script set: sync, render, check, qc-stills.

What it deliberately does **not** inherit: any layout. Every scene was redrawn
against a 1920 px portrait column.

## 2. `mycroft-thesisguard-9x16` — the house portrait convention

The sibling Mycroft project established how this workspace does a 9:16 cut,
and this project follows it rather than inventing a second convention:

- **2160 × 3840**, not 1080 × 1920 — 4K vertical, matching the 16:9 cut's tier.
- `SAFE = {left: 120, right: 120, top: 170, bottom: 170}`.
- A `config/` directory with `video-config.json`, `render-config.json`, and
  `films-manifest.json`, plus a `docs/` directory with `VIDEO-SPECIFICATIONS.md`,
  `FILMS.md`, and `RENDERING.md`. The 16:9 projects keep a flat `.md` set; the
  9:16 projects use this split, and so does this one.
- Header split into two lines — presenter name at 80 px, film title at 120 px —
  because the portrait header row is too narrow for one combined line.
- Horizontal chains become vertical stacks with down-arrows; two-column
  comparisons become top/bottom stacks.
- Narration reused from the landscape project, never duplicated.

## 3. The supplied Mycroft reference video

Used only to understand the delivery format the creator works in: a 4K master,
three-minute runtime, editorial cream palette, thin bordered cards, one idea
per scene, progressive reveals, restrained motion, and a source tag that stays
on screen rather than flashing. Its narration, wording, layouts, and creative
assets were not reproduced.

## What this cut does differently from the Mycroft 9:16, and why

**No evidence images.** The Mycroft portrait cut re-crops captured notebook
screenshots for a vertical frame. This film has no screenshots to re-crop — it
cites published literature — so the portrait problem here is typographic
rather than photographic. The layout work went into stacking cards and
re-anchoring a chart label instead of choosing new crop windows.

**A taller chart rather than a narrower one.** The obvious portrait move is to
shrink a wide chart. That would have compressed the 1986–1993 cuprate cluster
to the point of illegibility. Instead the chart grew from 452 px to 860 px
tall, using the height portrait actually provides, and one label was
re-anchored to clear its neighbour.

**A stacked comparison that is still simultaneous.** Scene 08's side-by-side is
the film's hardest production-gate requirement. Rotating it to top/bottom
keeps both panels on screen together for 11.2 s. The axis of comparison
changed; the simultaneity did not — and that distinction is what keeps the
gate satisfied rather than merely re-argued.
