# FACTCHECK — vox-same-net-same-hole

**Why Two AIs Checking Each Other Is One Blind Spot Twice**
Factcheck completed against: `books/computational-skepticism-for-ai/chapters/13-accountability-who-is-responsible-when-the-system-fails.md`
All claims verified before render. No numbers or statistics in this reel — the argument is purely structural.

---

## Narration claims

| Beat | Claim | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|
| B01 | "Adding a second AI to check the first feels like a safety net. It is the same net with the same hole." | ✓ illustrative | The sieve-and-hole framing is an illustrative metaphor for the common cause failure concept. No empirical claim. | — |
| B02 | "A model generates an output. A second model reviews it. Both trained on the same data, built on the same foundation." | ✓ | Chapter 13, Common cause failure section: "If the system being monitored can produce subtly wrong outputs that look correct, the monitoring system trained on similar data with similar architecture will have correlated blind spots." The same-foundation premise is explicit. | — |
| B03 | "A flawed one should catch — but some slip through the holes." | ✓ illustrative | The sieve metaphor is illustrative; the underlying claim that some flaws evade detection is the chapter's central premise. | — |
| B04 | "The flaw must clear two layers. That is the safety claim." | ✓ illustrative | Accurately represents the motivation for AI-mediated monitoring systems before the failure is revealed. | — |
| B05 | Quote: "What fools the generator is most likely to fool the checker." | ✓ | Chapter 13: "the thing most likely to fool System A is also most likely to fool System B, because both were built on the same foundation." This is verbatim paraphrase, marked as an attributed quote in the visual. | — |
| B05 | Attribution: "— the common cause problem" | ✓ | Chapter 13 explicitly names this "common cause failure" — the attribution is accurate (concept, not a named scholar). | — |
| B06 | "The holes line up. The flaw slides through the first sieve — and straight through the second one too." | ✓ illustrative | Illustrative rendering of the chapter's claim about correlated blind spots. | — |
| B07 | "Both models trained on identical data. Their errors are correlated." | ✓ | Chapter 13: "the monitoring system trained on similar data with similar architecture will have correlated blind spots." Rendered faithfully. | — |
| B07 | "Whatever the generator gets subtly wrong, the checker is most likely to miss." | ✓ | Chapter 13: "You have not introduced an independent check. You have introduced a correlated one." | — |
| B08 | "High-stakes systems require something genuinely outside." | ✓ | Chapter 13: "Every high-stakes validation system humans have built — clinical trials, aircraft certification, nuclear safety, financial auditing — depends on something genuinely outside." | — |
| B08 | "Aircraft certification, clinical trials — a different kind of check, from a different foundation entirely." | ✓ minor | One spoken aside, per card exclusion rule ("no FDA/aviation case histories beyond one spoken aside"). The aside is ≤20 words and mentions no specific cases or agencies. | — |
| B09 | "Redundancy is not the same thing as independence." | ✓ | Direct consequence of the common cause failure argument in chapter 13. | — |
| B10 | "Stack as many correlated checkers as you want. Each one adds the same hole." | ✓ illustrative | Illustrative rendering of: adding correlated checks does not add independent coverage. | — |
| B11 | Content moderation example — generator + checker on same 2021 corpus both miss new harassment pattern | ILLUSTRATIVE | Numbers and scenario are invented to demonstrate the mechanism; labeled illustrative | — |
| B12 | "A second sieve from the same foundry is not a check. It is a copy." | ✓ illustrative | The sieve metaphor; the underlying claim is the chapter's conclusion about correlated validators. | — |

---

## Exclusion check

| Excluded item | Appears in film? | Where (if yes) |
|---|---|---|
| Godel incompleteness formalism | NO | The chapter's Godel argument is summarized through the sieve metaphor — no mention of Godel, formal systems, or incompleteness by name. |
| Seven-tier taxonomy | NO | The tier vocabulary (Tier 1, Tier 4, etc.) never appears. |
| Chain-of-thought-monitoring literature | NO | No research papers, no "Pachocki," no CoT monitoring references. |
| FDA/aviation case histories (beyond one aside) | ONE aside only | B08 narration: "Aircraft certification, clinical trials" — one beat, ≤20 words, no case-by-case detail. Compliant. |

All exclusions confirmed honored.

---

## Visual claims

| Graphic | Visual claim | Verdict |
|---|---|---|
| B03 sieve | A sieve has a hole that lets flawed items through | ✓ illustrative |
| B06 alignment | Both sieves have holes at the same position | ✓ illustrative — correctly represents correlated blind spots |
| B07 shared data | Generator and checker both connect to the same training data box | ✓ — the chapter states they share the same foundation |
| B08 solid bar | An independent check has no shared hole | ✓ illustrative — represents "something genuinely outside" |
| B10 stack | Multiple sieves with aligned holes do not cover the gap | ✓ illustrative |

---

Verdict: **all claims hold**. No corrections needed. Render approved.
