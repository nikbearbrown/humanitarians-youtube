# What Had to Be Invented

Tanmay Kulkarni, in for Humanitarians AI · Week 22 work video · built 2026-09-13

Text and code only. **The two masters live in the shared Google Drive**, not in this
repository — see the links below. Re-uploaded 2026-09-14 after a fix that removed beat
identifiers from the frames; any earlier copy of these links is superseded. The working folder, the reference implementation and the
full build record are outside this repo.

---

## Watch

| Cut | Aspect | Link |
|---|---|---|
| **Long** | 16:9 | <!-- VIDEO_LINK_LONG --> [Watch on Drive](https://drive.google.com/file/d/1_y4cirbvzjSiWbWvRHWrByVf3RCd0Om5/view?usp=drive_link) |
| **Short** | 9:16 | <!-- VIDEO_LINK_SHORT --> [Watch on Drive](https://drive.google.com/file/d/1I_zS37uE34p2vunGWMmXBY5Y20h8imOm/view?usp=drive_link) |

## The two cuts

| File | Aspect | Resolution | Runtime | Loudness |
|---|---|---|---|---|
| `2026-09-14-what-had-to-be-invented.mp4` | 16:9 | 3840 × 2160 | **4:42.5** | −16.2 LUFS / −1.96 dBTP |
| `2026-09-14-what-had-to-be-invented-short.mp4` | 9:16 | 2160 × 3840 | **1:37.0** | −16.2 LUFS / −1.98 dBTP |

Both carry one lossy audio generation: narration is normalised on PCM before a single AAC
encode. Crest factor 4.79 and 4.96 against ~10.4 in the source narration.

## What the film argues

The subject is a reference implementation of Capital One's Chat Concierge — intake, plan,
validation gate, explain, hand off — built using **only what Capital One has published**.

To make any stage of a system actually run you have to answer questions the public record
does not answer, and there are three honest moves: **confirm** it when a source states it,
**construct** it and say so in the file, or **refuse** and leave the hole exactly where the
evidence stopped. The film walks five stages and shows which of the three each one took.

**Marked absences in that implementation are documented boundaries, not defects.** Where the
public record stops, the code stops and says so — 7 `CONFIRMED`, 10 `CONSTRUCTED` and 15
`[DEV]` markers across eight source files, plus an eleven-entry decision log tying each
choice to the review pass that settled it. That discipline is the subject, and anyone editing
these files later should keep that framing.

The final beat names the framework's own limit: Capital One published the evaluator-to-planner
correction loop, and it fits none of the three moves, because the record speaks and this build
is simply not the place to implement it. A scope line, not a missing piece.

## The record

| File | What it is |
|---|---|
| `FACTCHECK.md` | Claims split in two — those about the build, verified by running the code, and those about Capital One, resolved to primary sources |
| `PEDAGOGY.md` | The signed Gate P record. Read aloud against the slates and signed 09/13/2026 |
| `PROOF-REVIEW.md` | Three reviews. Review 1 found the framework growing a fourth category it never named; review 3 is the first with a master, so the first where the production gate could be scored |
| `PROOF-REVIEW-SHORT.md` | The Short reviewed as a trailer, including a silent beat added so the viewer answers before the film does |
| `ANGLE.md` | Why this angle — **including the first angle I proposed and why it was wrong.** It read a documented design contract as an accident. The correction is kept rather than quietly replaced |
| `READ-ALOUD.md` | The sheet Gate P was performed against |
| `beat_sheet.json` | 16 beats. Source of truth; measured Kokoro audio is the clock |
| `beat_sheet-short.json` | 7 beats, reusing the parent's narration with two recorded trims and one silent card |

## Notes worth keeping

**Narration is Kokoro, run locally. Total spend $0.00.**

Two documentation corrections were found while fact-checking and applied to the reference
implementation's README: an officer title the case study had itself flagged as outstanding
(Milind Naphade is SVP, Technology, AI Foundations — not Chief AI Officer), and a stale test
count (32 tests, not 27; all passing).

Three findings from the case study were deliberately **not** used. Both reported "55%"
figures are self-reported and unaudited, and the number-collision angle would have duplicated
Week 21's topic video. The four-agent breakdown is a secondary-source specification, not
Capital One's own stated architecture.
