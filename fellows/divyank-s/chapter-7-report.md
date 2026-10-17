# Report: Claude, Signed. — Chapter 7 (Facts: Check a Claim, Record It, Sign It), Two Cuts

**Topic:** AI1 CLI Chapter 7 — Facts (the `facts.json` claims database, the three constitutional rules, trace/add/sign/refuse, and the chapter's own real worked example)
**Skill:** `deep-explainer` (brutalist.art toolkit)
**Location:** `humanitarians-youtube/fellows/divyank-s/2026-10-04-chapter7/`
**Cost:** $0.00 (Kokoro TTS, local Remotion rendering, no API keys)

## 1. Deliverables

| | 16:9 master | 9:16 Short |
|---|---|---|
| **File** | `claude-liam-facts-checked-and-signed.mp4` | `short/claude-liam-facts-checked-and-signed-short.mp4` |
| **Resolution** | 3840×2160 (4K UHD) | 2160×3840 (4K UHD, vertical) |
| **Duration** | 339.61s (5:39.6) | 163.79s (2:43.8) — includes the full verdict beat |
| **Beats** | 32 | 12 |
| **Gate** | `PEDAGOGY.md` — `VERDICT: PASS` | derived from the signed-off parent; outro narration hand-rewritten and regenerated |
| **Signed** | "Liam, in for Divyank" / `@DivyankSingh` throughout, including the outro card and the Short's silent end card | same |

Both are real, rendered, playable files. Neither is published or authorized for publication.

## 2. Source and how it's covered

Source: `ai1-cli/chapters/07-facts-check-a-claim-record-it-sign-it.md`,
read in full and cross-checked against its matching research doc and the
live `ai1-cli/facts/facts.json` file. The chapter closes Part I of the
book, and its shape maps to 4 acts:

| Act | Content | Beats |
|---|---|---|
| **I — A Fact Is a Record, Not a Recollection** | *Mata v. Avianca* (2023, a real case — a lawyer fined for filing invented court citations), models as fluent liars, the `facts.json` schema and its human-only `verified` flag | `A1-1`–`A1-6` |
| **II — Three Rules, Straight From the Constitution** | Check `facts.json` before searching; new facts enter `verified: false`; verified facts are append-only, with consensus derived from evidence, never hand-set | `A2-1`–`A2-6` |
| **III — Trace, Add, Sign — and Refuse** | The three-step exercise, plus the chapter's real worked example (the actual Rosser Reeves USP entry recorded in the book's own `facts.json`), and the parallel to GATE 0/GATE 1's human-signature mechanism | `A3-1`–`A3-6` |
| **IV — What Can Go Wrong** | The chapter's own 4-row failure table (unsourced claims, signing without being sure, disagreeing sources, editing a verified fact), bridging to Part I's close | `A4-1`–`A4-6` |

## 3. Sourcing and fact-check method

Per `FACTCHECK.md`, the Mata v. Avianca case and the chapter's own
"three rules" and failure-table rows are tagged **Cited** (traced to the
chapter's footnote and its own text). One claim was verified more
directly than usual: the chapter asserts its worked example — the Rosser
Reeves Unique Selling Proposition fact — is a **real**, not illustrative,
entry in the book's own `facts.json`. This was checked by opening the
live `ai1-cli/facts/facts.json` file during this session and confirming
the "Rosser Reeves" canonical text appears verbatim, exactly as the
chapter prints it. No claim is made that this session actually ran
`facts.py lookup/record` or `verify.py sign` against the live repo — the
video narrates the chapter's method and its pre-existing real example,
not a fresh run performed this session.

## 4. The archival imagery — used as metaphor, not evidence

| Beat | Image | Stands in for |
|---|---|---|
| A1-1 | Courtroom One Gavel | a real court case's consequences, without depicting the specific case or any identifiable person |
| A1-4 | *How the Eagle Landed* — the Grumman Construction Log (Apollo LM-5 engineering log) | a written, timestamped, signed record kept over time |
| A2-1 | LOC Main Reading Room (Library of Congress) | checking an existing record before searching fresh |
| A3-1 | A woman reading a book with a magnifying glass (Wellcome Collection) | tracing a claim closely back to its source |
| A4-1 | Antique two-pan balance scale | weighing two disagreeing sources against each other |

All 5 are real Wikimedia Commons photographs (public domain or
CC-licensed), sourced and sidecar'd per image. One image was swapped
during QC: the first ledger photo sourced for A1-4 turned out, on full
review, to be a blank unfilled page — it was replaced with a genuine
handwritten, dated, and signed 1968 Apollo program engineering log before
the final render, which is a substantially stronger match for the "a
record, not a recollection" narration it illustrates.

## 5. Lessons carried forward from the Chapter 6 build

Two bugs surfaced during the Chapter 6 build (a silent master caused by
under-specified act-card beats, and a Short end-card handle that
silently ignored a JSON edit) were applied as fixes from the start here:
the four act-card beats shipped with real spoken narration and the
correct prop shape from first draft, and `shorts.py` was called with
`--handle @DivyankSingh` explicitly rather than discovering the default
afterward. Both held — the master compiled with `audio: per-beat
narration` on the first pass, and the Short's end card showed the
correct handle without a second compile.

## 6. Building the two aspect ratios

Signed for Divyank from the first draft throughout, including the outro
card. Portrait coverage was planned into the beat sheet up front: one
`BinaryBranch`/`DivergentFates` hero beat per act (`A1-5`, `A2-4`,
`A3-3`, `A4-3`). The manual Short plan needed two rounds of trimming — an
initial plan with two VOX stills in Act I plus the full verdict beat
landed at 191.3s, and a corrected one-VOX-per-act version still landed at
181.8s — both over the 3:00 cap — before dropping the Act IV VOX still
(`A4-1`) brought it to 171.9s. The recurring auto-rewritten-outro bug
(raw narration fragments stitched into a broken sentence) appeared again
and was hand-fixed before its audio was generated.

## 7. Known limitations

- **No frame-level Visual QC** was run on either cut (`ART_QC=0`, this
  session's standing agreement).
- **`shorts.py`'s auto-planner still has no concept of portrait-composition
  support or the verdict beat's outsized duration** — manual `--drop`
  iteration was needed before the Short fit the cap.
- **Neither video is published or authorized for publication.**
