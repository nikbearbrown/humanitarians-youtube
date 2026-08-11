# Tanmay Kulkarni

Weekly work reports for the **Agentic AI in Financial Services** case-study
series. Each episode pairs a primary-sourced case study with a working
reference implementation, and the video walks the build rather than
summarising the findings.

Each episode folder begins with `YYYY-MM-DD` and is dated to the **work week
being reported on**, not the day the video was rendered.

## Voice

**Kokoro `af_bella` ("Bella") is the voice for this series**, and is recorded in
every episode's `beat_sheet.json` under `metadata.voice_kokoro`.

**Documented re-voice, 2026-07-29.** The first episode (CommBank) was produced
in the Teardown register with `am_onyx`. From the Klarna episode onward the
series moved to the Pragmatist register with `af_bella`, because these reports
teach a method rather than dismantle a claim, and the warmer register suits a
walkthrough. Recording it here per `fellows/README.md`, which asks that a voice
change be an explicit, documented decision rather than a per-episode default.
`af_bella` is the standing choice; any future change gets logged the same way.

## Episodes

| Week reported | Folder | Subject |
|---|---|---|
| 2026-07-28 | [`2026-07-28 case-study-video`](./2026-07-28%20case-study-video/) | CommBank — untangling two conflated AI systems |
| 2026-07-29 | [`2026-07-29 AI Crossroads - Build or Buy Video - Klarna`](./2026-07-29%20AI%20Crossroads%20-%20Build%20or%20Buy%20Video%20-%20Klarna/) | Klarna — build-or-buy, read through the Productivity J-Curve |
| 2026-08-05 | [`2026-08-05-lemonade-claims-bot-mycroft`](./2026-08-05-lemonade-claims-bot-mycroft/) | Lemonade — building the claims workflow, and what production would demand |

## Two lanes

These reports come in two kinds, and they are deliberately not mixed:

- **Work-derived** — a film about the week's actual work (CommBank, Lemonade).
- **Repo-topic** — a film built from a topic suggestion in this repo, replacing
  an earlier fictional draft (Klarna).

They carry different registers and different act structures. Referencing a
previous episode for *format conventions* is fine; content, visuals and
structure are built fresh for each film.

## Standards

Every episode is built to two documents kept outside this repo:

- **`PLAYBOOK.md`** — production discipline: audio-first timing, one bounded
  render at a time, verify by looking at frames rather than probing the mp4,
  4K output confirmed by `ffprobe`, deliverables kept separate from the raw
  working folder.
- **`PROOF.md`** — the content standard: a six-criterion teaching rubric scored
  out of 12, plus a binary production gate (evidence legible at the moment of
  assertion, sources on screen rather than only voiced, comparisons held
  side-by-side). Public release requires ≥8/12 **and** a passing gate.

Each episode folder carries its own `QC-REPORT.md` logging every defect found
and fixed. From the Lemonade episode onward a `PROOF-REVIEW.md` records the
formal review, including any finding that sent the cut back before publishing.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured
audio becomes the clock, generated visual beats compile immediately, and
unavailable media remains as labeled slates until a human fills the pantry. The
human conducts, watches, fact-checks, refines, and decides whether anything is
published.

**Note on `compile.py`:** it is a hard-cut concat with no transition or pause
mechanism. The 1.0s hold before every cut used across this series is a separate
pass — see `pacing_pass.py` in the Lemonade episode folder — and must be re-run
after any recompile.
