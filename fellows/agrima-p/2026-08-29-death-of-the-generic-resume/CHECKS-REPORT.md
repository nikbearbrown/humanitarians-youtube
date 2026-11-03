# CHECKS-REPORT — death-of-the-generic-resume
Written before the first slate compile, per PROOF GATE (skills/make/deep-explainer
and ai-explainer SKILL.md — this reel is built on the ai-explainer chassis; see
metadata.note in beat_sheet.json for why).

## Per-beat classification

16 SHOW / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Why |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk, ask shown answered (cold open); plain ask-focused hook — self-intro moved to B00B |
| B00B | SHOW | Manim presenter card, names its artifact (name + lead-in line); host self-intro, per user correction — matches two-threads-one-week's B01 pattern |
| B01 | SHOW | Manim two-step card, names its artifact (recruiter reaches out -> you apply) |
| B02 | SHOW | Manim timeline, names its artifact (Applied -> clock -> Rejected) |
| B03 | SHOW | Manim typographic reveal, names its artifact (the phrase itself) |
| B04 | SHOW | Manim quote card, names its artifact + attribution |
| B05 | SHOW | Manim quote card + checklist, names its artifact + attribution |
| B06 | SHOW | Manim black-box diagram, names its artifact (Application -> ? -> Rejected) |
| B07 | SHOW | Manim fan-out diagram, names its artifact (one resume -> five tailored) |
| B08 | SHOW | Manim grid, names its artifact (near-identical resume cards) |
| B09 | SHOW | Manim grid + flag, names its artifact (FILTERED tag) |
| B10 | SHOW | Manim typographic card, names its artifact (the reframe line) |
| B11 | SHOW | Manim diagram, names its artifact (Your AI / negotiating / Their AI / you: waiting) |
| B12 | SHOW | Manim typographic beat, names its artifact (three-line reveal) |
| B13 | SHOW | ClaudeComposerAsk handoff, prompt read + discussed (HANDOFF LAW) |
| B14 | SHOW | ClaudeTitleOutro, title restated |

Every claim-bearing beat names its on-screen artifact in `shot.visual_intent`
or the Remotion props. No beat is a bare CARD carrying an unvisualized claim.

## Teaching-arc checklist

- FRAMEWORK ✓ — B01–B03 establish the concrete experience (the "why care")
  before any interpretation is offered.
- WORKED EXAMPLE ✓ — the recruiter-contradiction beats (B04/B05) and the
  black-box beat (B06) are the concrete, named mechanism the essay's
  argument rests on, not abstract assertion.
- FALSIFIABILITY ✓ — the video is explicit about what it does NOT know
  (B06: "you have no way to know which one just happened"; FACTCHECK.md
  hedges every claim as framing, never as measured fact) — it does not
  overclaim certainty about mechanisms it can't verify.
- SCAFFOLDED TASK ✓ — B13 hands the viewer a concrete, narrower version of
  the same exercise (bring your own rejection, ask Claude to separate
  signal from noise).
- BOOKENDS ✓ — B00 cold open (Claude composer, ask answered, host self-intro)
  / B14 title restate outro — both present, correct order.
- NO-SOURCE-NO-VERDICT ✓ — see FACTCHECK.md: every claim is either the
  user's own supplied framing (explicitly attributed as such) or a reasoned
  consequence of it; no invented statistics, no named companies/tools.

## Deviations from house defaults (disclosed, not hidden)

1. **Chassis substitution**: user asked for "Deep Explainer" by name. Built
   on `ai-explainer`'s chassis instead of the actual `deep-explainer` skill
   — see beat_sheet.json metadata.note for the full reasoning (duration
   conflict: user wants exactly 4:00, deep-explainer targets 5-10 min as an
   output never a fixed target; and no natural archival-photo angle for
   deep-explainer's required ~20-25% pantry-still quota, which would have
   introduced an external sourcing dependency this session has otherwise
   avoided entirely). Disclosed to the user before building, not silently
   substituted.
2. **Register/voice**: `af_bella` (Bella), conversational-reflective, first
   person — matches the precedent already established on this user's other
   two reels, not the house Teardown register / `am_onyx` that is
   ai-explainer's own documented default.
3. **Channel handle**: `@HumanitariansAI` throughout, matching this user's
   other reels in this book.
4. **No pantry/vox beats**: every body beat is self-generated Manim, zero
   external images. This is a deliberate simplification versus the
   deep-explainer genre's own beat-mix contract (which would require a VOX
   lane) — appropriate here since the chassis itself was substituted; see
   deviation #1.
5. **B00B presenter-intro beat added (post-first-cut correction)**: the host
   self-introduction ("Hi, I'm Agrima...") was originally folded into B00's
   cold-open narration; moved to its own dedicated B00B beat (Manim
   presenter card) per user request, matching the precedent already set on
   two-threads-one-week's B01 rather than inventing a new pattern.

GATE F: FACTCHECK.md / SHOTLIST.md / PROMPTS.md all present. CHECKS-REPORT
written before first render. Proceeding to audio generation.
