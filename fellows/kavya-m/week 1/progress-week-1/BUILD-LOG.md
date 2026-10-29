# BUILD-LOG — Brutalist Progress — Week 1 (Kavya)

"Brutalist Progress — Week 1" — personal project, presenter Kavya Mehta,
voice `am_onyx` (Kokoro), palette `claude`.

## Structural decisions

- **Adapted from an earlier reel, re-branded, not re-fabricated.** This
  reel's factual content (six real pipeline bugs, the four-stage pipeline,
  the Schema Scout milestone) is identical to
  `youtube/brutalist/claude-liam-brutalist-week1-progress/`, built earlier
  this session under the claude-liam / Nik Bear Brown persona. Only the
  presentation layer changed: greeting, folder chip, terminal `host` field,
  and the outro were rewritten to credit Kavya Mehta directly, per explicit
  direction, with no NikBearBrown/claude-liam branding anywhere.
- **Outro swapped from `ClaudeTitleOutro` to `ClaudeVerdictArtifact`.**
  `ClaudeTitleOutro`'s `@NikBearBrown` handle is hardcoded in the component
  source (`runtime/remotion/src/scenes/ClaudeTitleOutro.tsx:19`) with no
  prop override — using it here would misattribute this personal reel.
  `ClaudeVerdictArtifact` (no hardcoded branding) renders a simple
  "Built by — Kavya Mehta" closing card instead, same pattern as
  `youtube/kavya-cabstream-week1-progress/`.
- **B00 narration opens with the literal required submission line** —
  "Hi, I am Kavya, and this video is about my first week setting up and
  debugging the Brutalist video pipeline" — followed immediately by an
  AI-narration disclosure sentence, per `docs/FELLOWS-SUBMISSION.md`'s
  required-content rules (full-length narration verified against the
  compiled audio, not just the beat sheet text).

## Infra bugs hit (and fixed) building THIS reel

Two new, previously-undiscovered environment bugs surfaced in this build,
on top of the six already fixed in the earlier reel:

1. **`generate_audio_kokoro.py` resolved `ffmpeg` to nothing on this shell.**
   `FFMPEG = shutil.which("ffmpeg") or "ffmpeg"` silently fell back to the
   bare string when ffmpeg wasn't on `PATH` in this particular shell
   session, causing a `FileNotFoundError` deep inside `subprocess.run`.
   Worked around per-invocation by prepending
   `runtime/bin/ffmpeg-master-latest-win64-gpl/bin` to `PATH` before each
   pipeline command. Not fixed at the root (would need either a bundled
   fallback path in the script or a permanent `PATH`/`setx` change, which
   is a system-level change outside this build's scope).
2. **`compile.py` crashed with `UnicodeEncodeError` on a Windows console.**
   `'charmap' codec can't encode character '←'` — compile.py prints an
   arrow character (←) to stdout for its "compiled Bnn ← Bnn.mp4" log lines,
   and Windows' default console codepage (cp1252) can't encode it. Worked
   around per-invocation with `PYTHONIOENCODING=utf-8`. Not fixed at the
   root for the same reason as above.
3. **Root cause, fixed at the root: `shorts.py`'s `root_tsx_text()` read
   `Root.tsx` without specifying an encoding**, so on this Windows machine
   the read silently failed (cp1252 can't decode the file's em dashes and
   arrows) and fell back to `return ""` inside a bare `except Exception`.
   Every ONDA CHECK 916-composition lookup in `./art vertical` then failed
   against an empty string, falsely reporting that none of the 916 portrait
   compositions existed in `Root.tsx` — when all nine were actually
   registered and renderable. Fixed by changing
   `p.read_text()` → `p.read_text(encoding="utf-8")` in
   `runtime/scripts/shorts.py`. This is the same bug class as the
   `pronunciation.py:23` fix from the earlier reel — confirmed by testing:
   `./art vertical` correctly rewired all 9 beats to their `916`
   compositions immediately after the fix, with no other change.

## GATE T advisory (not treated as a blocker)

`type_check.py` flagged B03 (`ClaudeScienceLayerStack`) for one "8px text
run" below the 1.9%-of-height legibility floor. Two frames were extracted
directly from the compiled `media/B03.mp4` (mid-clip and near end-of-clip)
and visually inspected — every card title and sub-label is clearly legible
at normal reading size; no 8px text is visible anywhere in either frame.
The most likely explanation is the same false-positive class already
documented for `ReqBars`' bar fill earlier this session: a narrow,
tall colored accent bar (structural, not text) being misclassified as a
text run by the checker's bounding-box heuristic. Not chased further under
this build's time budget; logged here per house doctrine rather than
silently dismissed, and in FACTCHECK.md/CHECKS-REPORT.md.

## Fellows-submission compliance notes (this build's purpose)

Built specifically to satisfy `docs/FELLOWS-SUBMISSION.md`'s required-content
rules, on top of the house ai-explainer paperwork: required intro line
present verbatim in B00's narration, AI-narration disclosed in the same
beat, native 16:9 (3840×2160) and 9:16 (2160×3840) renders (not a crop of
one master), and a README following the submission guide's template — see
README.md. GitHub/Drive packaging, PM notification, branch/PR creation, and
Drive upload are human steps outside this toolkit's scope (the guide is
explicit: "Brutalist does not upload or publish") — not performed here.
