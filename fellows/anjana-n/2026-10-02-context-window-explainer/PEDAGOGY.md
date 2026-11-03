# PEDAGOGY — What a Context Window Really Is (ai-explainer, narrated by Anjana)

Like ECIS Episode 9, this folder arrived with a **pre-written `script.md` and
`README.md`** alongside the narration and visual briefs. Both were **preserved
and extended, not rewritten** — see the authoring decisions below.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B06 (verdict) / B07 (handoff) /
  B08 (outro). B01–B05 illustrate the mechanism — the conveyor belt, the token
  split and the two bars, the quadratic grid and the VRAM meter, the U-shaped
  attention curve, the three strategies ✓
- SHOW-DON'T-TELL LAW: every body beat carries a `show` block; the evidence (the
  block falling off the belt, 128K next to a visibly shorter 96K, the grid
  quadrupling when the length doubles, the needle coming up empty in the middle)
  lives on screen ✓
- your-turn closing standard: B06 VERDICT → B07 YOUR TURN → B08 TITLE outro ✓
- Narrator: Anjana, no channel handle. Source `beats.json` says `am_onyx` —
  overridden to `af_bella` per the series convention ✓
- Dark-stage deviation: B01–B05 on the dark ground, same PEDAGOGY-approved
  deviation as the ECIS episodes and the other standalones.
- **NARRATION BUDGET:** body beats run 52–74 words. B03 (74) is marginally over
  the 45–70 range; noted below, not argued at length.

## Three authoring decisions

**1. The pre-written `script.md` and `README.md` were extended, not replaced.**
B01–B05 narration and visual direction are the author's text, with the single
exception in decision 2. What was added: the B00 ask, B06 verdict, B07 handoff,
B08 outro, and a header block. The script carries a note recording which parts
are authored and which were added, so the distinction stays in the file.

## Evidence discipline (DOUBLE-CHECK LAW)

No proprietary claims. Every statement is about how transformer LLMs work in
general, checkable against published work. Two rows needed real checking rather than a nod, and both are recorded below.

### Claims about how the technology works

| Claim (as scripted) | Where | Status |
|---|---|---|
| The model reads the whole context on each generation step, from a fixed-size buffer | B01 | ☑ standard |
| Context is measured in tokens, not words; tokenizers split into subword pieces | B02 | ☑ standard |
| One token ≈ ¾ of a word, so 128K tokens ≈ 96,000 words | B02 | ☑ the standard English rule of thumb, and the arithmetic is exact. See the honesty note below on what it depends on. |
| Attention scales quadratically with sequence length — double the length, quadruple the computation | B03 | ☑ standard for full attention |
| The KV cache stores key and value vectors for processed tokens so they are not recomputed | B03 | ☑ standard |
| At long context the cache alone consumes tens of gigabytes of VRAM | B03 | ☑ **checked, not assumed** — see below |
| LLMs attend more strongly to the beginning and end of the context than the middle ("lost in the middle") | B04 | ☑ a published, replicated finding, not folklore |
| Chunking, summarization and retrieval are the standard workarounds | B05 | ☑ standard |

**The VRAM figure was computed rather than quoted.** The brief asks for
"~40 GB (KV cache alone)" at 128K. For a large model with 80 layers, 8 KV heads
(grouped-query attention), head dimension 128, in fp16, the cache is
`2 (K and V) × 80 × 8 × 128 × 2 bytes` ≈ **0.33 MB per token**, and
`0.33 MB × 131,072 tokens ≈ 43 GB`. So the figure is defensible for a model of
that shape, and the narration's hedge ("a large model", "tens of gigabytes") is
doing real work — the number swings by an order of magnitude with layer count,
GQA ratio and precision. Logged as illustrative-but-derived, with the shape it
assumes stated here rather than implied on screen.

### Illustrative placeholders

| Figure | Where | Status |
|---|---|---|
| The four blocks on the belt and the one that falls off | B01 | ☑ illustrative |
| "understanding" = 1 token, "tokenization" = 3 | B02 | ☑ illustrative and **tokenizer-dependent** — the exact split differs between tokenizers; the point is that the split exists and is sub-word, not that these counts are universal |
| "128K tokens × 0.75 = ~96,000 words" | B02 | ☑ exact arithmetic on an approximate rule |
| The 1K→2K grid and its quadrupling area | B03 | ☑ illustrative, and the geometry is honest — doubling a side does quadruple the area |
| "~40 GB VRAM" and the filling memory bar | B03 | ☑ derived; see above |
| The U-shaped attention curve and the needle that comes up empty | B04 | ☑ illustrative — the *shape* is the published finding; the specific curve is drawn, not measured |


## Friction protected

- Kept: the block visibly **falling off** the belt in B01 rather than fading.
  A fade reads as "removed tidily"; falling off reads as "lost", which is the
  point.
- Kept: both bars in B02. "128K tokens is not 128K words" is an assertion until
  the shorter bar is sitting next to the longer one at visibly different length.
- Kept: the grid **quadrupling** in B03 rather than being described as
  quadrupling. It is the one place in the video where a viewer can see a
  quadratic cost rather than be told about it.
- Kept: the U-shape in B04 drawn as a continuous curve over the whole window,
  not as three labelled zones. The degradation is gradual, and three zones would
  imply a cliff that isn't there.

## Sign-off notes

1. No proprietary claims; the evidence table splits general-technology facts
   from illustrative placeholders, and the one figure that could have been
   quoted blind (the VRAM number) was derived here with its assumptions stated.
2. The author's `script.md` and `README.md` were extended rather than replaced.
3. The single narration edit — the B02 example — was confirmed with the author
   before audio spend and is logged above with its reasoning.
4. B03 runs 74 words, marginally over budget; noted rather than argued.
5. Animated-slate review after `remotion_scenes.py` renders — frame-grab QC per
   VISUAL QC LAW, both orientations.

VERDICT: PASS
