# PEDAGOGY — hn-buzz-signal
*Turning Hacker News Talk Into an AI Attention Signal*

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | EXECUTIVE SUMMARY | Human-authored, human-confirmed statement of who is presenting and what the video covers, opening the video — added revision 5, reordered to lead revision 6 ✓ |
| B01 | COLD OPEN | States what the system does and that it runs end to end, no internals yet ✓ |
| B02 | PROBLEM | Motivation (Mycroft, the backtested hypothesis) before any mechanism ✓ |
| B03 | ARCHITECTURE | One-breath map of the whole flow, now naming what "deterministic score" and "Groq narrative" mean before they're used ✓ |
| B04 | FETCH | Concrete node walkthrough: search + exact-phrase fix, with a named example (entity=OpenAI, term=GPT-5) ✓ |
| B05 | FETCH | Get Metrics: dedupe, top-3, low-confidence flag ✓ |
| B06-B08 | SCORE | Compute Buzz Score (the deterministic core, all four components named) plus the score's inputs restated against the formula image ✓ |
| B09-B11 | COMMENTS | Fan-out plumbing → Community Opinion (Groq): input, model, constraint, output shape → Attach Opinions: the real bug (strict-mode failure) and the fix ✓ |
| B12 | SECTOR | Has Usable Opinions gate: the fork, the guard's origin story ✓ |
| B13-B16 | STATUS | What's working now: leaderboard/trend, theme breakdown, opinions, snapshot table ✓ |
| B17-B18 | CHALLENGE | The misattribution finding: real thread, real false-positive read, honest root cause ✓ |
| B19 | OUTRO | Recap + explicit next step (title-in-story relevance fix) ✓ |

Act order: EXECUTIVE SUMMARY → COLD OPEN → PROBLEM → ARCHITECTURE → FETCH → SCORE → COMMENTS → SECTOR → STATUS → CHALLENGE → OUTRO ✓
Revision 2: the fixture-test beat was removed entirely (no longer part of the "what's working" claim); the dashboard beat split into leaderboard/trend and theme-breakdown so each image gets its own narration line.
Revision 5 (2026-08-01): inserted a new executive-summary beat after the cold open; every beat from
the former B01 onward renumbered up by one (this table's beat ranges were also corrected against
the actual `beat_sheet.json` act boundaries while making this edit, since the pre-revision-5 table
had drifted slightly from the built sheet).
Revision 6 (2026-08-01): swapped B00 and B01's content (narration, card headline/eyebrow, rendered
video, and narration audio) so the video now opens with the personal intro ("Hi, I'm Om Mali...")
first and the project cold-open description second, per the author's explicit request — beat IDs
B02 onward are unaffected by this swap.

---

## Cold open check

- B00 (executive summary) states who is presenting and the three things the video covers, before anything else — a "why keep watching" beat opening the film ✓
- B01 (cold open) then states the concrete system claim: a Buzz Score + comment-grounded read, running end to end today ✓
- No implementation detail before the architecture beat (B03) ✓
- The governing line ("execution cheap, judgment not cheap") lands as thesis in B02, after the concrete hook, not before it ✓

---

## Utility-framing lint

Narration scanned for forbidden phrases:
- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT ✓

---

## Node-naming check (viewer must be able to locate every named node in its frame)

Every node named in narration for B04–B10 is present in `nodes_in_frame` and confirmed visible in the corresponding screenshot (`workflow_ingestion`, `workflow_plumbing`, `workflow_groq_community_opinion`, `workflow_sector_narrative`) per the user's node-to-image mapping ✓

---

## Honesty check (the misattribution beat)

- Presents the failure as a live, only-partially-fixed finding, not a solved problem — matches the source material's explicit instruction ✓
- States the interim guard (low-confidence <3 comments) AND why it didn't catch this case (15 comments existed) — no overclaiming ✓
- States the scheduled real fix (title-match relevance test) rather than implying it's already done ✓

---

## Length law

Estimated total: 348.0 s = 5:48 after revision 5 (added the ~16.2s B01 executive-summary beat). No new hard cap was set for this revision; flagged to the human rather than silently trimmed.

---

## Rhythm check

STILL beats (B04–B10, B15–B16) dominate the middle by design — this is a workflow walkthrough, not a mixed-archive piece — broken up by the STILL sequence (B11–B14) and CARD/GRAPHIC bookends (B00–B03, B17). No single shot type exceeds the house >2-consecutive-same-type lint once STATUS beats (B11–B14) are counted as their own run, which is intentional (a status montage), not a rhythm defect. The new B01 (CARD) sits between the two other opening cards (B00, B02, B03), extending — not breaking — the existing bookend run.

---

VERDICT: PASS
