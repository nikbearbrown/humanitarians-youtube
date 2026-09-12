# SHOTLIST — rescue-reinvented
# Typed work order per beat. Gate F open. Pass 1 (pre-audio-lock estimates).
# ai-explainer chassis (Claude bookends + all-self-generated body) — no
# pantry stills, no shopping list, no external asset dependency.

## OPEN — INTRO (B00)

B00 · ClaudeComposerAsk (Remotion)
  action: render → media/B00.mp4
  props: greeting="Hi,", command="claude \"help me understand how AI is
         actually helping animal shelters and rescues\"", output=[3 lines]
  show: composer types → running indicator → output lands. Plain ask-focused
        hook — self-intro lives in B00B, not here.
  status: RENDERABLE

B00B · Manim B00B_AgrimaIntro (scenes.py)
  action: render → manim/B00B.mp4
  show: presenter card — "Hi, I'm Agrima." + topic lead-in
  status: RENDERABLE

## BEAT 1 — the backdrop (B01)

B01 · Manim B01_TheBackdrop (scenes.py)
  action: render → manim/B01.mp4
  show: 2x2 grid — overcrowded kennels / staffing shortages / hard-to-recruit
        volunteers / donations that lag behind need
  status: RENDERABLE

## BEAT 2 — win #1 (B02)

B02 · Manim B02_LostPetMatch (scenes.py)
  action: render → manim/B02.mp4
  show: lost/found pet photo-match graphic — two photo cards, a checkmark
        match badge, "+25% recovery" stat
  status: RENDERABLE

## BEAT 3 — win #2 (B03)

B03 · Manim B03_NotesToContent (scenes.py)
  action: render → manim/B03.mp4
  show: one "Rushed notes" card fanning into three output cards — adoption
        post, social caption, donor update
  status: RENDERABLE

## BEAT 4 — win #3 (B04)

B04 · Manim B04_CoordinationHub (scenes.py)
  action: render → manim/B04.mp4
  show: central "Coordination" card with three fanned tags — foster
        placements, volunteer schedules, transport relays
  status: RENDERABLE

## BEAT 5 — honest context (B05)

B05 · Manim B05_HonestNumbers (scenes.py)
  action: render → manim/B05.mp4
  show: two-stat contrast — "4.2M adopted in 2025" vs "still stretched
        thin — shelter capacity, nationally"
  status: RENDERABLE

## BEAT 6 — the forward-looking close (B06)

B06 · Manim B06_NotSmarterAI (scenes.py)
  action: render → manim/B06.mp4
  show: "Not smarter AI." + subline "Wider adoption of what already works."
  status: RENDERABLE

## CLOSE — HANDOFF / OUTRO (B07–B08)

B07 · ClaudeComposerAsk (Remotion) — HANDOFF LAW
  action: render → media/B07.mp4
  props: greeting="Your turn.", command=(viewer prompt, read + discussed
         in narration)
  status: RENDERABLE

B08 · ClaudeTitleOutro (Remotion)
  action: render → media/B08.mp4
  props: title="Rescue, Reinvented.", handle="@HumanitariansAI",
         subline="real progress, honestly told"
  status: RENDERABLE

## Notes

- No pantry / archival stills used in this reel — every visual is either a
  Claude-skin Remotion composer/outro beat or a from-scratch Manim scene
  built for this reel (scenes.py). No open pantry slots, no SHOPPING.md.
- All 6 Manim scenes render at 4K by default via `./art run`
  (hardcoded 3840x2160 in run.sh for 16:9 reels).
- `@HumanitariansAI` matches the branding precedent set on this user's
  other reels in this book.
- Target duration: exactly 4:00 (240s), per explicit user request — narration
  drafted toward the established 2.78 wps af_bella calibration to land close
  on the first pass; actual timing confirmed only once Kokoro audio is
  generated and measured (audio-first principle).
- Source article was pasted directly in the build request (not a file) —
  no encoding issue this time.
- Source attribution (ASPCA, DigitalDefynd, Who Will Let the Dogs Out)
  included in the outro narration from the first pass, learning from the
  ai-nonprofit-marketing reel where this had to be added after the fact.
