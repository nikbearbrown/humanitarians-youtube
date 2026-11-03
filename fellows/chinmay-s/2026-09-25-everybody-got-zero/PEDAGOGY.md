# PEDAGOGY.md — The Test Where Everybody Got Zero (GATE P)

**Reel:** `hai-everybody-got-zero` · 22 beats · Bella (`af_bella`) · Humanitarians AI
**Audience:** children / complete beginners. Watchable by an adult without feeling talked down to.
**Source:** the same prompt-engineering notebook as `hai-your-eval-is-lying` (verified
byte-identical in source — only the filename differs).

---

## 1. What makes this the kid cut

The technical content is **unchanged**. What changed is how it is carried:

| Concept | How the kid cut carries it |
|---|---|
| trailing-punctuation bug in `normalize_text` | a full stop stuck to the word **like chewing gum** |
| unicode stripping (`[^a-z0-9\s\.\-]`) | a **machine that eats letters**, snapping Brasília into "bras lia" |
| exact match | "every letter must line up, or nothing" — named once, after it is shown |
| token-overlap F1 | "count how many words match" — partial credit, no formula on screen |
| `except Exception: OPENAI_AVAILABLE = False` | the **robot was never switched on**, and the test carried on regardless |
| golden tests for the scorer | "hand the marker an answer you already know is right" |

Rules followed throughout: short sentences, concrete nouns, no unexplained jargon, and
every technical term shown before it is named. No regex appears on screen anywhere.

## 2. Nothing was dumbed down into being wrong

Every figure is still recomputed at build time by the notebook's **own** scoring functions,
copied verbatim into `build_beat_sheet.py`, and guarded by five assertions:

```
broken marker EM = 0.60   mended EM = 1.00
"Delhi" vs "New Delhi"  F1 = 0.67
"The capital of France is Paris." vs "Paris"  F1 = 0.00
normalize("Brasília") -> 'bras lia'
```

The 60% → 100% in B16 is a real measurement of a real fix, not an illustration.

## 3. The cast

Two characters, both built only from cream, warm ink and the single terracotta accent —
cartoon **behaviour** (squash-and-stretch, anticipation, overshoot, bob, wobble), never
cartoon colour. `Grader` is reused from `EvalCartoon.tsx`; `Robo` is new in `KidEval.tsx`.

Eight of the 22 beats are character scenes; the rest are the Claude-skin statement cards
and bookends, so the reel still reads as part of the same series.

## 4. Honesty notes

- The five prediction/gold pairs in B16 are **illustrative inputs** — the shapes of answer
  a model returns. What is measured is the scorer's reaction to them, which is real.
- The reel makes **no claim** about whether chain-of-thought beat the baseline prompt. The
  notebook never called a model, so that question is genuinely unanswered, and the kid cut
  does not fill the gap with a guess.
- B09 says "the robot was never switched on." Precisely: the OpenAI client failed to
  construct, `OPENAI_AVAILABLE` was set to `False`, and `call_model` returned the literal
  string `MOCK_OUTPUT`. The metaphor is accurate, not a simplification that misleads.

## 5. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Generated with `--no-gate`, on the record. Worth one extra check for this cut: read it as
a child would and confirm no sentence needs a second pass.
