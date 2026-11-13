# Report: Claude, Tested. — Chapter 5 (Generate the Assessments the Blueprint Promised), Two Cuts

**Topic:** AI1 CLI Chapter 5 — Generate the Assessments the Blueprint Promised (quizzes/flashcards/exercises, the cognitive-science backing, Bloom's taxonomy as audit vocabulary, the real worked example)
**Skill:** `deep-explainer` (brutalist.art toolkit)
**Location:** `humanitarians-youtube/fellows/divyank-s/2026-09-20-chapter5/`
**Cost:** $0.00 (Kokoro TTS, local Remotion rendering, no API keys)

## 1. Deliverables

| | 16:9 master | 9:16 Short |
|---|---|---|
| **File** | `claude-liam-generate-the-assessments-the-blueprint-promised.mp4` | `short/claude-liam-generate-the-assessments-the-blueprint-promised-short.mp4` |
| **Resolution** | 3840×2160 (4K UHD) | 2160×3840 (4K UHD, vertical) |
| **Duration** | 348.53s (5:48.5) | 137.02s (2:17.0) |
| **Beats** | 32 | 13 |
| **Gate** | `PEDAGOGY.md` — `VERDICT: PASS` | derived from the signed-off parent |
| **Signed** | "Liam, in for Divyank" / `@DivyankSingh` throughout — **except the outro title card, see §5** | same |

Both are real, rendered, playable files. Neither is published or authorized for publication.

## 2. Source and how it's covered

Source: `ai1-cli/chapters/05-generate-the-assessments-the-blueprint-promised.md`,
read in full. The chapter's own shape maps to 4 acts:

| Act | Content | Beats |
|---|---|---|
| **I — Three Reasons These Aren't Decoration** | Quizzes (testing effect, Roediger & Karpicke 2006, ~61% vs. ~40%), flashcards (spacing effect, Ebbinghaus 1885, Anki's SM-2/Woźniak 1987), and exercises (pushing past recall into application) | `A1-1`–`A1-6` |
| **II — The Word For What's Wrong** | Bloom's taxonomy (Anderson & Krathwohl's 2001 revision) as the vocabulary for diagnosing a question that tests below its outcome's demanded level | `A2-1`–`A2-6` |
| **III — Generate, Then Hunt the Failure** | The chapter's real worked example: a generated Chapter-3 quiz question ("What command builds the book?") that tested Remember when its outcome demanded Apply, and its fix | `A3-1`–`A3-6` |
| **IV — What Goes Wrong** | The chapter's own failure table (symptoms of under-tested outcomes) and the bridge to Chapter 6 (export to an LMS) | `A4-1`–`A4-6` |

## 3. Sourcing and fact-check method

Per `FACTCHECK.md`, every claim down to specific figures (the ~61%/~40%
delayed-test result, the four academic citations) was checked
verbatim or near-verbatim against the chapter's own text and its own
footnotes — no claim was sourced independently of what the chapter
itself cites. The one honesty note carried through explicitly: the
chapter's own draft note states the single-question
generation-and-audit is real and live, while a full batch run across
every chapter was not executed in the chapter's own drafting session —
this video presents the worked example exactly as the chapter frames
it, a real single-item demonstration, not a claim that a full quiz
suite was generated.

## 4. The archival imagery — used as metaphor, not evidence

| Beat | Image | Stands in for |
|---|---|---|
| A1-1 | Students taking a computerized exam | the testing moment itself |
| A1-4 | Vintage pocket watch | spaced, distributed study over time |
| A2-1 | The Monument, London — spiral staircase | ascending levels (Bloom's taxonomy) |
| A3-1 | Vintage pocket watch display | precision — one level, checked exactly |
| A4-1 | Railway crossing warning sign | a warning signal for what can go wrong |

All 5 are real Wikimedia Commons photographs (CC-licensed), sourced and
sidecar'd per image.

## 5. A finding from this report's own review: the outro handle bug predates its fix

While preparing this report, I checked the master's qc-sheet directly
and confirmed the outro title card renders **`@NikBearBrown`**, not
`@DivyankSingh` — despite the beat sheet's own JSON correctly specifying
`"handle": "@DivyankSingh"`. This build was compiled on 2026-09-21, which
predates a toolkit bug found and fixed later in the session (during the
FastAPI vs gRPC build, 2026-10-04): `ClaudeTitleOutro`/
`ClaudeTitleOutro916` originally hardcoded the outro handle to
`@NikBearBrown` with no prop able to override it, so any beat sheet's
`handle` field was silently ignored at render time. The fix added an
optional `handle` prop to both components; builds made before that fix
— this one, plus the earlier llm-as-a-judge, chapter-4, and
vector-databases builds — were never revisited to apply it. The Short's
derived silent end card carries the same issue (`@nikbearbrown`,
confirmed directly in its `beat_sheet.json`). Everything else in both
cuts (composer `folderLabel`, handoff card, spoken narration) correctly
says Divyank throughout. Fixing this would require re-rendering and
recompiling just the `BOUT` beat (master) and the `BOUT`/`END` beats
(Short) — not a rebuild from scratch — but was not done as part of
generating this report; let me know if you'd like it corrected.

## 6. Building the two aspect ratios

Signed for Divyank from authoring time (`@DivyankSingh`, "in for
Divyank" throughout the spoken narration and composer cards). Portrait
coverage was planned into the beat sheet up front: one
`BinaryBranch`/`DivergentFates` hero beat per act (`A1-5`, `A2-4`,
`A3-3`, `A4-3`), specifically to avoid the post-hoc drop-list retrofit
needed on earlier builds this session.

## 7. Known limitations

- **No frame-level Visual QC** was run on either cut (`ART_QC=0`, this
  session's standing agreement).
- **The outro handle bug (§5) was not fixed as part of this report.**
- **Neither video is published or authorized for publication.**
