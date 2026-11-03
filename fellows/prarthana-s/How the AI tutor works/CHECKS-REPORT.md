# CHECKS-REPORT — How the Tutor Stays Grounded in Your Textbook

Written before the first compile, per the PROOF GATE in `skills/make/ai-explainer/SKILL.md`.

```
10 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

| Beat | Act | Scene | Class | Note |
|---|---|---|---|---|
| B00 | HOOK | `MedhavyTerminalAsk` | SHOW | Cold open on the ask surface; the puzzle holds before it is answered. |
| B01 | OVERVIEW | `MedhavyOpen` | SHOW | The whole claim in one breath, one line per spoken clause. Advance organizer. |
| B02 | CONTRAST | `MedhavyTwoColumnCard` | SHOW | Framework beat, placed before any example. Comparison held side by side ≥2s. |
| B03 | MECHANISM | `MedhavyConceptCard` | SHOW | Four steps reveal in narration order; step four visually separated. |
| B04 | PREDICT | `MedhavyPredictCard` | SHOW | Viewer commits before the reveal. Deliberate quiet beat. |
| B05 | REVEAL | `MedhavyCodeBlock` | SHOW | Real index record, not prose restyled as code. Worked example. |
| B06 | TEST | `MedhavyConceptCard` | SHOW | A test the viewer can run, plus the honest cost. Falsifiability. |
| B07 | CLOSE | `MedhavyTwoColumnCard` | SHOW | Verdict; benefit and cost weighted equally, neither faded. |
| B08 | HANDOFF | `MedhavyTerminalAsk` | SHOW | Prompt typed **and** read aloud verbatim, then discussed. |
| B09 | OUTRO | `MedhavyOutro` | SHOW | Series end card, identical to episode 01. |

## GATE L — library-first

Every pattern checked renderable against `Root.tsx` before authoring. **Zero punts, zero
slates** — the first compile is a complete cut, not a previz.

```
MedhavyTerminalAsk  OK    MedhavyOpen        OK    MedhavyTwoColumnCard  OK
MedhavyConceptCard  OK    MedhavyPredictCard OK    MedhavyCodeBlock      OK
MedhavyOutro        OK
```

**Not used, and why:** episode 01's scenes (`MedhavyHook`, `GroundedTutor`,
`MedhavyBookTutor`, `MedhavyHub`, `LearningPaths`, `LearnerMemory`, `InstructorIntro`,
`CoInstructorPipeline`, `CourseCreationProblem`, `CourseImportPipeline`, `MedhavyClose`)
declare **no props** — they are hardcoded to that episode's content and cannot carry new
material. Reusing them would have meant a caption saying one thing while the picture said
another.

## Anti-wallpaper audit

No two consecutive beats share a scene. `MedhavyConceptCard` recurs at B03 and B06,
`MedhavyTwoColumnCard` at B02 and B07, `MedhavyTerminalAsk` at B00 and B08 — each pair
separated by at least two beats.

## Audio — the clock (locked 2026-09-09)

Kokoro `af_bella`, `--speed 0.9`, matching episode 01.

```
B00 16.87   B01 19.75   B02 19.61   B03 20.50   B04 16.28
B05 22.04   B06 20.97   B07 17.54   B08 24.58   B09  3.73
                                        total  182.0s = 3:02
```

Episode 01's target was 180s. This lands within two seconds of it without being trimmed
to fit — duration stayed an output.

## Narration budget

Body beats B01–B07: 50–63 words, inside the ~45–70 band. B00 (47) and B08 (72) sit under
the bookend exemption — the handoff's read-and-discuss requirement pushes it long by design.

## Build environment

Two Windows bugs in the toolkit blocked rendering; both patched locally in this clone and
written up in `../BRUTALIST-WINDOWS-BUGS.md` for upstream. `run.sh` was bypassed in favour
of calling `remotion_scenes.py` and `compile.py` directly, which the toolkit sanctions.

## Open items

- [ ] Visual QC pass — sample frames at ≥2 fps into `_qc/`, **read the PNGs**, audit the
      9-point rubric, log to `_qc/REPORT.md`. A build nobody looked at is not done.
- [ ] `BUILD-PROMPT.md` — mandatory; a reel without its build prompt is unfinished.
- [ ] GATE F paperwork (`FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`) if `./art run` is
      used later instead of the direct scripts.
- [ ] 9:16 companion — a separate beat sheet with portrait-native scenes, never a crop.
      Note this cut is 3:02, already at the shorts cap, so the vertical needs trimming.
