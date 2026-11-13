# NARRATION-SCRIPT — ab-testing-can-lie-to-you

**Format:** CLI-explainer, 12-beat required spine · **Skin:** `claude` · **Persona:** none — direct
author attribution, visible on-screen handle "Supriya" (no "in for X") · **Register:** Teardown ·
**Voice:** Kokoro `af_bella` · **Words:** 411 · **Estimated runtime:** ~161s (at the measured
2.56 words/s from earlier reels) — the 16:9 must stay under ~175s so the 9:16 (plus its 4.5s
endcard) is full-length.

**GATE P PASS — signed by Supriya 2026-10-18.** Once approved, this text goes into `beat_sheet.json`, which becomes the source
of truth. Narration spells "A-B test" so Kokoro doesn't read "A slash B"; on-screen text keeps
"A/B". All simulated numbers below are the real output of `py/*.py` (saved in `py/*.out`).

---

**B00 — INTRO**
> Hi, I am Supriya and this video is about how an A-B test can look significant and still lie to you.

*On screen:* composer, greeting "Hi, I am Supriya", ask `claude "can I trust this A/B test result?"`.

**B01 — PROBLEM**
> Here's the problem. A product team at MSN gave a carousel sixteen rotating cards instead of twelve. They expected more clicks. The test said the opposite: a statistically significant drop. On that result, you don't ship. This is real, from a twenty nineteen paper led by Microsoft researchers.

*On screen:* a carousel of 12 cards grows to 16; an engagement arrow dives with "p < 0.05" beside it;
source line "Fabijan et al., KDD 2019".

**B02 — CLI**
> We can't see MSN's data, so the ask: simulate the mechanism. Two groups of users, a bot filter, then compare clicks.

*On screen:* greeting "The ask,", `claude "simulate an A/B test with a bot filter, then compare clicks per user"`.

**B03 — CODE**
> Here's the simulation. Most users click zero to six times. One and a half percent are fans, and the new carousel gives them forty more clicks. Then the standard cleanup: anyone over eighty clicks counts as a bot and gets dropped.

*On screen:* `py/carousel_v1.py`, verbatim; chip "SIMULATION".

**B04 — OUTPUT**
> The readout. Control: three point eight nine clicks per user. Test: three point two. A z score of minus forty. Significant, and clearly worse. Don't ship.

*On screen:* two bars, 3.89 vs 3.20, test bar sinking; "z −40.4 · p < 1e-9" (real `carousel_v1.out`).

**B05 — CLI**
> The revision. Before reading any metric, check the split. Fifty-fifty in should mean fifty-fifty out.

*On screen:* greeting "The change,", `claude "before any metric: check the 50/50 split, then fix the bot filter"`, running "updating…".

**B06 — CODE**
> Two changes. A chi-square test on the group sizes against fifty-fifty. And the fix: judge bots by their clicks from before the test, which the new carousel can't touch.

*On screen:* `py/carousel_v2.py` (the `srm_check` call and the `kept(users, col)` filter), with
`srm_check` from `py/abtest.py`.

**B07 — OUTPUT**
> The test group is three thousand users short. The odds of that by chance: about two in a million. That's a sample ratio mismatch. Fix the filter, and it's three point eight nine against four point six five. The loss was a win.

*On screen:* two user stacks, 200,000 vs 196,997, "SRM p 2e-06"; then the B04 bars re-grow to 3.89 vs
4.65 and the arrow flips up (real `carousel_v2.out`).
Source line (Flag C, approved): "Real SRMs are this subtle — Fabijan et al.'s example: 821,588 vs
815,482 users, < 1 in 500k by chance."

**B08 — SECOND LIE: PEEKING**
> The second lie is peeking. I ran a thousand A-A tests, both groups identical, checking every day for twenty days. Stop at the first significant day, and a quarter of them crown a winner. Look once, at the end: under five percent. Researchers at Stanford and Optimizely found nonstop checking can push it past thirty.

*On screen:* the false-winner curve climbs day by day, 3.5% → 24.6%, against a flat 5% line; "look once:
3.8%" (real `peeking.out`); source line "Johari, Pekelis & Walsh, 2015".

**B09 — SUMMARY**
> Back to MSN. The bot filter had dropped the most engaged users in the sixteen-card group. Once that was fixed, the result flipped, and the feature shipped. The paper says about six percent of Microsoft's experiments show this mismatch. So: check the split first, fix your sample size in advance, and if you must peek, use a test built for it.

*On screen:* the B01 carousel returns, arrow flips up, "shipped"; "~6% of Microsoft experiments had an
SRM"; three checks build in.

**B10 — NEXT STEPS**
> Your turn. Paste this into Claude with your last test: compare the group sizes to the split you planned, and list everything that could drop users from just one group. If the split is off, don't read the metrics yet.

*On screen:* greeting "Your turn.", `claude "compare my last test's group sizes to the planned split; what could drop users from one arm?"`, running "paste this into Claude…".

**B11 — OUTRO**
> A-B Tests Can Lie. Check the split first. I am Supriya.

*On screen:* `ClaudeTitleOutroFilled` — "A/B Tests Can Lie." with full-size "Supriya".
