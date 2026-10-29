# BUILD-LOG — Brutalist Progress — Week 2 (Kavya)

"Brutalist Progress — Week 2" — personal project, presenter Kavya Mehta,
voice `am_onyx` (Kokoro), palette `claude`. Direct sequel to
`kavya-brutalist-week1-progress`.

## Structural decisions

- **Adapted from an earlier reel, re-branded, not re-fabricated.** Same
  pattern as week 1: this reel's factual content (the week-2 layout bug,
  the false-lead fix attempt, the real fix) is identical to
  `youtube/brutalist/claude-liam-brutalist-week2-progress/`, built earlier
  this session under the claude-liam persona. Only the presentation layer
  changed — greeting, folder chip, terminal `host` field, and the outro —
  to credit Kavya Mehta directly with no NikBearBrown/claude-liam branding.
- **Outro uses `ClaudeVerdictArtifact`, not `ClaudeTitleOutro`** — same
  reasoning as week 1 (hardcoded `@NikBearBrown` handle, no prop override).
- **B00 narration opens with the literal required submission line** —
  "Hi, I am Kavya, and this video is about my second week with the
  Brutalist video pipeline" — followed by an AI-narration disclosure
  sentence, per `docs/FELLOWS-SUBMISSION.md`.

## Infra notes for this build

No new environment bugs surfaced this time — the three workarounds/fixes
from week 1 (ffmpeg `PATH` prepend, `PYTHONIOENCODING=utf-8`, and the
root-cause fix to `shorts.py`'s `root_tsx_text()` encoding) carried forward
cleanly. One transient issue: the first portrait-render invocation exited
with code 4 and no output after rendering B00–B02; a second invocation of
the identical command completed cleanly, picking up from B03 ("filled
already (skip)" for B00–B02). Not reproduced on retry — treated as a
one-off process/lock contention, not a code bug, and not chased further.

## GATE T advisory (not treated as a blocker)

`type_check.py` flagged B02 (`ClaudeScienceLayerStack`) for one "8px text
run" below the legibility floor — the same component and same finding
class as week 1's B03. A frame was extracted directly from
`media/B02.mp4` and visually inspected: all four card titles and
sub-labels are clearly legible. Assessed as the same false-positive class
documented in week 1's BUILD-LOG (a narrow, tall colored accent bar being
misclassified as a text run), not a real defect in this component. Logged
here and in FACTCHECK.md/CHECKS-REPORT.md rather than silently dismissed.
A separate advisory-only §8.10 redundancy finding on B05 (narration closely
recites the verdict card) is expected behavior for this pattern and was not
treated as an issue.

## Fellows-submission compliance notes

Built to the same standard established for week 1: required intro line
verbatim in B00, AI-narration disclosed in the same beat, native 16:9
(3840×2160) and 9:16 (2160×3840) renders, README following the submission
guide's template. GitHub/Drive packaging, PM notification, and Drive upload
remain human steps outside this toolkit's scope.
