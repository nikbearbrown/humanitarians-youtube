# NARRATION — GATE P — "Does the Fancy Part Earn It?" · Tagging Ablation

**Voice:** Kokoro `af_bella` ("Bella"). **Register:** Pragmatist / skeptical-explainer. **Narrator:** Satwik.
Framework-FIRST (PROOF): B01 shows the 5-check rubric before any result. Review on the animated slate
before any audio. GATE P. Every on-screen number carries its `n` (see SOURCES).

| Beat | Act | Narration (spoken) |
|---|---|---|
| **B00** | hook / ASK | Hello, fellows. The method paper flagged an honest worry: an AI tagger is stochastic — run it twice, get different tags. So can you trust it? Rather than argue, we ran the ablation. The real question: does the fancy tagger earn its place, or does the cheap, deterministic one already do the job? |
| **B01** | the framework (5 checks) | First — how to read an ablation, in five checks. One, isolate: change exactly one thing. Two, stability: run it a few times — same answer? Three, agreement: does the fancy option actually differ, and where? Four, weight: judge the field that drives the decision, not the average. Five, denominator: is the headline padded by trivial cases? Keep the simple default unless the fancy part earns it. |
| **B02** | check 1 · isolate | Check one — isolate. Same sixty sections, same vocabulary, same interface. The only thing that changes is the backend: a deterministic rule-based matcher, versus a pinned open model — qwen two-point-five, seven billion, temperature zero, on our own hardware. Three runs each. One variable; everything else fixed. |
| **B03** | check 2 · stability | Check two — stability. Run each three times; do the tags hold? The rule-based backend is exactly reproducible — one-point-oh on every field, byte for byte. The model, even at temperature zero, lands near zero-point-nine-nine. That's not randomness — the drift is GPU floating-point. Exact reproducibility is free with the deterministic backend; the model gets close, never quite there. |
| **B04** | check 3 · agreement | Check three — agreement. Field by field, the two mostly diverge in the expected way: on the fuzzy, interpretive fields the model tags more liberally — one to two extra terms — and overlap sits near forty percent. Neither is ground truth; which of those extra tags are signal is exactly what faculty review decides. |
| **B05** | check 4 · weight | Check four — weight it. Don't average every field equally; judge the one that drives the decision. Here that's materials — it sets a section's core role downstream. And that's where the two agree most: Jaccard zero-point-eight-nine. Where the call actually matters, the cheap backend and the model substantially agree. |
| **B06** | check 5 · denominator (falsifiability) | Check five — the denominator. And here you have to be honest. Empty-versus-empty counts as agreement, so sparse fields read high for free. Strip the padding, and materials stability falls from zero-point-nine-nine-six to zero-point-nine-three — on just four sections. The rule-based control stays exactly one-point-oh even here. So materials is directionally encouraging, not yet robust — it needs the denser re-run to defend. |
| **B07** | verdict / decision | So — does the fancy tagger earn it? On this evidence, no: ship the deterministic default. It's exactly reproducible, offline, needs no key, and it agrees with the model where it matters. Keep the model as a named, pinned option for later. And where the two disagree — the fuzzy fields, the difficulty score — that isn't failure; it's the agenda for faculty review. One caveat stays on the record: the strongest number rests on four sections. |
| **B08** | your turn / handoff | Your turn. Take any simple-versus-fancy choice in your own pipeline and run the five checks: isolate one variable, test stability over a few runs, compare agreement field by field, weight the field that drives your decision — and always report the n behind your headline. Ship the simple default unless the fancy part earns it. |
| **B09** | outro | Does the fancy part earn it. This is Satwik for Humanitarians AI. |

## Register & claim notes for the reviewer (PROOF)

- **Framework-first:** B01 lands the 5-check rubric BEFORE any result — the reusable method, not the numbers.
- **Falsifiability = B06 (DENOMINATOR):** the study breaks its own headline once empty-vs-empty padding is stripped (0.996 → 0.933, n=4); the control stays 1.000. Verdict kept **provisional** (n=4, pending `--chapters 19-27`).
- **No source, no verdict:** on-screen tables carry every figure; `n` shown wherever a small-sample number is. Model named exactly.
- **Not "LLM bad":** it's a precision/recall trade-off with no gold standard; the LLM is near-reproducible and agrees where it matters. Difficulty (35%) = weakest signal / faculty-calibration item.
- **CTA is a scaffold**, not "ask Claude": the 5-check template + the real reproducible command.
- **Numbers spoken:** five checks · 60 / K=3 · "1.000 vs ~0.99" · "materials ~0.89" · "0.996 → 0.93 on four sections" · "35%." Rest on-screen.
- **Length:** ≈ 510 spoken words → est. **~3:30–3:45** at Bella's measured pace. Duration confirmed after audio; trim B01/B06/B07 before sign-off if ≤3:00 wanted.

---

Human sign-off required before Kokoro (Bella) audio spend. GATE P.
VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-07-30
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
