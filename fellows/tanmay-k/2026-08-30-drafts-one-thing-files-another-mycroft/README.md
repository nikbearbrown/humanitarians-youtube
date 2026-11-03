# Morgan Stanley's AI Drafts One Thing and Files Another

Tanmay Kulkarni, in for Humanitarians AI · Week 20 work video · built 2026-08-30

Text and code only. **The two masters live in the shared Google Drive**, not in this
repository — see the links below. The working folder and the full build record are outside
this repo.

---

## Watch

| Cut | Aspect | Link |
|---|---|---|
| **Long** | 16:9 | <!-- VIDEO_LINK_LONG --> [Watch on Drive](https://drive.google.com/file/d/1C9UT8y_49pTjqO7_pEqjXrbLBI8J8u6o/view?usp=sharing) |
| **Short** | 9:16 | <!-- VIDEO_LINK_SHORT --> [Watch on Drive](https://drive.google.com/file/d/1nA29WW_HEOSK-3n8xyL8h-DFWwWJwJy8/view?usp=sharing) |

## The two cuts

| File | Aspect | Resolution | Runtime | Loudness |
|---|---|---|---|---|
| `2026-08-30-drafts-one-thing-files-another.mp4` | 16:9 | 3840 × 2160 | **6:18.4** | −14.36 LUFS / −1.34 dBTP |
| `2026-08-30-drafts-one-thing-files-another-short.mp4` | 9:16 | 2160 × 3840 | **2:39.8** | −14.43 LUFS / −1.36 dBTP |

Both are clean masters. Voice is Kokoro `af_bella`, the standing choice for this series.

**The Short is a trailer, not a shortened film.** Six beats plus a rewritten outro: the source
sentence, the title card, the three-question check, what the review caught, the line that
prevents it, and a
pointer to the long. Every kept beat reuses the parent's audio unchanged; the outro is the only
regenerated narration, and it names what was cut rather than teasing it.

## What it teaches

Building from someone else's public description can fail three ways. You can invent something
the source doesn't say — easy to catch, you know you did it. You can drop something it does
say — also easy, missing things are findable. Or you can take **two things the source treats
differently and flatten them into one**. Nothing looks wrong afterwards.

The method is three questions, on a card, run on any build:

| | |
|---|---|
| **1** | What does the source treat as two different things? |
| **2** | Are they still two different things in the code? |
| **3** | Is there a line that fails if someone makes them one? |

The answer to the third is one assertion:

```python
assert result["email_status"] != result["salesforce_note_status"]
```

It checks neither value — other tests do that. It only asserts the two can never collapse into
one. That is the whole transferable idea: **when two things must stay different, assert that
they are different.**

## The worked example

Morgan Stanley's 26 June 2024 release describes what its meeting AI does after a client call
in one sentence with three parallel verbs — *summarizes*, *creates*, *saves* — and a ten-word
qualifier on exactly one of them: *"for an Advisor to edit and send at their discretion."*

The email waits for a person. The Salesforce note does not. That distinction is stated plainly
without being emphasised — and **a review pass against the source is what surfaced it**, after
an early version of the build had treated the two outputs alike. Catching it is the reason the
film has something to teach.

## The structure is A/A′, and that is deliberate

The film runs the same check **twice, on screen**. Pass one is Morgan Stanley's material and my
build of it. Pass two puts the identical card back, blank, and runs it on **this repository** —
where it finds something worth reporting: the forbidden-name guard checks for `write` on the
Debrief modules and not on the Assistant ones, while four of the project's own documents
describe it as a single guard.

**The code is correct** — the full word list run against all four modules returns no hits. What
is narrower than advertised is the *coverage*: two of the four are enforced, two happen to be
clean. It is left open deliberately, and the film says so on camera, because a check is more
convincing when you can watch it find something real.

Every previous entry in this series is linear: hook → framework → example → finding → CTA.
This is the first that is not.

## What fetching the primary source changed

The project began from this series' own case study, which renders the middle clause as
*"drafts a follow-up email."* The release says **"creates an email"**; the words *drafts* and
*follow-up* appear **zero times** on the page.

"Drafts" implies an incompleteness Morgan Stanley's verb does not carry — so the paraphrase was
*easier* to read correctly than the original. That is the opposite of what you would expect,
and it is the strongest evidence in the film. It was unavailable while reading a reading.

## This is not Morgan Stanley's system

The reference implementation is mine. It runs on fabricated mock data, connects to nothing of
Morgan Stanley's, and is not a disclosure of their architecture. Two pipelines, 12 modules, 29
tests across 10 files — all 29 run and pass, verified for this video.

The film observes only that Morgan Stanley does not publish mechanism, and states that this is
normal for a bank rather than a criticism. Their disclosure of the email/Salesforce distinction
is presented as a credit — **they published it clearly**, and the work of reading it precisely
was mine to do.

## Files here

**The six core files**, the same set every episode in this series carries:

| | |
|---|---|
| `README.md` | this file |
| `PEDAGOGY.md` | Gate P, signed before any audio was generated |
| `FACTCHECK.md` | 12 claims, every one verified mechanically against the primary source or the code |
| `QC-REPORT.md` | deliverable specs, loudness, resolution, gates — all `ffprobe`-verified |
| `beat_sheet.json` | the source of truth for the long cut |
| `beat_sheet-short.json` | the source of truth for the Short |

**The case study and the reference implementation live in the Mycroft repository**, where
this series keeps its build artifacts. Both are named in Source material below, and
`FACTCHECK.md` records the result of running the suite: **29 tests across 10 files, all
passing as run 2026-08-30**.

Also not included here: the build scripts, the Manim scenes, and the intermediate reviews.
Those stay in the working folder — this folder is the deliverable and its record, not the
workshop.

Captions (`.srt`/`.vtt`) and the YouTube description are produced at build time and kept with
the masters in the shared Drive, per this collection's convention.

## Source material

- **`10-morgan-stanley-agentic-ai-wealth-management.md`** — this series' case study, the
  reading the project started from. Filed in the **Mycroft repository**.
- **`morgan_stanley_reference/`** — the reference implementation. Two pipelines, 12 modules,
  10 test files, **29/29 passing as run 2026-08-30**, verified rather than taken from its
  README. Filed in the **Mycroft repository**.
- **Morgan Stanley, "Launch of AI @ Morgan Stanley Debrief," 26 June 2024** —
  `morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch`, fetched directly.

The third item is the **primary source**, and going to it directly is what produced the film's
strongest finding — see "What fetching the primary source changed" above.

## Built with

Brutalist toolkit — Kokoro `af_bella` for narration, Remotion for eleven beats, Manim for
four, `compile.py` at `--height 2160` / `3840`, `shorts.py` with an explicit drop plan.

**Nine components were authored for this film**, all in `brutalist.art/runtime/remotion/src/scenes/`:
`QuotePair`, `CheckCard`, `TitlePlate`, `FiguresPlate`, `BeforeAfter`, `TerminalPlate`,
`TensionPlate`, `RepoPlate`, plus portrait cuts of five of them (`*916`). The Manim scenes are
`scenes.py` (16:9) and `scenes_short.py` (9:16).

Every composition is registered with `defaultProps={schema.parse({})}`, which derives defaults
from the zod schema rather than an object literal — so there is nowhere to write a default that
asserts something about the work. That guard exists because a shared component's default once
put a model name the film never used into a compiled master.

## Four build guards in `build_beat_sheet.py`

The beat sheet is generated, never hand-edited, and the generator refuses to emit a sheet that
fails any of these:

| | |
|---|---|
| `PLACEHOLDER` | no lorem or TODO text can reach a render |
| `SCENE_PROPS` | a beat cannot pass a prop its scene does not declare |
| `SCENE_DEFAULTS` | Root's defaults cannot leak into a beat |
| `ASSERTIVE_DEFAULTS` | a prop whose default *makes a claim about the work* must be set explicitly |

Each guard was written the first time its class of problem came up, and each was tested against
that exact case before being relied on — so the check is proven rather than assumed.

## Status

Teaching **12/12** (ship bar 8), self-assessed — the defensible claim is that no criterion is
obviously unmet. Production gate **PASS** in both aspects, re-run on frames pulled from the
compiled masters. Gate P signed in `PEDAGOGY.md`. Both cuts watched end to end.

**Not published** — publication is a separate decision.
