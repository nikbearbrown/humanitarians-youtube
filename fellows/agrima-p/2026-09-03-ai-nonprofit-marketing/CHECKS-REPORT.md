# CHECKS-REPORT — ai-nonprofit-marketing
Written before the first slate compile, per PROOF GATE (skills/make/deep-explainer
and ai-explainer SKILL.md — this reel is built on the ai-explainer chassis; see
metadata.note in beat_sheet.json for why).

## Per-beat classification

13 SHOW / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Why |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk, ask shown answered (cold open); plain ask-focused hook, no self-intro here |
| B00B | SHOW | Manim presenter card, names its artifact (name + Loon Project lead-in); self-intro lives here from the start, per established precedent |
| B01 | SHOW | Manim fan-out diagram, names its artifact (one-person card + four role tags) |
| B02 | SHOW | Manim two-card comparison + budget bar, names its artifact |
| B03 | SHOW | Manim stat cards, names its artifact (50%+ / ~30% stat lines) |
| B04 | SHOW | Manim 2x2 grid, names its artifact (the four task cards) |
| B05 | SHOW | Manim before/after mockup, names its artifact (generic vs personalized email) |
| B06 | SHOW | Manim bar comparison, names its artifact ($115 vs $161) |
| B07 | SHOW | Manim typographic contrast, names its artifact (the three-line reveal) |
| B08 | SHOW | Manim typographic reframe, names its artifact |
| B09 | SHOW | Manim closing typographic beat, names its artifact, captioned with the Loon Project |
| B10 | SHOW | ClaudeComposerAsk handoff, prompt read + discussed (HANDOFF LAW) |
| B11 | SHOW | ClaudeTitleOutro, title restated |

Every claim-bearing beat names its on-screen artifact in `shot.visual_intent`
or the Remotion props. No beat is a bare CARD carrying an unvisualized claim.

## Teaching-arc checklist

- FRAMEWORK ✓ — B01–B02 establish the concrete problem (one person, many
  roles, a fraction of the budget) before any AI-adoption claim is offered.
- WORKED EXAMPLE ✓ — B05/B06 are the concrete, sourced mechanism the video's
  argument rests on (personalization → ~2x open rate; optimized forms →
  $161 vs $115), not abstract assertion.
- FALSIFIABILITY ✓ — B07 is explicit about what AI does NOT do (decide what
  to say, judge honesty); FACTCHECK.md hedges every statistic as the
  article's own cited claim, never independently re-verified, and preserves
  the article's own approximation language ("more than half," "reportedly
  double") rather than overstating precision.
- SCAFFOLDED TASK ✓ — B10 hands the viewer a concrete, narrower version of
  the same exercise (find one AI tool for their own team's outreach this
  week).
- BOOKENDS ✓ — B00 cold open (Claude composer, ask answered) / B11 title
  restate outro — both present, correct order.
- NO-SOURCE-NO-VERDICT ✓ — see FACTCHECK.md: every statistic is attributed
  to the article's own named source; no invented numbers, no claim
  presented as more certain than the article itself states it.

## Deviations from house defaults (disclosed, not hidden)

1. **Chassis substitution**: user asked for "Deep Explainer" by name. Built
   on `ai-explainer`'s chassis instead of the actual `deep-explainer` skill
   — deep-explainer targets 5-10 min as an output-not-target (conflicts with
   the user's exact 4:00 ask) and requires ~20-25% archival/pantry-still
   body beats, which the user explicitly said don't exist for this topic
   ("no footage or screenshots specific to this article"). Disclosed to the
   user's own framing, not silently substituted — matches the precedent set
   on this user's death-of-the-generic-resume reel.
2. **Register/voice**: `af_bella` (Bella), professional and first-person —
   matches the precedent already established on this user's other reels,
   not the house Teardown register / `am_onyx` that is ai-explainer's own
   documented default. Per explicit user request for a woman's voice —
   af_bella is the only female voice this toolkit ships.
3. **Channel handle**: `@HumanitariansAI` throughout, matching this user's
   other reels in this book.
4. **No pantry/vox beats**: every body beat is self-generated Manim, zero
   external images — the user confirmed no dedicated footage exists.
5. **B00B presenter-intro beat from the start**: unlike the earlier
   death-of-the-generic-resume build in this same session (which initially
   folded the self-intro into B00 and required a correction), this reel
   applies the established fix from the first pass — the self-intro lives
   in its own dedicated B00B Manim beat, matching two-threads-one-week's B01
   precedent directly.

GATE F: FACTCHECK.md / SHOTLIST.md / PROMPTS.md all present. CHECKS-REPORT
written before first render. Proceeding to audio generation.
