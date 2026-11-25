# SOURCES — Both Sides Passed

## Primary evidence (ships in this folder)

**`boundary_evidence.py`** — pure numpy, no download, runs instantly.
**Every count shown in the reel is printed by this file.**

5,000 synthetic payment events (`event_id`, `ts_ms`, `amount`, `currency`,
`status`), with timestamps following a realistic daily rhythm — quiet
overnight, peaking early afternoon. Seven defects, each applied on its own to a
known-good batch, then run past three levels of checking.

| Level | What it checks | Caught |
|---|---|---|
| **in-stage** | Required fields, types, positive timestamps — what a stage can verify about its own data alone | **1 / 7** |
| **boundary** | A contract profiled from a known-good run: agreed medians, allowed status values, key uniqueness, negative-amount rate | **6 / 7** |
| **+ shape** | The same contract plus the hour-of-day distribution, compared by total variation distance | **7 / 7** |

The seven defects: timestamps in seconds not milliseconds · amount in cents not
dollars · a new status value · nulls encoded as −1 · a +5:30 timezone shift ·
amount arriving as a string · late rows duplicating `event_id`.

The only one in-stage checks catch is the string amount — the single defect
that changes a *type*. Every other one leaves each record individually valid on
both sides.

## Reference

**Breck, E., Zinkevich, M., Polyzotis, N., Whang, S. & Roy, S. (2019).**
*Data Validation for Machine Learning.* Proceedings of SysML 2019.
<https://research.google/pubs/data-validation-for-machine-learning/>

**B05 paraphrases this paper; it does not quote it.** The card is labelled
`REFERENCE (paraphrased, not quoted)` and the narration says "described",
not "wrote". The full abstract could not be retrieved, and the only verbatim
sentence obtained — *"Machine learning is a powerful tool for gleaning
knowledge from massive amounts of data."* — is an opening line that carries
none of the relevant content. Rather than wrap a paraphrase in quotation marks,
the card states the two facts that were confirmed:

- the system is deployed inside Google's TFX platform
- it detects anomalies in data fed into ML pipelines, including training and
  serving drifting apart

Every previous reel on this channel has quoted its source verbatim. This one
does not, and says so on screen.

## Deliberate omissions

1. **No real-world frequency claim.** The seven defects are a constructed
   catalogue of ordinary integration failures, not a sample of real incidents.
   "1 of 7" describes *this catalogue* against *these checks*. The reel does
   not say 1 in 7 of your bugs, or anything like it.
2. **No claim that boundary checks catch everything.** The headline is 7/7 on a
   catalogue chosen before the checks were written — but a catalogue the same
   author wrote. A defect nobody thought of is not in it.
3. **No scale figure for the Google system.** Reports of "petabytes per day"
   and "hundreds of teams" appear in secondary summaries; not having read them
   in the paper, the reel says only "a very large amount of production data".
4. **The hour-of-day check only works because the data has a daily rhythm.**
   An earlier version of this experiment used uniformly distributed
   timestamps, and the shape check caught nothing at all — a timezone shift is
   invisible if there is no shape to shift. See `FACTCHECK.md`.
