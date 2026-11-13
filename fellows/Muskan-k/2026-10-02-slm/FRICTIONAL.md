# Frictional log — Explainer: Small Language Models

## 2026-10-02 — claude-hai explainer, 16:9 + 9:16
- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G
Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(11/12, gate PASS), `slm.mp4`, `short/slm-short.mp4`. (YouTube / Drive: TBD.)

**What I was working on.** An explainer on Small Language Models (SLMs), framework-first:
size is a trade, not a score — for a narrow, repeated task a small specialized model can
match a big general one (faster, cheaper, private), but the big model still wins for
open-ended / broad / novel work.

**What I tried, and what I expected.**
* I wanted it to stay non-dating, so I deliberately avoided parameter counts, benchmark
  numbers, and model names — all comparisons qualitative.

**Where it resisted, and what I did next.**
* The qualitative framing is safe but it creates one tension: the worked example (B03,
  ticket routing) claims a small model "routes as well as a frontier model." PROOF
  flagged that as the one place I *assert* a comparison without showing evidence. Left
  it, but noted the fix (soften to "can match, on a task this narrow", or show a real
  before/after).

**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework (size is a trade), GATE P, review.
* Claude's: authored the reel with the qualitative framing; rendered/compiled; ran PROOF
  and surfaced the assert-without-evidence finding.

**What I understand now, and what I still do not.**
* Understood: avoiding specific numbers keeps a concept reel from dating — but any
  comparative claim ("matches X") still wants either evidence or softer wording.
* Not resolved: whether to soften B03's claim or add a real benchmark.
