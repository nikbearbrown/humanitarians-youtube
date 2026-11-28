# SCRIPT — Confidently Out Of Date

Week ending 2026-11-27 · `ai-` track.

Narration as delivered. Kokoro `am_onyx`; measured durations are the master clock.

**Total 2:13.4** across 8 beats. Master 16:9 3840×2160.

---

### B00 — ASK · 17.83s

*ClaudeComposerAsk* — greeting `Salaam, Jainil` (Arabic/Farsi)

> Salaam. This is Jainil. You build a search index over your documents once. A year goes by. The documents keep arriving, the vocabulary moves — new words appear, and a few old words quietly change which conversation they belong to. Nobody rebuilds the index. Today: what that actually does to your results, and which half of it you will never notice.

### B01 — BLUF · 11.82s (+0.8s lead silence)

*BrutalistHesitantWriter* — types **loudly**, deletes it, types **quietly**

> A stale index fails quietly. It does not throw and it does not come back empty — it returns five confident results from the wrong neighbourhood, with a similarity score that looks exactly like a good day.

### B02 — SETUP · 16.83s

*StageRail*

> Here is the setup. An index gets built on one year of text. Then the language moves, in two ordinary ways: new terms appear that the index has never seen, and one existing term migrates — it used to belong to infrastructure, and now it belongs to data. The index itself does not change. Nothing ever tells it to.

### B03 — BODY · 18.24s

*PairedBars*

> So measure it. When none of the query uses new language, the stale index is perfect — a hundred percent recall, identical to a freshly rebuilt one. Half new words, still perfect, because the old words that survived carry the query on their own. It is only when the whole query is today's vocabulary that it breaks. And it breaks completely: zero percent.

### B04 — BODY · 22.57s

*CardSet* — the beat the title refers to

> Which is two completely different failures wearing the same label. A word the index never learned fails loudly — there is no vector, so there is no result, and anybody watching sees an empty page. But a word that moved fails quietly. The index has a vector for pipeline. It is confident about it. It is simply pointing at where that word used to live. Recall, zero. Similarity on the top result, zero point eight nine. Every single result from the wrong topic.

### B05 — LAND · 22.12s

*StageRail*

> So the fix is not a bigger model. It is a clock and a canary. Re-embed on a cadence, because text drifts whether or not anybody is watching it. And monitor the out-of-vocabulary rate on live queries, because that is the one number that actually moves when the language moves. The similarity score will not tell you. Across these queries it fell by seven hundredths — from zero point nine six to zero point eight nine — while recall went from everything to nothing.

### B06 — HANDOFF · 19.63s

*ClaudeComposerAsk*

> Your turn. Paste this into Claude. Take the last month of real queries against your search or your RAG system, and work out what fraction of their terms did not exist in the corpus the index was built on. Then go looking for the words that did exist but have changed what they sit next to. The first number tells you when to rebuild. The second tells you what you have been confidently getting wrong.

### B07 — OUTRO · 3.58s

*HaiTitleOutro*

> Confidently out of date. This is Jainil. Subscribe.

---

## Register note

Teardown: narrate the mechanism, then judge it. The judgment is B05 — the fix
is a clock and a canary, not a bigger model.

**On the BLUF.** `loudly` → **quietly** is the reel's whole claim: a stale index
does not announce itself. The trigger is one whitespace-delimited token, so it
actually fires (A11).

**On a line that was corrected twice.** B05 originally said the similarity score
"never dropped at all". It falls from 0.961 to 0.892 — a move of 0.069. The line
was rewritten to state the figure. That correction was then SILENTLY REVERTED by
a render still in flight, which stamped the beat sheet back from its startup copy
(A27); it was re-applied and verified by reading the file back before compile. The
rendered frame carries the corrected note and both numbers.

**On what this reel does not argue.** Staleness is reported as harmless where it
is harmless — 100% recall at half-new vocabulary, identical to a rebuilt index.
The first version of the experiment produced a null and that is in `FACTCHECK.md`
rather than hidden; the fix was to change the question, not to reweight the
queries until a collapse appeared.
