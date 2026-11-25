# SCRIPT — It Tested Clean

Week ending 2026-11-20 · `ai-` track.

Narration as delivered. Kokoro `am_onyx`; measured durations are the master clock.

**Total 2:31.1** across 9 beats. Master 16:9 3840×2160.

---

### B00 — ASK · 18.13s

*ClaudeComposerAsk* — greeting `Bula, Jainil` (Fijian)

> Bula. This is Jainil. A model goes to production. Offline it scores seventy-three percent accuracy, and it keeps scoring seventy-three percent, every day, forever. In production it is getting forty-one. Nobody changed the model, nobody deployed anything, and there is no error in any log. Today: how that happens, and why the test never notices.

### B01 — BLUF · 14.17s (+0.8s lead silence)

*BrutalistHesitantWriter* — types **model**, deletes it, types **feature**

> It passed every test, then the feature broke. The model is fine — it was fit once on correct data and nobody has touched it since. What changed is how one number gets computed at the moment it is asked for, and nothing in the system is set up to notice.

### B02 — SETUP · 14.89s

*StageRail*

> Here is the shape of it. The offline test reads the warehouse — the clean, complete, backfilled table. The live model reads the feature store, computed in a hurry, at request time. Both are supposed to produce the same number for the same user. Nothing anywhere checks that they do.

### B03 — BODY · 20.65s

*PairedBars*

> So break it four ordinary ways. A thirty-day window served as seven days. Dollars served as cents. An aggregate only eighty percent complete when the model asks. Twelve percent of lookups missing and filled with a zero. Offline accuracy stays at seventy-three point four for every single one, because offline reads the warehouse. What the model actually scores goes to sixty-four, and then to forty-one.

### B04 — BODY · 20.16s

*ClaudeBarChart*

> The cents one is worth stopping on. Offline, the model's average predicted probability is zero point four two. Fed cents instead of dollars, it is zero point nine nine. It has stopped being a classifier and become a machine that says yes to everyone. Forty-one percent accuracy is worse than ignoring the model entirely and always guessing the majority class, which would get fifty-nine.

### B05 — BODY · 19.78s

*CardSet*

> So would monitoring catch it? Pointed at the serving log — the values the model actually received — a standard drift check fires loudly on both big ones. Pointed at the warehouse table, which is where monitoring usually ends up wired, the very same check returns zero point zero zero one. For all four. The check is not weak. It is reading a table that never saw the problem.

### B06 — LAND · 18.92s

*StageRail*

> Which means the fix is not a better metric. It is a wire. Log the features the model actually received, at the moment it received them, and compare those against what training saw. That is the only place the two paths can be caught disagreeing, because it is the only place both numbers exist at once. Everything else is checking the copy that was always going to be right.

### B07 — HANDOFF · 20.31s

*ClaudeComposerAsk*

> Your turn. Paste this into Claude. Take one feature your model uses in production and write down exactly how it is computed in training, and exactly how it is computed at request time — the window, the units, the null handling, how complete the data is. Then ask where those two can differ. Run it on the feature you would least expect to be wrong. In my experience the answer is usually hiding in the null handling.

### B08 — OUTRO · 3.33s

*HaiTitleOutro*

> It tested clean. This is Jainil. Subscribe.

---

## Register note

Teardown: narrate the mechanism, then judge it. The judgment is B06 — the fix
is a wire, not a metric.

**On the BLUF.** The correction is `model` → `feature`, which is the
misdiagnosis the whole reel exists to undo. The trigger is one
whitespace-delimited token, so it actually fires (A11).

**On what this reel does NOT argue.** It does not say drift detection is
useless — measured, a standard check catches both damaging cases when it reads
the serving log. The failure is where the check is pointed. The angle I
expected going in, that the quiet skews are the deadly ones, is FALSE in this
data and was dropped rather than written around. See `FACTCHECK.md`,
correction 2.

**On the model.** The first fit was unstandardised, unconverged, and two
'skews' improved its score. That version would have demonstrated a broken
model, not skew. Refit before any figure was used.
