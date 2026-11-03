# Week 27 — Angle audit: the birthday paradox

Status: **audit done, angle not yet chosen.** Subject locked in `TOPIC-DECISION.md`.

## 1. Uniqueness audit

### Repo (all 65 refs, read-only, one pass over 56,521 text blobs)

Searched for the underlying ideas, not just the name:

| Idea searched | Hits | Verdict |
|---|---|---|
| "23 people" / "room of twenty-three" | 1 file | **False positive.** Our own Week 22 line "A later study measured twenty three people" (Moelants tapping study). Unrelated. |
| pair-counting (n(n-1)/2, "n choose 2", "253 pairs", "number of pairs") | 0 | clear |
| hash collision / collision probability / pigeonhole | 6 files | **False positives.** Gödel video's "pigeonholes" scrolls prop; math-olympiad "pigeonhole early exit" (a voting rule). Neither is the birthday idea. |
| "probability that no / at least two share" | 6 files | **False positives.** Superposition-slosh beats (quantum probability swapping sides) and a branding ideas list. |
| expected number of pairs / matches / collisions | 0 | clear |
| "coincidence" | 157 files | Common word. Spot-read the top clusters (two-hit, hpv-dual-hit, exchange-avoidance, fluency-trap): all use it casually. None teaches "coincidences are likelier than they feel". |
| birthday paradox / problem / attack, shared / same birthday | 0 | clear (earlier sweep, control search worked) |

### Our own films (Weeks 17–26 narration and beat sheets)

No birthday, pair-counting or collision-probability content. The only "collision" is the Week 21 act title THE COLLISION (a different idea).

### Structures already used (so this film must not repeat them)

| Week | Shape |
|---|---|
| 17 | hook, framework, apply and build twice, limits, handoff |
| 20 | an instrument being read (scale, calibration, readings) |
| 21 | one table, the same move at larger and larger sizes |
| 22 | three witnesses, then a verdict |
| 23 | framework, scenarios, guess-and-reveal, verdict |
| 24 | a house, one room per intelligence |
| 25 | two always-strategies, then a coin that beats both |
| 26 | acoustic halls, a record as a room |

Boundaries to stay clear of:

- **Rooms.** Weeks 23, 24 and 26 all use room or hall framing. Do not stage this film as a room filling with guests, even though the classic setup invites it.
- **Witnesses and verdicts** (Week 22), **numbered framework to "your turn" rubric** (most earlier films).
- **"One size up" ladders** (Week 21). Angle C below touches this, so it needs a different engine than repeating one move.
- Signature phrasing to avoid: "confident, wrong answer", "two inputs look the same".

Nearest probability-intuition neighbours elsewhere in the repo (fellows' work, not ours to restage): `vox-base-rate`, `vox-99-percent-test`, `vox-prosecutors-fallacy`, `vox-turkey-problem`, the Simpson and survivorship videos. None covers pairs or collisions.

Caveat: birthday paradox is heavily covered on YouTube generally. The gate here is the repo and our own weeks, which are clear. The angle should still be one a typical explainer does not make.

## 2. Candidate angles

**A. "Count the pairs, not the people."** The gap between 23 people and 253 pairs. Build the whole film on one growing counter: each new person adds as many pairs as there are people already.
- Teachable move: when an intuition feels wrong, check what is actually growing.
- Risk: this is the standard explainer. Needs a staging that is not a filling room.

**B. "Match me" versus "match anyone."** The same crowd, two questions. 23 people for a shared birthday somewhere, but 253 for a match with *your* birthday. The paradox is a swapped question.
- Teachable move: ask whether a claim is about you or about any pair.
- Risk: close to Week 22's "what exactly was measured". Must be differentiated.

**C. "Where the square root lives."** Collisions arrive near the square root of the space: 365 days, then ID spaces, then hash outputs (the birthday attack). Real stakes, verifiable facts (for example the 2017 SHA-1 collision).
- Teachable move: how long until two things collide scales with the square root of the number of possibilities.
- Risk: a scaling ladder echoes Week 21. Needs a different engine, such as one question asked of progressively bigger "calendars" with a stake at each.

**D. "Test it on real people."** The model assumes every day is equally likely. Real births are not, and real squads and rosters are testable. The film is three trials with a prediction before each.
- Teachable move: when a clean model says 50%, test it on messy data, and know which way the mess pushes the answer. Non-uniform birthdays can only raise the chance of a match.
- Trials use only sources that are safe for a monetised channel: our own simulations, and US federal births-by-day counts (NCHS and SSA, US government statistics) as the "real calendar". **No political content, no named real individuals, no third-party text or images.** Rosters, presidents and similar lists are out.
- Structure only this subject has: the chapters are the trials. It needs no room, no witnesses and no rubric. It can end on one open question rather than a checklist.
- Risk: data must be fetched and licensed, and results computed, not recalled.

## 3. Recommendation

**D**, with the square-root idea from C held back as a possible closing turn. D is the most distinct from all earlier films, rests on checkable numbers rather than a familiar derivation, and fits "each film needs its own structure".

Open item before building: confirm the real-world datasets and their licences, and compute the match rates ourselves.
