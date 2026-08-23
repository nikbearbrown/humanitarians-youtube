# PEDAGOGY — FinBERT: BERT, Fine-Tuned for Finance (ai-explainer, narrated by Anjana)

Fresh build from `script.md` + `visuals/*.md` (original pre-production briefs,
no source reel). One insight: FinBERT isn't a new architecture — it's the
same BERT, reshaped by different training data, which is why the same word
("decline") can mean opposite things depending on what it's next to.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B06 (verdict) / B07 (handoff) /
  B08 (outro). B01–B05 illustrate the FinBERT mechanism itself — no UI
  wallpaper ✓
- SHOW-DON'T-TELL LAW: every beat carries a `show` block; evidence (the
  pass/fail tags, the general-vs-financial column pairs, the training
  stream, the attention web, the probability bars) lives on screen ✓
- NARRATION BUDGET: two source fixes made before signing:
  1. `narration/05_close.txt` was truncated versus `script.md` — cut off
     after "It stops reading words," missing "It starts reading money,"
     which is the exact line the B05 visual brief syncs its payoff to
     (FinBERT growing to fill the frame). Restored the full line from
     `script.md` — the beat doesn't work without it.
  2. B03 and B04's narration ran ~85 words each in the source, over the
     ~70-word body-beat budget. Trimmed to ~65/~62 words by moving
     secondary detail onto on-screen-only captions ("in line with
     expectations → neutral, not positive" on B03; "that is the key"
     filler cut on B04). Nothing was cut that isn't still shown on screen.
- your-turn closing standard: B06 VERDICT (`ClaudeVerdictArtifact`, handoff
  line "Let's recap with Claude.") → B07 YOUR TURN (`ClaudeComposerAsk`,
  prompt read aloud verbatim + discussed per HANDOFF LAW) → B08 TITLE outro
  (Anjana re-reads the title) ✓
- Narrator: Anjana narrates directly, no channel handle or brand chip.
  Source files say `am_onyx` — overridden to `af_bella` (Anjana's voice) ✓
- Dark-stage deviation: B01–B05 render on the dark ground (`#0a0a0f`) rather
  than the default cream fidelity stage — this suits the training-stream
  and attention-web visuals better than the cream ground would. ai-explainer
  is normally a FIDELITY-palette skill, so this is a deliberate, logged
  departure that needs an explicit human nod, not silent drift.
- **No invented company names or tickers anywhere in this reel** — this
  topic never needed any; it's pure NLP-internals content (tokens,
  attention, a classification head), not a claim about any real company's
  filings.

## Evidence discipline (DOUBLE-CHECK LAW)

This describes a real, published model (FinBERT) and a real architecture
(BERT/transformers), not an external article being summarized. **Human
sign-off must confirm**:

| Claim (as scripted) | Where it appears | Confirmed accurate / clearly illustrative? |
|---|---|---|
| BERT reads text bidirectionally and understands context in general English | B00, B01 | ☑ factual — established BERT property |
| BERT can misclassify financial hedge language (e.g. reading "narrow margin" as positive sentiment) | B01 (illustrative demo, not a citation of a specific benchmark run) | ☑ illustrative — reads as demo, not citation |
| FinBERT = BERT fine-tuned on a financial-text corpus; architecture unchanged, weights change | B03, B06 | ☑ factual — matches published FinBERT approach |
| "Fifty thousand financial sentences" as the fine-tuning corpus size | B03 (order-of-magnitude figure) | ☑ illustrative — order of magnitude, not an exact cited count |
| Self-attention mechanism: every token attends to every other token in parallel, not left-to-right | B04 | ☑ factual — core transformer property |
| Classification head outputs 3 probabilities (positive/negative/neutral) | B04 | ☑ factual — matches FinBERT's sentiment head |
| "~10ms" inference speed for one sentence | B04 (illustrative order-of-magnitude, not a benchmarked number on specific hardware) | ☑ illustrative, framed as approximate |
| Example probability output (0.24 / 0.11 / 0.65) for "We expect moderate growth in the second half" | B04 (illustrative example output, not a live model run) | ☑ illustrative example |

If any row is wrong or the real FinBERT specifics differ (corpus size,
speed, architecture details), fix the beat's narration/on-screen text before
signing — never let an illustrative number pass as a verified benchmark.

## Friction protected

- Kept: the "revenue decline vs. expense decline" contrast in B03 — this is
  the single clearest demonstration of what fine-tuning actually changes,
  cutting it for time would gut the thesis.
- Kept: the attention-web beat (B04) as the visual centerpiece per the
  script's own production notes — this is the "wow" moment, not filler.

## Sign-off notes

1. Evidence table confirmed — factual claims accurate, illustrative
   figures (corpus size, inference speed, example probabilities) framed
   as approximate/illustrative rather than cited benchmarks.
2. The two source-text fixes (restored B05 punchline, trimmed B03/B04
   narration) confirmed to read correctly against the original intent.
3. Animated-slate review (once `remotion_scenes.py` renders it) is
   acknowledged as still outstanding — will review after render.

VERDICT: PASS
