# Same Room, Different Argument

Tanmay Kulkarni, in for Humanitarians AI · Week 23 topic video · built 2026-09-20

Text and code only. **The two masters live in the shared Google Drive**, not in this
repository — see the links below. The working folder and the full build record are
outside this repo.

---

## Watch

| Cut | Aspect | Link |
|---|---|---|
| **Long** | 16:9 | <!-- VIDEO_LINK_LONG --> [Watch on Drive](https://drive.google.com/file/d/1RYRtIXfmmQI06_SrlplkmoN_CahKzOpB/view?usp=drive_link) |
| **Short** | 9:16 | <!-- VIDEO_LINK_SHORT --> [Watch on Drive](https://drive.google.com/file/d/18IMZUvb5kfu5o3dJLZQIEeSijNEwqXkH/view?usp=drive_link) |

## The two cuts

| File | Aspect | Resolution | Runtime | Loudness |
|---|---|---|---|---|
| `same-room-different-argument-final.mp4` | 16:9 | 3840 × 2160 | **5:46.4** | −24.86 LUFS / −3.39 dBTP |
| `same-room-different-argument-short-final.mp4` | 9:16 | 2160 × 3840 | **1:27.3** | −24.93 LUFS / −5.22 dBTP |

Both carry one lossy audio generation: narration is normalised on PCM before a single
AAC encode.

**Title as published:** *Same Room, Different Argument* — locked as final, 2026-09-22.

**Topic drawn from:** `claude-for-computer-science/chinese-room-explainer-vox` — the
existing 8-beat cut there is marked never publish and was superseded by this lineage
structure, not reused. See `TOPIC-DECISION.md`.

## What the film argues

Four names, four decades apart: Searle (1980), Harnad (1990), Bender & Koller (2020),
and Bender with three co-authors (2021). The popular retelling says it's one argument,
handed down and aimed at a new target each time. This film runs one checklist on all
four — what does the argument specifically claim to prove, does it name and answer the
one before it, and has the original author ever had to correct how it gets used — and
finds that the tidy version is the part nobody actually checked.

A game sits in the middle: two unlabeled questions, one from Searle, one from Bender and
Koller. The viewer gets a few seconds to guess which is which before the reveal names
the actual difference between them — not the difference the popular retelling assumes.

The closing beat restates the checklist as something a viewer can run on any claim that
says "this is really just [an older argument] again."

## The record

| File | What it is |
|---|---|
| `FACTCHECK.md` | Four legs (Searle 1980, Harnad 1990, Bender & Koller 2020, Bender et al. 2021), every claim leveled primary-read / citing-source / search-summary, plus a rejected-claims table |
| `BEATS-DRAFT.md` | Structural reasoning and the beat-to-FACTCHECK sourcing map, plus the draft 1→4 revision history that took the production gate from 9/12 to 12/12 |
| `PEDAGOGY.md` | The signed Gate P record. Read aloud and signed by Tanmay Kulkarni, 2026-09-20 |
| `PROOF-REVIEW.md` | Twelve reviews, ending in a joint sign-off covering both formats together |
| `SHORTS-BUILD-LOG.md` | The Short's own build history (toolkit gaps found and fixed), its own PROOF review, and its final Trailer Gate score |
| `TOPIC-DECISION.md` | The randomized draw, the uniqueness sweep across every other fellow's branch, and the correction made after fact-checking narrowed the angle |
| `READ-ALOUD.md` | The sheet Gate P was performed against |
| `beat_sheet.json` | 18 beats. Source of truth; measured Kokoro audio is the clock |
| `beat_sheet-short.json` | 6 beats, the Short's own structure |

## Notes worth keeping

**Narration is Kokoro, run locally. Total spend $0.00.**

One sourced photograph appears in the film (Searle, Oxford, 2005): Wikimedia Commons, CC
BY-SA 3.0 / GFDL, attribution required before publish (photographer: Matthew Breindel).
Every other visual beat is code-rendered.

A misquote was caught before Gate P signed off: an early draft dropped "haphazardly"
from Bender et al.'s own sentence and silently substituted Margaret Mitchell's real name
for her published pseudonym (Shmargaret Shmitchell) with no acknowledgment. Both fixed —
the quote restored verbatim, and the narration names both the real person and her
published byline.

The Short is a hand-written trailer, not a summary — its own intro and outro were
rewritten twice on direct feedback (name landing too late; the guess/reveal feeling
disconnected from the bigger argument; 71.2s undersold the film) before the guess/reveal
and the Harnad irony beat earned their place as the two turns actually shown.
