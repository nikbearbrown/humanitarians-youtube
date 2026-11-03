# The Stages That Stayed Dark

Tanmay Kulkarni, in for Humanitarians AI · Week 21 work video · built 2026-09-03

Text and code only. **The two masters live in the shared Google Drive**, not in this
repository — see the links below. The working folder and the full build record are outside
this repo.

---

## Watch

| Cut | Aspect | Link |
|---|---|---|
| **Long** | 16:9 | <!-- VIDEO_LINK_LONG --> [Watch on Drive](https://drive.google.com/file/d/1od-c7KrKpFPcRlft3pWUMroG_nCe83b5/view?usp=drive_link) |
| **Short** | 9:16 | <!-- VIDEO_LINK_SHORT --> [Watch on Drive](https://drive.google.com/file/d/1RgIB0bOxSX3cRpwmW_57FEgwESiIrTMx/view?usp=drive_link) |

## The two cuts

| File | Aspect | Resolution | Runtime | Loudness |
|---|---|---|---|---|
| `2026-09-03-the-stages-that-stayed-dark.mp4` | 16:9 | 3840 × 2160 | **4:25.5** | −14.8 LUFS / −1.4 dBFS |
| `2026-09-03-the-stages-that-stayed-dark-short.mp4` | 9:16 | 2160 × 3840 | **2:37.2** | −14.8 LUFS / −1.3 dBFS |

Both are clean masters. Voice is Kokoro `am_onyx`, matching the topic video released the same
week — both films name the same presenter aloud, so they carry the same timbre.

**A note on that choice, because it was nearly got wrong.** The first draft specified
`af_bella` on the strength of Week 19's `SCRIPT.md` header. Week 19's `beat_sheet.json` — the
file that actually generated its audio — says `am_onyx`. The document and the artifact
disagreed, and the document was the one I copied.

## What it teaches

Move one line in a claims pipeline and **27 of its 28 tests still pass.**

The reference implementation is a five-stage pipeline — intake, extraction, coverage check,
authorization gate, resolve. Break it as gently as possible: one line moved up four positions,
so the coverage check runs before the extraction halt is honoured. Same claim in, **byte-identical
output** — same status, same reason, same detail string. Every assertion about what came out
still passes.

What changed is that the broken pipeline fetched a customer's policy record, for a claim that
should have stopped a stage earlier. In a claims system, looking up someone's policy is not
free and it is not invisible. It is an event.

One test catches it: not an assertion about the output, but an assertion about what was
**never called**.

There are eight of those in the suite, and they are not eight arbitrary tests. An incomplete
intake proves three stages never ran; low confidence proves two; a missing policy proves one.
**3 + 2 + 1 + 2 = 8** — the eight assertions are the four shadows, summed. The further a claim
travels, the smaller the shadow behind it, and the assertion shrinks to match, because the
assertion is a description of the shadow.

The method: **for every condition that stops your pipeline early, name the stage that must not
run, and write the line that fails if it does.**

## Why this angle, and the two that were withdrawn

Two earlier angles were dropped for repeating a prior episode's *thesis* rather than its shape:

- **The empty authorization gate** — this is Week 19's film near-verbatim. Its own gate reads
  *"never putting a construction where a judgement belongs… can this run without a human
  answering?"* The Zurich build's docstring even cites the lineage.
- **The two same-named Claras** — a genuine and verified trap, but "two things that look like
  one" is Week 18's teachable claim *and* Week 20's. A third use would be a pattern.

Both survive in `FACTCHECK.md` as verified findings deliberately kept out of the narration.

## The positive frame, and why it is not a story about thin disclosure

Zurich confirms exactly one thing about how Clara behaves: it keeps *"a transparent and
auditable trail of the reasoning behind decisions."*

The broken build's trail would be **accurate** — it really did fetch that record. The trail is
honest and the behaviour is wrong. **An auditable trail records what happened; it cannot tell
you that what happened should not have.**

So the negative assertions are not a defensive response to a thin public record. They are the
technique that protects the one property Zurich actually claimed. The film builds toward what
was confirmed rather than around what was not.

## What it claims, and what it does not

**Thirteen claims, twelve of them executable.** `verify_claims.py` produces them rather than
asserting them — including the broken pipeline itself, so the centrepiece is reproducible.

**One claim about Zurich, and only one:** that its published description of Clara contains the
auditable-trail sentence. Everything else is about this repository's own code.

**The technique's limit is stated on screen.** On the happy path, the broken build and the
correct build fetch the same record in the same order and no assertion in the suite can tell
them apart. Eight assertions do not cover a system, and a film about proving a negative that
never stated its own limit would be doing the thing it warns against.

**A near-miss recorded rather than quietly fixed.** The first version of the verification
harness held its own module references, so the tests' patches never reached the broken code and
it reported **0 failures** — a false all-clear that read exactly like success, on a film about
tests failing open. `FACTCHECK.md` carries it as an addendum.

## What was checked in the case study, not assumed

The case study claims *"28 tests across seven modules, run in full."* Counted: **28**. Run:
**28/28 pass.** The count and the pass rate hold exactly.

One phrase is loose — there are seven *source* modules but **six** test files; `mock_data.py`
is fixtures. Recorded because loose phrasing is where the next error gets in, which is the
sibling film's entire subject.

Practical note for anyone cloning the reference implementation: the suite is stdlib
`unittest`, **not pytest**. Run it per file, or you will conclude it is broken.

## Files here

**The six core files**, the same set every episode in this series carries:

| | |
|---|---|
| `README.md` | this file |
| `PEDAGOGY.md` | Gate P, signed 2026-09-03, no revisions |
| `FACTCHECK.md` | 13 claims, plus six verified findings deliberately kept out of the film |
| `QC-REPORT.md` | deliverable specs, loudness, resolution, gates — all measured |
| `beat_sheet.json` | the source of truth for the long cut |
| `beat_sheet-short.json` | the source of truth for the Short |
| `VERIFY-RESULTS.txt` | the saved run that produced every number in the film |

**Why `verify_claims.py` is not here.** It imports the Zurich/Clara reference implementation,
which lives with the case study rather than in this repository, so it would not run from this
folder. A script that cannot run is worse than no script; the saved output is included instead
and labelled as evidence of record.

Not included here: the build scripts, the Manim scenes, the read-aloud sheet, the angle
documents and the intermediate reviews. Those live in the working folder — this folder is the
deliverable and its evidence, not the workshop.

Captions (`.srt`/`.vtt`) and the YouTube description are produced at build time and kept with
the masters in the shared Drive, per this collection's convention.
