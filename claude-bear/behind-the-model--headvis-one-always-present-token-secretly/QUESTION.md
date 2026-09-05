# QUESTION

**The question:** Why does one always-present token secretly hijack every
attention statistic?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/headvis-one-always-present-token-secretly/beat_sheet.json`
(Teardown-register scaffold, `register: "Teardown"`, `builder: "ai-explainer"`,
cold open a stat-card `FormBCard` beat, body `FormBCard` GRAPHIC beats, Your
Turn, `ClaudeTitleOutro`). The source sheet was never rendered (all beats
`SLATE`, no media) but its narration was fully authored — every fact below
carries forward unchanged.

**Why it earns a reel:** softmax forces attention weights on every row to sum
to one, whether or not any key actually deserves the mass. Across a real head
(layer four, head three, fifty thousand sentences) the max-attention position
lands on token zero — the sentence-start marker, present in every sequence and
carrying no sentence-specific meaning — in 91% of cases, with more than half
the weight. Any statistic that reduces attention to "which position gets the
max" reports that sink, not the sentence structure the viewer actually wants
to see; the real verb-to-subject dependency only surfaces once token zero is
excluded from the count.

**Naive framing (B00, corrected on screen):** "Token zero keeps winning the
attention max — that must be the real signal, right?" → corrects "signal" to
"sink" (the real frame: winning the max by default is not the same as
carrying meaning).

**Body facts carried from source (unchanged):**
- the concrete case: layer 4, head 3, 50,000 sequences, max-attention position
  is token 0 with weight > 0.55 in 91% of cases; the verb→subject dependency
  only appears once position 0 is excluded from the max (source B00) — this
  is the reel's anchor, planted with the raw stat
- the question the source poses: softmax forces attention to sum to 1
  regardless of content, so why should one position consistently absorb the
  plurality of the mass across thousands of diverse inputs? (source B01)
- the tension: including a single structural token in an aggregation makes
  every meaningful attention pattern invisible (source B02)
- the mechanism: when no key is strongly preferred, softmax must still spend
  its probability somewhere; the ever-present, semantically-neutral BOS token
  becomes the low-resistance sink where heads park leftover attention, so any
  max-reduction that includes it reports the sink, not the structure (source
  B03) — kept near-verbatim, it already carries no design judgment
- the worked example: for "sat" in ["BOS","The","cat","sat",…], weights run
  roughly [0.58, 0.04, 0.12, 0.09, …]; position 0 wins the max in 94% of 1000
  sequences; after excluding position 0, "sat"→"cat" wins 68% (source B04)
- the visual object: an attention heatmap with column 0 glowing across every
  row; masking it lets diverse real patterns light up in the remaining
  columns (source metadata `visual_object`) — this is the reel's anchor
  payoff visual
- the your-turn ask: investigating attention and token 0 keeps dominating the
  max — ask what token 0 is typically doing (delimiter, start token, routing
  sink) and how to tell a genuine attention signal from a head parking weight
  on the separator (source YOURTURN)

**Compression, per the established hai-simple `behind-the-model` precedent
(e.g. `claude-liam-solve-verify-asymmetry`):** ten beats — B00 (writer) +
B01–B06 (body) + BCRY + BHTF + BOUT — matching the source's eight-beat shape
(B00–B05, YOURTURN, OUTRO) expanded by two beats to carry BOTH-DIRECTIONS
(a law the source scaffold never authored) without cutting any source fact.
B01 plants the anchor (the heatmap + the concrete 91%/verb-subject stat); B02
states the wrong guess (winning the max must mean carrying meaning); B03
breaks it with the mechanism (softmax must spend its mass somewhere, BOS is
the cheapest seat); B04 continues with the worked numeric example; B05 covers
direction A (a dominant sink doesn't mean the head learned nothing — the real
signal can still be in the non-max mass); B06 covers direction B (a head that
doesn't lean on BOS isn't automatically clean either — it may be parking on a
different filler token) and pays off the anchor with the masked heatmap.

**No inference flag.** Every claim restates the source's own stated mechanism
(softmax normalization forcing mass onto the lowest-resistance token) and its
measured example, not a leap about model internals beyond what the source
already asserts. Per `simple`'s ONE-FLAG LAW: "if the source genuinely
supports everything, there is no flag."

**No AI-video, no pantry, no paid step.** Source's cold-open and body beats
were already GRAPHIC (Remotion `FormBCard` stat cards) — none were AI-VIDEO,
pantry, or a human-drop slot, so no NO-GENAI/NO-PANTRY substitution was
needed beyond B00 becoming `BrutalistHesitantWriter` per WRITER LAW. Body
beats become bespoke Manim (a heatmap and its mechanism are better shown
drawn than as stat cards). GATE L (`./art scenes --check` on
`BrutalistHesitantWriter`, `WantQuote`, `ClaudeComposerAsk`, `OutroCTA`)
confirmed all four Remotion patterns renderable before slating.
