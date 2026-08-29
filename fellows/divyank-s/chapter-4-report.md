# Report: Claude, Rewritten. — Chapter 4, Two Cuts

**Source chapter:** `ai1-cli/chapters/04-rewrite-a-chapter-in-another-voice.md`
**Skill:** `deep-explainer` (brutalist.art toolkit)
**Location:** `humanitarians-youtube/chapter-4/`
**Cost:** $0.00 (Kokoro TTS, local Remotion rendering, no API keys)

## 1. Deliverables

| | 16:9 master | 9:16 Short |
|---|---|---|
| **File** | `claude-liam-rewrite-a-chapter-in-another-voice.mp4` | `short/claude-liam-rewrite-a-chapter-in-another-voice-short.mp4` |
| **Resolution** | 3840×2160 (4K UHD) | 2160×3840 (4K UHD, vertical) |
| **Duration** | 391.5s (6:31.5) | 162.99s (2:43.0) |
| **File size** | 103.7 MB | 68.6 MB |
| **Beats** | 32 | 13 |
| **Gate** | `PEDAGOGY.md` — `VERDICT: PASS` | `short/PEDAGOGY.md` — `VERDICT: PASS` (covers the one new line, the rewritten outro) |

Both are real, rendered, playable files. Neither is published or
authorized for publication.

## 2. What the master covers, act by act

The chapter's own structure (voice mechanism → the exercise → the worked
example → what goes wrong) maps directly onto 4 acts:

- **Act I — A Voice Is a File, Not a Vibe.** A voice is a specification —
  `voices/<voice>/VOICE.md`, a conversion contract naming what survives a
  rewrite untouched and what transforms — never a prompt. All seven
  shipped voices are named with their one-line register (Wonder, Generic,
  Socratic, Sardonic, Narrative, Pragmatist, Teardown), and the act closes
  on picking two that genuinely disagree (`A1-5`, `BinaryBranch`:
  Socratic vs. Pragmatist as the example pair).
- **Act II — Diff the Change, Not the Charm.** The chapter's central
  discipline: reading a rewrite and nodding is taste; diffing it against
  the original is evidence (`A2-2`, `DivergentFates`). Every marked change
  is judged better/worse/neutral **for the reader your Blueprint named**,
  never in the abstract — illustrated with the chapter's own example of a
  deleted definition being worse for a reference-seeker and better for a
  concept-builder (`A2-5`, `BinaryBranch`).
- **Act III — The Verdict Needs Quotes.** Built entirely from the
  chapter's real, verbatim worked example: one sentence — *"A finished
  book, in this system, is not a Word document you email around"* —
  rewritten into real Socratic and real Pragmatist passages, quoted
  exactly as the chapter gives them (`A3-3`, `DivergentFates`), then the
  chapter's own diff-level judgment and final verdict ("lead Socratic,
  land Pragmatist").
- **Act IV — What Goes Wrong.** The chapter's own four-row failure table
  (agent edits `chapters/` directly; "liked it" instead of diffing; a
  verdict with no quotes; two voices that don't actually fight), the
  "unfalsifiable" argument for why quotes are mandatory (`A4-3`,
  `BinaryBranch`), and the chapter's own bridge line to Chapter 5.

## 3. Sourcing and fact-check method

Unlike the `llm-as-a-judge` build, this reel has a single, fully-read
source document. Every claim in `FACTCHECK.md` is checked line-by-line
against `chapters/04-rewrite-a-chapter-in-another-voice.md`, including the
chapter's own honesty caveat (line 86): the Socratic/Pragmatist worked
example is explicitly flagged by the chapter itself as an illustrative
single-sentence demonstration, not a full-chapter rewrite — the reel
repeats that framing rather than overstating what was actually run.

## 4. The archival imagery — no Smithsonian, used honestly as metaphor

Per this build's explicit instruction, **no Smithsonian images** were
used (all 5 sourced via the Wikimedia Commons API instead, as with every
prior build this session, since Smithsonian's own search page returns
`HTTP 403` to non-browser fetches anyway). None depict the AI1 CLI
exercise literally — each stands in for a concept:

| Beat | Image | Stands in for | License |
|---|---|---|---|
| A1-1 | Comedy/Tragedy masks, Suisun Harbor Theater | many registers, one book | CC BY-SA 4.0 |
| A2-1 | Crossroads and Signpost, Dalgety Bay | choosing two voices that fight | CC BY-SA 2.0 |
| A2-3 | Example of copyedited manuscript | the diff as evidence | CC BY-SA 3.0 |
| A3-1 | WTBBL magnifier | quoting the exact passage | CC BY-SA 3.0 |
| A4-1 | Patchway station warning signs | what goes wrong | CC BY-SA 4.0 |

## 5. Building the two aspect ratios — the lesson from the last build, applied

Unlike the `llm-as-a-judge` build (where the need for 9:16-compatible
components was discovered only after the fact), this beat sheet assigned
`BinaryBranch`/`DivergentFates` — the two components with real,
resolution-agnostic 916 coverage — to one hero mechanism beat per act
**from the start** (`A1-5`, `A2-2`, `A2-5`, `A3-3`, `A4-3`; see
`BUILD-LOG.md`).

That planning helped, but did not fully solve the derivation on its own:
`shorts.py`'s auto cap-check plans drops by duration alone, with no
awareness of which beats have portrait support. Its first proposal
dropped 14 beats but **still landed over the 3:00 cap**, and in doing so
cut 3 of the 5 pre-planned hero beats (the longest ones) while keeping
several shorter, portrait-*unsupported* `ChipGrid`/`FluencySegmentCard`
beats. The plan was manually overridden (`shorts.py --drop <20 explicit
beat IDs>`) to keep exactly the beats with real 916 rendering: the cold
open, one VOX still per act, all 5 mechanism beats, the handoff, and the
outro — 13 beats, 163.0s, zero `ONDA CHECK` blocks.

The same auto-rewritten-outro bug from the last build recurred
identically (raw narration fragments stitched into a broken sentence) and
was hand-fixed the same way before its audio was generated — see
`short/PEDAGOGY.md`.

## 6. Known limitations

- **No frame-level Visual QC** was run on either cut (`ART_QC=0`, this
  session's standing agreement) — both compile and play back correctly
  but have not had a 9-point-rubric frame inspection.
- **`shorts.py`'s auto-planner has no concept of portrait-composition
  support** — pre-assigning hero beats to 916-capable patterns reduces but
  does not eliminate the need for a manual `--drop` override; the
  auto-proposed plan should be treated as a starting point to review, not
  a plan to run unmodified, until the script itself accounts for this.
- **Neither video is published or authorized for publication.**
