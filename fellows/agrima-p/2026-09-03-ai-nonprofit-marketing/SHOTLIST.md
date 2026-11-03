# SHOTLIST — ai-nonprofit-marketing
# Typed work order per beat. Gate F open. Pass 1 (pre-audio-lock estimates).
# ai-explainer chassis (Claude bookends + all-self-generated body) — no
# pantry stills, no shopping list, no external asset dependency.

## OPEN — INTRO (B00)

B00 · ClaudeComposerAsk (Remotion)
  action: render → media/B00.mp4
  props: greeting="Hi,", command="claude \"help me understand how AI is
         actually helping nonprofit marketing teams\"", output=[3 lines]
  show: composer types → running indicator → output lands. Plain ask-focused
        hook — self-intro lives in B00B, not here.
  status: RENDERABLE

B00B · Manim B00B_AgrimaIntro (scenes.py)
  action: render → manim/B00B.mp4
  show: presenter card — "Hi, I'm Agrima." + Loon Project lead-in
  status: RENDERABLE

## ACT I — the problem (B01–B02)

B01 · Manim B01_OneTeamManyHats (scenes.py)
  action: render → manim/B01.mp4
  show: central "One person." card with four role tags fanning out and
        connecting to it (Outreach, Storytelling, Campaigns, Fundraising)
  status: RENDERABLE

B02 · Manim B02_LoonBudget (scenes.py)
  action: render → manim/B02.mp4
  show: "A full marketing team." vs "One person." card comparison + a
        budget bar showing the disparity, footer names the Loon Project
  status: RENDERABLE

## ACT II — where AI is helping (B03–B04)

B03 · Manim B03_AdoptionStats (scenes.py)
  action: render → manim/B03.mp4
  show: two stacked stats — 50%+ piloting/using AI, ~30% revenue increase
  status: RENDERABLE

B04 · Manim B04_UnglamorousTasks (scenes.py)
  action: render → manim/B04.mp4
  show: 2x2 grid — donor emails / impact reports→social / meeting
        notes→summaries / long content→short posts
  status: RENDERABLE

## ACT III — genuinely better (B05–B06)

B05 · Manim B05_EmailPersonalization (scenes.py)
  action: render → manim/B05.mp4
  show: generic vs personalized email mockup, "~2x open + click-through"
  status: RENDERABLE

B06 · Manim B06_DonationFormLift (scenes.py)
  action: render → manim/B06.mp4
  show: $115 industry-wide vs $161 AI-optimized form, two-bar comparison
  status: RENDERABLE

## ACT IV — the honest limit (B07)

B07 · Manim B07_HonestLimit (scenes.py)
  action: render → manim/B07.mp4
  show: "AI can draft fast." / "It can't decide what to say." / "That part
        stays human."
  status: RENDERABLE

## ACT V — the closing idea (B08–B09)

B08 · Manim B08_NotTopDown (scenes.py)
  action: render → manim/B08.mp4
  show: "Not big tech, top-down." + subline
  status: RENDERABLE

B09 · Manim B09_LoonClose (scenes.py)
  action: render → manim/B09.mp4
  show: three-line closing reveal, captioned "— the Loon Project"
  status: RENDERABLE

## CLOSE — HANDOFF / OUTRO (B10–B11)

B10 · ClaudeComposerAsk (Remotion) — HANDOFF LAW
  action: render → media/B10.mp4
  props: greeting="Your turn.", command=(viewer prompt, read + discussed
         in narration)
  status: RENDERABLE

B11 · ClaudeTitleOutro (Remotion)
  action: render → media/B11.mp4
  props: title="The Nonprofit Marketing Problem AI Is Quietly Solving.",
         handle="@HumanitariansAI", subline="help, not hype"
  status: RENDERABLE

## Notes

- No pantry / archival stills used in this reel — every visual is either a
  Claude-skin Remotion composer/outro beat or a from-scratch Manim scene
  built for this reel (scenes.py). No open pantry slots, no SHOPPING.md.
- All 10 Manim scenes render at 4K by default via `./art run`
  (hardcoded 3840x2160 in run.sh for 16:9 reels).
- `@HumanitariansAI` matches the branding precedent set on this user's
  other four reels in this book.
- Target duration: exactly 4:00 (240s), per explicit user request — narration
  length was drafted against a corrected wps estimate (2.78 wps, per this
  session's af_bella calibration) to land close on the first pass; actual
  timing is confirmed only once Kokoro audio is generated and measured
  (audio-first principle).
- Source article was UTF-16 encoded (BOM'd); read via explicit decode, the
  user's original file was not modified.
