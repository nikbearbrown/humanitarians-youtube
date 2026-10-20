# PEDAGOGY — ab-testing-can-lie-to-you

**Prepared by:** Claude (agent) · **Date:** 2026-10-18
**Skill:** `cli-explainer` (`skills/make/cli-explainer/SKILL.md`)

This is **GATE P**. `generate_audio_kokoro.py` checks it before any narration is generated. An
agent never signs its own gate: everything below is my checklist, and the verdict stays `PENDING`
until you sign it.

## Required-elements checklist

1. **12-beat spine** (INTRO → PROBLEM → CLI→CODE→OUTPUT → CLI→CODE→OUTPUT → SECOND LIE → SUMMARY →
   NEXT STEPS → OUTRO). **CHECK: satisfied** in `NARRATION-SCRIPT.md`. B08 (peeking) is one beat
   by your decision of 2026-10-18, not a full cycle. The MSN mechanism resolves in B09.
2. **REVISION LAW.** **CHECK: satisfied.** B05→B06→B07 (check the split, fix the filter) revises
   B02→B03→B04. The revision *is* the flip, so it stays in the full-length 9:16.
3. **ACTUAL-CODE LAW.** **CHECK: satisfied.** B03 = `py/carousel_v1.py`, B06 = `py/carousel_v2.py`
   (+ `srm_check` from `py/abtest.py`), B08 animates `py/peeking.py`. All three run (Python 3.13.1,
   stdlib, fixed seeds). Every number spoken or shown is in `py/*.out`. Every source line is ≤35
   characters, so the code cards can show it verbatim (lesson from correlation-is-not-causation).
4. **Output beats are motion.** **CHECK: planned.** B01, B04, B07, B08, B09 are Manim. The rest
   are Remotion. No stills.
5. **NO FABRICATION.** **CHECK: satisfied, with four flags.** 24 claims traced in `FACTCHECK.md`.
   Real-world claims come from the authors' PDFs in `sources/`. No carousel numbers are shown,
   because the paper gives none. The code beats are a labeled **simulation** of the mechanism the
   paper describes.
6. **HANDOFF LAW.** **CHECK: satisfied.** B10 reads the prompt aloud and says what to do with the
   answer ("If the split is off, don't read the metrics yet").
7. **Branding (PM).** **CHECK: satisfied on paper.** B00 narration starts with exactly "Hi, I am
   Supriya and this video is about…". No "in for X". "Supriya" appears on every beat: composer
   `folderLabel`, code `handle` chip, Manim corner handle, full-size outro, 9:16 endcard.
8. **Length.** 411 words, about 161s estimated at 2.56 words/s, under the ~175s ceiling, so the
   9:16 is full-length. If measured audio exceeds ~170s, I stop and tighten before rendering.
9. **Honesty caveats.** **CHECK: satisfied.** B02 says outright that we can't see MSN's data.
   B06's fix is framed as ours. B08 keeps the sim's 25% and the paper's 30%+ as separate claims.
10. **No paid services.** **CHECK: satisfied.**

## For you to decide before signing

Flags from `FACTCHECK.md`:

- [x] **Flag A, B01** "On that result, you don't ship." Accurate paraphrase. I suggest no change.
- [x] **Flag B, B06/B09.** The pre-test-clicks fix is attributed to our simulation, not to MSN,
      whose exact fix the paper doesn't describe. I suggest no change. OK?
- [x] **Flag C, B07.** The sim's SRM odds coincide with the paper's own example (~1 in 530k vs
      ~1 in 549k). (i) leave it, or (ii) add an on-screen source line with the paper's real
      821,588 vs 815,482. I lean (ii), on-screen only, with no narration change.
- [x] **Flag D, B08** "past thirty" is [2]'s every-observation case, kept separate from our
      20-look sim. I suggest no change.

## For you to check before signing

- [ ] Read the 12 blocks in `NARRATION-SCRIPT.md` aloud-ish: does the voice land, and is the B00
      phrase exactly what the PM wants?
- [ ] "A-B" spelled with a hyphen in the narration text so Kokoro says "A B", not "A slash B".
      I'll confirm by listening to B00 once audio exists.
- [ ] B03: is "one and a half percent are fans, and the new carousel gives them forty more clicks"
      clear enough for a general analytics audience?
- [ ] The handoff prompt (B10) is one you'd actually want viewers to paste.

Reviewer notes (2026-10-18): Flags A, B, D: leave as-is, agreed. Flag C: option (ii). Add the on-screen
source line with the paper's real figures (821,588 vs 815,482) in B07, with no narration change.
Applied to `NARRATION-SCRIPT.md` and `FACTCHECK.md`.

## VERDICT: PASS

Signed: Supriya Kushwaha (human, author)
Date: 2026-10-18
