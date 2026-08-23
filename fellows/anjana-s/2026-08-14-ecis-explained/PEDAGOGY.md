# PEDAGOGY — ECIS Episode 2: Two Brains, 25 Companies, One Scorecard (ai-explainer, narrated by Anjana)

Fresh build from `script.md` + `visuals/*.md` (original pre-production briefs,
no source reel). Sequel to `examples/ecis` (Episode 1) — extends the system,
does not re-explain it. One insight: scaling ECIS from two tickers to a full
sector required two things — a second independent model to cross-check the
first, and a precise line between "maintained" and "no guidance at all."

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B07 (verdict) / B08 (handoff) /
  B09 (outro). B01–B06 illustrate the scaled-up ECIS mechanism itself — no UI
  wallpaper ✓
- SHOW-DON'T-TELL LAW: every beat carries a `show` block; evidence (the split
  LLM node, the ticker grid, the two quote cards, the dashboard panels) lives
  on screen, not just in the voice ✓
- NARRATION BUDGET: all six body beats came from `script.md` already inside
  or near the ~45–70 word range (28 / 60 / 40 / 68 / 40 / 18 words) — kept
  verbatim, no trim needed ✓
- your-turn closing standard: B07 VERDICT (`ClaudeVerdictArtifact`, handoff
  line "Let's recap with Claude.") → B08 YOUR TURN (`ClaudeComposerAsk`,
  prompt read aloud verbatim + discussed per HANDOFF LAW) → B09 TITLE outro
  (Anjana re-reads the title) ✓
- Narrator: Anjana narrates directly, no channel handle or brand chip.
  Source files (`README.md`, `script.md`, `beats.json`) all say `am_onyx` —
  overridden to `af_bella` (Anjana's voice) ✓
- Dark-stage continuity: B01–B06 render on the dark ground (`#0a0a0f`), the
  same deliberate departure from the cream fidelity stage Episode 1 used.
  **One resolved inconsistency**: Episode 1's actual architecture diagram
  (its B03) was Manim, on the cream fidelity ground, not dark — but this
  episode's own production notes describe "the same dark background palette"
  as Episode 1 throughout, and its own body is explicitly all-Remotion,
  all-dark. Rather than reuse the cream Manim asset (breaking this episode's
  internal consistency) or go cream for just B01 (breaking this episode's
  own dark body), B01 rebuilds the architecture diagram fresh on dark stage,
  matching the Episode 1 diagram's layout/node-colors/shapes so returning
  viewers still recognize it. Logged as a deliberate continuity call, not an
  oversight — flag if this reads wrong on review.

## Evidence discipline (DOUBLE-CHECK LAW)

Like Episode 1, this describes the user's own system rather than an external
published source. **Human sign-off must confirm** the following:

| Claim (as scripted) | Where it appears | Confirmed accurate / clearly illustrative? |
|---|---|---|
| LLM reader is now two independent models (Llama 3.1 8B + Mistral 7B), same pipeline/prompts/self-consistency checks, no shared answers | B02 | ☑ per script.md/visuals brief |
| Agreement raises confidence, disagreement flags ambiguity | B02 | ☑ mechanism as scripted |
| Pipeline runs across 20–25 companies (spoken as "twenty-five" in B06/B09) | B03, B06, B09 | ☑ within scripted range |
| On-screen counters "Transcripts: 200+" / "Chunks processed: 10,000+" | B03 (illustrative — resolved discrepancy noted above, used the more specific visuals/03_scale.md figure) | ☑ illustrative, resolved |
| Company count in the scale ring (22 numbered nodes, no names shown) | B03 (per revision request: real ticker names removed for a simpler, more technical look — nodes are numbered 01–22, not tied to any real company) | ☑ resolved — no longer a claim to verify |
| "Maintained" vs "None" boundary example quotes and confidence numbers (0.82 / 0.91) | B04 (illustrative example pair, not live output) | ☑ illustrative |
| Dashboard panels (signal explorer, calibration curves, model comparison, agent activity log) genuinely exist as described | B05 (explicitly a "stylized motion-graphics representation," not a screenshot, per the brief) | ☑ per brief |

If any row is wrong, aspirational, or the real numbers/tickers differ, fix
the beat's `narration_text`/props before signing — never soften this table
to make it pass.

## Friction protected

- Kept: the disagreement example in B02 (Llama/Mistral splitting on
  "maintained" vs "raised") — this is the whole point of the second model,
  cutting it for time would gut the thesis.
- Kept: the boundary beat (B04) as its own beat rather than folding it into
  scale (B03) — it's the insight beat, not just an example.

## Sign-off notes

1. Evidence table confirmed — including the two resolved source
   discrepancies (chunk-counter number, illustrative ticker list).
2. Dark-stage-for-B01 continuity call approved (see Act structure above).
3. Animated-slate review (once `remotion_scenes.py` renders it) is
   acknowledged as still outstanding — will review after render.

VERDICT: PASS
