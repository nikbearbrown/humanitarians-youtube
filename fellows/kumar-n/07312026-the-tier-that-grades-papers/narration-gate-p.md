# NARRATION — GATE P — The Tier That Grades the Papers

Voice: HAI — Kokoro `am_onyx` ("Onyx"). Register: Pragmatist. Free/local.

The exhibit: **the paper's own three-tier validation framework** (Tier 1 =
multi-site prospective / Tier 2 = strong proof-of-concept / Tier 3 =
hypothesis-generating only), reused across beats via one component
(`TierPyramidBeat`, props: `grade`, `startAt`, `focus`) — same contract as
`EcosystemWheelBeat`. Real studies from the paper get plotted into it.

| Beat | Act | Narration |
|---|---|---|
| B00 | ASK (cold open) | Hi, this is Liam, for Kumar Karthik. There's a research review on using machine learning to read a chemical-sensing signal called SERS. Its best idea isn't a new algorithm — it's a three-tier framework for grading whether a published result is actually trustworthy. Let's test that framework for real: help me explain it, check it against real claims in the paper, and show what happens when someone actually checks the paper itself. *(Note: the composer visual displays a shorter third-person version of this as the typed prompt — see `remotion.props.command` in the beat sheet; only this spoken line is sent to the audio script.)* |
| B01 | EXHIBIT | SERS spectra are packed with information and packed with noise — substrate, instrument, sample all bleeding into the same signal. Machine learning is supposed to separate the two. Here's the paper's own scale for grading whether it actually worked: Tier one, two, three. Empty for now. Let's fill it in. |
| B02 | GRADE-METHODS | Classical methods first. Support vector machines and random forests are the most validated — they work with the small, noisy datasets this field actually has. Deep learning — C N Ns, transformers — hits ninety-plus percent on big single-site datasets, but on the small datasets most studies actually run, it holds no consistent edge at all. |
| B03 | GRADE-TIERS | Now the grading. One study — serum spectra, two independent patient cohorts, ninety-five point eight percent accuracy — reaches Tier two. Another — sixty-six thousand spectra, ninety-seven percent accuracy — sits right on the Tier two, three border: huge dataset, but one site, one time period. Almost everything else in this field: Tier three. Hypothesis-generating. Not one published study reaches Tier one. |
| B04 | PREDICT | So here's the twist question: is the paper making this argument itself trustworthy? Clean definitions, confident tone, no reasoning given for why these particular methods were chosen. Before I tell you what happened — is that a red flag, or just good editing? Commit. |
| B05 | TWIST | It was a red flag. The methodology section listed techniques but never argued for them — and read like it had been AI-generated. Kumar raised it. His P M confirmed it was a real problem. Then a second teammate, without being told any of this, read the same section and reached the identical conclusion on his own. |
| B06 | GRADE-FIX | The first rewrite pass still had citation and accuracy problems — a review process called it out directly. The next pass, built on that diagnosis, came back clean. The paper's own gaps — no external validation for wastewater deployment, no cross-site testing — are still there, honestly, in the text. That's the point: the fix wasn't polish, it was rigor. |
| B07 | VERDICT | The paper's real argument: this field doesn't need new architectures, it needs harder validation — and most of what gets published falls short of that bar. Kumar's team's own process — diagnose, confirm independently, then actually fix it — is a small working model of the exact discipline the paper is arguing for. That work is what supports his renewal. |
| B08 | HANDOFF | Your turn — paste this into Claude: here's a research paper making a strong claim. Help me build a three-tier framework for how trustworthy that claim really is, and test it against the paper's own evidence. |
| B09 | OUTRO | The Tier That Grades the Papers. This is Liam, for Kumar Karthik. |

Human sign-off required before any Kokoro audio generation. GATE P.

VERDICT: PASS (pending your read-through)
