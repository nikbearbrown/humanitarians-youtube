# SCRIPT — Significant On Tuesday

Week ending 2026-11-06 · `ai-` track.

Narration as delivered. Kokoro `am_onyx`; measured durations are the master
clock.

**Total 2:22.4** across 9 beats. Master 16:9 3840×2160.

---

### B00 — ASK · 16.92s

*ClaudeComposerAsk* — greeting `Yassou, Jainil` (Greek)

> Yassou. This is Jainil. Somebody starts an A/B test on Monday, checks it on Tuesday, and on Tuesday it is significant. So they ship it. Today, what that habit actually costs — measured across twenty thousand experiments where the two versions were identical by construction, so every winner is a false one.

### B01 — BLUF · 10.62s (+0.8s lead silence)

*BrutalistHesitantWriter* — types **truth**, deletes it, types **noise**

> Keep checking an A/B test, and you will eventually see noise. Not because the test is broken. Because looking is itself a decision, and nobody ever counted how many times you looked.

### B02 — SETUP · 18.26s

*ThresholdWalk* — band ±1.96

> Here is one of those twenty thousand. Both versions are identical, so the true difference is exactly zero. After the first hundred visitors per arm it is already outside the line — significant, in favour of B. Stop on Tuesday and you ship B. Keep going and it wanders back. By two thousand visitors there is nothing there, because there was never anything there.

### B03 — BODY · 17.86s

*ClaudeBarChart*

> So how often does that happen? Look once, at the end, and five percent of these null experiments come back significant — which is exactly what a five percent test promises. Look twice and it is nearly nine. Five times, fifteen. Twenty times, over twenty-five percent. The test never got worse. You just gave it more chances to be wrong.

### B04 — BODY · 18.75s

*DistributionShape*

> And a wrong call is not the worst of it. This is every difference measured by the runs that did stop early. Remember the truth is zero. There is nothing near zero. Not one of them stopped at under one point eight points, and the middle one said four point four. A small effect is never significant at a small sample — so the only way to stop early is to measure a big one.

### B05 — BODY · 18.52s

*CardSet*

> The fix is not to stop looking. It is to move the line. Split your five percent across the looks the Bonferroni way and you land at one point eight — safe, but you have thrown away power you already paid for. Calibrate a single boundary for the number of looks you actually take, and twenty-five percent falls back to five. Same data. Same peeking. One number changed.

### B06 — LAND · 18.41s

*ThresholdWalk* — band ±2.66, same twenty numbers as B02

> Here is Tuesday again, with the calibrated line. The run that fooled us never reaches it. That is not free — a wider boundary needs a bigger cap, and below about sixty-five percent power you will spend more visitors than one fixed test would. Above it you spend fewer. At eighty percent power, nineteen percent fewer, because a real effect gets called early.

### B07 — HANDOFF · 19.35s

*ClaudeComposerAsk* — `Your turn.`

> Your turn. Paste this into Claude. Simulate an A/B test where both arms are identical, check for significance every hundred users, stop at the first p below point oh five, then report how often you declare a winner and how big the effect looked when you did. Run it on your own numbers. The second answer is the one that will bother you, because it tells you what your past wins probably looked like.

### B08 — OUTRO · 3.75s

*HaiTitleOutro*

> Significant on Tuesday. This is Jainil. Subscribe.

---

## Register note

Teardown: narrate the mechanism, then judge it. The judgment lands in B06 and
it cuts both ways — the correct procedure is not free, and the reel says where
it costs you rather than only where it pays.

**On the BLUF.** The single-word correction is `truth` → `noise`, which is the
misconception the body dismantles: that watching an experiment reveals what is
true, rather than giving a fixed error budget more chances to be spent. The
trigger is one whitespace-delimited token, so it actually fires (Gotcha A11),
and the corrected sentence stands alone as the reel's claim.

**On what is not claimed.** The reel never estimates how often teams peek, never
attributes the replication crisis to it, and never calls sequential testing a
free saving. All three were available and all three were cut — see FACTCHECK,
"Claims considered and cut".
