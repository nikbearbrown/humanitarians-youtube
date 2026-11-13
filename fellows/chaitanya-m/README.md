# Chaitanya M.

**Role:** AI Software Engineer  
**Project:** Medhavi Hub — subsystem research reels  
**GitHub:** [@malepatic](https://github.com/malepatic)

Humanitarians AI fellow. Research-log teardowns of the **Medhavi** hub
(`medhavi-hub`): I audit one subsystem, verify every number against the source,
and document what I find — including when the finding is that something built
correctly is going unused. Video projects live in one dated lowercase-kebab
folder per reel, `YYYY-MM-DD-slug/`.

**Renders:** [Google Drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v)
**Renewal:** [RENEWAL.md](RENEWAL.md) · **Hours:** [HOURS.md](HOURS.md)
— masters, narration and beat clips. Source, beat sheets, scripts, subtitles,
build inputs and checks stay here in git, per `fellows/README.md`.

## Voice choice

**Series voice:** Bella (`af_bella`) — the `hai` persona.
**Register:** Pragmatist — method, when to use it, when not to.

Recorded as `metadata.voice_kokoro` in every beat sheet. Kept across the series
unless another explicit, documented re-voice decision is made.

### Re-voice decision — 2026-09-17

The series opened on Onyx (`am_onyx`). It is now **Bella (`af_bella`)**, decided
deliberately and recorded here, which is what `fellows/README.md` requires of a
voice change.

| | |
|---|---|
| **Was** | Onyx (`am_onyx`), locked at the first reel (2026-08-28, Concept Map) |
| **Now** | Bella (`af_bella`), from the second reel (2026-09-13, Memory API) onward |
| **Reason** | Bella is the voice the repo documents as the `hai` persona, and it is one of only two Kokoro voices the installed toolkit ships. Settled at episode two rather than left to accumulate |

**Consequence:** [What Is a Concept Map](2026-08-28-what-is-a-concept-map/) is
now the outlier — it is `am_onyx` and stays that way on disk. Re-voicing it is
optional and cheap in effort but not free: audio is the clock, so new narration
changes every beat duration and forces a re-cut of both masters. Worth doing if
the series is ever published as a set; not worth blocking on otherwise.

## House style

Two formats so far, and the series has moved from one to the other:

| Reel | Format | Brand | Palette | Type |
|---|---|---|---|---|
| Concept Map | Brutalist | `brutalist-script` | `#0A0A0A` / `#F2F0EB` / `#E8452C` / `#6B6B6B` | Helvetica Neue Bold + Menlo |
| Memory API | Brutalist | `brutalist-deck` | `#000` / `#fff` / `#FFE500` / `#FF3B00` | Archivo Black + IBM Plex Mono |
| Who Can Open What | `ai-explainer` | `claude` | Claude fidelity | house |
| Lookup, Not Training | `ai-explainer` | `claude` | Claude fidelity | house |
| The Logout That Didn't | `ai-explainer` | `claude` | Claude fidelity | house |
| One Sign-In, Many Books | `ai-explainer` | `claude` | Claude fidelity | house |

**The first two reels are Brutalist and deliberately not Claude-branded** — no
`ClaudeComposerAsk` cold open, no verdict page, no HANDOFF beat, no channel bug,
and the Claude fidelity palette unused. Each took its visual identity from the
artifact it documented, so their palettes differ from each other too. Every
departure from `ai-explainer` frame law is enumerated in that reel's
`BUILD-LOG.md`.

**From 2026-09-17 the reels are `ai-explainer`s with the spine intact** — cold
open → body → verdict page → handoff → outro, on the Claude fidelity palette and
the `@HumanitariansAI` channel. That is the current default; the Brutalist pair
stands as built and is not being retrofitted.

Visuals are always produced **out-of-tree** and dropped into per-beat slots, so
the brutalist toolkit stays **read-only** — used only for Kokoro narration,
conform/mux, and the 9:16 derivation. The renderer differs per reel: a
deterministic Pillow script, headless Chrome capturing a real deck, or the
toolkit's own scene components.

Where a 9:16 cut exists, its portrait frames are committed under `pantry/` as
build inputs. `shorts.py`'s default centre-cut keeps ~1200px of a 3840px frame
and destroys any two-column layout, so the overrides are what make the vertical
cut reproducible rather than an accident.

## Reports

| Date | Title | Subject | Runtime | Status |
|---|---|---|---|---|
| 2026-10-15 | [The Logout That Didn't](2026-10-15-the-logout-that-didnt/) | Postmortem — the Logout button that logged nobody out in production, and the HttpOnly cookie on another domain that explains it | 3:53 | Built · QC'd · fact-checked · GATE P signed · not published |
| 2026-10-01 | [Lookup, Not Training](2026-10-01-lookup-not-training/) | How the AI tutor knows the textbook — nothing is trained; it searches the book at question time and answers from the passages it was handed | 3:27 | Built · QC'd · fact-checked · GATE P signed · not published |
| 2026-09-21 | [One Sign-In, Many Books](2026-09-21-one-sign-in-many-books/) | How a separate textbook site lets you in without knowing you — the signed ticket, the call back to the hub, and the one logout timestamp that retires every ticket | 3:28 | Built · QC'd · GATE P signed · not published |
| 2026-09-17 | [Who Can Open What](2026-09-17-who-can-open-what/) | Hub access — the three kinds of permission, the two ways in, and what the model implies | 3:48 | Built · QC'd · GATE P signed · not published |
| 2026-09-13 | [Memory API](2026-09-13-memory-api/) | Cross-book learner memory — two tables, the `memory_subject` convention, and the fact that no textbook calls it yet | 2:51 | Built · fact-checked · GATE P signed · not published |
| 2026-08-28 | [What Is a Concept Map](2026-08-28-what-is-a-concept-map/) | Concept Map subsystem audit — schema, S3 layer, review gate, and the verified output's zero consumers | 3:49 | Built · QC'd · fact-checked · GATE P signed · not published |

GATE P is signed on all six reels. That signature covers the **narration** — it
is not a QC sign-off and not a fact-check sign-off; each reel's README lists what
remains open.

The first two reels landed the same finding from opposite ends of the hub: the
machinery is built and correct, and nothing downstream consumes it. The Concept
Map's verified output has zero readers; the Memory API has zero callers. The
2026-09-17 and 2026-09-21 reels turn to access, which *is* wired — so the
pattern is worth naming but is not universal.

## Media policy

Per `fellows/README.md` (rule of 2026-09-18): **renders go to Drive, build
inputs and source stay here**, excluded by location rather than file type.

- **Drive** — [renders folder](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v):
  masters, generated narration (`mp3/`, `audio/`), beat clips (`media/`,
  `clips/`), review cuts.
- **Git** — beat sheets, scripts, subtitles (`.srt`, `words.json`), renderers,
  prompts, checks, QC reports and contact sheets, and the assets used to *build*
  the video: `pantry/` portrait overrides, source decks, fixtures. All well
  under GitHub's 100 MB cap.

Two deliberate details. `pantry/` **is** committed — those portrait frames are
build inputs, and without them the 9:16 cuts are not reproducible from this
repo. And `timings.json` sits at each reel's root rather than in `mp3/`: `mp3/`
is an excluded *location*, and git will not descend into an excluded directory,
so a file left there would be silently dropped.

Rebuild with the free local toolkit
([brutalist.art](https://github.com/nikbearbrown/brutalist.art)).

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
