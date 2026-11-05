# CHECKS-REPORT — hai-agents-on-their-own

Every gate this reel was run through, with the result as the tool reported it.

## Gate T — typography and contrast

Spec: `skills/make/kerning/reference/type-spec.md` §8. Floor 1.9% frame-height,
contrast 4.5:1 WCAG, kern threshold 3.5x expected advance, wordy budget 2 elements.

**Landscape** — Reel: `hai-agents-on-their-own`  |  Checked: 2026-10-20T16:57  |  Overall: PASS  |  Beats checked: 10  |  FAILs: 0

**Vertical** — Reel: `hai-agents-on-their-own-vertical`  |  Checked: 2026-10-20T18:11  |  Overall: PASS  |  Beats checked: 10  |  FAILs: 0

Full per-beat table in [TYPECHECK.md](TYPECHECK.md).

## Gate V — visual QC

# Gate V — visual QC report

Frames sampled: 20  ·  BLOCKER: 0  ·  MAJOR: 0

Clean — no BLOCKER/MAJOR defects. ✓

Contact sheet: [qc-contact-sheet.png](qc-contact-sheet.png)

The per-beat frame grid (`qc-sheet.png`) is excluded by the repository's own
`.gitignore` rule `**/qc-sheet.png` and is held locally with the build.

## Gate F — fact check

Claim-level verdicts in [FACTCHECK.md](FACTCHECK.md). Rows marked SPEC-ASSERTED are the
open ones: consistent with local evidence but not checked against primary published
documentation during the build. That sign-off is the fellow's and is still outstanding.

## Build gate

Beats filled 10 of 10, zero slates, zero skin warnings.
Full record in [BUILD-LOG.md](BUILD-LOG.md).
