# CHECKS-REPORT — rescue-reinvented
Written before the first slate compile, per PROOF GATE (skills/make/deep-explainer
and ai-explainer SKILL.md — this reel is built on the ai-explainer chassis; see
metadata.note in beat_sheet.json for why).

## Per-beat classification

11 SHOW / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Why |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk, ask shown answered (cold open); plain ask-focused hook, no self-intro here |
| B00B | SHOW | Manim presenter card, names its artifact (name + lead-in) |
| B01 | SHOW | Manim 2x2 grid, names its artifact (the four strain-point cards) |
| B02 | SHOW | Manim photo-match diagram, names its artifact (LOST/FOUND cards + match badge + stat) |
| B03 | SHOW | Manim fan-out diagram, names its artifact (notes card -> three content cards) |
| B04 | SHOW | Manim fan-out diagram, names its artifact (coordination hub + three tags) |
| B05 | SHOW | Manim stat contrast, names its artifact (4.2M adopted vs. stretched-thin capacity) |
| B06 | SHOW | Manim typographic reframe, names its artifact |
| B07 | SHOW | ClaudeComposerAsk handoff, prompt read + discussed (HANDOFF LAW) |
| B08 | SHOW | ClaudeTitleOutro, title restated, sources named in narration |

Every claim-bearing beat names its on-screen artifact in `shot.visual_intent`
or the Remotion props. No beat is a bare CARD carrying an unvisualized claim.

## Teaching-arc checklist

- FRAMEWORK ✓ — B01 establishes the concrete backdrop (resource strain)
  before any AI-adoption claim is offered.
- WORKED EXAMPLE ✓ — B02–B04 are three concrete, sourced mechanisms (Finding
  Rover, AI content generation, Doobert) the video's argument rests on, not
  abstract assertion.
- FALSIFIABILITY ✓ — B05 is explicit about the honest, ongoing gap (shelter
  capacity still stretched thin, not every animal finds the ideal outcome);
  FACTCHECK.md hedges every statistic as the article's own cited claim,
  preserving its hedge language ("as much as 25%," "a significant number")
  rather than overstating precision.
- SCAFFOLDED TASK ✓ — B07 hands the viewer a concrete, narrower version of
  the same exercise (check whether their own local shelter uses these tools).
- BOOKENDS ✓ — B00 cold open (Claude composer, ask answered) / B08 title
  restate outro — both present, correct order.
- NO-SOURCE-NO-VERDICT ✓ — see FACTCHECK.md: every statistic is attributed
  to the article's own named source; no invented numbers, no claim
  presented as more certain than the article itself states it.

## Deviations from house defaults (disclosed, not hidden)

1. **Chassis substitution**: user asked for "Deep Explainer" by name. Built
   on `ai-explainer`'s chassis instead of the actual `deep-explainer` skill
   — deep-explainer targets 5-10 min as an output-not-target (conflicts with
   the user's exact 4:00 ask) and requires ~20-25% archival/pantry-still
   body beats, which the user explicitly said don't exist for this topic.
   Matches the precedent set on this user's death-of-the-generic-resume and
   ai-nonprofit-marketing reels.
2. **Register/voice**: `af_bella` (Bella), professional and optimistic-but-
   honest, first-person — per explicit user request for a woman's voice;
   af_bella is the only female voice this toolkit ships.
3. **Channel handle**: `@HumanitariansAI` throughout, matching precedent.
4. **No pantry/vox beats**: every body beat is self-generated Manim, zero
   external images — the user confirmed no dedicated footage exists.
5. **B00B presenter-intro beat from the start**: the self-intro lives in
   its own dedicated B00B Manim beat from the first pass, not folded into
   B00 — applying the established fix directly rather than needing a
   correction round.
6. **Source attribution in-video from the first pass**: the outro narration
   (B08) names all three sources (ASPCA, DigitalDefynd, Who Will Let the
   Dogs Out) — a lesson carried forward from ai-nonprofit-marketing, where
   this had to be added after the user asked whether sources were mentioned.

GATE F: FACTCHECK.md / SHOTLIST.md / PROMPTS.md all present. CHECKS-REPORT
written before first render. Proceeding to audio generation.
