# PEDAGOGY — ECIS Episode 4: Not Just What. Who, How Clean, and What Came Before. (ai-explainer, narrated by Anjana)

Fresh build from `script.md` + `visuals/*.md` (original pre-production briefs,
no source reel). Sequel to `examples/ecis-ep3` (Episode 3) — extends the
system, does not re-explain it. One insight: the same words from a CFO and
from an analyst asking a question are not the same signal — authority,
source cleanliness, and trend context all have to scale the raw reader
confidence before it means anything.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / verdict / handoff / outro.
  The six body beats illustrate the context-weighting mechanism itself
  (speaker authority, chunk quality, trend timelines, the combined
  triangulator equation) — no UI wallpaper ✓
- SHOW-DON'T-TELL LAW: every beat carries a `show` block; evidence (the
  weight badges, the quality meters, the timeline trend tags, the
  step-by-step equation) lives on screen ✓
- NARRATION BUDGET: all six body beats read tight in the source (5/15/12/12/8/5
  seconds against ~45–70-word body-beat guidance) — no trim needed, kept as
  scripted ✓
- Narrator: Anjana narrates directly, no channel handle or brand chip.
  Source files say `am_onyx` — overridden to `af_bella` (Anjana's voice),
  matching Episodes 1-3 ✓ confirmed.
- Continuity: purple (Llama), teal (Mistral), amber (Qwen) model nodes and
  the triangulator node style carry over unchanged from Episode 3.
- B04's two example timelines use fully generic placeholder names ("Company
  A" / "Company B") rather than real tickers, per explicit request — a
  deliberate departure from Episodes 2 and 3's dashboard beats, which used
  real illustrative tickers (NVDA, MSFT, GOOGL, AMD).

## Evidence discipline (DOUBLE-CHECK LAW)

Like Episodes 1-3, this describes the user's own system rather than an
external published source. Human sign-off confirmed the following:

| Claim (as scripted) | Where it appears | Confirmed accurate / clearly illustrative? |
|---|---|---|
| Speaker weight scale: CFO 1.0 / CEO 0.8 / COO 0.7 / IR 0.6 / Analyst 0.3 / Operator 0.0 | B02 | ☑ confirmed |
| Four chunk-quality dimensions (boilerplate ratio, token count, section completeness, speaker transitions) combining into one multiplier | B03 | ☑ confirmed |
| Worked example: confidence 0.85 × CFO weight 1.0 = 0.85; same 0.85 × analyst weight 0.3 = 0.26 | B02 | ☑ illustrative example, not a live output — acceptable as-is |
| Worked example: noisy-chunk quality 0.49, clean-chunk quality 0.94 | B03 | ☑ illustrative example — acceptable as-is |
| Combined chain: reader confidence 0.85 × speaker weight 0.8 = 0.68, then × chunk quality 0.92 = 0.63 | B05 | ☑ illustrative example — acceptable as-is |
| Four trend-tag categories: consecutive_raise, consecutive_lower, reversal, stable_maintained | B04 | ☑ confirmed |
| "Company A" / "Company B" as fully generic placeholder names, no real ticker or company identity implied | B04, B06 | ☑ generic by design, per explicit request — no company-identity claim of any kind |

All rows confirmed accurate against the real ECIS system by human sign-off.

## Friction protected

- Kept: the CFO-to-analyst swap in B02 as the visual centerpiece — same
  quote, same confidence, different authority, different outcome. This is
  the clearest possible demonstration of the episode's thesis.
- Kept: the reversal tag in B04 as a distinct, pulsing visual against the
  three-quarter green run before it — the whole point of trend context is
  that a reversal reads differently from a snapshot, and the visual needs
  to make that legible instantly.

## Sign-off notes

1. Evidence table confirmed — speaker-weight scale, chunk-quality dimensions,
   and trend-tag categories all checked against the real system.
2. Voice override (`am_onyx` → `af_bella`) confirmed, matching Episodes 1-3.
3. Delivery: this episode renders at 4K (3840×2160) in both 16:9 and 9:16
   (via the shorts pipeline, `aspect_ratio: "9:16"`, `--height 3840` for a
   2160×3840 vertical master) — noted here so the animated-slate review
   below covers both orientations, not just the 16:9 cut.
4. Animated-slate review (once `remotion_scenes.py` renders it, both
   orientations) is acknowledged as still outstanding — will review after
   render.

VERDICT: PASS
