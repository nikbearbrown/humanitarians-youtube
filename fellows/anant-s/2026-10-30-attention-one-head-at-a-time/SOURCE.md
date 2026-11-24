# SOURCE: Scaled dot-product attention, one head

This is the written source the `tldr` film is cut from. We wrote it ourselves because tldr expects written material, and it was fact-checked against the original paper on 2026-11-22 (see SOURCES.md). The film does not name it on screen (BOOKLOOP law).

Primary reference: A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, I. Polosukhin, "Attention Is All You Need," *NIPS 2017* (31st Conference on Neural Information Processing Systems), arXiv:1706.03762. Section numbers below refer to that paper.

---

## 1. The problem attention solves

A transformer turns each word (in practice, each token) into a list of numbers called an **embedding**. Most of what an embedding means depends on context: "chase" in *cats chase small dogs* is not "chase" in *kids chase a ball*. Each word therefore has to take information from the other words in the sentence. **Self-attention** is the step that does this. Every word looks at every word, itself included, and builds a new vector out of what it finds.

## 2. Three projections: query, key, value

Each word's embedding *x* (a row of the matrix *X*) is multiplied by three learned matrices (§3.2.2):

- **query** *q = x W^Q*: what this word is looking for
- **key** *k = x W^K*: what this word offers to be found by
- **value** *v = x W^V*: what this word hands over if it is attended to

Stacking the rows gives *Q = XW^Q*, *K = XW^K* and *V = XW^V*. Queries and keys have length *d_k*, and values have length *d_v* (§3.2.1). The words "query", "key" and "value" are labels for roles. Nothing in the arithmetic forces the interpretation; training is what makes the projections useful.

## 3. Scores, scaling, softmax

The match between word *i*'s query and word *j*'s key is their **dot product**, *q_i · k_j*. All the matches at once form the matrix *QKᵀ*, which is *n × n* for *n* words: row *i* holds how well word *i*'s query matches every key.

The scores are divided by √*d_k*. The paper's reason (§3.2.1): for large *d_k*, dot products grow large in magnitude. That pushes softmax into a region where one weight is close to 1, the rest are close to 0, and the gradients are extremely small. Its footnote gives the arithmetic: if the components of *q* and *k* are independent with mean 0 and variance 1, then *q · k* has mean 0 and variance *d_k*. Dividing by √*d_k* brings the variance back to 1. (Our demo checks this empirically: with *d* = 64 and 100,000 random pairs, the variance is 63.98 raw and 1.00 after dividing by 8.)

**Softmax** is then applied to each row separately. Softmax exponentiates each score and divides by the row's total, so every weight is strictly positive and every row sums to 1. The result is the matrix of **attention weights**, usually drawn as a heat map: rows are the words doing the asking, columns are the words being attended to.

## 4. The weighted sum of values

Each word's output is its row of weights applied to the value vectors:

  output_i = Σ_j a_ij v_j

The weights are positive and sum to one, so this is a **weighted average** of the values. Geometrically, the output lies inside the convex hull of the value vectors, pulled toward the values with the largest weights. In matrix form the whole head is Equation (1) of the paper:

  **Attention(Q, K, V) = softmax(QKᵀ / √d_k) V**

That is the mechanism the film teaches: *each word's new vector is a weighted average of every word's value, and the weights come from query·key similarity.*

Softmax never gives a weight of exactly zero, so attention always blends; it never selects just one word. A weight can come close to 1, which is how a head can act almost like a lookup.

## 5. Why not equal weights?

If every word gave every word the same weight (1/*n*), every word's output would be the same vector, the plain average of the values. The scores are what make the outputs differ from word to word.

## 6. What attention does not do on its own: word order

The computation above treats the sentence as a *set*. Reorder the words and *Q*, *K* and *V* reorder their rows. The weight matrix has its rows and columns permuted the same way, and each word's output vector is unchanged; it just appears in a new position. (Formally, self-attention is permutation-equivariant.) So *cats chase small dogs* and *dogs chase small cats* give "cats" exactly the same output.

The paper's fix (§3.5): the model has no recurrence and no convolution, so position information must be injected. The authors **add positional encodings to the input embeddings** at the bottom of the encoder and decoder stacks. They use sinusoids: PE(pos, 2i) = sin(pos / 10000^(2i/d_model)) and PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model)). Later models often use other position schemes, such as learned or rotary encodings. The principle is the same: order has to be supplied, because attention cannot see it.

## 7. One head, many heads, and what this source leaves out

The paper runs *h* = 8 heads in parallel, each with its own *W^Q*, *W^K* and *W^V* and with *d_k = d_v = d_model / h* = 64 (*d_model* = 512, §3.1–3.2.2). The heads' outputs are concatenated and projected by a further matrix *W^O*. In a full transformer layer, that result is added back to each word's vector (a residual connection) and normalized, and a feed-forward network follows.

These parts are deliberately **not** taught in the film: multi-head concatenation and *W^O*, residual connections and normalization, causal masking in decoders, and how training sets the weights. The film covers one head only, with toy numbers: *d_model* = 4, *d_k* = 4 (so √*d_k* = 2) and *d_v* = 2, so that each value and output is a point on a plane.

The paper also compares dot-product attention with additive attention (§3.2.1). The two are similar in theoretical complexity, but dot-product attention is much faster and more space-efficient in practice, because it uses optimized matrix multiplication.
