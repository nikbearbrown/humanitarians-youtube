# PEDAGOGY — Dead Links, Live Redirects. (9:16 SHORT)
# Auditor: Claude Opus 5 | 2026-08-14
# GATE P — quality gate, not a cost gate (Kokoro audio is free).
# Human sign-off required below before generate_audio_kokoro.py runs.

## What this is
The 9:16 Shorts cut derived from `claude-hai-dead-links-live-redirects` (16:9,
278.4s). A Short is a **derivative cut, not a re-edit** (SHORTS LAW): beats were
cut, never re-authored, and every surviving beat reuses the parent's existing MP3.
**Exactly one line of new narration exists** — the rewritten outro, below.

## Cap check
Parent 278.4s → Shorts hard cap is 180s. Cut to **6 beats, ~100s (1:40)**,
comfortably inside the cap.

## The cut
Kept: **B00** (intro) → **B05** (the ask) → **B06** (the delete) → **B07** (the
404) → **B16** (outro, rewritten) → silent endcard 4.5s.

Dropped (10): B01, B02, B03, B08, B09, B11, B12, B14, B14F, B15.

Rationale: cli-explainer says the 9:16 ships a **single cycle** and points at the
16:9 for the rest. The kept cycle is cycle 2 — the one that goes wrong — because
it is the only self-contained story in the reel with a hook, a turn and a payoff:
*consolidate five duplicate files → they were redirect destinations → 404.*
Cycle 1 (the crawler) is setup with no turn; cycles 3 and 4 are resolutions that
only make sense once the trap has landed.

**This cut honours the full spine.** Unlike the video-1 Short, it has a genuine
OUTPUT beat: ASK (B05) → CODE (B06) → OUTPUT (B07). No deviation to accept.

## The one new line (the reason this gate exists)
`shorts.py` auto-rewrites the outro to name what was cut, and its generated text
was defective in the same way it was for the video-1 Short — truncated fragments
of dropped beats stitched into a sentence:

> *"That's the short version. The full video also covers Link rot on a real…,
> dead links, live redirects. and Two things make this more… — watch Dead Links,
> Live Redirects. for the whole story."*

Unreadable aloud. Replaced by hand with:

> "That's the trap. The full video covers the crawler that found the dead links,
> the fix that keeps the file and hides the row, and the middleware rewrite behind
> three new subdomains. Watch Dead Links, Live Redirects. The link is right below."

Verified accurate against the parent: the crawler is B02–B03, "keeps the file and
hides the row" is B08–B09, the middleware rewrite is B11–B12. Nothing claimed here
is absent from the long.

## Portrait handling — no centre cuts
All five content beats are REMOTION renders, so the ONDA CHECK rewired them to
portrait compositions rather than cropping (a centre cut chops code mid-word):
- B00, B05 → `ClaudeComposerAsk916` (existed)
- B06 → `ClaudeCodeBeat916` (added during the video-1 Short)
- B16 → `ClaudeTitleOutro916` (existed)
- B07 → **`FellowsPortalLayerStack916` — newly added** for this cut

Zero centre-cut media is used.

## Toolkit change made for this cut
`FellowsPortalLayerStack916` did not exist, and unlike `ClaudeCodeBeat916` it was
not merely a missing registration. `illustrations/structural.tsx` declares
*"1280×720 stage assumed — geometry is in those units"* and hard-coded `1280` when
centring the card stack, so the component could not compose on a 1080-wide canvas.

Changed `LayerStack` to centre on the **actual** stage width from
`useVideoConfig()`. On the 1280×720 reel canvas the value *is* 1280, so every
existing landscape render is unchanged. `IlluStage` and `SparkLine` were already
responsive and needed nothing.

B07's props carry portrait geometry (`cardWidth` 900, `top` 560, `rowGap` 235,
larger type) because the parent's landscape values — `cardWidth` 1040 on a
1080-wide frame, top-anchored at 120 — would have overflowed the frame and left
the bottom two-thirds empty.

**Unverified until render:** that geometry is arithmetic, not yet an inspected
frame. The QC pass must confirm all three cards fit, the caption is fully opaque,
and the stack is vertically balanced rather than crowded at the top. If it reads
wrong, the fix is the props, not the component.

## Beat-level notes
- **B07 keeps `durationInFrames: 587`** (19.58s × 30). The reveal curve is
  fractional, so a mismatch leaves the caption part-opaque — the defect that hit
  B01/B14F in the parent at 17% and 33% opacity.
- **B06** is a `git show --stat` diffstat; its longest line is ~57 chars and will
  wrap in portrait rather than clip, per the `ClaudeCodeBeat` portrait rule.
- **Endcard** now reads `@HumanitariansAI`, resolved from the parent's
  `metadata.channel_title`. The video-1 Short shipped a draft endcard reading
  `@nikbearbrown` before that default was fixed in `shorts.py`.

## Estimated runtime
~100s across 6 beats (incl. 4.5s silent endcard) — an output of the cut, not a target.

---

**VERDICT: PASS**