# Frictional log — Explainer: System One

## 2026-09-25 — claude-hai explainer (product teardown), 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G
Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(11/12, gate PASS), `system-one.mp4`, `short/system-one-short.mp4`.
Source: the TypeSafe "System One" docs I pasted in. (YouTube / Drive: TBD.)

**What I was working on.** An explainer on "System One" models (TypeSafe's Jev) — a
class of model that returns a typed, calibrated *decision* rather than generated text.
Built strictly from the product docs I supplied, framework-first (definition before
examples).

**What I tried, and what I expected.**
* I expected to take only what the docs state — it's a product I can't independently
  verify, so no invented benchmarks, pricing, or adoption; example values marked
  illustrative (the docs say so).

**Where it resisted, and what I did next.**
* B01 (the definition flow): the output chip text "typed answer + confidence"
  overflowed its box and the arrowhead clipped the first letters. Shortened to
  "a typed answer" (the "+ probability" already lives in the caption/footer).
* PROOF's real catch: the entire reel makes factual claims about one vendor's product
  with no on-screen source citation — a "no source, no verdict" gap for a product video.

**What Claude contributed, and what I did with it.**
* Mine: supplied the docs, chose to build it as a product explainer, GATE P, review.
* Claude's: authored from the docs under DOUBLE-CHECK (only what's stated, values
  flagged illustrative); fixed the overflow; ran PROOF and surfaced the citation gap.

**What I understand now, and what I still do not.**
* Understood: a product explainer should put "Source: … docs" on screen once — PROOF's
  own-standard rule applies to claims *about* a product, not just fact-checks.
* Not resolved: whether to add that citation; and whether TypeSafe/Jev is current.
