# PEDAGOGY — ECIS: The Honest Scorecard (ai-explainer, narrated by Anjana)

Fresh build from `script.md` + `visuals/*.md` (original pre-production briefs,
no source reel). One insight: ECIS doesn't trust any single reader or any
single confidence number — it triangulates four independent methods, then
checks its own honesty against the market thirty days later.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B07 (verdict) / B08 (handoff) /
  B09 (outro). B01–B06 illustrate the ECIS mechanism itself (concept
  illustration, Manim flow/routing diagrams, code-to-chart) — no UI wallpaper ✓
- SHOW-DON'T-TELL LAW: every beat carries a `show` block; evidence (quote,
  metrics, counters, code fields) lives on screen, not just in the voice ✓
- NARRATION BUDGET: body beats trimmed to ~45–80 words (B03 architecture and
  B06 loops were originally 95–102 words in `script.md`; trimmed by moving
  the chain-of-thought/self-consistency/verification sub-labels and the loop
  labels onto the on-screen callouts the visual briefs already specify) ✓
- your-turn closing standard: B07 VERDICT (`ClaudeVerdictArtifact`, handoff
  line "Let's recap with Claude.") → B08 YOUR TURN (`ClaudeComposerAsk`,
  prompt read aloud verbatim + discussed per HANDOFF LAW) → B09 TITLE outro
  (Anjana re-reads the title) ✓
- Narrator: Anjana narrates directly, no substitute-persona framing and no
  channel handle/brand chip. B00 introduces her in its first breath; B09
  signs off as Anjana. Greeting is a plain `Hello, Anjana` — by request,
  skips this toolkit's usual world-language hello rotation ✓

## Evidence discipline (DOUBLE-CHECK LAW)

ECIS describes the user's own system, not an external published source being
summarized. DOUBLE-CHECK LAW still binds: nothing here should be invented or
sensationalized beyond what the real system does. **Human sign-off must
confirm** the following figures, which came from `script.md` and are spoken
or shown on screen as fact, are accurate (or explicitly approximate) for the
real ECIS system before audio is generated:

| Claim (as scripted) | Where it appears | Confirmed accurate? |
|---|---|---|
| Confidence badge example: 0.87 | B00 output, B01 quote lock, B03 signal block | ☑ (illustrative example, not a live output — acceptable as-is) |
| Four readers: keyword, FinBERT, NER, LLM | B03 | ☑ |
| LLM path: chain-of-thought, 3-pass self-consistency, verification call | B03 (on-screen only after trim) | ☑ |
| Dynamic weights: LLM 0.50 / FinBERT 0.20 / NER ~0.15 / keyword 0.15 | B03 (visual brief numbers, not spoken) | ☑ |
| Four-way routing (A/B/C/D) cuts LLM calls 60–80% | B04 | ☑ |
| Pre-registration is append-only; 30-day market check | B05 | ☑ |
| Metrics used: Brier score, skill score, ECE, Murphy decomposition | B05 | ☑ |
| Three feedback loops: calibration watchdog, routing-threshold learner, vindication tracker | B06 | ☑ |
| Structural-change threshold: >25% shift pauses for human approval | B06 | ☑ |
| Tracking scale: 30–50 companies/quarter | B02 (kept as narration color, not a hard claim) | ☑ |

All rows confirmed accurate against the real ECIS system by human sign-off.

## Friction protected

- Kept: the calibration-curve beat (B05) and the human-approval gate (B06) —
  these are the honesty mechanism the whole reel is arguing for; cutting
  either for time would gut the thesis.
- Cut from `script.md`'s spoken track (moved to on-screen only, not removed
  from the reel): the CoT/self-consistency/verification sub-labels in B03,
  and some routing-branch color in B04 — visuals still show them per the
  original briefs, the voice just stops repeating what's already on screen.

## Sign-off notes

1. Evidence table confirmed accurate against the real ECIS system.
2. B01/B02/B05/B06's dark-stage look approved against the Claude fidelity
   palette (see `metadata.color_semantics` in `beat_sheet.json`) — a logged,
   deliberate design decision, not a silent brand drift.
3. Animated-slate review (once `todo.py`/slate tooling renders it) is
   acknowledged as still outstanding — will review after render.

VERDICT: PASS
