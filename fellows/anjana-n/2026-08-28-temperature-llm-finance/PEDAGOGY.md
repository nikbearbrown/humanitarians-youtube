# PEDAGOGY — Temperature: The Dial Between Prediction and Hallucination (ai-explainer, narrated by Anjana)

Fresh build from `script.md` + `visuals/*.md` (original pre-production briefs,
no source reel). One insight: temperature isn't a quality knob, it's a
randomness knob — turning it up doesn't make a model smarter, it makes it
less likely to agree with itself, which is exactly the wrong property for
financial extraction. Companion piece to `examples/attention-finance` (same
NLP-internals territory) but self-contained — this video is about sampling
randomness, not the attention mechanism.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B05 (verdict) / B06 (handoff) /
  B07 (outro). B01–B04 illustrate the temperature mechanism itself, using
  the recurring dial icon and one running example quote — no UI wallpaper ✓
- SHOW-DON'T-TELL LAW: every beat carries a `show` block; evidence (the
  token-probability bars, the three-run comparison columns, the dial
  position) lives on screen ✓
- NARRATION BUDGET: all four body beats read within or close to the
  ~45–70-word body-beat range as scripted — no trim needed ✓
- your-turn closing standard: B05 VERDICT (`ClaudeVerdictArtifact`, handoff
  line "Let's recap with Claude.") → B06 YOUR TURN (`ClaudeComposerAsk`,
  prompt read aloud verbatim + discussed per HANDOFF LAW) → B07 TITLE outro
  (Anjana re-reads the title) ✓
- Narrator: Anjana narrates directly, no channel handle or brand chip.
  Source files say `am_onyx` — overridden to `af_bella` (Anjana's voice),
  matching the attention-finance companion build ✓
- Dark-stage deviation: B01–B04 render on the dark ground (`#0a0a0f`) rather
  than the default cream fidelity stage — matches the attention-finance and
  finbert-explainer companion pieces' treatment of NLP-internals content; a
  deliberate, logged departure that needs an explicit human nod, not silent
  drift.
- **No invented company names, tickers, or real transcript quotes anywhere
  in this reel** — the earnings quote and every three-run comparison is a
  generic, illustrative construction, matching the precedent set by
  attention-finance.

## Evidence discipline (DOUBLE-CHECK LAW)

This video explains a well-established, public LLM sampling mechanism
(temperature scaling of the output softmax distribution) plus a published
decoding technique (self-consistency), not a proprietary system. **Human
sign-off confirmed**:

| Claim (as scripted) | Where it appears | Confirmed accurate / clearly illustrative? |
|---|---|---|
| Temperature 0 = greedy decoding — always picks the single highest-probability token, deterministic output for a fixed input | B01, B02 | ☑ factual — standard decoding behavior |
| Raising temperature flattens the softmax output distribution, giving lower-probability tokens more chance of being sampled | B02 | ☑ factual — core temperature-scaling mechanism |
| Financial/extraction systems generally favor low temperature for reliability; high temperature suits creative generation | B02, B03 | ☑ factual as general, well-accepted practice — not a citation of one specific system's configuration |
| Self-consistency decoding: sample the same prompt multiple times, take a majority vote | B03 | ☑ factual — published technique (Wang et al., "Self-Consistency Improves Chain of Thought Reasoning") |
| The running earnings quote and every three-run extraction result (confidences, directions) | B01, B03 | ☑ illustrative — invented construction, not a real transcript or a live model run |
| Token-probability bar chart shapes at T=0.0 / 0.5 / 1.0 | B02 | ☑ illustrative — shape is representative of the real mechanism, exact bar heights are not measured data |

If any row would read to a viewer as a claim about a specific real system's
benchmarked behavior rather than an illustration of the general mechanism,
fix the beat's on-screen text before signing — never let an illustrative
demo pass as a verified result.

## Friction protected

- Kept: the twitch-and-snap close (Beat 4) rather than a plain fade-out —
  it's the visual punchline that makes "creativity is for poets, consistency
  is for predictions" land as an argument, not just a tagline.
- Kept: all three T=1.0 runs landing on three different directions in Beat
  3, rather than softening it to two-out-of-three — the chaos at high
  temperature is the whole point of the contrast with T=0's lock.

## Sign-off notes

1. Evidence table confirmed — the temperature mechanism and self-consistency
   reference are factually accurate; the running quote and all three-run
   comparisons are clearly illustrative, not citations.
2. Dark-stage deviation for B01–B04 approved, matching the attention-finance
   and finbert-explainer companion pieces.
3. Animated-slate review (once `remotion_scenes.py` renders it) is
   acknowledged as still outstanding — will review after render.

VERDICT: PASS
