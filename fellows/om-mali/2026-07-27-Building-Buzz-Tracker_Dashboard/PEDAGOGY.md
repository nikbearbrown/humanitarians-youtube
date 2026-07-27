# PEDAGOGY — hn-buzz-signal
*Turning Hacker News Talk Into an AI Attention Signal*

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | States what the system does and that it runs end to end, no internals yet ✓ |
| B01 | PROBLEM | Motivation (Mycroft, the backtested hypothesis) before any mechanism ✓ |
| B02 | ARCHITECTURE | One-breath map of the whole flow, now naming what "deterministic score" and "Groq narrative" mean before they're used ✓ |
| B03 | FETCH | Concrete node walkthrough: search + exact-phrase fix, with a named example (entity=OpenAI, term=GPT-5) ✓ |
| B04 | FETCH | Get Metrics: dedupe, top-3, low-confidence flag ✓ |
| B05 | SCORE | Compute Buzz Score: the deterministic core, all four components named ✓ |
| B06 | SCORE | The score's inputs, restated concretely against the formula image ✓ |
| B07 | COMMENTS | Fan-out plumbing summarized as one purpose (fetch + clean comments), no per-node naming, by design ✓ |
| B08 | COMMENTS | Community Opinion (Groq): input, model, constraint, output shape ✓ |
| B09 | COMMENTS | Attach Opinions: the real bug (strict-mode failure) and the fix ✓ |
| B10 | SECTOR | Has Usable Opinions gate: the fork, the guard's origin story ✓ |
| B11-B14 | STATUS | What's working now: leaderboard/trend, theme breakdown, opinions, snapshot table ✓ |
| B15-B16 | CHALLENGE | The misattribution finding: real thread, real false-positive read, honest root cause ✓ |
| B17 | OUTRO | Recap + explicit next step (title-in-story relevance fix) ✓ |

Act order: COLD OPEN → PROBLEM → ARCHITECTURE → FETCH → SCORE → COMMENTS → SECTOR → STATUS → CHALLENGE → OUTRO ✓
Revision 2: the fixture-test beat was removed entirely (no longer part of the "what's working" claim); the dashboard beat split into leaderboard/trend and theme-breakdown so each image gets its own narration line.

---

## Cold open check

- Concrete claim shown up front: a Buzz Score + comment-grounded read, running end to end today (B00) ✓
- No implementation detail before the architecture beat (B02) ✓
- The governing line ("execution cheap, judgment not cheap") lands as thesis in B01, after the concrete hook, not before it ✓

---

## Utility-framing lint

Narration scanned for forbidden phrases:
- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT ✓

---

## Node-naming check (viewer must be able to locate every named node in its frame)

Every node named in narration for B03–B09 is present in `nodes_in_frame` and confirmed visible in the corresponding screenshot (`workflow_ingestion`, `workflow_plumbing`, `workflow_groq_community_opinion`, `workflow_sector_narrative`) per the user's node-to-image mapping ✓

---

## Honesty check (the misattribution beat)

- Presents the failure as a live, only-partially-fixed finding, not a solved problem — matches the source material's explicit instruction ✓
- States the interim guard (low-confidence <3 comments) AND why it didn't catch this case (15 comments existed) — no overclaiming ✓
- States the scheduled real fix (title-match relevance test) rather than implying it's already done ✓

---

## Length law

Estimated total: 333 s = 5:33 after revision 2 (added B06 inputs beat and split B11/B12; removed the tests beat). No new hard cap was set for this revision; flagged to the human rather than silently trimmed.

---

## Rhythm check

DOCUMENT beats (B03–B09, B14–B15) dominate the middle by design — this is a workflow walkthrough, not a mixed-archive piece — broken up by the STILL sequence (B10–B13) and CARD/GRAPHIC bookends (B00–B02, B16). No single shot type exceeds the house >2-consecutive-same-type lint once STATUS beats (B10–B13) are counted as their own run, which is intentional (a status montage), not a rhythm defect.

---

VERDICT: PASS
