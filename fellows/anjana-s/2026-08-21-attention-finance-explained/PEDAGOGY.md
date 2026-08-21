# PEDAGOGY — Attention Is All You Need (To Read an Earnings Call) (ai-explainer, narrated by Anjana)

Fresh build from `script.md` + `visuals/*.md` (original pre-production briefs,
no source reel). One insight: self-attention isn't a bigger model or more
data — it's the ability to see the whole sentence at once, so a late word
("headwinds," "however," "excluding") can change the meaning of an early one
before any decision is made. Companion piece to `examples/finbert-explainer`
(same NLP-internals territory) but self-contained — this video is about the
mechanism itself, not about fine-tuning.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B06 (verdict) / B07 (handoff) /
  B08 (outro). B01–B05 illustrate the attention mechanism itself, using one
  running example sentence throughout — no UI wallpaper ✓
- SHOW-DON'T-TELL LAW: every beat carries a `show` block; evidence (the
  word-by-word coloring, the attention lines, the verdict bars, the
  pass/fail stamps) lives on screen ✓
- NARRATION BUDGET: all five body beats read within or close to the
  ~45–70-word body-beat range as scripted — no trim needed ✓
- your-turn closing standard: B06 VERDICT (`ClaudeVerdictArtifact`, handoff
  line "Let's recap with Claude.") → B07 YOUR TURN (`ClaudeComposerAsk`,
  prompt read aloud verbatim + discussed per HANDOFF LAW) → B08 TITLE outro
  (Anjana re-reads the title) ✓
- Narrator: Anjana narrates directly, no channel handle or brand chip.
  Source files say `am_onyx` — overridden to `af_bella` (Anjana's voice),
  matching the finbert-explainer companion build ✓
- Dark-stage deviation: B01–B05 render on the dark ground (`#0a0a0f`) rather
  than the default cream fidelity stage — matches the finbert-explainer
  companion piece's treatment of NLP-internals content; a deliberate, logged
  departure that needs an explicit human nod, not silent drift.
- **No invented company names, tickers, or real transcript quotes anywhere
  in this reel** — every example sentence (the running Beat 1 sentence and
  the three Beat 4 examples) is a generic, illustrative construction built
  to demonstrate the pattern, not a citation of any real earnings call.

## Evidence discipline (DOUBLE-CHECK LAW)

This video explains a well-established, public mechanism (self-attention,
as introduced in Vaswani et al.'s 2017 "Attention Is All You Need"), not a
proprietary system. **Human sign-off confirmed**:

| Claim (as scripted) | Where it appears | Confirmed accurate / clearly illustrative? |
|---|---|---|
| Self-attention: every token computes relevance to every other token in parallel, before any final decision | B03, B05 | ☑ factual — core transformer mechanism |
| "Attention Is All You Need" is the actual title of the 2017 paper that introduced the transformer | B05 (title riff) | ☑ factual |
| Older (pre-transformer) sequence models process text left-to-right and can't revisit an earlier token's interpretation once later context arrives | B02 | ☑ illustrative simplification — a fair pedagogical contrast against self-attention, not a literal claim about every pre-transformer architecture (e.g. bidirectional LSTMs existed too); framed as "the old way" for a clean two-beat comparison |
| The running example sentence and its "positive vs. cautious" readings | B01–B03, B05 | ☑ illustrative — invented CEO-speak, not a real transcript quote |
| The three Beat 4 finance examples and their without/with-attention verdicts | B04 | ☑ illustrative — invented sentences demonstrating the pattern, not benchmarked model outputs |

If any row would read to a viewer as a claim about a specific real system's
benchmarked behavior rather than an illustration of the general mechanism,
fix the beat's on-screen text before signing — never let an illustrative
demo pass as a verified result.

## Friction protected

- Kept: the single running sentence reused across Beats 1, 2, 3, and 5 — the
  through-line that makes "same sentence, two readings" legible; introducing
  a new sentence each beat would dilute the payoff.
- Kept: all three Beat 4 examples rather than trimming to one or two — the
  rhythm (accelerating, same template, three data points) is what sells
  "this is a pattern," not a one-off.

## Sign-off notes

1. Evidence table confirmed — the self-attention mechanism and the "Attention
   Is All You Need" reference are factually accurate; the "old way" framing
   and all example sentences are clearly illustrative, not citations.
2. Dark-stage deviation for B01–B05 approved, matching the finbert-explainer
   companion piece.
3. Animated-slate review (once `remotion_scenes.py` renders it) is
   acknowledged as still outstanding — will review after render.

VERDICT: PASS
