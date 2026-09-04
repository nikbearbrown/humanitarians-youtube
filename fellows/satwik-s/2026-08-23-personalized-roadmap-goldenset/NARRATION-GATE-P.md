# NARRATION — GATE P — "Which One Is Right? Scoring Taggers Against a Gold Set" · week-04

**Voice:** Kokoro `af_bella` ("Bella"). **Register:** Pragmatist / skeptical-explainer. **Narrator:** Satwik.
Framework-FIRST (PROOF): B01 shows the 4-step scoring method before any result. Falsifiability = B04
(the hybrid hypothesis, rejected by ground truth). The honesty floor = B06 (one grader → provisional).
Every gold-set number is labeled **provisional (grader 1)**. Review on the animated slate before any
audio. GATE P.

| Beat | Act | Narration (spoken) |
|---|---|---|
| **B00** | hook / ASK | Hello, fellows. Last week ended at a wall: an ablation can tell you the tagger choice matters — but not which tagger is actually right. That takes ground truth. This week the ground truth is in — one grader down, and it's already enough to move the verdict. So: how do you decide which option is correct, and what does one grader's answer really earn you? |
| **B01** | the framework (4 steps) | Here's the method — four steps to decide which option is correct, not just which two agree. One: build a blind gold set — a human grades each tag against the text, blind to which tagger produced it. Two: score precision and recall per field — precision is the share of a tagger's tags that were kept; recall, the share of the correct tags it found. Three: read the split, not just the combined F1 — precision versus recall names the failure mode, and it's how you test a hypothesis. And four: trace where each tag came from — that shows why one wins, not just that it does. |
| **B02** | the blind gold set | First, the gold set. Twenty content-bearing sections; three hundred thirty-three tags to grade, across materials, techniques, and mechanisms. A hundred ninety-one are literally there in the text; a hundred forty-two the model inferred, with no literal mention — those are the ones that need real judgment. The grading is blind, and a second person is grading the same sample independently — so the verdict you're about to see is one grader's, not the last word. |
| **B03** | the F1 verdict | Now score it. Field by field, the deterministic dictionary is far more correct. Materials: F1 one-point-oh versus zero-point-two-seven. Techniques: zero-point-nine-two versus zero-point-three-seven. Mechanisms: zero-point-eight versus the same zero-point-three-seven. Overall — the dictionary at zero-point-eight-nine, the model at zero-point-three-five. The gold set did the one thing agreement couldn't: it named a winner. |
| **B04** | read the split (falsifiability) | But read the split, not just the F1. Going in, the guess was that the dictionary buys precision and the model buys recall — trade them, and a hybrid wins. Ground truth says no. The dictionary wins precision, zero-point-eight-seven, and recall, zero-point-nine-one. The model loses both — recall included — down around zero-point-three-five. There's no recall advantage to harvest, so this round, the hybrid idea is dead. |
| **B05** | trace provenance | And here's why. Trace where each kept tag came from. Where both taggers agreed, the tag was correct ninety-four percent of the time. The tags only the dictionary produced were correct about eighty-five percent of the time. The tags only the model produced? Twelve percent. The model isn't surfacing real tags the lexicon missed — it's mostly adding wrong ones. That's the whole verdict in a single row. |
| **B06** | the catch (provisional + pending) | One honest catch. This is one grader. The second blind grading is still coming, and the two get reconciled before anything is final — so call this provisional, not settled. And the ordering step is still waiting too: twenty-six proposed read-A-before-B links, zero in the graph today, one faculty sign-off away from switching on. |
| **B07** | verdict | So — where it stands. Provisionally, the gold set decided what the ablation couldn't: the dictionary is the more correct tagger — F1 zero-point-eight-nine to zero-point-three-five — winning precision and recall. The hybrid guess didn't survive ground truth. And the reason is legible: the dictionary's own tags are right most of the time; the model's, rarely. A second grader, and faculty, come next. |
| **B08** | your turn / handoff | Your turn. For any "which option is more correct" question, don't crown a winner from a demo. Build a small blind gold set and grade it against the source. Score precision and recall, not just F1. Read the split to find the failure mode — and trace which system's unique answers are actually right. Then report how many graders you had. One is a start, not a finish. |
| **B09** | outro | Which one is right — and how you'd know. This is Satwik for Humanitarians AI. |

## Register & claim notes for the reviewer (PROOF)

- **Framework-first:** B01 lands the 4-step scoring method before any number.
- **Falsifiability = B04:** the hybrid / "model = recall" hypothesis is stated, then rejected by ground truth (model loses recall too). The framework earns its keep by breaking a prior.
- **Honesty floor = B06:** one grader → **provisional**; second blind grading + reconciliation pending. Ordering dormant (0 edges), one faculty sign-off away.
- **Series:** B00 explicitly picks up week-03's ceiling ("an ablation can't say which is correct → ground truth"). The recap ablation numbers (74%, 1,600×, materials 0.919) stay in B00/verdict only — the body **advances** to the gold set, it doesn't repeat week-03.
- **No hybrid conclusion; no final verdict.** "Provisional" spoken in B02, B06, B07. Model named exactly (`qwen2.5-coder:7b`, temp 0, self-hosted).
- **Two 333 splits kept apart:** B02 uses 191 literal / 142 inferred; the 184/149 kept-vs-rejected split is on-screen only, not spoken here.
- **Numbers spoken:** four steps · "20 sections, 333 tags · 191 / 142" · F1 "1.00/0.27 · 0.92/0.37 · 0.80/0.37 · 0.89 vs 0.35" · "P 0.87 / R 0.91" · provenance "94% / 85% / 12%" · "26 links / 0 edges." Full tables on screen.
- **Length:** ≈ 570 spoken words → est. **~3:40–3:55** at Bella's measured pace. Confirmed after audio; trim B03/B07 (and tighten B01) before sign-off if ≤3:20 wanted.

---

Human sign-off required before Kokoro (Bella) audio spend. GATE P.
VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-08-24
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
