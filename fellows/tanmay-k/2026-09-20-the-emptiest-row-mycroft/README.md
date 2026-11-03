# The Emptiest Row

Tanmay Kulkarni, in for Humanitarians AI · Week 23 work video · built 2026-09-20

Text and code only. **The two masters live in the shared Google Drive**, not in this
repository — see the links below. The working folder, the reference implementation and
the full build record are outside this repo.

---

## Watch

| Cut | Aspect | Link |
|---|---|---|
| **Long** | 16:9 | <!-- VIDEO_LINK_LONG --> [Watch on Drive](https://drive.google.com/file/d/1xoEjju1P0Y96lUTL8wFtmgeXfpp6RI5I/view?usp=drive_link) |
| **Short** | 9:16 | <!-- VIDEO_LINK_SHORT --> [Watch on Drive](https://drive.google.com/file/d/1Jq7BlPN5IXq32ElPiWzMwC8XoV28MRMZ/view?usp=drive_link) |

## The two cuts

| File | Aspect | Resolution | Runtime | Loudness |
|---|---|---|---|---|
| `the-emptiest-row.mp4` | 16:9 | 3840 × 2160 | **5:19.8** | −24.2 LUFS / −2.81 dBTP |
| `the-emptiest-row-short.mp4` | 9:16 | 2160 × 3840 | **1:24.9** | −24.63 LUFS / −2.96 dBTP |

Both carry one lossy audio generation: narration is normalised on PCM before a single
AAC encode. Crest factor 11.04 and 11.38 against ~10.4 in the source narration.

**Title as published:** *The Emptiest Row* — locked as final, 2026-09-22.

**Source:** `13-lloyds-banking-group-agentic-ai-retail-banking-CASE-STUDY.md` and its
companion reference implementation, `lloyds_financial_assistant_pipeline.zip`.

## What the film argues

Lloyds Banking Group discloses four of its own AI systems across the same set of public
documents. Most coverage treats that as one company doing AI. This film refuses to
average them — it scores all four on the same two axes (is the mechanism disclosed, does
a human check the answer before a customer hears it) and finds a pattern no single
write-up would show: the system with the least disclosed mechanism and the least
disclosed outcome is also the only one of the four answering a customer directly, with
nobody checking first.

The second half builds a tested reference implementation around exactly that system, and
shows what a deliberate adversarial-testing pass actually catches: not a crash, but a
confident, wrong answer to a customer's question that a clean 29-for-29 test run never
would have found.

**The angle was checked against every prior work video in this fellow's run before
building** — deliberately not a fourth repeat of the "authorization gate ships with zero
default criteria" thesis already used at Lemonade, Zurich, and Capital One (Weeks 21–22
of this same run). See `ANGLE.md` for the full survey, including two angles ruled out and
why.

## The record

| File | What it is |
|---|---|
| `ANGLE.md` | Why this angle — a cross-system disclosure matrix, checked against every prior work video before building |
| `FACTCHECK.md` | Claims split in two: about Lloyds, resolved to primary sources; about the build, verified by running the code |
| `PEDAGOGY.md` | The signed Gate P record for the long — two drafts, a full read plus a scoped re-read of one beat after a PROOF-flagged fix |
| `PEDAGOGY-SHORT.md` | The Short's own signed Gate P record — a full independent read-aloud, not reused from the long |
| `PROOF-REVIEW.md` | Four reviews: script-stage, a toolkit incident found and fixed, a frame-level pass on the delivered file, and a final joint sign-off with the Short |
| `PROOF-REVIEW-SHORT.md` | The Short's own three reviews, including the one continuity seam found and fixed before Gate P |
| `READ-ALOUD.md` | The sheet Gate P was performed against for the long |
| `READ-ALOUD-SHORT.md` | The sheet Gate P was performed against for the Short |
| `beat_sheet.json` | 17 beats. Source of truth; measured Kokoro audio is the clock |
| `beat_sheet-short.json` | 5 beats, hand-authored fresh — not spliced from the long |

## Notes worth keeping

**Narration is Kokoro, run locally. Total spend $0.00.**

**A real toolkit incident, not silently worked around.** The shared `compile.py` was
tried first for the long. On its first run, finding nothing in the slot it checks, it
silently generated its own placeholder videos into its own scratch directory. A
directory-fix step taken immediately after unknowingly propagated those placeholders
into the real asset folder, and the review cut and its visual-QC check both unknowingly
graded the placeholders, not the film. Caught by extracting and looking at actual frames
rather than trusting the compile log. Root-caused, all clips re-rendered and
independently re-verified before compiling. Full account in `PROOF-REVIEW.md`.

**The Short is a fresh, hand-authored script, not spliced beats.** After this week's
topic-video Short first shipped with two reused segments and read as scattered, this
Short was written from scratch as one continuous argument. Its own PROOF review
specifically checked beat-to-beat continuity (not just per-beat legibility) and found and
fixed one real seam — a generic backreference with no lexical tie to the sentence before
it — before Gate P, not after.
