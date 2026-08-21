# PEDAGOGY — ECIS Episode 3: Three Models, Zero Shortcuts (ai-explainer, narrated by Anjana)

Fresh build from `script.md` + `visuals/*.md` (original pre-production briefs,
no source reel). Sequel to `examples/ecis-ep2` (Episode 2) — extends the
system, does not re-explain it. One insight: adding a third model isn't the
point — the point is that more readers means more noise unless the pipeline
gates its own input and output, and stores full provenance so nothing is a
black box.

**Scope correction:** this episode covers implementation only. The third
model, the quality gates, and provenance tracking were built and tested this
week, but the pipeline has not yet been run across the full 25-company set —
that is future work. The original close beat claimed "twenty-five companies"
as this episode's own result; that was inaccurate and has been corrected to
"every input gated" in `script.md`, `narration/06_close.txt`, and
`visuals/06_close.md`. No scale claim belongs anywhere in this episode.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / verdict / handoff / outro.
  The six body beats illustrate the pipeline mechanism itself (architecture
  node diagram, conveyor-belt quality gates, the provenance stack, the
  dashboard) — no UI wallpaper ✓
- SHOW-DON'T-TELL LAW: every beat carries a `show` block; evidence (the
  per-model confidence numbers, the rejection stamps, the provenance layers,
  the calibration lines) lives on screen ✓
- NARRATION BUDGET: all six body beats read tight in the source
  (5/15/12/12/10/6 seconds against ~45–70-word body-beat guidance) — no trim
  needed, kept as scripted ✓
- Narrator: Anjana narrates directly, no channel handle or brand chip.
  Source files say `am_onyx` — overridden to `af_bella` (Anjana's voice),
  matching Episodes 1 and 2 ✓ confirmed.
- Continuity: purple (Llama) and teal (Mistral) carry over from Episode 2
  unchanged; amber (Qwen) is a new, deliberate series color to be kept
  consistent in any future episode that reuses this model.

## Evidence discipline (DOUBLE-CHECK LAW)

Like Episodes 1 and 2, this describes the user's own system rather than an
external published source. Human sign-off confirmed the following:

| Claim (as scripted) | Where it appears | Confirmed accurate / clearly illustrative? |
|---|---|---|
| Qwen2.5, 14B parameters | B02 | ☑ confirmed |
| Confidence gating threshold (output gate; example shown: 0.31) | B03 | ☑ confirmed |
| Boilerplate rejection ratio (example shown: 0.87, gate at >0.8) | B03 | ☑ confirmed |
| Three-way model agreement example: Llama 0.81 / Mistral 0.77 / Qwen 0.84 → triangulated 0.86 | B02 | ☑ illustrative example, not a live output — acceptable as-is |
| Provenance record contents: system prompt, few-shot examples, temporal context, source chunk | B04 | ☑ per script/visuals brief |
| Multi-model architecture reworked so model identity flows through pipeline state (native, not bolted on) | B02 | ☑ per script/visuals brief |
| Signal card format (ticker, direction, confidence, supporting quote) unchanged from Episode 1 | B04 | ☑ established in Episode 1, reused here |

All rows confirmed accurate against the real ECIS system by human sign-off.

## Friction protected

- Kept: the input/output quality-gate beat (B03) as its own beat rather than
  folding it into the third-model beat (B02) — it's the discipline argument
  the episode is actually making, not a footnote to the model count.
- Kept: the provenance stack (B04) as a full beat — "every decision has a
  receipt" is the payoff line the dashboard beat (B05) depends on.

## Sign-off notes

1. The company-scale claim in B06 was caught and corrected (see Scope
   correction above) — the episode no longer claims a 25-company run.
2. Evidence table confirmed — parameter count, confidence threshold, and
   boilerplate ratio all checked against the real system.
3. Voice override (`am_onyx` → `af_bella`) confirmed, matching Episodes 1
   and 2.
4. `beat_sheet.json` and the six `Ecis3*` Remotion illustrations
   (`runtime/remotion/src/illustrations/ecis-ep3/`) are authored and
   registered in `Root.tsx`; `npx tsc --noEmit` passes clean.
5. Animated-slate review (once `remotion_scenes.py` renders it) is still
   outstanding — will review after render.

VERDICT: PASS
