# 2026-08-28 - Measuring a local AI model against the matcher

**Week covered:** 2026-08-24 - 2026-08-30

**Video:** [Mycroft_OmMali_28_08_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Private AI Valuation Agent works out a per-share price for private companies such as Anthropic, OpenAI, SpaceX and Databricks, using the quarterly reports that US mutual funds are required to file with the SEC: a fund must disclose what a holding is worth in dollars and how many shares it owns, and dividing one by the other gives a price for a company that has no share price.

Matching those names is the hardest part, so this week tested whether a
language model does it better than the simple rule-based matcher already in
place. **It does not, and the decision to reject it was committed to in advance
of running the test.**

- **An 8-billion-parameter model ran locally over 322 test cases** with no
  failures, given exactly the same information the rule-based matcher gets.
- **Accuracy got worse, not better: precision fell from 99.6% to 94.5%.** In
  practical terms, one wrongly included holding becomes 196.
- **Of 85 difficult cases it fixed 1 and broke 14**, and every failure is the
  same mistake: the matcher had correctly concluded "no match", and the model
  named a company anyway. In one case it matched an internal Fidelity reference
  code to X.AI; in another it invented a corporate relationship to justify its
  answer.
- **The model's own confidence score is useless for deciding what to check.**
  It reported maximum confidence on 315 of 322 answers, including most of the
  wrong ones.
- **Speed was measured as well** (about 3.2 seconds per answer), so that cost
  cannot be mistaken for the reason it was rejected. The reason is accuracy.
- **The existing matcher was kept.** The model's results are published in full
  so the comparison can be checked.

## Rules

- **`pantry/` is reference only.** Do not slot these directly as media and do not copy them into
  `images/` — the toolkit writes compile output there. Same convention as the week 3 folder.
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
