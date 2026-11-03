# Where the Record Stops

Tanmay Kulkarni, in for Humanitarians AI · Week 19 work video · built 2026-08-25, filed 2026-08-23 with the week's topic video

Deliverables-only folder (PLAYBOOK §7). Working folder and extended build record are outside this repo.

---

## The two cuts

| File | Aspect | Resolution | Runtime |
|---|---|---|---|
| `2026-08-23-where-the-record-stops.mp4` | 16:9 | 3840 × 2160 | **4:47.9** |
| `2026-08-23-where-the-record-stops-short.mp4` | 9:16 | 2160 × 3840 | **1:41.2** |

Both are clean masters and both are paced — a hold sits before every cut so an idea lands
before the next one starts (0.60s default, **1.10s on the three code beats**, where the
viewer is reading a file rather than hearing a sentence).

**The Short is a trailer, not a shortened film.** Five beats plus a rewritten outro: the
hook, the framework, the empty gate, the refusal to guess, and a pointer to the long cut. It
never names DBS in narration, so it makes no claim about them; the non-claim rides on the
endcard instead. Every kept beat reuses the parent's audio unchanged.

## What it teaches

You build something from what a company published. Ten minutes in you hit the first thing
they didn't say. **That** is the job — not the building.

The method: every element of a build is one of three.

| | |
|---|---|
| **CONFIRMED** | the source actually said it |
| **CONSTRUCTED** | you invented it, because code has to run — and you labelled it |
| **BLANK** | you left it empty on purpose, and made it impossible to skip |

One rule holds it up: **never put a construction where a judgement goes.** And one test makes
it real: *can this run without a human answering?* If yes, you invented a judgement.

The worked example is a credit-memo pipeline built from DBS Bank's public disclosure. Its
Human Review Gate ships with no approval criteria at all — no confidence score, no threshold,
no rule — and raises rather than continuing when handed an answer it doesn't recognise. A
gate that shrugs when it's confused isn't a gate; that's **failing open**, and it's how
systems approve things nobody approved.

The film then does the harder thing: it admits the framework strains. The gate's reject path
fits no column cleanly — the *name* came from DBS's language, the *existence of the path*
came from a governance quote, and nothing DBS published ever walked through a rejection. That
gets rendered on screen as *"reasoned, never demonstrated"* rather than filed under
CONSTRUCTED and forgotten.

## This is not DBS's system

Stated in the first 45 seconds, on screen, quoted verbatim from the repository's own Explicit
Non-Claims — not as a closing disclaimer. The film is about **craft**, not about DBS's
disclosure practice. The only thing it observes DBS did not publish is internal
implementation detail, which is normal and expected of any bank.

DBS's own governance candour is presented as a credit to them, which is also how the source
case study reads it.

## Files

| File | What it is |
|---|---|
| `*.mp4` × 2 | the two masters |
| `beat_sheet.json` · `beat_sheet-short.json` | source of truth for each cut |
| `NARRATION.md` · `NARRATION-short.md` | verbatim transcripts |
| `SCRIPT.md` | beat-by-beat script, tone arc, PROOF gates at both phases |
| `FACTCHECK.md` | every spoken **and on-screen** claim, verdict, source |
| `QC-REPORT.md` | resolution chain, seven defects found and fixed, truncation and pacing |
| `PROOF-REVIEW.md` | both review rounds — what failed, what changed |
| `PEDAGOGY.md` | append-only build log and Gate P sign-off |
| `IDEAS.md` | the four angles considered, and why this one |
| `pacing_pass.py` | the post-compile hold pass — **re-run after ANY recompile** |
| `qc-sheet-*.png` | contact sheets, both aspects |

## Source material

- `../../09-dbs-agentic-ai-investment-commercial-banking-CASE-STUDY.md`
- `../../dbs_credit_memo/` — the reference implementation. Six modules, six test files,
  **all passing as run 2026-08-25** (verified, not taken from its README)

## Built with

Brutalist toolkit — Kokoro `am_onyx` for narration, Remotion for every beat, `compile.py` at
`--height 2160` / `3840`, `shorts.py` with an explicit drop plan, and `pacing_pass.py` for
the holds.

Four components were authored or extended for this film: `BuildLedger`, `StageRefinement`,
`ClaudeCodeBeat916`, and a `sourceNote` field on `BuildLedger` added after review 1. All live
in `brutalist.art/runtime/remotion/src/scenes/`.

## Status

Teaching **12/12** (ship bar 8). Production gate **PASS** in both aspects, re-run on rendered
frames after the punch list. Gate P signed in `PEDAGOGY.md`. Both cuts watched end to end.

**Not published** — publication is a separate decision.
