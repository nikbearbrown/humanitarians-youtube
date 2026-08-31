# Week 5 — Measuring a local LLM against the matcher

Five figures for the week 5 narration. The week's finding is a **negative result**: an 8B local
model, given the same evidence as the deterministic matcher, costs 5.1 points of precision and
was not adopted.

| File | Beat | What it shows |
|---|---|---|
| `pantry/w5-setup.png` | 0:14 | One real holding exactly as it reached the model — the four fields given, and the price and the answer both withheld |
| `pantry/w5-scoreboard.png` | 0:42 | 0.9959 → 0.9449 precision, and the same error counted in records: 1 → 196 |
| `pantry/w5-failures.png` | 1:00 | Three answers in the model's own words, including the invented parent company |
| `pantry/w5-confidence.png` | 1:32 | 322 dots, one per answer: 315 at confidence 1.000, with the 15 disagreements inside that block |
| `pantry/w5-veto.png` | 1:52 | Every row the veto policy would ever see. All four of them |

SVG sources sit beside each PNG. PNGs are 2917 × 1750.

## Rules

- **`pantry/` is reference only.** Do not slot these directly as media and do not copy them into
  `images/` — the toolkit writes compile output there. Same convention as the week 4 folder.
- Every number in every figure is generated from the measured artifacts at build time
  (`scripts/make_week5_figures.py` in the project repo, reading the cached model replies). No
  figure carries a hand-typed number. Re-running the script is the only way they change.
- Both QA passes were run: `npm run audit:layout` reports 0 errors on all five, and each PNG was
  read and checked for substance.

## Two corrections these figures forced

Worth knowing before the voiceover, because the prose said something different until today:

1. **Confidence was 1.000 on 315 of 322 answers, not 308.** Twelve of the fifteen answers that
   disagree with their label came back at 0.95 or above, not "nine of fourteen". The original
   numbers were hand-typed; the dot figure generates its counts from the cached replies and
   disagreed with the text, which is how the error surfaced. The narration script is corrected.

2. **The model was offered 11 candidate companies, not 7.** Seven are the universe; four are
   watchlist companies — which matters, because Scale AI and X.AI are both watchlist names and
   the model's worst answers promote holdings to exactly those.

## Colour

Six tokens from `brutalist/DESIGN.md`, nothing else. Red is the primary series, never "danger":
in the scoreboard it marks the deterministic matcher because that is the system that ships; in
the failure and confidence figures it marks the model's answers because those are the subject.
Ochre appears twice, as annotation only.

---

## The built reel

*(Appended by the brutalist.art build. Everything above is the original figure brief and is
unmodified.)*

Rebuilt as a 12-beat `ai-explainer` / `claude-hai` reel — **twelve beats, zero slates, $0.00**.
Free/local throughout: Kokoro TTS + Remotion + ffmpeg.

**Two masters, one edit.** 16:9 at 3840×2160 and 9:16 at 2160×3840, from the same components,
the same props and the same narration mp3s. The vertical cut is a re-layout, not a crop.

| Where | What |
|---|---|
| `measuring-a-local-llm-against-the-matcher.mp4` | 16:9 master, 3840×2160 |
| `vertical/measuring-a-local-llm-against-the-matcher-916.mp4` | 9:16 master, 2160×3840 |
| `*-slate.mp4` | review cuts with beat IDs and running timecode |
| `PEDAGOGY.md` | GATE P — what the author is asked to sign |
| `FACTCHECK.md` | 20 rows; read 3, 9, 13 and 18 |
| `CHECKS-REPORT.md` | PROOF GATE, written before the first compile |
| `BUILD-LOG.md` | decisions, toolkit defects found, what QC caught |
| `BUILD-PROMPT.md` | the paste-ready prompt that rebuilds both cuts |
| `build_beat_sheet.py` | the injection — every on-screen number, under assertions |

The five figures in `pantry/` were used as REFERENCE and rebuilt as native animated scenes
(REBUILD LAW). They were never slotted as media and never copied into `images/`.
