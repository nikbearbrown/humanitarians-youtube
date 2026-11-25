# FACTCHECK: Attention, One Head at a Time

Status: drafted and self-checked by the tldr-attention planning session, 2026-11-22. NOT yet signed off by the human (narration gate pending).

Verdicts:
- **✓** verified
- **✓ (minor)**: true with a qualifier (counts as a pass)
- **CORRECTED**: wrong in the draft, now fixed
- **WRONG**

"Executed" means the number was produced by `demo/attention_demo.py` (seed 290537), with the run in `demo/RUN-LOG.txt`. `make_sheet.py` asserts every spoken number against `evidence.json` before it writes the sheet.

The paper ("Vaswani") was checked against arXiv:1706.03762 (abstract page plus the ar5iv full text) on 2026-11-22.

- Script sha256: `7f79b621…7e15`
- Evidence sha256: `b48f90c9…6ceb` (full hashes at the end of RUN-LOG.txt)

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Attention is the step where words in a transformer read each other | ✓ | Self-attention: Q, K and V all come from the same sequence (Vaswani §3.2.3) | — |
| 2 | B00 | Draft: "a weighted average of all the words" | CORRECTED | The average is over **value** vectors, not over the words or their embeddings | Now "a weighted average of what all the words carry" |
| 3 | B00/B02 | Draft: "Attention never picks" | CORRECTED | Softmax weights are strictly positive, but they can be arbitrarily close to one-hot. "Never" overstated it. | Now "blends rather than picks" / "Attention doesn't pick" |
| 4 | B00 | "New meaning" = the head's weighted average | ✓ (minor) | Metaphor. In a full layer the head output is projected by *W^O* and **added** to the word's vector (residual connection). That is not taught and is logged as deferred in the sections card. | Tangent LHS says "what the head hands each word", which is accurate |
| 5 | B01 | Draft: every transformer LM runs this step "in every layer" | CORRECTED | Hybrid architectures replace some attention layers. The claim should not depend on architecture fashions. | Now "across many heads, layer after layer" |
| 6 | B01 | Four moves: project, score, softmax, sum | ✓ | Eq. 1 plus the Q/K/V projections (§3.2.1–3.2.2). The ÷√d_k is part of "score". | — |
| 7 | B03 | Dot product: "big when two lists point the same way" | ✓ (minor) | True for vectors of fixed length. Magnitude also matters. | Accepted for a one-line term |
| 8 | B03 | Softmax: positive weights that add up to one | ✓ | Definition | — |
| 9 | B10 | Chase's input row is unchanged when cats → kids, but its output moves | ✓ executed | `X[1]` untouched. The script asserts chase's query is unchanged. Output (1.1068, 1.6395) → (0.9307, 1.0644), a move of 0.6015. | — |
| 10 | B10 | Draft: "Nothing from outside the sentence went in" | CORRECTED | The learned matrices W^Q/W^K/W^V come from outside the sentence. Only the *other words* are the sentence. | Now "The head only sees these four words" |
| 11 | B11 | Half-and-half of cats (1, 2) and small (−1, −2) is the middle; 0.8 on cats moves toward cats | ✓ executed | (0, 0) and (0.6, 1.2) | — |
| 12 | B11 | With positive weights summing to one, the mix never leaves the shape | ✓ | Convex combination ⇒ inside the convex hull. The demo asserts the four value points are in convex position. | — |
| 13 | B11 | Values with two numbers; real heads use 64 | ✓ | Vaswani §3.2.2: d_k = d_v = 64 | Marked on screen as a simplification |
| 14 | B12 | Chase's request [1 0 1 0]; scores against the offers 3, 2, −1, −1 | ✓ executed | Products [2 0 1 0], [0 0 2 0], [0 0 −1 0], [−1 0 0 0] | — |
| 15 | B12 | Asking from small reshuffles the scores | ✓ executed | Small's query [1 1 −1 −1] gives scores [0 −3 2 −1] | — |
| 16 | B13 | Equal weights put all four words on the same point, the middle | ✓ executed | Every output = (0.5, 0.75) = mean of V. The script asserts `all_same`. | — |
| 17 | B14 | Divide each score by two | ✓ | √d_k = √4 = 2 | — |
| 18 | B14 | Softmax makes each row positive and sum to one | ✓ executed | Row sums are 1.000000 (unrounded) | — |
| 19 | B14 | Heat-map cells as shown add to one | ✓ (minor) | At two decimals, chase's row reads 0.99 and dogs' row 1.01 (rounding) | Dim caption on screen: "rounded; every row sums to 1" |
| 20 | B14/B15 | Chase's row: 0.53 cats, 0.32 itself, 0.07, 0.07 | ✓ executed | 0.5327, 0.3231, 0.0721, 0.0721 | — |
| 21 | B15 | The heat-map row used as blend weights lands exactly on the head's output | ✓ executed | The script asserts `O[1] == Σ a_1j v_j`. B15 lands on B10's point by construction. | — |
| 22 | B15 | Every other row lands somewhere of its own | ✓ executed | cats (1.11, 1.02), small (−0.28, −0.52), dogs (0.72, 1.33): four distinct points | — |
| 23 | B16 | Attention(Q,K,V) = softmax(QKᵀ/√d_k) V | ✓ | Vaswani Eq. (1), §3.2.1 | — |
| 24 | B16 | Request = query, offer = key, handed-over point = value | ✓ | Role names per §3.2. The analogy is a teaching gloss (SOURCE §2). | — |
| 25 | B17 | "d k is the length of a key, four here" | ✓ | d_k = 4 in the demo | — |
| 26 | B17 | Without the division, long keys make huge scores and softmax "stops blending and starts picking" | ✓ | Vaswani §3.2.1: large d_k pushes softmax toward regions with tiny gradients. Footnote: var(q·k) = d_k for unit-variance components. Executed: var 63.98 raw vs 1.00 scaled at d = 64. Toy row unscaled is [0.71 0.26 0.01 0.01] vs scaled [0.53 0.32 0.07 0.07]. | — |
| 27 | B17 | √d_k is "a design choice" (values claim) | ✓ | The paper presents it as a remedy ("we suspect…"), not a theorem. Other scalings exist (e.g. 1/d in some width-scaling schemes). | Stated as contestable, per EQUATIONS.md zone 5 |
| 28 | B18 | Chase's request scored 3 against cats' offer but −1 against kids' | ✓ executed | kids key [0 1 −1 0] · [1 0 1 0] = −1 | — |
| 29 | B18 | The weight drains mostly back onto chase itself | ✓ executed | Chase→chase weight 0.3231 → 0.5990. Kids, small and dogs get 0.1337 each. | — |
| 30 | B19 | Reordered, every word lands on exactly the same point | ✓ executed (minor) | Outputs permute identically. The maximum difference is 2.2e−16 (floating-point summation order). The demo asserts the weights permute as A[perm, perm]. | "Exactly" is true to every displayed digit |
| 31 | B19 | Draft: "Transformers fix this by adding a position signal to each word's numbers" | CORRECTED | True of the original (§3.5: positional encodings *added* to the input embeddings). Many later models instead use rotary or relative schemes applied inside attention. | Now "The original transformer fixes this by adding…" |
| 32 | B19 | With position added, cats lands somewhere new | ✓ executed | Sinusoidal PE (§3.5 formula) added to X: cats (−0.756, −1.199) vs (−1.322, −2.143), moved 1.10 | — |
| 33 | BVDT | Q, K, V come from "three learned grids" | ✓ | In a real model W^Q, W^K, W^V are learned. In the demo they are seeded toys, and B10 says so on screen. | — |
| 34 | BHTF | Reversing the words only reorders the outputs (rubric) | ✓ | Permutation equivariance; row 30 | — |

## Algebra checks (MATH-TYPESETTING.md)
- **Shapes.** X is 4×4. W_Q and W_K are 4×4, so Q and K are 4×4. W_V is 4×2, so V is 4×2. QKᵀ is (4×4)(4×4)ᵀ = 4×4. softmax(·)V is (4×4)(4×2) = 4×2: one 2-number output per word ✓.
- **Indices.** (QKᵀ)_ij = q_i · k_j. Row *i* is the asker (query) and column *j* is the one asked (key). The softmax runs over *j* (along each row), not down the columns. The weights' row *i* multiplies V, so output_i = Σ_j a_ij v_j ✓.
- **The √ applies to d_k (the key length), not to d_model.** They are equal here (both 4), which makes the B16 narration "root d" ambiguous. The B17 tangent narrates "d k is the length of a key", and the MathTex shows √d_k.
- **Sign / domain.** d_k > 0, so √d_k is real. Softmax outputs lie in (0, 1) and sum to 1. "=" is an identity (a definition of the head's output), and the narration reads it as "a promise: same thing, row for row".
- **Numeric case (chase).**
  - Scores: 3, 2, −1, −1 → ÷2 → 1.5, 1, −0.5, −0.5.
  - e^x = 4.4817, 2.7183, 0.6065, 0.6065. The sum is 8.4130.
  - Weights: 0.5327, 0.3231, 0.0721, 0.0721.
  - Output x = 0.5327·1 + 0.3231·2 + 0.0721·(−1) + 0.0721·0 = 1.1068 ✓.
  - Output y = 0.5327·2 + 0.3231·2 + 0.0721·(−2) + 0.0721·1 = 1.6395 ✓.
- **Numeric case (kids swap).** Scores −1, 2, −1, −1 → ÷2 → e^x = 0.6065, 2.7183, 0.6065, 0.6065. The sum is 4.5378, so chase's weight on itself is 2.7183 / 4.5378 = 0.5990 ✓.
- **Positional encoding formula in code.** The loop index `i` steps 0, 2, so `i/d` = 2i'/d_model, matching §3.5 ✓.

## Datable content
No model names, parameter counts, dates or "today" claims appear in the narration. "The original transformer" refers to a fixed historical paper.

## Format conversion, 2026-11-24 (appended; the rows above are unchanged)

The film was converted from TL;DR to ai-explainer. TL;DR beats B00–B03 are retired (rows 1–8 covered them), and their wording no longer appears in the film. The body (B10–B19), BVDT, BHTF and BOUT are unchanged, so rows 9–34 still apply. Narration approval: the original narration on 2026-11-22 ("approve all six"); the new B00 and B01 on 2026-11-24, by Anant.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 35 | B00 (spoken) | "How does a transformer let each word use the words around it? … Show me one attention head, with real numbers." | EXEMPT | The ask: a question, not a claim | — |
| 36 | B00 (on screen) | "the mix: each word becomes a weighted average of every word" | FLAG | The same simplification row 2 corrected. The average is over the words' **value** vectors, not the words. Accurate wording: "a weighted average of what every word carries". On screen only; not spoken. | Kept as is: Anant decided on 2026-11-24 not to re-render (on screen only; the narration is accurate) |
| 37 | B00 (on screen) | "worked example: chase puts 0.53 of its weight on cats" | ✓ executed | Row 20: 0.5327 | — |
| 38 | B00 (on screen) | "the limit: attention alone can't see word order" | ✓ executed | Rows 30–32: reordered outputs permute identically; position has to be added | — |
| 39 | B01 | "Each word in a sentence blends every word around it. It doesn't pick one." | ✓ (minor) | The same metaphor as the approved "blend the words around it" and row 3's "doesn't pick". Strictly, the blend is of the words' values. | — |
| 40 | B01 | "It takes a weighted mix, weighted by how well two words match." | ✓ | The weights are the softmax of query · key scores (rows 14, 18) | — |
| 41 | B01 | "Every transformer runs on this step." | ✓ (minor) | Attention defines a transformer. Unlike the draft row 5 corrected, this makes no "every layer" claim. | — |
