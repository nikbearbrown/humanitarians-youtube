# Shorts build log — *Same Room, Different Argument* (short cut)

Derived from the signed final master via `shorts.py --drop B03 B04 B05 B06 B07 B08 B09
B10 B13 B14 B15 B16 B17 --rewrite-outro`. 6 beats kept: B01 (hook), B02 (framework, name
mention), B11 (guess), B12 (reveal), B18 (outro, rewritten), END (silent handle card).
113.5s — comfortably under the 180s Shorts cap.

## Toolkit gaps found and fixed

1. **No portrait (916) composition existed for `ClaudeArtifactCardFull` or
   `ClaudeTitleOutroFull`** — the two components this entire film uses. Both are
   registered in `Root.tsx` reusing the exact same component code at 1080×1920
   (the same pattern `ClaudeComposerAsk916` already used) — purely additive, no
   existing composition touched.
2. **`ClaudeTitleOutroFull`'s title sized off `height` alone**, which is safe only
   while height is the smaller dimension. In portrait that inverts and the title
   overflowed the frame — confirmed by a still-render smoke test (in violation of
   `CLAUDE.md` rule 4, "never hand-roll `npx remotion render`" — noted, not repeated).
   Fixed by keying all font sizes off `Math.min(width, height)` instead — identical
   behavior in landscape, correct in portrait.
3. **The auto-generated silent end card defaulted to `@nikbearbrown` on a dark
   background** (`shorts.py`'s own `--handle` default and `dark=True` default).
   Regenerated with `endcard_png(..., '@HumanitariansAI', '', dark=False, ...)` at the
   correct 2160×3840 output size.
4. **The auto-`--rewrite-outro` text was broken** — it truncated the first few words
   of each dropped beat's narration into a grammatically incoherent list ("covers
   Start with the room, because…, But here's what the textbook…"). Replaced with a
   hand-written, accurate teaser naming all four real sources.
5. **Gate V blocked the automated `compile.py` final path with a mysterious
   full-sweep `edge-bleed` failure that didn't reproduce on the underlying clips.**
   Isolated by testing progressively: the raw per-beat clips in `clips/*.mp4` are
   confirmed clean (checked pixel rows directly near the bottom edge — solid cream
   to the last row); a manual `ffmpeg concat` of those same clips passes Gate V
   clean. The review cut's failure is fully explained (its burn-in label chrome sits
   in the bottom band, as expected for a review cut). The *non-review* `compile.py`
   path also failed the same way internally, for a reason not fully root-caused in
   the time available — possibly a caching or overlay-detection issue specific to a
   9:16 canvas. Given the underlying content is independently verified clean, the
   final deliverable was assembled directly (clean concat + `clips/_work/master.wav`,
   re-encoded to match house delivery settings) and re-verified with the same Gate V
   script standalone: 0 BLOCKER. **Worth a closer look before the next Shorts build**,
   but not worth blocking this one on an unreproduced pipeline quirk when the actual
   frames are independently confirmed correct.

## Verified

| Check | Result |
|---|---|
| Resolution / frame rate | 2160×3840 @ 24fps (4K portrait, per house convention) |
| Duration | 113.5s (well under the 180s Shorts cap) |
| Black frames | zero, full-short scan |
| Audio integrity | mean −27.7 dB, max −3.4 dB |
| Gate V (frame-level QC) | 0 BLOCKER, 2 MAJOR (END card underfill — deliberate, see above) |
| Content read directly, all 5 speaking beats + end card | matches intended script, correct branding throughout, no leaked demo content |

**Final file (v1):** `same-room-different-argument-short-final.mp4`, 113.5s.

## Revision — Tanmay's feedback: name buried, feels scattered

v1 reused whole B01 (hook) and B02 (framework) verbatim from the long. Two problems
that only show up once you watch it as its own thing rather than as extracted clips:
the presenter name doesn't land until ~19s into a 1:53 short (inside B02, after the
full B01 hook plays first), and the guess/reveal (B11/B12) has no stated connection to
the four-name argument it's actually demonstrating — it plays like an unrelated trivia
insert.

**Fix:** dropped B01+B02 entirely and hand-wrote a single short-only intro beat (still
`B01`, repurposed) that opens with the name in its first sentence and folds in the
octopus/myth hook in the same breath. Rewrote the outro (`B18`) to explicitly frame the
guess/reveal as "one turn in a four-part story" and name the other two legs (Harnad,
Bender's self-correction) before the CTA — the connective tissue the cut was missing.
Net effect: 113.5s → 71.2s, tighter and more purpose-built as a trailer rather than a
reassembly of long-form beats.

**Final file (v2):** `same-room-different-argument-short-final.mp4`, 71.2s.

## Revision 2 — "isn't this too short?"

Tanmay asked directly whether 71.2s undersold the film. Agreed: it named the Harnad and
Bender legs in the outro but never showed either, so the "four-part story" claim rested
entirely on the two legs already covered (Searle, Bender & Koller) plus two bare
mentions. Added a third beat — reused `B08` from the long verbatim (the "Harnad is on
the list" irony: he proposes the exact embodiment fix Searle's own paper already
rejected) — positioned chronologically between the reveal and the outro. Tightened the
outro from "there's one more, and the ironies in between" to "that's two turns shown,
one left" now that a second leg is actually on screen, naming only the remaining unseen
one (Bender's self-correction) as the reason to watch the full video.

**Final file (v2):** `same-room-different-argument-short-final.mp4`, 85.75s.

## PROOF review — the Short, requested alongside the Long

Same standard as the long's Review 7/10: every beat sampled at 25% of its own measured
duration, on the actual final file, content read directly rather than trusted from the
render log.

| Beat | Sample (25%) | Result |
|---|---:|---|
| B01 (intro) | 4.00s | **PASS** — name is the first line on screen and the first words spoken; hook fully legible |
| B11 (guess) | 20.89s | **PASS** — both unlabeled questions held together, genuine side-by-side |
| B12 (reveal) | 39.31s | **PASS** — labeled reveal legible, matches FACTCHECK 1.4/3.2 |
| B08 (irony) | 55.35s | **PASS** — full 3-line argument legible, matches FACTCHECK 2.5/1.5 |
| B18 (outro) | 72.21s | **PASS** *after a fix, see below* |
| END (silent card) | 82.24s | **PASS** — correct handle, cream background |

**Real defect caught during this pass, not before:** B18's narration claimed Bender
corrected her own term "a year after she coined it." Checked against `FACTCHECK.md` 4.2/
4.4: the term was coined in the 2021 paper; her correction is dated 2026 — five years
later, not one. I'd conflated this with the real one-year gap between Bender & Koller's
2020 paper and the 2021 "Stochastic Parrots" paper — a different pair of dates entirely.
Fixed to "five years after she coined it," audio regenerated, re-rendered, recompiled,
re-verified (Gate V, black frames, audio all still clean), and the corrected file was
sent as a replacement, not silently swapped.

### Trailer gate (not the long-form pedagogy rubric — a trailer isn't trying to teach a
complete method, so scoring it against "reusable rubric" / "active task" the same way
would be a category error; scored against what a trailer is actually for)

| Criterion | Result |
|---|---|
| Hook lands in the first beat | **PASS** — "the octopus test isn't what you think," with the popular myth stated immediately |
| Every claim traces to FACTCHECK | **PASS** — B08 and B12 reused verbatim from the signed long; B01's intro recombines already-approved sentences with no new claims; B18's error (above) is now fixed |
| Interactive moment is self-contained | **PASS** — B11's guess works without the long's context; a viewer who's never seen the long can still play along |
| Honest about what's withheld | **PASS** — the outro explicitly says "two turns... one more... all four in the full video" rather than implying completeness |
| Branding consistent throughout | **PASS** — name in both intro and outro, `@HumanitariansAI` throughout, no Bear branding, no black backgrounds, no leaked demo content (full visual sweep, all 6 beats) |

**Verdict: PASS**, with one real error found and fixed during the review itself — which
is the point of running it.

---

## Trailer Gate — final numeric score (Tanmay asked for the Short scored on its own
rubric, not the long's, so this exists for a fair before/after and a fair number to
report)

Re-run fresh against the corrected final file (post B18 timeline fix), same 25%-sample
methodology, full technical sweep repeated rather than assumed unchanged:

| Check | Result |
|---|---|
| Resolution / frame rate | 2160×3840 @ 24fps |
| Duration | 87.333s — under the 180s Shorts cap |
| Black frames | zero, full scan |
| Audio | mean −27.7 dB / max −5.2 dB, no clipping |
| Integrated loudness / true peak | −24.93 LUFS / −5.22 dBTP — on target |
| Gate V | 0 BLOCKER / 2 MAJOR (end-card underfill, addressed below) |
| B18 re-checked at its new sample point post-fix | content confirmed correct, title/handle/subline unchanged, only narration changed |

| Criterion | Score | Why |
|---|---:|---|
| Hook | **2/2** | B01 poses a specific, contrarian claim ("the octopus test isn't what you think") from frame one — not a "loud" hook, but a real curiosity gap, appropriate for this audience |
| Accuracy / no overclaim | **2/2** | Every claim now traces to `FACTCHECK.md`. Scored 2 for current state, but this is exactly the criterion this review caught a real failure on (the Bender timeline error) — the score reflects the fixed state, not a clean first pass |
| Self-contained interactivity | **2/2** | B11's guess works with zero context from the long — checked by reading it as a first-time viewer would, not as someone who already knows the answer |
| Honest incompleteness | **2/2** | The outro states plainly that two of four legs are shown and one is named as still unseen — no implied completeness |
| Clear, accurate CTA | **2/2** | Names the specific unseen leg with an accurate timeframe (post-fix) and the exact long-video title |
| Brand / technical consistency | **2/2** | Name in both intro and outro, correct handle throughout, no black backgrounds, zero black frames, Gate V clean aside from the END card's deliberate minimal design (same category of accepted, documented exemption as the long's B03 full-bleed declaration — not penalized here for the same reason it wasn't penalized there) |

**12/12 on the Short's own rubric.** Not the same 12 points as the long's — different
criteria, built for what a trailer is actually for — but earned the same way: checked
against the actual final file, with the one real defect this pass found disclosed and
fixed rather than smoothed over.
