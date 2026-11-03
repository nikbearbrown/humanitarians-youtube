# PEDAGOGY.md — Finishing Your Sentences (GATE P)

**Reel:** `hai-finishing-your-sentences` · 21 beats · Bella (`af_bella`) · Humanitarians AI
**Audience:** children / complete beginners; watchable by an adult without condescension.
**Source:** a from-scratch GPT notebook, 73 cells, NumPy and Matplotlib only.

---

## 1. This reel teaches. It is not a teardown.

The source notebook is unusually rigorous, and the reel reflects that rather than
hunting for faults. Four things it does that most tutorial code does not:

1. **A hand-written autodiff engine, with its own gradient check** (cell 26) — worst
   relative error `4.81e-07`.
2. **A second gradient check on the full Transformer** (cell 36) — `7.98e-06`.
3. **A copy-task sanity check before the real run** (cells 40–42). The model must learn
   to echo a random sequence, reaching `100.0%`, before anything harder is attempted.
4. **A KV-cache correctness check** (cells 64–66) — the fast path is verified to give the
   same output as the slow path before being used.

B08, B09 and B16 carry those directly, and B09's line — *"a machine that cannot do that
has no business trying anything harder"* — is the reel's thesis about method.

## 2. Provenance

`build_beat_sheet.py` **parses** every figure out of the notebook's recorded stream
outputs (cells 6, 8, 11, 13, 15, 17, 26, 36, 40, 44, 46, 57, 65, 68). Nothing is
transcribed by hand. Nine assertions guard the result:

```
corpus 2,053,690 chars from 73 files · spaces 28.8% · V = 96
choices: uniform 96 -> bigram 11.5 -> GPT 4.6
gradient checks 4.81e-07 (engine) / 7.98e-06 (full model)
copy task 100.0% in 5.5s · 116,480 params · loss 4.59 -> 1.379 train / 1.529 val in 213s
cache 47 -> 22 ms · 2,016 -> 63 positions (32x less work)
```

## 3. The one derived quantity, and why

Cross-entropy loss means nothing to a child, so the reel converts it with `exp(loss)` into
**"how many characters is it still choosing between"**:

| | loss | choices |
|---|---|---|
| guessing blindly | 4.564 | 96 |
| counting letter pairs | 2.443 | 11.5 |
| the finished model | 1.529 | 4.6 |

This is exact, not a simplification — perplexity *is* `exp(loss)`, and the notebook's own
cell 4 introduces it the same way. An assertion checks that `exp(uniform)` recovers the
vocabulary size, which it does to within 1.0.

## 4. How the hard ideas are carried

| Real concept | What a child sees |
|---|---|
| next-token prediction | a guessing game: what letter comes next? |
| perplexity | how many letters are still in the running |
| BPE tokenization | inventing shortcuts by gluing common pieces together |
| causal self-attention | each letter looks back; thicker line, more attention |
| the causal mask | "no peeking — the answer is right there" |
| gradient checking | working it out by hand, then counting it a second way |
| the copy task | an easy exam before the hard one |
| temperature | a dial for how adventurous to be |
| KV caching | remembering instead of re-reading the whole page |

No equations appear on screen. "Transformer", "attention", "perplexity" and "tokenizer"
are deliberately absent from the narration.

## 5. Honesty notes

- B14's four generated samples are quoted from the notebook's own cell 54 output,
  truncated to fit one line each. They are real output, not invented examples.
- The attention visual in B06 is a **schematic** of causal attention, not a replay of the
  notebook's attention maps. Cell 60 notes real maps are "messier than the copy task's
  clean stripe" — the reel does not claim otherwise.
- B17's "about 90 billion times more" is the notebook's own `9e+10` figure, converted to
  words so it can be spoken. The underlying comparison is theirs.
- No training was re-run. All model-dependent numbers are the notebook's recorded run.

## 6. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Generated with `--no-gate`, on the record. Two checks for this cut: read it as a child
would, and confirm §1's characterisation — the reel praises this notebook's method by
name, so that praise should match your own reading.
