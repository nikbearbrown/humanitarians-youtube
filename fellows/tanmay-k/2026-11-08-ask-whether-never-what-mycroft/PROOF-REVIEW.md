# PROOF review of the two compiled videos (moment-of-assertion, 2026-11-09)

> Final-stage review of the compiled films (earlier stage reviews are kept locally; this one supersedes them).

**Reviewed:** `ask-whether-never-what.mp4` (long, 209.8 s) and `ask-whether-never-what-short.mp4` (Short, 80.1 s). Method: (1) `build/proof_moments.py` takes 38 claims, finds the second each is spoken on the Whisper clock, and checks whether its evidence is already on screen, at what opacity (the fade is 0.35 s, smoothstep) and for how long it stays up (`proof_moments.out`); (2) frames pulled from the compiled files at the moment of the claim (B00b, B03, B04, B05, B06, B07b x2, B08, B10; S02, S03, S04, S05, S06 x2), read for legibility; (3) the measured gates in `PROOF-REVIEW-VIDEO.md` (16 of 16).

## Long film, 16:9
**Verdict: clear-for-public at video level. Teaching 12/12. Production gate PASS.**
One line: this film teaches one move (ask whether a secret exists, who must approve it, and never what it is) by following one row all the way, and it shows the receipt for each claim as the word is spoken.

| Criterion | Score | Evidence in the film |
|---|---|---|
| Explicit framework | 2 | B02: the three facts (is it there, who says yes, the value) appear as three boxes, the third closed, before any row exists. |
| Reusable rubric | 2 | The same three questions apply to any key, service or account; B09 hands them over on screen. |
| Worked example | 2 | B03 to B05: one row fills field by field on the word (`name`, `status`, `reason`, `GROQ_API_KEY`, the three `false` fields). |
| Falsifiability / edge case | 2 | B07b: both keys set, both `credential_present: true`, and `found: none` and `37 of 37` on screen as they are spoken. |
| Active task | 2 | B09: a three-line card, the first two filled, the third left closed. |
| Friction | 2 | B00b poses the question over a clean run; B07 is a real tension (a test of secrecy needs a secret), resolved on screen. |

**Production gate**
- **Evidence legible at the moment of assertion: PASS.** 23 long-film claims checked: every evidence group is on screen at its word with opacity at least 0.6 (21 of 23 at exactly 0.61, the lead I set, and 2 fully in), above the 0.4 floor. The frames show every field readable at the moment (B04 `credential_present: false` and `here: no`, B05 four `false` fields, B07b `found: none`).
- **Sources on screen: PASS.** Every evidence beat carries its file in the footer: `source-check.json` (B00b, B03 to B06), the step 2 script (B04), the self-test results (B07b), `ingest-audit.md` (B08), the recipe and pull request address (B10). Beats with no factual claim (B00, B02, B04b, B09, B11) show none, which is correct.
- **Side by side, held at least 2 s: PASS.** B04's row and code excerpt together for about 9.9 s; B07b's split (rows left, scan right) about 14.8 s; B06's four rows with the 12 / 10 / 0 panel and the hand-off line about 15 s.

**Findings (all minor; none blocks)**
1. **[JUDGEMENT] B01**: the six-step list sits for about 9 s before the step-two highlight (the narration is introducing the recipe). Optional edit: let the rows arrive as "five of its six steps" is said. Within the 12 s limit.
2. **[JUDGEMENT] B08**: the footer's first clause is bright and the second half dimmed, as you chose; the narration says "never stored". Nothing to change.

## Short, 9:16
**Verdict: clear-for-public. Shorts rubric 12/12 after the two timing fixes below (applied and re-measured 2026-11-09).**
One line: this Short opens on a puzzle, builds its context before any technical word, and ends on its own thought and the long film's exact title; two seams in its reveal timing are worth a small edit.

| Criterion | Score | Evidence |
|---|---|---|
| Hook | 2 | The puzzle is spoken from 0.3 s and its first headline line is on screen from frame 1. |
| Standalone context | 2 | Who and what (S02), what the pipeline reaches for (S03) come before the first field name; "environment" is spoken as "the program's settings". |
| One arc with its own ending | 2 | Question (S01), the row (S03 to S05), the test (S06), the ask and the title (S07); not the long film's beats stitched together. |
| Phone legibility | 2 | Smallest type 68 px at master size, all ink inside the safe zone on every sampled frame. |
| Pace | 2 | Longest still stretch 3.0 s (limit 3.0): the row changes on the words; the mid-line headline reveals do the rest. Exactly at the limit, so any further delay would fail. |
| Trailer function | 2 | The exact title with its colon is fully up for about 2.7 s before the loop fade; name and channel are spoken in S02. |
| Moment of assertion | 2 | 15 of 15 claims pass after the fixes (38 of 38 across both films). |

**Moment-of-assertion flags (Short): both fixed.** S02: the slate dissolve now starts 0.5 s before the line (was 0.2 s), so the name is at opacity 0.61 as it is spoken. S03: the `reason` field is revealed 0.45 s ahead of its word, so it is up for 2.1 s. Re-measured: all nine Short checks pass; 38 of 38 claims pass.

Original flags:
1. **[EDIT] S02, "Tanmay K."**: the name starts to fade in at the instant it is spoken (opacity 0.0 at onset, full about 0.35 s later), because the slate dissolve into S02 is still under way. Fix: start the S02 slate dissolve about 0.3 s earlier, or reveal the name on "I'm". Cosmetic; it still lands inside the name's three words.
2. **[EDIT, minor] S03, "reason"**: the last field is up only 1.8 s (under the 2 s rule) because the dissolve into S03b begins at 28.7 s, 0.6 s after S03's last word. The words and the field are in step; the field simply goes quickly. Fix: a 0.4 s longer pause after S03, or start S03b's dissolve 0.3 s later.

## What could not be judged here
- **Fonts**: Arial and Menlo again, as in the topic films; the earlier question about open fonts has had no answer, so the YouTube text and README will make no open-fonts claim (see the font note in memory).
- **Links**: README placeholders for the two YouTube addresses stay as placeholders.

## What works
- The one-row design holds through both films: the closed value cell is on screen in every frame where it matters, and nothing key-shaped appears anywhere.
- Every number and field name on screen is read from the committed files, and a fresh run of the command reproduced the terminal shot.
- No hard cut anywhere (largest frame-to-frame change 2.23 of 255 long, 1.16 Short), and the Short loops (difference 0.02 of 255).
