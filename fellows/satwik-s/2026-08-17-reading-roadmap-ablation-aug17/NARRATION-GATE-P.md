# NARRATION — GATE P — "What an Ablation Can (and Can't) Decide" · Full-Book Tagging

**Voice:** Kokoro `af_bella` ("Bella"). **Register:** Pragmatist / skeptical-explainer. **Narrator:** Satwik.
Framework-FIRST (PROOF): B01 shows the 4-question frame before any result. The falsifiability beat is
B05 (the ceiling: an ablation can't say which is *correct*). Every on-screen agreement number carries
its `n`. Review on the animated slate before any audio. GATE P.

| Beat | Act | Narration (spoken) |
|---|---|---|
| **B00** | hook / ASK | Hello, fellows. Last week's tagging ablation was promising — but the strongest number rested on just four sections. So this week we ran it on the whole book: all one thousand three hundred forty. And that raises a sharper question — what can an ablation actually decide, and what can't it? |
| **B01** | the framework (4 questions) | Here's the frame — four questions. One: is each option reproducible? Two: does the choice even matter — measured downstream, not at the part you swapped? Three: where do the two differ, field by field, with the sample size in view? And four: which one is actually correct? Hold that last one. An ablation can answer the first three — but not the fourth. |
| **B02** | Q1 · reproducible? | Question one — reproducible? The dictionary tagger is exact: one-point-oh, every run. The open model, even at temperature zero, only gets near — about zero-point-nine-nine. And it's not just reproducibility: on the full book the dictionary tags all thirteen hundred forty sections in about twelve seconds, free and offline; the model takes five and a half hours on a GPU. Roughly sixteen hundred times faster. |
| **B03** | Q2 · does it matter? | Question two — does the choice even matter? You can't tell at the tagger; you have to look downstream, at the roadmap it produces. And it matters a lot: swap the tagger, and about seventy-four percent of a student's reading list changes. Same book, same project — the model tags materials into far more sections and promotes many more to core. |
| **B04** | Q3 · where do they differ? | Question three — where do they differ? Field by field, with the sample size shown. On materials — the field that drives core relevance — they strongly agree: about zero-point-nine-two, now over a hundred sections, not last week's four. On the fuzzier fields, like concepts and disease context, they diverge — because the model tags more freely. |
| **B05** | Q4 · which is correct? — the ceiling (falsifiability) | Question four — which one is correct? Here's the honest part: the ablation can't tell you. Reproducibility and agreement only compare the two backends to each other. Agreeing at zero-point-nine-two doesn't make either one right. To say which tagger is more correct, you need something the ablation doesn't have — ground truth. |
| **B06** | the gold set + the pending step | So we built the ground truth: a gold set. Twenty sections, three hundred thirty-three tags, graded by hand against the text — a hundred ninety-one are literally there, a hundred forty-two the model inferred. It's blind, and a second grader grades it independently. That's what will finally decide dictionary, model, or a hybrid — and it's still being graded. Alongside it, one human step remains: faculty approving the read-A-before-B links that switch the ordering on. |
| **B07** | verdict | So — where it stands. On the full book, the choice is real: about seventy-four percent of the reading list turns over. The dictionary wins reproducibility, speed, and cost, and agrees where it matters most. But which tagger is more correct is not decided — the gold set settles that, and it's still being graded — and the ordering is still waiting on faculty. The ablation told us the choice matters and where to look; it doesn't get to crown the winner. |
| **B08** | your turn / handoff | Your turn. For any simple-versus-fancy choice, run the four questions: is it reproducible, does it matter downstream, and where do they differ — with the n shown. Then, before you pick a winner, build a small blind gold set and score precision and recall. Ship the cheap default until the ground truth says otherwise. |
| **B09** | outro | What an ablation can, and can't, decide. This is Satwik for Humanitarians AI. |

## Register & claim notes for the reviewer (PROOF)

- **Framework-first:** B01 lands the 4-question frame — and flags up front that Q4 is unanswerable by ablation — before any result.
- **Falsifiability = B05 (the ceiling):** agreement ≠ correctness; "0.92 doesn't make either right." Names ground truth as the missing thing.
- **Series progress:** B00 + B04 connect to week-02 explicitly (n=4 → n=102, "not last week's four").
- **No winner:** the gold set is **being graded, not scored** — no precision/recall/F1 number; "hybrid" is a labeled hypothesis (B06/B07). Ordering **dormant** (B06/B07).
- **"The choice matters," not "the model is wrong":** the 74% downstream swing is the headline; divergence is a precision/recall trade-off with no gold standard.
- **`n` shown** with every agreement number (on-screen). Model named exactly (`qwen2.5-coder:7b`, temp 0, self-hosted).
- **Numbers spoken:** four questions · 1,340 · "1.000 vs ~0.99" · "12 seconds vs 5.5 hours / ~1,600×" · "74%" · "materials ~0.92 over 100+ sections" · "20 sections, 333 tags (191/142)". Full per-field table + role splits on-screen.
- **Length:** ≈ 500 spoken words → est. **~3:30–3:45** at Bella's measured pace. Confirmed after audio; trim B02/B06/B07 before sign-off if ≤3:00 wanted.

---

Human sign-off required before Kokoro (Bella) audio spend. GATE P.
VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-08-16
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
