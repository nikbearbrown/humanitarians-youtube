# Temperature: The Dial Between Prediction and Hallucination

**Skill:** ai-explainer
**Target length:** ~45 seconds
**Voice:** am_onyx (Onyx)
**Style:** Technical but accessible. Companion piece to `attention-finance` — same NLP-internals territory, different single idea (sampling randomness, not the attention mechanism).

---

## Beat 1 — The Hook

**Duration:** ~8 seconds

**Narration:**

You give an LLM the same earnings call quote three times. Same model. Same prompt. But you get three different answers. The output changed because you turned one dial. Temperature.

**Visual direction:**

Three identical quote cards appear in a row: "We anticipate moderate revenue growth in the back half of the year." Below each, a different extraction result fades in — "raised, 0.72" / "maintained, 0.65" / "raised, 0.81". A question mark pulses above. On "Temperature," the word lands large below the cards, and a circular dial icon fades in beside it, needle at an ambiguous mid-point — the recurring visual anchor for the rest of the video.

---

## Beat 2 — The Dial

**Duration:** ~12 seconds

**Narration:**

Temperature controls randomness. At zero, the model picks the single most likely next token every time. Deterministic. Same input, same output, guaranteed. At zero point five, it considers a wider range of tokens. There is variation, but it stays close to the most probable answer. At one point zero, the distribution flattens. Rare tokens get a real chance. The model becomes creative. In fiction writing, that is interesting. In financial extraction, that is a hallucination.

**Visual direction:**

A vertical token-probability bar chart (~15-20 bars, abstract, no real words), with the temperature dial in the top-left showing the current setting. At T=0.0: one dominant bar towers over flat others, labeled "Always picks this one," caption "Deterministic. Same input → same output." Dial animates to T=0.5: the tallest bar shrinks ~30%, second/third bars grow, caption "Slight variation. Mostly predictable." Dial animates to T=1.0: distribution flattens dramatically, rare tokens get visible mass, caption "Creative. Unpredictable." The tallest bar's color shifts cool blue (T=0.0) to warm red (T=1.0) as the dial turns.

---

## Beat 3 — What This Means for Finance

**Duration:** ~15 seconds

**Narration:**

Here is the same earnings quote run at three temperatures. At zero, the model says "maintained" with zero point seven one confidence. Run it again, same answer. And again, same answer. Locked. At zero point five, it says "maintained" twice, then "raised" once. Two out of three agree. At one point zero, it says "raised," then "maintained," then "lowered." Three runs, three different answers. None of them reliable. This is why financial extraction systems run at low temperature. And why self-consistency decoding runs the same prompt multiple times and votes. If the model cannot agree with itself, the answer is not stable enough to trust.

**Visual direction:**

The earnings quote returns at top. Three columns appear side by side, each headed by a temperature setting and dial position. Column T=0.0: three identical rows ("maintained — 0.71" ×3, all blue), lock icon, calm green border, label "Stable." Column T=0.5: three rows (two "maintained" blue, one "raised" green), amber border, "2/3 agree" tag, label "Mostly stable." Column T=1.0: three rows, three different directions/colors (raised/maintained/lowered), warning triangle, red border, label "Unstable." A bracket draws around Column 2's three runs with an arrow to a verdict box: "Vote → maintained (2/3)" — label: "Self-consistency: run multiple times, take the majority."

---

## Beat 4 — The Close

**Duration:** ~7 seconds

**Narration:**

Temperature is one number. It controls whether your model gives you the same answer every time or a different answer every time. In finance, you want the first one. Creativity is for poets. Consistency is for predictions.

**Visual direction:**

The dial returns, centered, large, set near zero — calm, steady. On "Creativity is for poets," the needle briefly twitches toward 1.0, background flickers warm/chaotic (reds, oranges), the Beat 2 token distribution flashes its flattened T=1.0 state. On "Consistency is for predictions," the dial snaps back to near-zero, background settles calm, distribution reappears locked (one dominant bar). Title lands: **Temperature.** / *The dial between prediction and hallucination.* Fade to Claude-branded outro bookend.

---

## Production Notes

**Total estimated duration:** ~42 seconds of narration + bookends = ~48 seconds total

**Voice:** am_onyx — clear and measured, matching the attention-finance companion register.

**Visual mix:** All Remotion. The temperature dial is the recurring visual anchor across all four beats — build it once, reuse the asset. The token-probability bar chart (Beat 2) and the three-column comparison (Beat 3) are the signature visuals.

**Tone:** One idea, landed hard. No invented company names or real tickers — the earnings quote is a generic, illustrative construction; the three-run comparisons are illustrative demonstrations of the sampling-variance pattern, not citations of a specific benchmarked model run.
