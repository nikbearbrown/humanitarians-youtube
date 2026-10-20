# NARRATION-SCRIPT — correlation-is-not-causation

**Format:** CLI-explainer, 12-beat required spine · **Skin:** `claude` · **Persona:** none — direct
author attribution, visible on-screen handle "Supriya" (no "in for X") · **Register:** Teardown ·
**Voice:** Kokoro `af_bella` · **Words:** 379 · **Estimated runtime:** ~148s (at the measured
2.56 words/s from the v2 banking reel) — must stay under 180s with the 4.5s 9:16 endcard so the
9:16 is full-length.

Draft for review. Once approved, this text goes into `beat_sheet.json`, which becomes the source
of truth.

---

**B00 — INTRO** · ~9.8s
> Hi, I am Supriya and this video is about why correlation isn't causation, and how real hospital data can point you to the wrong answer.

*On screen:* composer, greeting "Hi, I am Supriya", ask `claude "which kidney stone treatment works better?"`.

**B01 — PROBLEM** · ~18.0s
> Here's the problem. A study compared two ways of treating kidney stones: open surgery, and a keyhole procedure. Three hundred fifty patients each. The data is real, from a British Medical Journal study in nineteen eighty-six. Say you run the hospital. You have to pick one.

*On screen:* two columns of 350 patient dots, labelled; "Charig et al., BMJ 1986" source line.

**B02 — CLI** · ~8.6s
> So the ask: compare the success rate of each treatment. Success means the stones were gone, or nearly gone, three months later.

*On screen:* `claude "compare success rates for open surgery vs keyhole in kidney_stones"`.

**B03 — CODE** · ~13.3s
> Here's the query. One table, one row per treatment and stone size. Sum the successes, divide by the patients, group by treatment. Nothing fancy. Notice what it leaves out: which patients got which treatment.

*On screen:* `sql/q1_by_treatment.sql`, verbatim.

**B04 — OUTPUT** · ~7.8s
> Keyhole: eighty-two point six percent. Open surgery: seventy-eight. Keyhole wins by almost five points. Most dashboards would stop right here.

*On screen:* two bars grow to 82.6 and 78.0 (real `q1_by_treatment.out`).

**B05 — CLI** · ~8.2s
> The revision. Large stones are harder to clear than small ones. So the change: split the same numbers by stone size.

*On screen:* greeting "The change,", `claude "split the same comparison by stone size"`, running "updating…".

**B06 — CODE** · ~9.8s
> One change: stone size goes into the group by. Same table, same rows. I kept the patient count too, because it matters in a second.

*On screen:* `sql/q2_by_size.sql`, verbatim.

**B07 — OUTPUT** · ~8.6s
> Now look. Small stones: open surgery ninety-three percent, keyhole eighty-seven. Large stones: open surgery seventy-three, keyhole sixty-nine. Open surgery wins both groups.

*On screen:* the two bars split into four (real `q2_by_size.out`); surgery highlighted in both pairs.

**B08 — MECHANISM** · ~19.9s
> Here's why. Look at the patient counts. The hard cases went to surgery: two hundred sixty-three of its three hundred fifty patients had large stones. Keyhole got mostly easy ones: two hundred seventy small. Stone size drove the treatment and the outcome. The overall number measured the patients, not the procedure.

*On screen:* the B01 dots re-sort by stone size — surgery's column mostly large, keyhole's mostly small.

**B09 — SUMMARY** · ~23.0s
> So the correlation was real. Keyhole patients did better. The gap came from the patient mix, not the procedure. Before you act on a gap, ask three things: who got which option, what else drives the outcome, and does the gap survive a split. And even the split is still observational. Only randomizing rules out the causes nobody measured.

*On screen:* three questions build in; caveat line last.

**B10 — NEXT STEPS** · ~16.8s
> Your turn. Paste this into Claude with your own data: find a variable that drives both who got the treatment and the outcome, then re-run the comparison split by it. If the winner flips, your dashboard was measuring the mix, not the effect.

*On screen:* greeting "Your turn.", `claude "find a variable driving both who got treated and the outcome; re-run split by it"`, running "paste this into Claude…".

**B11 — OUTRO** · ~4.3s
> Correlation Is Not Causation. Check who got what. I am Supriya.

*On screen:* `ClaudeTitleOutroFilled` — "Correlation Is Not Causation." with full-size "Supriya".
