# PEDAGOGY — correlation-is-not-causation

**Prepared by:** Claude (agent) · **Date:** 2026-10-14
**Skill:** `cli-explainer` (`skills/make/cli-explainer/SKILL.md`)

This is **GATE P**. `generate_audio_kokoro.py` checks it before any narration is generated. An
agent never signs its own gate: everything below is my checklist, and the verdict stays `PENDING`
until you sign it.

## Required-elements checklist

1. **12-beat spine** (INTRO → PROBLEM → CLI→CODE→OUTPUT → CLI→CODE→OUTPUT → MECHANISM → SUMMARY →
   NEXT STEPS → OUTRO). **CHECK: satisfied.** B00–B11 in `beat_sheet.json`. MECHANISM sits after
   the second output (B08) because the "why" only makes sense once the flip has been seen.
2. **REVISION LAW.** At least one revision cycle. **CHECK: satisfied.** B05→B06→B07 (split by stone
   size) after B02→B03→B04. Here the revision *is* the lesson, so it stays in the 9:16 too
   (full-length, approved).
3. **ACTUAL-CODE LAW.** **CHECK: satisfied.** B03 = `sql/q1_by_treatment.sql` and B06 =
   `sql/q2_by_size.sql`, verbatim. Both run on SQLite against `sql/kidney_stones.sql`, and their
   saved output (`sql/*.out`) is exactly what B04 and B07 animate. Re-run 2026-10-14 after the
   comment fix: output unchanged.
4. **Output beats are motion.** **CHECK: satisfied.** B01, B04, B07, B08, B09 are Manim; the rest
   are Remotion. No stills.
5. **NO FABRICATION.** **CHECK: satisfied, with three wording flags.** All 14 claims trace to the
   scanned primary pages; see `FACTCHECK.md`. Citations verified against PubMed and the printed
   pages (one page-range correction: Julious & Mullee is 1480–1481). Flags A and B below are
   accuracy-of-framing issues, not wrong numbers.
6. **HANDOFF LAW.** **CHECK: satisfied.** B10 reads the prompt aloud and says what to watch for:
   if the winner flips, the dashboard was measuring the mix.
7. **Branding (PM).** **CHECK: satisfied on paper.** B00 narration starts with the exact phrase
   "Hi, I am Supriya and this video is about…". No "in for X". "Supriya" appears on every beat:
   composer `folderLabel`, code `handle` chip, Manim corner handle, full-size outro `handle`, and
   the 9:16 endcard.
8. **Length.** ~148s estimated (379 words at the measured 2.56 words/s), so the full-length 9:16
   fits under the 180s cap with the endcard.
9. **Honesty caveat.** **CHECK: satisfied.** B09 says the split is still observational, backed by
   Julious & Mullee's own wording.
10. **No paid services.** **CHECK: satisfied.** SQLite, Kokoro, Manim, Remotion, all local.

## For you to decide before signing

Flags from `FACTCHECK.md`. Decisions recorded 2026-10-15.

- [x] **Flag A, B00.** "point you to the worse treatment" → *suggested* "point you to the wrong
      answer". The paper weighs cost and morbidity too, so "worse" overstates it.
- [x] **Flag B, B01.** "Doctors treated kidney stones two ways" → *suggested* "A study compared
      two ways of treating kidney stones". The study also had a third method (ESWL).
- [x] **Flag C, the eras.** Open surgery 1972–80, PCNL 1980–85. I suggest no narration change,
      because B09's caveat covers it. Agree?

## For you to check before signing

- [ ] Read the 12 blocks in `NARRATION-SCRIPT.md` aloud-ish: does the voice land, and is the B00
      phrase exactly what the PM wants?
- [ ] B08's "the hard cases went to surgery": clear to a general audience, and fair (it describes
      who got what, not anyone's intent)?
- [ ] "Large stones" in the narration while the on-screen label reads "≥2 cm or multiple": is that
      simplification acceptable?
- [ ] The handoff prompt (B10) is one you'd actually want viewers to paste.

Reviewer notes (2026-10-15): Flags A and B accepted and applied to `NARRATION-SCRIPT.md` and
`beat_sheet.json`. Flag C: no change, because B09's caveat already covers it.

## VERDICT: PASS

Signed: Supriya Kushwaha (human, author)
Date: 2026-10-15
