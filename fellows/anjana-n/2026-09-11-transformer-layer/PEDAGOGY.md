# PEDAGOGY — What Happens Inside a Transformer Layer (ai-explainer, narrated by Anjana)

Build from the pre-authored `script.md` + `narration/*.txt` + `visuals/*.md`
(the script was already populated; `README.md`). One insight:
every transformer layer is the same four operations in the same order, and the
two unglamorous ones — residual connections and layer norm — are the reason
the glamorous two can be stacked ninety-six deep without the model falling
over.

Companion to `examples/attention-finance` (which covers *why* attention beats
left-to-right reading) — this video is the next level down: what one layer
actually does to one token, with attention as one of four steps rather than
the whole story.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B06 (verdict) / B07 (handoff) /
  B08 (outro). B01–B05 illustrate the layer itself — the stack, the QKV
  scores, the expand/activate/compress strip, the residual bypass, the
  stacking payoff ✓
- SHOW-DON'T-TELL LAW: every body beat carries a `show` block; the evidence
  (the five attention scores summing to 1.0, the 4× expansion, the "+" node,
  the twelve-vs-ninety-six stack) lives on screen ✓
- your-turn closing standard: B06 VERDICT → B07 YOUR TURN (prompt read aloud
  and discussed per HANDOFF LAW) → B08 TITLE outro ✓
- Narrator: Anjana, no channel handle. Source files say `am_onyx` — overridden
  to `af_bella` per the series convention ✓
- Dark-stage deviation: B01–B05 on the dark ground (`#0a0a0f`), matching the
  attention-finance and temperature-finance companion pieces.
- **Recurring visual anchor:** the layer opens like a cross-section in B01 and
  closes again in B05 — microscope in, microscope out. B02–B04 happen inside it.
- **Color law:** Q is gold, K is blue, V is green throughout B02; the token
  "revenue" is terracotta. These four do not get reused for anything else.
- **NARRATION BUDGET — logged deviation.** B02 (~115 words, ~42s) and B04
  (~121 words, ~45s) run well over the 45–70-word range. Kept verbatim; each is
  built as a genuine multi-stage animation (QKV → scores → weighted sum; split →
  add → norm → repeat) sized to fill its real audio span rather than
  freeze-holding early.
- **No company names anywhere** — "We expect revenue growth to moderate" is a
  generic illustrative construction.

## Evidence discipline (DOUBLE-CHECK LAW)

This video explains a public, well-documented architecture (Vaswani et al.,
2017, "Attention Is All You Need"), not a proprietary system. Every claim is
either textbook-accurate or a deliberate, flagged simplification.

| Claim (as scripted) | Where | Status |
|---|---|---|
| Every layer = self-attention → feed-forward → with layer norm and residual connections | B01, B05 | ☑ factual |
| Attention creates Q, K, V from each token; query scored against every key; scores become weights via softmax; weighted sum of values | B02 | ☑ factual — **simplified to single-head** (real layers run several heads in parallel). Flagged in the script's own notes; the mechanism is identical per head. |
| The five attention scores (0.42 / 0.31 / 0.15 / 0.07 / 0.05) | B02 | ☑ illustrative — plausible post-softmax weights that sum to 1.00, not values from a real model |
| Feed-forward = two linear maps with a non-linearity between; expands to a higher dimension then compresses back | B03 | ☑ factual |
| Expansion ratio 4× (d_model → 4·d_model) | B03 | ☑ standard for the original transformer, BERT, and GPT-2/3. Some newer models use other ratios; "4×" is the textbook value and is what the script states. |
| Activation labelled GELU | B03 | ☑ GELU is what BERT and GPT use; the original paper used ReLU. Script notes say either label is fine. |
| Residual: the original input is added back after each of the two sub-blocks; a layer that learns nothing passes the token through unchanged | B04 | ☑ factual |
| Layer norm rescales values into a stable range; without it activations drift across many layers | B04 | ☑ factual (simplified — "drift higher and higher" is the intuition, not a precise account of the instability) |
| **Layer norm placed after the add (post-norm)** | B04 | ⚠ **flagged simplification.** Post-norm is the original Vaswani arrangement and what the script's notes specify. Most modern models (GPT-2 onward, LLaMA, etc.) use *pre-norm* — norm before each sub-block, not after the add. Kept as scripted because it matches the source and the narration says "runs after each addition"; a viewer who goes on to read a modern architecture will find the norm in a different spot. Logged so this is a known choice. |
| Twelve layers = BERT; twenty-four = (BERT-large); ninety-six = GPT | B04, B05 | ☑ BERT-base is 12 layers, BERT-large is 24, **GPT-3 (175B) is 96**. "GPT" unqualified is loose — GPT-2 tops out at 48 — but the pairing of 96 with the largest well-known GPT is correct. |
| The running sentence "We expect revenue growth to moderate" | B01–B05 | ☑ illustrative — generic construction, no company, no real transcript |

**Standing rule:** the two flagged rows (single-head, post-norm) are
simplifications, not errors. If a future edit wants the video to reflect
modern practice, B04's norm boxes move to before each sub-block and the
narration line "runs after each addition" changes — that is a narration change
and needs GATE P again.

## Friction protected

- Kept: all five attention scores on screen in B02, not just the top two. The
  point is that scores are a *distribution* that sums to 1.0 — showing only
  the winners loses that.
- Kept: the "if attention learns nothing, the residual passes the token
  through unchanged" flash in B04. It is the single most important intuition
  about why deep stacks train, and it is a one-second animation.
- Kept: the full Input → Attention → Add & Norm → FFN → Add & Norm → Output
  structure at the end of B04, even though the narration only walks the first
  half in detail. The viewer needs to see the pattern *repeat* to believe it is
  a pattern.
- Kept: the dramatic stack extension to 96 in B05. It is the scale payoff for
  the whole video; a modest bump to 24 would not land it.

## Sign-off notes

1. Evidence table is per-claim. Two simplifications are flagged rather than
   silently shipped: single-head attention, and post-norm placement.
2. Narration-budget deviation on B02/B04 logged; both components are built to
   fill their real audio spans.
3. Dark-stage deviation for B01–B05 approved, matching the companion pieces.
4. Q/K/V color law logged.
5. Animated-slate review after `remotion_scenes.py` renders — frame-grab QC per
   VISUAL QC LAW, both orientations.

VERDICT: PASS
