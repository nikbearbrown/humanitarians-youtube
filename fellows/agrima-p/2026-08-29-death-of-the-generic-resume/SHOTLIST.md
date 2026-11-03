# SHOTLIST — death-of-the-generic-resume
# Typed work order per beat. Gate F open. Pass 1 (pre-audio-lock estimates).
# ai-explainer chassis (Claude bookends + all-self-generated body) — no
# pantry stills, no shopping list, no external asset dependency.

## OPEN — INTRO (B00)

B00 · ClaudeComposerAsk (Remotion)
  action: render → media/B00.mp4
  props: greeting="Hi,", command="claude \"help me put into words a pattern
         I keep noticing every time I apply for a job\"", output=[3 lines]
  show: composer types → running indicator → output lands. Narration is a
        plain ask-focused hook (no self-intro here — see B00B).
  status: RENDERABLE

B00B · Manim B00B_AgrimaIntro (scenes.py) — CORRECTION per user request
  action: render → manim/B00B.mp4
  show: presenter card — "Hi, I'm Agrima." + a short lead-in line, fading
        in beneath a grown-in rule. Matches the presenter-intro pattern
        used on two-threads-one-week's B01 (name + short summary card)
        rather than folding the self-intro into B00's composer narration.
  status: RENDERABLE

## ACT I — the experience (B01–B03)

B01 · Manim B01_TheOutreach (scenes.py)
  action: render → manim/B01.mp4
  show: two-step card sequence — recruiter reaches out -> you apply
  status: RENDERABLE

B02 · Manim B02_InstantReject (scenes.py)
  action: render → manim/B02.mp4
  show: Applied -> fast clock (00:00:47) -> Rejected, footer "no feedback,
        no reason, just no"
  status: RENDERABLE

B03 · Manim B03_Gaslit (scenes.py)
  action: render → manim/B03.mp4
  show: typographic reveal — "Gaslit by the process." + subline
  status: RENDERABLE

## ACT II — who's responsible (B04–B06)

B04 · Manim B04_QuoteDeny (scenes.py)
  action: render → manim/B04.mp4
  show: quote card — "No AI auto-rejects candidates..." — some recruiters
  status: RENDERABLE

B05 · Manim B05_QuoteAdmit (scenes.py)
  action: render → manim/B05.mp4
  show: quote card — "We pre-screen for the hard requirements..." + a
        checklist (Visa / Location / Years of experience)
  status: RENDERABLE

B06 · Manim B06_BlackBox (scenes.py)
  action: render → manim/B06.mp4
  show: black-box diagram — Application -> [ ? ] -> Rejected
  status: RENDERABLE

## ACT III — the arms race (B07–B09)

B07 · Manim B07_TailoredStack (scenes.py)
  action: render → manim/B07.mp4
  show: one resume card fanning into five tailored versions
  status: RENDERABLE

B08 · Manim B08_IdenticalGrid (scenes.py)
  action: render → manim/B08.mp4
  show: grid of near-identical resume cards
  status: RENDERABLE

B09 · Manim B09_FilteredOut (scenes.py)
  action: render → manim/B09.mp4
  show: same grid, one card flagged "FILTERED"
  status: RENDERABLE

## ACT IV — the closing idea (B10–B12)

B10 · Manim B10_NotDying (scenes.py)
  action: render → manim/B10.mp4
  show: minimal reframe card — "Not a story about the resume dying."
  status: RENDERABLE

B11 · Manim B11_TwoAIs (scenes.py)
  action: render → manim/B11.mp4
  show: diagram — Your AI <-negotiating-> Their AI, "you: waiting" beneath
  status: RENDERABLE

B12 · Manim B12_AboutYou (scenes.py)
  action: render → manim/B12.mp4
  show: three-line typographic beat — Two systems. / Talking past you. /
        About you.
  status: RENDERABLE

## CLOSE — HANDOFF / OUTRO (B13–B14)

B13 · ClaudeComposerAsk (Remotion) — HANDOFF LAW
  action: render → media/B13.mp4
  props: greeting="Your turn.", command=(viewer prompt, read + discussed
         in narration)
  status: RENDERABLE

B14 · ClaudeTitleOutro (Remotion)
  action: render → media/B14.mp4
  props: title="AI and the Death of the 'Generic' Resume.",
         handle="@HumanitariansAI", subline="a pattern, not a headline"
  status: RENDERABLE

## Notes

- No pantry / archival stills used in this reel — every visual is either a
  Claude-skin Remotion composer/outro beat or a from-scratch Manim scene
  built for this reel (scenes.py). No open pantry slots, no SHOPPING.md.
- All 12 Manim scenes render at 4K by default via `./art run`
  (hardcoded 3840x2160 in run.sh for 16:9 reels).
- `@HumanitariansAI` in B00/B13/B14 matches the branding precedent set on
  this user's other two reels in this book.
- Target duration: exactly 4:00 (240s), per explicit user request — narration
  length was drafted against this target; actual timing is confirmed only
  once Kokoro audio is generated and measured (audio-first principle — the
  measured mp3s are the real clock, not the word-count estimate). A short
  trim/pad pass may follow the first audio generation to converge on 240s.
