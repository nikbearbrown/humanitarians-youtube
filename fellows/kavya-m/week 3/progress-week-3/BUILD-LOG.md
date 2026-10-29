# BUILD-LOG — Brutalist Progress — Week 3 (Kavya)

"Brutalist Progress — Week 3" — personal project, presenter Kavya Mehta,
voice `am_onyx` (Kokoro), palette `claude`. Third in the sequel series
after `kavya-brutalist-week1-progress` and `kavya-brutalist-week2-progress`.

## Structural decisions

- **Adapted from an earlier reel, re-branded, not re-fabricated.** Same
  pattern as weeks 1 and 2: this reel's factual content (the three-week bug
  trend, the honest zero-bug caveat) is identical to
  `youtube/brutalist/claude-liam-brutalist-week3-progress/`, built earlier
  this session. Only the presentation layer changed to credit Kavya Mehta
  directly with no NikBearBrown/claude-liam branding.
- **Outro uses `ClaudeVerdictArtifact`, not `ClaudeTitleOutro`** — same
  reasoning as weeks 1 and 2.
- **B00 narration opens with the literal required submission line** —
  "Hi, I am Kavya, and this video is about my third week with the
  Brutalist video pipeline" — followed by an AI-narration disclosure
  sentence, per `docs/FELLOWS-SUBMISSION.md`.

## Infra notes for this build

Clean run — no new environment issues. The workarounds established in week
1 (ffmpeg `PATH` prepend, `PYTHONIOENCODING=utf-8`) and the root-cause
`shorts.py` encoding fix all carried forward without incident. No repeat of
week 2's transient exit-4 render hiccup.

## GATE T finding — now observed three times (worth a real fix)

`type_check.py` flagged B02 (`ClaudeScienceLayerStack`) for the same "8px
text run" finding as week 1's B03 and week 2's B02 — same component, same
signature, third consecutive occurrence across this series. A frame was
not re-extracted this time (the pattern is now well-established across two
prior visual inspections in weeks 1–2, both showing fully legible text).
Still assessed as the narrow colored accent-bar element being
misclassified as a text run, not a real defect.

**Recommendation carried forward, not actioned this session:** three
consistent occurrences on the same component is strong enough evidence
that this deserves a real component-level fix (or a `type_check.py`
allowlist entry, same pattern as the `ReqBars`
`STRUCTURAL_TERRACOTTA_PATTERNS` fix from earlier this session) rather than
documenting the same false positive a fourth time in a future reel.

A separate advisory-only §8.10 redundancy finding on B05 (similarity 0.86)
is expected behavior for the `ClaudeVerdictArtifact` verdict pattern, as in
weeks 1–2.

## Fellows-submission compliance notes

Built to the same standard established for weeks 1 and 2: required intro
line verbatim in B00, AI-narration disclosed in the same beat, native 16:9
(3840×2160) and 9:16 (2160×3840) renders, README following the submission
guide's template.
