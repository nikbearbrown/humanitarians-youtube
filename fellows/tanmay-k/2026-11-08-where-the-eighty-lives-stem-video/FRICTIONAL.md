# Frictional Log — where-the-eighty-lives (Week 30 topic video, long and Short)

**Record provenance:** drafted 2026-11-08 with Claude from this folder's own records (`TOPIC-DECISION.md`, `ANGLE.md`, `MEASUREMENTS.md`, `FACTCHECK.md`,
`AUDIO-CHECK.md`, the proof reviews, the gate logs), after the work was done rather than while it happened. **Awaiting Tanmay's review.**
Every entry points at the record it comes from.

## 2026-11-07 — Two draws that looked unique and were not, and a pool with a hole in it
- **Work and expectation:** draw the week's topic at random from the `claude-for-<topic>` collections, check nothing else covers it, with commands that only read (Tanmay asked that fellows' work not be disturbed, so no `git fetch`; branches and trees came from read-only GitHub API calls).
- **Where it resisted:** the first draw, `claude-for-design/json`, is a folder name that hides a film: the "AI help made students worse" thesis already sits in five other folders under other names. The second, `ai-slop`, had a second copy outside `claude-for-*` (under `claude/claude-research/`). The pool script had never scanned `claude/`, `codex/` or `claude-bear/`, so name-based counting missed both.
- **What was done:** both draws were rejected before any angle work; the pool was rebuilt wider (3,961 paths instead of 2,191); only `lstm-ops` and `mma-vs-boxing` appeared once library-wide; the third draw landed on `lstm-ops`, and a code search for its idea returned only its own folder.
- **Record:** `TOPIC-DECISION.md`.

## 2026-11-07 — An observation that needed a mechanism
- **Work and expectation:** the library film shows a smaller model running far slower than a bigger one. Our angle was to build on that and ask where the time can come from, without contradicting it.
- **Where it resisted:** counting multiply-adds gives the two cost models the same arithmetic, so counting could not be the source of any gap. The first Python pass showed a large gap (28x), but it was mostly interpreter overhead and could not be quoted.
- **What was done:** the comparison was rebuilt in compiled C with the weights, the multiply-adds and (after the fix below) the gate work held equal, and the only difference left was dependency. Re-measured across four kernels, the gap grows with how much each loaded weight can be reused: 1.0x with nothing to overlap, about 1.3x with reuse, about 3.7x with an optimized multiply. The dial of "how much the chip can do at once" came from that result, not the other way round.
- **Record:** `ANGLE.md`, `MEASUREMENTS.md`.

## 2026-11-08 — A comparison that was not like for like
- **Work and expectation:** the narration said "same arithmetic"; the measurement file said the two sides did the same gate work too.
- **Where it resisted:** re-reading the code against the claim during the fact-check showed the recurrent side evaluated five gate functions per hidden unit per step and the parallel side two. The multiply-adds were equal; the gate work was not. Fixing it moved the optimized-multiply gap from 5.7x to about 3.7x (the repeats of the original program had ranged 5.2x to 6.5x), the plain-loop result from 1.03x to 1.0x, and the "most I could make" from about six times to about four.
- **What was done:** the measurement code and file were corrected and the superseded run kept (`measurements_v1/`); an ablation without the gate work gave the matrix-only figure (about 6.3x) as the explanation of the earlier number; Tanmay chose the full-step set; six narration lines were reworded and re-signed, then the audio, captions, both videos and both YouTube files were rebuilt and re-measured. The structure and the argument did not change.
- **What it is evidence of:** the fact-check worked, before anything was published.
- **Record:** `FACTCHECK.md`, `MEASUREMENTS.md`, `GATE-P-SIGNOFF.md`.

## 2026-11-08 — Two words the voice cannot spell
- **Work and expectation:** the film turns on "weights" and "wait", which sound the same.
- **Where it resisted:** Whisper heard "weight" for "wait" in four lines (S04, S07, S10, B07) even with the sentence around it. Kokoro says the words correctly; the two words are the same sound.
- **What was done:** Gate P had kept the pair with a condition (captions show the spelling); Tanmay listened and chose to keep all four lines, and the pace of B00 and B09 as well. No narration changed.
- **Record:** `AUDIO-CHECK.md`, `GATE-P-SIGNOFF.md`.

## 2026-11-08 — What the measurements found before anyone watched
- **Where it resisted:** Whisper writes "6.9" as two tokens, so the first figure timing found nothing and every figure appeared before it was spoken; the three-panel frame vanished at the start of each beat and came back at the end; table cells bunched into the first four seconds of B08 and left 11.7 s still; "THE SAME" appeared before the second bar in S06; S09's "80" matched the word "eighty" in S01; a ring sat off-centre round its text; B09's source line landed 0.6 s after its claim. The Short as first built dissolved between slides, with 0.7% to 17% of the picture carried across line changes. The check script itself loaded a whole film into 8 GB of memory and ran for over 40 minutes.
- **What was done:** each was fixed and re-measured. Figures are pinned to the word that voices them; the Short was redesigned as one persistent scene (48% to 91% carried); the dial turns in both formats; the check now streams frames and runs in 87 seconds.
- **Record:** `PROOF-REVIEW-FRAMES.md`, `PROOF-REVIEW-FRAMES-2.md`, `PROOF-REVIEW-VIDEO.md`, `PROOF-REVIEW-VIDEO-2.md`, `check_video.out`, `proof_video.out`.

## 2026-11-08 — Fonts the channel does not own
- **Where it resisted:** both films are drawn in Arial and Menlo, which ship with macOS; Weeks 27 to 29 used open-licence fonts. The licence terms for a monetized channel were not verified.
- **What was done:** Tanmay chose to keep them for now; the YouTube text says nothing about the fonts; the question comes back before the folder is staged.
- **Record:** the saved note on this decision, `where-the-eighty-lives-youtube.md`.
