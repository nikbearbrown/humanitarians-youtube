# CHECKS-REPORT — documenting-the-system-and-making-the-demo-runnable

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types an AUDIT instruction — "do not trust my memory" — and lands three answer lines. The week turned out to be about that instruction, so the reel opens on it (COLD OPEN LAW). |
| B01 | SHOW | Claim: the code was the easy part. Two deliverable cards land naming what each is FOR, the stated requirement lands beneath them, and the number of times it had been met lands as a chip and is **struck through**. |
| B02 | SHOW | Claim: six named, three absent. Six rows land with before and after; the three absent rows print **words** in the before cell rather than a zero, and their bars take the accent. The totals separate lines written from nothing from lines added. |
| B03 | SHOW | Claim: which zero is which. The five grepped names land as chips; the two published documents at a real zero land with their before-and-after; the third lands below a dashed rule, dimmed, with the reason it is not the same finding. |
| B04 | SHOW | Claim: one citation is not decoration. A single bar splits 21/1 with the one taking the accent, then a four-step chain lands — established, reproduced, rule changed, draft overturned — with the last step accented. |
| B05 | SHOW | Claim: three layers, three rules for changing. Each card leads with its **mutability** rather than its row count, because what the layer may do is the claim. The 5,806 = 5,806 identity lands beneath, with the 327 that are not marks. |
| B06 | SHOW | Claim: eight links that join. The chain draws downward as a **connected** descent — dot, segment, dot — rather than a bulleted list, because the claim is that the links connect. Both ends take the accent. |
| B07 | SHOW | Claim: a demo that re-runs and writes nothing. Five acts land in order, Act II accented; then the zero lands at headline size with the scope of the scan beside it. |
| B08 | SHOW | Claim: four things this does not establish. Each limit is drawn **beside the claim it narrows**, not as a free-floating caveat list. The run-log limit takes the accent. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B03's
  non-finding zero at 0.62 and B04's context segment at 0.55
- Comparisons shown side-by-side, held ≥2s ✓ — B02's before/after columns, B03's real zero
  against the non-finding zero, B04's 21 against 1, B05's three layer cards and B07's acts
  against the zero all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01 — both deliverables named by what they are FOR, and the requirement
                 stated before the count that failed it, so the failure has a referent
WORKED EXAMPLE ✓ B02/B03 — one real audit, six real documents, followed all the way to
                 which of the three zeroes is actually a finding
FALSIFIABILITY ✓ B03 narrows the reel's own headline from three documents to two, against
                 what the source figure's table shows; B04 separates the one citation that
                 changed something from the 21 that did not; B08 attaches a limit to every
                 claim the reel makes, including the run log that has two rows in it
SCAFFOLDED TASK ✓ B10 — list every MUST in your own plan and grep HEAD for evidence of
                 each, rather than checking it against memory
BOOKENDS ✓       B00 cold open · B01 BLUF · B09 verdict · B10 handoff · B11 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop injected by build_beat_sheet.py from
                 figdata.json; the injection ASSERTS six named documents with exactly three
                 absent, that an absent file has no before-count, the 444/104 line split,
                 that exactly 2 of the 3 zeroes are in published documents, the 22/13
                 citation split, that the layer tables account for all 15 tables and each
                 layer's total is the sum of its OWN tables, the 5,806 = 5,806 identity and
                 the 327 that are not marks, 1,019/4,079 == 0.2498, and the demo's 5/5/0 —
                 and fails the build otherwise
```

**0 violations.** Four authoring judgment calls are logged in `BUILD-LOG.md` rather than passed
silently: the six script sections split into eight body beats, narrowing the prior-art zero from
three documents to two, adding B04 (which separates the load-bearing citation from the other
21), and adding the run-log limit to B08.

## The four values not under an assertion

`figdata.json` does not carry the five prior-art names, what the Gornall & Strebulaev citation
changed, the eight-link chain's structure, or the two language-model sites. All four come from
`narration_script.md` and the documents behind it. Each is passed into the build as a named
constant rather than written into a string, and **each beat that uses one says so in its
on-screen source line**. `FACTCHECK.md` rows 6, 10, 17 and 20.

Row 5 is the one that carries weight, and it is not one of those four — it is a *derivation*
that contradicts the source figure's table. `w12-priorart.png` shows three documents at
BEFORE 0; this reel shows two, because the third file did not exist. The figure's own caption
agrees with the reel ("in either published document"). If that reading is wrong, B03 is wrong
and B09's second finding goes with it.

## What this cut is asked NOT to do, and does not

| The material says | This cut |
|---|---|
| "Not thin, not stale — absent" | B02 prints words in the before cell for exactly those three rows. A 0 there would mean "a document with no lines", which is a weaker claim than "no document". |
| "In either published document" | B03 shows two, and separates the third with the reason. The script's own precision is put on the frame rather than left in the voice. |
| One citation is the point | B04 is a whole beat, and it shows the 21 it is being distinguished from. |
| "Break any link and you have an output, not evidence" | B06 draws the chain as a connected descent. A bulleted list would undercut the sentence directly above it. |
| "A demo that recorded a judgment would be clearing a gate for a screenshot" | B07 accents Act II and states what it deliberately does not do. |
| Red is the primary series, never a warning | Terracotta marks the absent documents, the real zero, the load-bearing citation, the append-only layer, the two ends of the chain and the zero write statements — the subject of each beat, never a hazard. |
