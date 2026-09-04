# NARRATION — GATE P — "Does It Reason, or Just Retrieve?" · week-05

**Voice:** Kokoro `af_bella` ("Bella"). **Register:** Pragmatist / skeptical-explainer. **Narrator:** Satwik.
Framework-FIRST (PROOF): B01 shows the 4-step "reasons or retrieves?" test before any result.
Falsifiability = B04 (insertion, not reshuffle — 0 matched sections moved). The reordering is **DRAFT**
(auto-proposed; authoritative graph = 0); the tagging verdict is **provisional (grader 1)**. Review on
the animated slate before any audio. GATE P.

| Beat | Act | Narration (spoken) |
|---|---|---|
| **B00** | hook / ASK | Hello, fellows. The dependency graph has been sitting dormant — zero authoritative edges — while we wait on the faculty review of the prerequisite links. It left a fair question: does this system actually reason about what to read, or is it just a fancy search? This week we turned the graph on — in draft — and ran each roadmap with it and without. So: reasons, or retrieves? |
| **B01** | the framework (4 steps) | Here's the test — four steps to tell reasoning from retrieval. One: A/B the mechanism — run it with the component and without, everything else fixed. Two: count what retrieval can't reach — what it adds that isn't similar to your query. Three: name the mechanism precisely — did it insert, or reorder? And four: mark what's draft — if it rests on auto-proposed data, say so. |
| **B02** | with vs without (the A/B) | Step one — the A/B. Same book, same project; the only change is the graph, on or off. Without it, the LNP roadmap selects sixty-four sections; with it, a hundred. Photothermal goes forty-five to sixty-four. The graph doesn't trim the list — it grows it. The question is what it added. |
| **B03** | what retrieval can't reach | Step two — count what retrieval can't reach. Those extra thirty-six sections, and nineteen for photothermal, are foundations: cell death, what defines a cancer — background the project never mentions, so it's similar to nothing you searched for. A top-k search never returns them — but you can't read the nanoparticle chapters without them. That's the system selecting and sequencing, not retrieving. |
| **B04** | insertion, not reshuffle (falsifiability) | Step three — name it precisely, because this is where it's easy to overclaim. It's tempting to say the graph reshuffled your reading list. It didn't — zero of the original sixty-four matched sections moved. It inserted the missing foundations and placed them first: insertion, not reshuffle. A true rank inversion needs one more refinement we haven't built. Claim the insertion, not the reshuffle. |
| **B05** | the draft status | Step four — mark what's draft. Those read-before links, sixty-two and forty-three, are real but auto-proposed, not faculty-approved. The authoritative graph still has zero edges; this run was a non-destructive preview. Across the whole book the proposer flagged fourteen hundred eighty-three candidate links — the size of the one-time faculty review, ranked and capped. One sign-off makes it authoritative. |
| **B06** | tagging verdict, hardened | One result carried over and hardened. Last week the gold set called the dictionary the more correct tagger — F1 zero-point-eight-nine to zero-point-three-five. This week we added the counts and a confidence interval: the gap is zero-point-five-four, and its interval clears zero. So the win isn't a small-sample fluke — still one grader, but now defensible. |
| **B07** | verdict | So — where it stands. Turned on, the graph pulls in foundations a search would miss and states dozens of read-before links: the system selects and sequences, it doesn't just retrieve. The honest limits — it's insertion, not reshuffle; the edges are draft, the authoritative graph still zero, a big review ahead. And the tagging win held under a confidence interval. Real progress, precisely claimed. |
| **B08** | your turn / handoff | Your turn. To tell whether your own system reasons or just searches: run it with the mechanism and without. Count what pure retrieval could never reach. Name what actually changed — insertion or reordering — and claim only that. And if it runs on auto-proposed data, call it draft until someone signs off. |
| **B09** | outro | Reasons, or retrieves? Now we can tell. This is Satwik for Humanitarians AI. |

## Register & claim notes for the reviewer (PROOF)

- **Framework-first:** B01 lands the 4-step "reasons or retrieves?" test before any number.
- **Falsifiability = B04:** "insertion, not reshuffle" — 0 matched sections moved; the naive "it reordered my list" claim is refused. A true rank inversion is named as not-yet-built.
- **DRAFT, not authoritative:** B05 (and B07) — auto-proposed edges, authoritative graph = 0, 1,483 = review size (ranked/capped), one sign-off away.
- **Tagging hardened but provisional:** B06 — CI [0.44, 0.64] clears zero (not a fluke), still grader 1.
- **Series:** B00 picks up wk-04's dormant ordering ("0 edges, pending faculty"). The core "selects and sequences, not retrieves" claim is the payoff.
- **Show-don't-assert:** the +36/+19 foundations (a search misses) are the on-screen proof of reasoning; the 0-reordered fact is the on-screen honesty.
- **Numbers spoken:** four steps · "64→100, 45→64" · "36 and 19 foundations" · "0 reordered — insertion not reshuffle" · "62 and 43 read-before links · authoritative still 0 · 1,483 review" · "F1 0.89 vs 0.35, gap interval clears zero" · "one grader." Full tables on screen.
- **Length:** ≈ 555 spoken words → est. **~3:40–3:55** at Bella's measured pace. Confirmed after audio; trim B03/B05/B07 if ≤3:20 wanted.

---

Human sign-off required before Kokoro (Bella) audio spend. GATE P.
VERDICT: PASS
Reviewer: Satwik Reddy Sripathi
Date: 2026-08-29
Do **not** run `generate_audio_kokoro.py` until this line reads `VERDICT: PASS` with a reviewer name/date.
