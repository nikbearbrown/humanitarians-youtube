# PEDAGOGY.md — Your Eval Is Lying to You (GATE P)

**Reel:** `hai-your-eval-is-lying` · 16 beats · Bella (`af_bella`) · Humanitarians AI
**Projected:** 3m57s · **Source:** `Worked_Examples_in_Generative_AI_Prompt_Engineering_&_Evaluation.ipynb`

---

## 1. What the reel teaches

One thesis: **an evaluation harness is code, and nobody reviews it.**

The notebook compares baseline vs chain-of-thought prompting across a knowledge dataset
(geography) and a reasoning dataset (arithmetic), scored with exact match and token F1.
That design is sound. The reel does not dispute it. What the reel takes apart is the
*measurement*, which has three defects that between them make a perfect model look broken.

| # | Bug | Beat |
|---|---|---|
| 1 | The model was never called. `OPENAI_AVAILABLE` was False, every prediction is the literal `"MOCK_OUTPUT"`, every metric is `0.0`, and `plt.show()` rendered four zero bars without error. | B04–B06 |
| 2 | `normalize_text` strips non-ASCII, so `normalize("Brasília")` → `'bras lia'` — two tokens — and can never match the unaccented spelling a model emits. | B07–B08 |
| 3 | The allow-list `[^a-z0-9\s\.\-]` **preserves the full stop**, so `"...is Paris."` tokenizes to `paris.` which never matches `paris`. A correct answer scores 0 on EM *and* 0 on F1. | B09 |

The fix (B11) is four lines: NFKD-fold to ASCII, and remove `\.` from the allow-list.

## 2. Provenance of every number on screen

**No figure in this reel was typed by hand.** `build_beat_sheet.py` contains the notebook's
`normalize_text`, `extract_final_answer`, `exact_match` and `f1_tokens` copied verbatim, and
recomputes the scoreboard and the before/after bars at build time. Re-run the script and the
beat sheet regenerates from the code itself. If the notebook's functions change, the video's
numbers change with them.

Computed values, reproducible by running the script:

```
Paris                            Paris       EM=1 F1=1.00
The capital of France is Paris.  Paris       EM=0 F1=0.00
Delhi                            New Delhi   EM=0 F1=0.67
Brasilia                         Brasília    EM=0 F1=0.00
Final answer: 7                  7           EM=1 F1=1.00

BEFORE (notebook normalizer) = 0.60      AFTER (fixed) = 1.00
```

## 3. The honesty boundary — read this one

**No LLM was called.** The notebook could not reach a model, and this reel deliberately did
not run it either (free-only toolkit, no API keys). Therefore:

- **The reel makes no claim about model performance, or about whether chain-of-thought
  beats baseline.** That question is genuinely unanswered by this notebook and the video
  says so rather than filling the gap.
- **The five predictions in the scoreboard are illustrative inputs** — the *shapes* of answer
  a model returns (bare, verbose, partial, unaccented, prefixed). They were written, not
  sampled from a model. What is real and measured is the **scorer's response to them**.
- The `0.60 → 1.00` result is a measurement **of the harness**, not of any model.

If this is ever presented as an empirical comparison of prompting strategies, that would be
a misrepresentation. It is a code review of an evaluation, and should be described that way.

## 4. Where it could still mislead

- B01 says the design is "reasonable," which is a judgment, not a finding.
- The reel implies the three bugs are the *only* problems. They are the ones surfaced by
  running the scoring functions; the prompts and datasets were not separately audited.
- `extract_final_answer` falls back to returning the whole string when the regex misses.
  That is arguably a fourth latent bug — silently scoring reasoning text as the answer —
  but it never fires on these examples, so the reel does not claim it.

## 5. Naming

The notebook carries a personal copyright line. **No individual is named** in narration or
on screen. A programmatic guard in `build_beat_sheet.py` checks all five spellings and
reports CLEAN.

## 6. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Audio generated with `--no-gate`, on the record. §3 is the section that most needs your
judgment: the reel critiques your own notebook, and the framing must stay "the measurement
was broken," never "the prompting was bad." Replace this block with `VERDICT: PASS` and a
date once you have read it.
