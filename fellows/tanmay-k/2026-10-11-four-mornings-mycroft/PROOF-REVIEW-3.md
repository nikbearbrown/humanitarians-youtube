# PROOF review 3: both masters, *Four Mornings* (Week 26 work video, Mycroft PR #64)

**Stage:** the finished files (2026-10-10). Every frame reviewed here comes out of the masters themselves, 0.7 s
after each on-screen cue as it's spoken, plus 85% of each beat (`_qc/assertion/`, `short/_qc/assertion/`).
- `four-mornings-final.mp4`: 3840×2160, 3:06, 10 beats, 22 frames. The timeline rebuilt from the paced clips
  matches the file (186.3 s against 186.4 s).
- `short/four-mornings-short-final.mp4`: 2160×3840, 1:53, 7 beats, 19 frames (timeline 112.5 s against 112.6 s).

## Verdict

| | Teaching | Production gate |
|---|---|---|
| 16:9 | **12/12** | **PASS**, one cosmetic [EDIT] offered (B08) |
| Short | **11/12** | **PASS** |

No condition for public beyond the usual ones. Every claim traces to `FACTCHECK.md` (W1–W22, main @ 5097a8f), and
every price is invented and labelled on every frame.

---

## 16:9 rubric

| Criterion | Score | Evidence, in the master |
|---|---|---|
| Explicit framework | 2 | B01: the four hand-offs as a strip, all ON TRUST, before any morning |
| Reusable rubric | 2 | "What would they have seen, and what says so now?", asked four times. Each box lights on the line that names its check (B03 21.9 s, B04 9.1 s, B05 15.7 s, B06 8.6 s) |
| Worked example | 2 | Each morning shows the slip, what the reader sees, the step that speaks up, and its committed record |
| Falsifiability / edge | 2 | B07: my own test passed when it couldn't fail. "pass" appears on "It passed", is struck on "But the broken version", and the catch appears on "Now the test". B08: what still runs on trust |
| Active task | 2 | B09: your number, with a good and a weak answer on screen |
| Friction | 2 | B03: the behaviour kept *and* flagged; "the math is right" set against "the reader doesn't know" |

## Short rubric

| Criterion | Score | Evidence, in the master |
|---|---|---|
| Explicit framework | 2 | S02: hand-offs, and the one question for the video, before the example |
| Reusable rubric | 2 | "When a hand-off slips, does anything say so?" asked of META (S03), of GOOGL (S04), answered in S05, then handed to you (S06) |
| Worked example | 2 | S03: the zero, the rule in plain words, then 590.00 (previous close), each on its spoken line (2.7 s, 5.6 s, 16.7 s) |
| Falsifiability / edge | **1** | S04 widens the case (two of five, a missing price as well as a zero), but nothing in the Short tests the fix itself. The long film's B07 does that, and the Short only points to it |
| Active task | 2 | S06, with good and weak answers and a held silence (**measured in the master: 2.57 s**, the 2 s hold plus the beat's tail) |
| Friction | 2 | S05: "didn't change that rule… it's the workflow's choice, not mine" set against "what I added is a record" |

**11/12.** Getting the last point would mean adding a test of the fix (for example, a line on how my own test was
made to fail first). That would lengthen a Short that already carries its own context. Recorded as a choice, not a gap.

---

## Production gate, on the masters

| Check | 16:9 | Short |
|---|---|---|
| Evidence legible at the moment it's said | **PASS.** All 22 frames: B01's total, B03's record and code, B04's ZZZZ set aside, B05's two copies, B06's placeholder id, B07's catch, B08's DRAFT and open steps | **PASS.** All 19 frames: S01's README line, S02's question, S03's three items in order, GOOGL lighting on "The Google stock's" (S04, 4.3 s), S05's record line by line (12.7 s / 13.9 s / 15.2 s) |
| Sources on screen | **PASS.** A committed path and `main @ 5097a8f` on every claim beat. B02's card cites the README and PR #64 | **PASS** on every claim beat |
| "Illustration · every price invented" | **PASS**, all eight dashboard beats | **PASS**, all seven beats |
| Side-by-side held | **PASS.** B05's copies from 10.6 s; B07's struck "pass" beside the catch from 17.1 s | n/a (one-arc Short) |
| Consistency between cuts | **PASS.** B03 now tags GOOGL as well as META, matching the Short and the record (W20) | **PASS** |
| Gate V | 20 frames, 0 BLOCKER / 0 MAJOR | 14 frames, 0 BLOCKER / 0 MAJOR |
| Shorts zones | n/a | Portrait gate 19/19 on master frames |
| Audio | −14.8 LUFS, −1.6 dBTP, 48 kHz. No silence ≥ 1 s | −14.7 LUFS, −1.9 dBTP, 48 kHz. Two silences ≥ 1 s: the S06 task hold (2.57 s), and 1.01 s at the S04→S05 cut, a natural breath before the answer |
| Whisper on the master audio | 0.983. The differences are Whisper's spelling ("$" for dollars, "handoffs", "behavior") plus four dropped or merged words at its 30-second window joins. The same lines read back word for word in the per-beat check, and pacing only adds silence | 0.982. Spelling only ("$", "handoffs", "services" for "service's") |
| Length | 3:06 | 1:53 (under 180 s) |

## Finding

| # | Where | What | Fix | Cost |
|---|---|---|---|---|
| E1 (cosmetic, optional) | 16:9 B08 | The panel title "Still on trust" sits right above a list labelled "STILL ON TRUST", so the same words appear twice | Retitle the panel to what its line says, e.g. "Both recipes still say DRAFT", and keep the list label | Re-render B08 alone, then recompile, re-pace, re-normalise and re-check the master |

## What works

- **The structure carries.** Five mornings on one dashboard, each a different slip. The hand-off strip fills in
  as the film goes, so the viewer can see where they are.
- **The turn is mine, and it's shown as rigour.** B07 is the only mistake in the film. It's shown with its fix and
  the one-cent catch, never as a gotcha.
- **The Short stands alone.** Who, what and why come first, the idea comes before the example, and the jargon is
  explained. Two cases, the record as the answer, then your turn. It reads as one arc, and each frame opens where the
  last one ended.

## Tooling note (recorded, not hidden)

Neither pixel gate catches overlapping text. The S03/S05 overlaps at the stills stage were found only by looking.
Every frame in this review was looked at, not just gated.

## E1 applied (2026-10-11)

B08's panel is retitled "Both recipes still say DRAFT" (the list keeps "STILL ON TRUST"). Only B08 was re-rendered;
the other nine beats' props are unchanged and their render stamps kept. The 16:9 master was recompiled, re-paced and
re-normalised: −14.8 LUFS, Gate V 20 frames 0/0, all 22 timing frames re-extracted, and B08 checked at 14.1 s.
